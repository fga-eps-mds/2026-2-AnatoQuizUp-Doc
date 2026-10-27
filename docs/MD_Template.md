# Registro individual de decisões e uso crítico de IA — R2

| Campo | Valor |
| --- | --- |
| Estudante | Letícia Torres Soares Martins |
| Matrícula | Preencher somente na cópia individual submetida no Aprender 3 |
| Time | AnatoQuizUp |
| Release | R2 |
| Período registrado | 06/10/2026 a 26/10/2026 |
| Data da consolidação | 26/10/2026 |

Este arquivo acumula cinco ciclos individuais de uso de IA durante a R2. Em cada ciclo, a IA foi usada para investigar, rascunhar ou revisar; as decisões foram conferidas em código, métricas, reuniões e registros do projeto antes de serem aceitas. O registro segue o critério da disciplina de explicitar o que foi aceito, corrigido ou rejeitado e manter rastreabilidade verificável.

## Ciclo 1 — Diagnóstico do ambiente e da documentação

**Data:** 06/10/2026  
**Objetivo:** identificar divergências entre a arquitetura documentada, a configuração de homologação e o comportamento dos serviços.

**Interação com IA.** Solicitei uma análise do repositório e dos documentos de arquitetura e homologação para localizar lacunas, dependências e riscos da R2. A IA ajudou a organizar um checklist de rotas, variáveis de ambiente, serviços e fluxos que precisavam ser conferidos.

**Revisão humana e decisão.** Aceitei a estrutura do checklist. Corrigi inferências que confundiam o domínio público do BFF com um serviço MinIO e rejeitei qualquer conclusão sobre funcionamento baseada apenas no nome do domínio. Mantive como regra que uma funcionalidade só seria declarada pronta depois de confrontar documentação, código e teste no ambiente.

**Evidências:** [ata de alinhamento técnico de 06/10](reunioes/reuniao-06-10-26.md) · [ambiente de homologação](operacao/ambiente-homologacao.md) · [issue #41](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/41)

### Aprendizados intermediários

- Nomes de serviços e URLs são pistas, não evidências de arquitetura implantada.
- A análise assistida por IA precisa terminar em uma verificação observável: código, configuração documentada ou teste reproduzível.
- Limitações conhecidas devem ser registradas para impedir que uma demonstração seja tratada como validação completa.

## Ciclo 2 — Replanejamento do escopo da R2

**Data:** 12/10/2026  
**Objetivo:** alinhar backlog, roadmap, EAP e Lean Inception ao MVP ampliado e às entregas possíveis no período.

**Interação com IA.** Pedi apoio para comparar os artefatos de planejamento, encontrar conflitos de datas e escopo e transformar as diferenças em itens rastreáveis. A IA sugeriu reorganizar o MVP em ciclos e explicitar dependências entre histórias.

**Revisão humana e decisão.** Aceitei a comparação entre artefatos e a explicitação de dependências. Corrigi propostas que tratavam toda funcionalidade planejada como compromisso da R2. A decisão humana foi manter no backlog o ciclo completo do produto, mas separar o que seria entregue, validado ou continuado em release posterior.

**Evidências:** [roadmap](produto/roadmap.md) · [EAP](produto/EAP.md) · [Lean Inception](produto/lean_inception.md) · [backlog](backlog/visao-geral.md)

### Aprendizados intermediários

- Planejamento coerente exige a mesma data de corte e o mesmo vocabulário em todos os artefatos.
- Backlog de produto e compromisso de release são visões relacionadas, mas possuem finalidades diferentes.
- Uma sugestão de IA sobre prioridade só pode ser aceita depois de considerar dependências, capacidade e validação dos POs.

## Ciclo 3 — Regras de gamificação validadas com os POs

**Data:** 19/10/2026  
**Objetivo:** transformar decisões de produto sobre missões, XP e progressão em regras implementáveis e rastreáveis.

**Interação com IA.** Usei IA para confrontar atas, issues, documentação e implementação, destacando regras ambíguas ou contraditórias. Foram levantadas perguntas sobre metas, recompensas, renovação, missões semanais e perda de elo por inatividade.

**Revisão humana e decisão.** Confirmei com os POs as metas e recompensas, o escopo de missões semanais e a redução do tempo até o rebaixamento por inatividade. Corrigi a hipótese inicial de que as missões semanais ainda aguardavam validação. Também rejeitei a promessa de um total fixo de XP diário: as três missões são sorteadas e a recompensa depende da composição recebida.

**Evidências:** [ata de validação de 19/10](reunioes/reuniao-19-10-26.md) · [plano de gamificação](produto/plano-gamificacao.md) · [missões diárias](produto/missoes-diarias.md) · [issue #84](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/84) · [issue #89](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/89)

### Aprendizados intermediários

- A IA ajuda a encontrar contradições, mas não substitui a decisão do PO sobre comportamento e impacto motivacional.
- Regras de gamificação precisam registrar fonte do evento, limite de recompensa, renovação e idempotência.
- Uma decisão validada deve atualizar tanto o documento de produto quanto os critérios de aceite e a implementação.

## Ciclo 4 — Métricas e decisões gerenciais da R2

**Data:** 26/10/2026  
**Objetivo:** comparar R1 e R2 com dados verificáveis e usar os resultados no planejamento da R3.

**Interação com IA.** Solicitei a leitura dos JSONs de métricas, o cálculo de indicadores comparáveis e uma análise de cobertura, segurança, duplicação, velocidade e defeitos. A IA sugeriu normalizações e um índice agregado para apoiar a leitura do dashboard.

**Revisão humana e decisão.** Aceitei os cálculos somente após conferir as fontes e deixar fórmulas e limitações visíveis. Corrigi a janela da velocidade: o primeiro recorte ignorava a última sprint completa e foi refeito para 28/09–25/10. Rejeitei interpretar três issues com rótulo `bug` no repositório de documentação como o total de defeitos do produto. Os dados sustentaram três decisões para a R3: distribuir entregas ao longo da sprint, estimar itens e registrar horas reais, e priorizar os achados de segurança da Web.

**Evidências:** [análise do dashboard R2](dashboard-r2.md) · [dashboard publicado](https://2026-2-anatoquizup-doc.streamlit.app/) · [PR #112](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/pull/112) · [PR #116](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/pull/116)

### Aprendizados intermediários

- Métricas sem recorte, unidade e fonte visíveis produzem conclusões frágeis.
- Um índice agregado facilita comparação, mas pode esconder um risco específico, como a nota C de segurança da Web.
- Ausência de horas reais e pontos por história impede tratar proxies de custo e fluxo como EVM completa ou produtividade individual.

## Ciclo 5 — Fechamento integrado da R2

**Data:** 26/10/2026  
**Objetivo:** verificar se documentação, backend e frontend descreviam e entregavam o mesmo fluxo para revisão de erros e missões semanais.

**Interação com IA.** Pedi uma auditoria cruzada dos repositórios e PRs para localizar lacunas entre contrato, implementação e interface. A análise apontou o risco de ativar o catálogo semanal no banco antes de o estudante conseguir visualizar suas missões, o que poderia conceder XP de maneira pouco compreensível.

**Revisão humana e decisão.** Aceitei o risco identificado e defini a ativação coordenada como critério de segurança da entrega. O catálogo semanal deve permanecer inativo até que API, BFF, Web e validação estejam disponíveis juntos. Confirmei no código que o BFF já usa encaminhamento genérico de rotas de missões e que a Web possui a integração específica no PR correspondente; a ativação final depende da integração e do teste ponta a ponta. Para a US08, mantive contrato, estados vazios e tratamento de erro alinhados entre serviço e tela.

**Evidências:** [PR de missões semanais no Quiz-Service #19](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Quiz-Service/pull/19) · [PR de missões semanais na Web #26](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Web/pull/26) · [PR de revisão de erros no Quiz-Service #18](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Quiz-Service/pull/18) · [PR de revisão de erros na Web #25](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Web/pull/25) · [PR da especificação da US08 #119](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/pull/119)

### Aprendizados intermediários

- Uma migration pode alterar a experiência do usuário mesmo sem mudança de tela; dados ativos também são uma forma de lançamento.
- Funcionalidades distribuídas precisam de critério de ativação que cubra serviço, gateway, interface e teste integrado.
- Revisar cada PR isoladamente não detecta todas as lacunas; a unidade de validação deve ser o fluxo percebido pelo estudante.

## Síntese da decisão da R2

Na R2, decidi usar métricas e rastreabilidade como critérios de aceite das análises geradas com IA. Sugestões automáticas só foram incorporadas quando possuíam fonte verificável e permaneceram identificadas como hipótese quando dependiam de julgamento do time ou dos POs. Essa decisão evitou três erros concretos: uma janela incorreta de velocidade, a interpretação indevida de issues de documentação como defeitos totais e a ativação antecipada de missões semanais.

O sucesso desta decisão é verificável por quatro resultados: cinco ciclos registrados; recortes e fórmulas publicados no dashboard; pelo menos três decisões gerenciais ligadas a dados; e funcionalidades distribuídas com evidências cruzadas entre documentação e PRs.

## Referências

- INTERNATIONAL ORGANIZATION FOR STANDARDIZATION. **ISO/IEC 25010:2023 — Systems and software engineering: Product quality model**. 2023.
- MARTÍNEZ-FERNÁNDEZ, Silverio et al. **A Quality Model for Actionable Analytics in Rapid Software Development**. 2018.
- CHOMA, Joel et al. **Towards an artifact to support agile teams in software analytics activities**. 2022.
- KIM, Amy Jo. **Game Thinking: Innovate Smarter & Drive Deep Engagement with Design Techniques from Hit Games**. 2018.
- WERBACH, Kevin; HUNTER, Dan. **For the Win: The Power of Gamification and Game Thinking in Business, Education, Government, and Social Impact**. 2020.

## Checklist da R2

- [x] Cinco ciclos individuais acumulados.
- [x] Seção de aprendizados intermediários em todos os ciclos.
- [x] Uso crítico de IA com itens aceitos, corrigidos ou rejeitados.
- [x] Evidências rastreáveis em documentos, issues, PRs e dashboard.
- [x] Decisão e critérios de sucesso mensuráveis.
- [ ] Matrícula incluída na cópia individual enviada ao Aprender 3.
- [ ] Revisão final da estudante antes da submissão individual.
