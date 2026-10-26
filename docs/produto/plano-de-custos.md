# Plano de Gerenciamento de Custos - AnatoQuizUp

## Histórico de Versão

| Data | Versão | Descrição | Autor | Revisor(es) |
| --- | --- | --- | --- | --- |
| 14/09/2026 | 1.0 | Criação e estruturação do plano de custos unificado | [João Paulo Lima](https://github.com/jpaulohe4rt) | [Letícia Torres Soares Martins](https://github.com/leticiatmartins) ([PR #15](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/pull/15)) |
| 27/09/2026 | 1.1 | Adição do rateio de custo por release major (R1, R2, R3) com base nas datas do cronograma oficial | [João Paulo Lima](https://github.com/jpaulohe4rt) | [João Lucas Araújo Siqueira](https://github.com/jlucasiqueira) ([PR #44](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/pull/44)) |
| 21/10/2026 | 1.2 | Substituição do salário de mercado fictício pelo custo-hora real do estudante da UnB, adição do Custo por Story Point e reestruturação do EVM ágil para uso de dados reais de sprint (issue [#78](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/78)) | [João Paulo Lima](https://github.com/jpaulohe4rt) | |
| 25/10/2026 | 2.0 | Custo derivado do crédito da disciplina, computadores por depreciação em vez de compra, energia, internet e hospedagem rateadas, planilha de cálculo publicada e AgileEVM com BAC, PV, EV, AC, SPI e CPI, incluindo a situação da R1 | [João Paulo Lima](https://github.com/jpaulohe4rt) | |
| 25/10/2026 | 2.1 | Premissas reancoradas em fontes do nosso contexto: base de 2023 corrigida pelo IPCA real do Banco Central, créditos por ano tirados do fluxo de Engenharia de Software, carga semanal de 12 h 100% remotas derivada das cerimônias do time, tarifa da Neoenergia vigente desde 22/10/2026, consumo do notebook da equipe e depreciação pela regra do setor público (valor residual de 10%) | [João Paulo Lima](https://github.com/jpaulohe4rt) | |

---

## 1. Introdução

Este plano registra quanto custa construir o AnatoQuizUp e como a equipe acompanha esse custo ao longo do semestre. A organização segue o PMBOK [1]: primeiro as premissas e as estimativas, depois o controle do que foi efetivamente gasto.

O AnatoQuizUp é um projeto acadêmico da Universidade de Brasília, então nada aqui é cobrado de clientes, professores ou usuários. O custo real é o custo do estudante para a universidade: quanto a UnB investe no tempo que a equipe dedica à disciplina, mais a depreciação dos computadores que cada integrante já tem e o rateio de energia, internet e hospedagem. Nenhum salário de mercado entra na conta: foi a referência das versões 1.0 e 1.1 deste plano, e ela não descreve o custo de um projeto conduzido por estudantes.

A lógica de cálculo (custo do crédito, depreciação, rateio e AgileEVM) é a mesma que as outras equipes da disciplina usam, o que permite comparar os projetos. As premissas, por outro lado, são as do nosso contexto: o fluxo de Engenharia de Software, a carga de trabalho registrada na nossa [metodologia](../metodologia/metodologia.md), o notebook de referência da equipe e as tarifas vigentes em outubro de 2026. Cada uma traz a fonte ao lado, e quem quiser refazer a conta com outras premissas só precisa mudar a aba **Parâmetros** da planilha.

---

## 2. Premissas da Estimativa

| Premissa | Valor adotado | De onde vem |
| --- | ---: | --- |
| Período considerado | 18 semanas (10/08 a 14/12/2026) | Cronograma da disciplina |
| Semanas dentro das releases | 15 (R1 6 + R2 4 + R3 5) | [Roadmap](roadmap.md) |
| Equipe baseline | 13 integrantes | Lista do levantamento de disponibilidade da primeira semana |
| Equipe efetiva atual | 11 integrantes | [Página inicial da documentação](../index.md) |
| Carga semanal por integrante | 12 h, todas remotas | 4,5 h de cerimônias da [metodologia](../metodologia/metodologia.md) e 7,5 h de trabalho assíncrono |
| Créditos da disciplina (FGA0206) | 4 (60 h), 2 deles de extensão | Projeto pedagógico do curso [4] |
| Créditos cursados por ano | 46,4 | 232 créditos do fluxo em 10 semestres [4] |
| Duração da sprint | 1 semana | [Metodologia](../metodologia/metodologia.md) |
| Valor de referência do notebook | R$ 4.047,99 | Equipamento padrão adotado pela equipe |
| Vida útil e valor residual | 60 meses, 10% | Regra de depreciação do setor público [5] |
| Tarifa de energia | R$ 0,83429/kWh | Neoenergia Brasília, vigência 22/10/2026 [6] |
| Consumo em hora de trabalho | 0,075 kWh/h | Notebook em carga de desenvolvimento somado ao roteador |
| Plano de internet residencial | R$ 99,90/mês | Oi fibra [7] |
| Horas por mês para o rateio | 730 h | Média real do mês (8.766 h por ano) |
| Hospedagem | Railway Hobby, US$ 5,00/mês | Railway [8] |
| Cotação do dólar | R$ 4,9652 | Consulta em 23/10/2026 [9] |

Duas premissas merecem explicação.

A **carga de 12 h semanais** sai das nossas próprias cerimônias: planning, review e retrospectiva somam 3 h por sprint e a reunião com os POs mais 1,5 h, o que dá 4,5 h síncronas por semana. As outras 7,5 h são de trabalho assíncrono, bem abaixo da disponibilidade que o time declarou no levantamento da primeira semana do semestre. Como a equipe é 100% remota, as 12 h entram inteiras no rateio de energia e internet, sem a parcela presencial que outros times contabilizam.

A **equipe baseline de 13 integrantes** é o plano do início do semestre: o levantamento de disponibilidade da primeira semana lista 13 nomes, e dois deles saíram depois. O orçamento previsto (`PV`/`BAC`) usa esses 13, e o custo real (`AC`) acompanha a equipe efetiva de cada sprint, hoje 11. É a diferença entre os dois que dá sentido ao índice de custo (`CPI`): quando a equipe encolhe, o projeto gasta menos do que foi planejado, e isso precisa aparecer no acompanhamento.

---

## 3. Estimativa de Custos

### 3.1. Custo do estudante para a UnB

O MEC apurou um custo médio anual de R$ 52.533,00 por aluno de universidade federal no ano-base de 2023 [2]. Como o projeto acontece em 2026, o valor é corrigido pelo IPCA acumulado entre janeiro de 2024 e setembro de 2026, calculado a partir da série mensal do Banco Central [3]. O denominador é o nosso fluxo: 232 créditos distribuídos em 10 semestres, o que dá 23,2 créditos por semestre e 46,4 por ano [4].

| Item | Valor | Fonte / cálculo |
| --- | ---: | --- |
| Custo anual por estudante (2023) | R$ 52.533,00 | MEC, ano-base 2023 [2] |
| IPCA acumulado de jan/2024 a set/2026 | 13,62% | Série 433 do Banco Central [3] |
| Custo anual corrigido para 2026 | R$ 59.688,31 | 52.533,00 × 1,1362 |
| Créditos cursados por ano | 46,4 | 232 créditos em 10 semestres [4] |
| Custo por crédito | R$ 1.286,39 | 59.688,31 ÷ 46,4 |
| Créditos da disciplina | 4 (60 h) | FGA0206, dois créditos práticos e dois teóricos [4] |
| Custo por estudante na disciplina | R$ 5.145,54 | 1.286,39 × 4 |
| **Custo semanal por estudante** | **R$ 285,86** | 5.145,54 ÷ 18 semanas |

Ninguém desembolsa esse valor. Ele é uma aproximação do investimento público no tempo que os estudantes dedicam à disciplina.

### 3.2. Computadores (depreciação)

Cada integrante usa o próprio computador, então o plano não considera a compra de máquinas, só a depreciação do período do projeto. A regra aplicada é a do setor público, que é o contexto da UnB: equipamentos de processamento de dados têm vida útil de 60 meses e valor residual de 10%, ou seja, apenas 90% do valor é depreciável [5].

| Item | Valor |
| --- | ---: |
| Valor de referência do notebook | R$ 4.047,99 |
| Parcela depreciável (90%) | R$ 3.643,19 |
| Semanas de vida útil | 260 |
| **Depreciação semanal por integrante** | **R$ 14,01** |

### 3.3. Energia

Como o time é 100% remoto, todas as 12 h semanais consomem energia na casa de cada integrante. A tarifa é a da Neoenergia Brasília homologada pela ANEEL com vigência a partir de 22/10/2026 [6]. O consumo considera o notebook em carga de desenvolvimento, com cerca de 65 W, mais 10 W do roteador. É a premissa mais frágil da lista e vale medir com um wattímetro antes da próxima revisão.

| Item | Valor |
| --- | ---: |
| Horas de trabalho por semana | 12 h |
| Consumo estimado | 0,075 kWh/h |
| Tarifa | R$ 0,83429/kWh |
| **Custo semanal por integrante** | **R$ 0,75** |

### 3.4. Internet

A internet é uma assinatura mensal que atende a casa inteira, então entra rateada pelas horas de projeto. O mês usado no rateio é o mês médio real, de 730 h, e não um mês redondo de 720 h.

| Item | Valor |
| --- | ---: |
| Plano considerado | R$ 99,90/mês [7] |
| Horas no mês | 730 h |
| Custo por hora | R$ 0,14 |
| Horas de projeto por semana | 12 h |
| **Custo semanal por integrante** | **R$ 1,64** |

### 3.5. Hospedagem, deploy e ferramentas de apoio

O BFF, o Usuário-Service e o Quiz-Service rodam no Railway e o Web é publicado no Netlify, como descreve o [ambiente de homologação](../operacao/ambiente-homologacao.md). O custo considerado é o plano Hobby do Railway [8], convertido pela cotação de 23/10/2026 [9].

| Item | Valor |
| --- | ---: |
| Plano Railway Hobby | US$ 5,00/mês |
| Cotação utilizada | R$ 4,9652 |
| Custo mensal convertido | R$ 24,83 |
| **Custo semanal do projeto** | **R$ 5,73** |

As outras ferramentas são gratuitas no uso acadêmico e entram com custo zero: GitHub e GitHub Actions para versionamento e CI, Netlify para publicar o Web, SonarCloud para qualidade, ZenHub para o quadro, MkDocs Material para a documentação e Figma para os protótipos.

### 3.6. Custo por integrante e custo-hora

| Componente | R$/semana |
| --- | ---: |
| Disciplina (custo do estudante para a UnB) | 285,86 |
| Depreciação do computador | 14,01 |
| Internet | 1,64 |
| Energia | 0,75 |
| **Total por integrante** | **302,27** |

Os componentes aparecem arredondados; o total usa os valores cheios da planilha, por isso ele fecha em R$ 302,27 e não em R$ 302,26.

Com **12 h semanais** por integrante:

```
custo-hora = 302,27 ÷ 12 = R$ 25,19
```

Para converter escopo em dinheiro no EVM, a disciplina adota a referência de 8 h por story point para um desenvolvedor júnior. É uma média de planejamento, e não uma equivalência fixa entre pontos e horas [11]:

```
custo por story point = 25,19 × 8 = R$ 201,51
```

Somando a hospedagem, o custo semanal do projeto é de **R$ 3.935,23** com a equipe baseline de 13 integrantes e de **R$ 3.330,69** com a equipe efetiva de 11.

### 3.7. Orçamento por release (BAC)

```
BAC da release = custo semanal do projeto (baseline) × semanas da release
```

| Release | Período | Semanas | Horas planejadas | BAC |
| --- | --- | :---: | ---: | ---: |
| **R1** | 17/08 a 27/09/2026 | 6 | 936 | R$ 23.611,37 |
| **R2** | 28/09 a 25/10/2026 | 4 | 624 | R$ 15.740,92 |
| **R3** | 26/10 a 29/11/2026 | 5 | 780 | R$ 19.676,14 |
| **Subtotal das releases** | | **15** | **2.340** | **R$ 59.028,43** |
| Semanas fora das releases | 10/08 a 16/08 e 30/11 a 14/12 | 3 | 468 | R$ 11.805,69 |
| **Total do semestre** | | **18** | **2.808** | **R$ 70.834,12** |

As datas das releases seguem o [roadmap](roadmap.md). As três semanas restantes são a preparação inicial e o encerramento do projeto, que não têm release própria.

### 3.8. Estimativa consolidada

| Categoria | Custo semanal (13 integrantes) | Total em 18 semanas |
| --- | ---: | ---: |
| Disciplina (tempo dos estudantes) | R$ 3.716,23 | R$ 66.892,07 |
| Computadores (depreciação) | R$ 182,16 | R$ 3.278,87 |
| Internet | R$ 21,35 | R$ 384,27 |
| Energia | R$ 9,76 | R$ 175,70 |
| Hospedagem e deploy | R$ 5,73 | R$ 103,20 |
| Ferramentas de apoio | R$ 0,00 | R$ 0,00 |
| **Total estimado** | **R$ 3.935,23** | **R$ 70.834,12** |

A hospedagem é o único desembolso direto previsto. O resto representa custo acadêmico, depreciação ou rateio de recursos que a equipe já usa no dia a dia.

---

## 4. Planilha de custos

Os números acima não foram digitados no documento: são fórmulas na planilha do projeto. Mudar uma premissa na aba Parâmetros recalcula o custo-hora, o orçamento das releases e o EVM.

[Baixar a planilha de custos e AgileEVM](../assets/plano-de-custos-anatoquizup.xlsx){ .md-button .md-button--primary }

| Aba | Conteúdo |
| --- | --- |
| **Parâmetros** | Toda premissa com valor, unidade, fonte e fórmula |
| **Custo por integrante** | Componentes semanais, custo-hora e custo por story point |
| **Orçamento** | BAC por release e total do semestre |
| **Horas** | Uma linha por integrante por sprint, base do custo real (`AC`) |
| **AgileEVM** | PV, EV, AC, SPI, CPI, SV, CV, EAC e VAC acumulados por sprint |

---

## 5. Controle e monitoramento com AgileEVM

O acompanhamento segue o AgileEVM [10], que adapta o Earned Value Management ao Scrum medindo escopo em story points e tempo em sprints. O cálculo é cumulativo, então cada sprint mostra onde o projeto está até aquele ponto, e não um retrato isolado da semana.

### 5.1. Modelo e fórmulas

| Grandeza | Fórmula | O que responde |
| --- | --- | --- |
| **BAC** | custo semanal do projeto (baseline) × semanas da release | Orçamento autorizado da release |
| **PV (SP)** | pontos planejados acumulados | Escopo que deveria estar pronto |
| **EV (SP)** | pontos concluídos acumulados | Escopo efetivamente pronto |
| **SPI** | `EV(SP) ÷ PV(SP)` | Abaixo de 1: atraso de escopo |
| **PV (R$)** | custo semanal do projeto × sprints decorridas | Orçamento previsto até a data |
| **EV (R$)** | `SPI × PV(R$)` | Valor orçado do trabalho realizado |
| **AC (R$)** | horas reais acumuladas × custo-hora | Custo real incorrido |
| **CPI** | `EV(R$) ÷ AC(R$)` | Abaixo de 1: gasto maior que o entregue |
| **SV, CV** | `EV − PV`, `EV − AC` | Variações em reais |
| **EAC, VAC** | `BAC ÷ CPI`, `BAC − EAC` | Projeção de custo final e desvio |

No acompanhamento acumulado do projeto, o `EAC` usa o BAC das 15 semanas de release (R$ 59.028,43); no acompanhamento de uma release isolada, usa-se o BAC daquela release (§3.7).

### 5.2. De onde vem cada número

| Dado | Fonte |
| --- | --- |
| Pontos planejados e concluídos por sprint | Quadro do [ZenHub](https://app.zenhub.com/workspaces/2026-2-anatoquizup-62c22d94edb2f3001765c363/board) |
| Horas reais por integrante por sprint | Aba **Horas** da planilha |
| Custo-hora e custo semanal do projeto | Aba **Parâmetros** (§3.6) |
| BAC de cada release | Aba **Orçamento** (§3.7) |
| Itens concluídos por release | [Dashboards](../dashboards.md) |

### 5.3. Regras

- **Feito é issue fechada com estimativa.** Issue aberta não conta, em qualquer coluna do quadro.
- **Pontos só em User Story ou Task.** Uma história decomposta em tarefas não recebe pontos, para o mesmo escopo não ser contado duas vezes.
- **Baseline congelada na planning da release.** O escopo que entra depois é registrado como ponto adicionado, para a mudança ficar visível.
- **Sem horas registradas não há CPI.** O `AC` fica declarado como indisponível e nunca é substituído pelo custo planejado. Quem troca um pelo outro faz o `CPI` repetir o `SPI`, e aí o índice de custo não informa mais nada.
- **A equipe efetiva entra no `AC`, não no `PV`.** O orçamento previsto segue a baseline de 13 integrantes; o custo real acompanha quem estava ativo em cada sprint.

### 5.4. Situação da R1

A R1 não teve story points nem horas registradas. Isso já constava nos [dashboards](../dashboards.md) ("as estimativas em pontos e o histórico diário do burndown ainda não foram registrados pela equipe") e explica os índices sem rastreabilidade que apareceram na avaliação da release. A tabela abaixo reconstitui a posição da R1 com o dado real que existe e declara o que falta:

| Grandeza | Valor | Observação |
| --- | ---: | --- |
| BAC / PV (R$) | R$ 23.611,37 | Release encerrada: o previsto é o BAC integral |
| Itens planejados / concluídos | 11 / 6 | [Dashboards](../dashboards.md), 27/09/2026 |
| APC (proxy por itens) | 0,55 | Sem story points registrados, a conta usa os itens concluídos |
| EV (R$) | R$ 12.878,93 | `APC × PV` |
| SPI | 0,55 | 55% do escopo planejado da R1 entregue |
| AC (R$) | indisponível | Sem registro de horas na R1 |
| CPI, EAC, VAC | não calculados | Dependem do `AC` |

Para referência, a R1 com a equipe efetiva de 11 integrantes em 6 semanas custaria R$ 19.984,15. Esse número sai da capacidade planejada, não de horas medidas, por isso não entra como `AC`.

**A partir da R2:** estimar em pontos todos os itens na planning, congelar a baseline da release e registrar as horas de cada integrante por sprint na aba Horas da planilha. Com isso o `AC` passa a ser medido, o `CPI` sai de indisponível e o EVM alimenta o dashboard com dados que qualquer pessoa consegue auditar.

### 5.5. Matriz de análise geral

| | Atrasado | No Prazo | Adiantado |
| :-: | :---------: | :-------: | :--------: |
| **Abaixo do Orçamento** | Requer investigação | Cenário Ideal | Cenário Ideal |
| **No Orçamento** | Cenário Ruim | Cenário Ideal | Cenário Ideal |
| **Acima do Orçamento** | Cenário Ruim | Cenário Ruim | Requer investigação |

---

## 6. Referências

> [1] PMI. **Um guia do conhecimento em gerenciamento de projetos (Guia PMBOK)**. 6. ed. Project Management Institute, 2017.

> [2] PODER360. **Alunos de universidades federais têm custo anual de R$ 52.533**. 2025, com base em dados do MEC (Painel do Censo da Educação Superior e plataforma Universidade 360°) para o ano-base 2023. Disponível em: <https://www.poder360.com.br/poder-economia/alunos-de-universidades-federais-tem-custo-medio-anual-de-r-52-533/>.

> [3] BANCO CENTRAL DO BRASIL. **Sistema Gerenciador de Séries Temporais, série 433 (IPCA, variação mensal)**. Consulta em 25/10/2026, acumulando os meses de janeiro de 2024 a setembro de 2026 (fator 1,1362). Disponível em: <https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json>.

> [4] UNIVERSIDADE DE BRASÍLIA, FACULDADE DE CIÊNCIAS E TECNOLOGIAS EM ENGENHARIA. **Projeto Pedagógico do Curso de Engenharia de Software**. Créditos da disciplina FGA0206, Engenharia de Produto de Software (2 teóricos e 2 práticos, 60 h), e total de 232 créditos distribuídos em 10 semestres. Disponível em: <https://software.unb.br/matriz-curricular/>.

> [5] SECRETARIA DO TESOURO NACIONAL. **Manual SIAFI, macrofunção 020330: depreciação, amortização e exaustão**. Equipamentos de processamento de dados: vida útil de 60 meses e valor residual de 10%.

> [6] ANEEL / NEOENERGIA BRASÍLIA. **Resolução homologatória nº 3.614: tarifas de energia elétrica do grupo B**. Tarifa residencial convencional de R$ 0,83429/kWh, vigência de 22/10/2026 a 21/10/2027. Disponível em: <https://www.neoenergia.com/pt-br/para-sua-casa/tarifas>.

> [7] OI. **Internet fibra ótica: planos de internet banda larga**. Disponível em: <https://www.oi.com.br/internet>.

> [8] RAILWAY. **Pricing Plans**. Disponível em: <https://docs.railway.com/pricing/plans>.

> [9] AWESOMEAPI. **Cotação USD-BRL**. Consulta em 23/10/2026: R$ 4,9652. Disponível em: <https://economia.awesomeapi.com.br/last/USD-BRL>.

> [10] SULAIMAN, T.; BARTON, B.; BLACKBURN, T. **AgileEVM: Earned Value Management in Scrum Projects**. Agile Conference, 2006.

> [11] COHN, Mike. **Don't Equate Story Points to Hours**. Mountain Goat Software, 2024. Disponível em: <https://www.mountaingoatsoftware.com/blog/dont-equate-story-points-to-hours>.
