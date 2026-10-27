# Chatbot de simulação OSCE

> Documento de implementação: descreve a feature **já entregue**, não um plano. Reaproveita a mesma infraestrutura de IA do chat de ajuda (`/ia/perguntar`): Gemini chamada pelo BFF, sem serviço de IA dedicado (ver [DA-07](decisoes.md)).

## 1. O que é e por que existe

OSCE (*Objective Structured Clinical Examination*) é o formato de avaliação clínica usado em cursos de medicina: o estudante entra numa "estação" com um paciente (real, ator ou simulado) e precisa colher a história clínica (anamnese) e levantar hipóteses diagnósticas, sem o paciente simplesmente dizer qual é a doença.

A feature replica isso dentro do AnatoQuizUp: o aluno escolhe um **caso clínico**, conversa em texto no papel de médico, e a IA interpreta o paciente — respondendo só o que for perguntado, nunca entregando o diagnóstico. Ao final, o aluno pede uma **avaliação**, e a mesma IA troca de papel para "examinador", julgando a conversa contra a **rubrica** do caso — e o BFF transforma esse julgamento em pontuação (seção 5). Como num OSCE real, saem duas medidas: o checklist ponderado e uma nota global independente.

## 2. Arquitetura

```mermaid
flowchart LR
    aluno(["Aluno<br/>papel STUDENT"])
    web["Web<br/>/aluno/osce<br/>(público)"]
    bff["BFF<br/>/api/v1/ia/osce/*<br/>(público)"]
    gemini[("Gemini API<br/>(externa)")]

    aluno --> web
    web -->|"HTTPS REST<br/>Bearer JWT"| bff
    bff -->|"1. instrução 'modo paciente'<br/>perfil + roteiro oculto"| gemini
    bff -->|"2. instrução 'modo examinador'<br/>rubrica + âncoras"| gemini
    gemini -.->|"fala em personagem /<br/>julgamento em JSON"| bff
    bff -.->|"conversa / rubrica pontuada"| web
```

As duas chamadas usam o **mesmo** `geminiClient` e a mesma `GEMINI_API_KEY` do chat de ajuda; o que muda entre elas é só a instrução de sistema (seção 4). A chave fica no BFF e nunca chega ao Web.

Não existe um "Serviço de IA" separado nem RAG/Qdrant aqui — o BFF é a camada de IA do projeto ([DA-07](decisoes.md)). Diferente do chat de ajuda, o conteúdo de cada caso é pequeno e fixo (ver seção 3), então ele cabe inteiro no prompt da Gemini. Reavaliar RAG só se a biblioteca de casos crescer muito.

### Componentes tocados

| Repositório | Arquivo | Papel |
|---|---|---|
| BFF | `src/shared/constants/cenarios-osce.ts` | Os casos clínicos (parametrização, seção 3) |
| BFF | `src/routes/osce.routes.ts` | As 3 rotas HTTP (seção 4) |
| BFF | `src/shared/utils/pontuacao-osce.ts` | Pesos, soma, percentual, teto do item crítico e divergência checklist×nota global (seção 5) |
| BFF | `src/routes/index.ts` | Monta `/ia/osce` **antes** de `/ia` (o catch-all de `ia.routes.ts` intercepta qualquer sub-rota não mapeada de `/ia/*`) |
| Web | `src/features/osce/osceService.ts` | Chamadas HTTP às 3 rotas |
| Web | `src/pages/aluno/osce/OscePage.tsx` | Tela: lista de casos → chat → rubrica |
| Web | `src/pages/aluno/osce/RubricaResultado.tsx` | Painel do resultado: as duas medidas, domínios e item a item |
| Web | `src/app/router.tsx` | Rota `/aluno/osce`, protegida para `STUDENT` |
| Web | `src/widgets/header/ui/Header.tsx` | Item de menu "Simulação OSCE" (ícone `Stethoscope`) |

## 3. Parametrização: o que é um "cenário"

Cada caso clínico é um objeto `CenarioOsce` (`src/shared/constants/cenarios-osce.ts` no BFF):

| Campo | Visível para o aluno? | Uso |
|---|---|---|
| `id` | Sim | Identifica o caso nas rotas (`/api/v1/ia/osce/:id/...`) |
| `titulo` | Sim | Nome exibido na lista de casos |
| `especialidade` | Sim | Rótulo exibido (ex.: "Cardiologia") |
| `dificuldade` | Sim | `"Fácil" \| "Médio" \| "Difícil"`, exibido como selo colorido |
| `perfilPaciente` | **Não** | Idade, profissão, jeito de falar — molda o tom das respostas da IA |
| `queixaPrincipal` | **Não** | O que o paciente diz se perguntado "o que você está sentindo?" |
| `roteiroOculto` | **Não** | História completa, fatores de risco, achados de exame físico — a IA só revela o que for perguntado |
| `diagnosticoEsperado` | **Não** | Nunca é dito ao aluno; só aparece no feedback final |
| `rubrica` | **Não** (só após finalizar) | Checklist pontuado: itens, domínios, pesos, âncoras de crédito e itens críticos (ver seção 5) |

A rota `GET /api/v1/ia/osce/cenarios` devolve **só** os 4 primeiros campos — o resto nunca sai do BFF antes da hora, para não vazar a resposta do caso.

Hoje há 3 casos fixos (dor torácica/cardiologia, cefaleia súbita/neurologia, dor abdominal/apendicite) no próprio código. **Não há tela de autoria de caso para professor** — decisão deliberada (YAGNI): construir CRUD de casos sem uma demanda real validada seria antecipar um requisito que ninguém pediu ainda. Para adicionar um caso novo hoje, basta um objeto novo no array `CENARIOS_OSCE`, seguindo os 3 exemplos existentes como modelo.

## 4. Como funciona (fluxo e contratos)

Pré-requisito: o mesmo `GEMINI_API_KEY`/`GEMINI_MODEL` do chat de ajuda (`src/config/env.ts` do BFF). Sem a chave configurada, todas as rotas abaixo respondem `503 IA_INDISPONIVEL`, igual ao `/ia/perguntar`.

Todas as três rotas ficam atrás do `middlewareAutenticacao` (JWT validado na borda, como manda o [DA-03](decisoes.md)) e a tela `/aluno/osce` é protegida para o papel `STUDENT` no `router.tsx` do Web. Nenhum segredo do provedor entra na resposta: o Web nunca fala com a Gemini, só com o BFF.

### 4.1. `GET /api/v1/ia/osce/cenarios`

Lista os casos disponíveis (campos públicos da tabela acima). Sem corpo de requisição.

```json
{ "cenarios": [{ "id": "dor-toracica", "titulo": "...", "especialidade": "Cardiologia", "dificuldade": "Médio" }] }
```

### 4.2. `POST /api/v1/ia/osce/:id/mensagem` — uma fala do aluno

```json
{
  "mensagem": "Desde quando você sente essa dor?",
  "historico": [{ "autor": "aluno" | "paciente", "texto": "..." }]
}
```

O BFF monta a chamada à Gemini com:
- **Instrução de sistema** = perfil + queixa + roteiro oculto do caso, mais a regra "nunca saia do personagem, nunca diga o nome do diagnóstico".
- **`contents`** = o `historico` recebido, convertido em turnos `user` (aluno) / `model` (paciente), mais a nova `mensagem` como último turno.

O **histórico vive no front** (estado React da página), não no BFF — cada chamada reenvia a conversa inteira, do mesmo jeito que o `ChatAjudaModal` já faz para as perguntas livres. Isso mantém o BFF sem estado de sessão a gerenciar.

Resposta: `{ "resposta": "<fala do paciente, em personagem>" }`.

### 4.3. `POST /api/v1/ia/osce/:id/finalizar` — fim da simulação

```json
{ "historico": [{ "autor": "aluno" | "paciente", "texto": "..." }] }
```

Troca a instrução de sistema para o modo "examinador": a IA sai do personagem de paciente, recebe o `diagnosticoEsperado` e a `rubrica` do caso (cada item com suas **âncoras de crédito**) e produz **duas medidas independentes**, nesta ordem:

1. **Checklist** — classifica cada item em `competente` / `parcial` / `nao_realizado`, com justificativa citando a fala do aluno.
2. **Nota global (GRS)** — julga o desempenho como um todo, de 0 a 4, *sem* somar o checklist.

A resposta é forçada a JSON pelo `responseSchema` nativo da Gemini e validada com Zod no BFF — JSON inválido vira `502`, nunca uma nota silenciosamente errada.

**A IA não calcula nota.** Pesos, soma, percentual, teto do item crítico e a verificação de concordância entre as duas medidas são aplicados em código (`pontuacao-osce.ts`), porque modelo de linguagem não é confiável para aritmética e porque a regra de aprovação precisa ser auditável.

Resposta (abreviada):

```json
{
  "avaliacao": {
    "cenarioId": "dor-toracica",
    "titulo": "Dor torácica no pronto-socorro",
    "diagnosticoEsperado": "Síndrome coronariana aguda (angina/infarto)",
    "comentarioFinal": "Faltou investigar...",
    "itens": [
      {
        "id": "caracteriza-dor",
        "dominio": "Identificação do problema",
        "descricao": "Caracteriza a dor: localização, tipo e intensidade",
        "ancoras": {
          "competente": "Obtém localização E qualidade da dor (aperto, queimação, pontada) — as duas informações.",
          "parcial": "Pergunta só onde dói, ou só como é a dor, sem completar a caracterização."
        },
        "peso": 2,
        "permiteParcial": true,
        "critico": true,
        "nivel": "parcial",
        "justificativa": "Perguntou \"onde dói?\", mas não explorou o tipo da dor.",
        "pontos": 1,
        "pontosMaximos": 2
      }
    ],
    "pontuacao": 12.5,
    "pontuacaoMaxima": 17,
    "percentual": 74,
    "nivelChecklist": "limitrofe",
    "rotuloChecklist": "Limítrofe",
    "notaGlobal": 1,
    "rotuloNotaGlobal": "Limítrofe",
    "ancoraNotaGlobal": "Hesitante ou incompleto em pontos importantes; precisaria de supervisão direta o tempo todo.",
    "justificativaNotaGlobal": "Colheu os dados principais, mas sem fio condutor.",
    "aprovado": false,
    "itensCriticosNaoCumpridos": ["Caracteriza a dor: localização, tipo e intensidade"],
    "divergente": false
  }
}
```

## 5. A rubrica: âncoras de aceitação e pontuação

Esta seção explica **por que** a rubrica tem a forma que tem. Cada decisão aponta para a referência que a sustenta (numeração da seção 6).

O ponto de partida é o *Rating Checklist* do capítulo 14 de Amin, Chong & Khoo **[R1]**, mas o desenho foi alinhado ao que a literatura de avaliação em OSCE trata como padrão ouro, em especial as práticas da escola de Leeds **[R2] [R3] [R4]** — o grupo que escreveu os guias AMEE sobre qualidade e organização de OSCE.

### 5.1. Duas medidas independentes por estação

Esta é a decisão estrutural: um OSCE de boa qualidade **não** colhe uma medida só. Cada estação produz um **checklist ponderado** (o que foi feito) e uma **nota global** (quão competente foi), julgados separadamente **[R2] [R3]**.

As duas não são redundantes. A evidência mostra que a nota global é mais sensível a nível de treinamento e captura melhor as habilidades "moles" que o checklist fragmenta **[R5] [R6]**; o checklist, por sua vez, dá o detalhe acionável do feedback. A concordância entre elas é fraca justamente nas estações de **anamnese** — que é o nosso caso **[R6]**.

Na versão anterior desta feature a "nota global" era calculada *a partir* do percentual do checklist. Isso era um erro: uma medida derivada da outra não é uma segunda medida, e a concordância entre elas deixa de ser informação. Agora a IA atribui a nota global sem ver a soma, e a divergência entre as duas vira um sinal (seção 5.5).

### 5.2. Âncoras comportamentais por nível de crédito

| Campo de `ItemRubrica` | O que é |
|---|---|
| `id` | Identificador estável; é o que a IA devolve ao classificar |
| `dominio` | `Comunicação e rapport`, `Identificação do problema`, `Raciocínio clínico`, `Encerramento` — agrupamento do livro **[R1]** |
| `descricao` | O que se espera do aluno, na voz do examinador |
| `ancoras.competente` | **Âncora de crédito cheio**: o comportamento concreto que vale o peso inteiro |
| `ancoras.parcial` | **Âncora de crédito parcial**: o que vale metade. Ausente = item de duas âncoras, sem meio-termo |
| `peso` | `1` ou `2` pontos; itens centrais da estação valem 2 |
| `critico` | Item *killer*: falhar nele limita o resultado (seção 5.4) |

A mudança importante aqui foi trocar um único `aceitacao` (só definia "competente") por **âncoras por nível**. Em Leeds, o examinador recebe material de apoio no nível do item dizendo o que vale crédito cheio e o que vale crédito parcial — o exemplo citado é aferir pressão arterial: *"±5% para crédito cheio, ±10% para crédito parcial, 0 caso contrário"* **[R4]**. Sem isso, a fronteira entre "competente" e "parcial" fica no gosto do examinador; com um examinador-LLM, fica no gosto do modelo naquela amostragem.

Itens compostos usam três âncoras; itens simples usam duas — também é a prática de Leeds: *"'super-items' ... scored by three point anchors. A third group of simpler items are scored with two-point anchors"* **[R4]**. O `permiteParcial` deixou de ser um campo próprio e passou a ser derivado da existência da âncora `parcial`, para não haver duas fontes de verdade.

### 5.3. Pontuação e pesos

As três colunas do livro (*Performed competently* / *Performed but NOT fully competent* / *Not performed or incompetent*) **[R1]**:

| Nível | Pontos |
|---|---|
| `competente` | peso cheio (1 ou 2) |
| `parcial` | metade do peso — **ou 0**, se o item não tem âncora parcial |
| `nao_realizado` | 0 |

Item que a IA deixou de julgar conta como `nao_realizado`: resposta incompleta do modelo nunca infla a nota do aluno.

**Por que não um esquema de pesos mais sofisticado?** Porque a evidência não justifica. Homer et al. compararam o esquema ponderado real do exame com uma versão "simples" e a mudança afetou a decisão de ~3% dos candidatos no geral (~30% dos limítrofes), com métricas de qualidade "um pouco melhores" sob ponderação **[R4]**. Ponderar por julgamento de especialista é adequado **[R7]**; inventar um modelo complexo não compra nada. O que *compra* reliability é ter itens clinicamente discriminantes **[R8]** — por isso o esforço foi nas âncoras, não nos pesos.

O percentual do checklist cai numa faixa, alinhada ponto a ponto com a escala global para que as duas sejam comparáveis:

| Percentual | Faixa do checklist | Equivale a (GRS) |
|---|---|---|
| ≥ 90% | Excelente | 4 |
| 75–89% | Bom | 3 |
| 60–74% | Suficiente | 2 |
| 50–59% | Limítrofe | 1 |
| < 50% | Insuficiente | 0 |

### 5.4. A escala global (GRS) e o item crítico

A escala de 5 pontos é a de Leeds **[R2]**: *"0 = clear fail, 1 = borderline, 2 = clear pass, 3 = very good pass, 4 = excellent pass"*.

As âncoras, porém, foram reescritas em termos de **confiança/supervisão** ("eu deixaria este aluno conduzir sozinho?") em vez de adjetivos abstratos. Escalas alinhadas ao construto que o avaliador realmente usa — entrustment — são mais confiáveis do que escalas de "ruim/bom/ótimo" **[R9] [R10]**.

O **item crítico** vem da estação de exemplo do capítulo 14 **[R1]**: *"The candidate will not score better than 'borderline fail' in overall performance if he/she is unable to teach the right technique."* É o mesmo mecanismo do *red flag* / erro crítico usado em OSCEs regulatórios, onde um ato inseguro reprova a estação independentemente do resto **[R11]**.

Implementação: se qualquer item `critico` não for `competente`, a faixa do checklist é **rebaixada ao teto `Limítrofe`** e `aprovado` vira `false`. O teto nunca eleva uma nota já pior que ele. Cada cenário tem ao menos um item crítico (garantido por teste) — hoje sempre dois: **caracterizar o achado que define o caso** e **chegar à hipótese diagnóstica**. O aluno pode ser simpático e organizado e ainda assim não passar se não fizer o diagnóstico.

### 5.5. Qual das duas medidas decide a aprovação — e por quê

`aprovado = percentual do checklist ≥ 60% E nenhum item crítico falhado`. **A nota global não decide**; ela é reportada e usada como verificação.

Isso **inverte** o que a literatura recomenda para examinador humano, e é deliberado. Com humanos, a nota global é a medida mais confiável e o checklist penaliza o candidato experiente que é direto e eficiente **[R5] [R6]**. Com um juiz-LLM a assimetria é outra: o checklist é auditável item a item, com a evidência citada, enquanto a nota global é uma impressão sem rastro — e justamente em *history taking* a concordância entre LLM e examinador humano é fraca (ICC = 0,36 num estudo recente) **[R12]**.

A nota global entra, então, como **teste de concordância**: se a faixa do checklist e a nota global se afastam 2 ou mais pontos na escala de 5, o resultado é marcado como `divergente` e a interface diz ao aluno para levar o caso ao professor em vez de tomar o número como veredito. É o análogo, para um candidato só, do **R²** que o AMEE 49 usa para auditar uma estação: lá, R² < 0,5 entre checklist e nota global é sinal de revisar o desenho da estação **[R2]**.

### 5.6. O que NÃO é padrão ouro aqui (limitações)

- **O corte de 60% não vem de *standard setting*.** O padrão ouro para definir a nota de corte de uma estação é o **borderline regression method (BRM)**: regride-se a nota do checklist de *toda a coorte* sobre a nota global e lê-se na reta o ponto correspondente a "limítrofe" **[R13] [R2]**. BRM precisa de coorte; aqui n = 1 por simulação e não há persistência. Pior: com menos de ~50 candidatos o erro padrão explode e o R² fica instável **[R14]**. Portanto **o corte é criterial e provisório**. Caminho de evolução concreto: persistir as simulações → acumular ≥50 tentativas por cenário → calcular o cut-score por BRM e substituir o 60% fixo. Os dois dados que o BRM precisa (checklist e nota global por tentativa) já estão sendo produzidos.
- **Uma estação não é um OSCE.** São necessárias **14–18 estações** para uma medida confiável de desempenho **[R1] [R3]** — a confiabilidade depende mais do número de estações do que da duração de cada uma **[R1]**. O resultado de um caso isolado é **formativo**: serve para treinar e receber feedback, não como nota da disciplina.
- **O juiz é um LLM, não um examinador treinado.** A pontuação é determinística e auditável; a *classificação* não é. Dois `finalizar` sobre a mesma conversa podem divergir nos itens de julgamento mais sutil. Daí a justificativa obrigatória por item e a marca de divergência.
- **Sem métricas de qualidade da estação.** AMEE 49 **[R2]** audita estações com alpha de Cronbach (≥ 0,7), R² checklist×GRS (> 0,5 bom), discriminação intergrau, número de reprovações e variância entre grupos. Nada disso é calculável sem persistir resultados. Fica como o próximo passo natural depois da persistência.
- **Rubricas não validadas por especialista.** As âncoras foram escritas a partir da literatura e do roteiro clínico de cada caso, **não** revisadas por um médico ou professor da área. Antes de qualquer uso com turma real, isso precisa acontecer.

## 6. Referências

Numeração usada ao longo da seção 5.

**Base do modelo da rubrica**

- **[R1]** Amin, Z.; Chong, Y.S.; Khoo, H.E. *Practical Guide to Medical Student Assessment*. World Scientific, 2006. **Capítulo 14 — "Objective Structured Clinical Examination (OSCE)", p. 58-64.** Rating Checklist (p. 63), estação de exemplo com a regra de *borderline fail* (p. 60), recomendação de 14–18 estações e de escala global + treinamento de examinadores (p. 59, 64). ISBN 981-256-808-5.
- **[R2]** Pell, G.; Fuller, R.; Homer, M.; Roberts, T. **How to measure the quality of the OSCE: A review of metrics — AMEE Guide no. 49.** *Medical Teacher*, 32(10):802-811, 2010. Escala global de 5 pontos, R² checklist×GRS, alpha, discriminação intergrau, variância entre grupos. <https://doi.org/10.3109/0142159X.2010.507716>
- **[R3]** Khan, K.Z.; Gaunt, K.; Ramachandran, S.; Pushkar, P. **The Objective Structured Clinical Examination (OSCE): AMEE Guide No. 81. Part II: Organisation & Administration.** *Medical Teacher*, 35(9):e1447-e1463, 2013. Desenho de estação, escolha de rubrica de pontuação, treinamento de examinadores, garantia de qualidade. <https://doi.org/10.3109/0142159X.2013.818635>
- **[R4]** Homer, M.; Fuller, R.; Hallam, J.; Pell, G. **Shining a spotlight on scoring in the OSCE: Checklists and item weighting.** *Medical Teacher*, 42(9):1037-1042, 2020. Âncoras de dois e três pontos, material de apoio por item (o exemplo do ±5%/±10%), impacto real da ponderação (~3% dos candidatos, ~30% dos limítrofes). <https://doi.org/10.1080/0142159X.2020.1781072>

**Checklist versus nota global**

- **[R5]** Ilgen, J.S.; Ma, I.W.Y.; Hatala, R.; Cook, D.A. **A systematic review of validity evidence for checklists versus global rating scales in simulation-based assessment.** *Medical Education*, 49(2):161-173, 2015. Revisão sistemática: escalas globais têm confiabilidade igual ou superior e são mais sensíveis a nível de expertise. <https://doi.org/10.1111/medu.12621>
  (A afirmação equivalente aparece em [R1] p. 59, creditada a Norman, 2003, e em [R3].)
- **[R6]** Daniels, V.J. et al. **A Comparison of Checklist and Domain-Based Ratings in the Assessment of OSCE Performance.** *Cureus*, 2023. Correlação entre as duas medidas varia por estação: **fraca em estações de anamnese**, forte em estações de conduta. <https://pubmed.ncbi.nlm.nih.gov/37435263/>
- **[R7]** Kahraman, N. et al., sobre esquemas de ponderação em OSCE: julgamento de especialista para pesos de item é adequado e se relaciona melhor com critérios externos do que ponderação unitária. *Citado em [R4]* — não consultado no original.
- **[R8]** Daniels, V.J.; Bordage, G. et al. **Effect of clinically discriminating, evidence-based checklist items on the reliability of scores from an Internal Medicine residency OSCE.** *Advances in Health Sciences Education*, 2014. Itens clinicamente discriminantes aumentam a confiabilidade e reduzem o número de estações necessárias. <https://doi.org/10.1007/s10459-013-9482-4>

**Âncoras alinhadas ao construto**

- **[R9]** Crossley, J. et al. **Good questions, good answers: construct alignment improves the performance of workplace-based assessment scales.** *Medical Education*, 2011. Escalas com âncoras narrativas alinhadas ao construto são mais confiáveis.
- **[R10]** Rekman, J. et al. **Entrustability Scales: Outlining Their Usefulness for Competency-Based Clinical Assessment.** *Academic Medicine*, 91(2):186-190, 2016. Escalas de *entrustment* refletem o julgamento que o avaliador já faz na prática, aumentando a confiabilidade.
- **[R11]** Prática regulatória de *red flag* / erro crítico em OSCE (ex.: o OSCE do Nursing and Midwifery Council, Reino Unido): um ato inseguro reprova a estação independentemente do desempenho no restante. Documentação regulatória, não artigo revisado por pares — usado aqui apenas como reforço do mecanismo já descrito em [R1] p. 60.

**Juiz automatizado**

- **[R12]** **The Validity of Generative Artificial Intelligence in Evaluating Medical Students in Objective Structured Clinical Examination.** *JMIR Formative Research*, 2025. Concordância IA×examinador humano **fraca em anamnese (ICC = 0,36; IC 95% −0,32 a 0,78)**; a IA tendeu a dar notas mais altas que os médicos. <https://formative.jmir.org/2025/1/e79465>

**Standard setting**

- **[R13]** McKinley, D.W.; Norcini, J.J. **How to set standards on performance-based examinations: AMEE Guide No. 85.** *Medical Teacher*, 2014. Borderline regression method como método de referência para derivar a nota de corte de estações. <https://doi.org/10.3109/0142159X.2014.890600>
- **[R14]** Homer, M.; Setna, Z.; Jones, A. et al. **Setting defensible standards in small cohort OSCEs: Understanding better when borderline regression can "work".** *Medical Teacher*, 2020. Coortes abaixo de ~50 candidatos têm erro padrão alto e R² instável. <https://pubmed.ncbi.nlm.nih.gov/31657266/>

## 7. Decisões e limites conhecidos

- **Sem persistência**: a conversa e a rubrica pontuada não são salvas em banco — fecham a página, perde a simulação. Se a equipe quiser histórico de simulações (para o professor acompanhar progresso, por exemplo), isso é extensão futura, não construída aqui.
- **Sem streaming**: a resposta da Gemini chega de uma vez (igual ao `/ia/perguntar`), não token a token. O *thinking* da Gemini é desligado (`thinkingConfig.thinkingBudget: 0`) nas duas rotas: com ele a chamada levava 10–15s e às vezes estourava o `REQUEST_TIMEOUT_MS`. A UI mostra um spinner de carregamento enquanto espera.
- **Dado do aluno que cruza para a Gemini**: nenhum — diferente do `/ia/dica`, o modo OSCE não usa o desempenho do aluno, só o texto da conversa em si (que o próprio aluno está digitando). Sem risco de LGPD adicional em relação ao que o chat de ajuda já levanta.
- **Falha graciosa**: se a Gemini não estiver configurada ou falhar, a rota responde 503/502 com uma mensagem de erro — a página mostra o erro, sem quebrar a navegação.

## 8. Testes

A regra de pontuação é a parte auditável da feature, então é a parte testada: `tests/unit/pontuacao-osce.test.ts` (BFF, Jest) cobre os pesos e o crédito parcial, o item não julgado pela IA tratado como `nao_realizado`, o teto do item crítico, a nota global fora da escala e a marca de divergência — além da integridade das três rubricas (ids únicos, ao menos um item crítico, âncoras coerentes). São 13 casos.

**Gap conhecido**: `src/routes/osce.routes.ts` ainda **não** tem teste de rota (as outras rotas do BFF têm, em `tests/unit/*.routes.test.ts`, com o cliente externo mockado). Enquanto isso não existir, a feature consome a folga do `coverageThreshold` de 85% exigido pelo [DA-08](decisoes.md) — é o próximo item de qualidade desta feature.

## Documentos relacionados

- [Visão Geral da Arquitetura](visao-geral.md)
- [Decisões Arquiteturais](decisoes.md)
- [Endpoints](endpoints.md)

## Histórico de Versão

| Data | Versão | Descrição | Autor(es) |
| :--- | :--- | :--- | :--- |
| 26/10/2026 | 1.0 | Documentação da simulação OSCE: arquitetura, contratos, rubrica pontuada e limitações | [João Paulo](https://github.com/jpaulohe4rt), [Rafael Melo](https://github.com/rmatuda) |
