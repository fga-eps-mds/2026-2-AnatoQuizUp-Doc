# Plano de Gerenciamento de Custos - AnatoQuizUp

## Histórico de Versão

| Data | Versão | Descrição | Autor | Revisor(es) |
| --- | --- | --- | --- | --- |
| 14/09/2026 | 1.0 | Criação e estruturação do plano de custos unificado | [João Paulo Lima](https://github.com/jpaulohe4rt) | [Letícia Torres Soares Martins](https://github.com/leticiatmartins) ([PR #15](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/pull/15)) |
| 27/09/2026 | 1.1 | Adição do rateio de custo por release major (R1, R2, R3) com base nas datas do cronograma oficial | [João Paulo Lima](https://github.com/jpaulohe4rt) | [João Lucas Araújo Siqueira](https://github.com/jlucasiqueira) ([PR #44](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/pull/44)) |
| 21/10/2026 | 1.2 | Substituição do salário de mercado fictício pelo custo-hora real do estudante da UnB, adição do Custo por Story Point e reestruturação do EVM ágil para uso de dados reais de sprint (issue [#78](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/78)) | [João Paulo Lima](https://github.com/jpaulohe4rt) | |

---

## 1. Introdução

A gestão de custos é uma ferramenta fundamental para embasar as tomadas de decisão ao longo de um projeto, ajudando a prevenir gargalos, atrasos e outros desvios estruturais. Para alcançar esse objetivo, é indispensável construir uma estimativa orçamentária realista e executável. Seguindo as melhores práticas do PMBOK, o gerenciamento financeiro do projeto engloba desde o planejamento e as estimativas iniciais até o controle contínuo, garantindo que todas as entregas sejam concluídas dentro do valor previamente aprovado.

O **AnatoQuizUP** é uma plataforma educacional dedicada ao ensino e à aprendizagem de anatomia radiológica, voltada para estudantes, professores, profissionais e pesquisadores da saúde. Por combinar metodologias ativas, dinâmicas de gamificação e agentes de inteligência artificial, o projeto exige uma infraestrutura tecnológica robusta e uma equipe capacitada, o que torna o acompanhamento orçamentário vital para o seu sucesso.

---

## 2. Processos de Gerenciamento

O fluxo financeiro da plataforma foi estruturado em três etapas fundamentais: estimativa, consolidação do orçamento e controle de gastos.

### 2.1. Estimativa de Custos
Esta etapa consiste em prever todos os recursos monetários necessários para a execução das atividades propostas. O levantamento abrange tanto as horas de trabalho da equipe quanto os recursos de hardware e conectividade indispensáveis para o desenvolvimento.

### 2.2. Determinação do Orçamento
O orçamento total do projeto é calculado com base no custo mensal dos profissionais alocados, multiplicado pelo tempo de duração do desenvolvimento, somado aos custos operacionais e de infraestrutura.

---

## 3. Estimativas e Orçamento Consolidado

A previsão orçamentária engloba os custos diretos e indiretos necessários para manter a equipe operando durante os 4 meses previstos para a execução do projeto.

### 3.1. Custo com a Equipe

> **Reavaliação (v1.2):** a versão anterior deste plano precificava a equipe com um salário médio de mercado (R$ 4.500,00/mês), o que não reflete o custo real do projeto. Como a equipe é composta por estudantes da UnB, o custo de referência correto é o **custo-hora do estudante**, não um valor de mercado fictício — ainda que um integrante já trabalhe fora, o custo de oportunidade enquanto estudante é o que deve ser contabilizado.

- Como base, utiliza-se o custo médio anual por aluno em universidades federais apurado pelo MEC para o ano-base de 2023 (Painel do Censo da Educação Superior + plataforma Universidade 360°) e divulgado pelo Poder360 em 2025 (referência [5]): **R$ 52.533,00/ano**, ou **R$ 4.377,75/mês**.
- Esse valor é corrigido monetariamente pelo IPCA acumulado entre 2023 e 2026 (fator estimado de **1,13**, a ser validado pela equipe na calculadora de inflação do Banco Central já referenciada em §5 antes de cada nova revisão), resultando em um custo-aluno estimado de **R$ 4.939,84/mês** em 2026.
- Assumindo uma dedicação média de **20h/semana** (~86,6h/mês) por integrante — carga de trabalho esperada pela disciplina —, o **custo-hora do estudante** é:

  `CustoHora = R$ 4.939,84 ÷ 86,6h ≈ R$ 57,04/hora`

- Para os **13 integrantes** da equipe, o custo mensal com pessoal é:

  `CustoEquipeMensal = R$ 4.939,84 × 13 = R$ 64.217,92`

- Ao longo dos 4 meses de projeto, o investimento total em pessoal será de **R$ 256.871,68**.

### 3.1.1. Custo por Story Point

Para permitir o controle de valor agregado por sprint (ver §4), define-se o custo de uma história de usuário a partir do custo-hora do estudante. Seguindo a referência consolidada na disciplina de que um desenvolvedor júnior leva, em média, 8 horas para concluir um story point [6]:

`CustoPorSP = CustoHora × 8h = R$ 57,04 × 8 = R$ 456,32`

Esse valor só pode ser aplicado a partir do momento em que a equipe passar a registrar story points e velocity por sprint — o que ainda não ocorre (ver `docs/dashboards.md`, R1).

### 3.2. Infraestrutura de Hardware (Custo Não Recorrente)

Para garantir a performance no desenvolvimento da plataforma e no treinamento dos modelos de inteligência artificial, foi orçada a aquisição de computadores dedicados. Esse investimento é pontual e incide integralmente no primeiro mês.

- O equipamento padronizado para a equipe é o notebook **LOQ Intel Core i5-12450H (16GB, 512GB SSD, Linux, tela 15,6" FHD)**.
- Com um custo unitário de **R$ 4.047,99**, a aquisição para todos os 13 integrantes demanda um aporte de **R$ 52.623,87**.

### 3.3. Conectividade e Internet

Para suportar as atividades de pesquisa e o trabalho integrado da equipe, foi orçado um serviço de banda larga de alta qualidade, utilizando os valores da Oi, provedora bem avaliada na região do Distrito Federal.

- O plano básico de fibra ótica tem o custo mensal de **R$ 99,90** por pessoa.
- Para o grupo de 13 pessoas, isso representa **R$ 1.298,70** ao mês.
- No acumulado dos 4 meses, o custo com internet será de **R$ 5.194,80**.

### 3.4. Resumo de Despesas Mensais

| **Categoria** | **Mês 1** | **Mês 2** | **Mês 3** | **Mês 4** | **Total do Projeto** |
| --- | --- | --- | --- | --- | --- |
| **Equipe (custo-hora do estudante)** | R$ 64.217,92 | R$ 64.217,92 | R$ 64.217,92 | R$ 64.217,92 | **R$ 256.871,68** |
| **Hardware (Pagamento Único)** | R$ 52.623,87 | R$ 0,00 | R$ 0,00 | R$ 0,00 | **R$ 52.623,87** |
| **Internet** | R$ 1.298,70 | R$ 1.298,70 | R$ 1.298,70 | R$ 1.298,70 | **R$ 5.194,80** |
| **Orçamento Mensal** | **R$ 118.140,49** | **R$ 65.516,62** | **R$ 65.516,62** | **R$ 65.516,62** | **R$ 314.690,35** |

### 3.5. Custo por Release Major (R1, R2, R3)

O cronograma oficial da disciplina define três releases major, cujas datas-limite dividem o período de 18 semanas do projeto (10/08 a 14/12/2026). O custo recorrente (equipe + internet, R$ 262.066,48 no total) foi rateado proporcionalmente ao número de semanas de cada ciclo; o custo de hardware (R$ 52.623,87), por ser um investimento único realizado na primeira semana do projeto, foi integralmente atribuído à R1.

| Release | Período | Duração | Custo Recorrente | Custo Não Recorrente | Custo da Release |
| --- | --- | :---: | ---: | ---: | ---: |
| **R1** | 10/08 a 28/09/2026 | 7 semanas | R$ 101.914,74 | R$ 52.623,87 (hardware) | **R$ 154.538,61** |
| **R2** | 28/09 a 26/10/2026 | 4 semanas | R$ 58.236,99 | — | **R$ 58.236,99** |
| **R3** | 26/10 a 14/12/2026 | 7 semanas | R$ 101.914,74 | — | **R$ 101.914,74** |
| **Total** | | 18 semanas | R$ 262.066,47 | R$ 52.623,87 | **R$ 314.690,34** |

> R3 engloba também as duas semanas de encerramento do projeto (30/11 a 14/12), já que a disciplina não atribui peso orçamentário próprio a essa etapa de fechamento.

---

## 4. Controle e Monitoramento de Custos

O acompanhamento financeiro será realizado por meio da metodologia de Gerenciamento de Valor Agregado Ágil (Agile EVM). Essa prática permite monitorar o avanço real do AnatoQuizUP em relação ao que foi planejado, facilitando a atualização do orçamento e a gestão de eventuais mudanças na linha de base de custos.

> **Reavaliação (v1.2):** nas releases anteriores, os indicadores de desempenho (IDP/IDC) foram apresentados sem uma fórmula rastreável — não havia story points nem velocity registrados para alimentá-los (ver `docs/dashboards.md`, R1: "estimativas em pontos e histórico de burndown ainda não foram registrados"). A partir desta revisão, VP/VA/CR passam a ser derivados de dados reais de sprint usando o Custo por Story Point definido em §3.1.1, e só serão calculados quando essa coleta estiver em vigor (a partir da R2).

### 4.1. Pilares do Valor Agregado

- **Valor Planejado (VP):** `VP = pontos planejados para a sprint × CustoPorSP`. Representa o orçamento autorizado para o trabalho que deveria estar concluído até a data de acompanhamento.
- **Valor Agregado (VA):** `VA = pontos efetivamente concluídos na sprint × CustoPorSP`. Representa o valor orçado do trabalho efetivamente realizado.
- **Custo Real (CR):** Representa o custo efetivamente incorrido na execução do trabalho até a data de acompanhamento, apurado a partir das horas realmente dedicadas pela equipe (custo-hora × horas registradas), e não apenas do orçamento planejado.

### 4.2. Indicadores de Desempenho

Para entender a saúde do projeto de forma objetiva, utilizamos os seguintes indicadores:

**Variação de Prazos (VPR) e Variação de Custos (VC)**

- **VPR (`VA - VP`):** Indica, em termos de valor orçado do trabalho, se o projeto está adiantado (resultado > 0), conforme o planejado (resultado = 0) ou atrasado (resultado < 0).
- **VC (`VA - CR`):** Compara o valor orçado do trabalho realizado com seu custo real. Resultados positivos indicam economia; resultados iguais a zero indicam custo conforme o orçamento; resultados negativos indicam custo superior ao orçado para o trabalho realizado.

**Índices de Eficiência (IDP e IDC)**

- **Índice de Desempenho de Prazos (`IDP = VA / VP`):** Mede o desempenho do cronograma. Um índice maior que 1 indica avanço superior ao planejado; igual a 1, avanço conforme o planejado; menor que 1, avanço inferior ao planejado.
- **Índice de Desempenho de Custos (`IDC = VA / CR`):** Mede a eficiência no uso dos recursos. Um índice maior que 1 indica custo inferior ao orçado para o trabalho realizado; igual a 1, custo conforme o orçamento; menor que 1, custo superior ao orçado para o trabalho realizado.

Os índices devem considerar a mesma data de acompanhamento. O IDP não deve ser calculado quando o VP for zero, nem o IDC quando o CR for zero.

### 4.3. Matriz de Análise Geral

Cruzando os dados de prazo e orçamento, a coordenação do projeto utilizará a seguinte matriz para avaliar a situação do AnatoQuizUP:

| | Atrasado | No Prazo | Adiantado |
| :-: | :---------: | :-------: | :--------: |
| **Abaixo do Orçamento** | Requer investigação | Cenário Ideal | Cenário Ideal |
| **No Orçamento** | Cenário Ruim | Cenário Ideal | Cenário Ideal |
| **Acima do Orçamento** | Cenário Ruim | Cenário Ruim | Requer investigação |

---

## 5. Referências

* ALMEIDA, A. **5 Melhores Notebook para Programar em 2022**. Disponível em: <https://devporai.com.br/5-melhores-notebooks-para-programar/>.
* ANATEL. **Pesquisa de Satisfação e Qualidade**. Disponível em: <https://informacoes.anatel.gov.br/paineis/consumidor/pesquisa-de-satisfacao>.
* Banco Central do Brasil. **Calculadora de Ajuste de Inflação**. Disponível em: <https://www.bcb.gov.br>.
* OI. **Internet fibra ótica: planos de internet banda larga**. Disponível em: <https://www.oi.com.br/internet>.
* PMI. **Um guia do conhecimento em gerenciamento de projetos. Guia PMBOK** 6a. ed. - EUA: Project Management Institute, 2017.
* PMI. **Um guia do conhecimento em gerenciamento de Projetos (Guia PMBOK)**, Project Management Institute, 5ª Edição, Pennsylvania, Estados Unidos da América, 2013.
* PROJECT BUILDER; IBEC. **Gerenciando Custos em um Projeto**. [s.l: s.n.].
* [5] PODER360. **Alunos de universidades federais têm custo anual de R$ 52.533**. Publicado em 2025, com base em dados do MEC (Painel do Censo da Educação Superior e plataforma Universidade 360°) para o ano-base 2023. Disponível em: <https://www.poder360.com.br/poder-economia/alunos-de-universidades-federais-tem-custo-medio-anual-de-r-52-533/>. Valor-base utilizado em §3.1: R$ 52.533,00/ano (R$ 4.377,75/mês), custo médio nacional por aluno em universidade federal.
* [6] COHN, Mike. **Don't Equate Story Points to Hours**. Mountain Goat Software, 2024. Disponível em: <https://www.mountaingoatsoftware.com/blog/dont-equate-story-points-to-hours>.
