# Chatbot de simulação OSCE

> Documento de implementação: descreve a feature entregue (não é um plano de estudo, como `chatbot-ajuda-ia.md` — essa já foi construída). Reaproveita a mesma infraestrutura de IA do chat de ajuda (Gemini via BFF).

## 1. O que é e por que existe

OSCE (*Objective Structured Clinical Examination*) é o formato de avaliação clínica usado em cursos de medicina: o estudante entra numa "estação" com um paciente (real, ator ou simulado) e precisa colher a história clínica (anamnese) e levantar hipóteses diagnósticas, sem o paciente simplesmente dizer qual é a doença.

A feature replica isso dentro do AnatoQuizUp: o aluno escolhe um **caso clínico**, conversa em texto no papel de médico, e a IA interpreta o paciente — respondendo só o que for perguntado, nunca entregando o diagnóstico. Ao final, o aluno pede uma **avaliação**, e a mesma IA troca de papel para "examinador", julgando a conversa contra um checklist do caso.

## 2. Arquitetura

```
Aluno (Web) → /aluno/osce (nova aba do menu, só para o papel STUDENT)
   ↓
BFF (/ia/osce/*, roteador próprio, mesmo padrão de /ia/perguntar)
   ↓ proxy autenticado para a Gemini API (geminiClient já existente)
Gemini API — chamada 2x com instruções de sistema diferentes:
   1. "Modo paciente": interpreta o perfil clínico do caso
   2. "Modo examinador": avalia o histórico contra o checklist do caso
   ↓
Resposta volta pelo BFF → Web renderiza a conversa / o feedback
```

Não existe um "Serviço de IA" separado nem RAG/Qdrant aqui — diferente do chat de ajuda, o conteúdo de cada caso é pequeno e fixo (ver seção 3), então ele cabe inteiro no prompt da Gemini. Reavaliar RAG só se a biblioteca de casos crescer muito.

### Componentes tocados

| Repositório | Arquivo | Papel |
|---|---|---|
| BFF | `src/shared/constants/cenarios-osce.ts` | Os casos clínicos (parametrização, seção 3) |
| BFF | `src/routes/osce.routes.ts` | As 3 rotas HTTP (seção 4) |
| BFF | `src/routes/index.ts` | Monta `/ia/osce` **antes** de `/ia` (o catch-all de `ia.routes.ts` intercepta qualquer sub-rota não mapeada de `/ia/*`) |
| Web | `src/features/osce/osceService.ts` | Chamadas HTTP às 3 rotas |
| Web | `src/pages/aluno/osce/OscePage.tsx` | Tela: lista de casos → chat → feedback |
| Web | `src/app/router.tsx` | Rota `/aluno/osce`, protegida para `STUDENT` |
| Web | `src/widgets/header/ui/Header.tsx` | Item de menu "Simulação OSCE" (ícone `Stethoscope`) |

## 3. Parametrização: o que é um "cenário"

Cada caso clínico é um objeto `CenarioOsce` (`src/shared/constants/cenarios-osce.ts` no BFF):

| Campo | Visível para o aluno? | Uso |
|---|---|---|
| `id` | Sim | Identifica o caso nas rotas (`/ia/osce/:id/...`) |
| `titulo` | Sim | Nome exibido na lista de casos |
| `especialidade` | Sim | Rótulo exibido (ex.: "Cardiologia") |
| `dificuldade` | Sim | `"Fácil" \| "Médio" \| "Difícil"`, exibido como selo colorido |
| `perfilPaciente` | **Não** | Idade, profissão, jeito de falar — molda o tom das respostas da IA |
| `queixaPrincipal` | **Não** | O que o paciente diz se perguntado "o que você está sentindo?" |
| `roteiroOculto` | **Não** | História completa, fatores de risco, achados de exame físico — a IA só revela o que for perguntado |
| `diagnosticoEsperado` | **Não** | Nunca é dito ao aluno; só aparece no feedback final |
| `criteriosAvaliacao` | **Não** (só no feedback) | Checklist usado para montar o feedback (ver seção 4.3) |

A rota `GET /ia/osce/cenarios` devolve **só** os 4 primeiros campos — o resto nunca sai do BFF antes da hora, para não vazar a resposta do caso.

Hoje há 3 casos fixos (dor torácica/cardiologia, cefaleia súbita/neurologia, dor abdominal/apendicite) no próprio código. **Não há tela de autoria de caso para professor** — decisão deliberada (YAGNI): construir CRUD de casos sem uma demanda real validada seria antecipar um requisito que ninguém pediu ainda. Para adicionar um caso novo hoje, basta um objeto novo no array `CENARIOS_OSCE`, seguindo os 3 exemplos existentes como modelo.

## 4. Como funciona (fluxo e contratos)

Pré-requisito: o mesmo `GEMINI_API_KEY`/`GEMINI_MODEL` do chat de ajuda (`src/config/env.ts` do BFF). Sem a chave configurada, todas as rotas abaixo respondem `503 IA_INDISPONIVEL`, igual ao `/ia/perguntar`.

### 4.1. `GET /ia/osce/cenarios`

Lista os casos disponíveis (campos públicos da tabela acima). Sem corpo de requisição.

```json
{ "cenarios": [{ "id": "dor-toracica", "titulo": "...", "especialidade": "Cardiologia", "dificuldade": "Médio" }] }
```

### 4.2. `POST /ia/osce/:id/mensagem` — uma fala do aluno

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

### 4.3. `POST /ia/osce/:id/finalizar` — fim da simulação

```json
{ "historico": [{ "autor": "aluno" | "paciente", "texto": "..." }] }
```

Troca a instrução de sistema para o modo "examinador": a IA sai do personagem de paciente, recebe o `diagnosticoEsperado` e o `criteriosAvaliacao` do caso, e devolve um parecer item a item do checklist mais uma orientação curta do que faltou perguntar.

Resposta: `{ "feedback": "<texto do examinador>" }`.

## 5. Decisões e limites conhecidos

- **Sem persistência**: a conversa e o feedback não são salvos em banco — fecham a página, perde a simulação. Se a equipe quiser histórico de simulações (para o professor acompanhar progresso, por exemplo), isso é extensão futura, não construída aqui.
- **Sem streaming**: a resposta da Gemini chega de uma vez (igual ao `/ia/perguntar`), não token a token. A UI mostra um spinner de carregamento enquanto espera.
- **Dado do aluno que cruza para a Gemini**: nenhum — diferente do `/ia/dica`, o modo OSCE não usa o desempenho do aluno, só o texto da conversa em si (que o próprio aluno está digitando). Sem risco de LGPD adicional em relação ao que o chat de ajuda já levanta.
- **Falha graciosa**: se a Gemini não estiver configurada ou falhar, a rota responde 503/502 com uma mensagem de erro — a página mostra o erro, sem quebrar a navegação.
