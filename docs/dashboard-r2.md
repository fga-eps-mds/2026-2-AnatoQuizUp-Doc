# Análise do dashboard — R2

**Data de referência:** 26/10/2026, última coleta disponível nos JSONs publicados na `main` (até 11h17 no horário de Brasília). **Marco da entrega:** 26/10/2026. Esta página descreve a análise preparada para a R2. [Abrir o app Streamlit](https://2026-2-anatoquizup-doc.streamlit.app/).

## Fontes e recortes

| Indicador | Fonte | Recorte e unidade |
| --- | --- | --- |
| Cobertura, segurança e duplicação | JSONs SonarCloud em `analytics-raw-data/<repo>/` | Última coleta de cada repositório até 28/09/2026 (R1) e de 29/09 a 26/10/2026 (R2); percentuais ou nota A–E |
| Velocidade observada | Captura mais recente de issues do repositório Doc | Issues fechadas por janela **completa** de sete dias; média em issues/semana, sem story points e sem equivaler a histórias aceitas |
| Defeitos registrados | Rótulo `bug` na mesma captura de issues | Contagem pela data de criação da issue; **proxy limitado** ao backlog central, que contém documentação e DevOps |

O app lê os dois formatos do exportador SonarCloud: `baseComponent.measures` (setembro) e `project_measures` (outubro). O nome do projeto é normalizado porque a chave Sonar mudou entre as coletas. Os horários do app são exibidos no horário de Brasília. O workflow `metricas.yml` de cada serviço exporta após o merge de PR ou acionamento manual; não há coleta periódica garantida a cada sprint. As coletas de 26/10 foram conferidas nos quatro repositórios.

## Comparação disponível

| Repositório | Cobertura R1 | Cobertura R2 (26/10) | Variação |
| --- | ---: | ---: | ---: |
| BFF | 96,7% | 97,0% | +0,3 p.p. |
| Quiz-Service | 94,0% | 95,0% | +1,0 p.p. |
| Usuario-Service | 96,8% | 96,5% | −0,3 p.p. |
| Web | 91,6% | 92,1% | +0,5 p.p. |

No backlog central, a média nas janelas completas é **2,29 issues/semana na R1** (16 fechamentos em sete semanas) e **2,00 issues/semana na R2 até a coleta** (seis fechamentos em três semanas). Como a equipe não registrou pontos por história nesse conjunto de dados, isso é apenas um indicador de fluxo; diferenças de tamanho e tipo das issues não são controladas.

Há **uma issue rotulada `bug` criada na R1** ([#11, sobre templates](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/11)) e **duas na R2** ([#75, sobre Node no pipeline e Dockerfile](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/75), e [#106, sobre o parser do dashboard](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/106)). Não é uma série representativa dos defeitos do produto. A próxima evolução da coleta deve reunir issues de defeito dos quatro repositórios de código e aplicar o mesmo critério de classificação nos dois períodos.

## Normalização, pesos e agregação

O índice composto é uma **convenção analítica proposta**, sujeita à validação do time e do professor. Ele permite comparar unidades diferentes sem ocultar as medidas originais:

1. Cobertura: percentual SonarCloud limitado ao intervalo de 0 a 100.
2. Segurança: nota A, B, C, D ou E convertida respectivamente em 100, 75, 50, 25 ou 0.
3. Duplicação: `máximo(0, 100 − 10 × percentual de linhas duplicadas)`.
4. Índice por repositório: `0,50 × cobertura + 0,25 × segurança + 0,25 × duplicação`.
5. Índice do produto: média simples dos quatro repositórios, apenas se houver dados de todos eles em ambas as releases.

A cobertura recebe metade do peso porque a meta de 85% é um critério explícito da R2; os outros dois critérios dividem o restante. A fórmula **não substitui** a avaliação do SonarCloud, não mede defeitos em produção e não prova qualidade pedagógica. Os índices calculados com os arquivos atuais são **87,8/100 na R1** e **91,3/100 na R2** (arredondados). A nota de segurança do Quiz-Service melhorou de **C para A**; a Web permanece em **C**. O índice agregado não deve esconder esse ponto de atenção.

## Decisões gerenciais propostas para validação do time

Estas são recomendações fundamentadas no dashboard, **não atas de decisões já aprovadas**. Para cumprir o critério da disciplina, a equipe precisa registrar responsável, data de deliberação, decisão efetiva e acompanhamento na Wiki.

| # | Causa e evidência | Ação proposta | Confirmação necessária |
| --- | --- | --- | --- |
| 1 | O exportador de outubro mudou o campo de medidas e a chave do projeto; a correção do parser já chegou à `main` em 26/10. | Garantir que o painel R2 preserve essa leitura e conferir cobertura, segurança e duplicação dos quatro repositórios antes da apresentação. | Revisão do PR e comparação dos valores exibidos com os JSONs. |
| 2 | A média observada do backlog caiu de 2,29 para 2,00 issues/semana; as issues não têm tamanho estimado nessa fonte. | Revisar capacidade e WIP da próxima sprint com o ZenHub, registrar pontos e separar histórias de tarefas administrativas. | Retrospectiva do time e verificação do burndown no ZenHub. |
| 3 | A Web ainda tem nota de segurança C; a nota do Quiz-Service subiu de C para A; a cobertura do Usuario-Service caiu 0,3 p.p. | Inspecionar as causas na Web e no Usuario-Service, registrar o que mudou no Quiz-Service e priorizar correções verificáveis. | Triagem técnica e validação dos limiares com o professor. |

## Uso crítico de IA nesta análise

**Aproveitado como hipótese verificável:** a sugestão de comparar releases por repositório e de combinar métricas normalizadas. As fórmulas e os números foram conferidos contra os JSONs versionados. **Descartado:** tratar as três issues `bug` do repositório Doc como prova de apenas três defeitos do produto; seus títulos e escopos mostram que essa conclusão seria indevida. **Pendente de julgamento humano:** pesos do índice, causas da variação de velocidade, limiares de qualidade e adoção das três ações acima. O time deve complementar este registro com os prompts e resultados de IA usados pelos integrantes no `MD_Template.md` e na Wiki.

## Checklist de publicação

- [x] Conferir as coletas dos quatro repositórios publicadas em 26/10.
- [ ] Validar pesos, limiares e três decisões com o time e professor; registrar causa, evidência e ação na Wiki.
- [ ] Registrar a análise crítica de IA e as entradas individuais no `MD_Template.md`.
- [ ] Fazer merge do PR, abrir o app publicado, conferir a comparação R1 × R2 e enviar URL e PR no Aprender 3.
