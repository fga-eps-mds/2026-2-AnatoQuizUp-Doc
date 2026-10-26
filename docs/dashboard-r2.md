# Análise do dashboard — R2

**Data de referência:** 26/10/2026, última coleta disponível nos JSONs publicados na `main` (até 11h17 no horário de Brasília). **Marco da entrega:** 26/10/2026. Esta página descreve a análise preparada para a R2. [Abrir o app Streamlit](https://2026-2-anatoquizup-doc.streamlit.app/).

## Fontes e recortes

| Indicador | Fonte | Recorte e unidade |
| --- | --- | --- |
| Cobertura, segurança e duplicação | JSONs SonarCloud em `analytics-raw-data/<repo>/` | Última coleta de cada repositório até 28/09/2026 (R1) e de 29/09 a 26/10/2026 (R2); percentuais ou nota A–E |
| Velocidade observada | Captura mais recente de issues do repositório Doc | Semanas completas de sprint, de segunda a domingo: R1 de 10/08 a 27/09; R2 de 28/09 a 25/10; issues fechadas por semana, sem story points ou aceite do cliente |
| Defeitos registrados | Rótulo `bug` na mesma captura de issues | Contagem pela data de criação da issue; **proxy limitado** ao backlog central, que contém documentação e DevOps |

O app lê os dois formatos do exportador SonarCloud: `baseComponent.measures` (setembro) e `project_measures` (outubro). O nome do projeto é normalizado porque a chave Sonar mudou entre as coletas. Os horários do app são exibidos no horário de Brasília. O workflow `metricas.yml` de cada serviço exporta após o merge de PR ou acionamento manual; não há coleta periódica garantida a cada sprint. As coletas de 26/10 foram conferidas nos quatro repositórios.

## Comparação disponível

| Repositório | Cobertura R1 | Cobertura R2 (26/10) | Variação |
| --- | ---: | ---: | ---: |
| BFF | 96,7% | 97,0% | +0,3 p.p. |
| Quiz-Service | 94,0% | 95,0% | +1,0 p.p. |
| Usuario-Service | 96,8% | 96,5% | −0,3 p.p. |
| Web | 91,6% | 92,1% | +0,5 p.p. |

No backlog central, a média nas semanas completas é **2,29 issues/semana na R1** (16 fechamentos em sete semanas) e **8,25 issues/semana nas sprints da R2** (33 fechamentos em quatro semanas). A última sprint completa, de 19 a 25/10, concentrou **27 dos 33 fechamentos** (81,8%). O dia 26/10 ainda era parcial na coleta e não entra nessa média. O recorte das sprints R2 (28/09–25/10) segue o [plano de custos v2.1](produto/plano-de-custos.md); o recorte das métricas de produto permanece 29/09–26/10. Portanto, a média aumentou, mas as entregas ficaram concentradas no fim. Como não há pontos por história nessa captura, a contagem é apenas um indicador de fluxo: diferenças de tamanho e tipo das issues não são controladas.

Há **uma issue rotulada `bug` criada na R1** ([#11, sobre templates](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/11)) e **duas na R2** ([#75, sobre Node no pipeline e Dockerfile](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/75), e [#106, sobre o parser do dashboard](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/106)). Não é uma série representativa dos defeitos do produto. A próxima evolução da coleta deve reunir issues de defeito dos quatro repositórios de código e aplicar o mesmo critério de classificação nos dois períodos.

## Normalização, pesos e agregação

O índice composto é uma **convenção analítica proposta**, sujeita à validação do time e do professor. Ele permite comparar unidades diferentes sem ocultar as medidas originais:

1. Cobertura: percentual SonarCloud limitado ao intervalo de 0 a 100.
2. Segurança: nota A, B, C, D ou E convertida respectivamente em 100, 75, 50, 25 ou 0.
3. Duplicação: `máximo(0, 100 − 10 × percentual de linhas duplicadas)`.
4. Índice por repositório: `0,50 × cobertura + 0,25 × segurança + 0,25 × duplicação`.
5. Índice do produto: média simples dos quatro repositórios, apenas se houver dados de todos eles em ambas as releases.

A cobertura recebe metade do peso porque a meta de 85% é um critério explícito da R2; os outros dois critérios dividem o restante. A fórmula **não substitui** a avaliação do SonarCloud, não mede defeitos em produção e não prova qualidade pedagógica. Os índices calculados com os arquivos atuais são **87,8/100 na R1** e **91,3/100 na R2** (arredondados). A nota de segurança do Quiz-Service melhorou de **C para A**; a Web permanece em **C**. O índice agregado não deve esconder esse ponto de atenção.

### Índice exploratório de processo

O painel agrega dois indicadores normalizados de 0 a 100, calculados com as **mesmas semanas completas da velocidade**: **atividade** = `100 × semanas com ao menos um fechamento ÷ semanas completas`; **distribuição** = `100 × (1 − maior parcela semanal dos fechamentos) ÷ (1 − 1/número de semanas)`. O índice de processo é `0,50 × atividade + 0,50 × distribuição`. Os pesos iguais permitem ler cadência e concentração sem converter quantidade de issues em valor entregue. Se não houver fechamentos ou menos de duas semanas completas, o índice fica indisponível.

| Período | Fechamentos semanais | Atividade | Distribuição | Índice de processo |
| --- | --- | ---: | ---: | ---: |
| R1 | 0, 0, 0, 0, 1, 3, 12 | 42,9 | 29,2 | 36,0 |
| Sprints R2 | 4, 0, 2, 27 | 75,0 | 24,2 | 49,6 |

O índice subiu pela presença de fechamentos em mais semanas; a **distribuição piorou**, coerente com a concentração na última sprint. Ele mede somente o padrão de fechamento do backlog Doc. Não mede produtividade individual, complexidade, pontos entregues ou qualidade do processo de aceite.

### EVM-Ágil e custos

O painel passa a usar o [plano de custos v2.1](produto/plano-de-custos.md): BAC da R1 de **R$ 23.611,37**, da R2 de **R$ 15.740,92**, custo semanal baseline de **R$ 3.935,23** e **sem compra única de hardware**. Para a R1, seis de 11 itens do escopo haviam sido fechados até 27/09; o APC por quantidade é **54,5%** e o EV proxy é **R$ 12.878,93**. O burndown por quantidade de issues continua sendo um proxy, sem pontos por história. Como as horas reais por integrante não foram registradas, **AC e CPI ficam indisponíveis**; custo planejado não substitui AC.

## Decisões gerenciais para o planejamento da R3

As três decisões abaixo foram incorporadas a esta revisão em 26/10 para orientar o planejamento da R3 e [registradas na Wiki](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/wiki). A equipe ainda deve registrar a deliberação coletiva, os responsáveis individuais e os prazos; este documento não substitui a ata da equipe.

| # | Evidência do dashboard | Decisão gerencial | Acompanhamento |
| --- | --- | --- | --- |
| 1 | **27/33 issues** foram fechadas na última sprint completa da R2; a distribuição normalizada caiu de 29,2 para 24,2. | Distribuir entregas ao longo de cada sprint, limitar trabalho simultâneo e revisar bloqueios no meio da semana. | Acompanhar fechamentos por semana e discutir a concentração na review/retro da próxima sprint. |
| 2 | O backlog não tem pontos por história para esta série; o plano de custos não possui horas reais da R1, logo **AC/CPI são indisponíveis**. | Estimar story points dos itens elegíveis antes de iniciar a R3, congelar a baseline e registrar horas reais por integrante a cada sprint. | Conferir burndown e SPI em pontos no ZenHub; calcular CPI somente depois de medir AC. |
| 3 | A Web segue com nota de segurança **C**, enquanto o Quiz-Service passou de C para A. | Priorizar a triagem e correção dos achados de segurança da Web no backlog da R3 antes de ampliar o escopo do frontend. | Vincular issues e PRs às evidências SonarCloud e verificar a nota na próxima coleta. |

## Uso crítico de IA nesta análise

**Aproveitado como hipótese verificável:** comparar releases por repositório e combinar métricas normalizadas, sempre com fórmula e fonte visíveis. **Corrigido após conferência dos JSONs:** a conclusão anterior de queda na velocidade ignorava a última sprint completa porque o recorte começava numa terça-feira; os 33 fechamentos de 28/09 a 25/10 foram recontados. **Descartado:** tratar as três issues `bug` do repositório Doc como prova de apenas três defeitos do produto. **Pendente de julgamento humano:** pesos dos índices, causas da concentração de fechamentos e limiares de qualidade. O time deve complementar este registro com os prompts e resultados de IA usados pelos integrantes no `MD_Template.md` e na Wiki.

## Checklist de publicação

- [x] Conferir as coletas dos quatro repositórios publicadas em 26/10.
- [x] Registrar as três decisões, evidências e acompanhamento na Wiki.
- [ ] Registrar a deliberação coletiva, responsáveis e prazos; validar pesos e limiares com o time e professor.
- [ ] Registrar a análise crítica de IA e as entradas individuais no `MD_Template.md`.
- [ ] Fazer merge do PR, abrir o app publicado, conferir a comparação R1 × R2 e enviar URL e PR no Aprender 3.
