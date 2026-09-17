# Plano de Gerenciamento de Custos - AnatoQuizUp

## Histórico de Revisões
| Data | Versão | Descrição | Autor |
|---|---|---|---|
| 14/09/2026 | 1.0 | Criação e estruturação do plano de custos unificado | [João Paulo Lima](https://github.com/jpaulohe4rt) | |

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
Para fins de precificação, os 13 integrantes da equipe foram alocados sob o perfil de Desenvolvedores Júnior.
* Considerando o mercado atual, adotou-se o salário médio de **R$ 4.500,00** mensais para cada profissional.
* Dessa forma, a folha de pagamento mensal da equipe de **13 desenvolvedores** totaliza **R$ 58.500,00**.
* Ao longo dos 4 meses de projeto, o investimento total em pessoal será de **R$ 234.000,00**.

### 3.2. Infraestrutura de Hardware (Custo Não Recorrente)
Para garantir a performance no desenvolvimento da plataforma e no treinamento dos modelos de inteligência artificial, foi orçada a aquisição de computadores dedicados. Esse investimento é pontual e incide integralmente no primeiro mês.
* O equipamento padronizado para a equipe é o notebook **LOQ Intel Core i5-12450H (16GB, 512GB SSD, Linux, tela 15,6" FHD)**.
* Com um custo unitário de **R$ 4.047,99**, a aquisição para todos os 13 integrantes demanda um aporte de **R$ 52.623,87**.

### 3.3. Conectividade e Internet
Para suportar as atividades de pesquisa e o trabalho integrado da equipe, foi orçado um serviço de banda larga de alta qualidade, utilizando os valores da Oi, provedora bem avaliada na região do Distrito Federal.
* O plano básico de fibra ótica tem o custo mensal de **R$ 99,90** por pessoa.
* Para o grupo de 13 pessoas, isso representa **R$ 1.298,70** ao mês.
* No acumulado dos 4 meses, o custo com internet será de **R$ 5.194,80**.

### 3.4. Resumo de Despesas Mensais

| **Categoria** | **Mês 1** | **Mês 2** | **Mês 3** | **Mês 4** | **Total do Projeto** |
| --- | --- | --- | --- | --- | --- |
| **Equipe (Dev. Júnior)** | R$ 58.500,00 | R$ 58.500,00 | R$ 58.500,00 | R$ 58.500,00 | **R$ 234.000,00** |
| **Hardware (Pagamento Único)** | R$ 52.623,87 | R$ 0,00 | R$ 0,00 | R$ 0,00 | **R$ 52.623,87** |
| **Internet** | R$ 1.298,70 | R$ 1.298,70 | R$ 1.298,70 | R$ 1.298,70 | **R$ 5.194,80** |
| **Orçamento Mensal** | **R$ 112.422,57** | **R$ 59.798,70** | **R$ 59.798,70** | **R$ 59.798,70** | **R$ 291.818,67** |

---

## 4. Controle e Monitoramento de Custos

O acompanhamento financeiro será realizado por meio da metodologia de Gerenciamento de Valor Agregado (EVM). Essa prática permite monitorar o avanço real do AnatoQuizUP em relação ao que foi planejado, facilitando a atualização do orçamento e a gestão de eventuais mudanças na linha de base de custos.

### 4.1. Pilares do Valor Agregado

* **Valor Planejado (VP):** Representa a parcela do orçamento que foi autorizada e designada para as atividades agendadas.
* **Valor Agregado (VA):** Reflete o orçamento associado ao trabalho que já foi efetivamente concluído pela equipe. É calculado multiplicando o VP pela porcentagem de conclusão da tarefa.
* **Custo Real (CR):** Demonstra o montante financeiro que já foi concretamente gasto durante a execução do trabalho.

### 4.2. Indicadores de Desempenho

Para entender a saúde do projeto de forma objetiva, utilizamos os seguintes indicadores:

**Variação de Prazos (VPR) e Variação de Custos (VC)**
* **VPR (`VA - VP`):** Indica, em termos financeiros, se o projeto está adiantado (resultado > 0) ou atrasado (resultado < 0) em relação ao cronograma.
* **VC (`VA - CR`):** Aponta se há déficit ou economia orçamentária. Resultados positivos indicam que o custo está abaixo do planejado, enquanto valores negativos apontam gastos excessivos.

**Índices de Eficiência (IDP e IDC)**
* **Desempenho de Prazos (`IDP = VA / VP`):** Mede a eficiência do cronograma. Um índice maior que 1 significa que a equipe está adiantada; menor que 1, que há atrasos.
* **Desempenho de Custos (`IDC = VA / CR`):** Mede a eficiência no uso dos recursos. Um IDC acima de 1 demonstra que as entregas estão custando menos do que o previsto; abaixo de 1, indica estouro do orçamento.

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
* O Globo. **Raio-X do custo por aluno nas universidades federais**. Publicado em 2016.