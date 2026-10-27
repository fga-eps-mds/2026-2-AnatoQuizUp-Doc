# Roadmap e Releases

## Objetivo

Este documento apresenta o planejamento incremental do AnatoQuizUp e relaciona cada release ao valor esperado para estudantes e professores. O roadmap considera o MVP ampliado após a revisão acadêmica, o sequenciador da Lean Inception e a necessidade de validar o produto como uma experiência educacional completa, e não apenas como um conjunto isolado de funcionalidades.

O planejamento deve ser revisado ao fim de cada sprint, considerando entregas realizadas, riscos, métricas coletadas, decisões dos Product Owners e feedback dos usuários.

## Diretrizes de planejamento

- O MVP é cumulativo: as entregas das Releases 1, 2 e 3 formam, juntas, a primeira versão validável do produto.
- As ondas 1 a 4 do sequenciador orientam o MVP. A onda 5 permanece como incremento posterior.
- O MVP deve fechar três ciclos de valor: aprendizagem do estudante, gamificação e acompanhamento do professor.
- Apenas um piloto avançado será incorporado ao MVP: **OSCE pré-configurado** ou **chatbot contextual**. A escolha depende de decisão dos Product Owners e de análise de viabilidade técnica.
- Funcionalidades herdadas somente são consideradas parte do MVP quando estiverem integradas, testadas e observáveis por métricas.

## Visão geral das releases

| Release | Período | Foco | Resultado esperado | Situação |
| :--- | :--- | :--- | :--- | :--- |
| **Release 1** | 17/08 a 27/09 | Identidade e base da gamificação | Usuários personalizam o avatar, acessam a loja e dispõem da fundação necessária para a progressão gamificada. | Concluída |
| **Release 2** | Desenvolvimento de 28/09 a 25/10; marco de entrega em 26/10 | Ciclo de aprendizagem e progressão | Estudantes realizam quizzes por tema e nível, recebem feedback, revisam erros e acompanham o próprio progresso; XP, moedas, missões e ranking conectam estudo e gamificação. | Em validação; critérios de saída pendentes |
| **Release 3** | 26/10 a 29/11 | Ciclo do professor e validação do MVP | Professores selecionam conteúdo validado, organizam listas, acompanham resultados e ajustam atividades; um piloto avançado é validado junto ao fluxo principal. | Planejada |

## Linha do tempo

| Período | Marco | Resultado |
| :--- | :--- | :--- |
| 10/08 | Kickoff e planejamento inicial | Alinhamento do problema, público e objetivos do semestre. |
| 17/08 a 27/09 | Release 1 | Fundação de identidade, avatar e loja. |
| 28/09 a 25/10; entrega em 26/10 | Release 2 | Ciclo de aprendizagem integrado à progressão gamificada; o dia 26/10 é o marco de apresentação e aceite, conforme a EAP. |
| 26/10 a 29/11 | Release 3 | Ciclo do professor, piloto avançado e estabilização do MVP. |
| 30/11 a 14/12 | Validação e encerramento | Avaliação das métricas, correções finais, documentação e apresentação dos resultados. |

## Release 1 — Identidade e base da gamificação

### Objetivo

Estabelecer a identidade do usuário e a base visual e transacional da experiência gamificada.

### Escopo

- Personalização e interação com o avatar.
- Compra, uso e gerenciamento de itens na loja.
- Estrutura necessária para associar recompensas ao perfil do usuário.

### Critérios de saída

- O usuário consegue visualizar e personalizar o avatar.
- O usuário consegue consultar a loja, adquirir itens permitidos e equipá-los.
- Os principais fluxos estão integrados e documentados.

### Resultado

A Release 1 foi concluída em **28/09/2026**, entregando o fluxo de loja e a personalização do avatar. A experiência de pontos de experiência (XP), inicialmente prevista nesta etapa, foi repriorizada para a Release 2 para que fosse integrada ao ciclo real de aprendizagem, em vez de permanecer como uma pontuação sem origem pedagógica clara.

## Release 2 — Aprendizagem e progressão

### Objetivo

Transformar as funcionalidades existentes em um ciclo completo de estudo, conectando atividade, feedback, revisão e progressão.

### Escopo do estudante

- Acesso autenticado e seleção de perfil.
- Seleção de tema e nível de dificuldade.
- Execução de quiz com questões previamente validadas. A restauração de imagens radiológicas foi retirada do recorte desta entrega.
- Feedback com resposta, explicação e indicação do erro.
- Revisão dos erros e acompanhamento do próprio progresso.

### Escopo de gamificação

- Concessão de XP e moedas por atividades concluídas.
- Missões associadas a comportamentos de aprendizagem.
- Ranking com critérios compreensíveis para o usuário.
- Integração das recompensas com a loja e o avatar.

### Base pedagógica do professor

- Seleção de questões validadas.
- Criação e atribuição de listas para turmas.
- Consulta inicial dos resultados individuais e coletivos.

### Critérios de saída

- Um estudante conclui o percurso do acesso até o feedback e a revisão sem interrupções críticas.
- XP, moedas e missões são gerados por ações educacionais verificáveis.
- Um professor consegue atribuir uma lista e consultar seu resultado.
- Eventos mínimos de produto são coletados para medir conclusão, acerto e retorno.

## Release 3 — Acompanhamento, piloto e validação

### Objetivo

Consolidar o ciclo do professor, melhorar a confiabilidade do conteúdo e validar o MVP com usuários representativos.

### Escopo

- Painel de resultados individuais e coletivos.
- Identificação dos tópicos com maior incidência de erro.
- Ajuste das atividades a partir dos resultados observados.
- Fluxo humano de aprovação e rejeição de conteúdo.
- Administração de perfis e permissões.
- Seleção e integração de **um** piloto avançado:
  - OSCE pré-configurado; **ou**
  - chatbot contextual de apoio ao estudo.
- Estabilização, acessibilidade essencial e correção dos principais problemas encontrados na validação.

### Critérios de saída

- O professor utiliza resultados reais para adaptar uma atividade ou lista.
- O conteúdo apresentado ao estudante possui situação de validação identificável.
- O piloto escolhido está integrado a um cenário de uso, com hipótese e métrica definidas.
- Os três ciclos do MVP funcionam de forma integrada e podem ser demonstrados de ponta a ponta.

### Planejamento de capacidade

Esta seção ajusta a capacidade da R3 com a vazão real registrada na [análise do dashboard da R2](../dashboard-r2.md). A unidade é **issue fechada no backlog central (repositório Doc) por semana completa de sprint**, sem story points, porque o projeto não os registra.

#### Histórico de vazão

Contagem por semana (segunda a domingo, horário de Brasília) na captura de issues usada pelo dashboard (26/10/2026):

| Release | Semanas | Fechamentos por semana | Total | Média semanal | Concentração na última semana |
| --- | ---: | --- | ---: | ---: | ---: |
| R1 (10/08 a 27/09) | 7 | 0 · 0 · 0 · 0 · 1 · 3 · 12 | 16 | 2,29 | 12 de 16 (75,0%) |
| R2 (28/09 a 25/10) | 4 | 4 · 0 · 2 · 27 | 33 | 8,25 | 27 de 33 (81,8%) |
| R1 + R2 | 11 | — | 49 | 4,45 | — |

O recorte da R1 começa em 10/08, como no dashboard, e não em 17/08, como na tabela de releases. Os fechamentos de 26/10 (dia parcial na captura) pertencem à R3 e não entram nas médias.

As duas releases concentraram a maior parte das entregas na última semana. Fora dessas semanas finais, o time fechou 10 issues em 9 semanas (1,11 por semana). Na R2, as três primeiras semanas somaram 6 fechamentos (2,00 por semana), valor próximo à média da R1.

#### Referência de planejamento

| Referência | Vazão | Justificativa |
| --- | ---: | --- |
| Mínima | 2,29 issues/semana | Média da R1, equivalente ao ritmo da R2 fora da última semana (2,00). Representa a entrega sem depender de um pico final. |
| Esperada | 4,45 issues/semana | Média das 11 semanas completas de R1 e R2. Inclui os dois picos de fim de release, mas os dilui no semestre. |
| Teto observado | 8,25 issues/semana | Média da R2, alcançada com 81,8% das entregas em uma semana. **Não é usada como base de planejamento**, porque não demonstrou ser sustentável. |

A faixa de planejamento adotada vai da referência mínima à esperada. A equipe efetiva considerada é a mesma da R2 (11 integrantes, conforme o [plano de custos](plano-de-custos.md)), com sprints de uma semana.

#### Capacidade da R3

A R3 vai de 26/10 a 29/11, o que corresponde a **5 semanas completas de sprint**. Valores arredondados para baixo:

| Referência | Cálculo | Capacidade da R3 |
| --- | --- | ---: |
| Mínima | 2,29 × 5 = 11,45 | **11 issues** |
| Esperada | 4,45 × 5 = 22,27 | **22 issues** |
| Teto observado (não planejado) | 8,25 × 5 = 41,25 | 41 issues |

A capacidade planejada da R3 é, portanto, de **11 a 22 issues fechadas no backlog central**.

#### Comparação com o backlog

O backlog da R3 **ainda não está decomposto em issues**: a [visão geral do backlog](../backlog/visao-geral.md) registra que a R3 está "a detalhar após seleção do piloto com os Product Owners". Por isso, a demanda abaixo é contada em **frentes de trabalho**, e não em issues. Uma frente pode gerar várias issues e uma história de usuário pode depender de várias frentes.

| Origem | Frentes | Prioridade registrada |
| --- | --- | --- |
| Escopo da R3 neste roadmap | 1. Painel de resultados individuais e coletivos; 2. Tópicos com maior incidência de erro; 3. Ajuste de atividades a partir dos resultados; 4. Fluxo humano de aprovação de conteúdo (US12); 5. Administração de perfis e permissões (US14); 6. Um piloto avançado (US11 **ou** US13); 7. Estabilização e acessibilidade essencial | Must, exceto o piloto (Should) |
| Pendências da R2 ([backlog da R2](../backlog/release-2.md)) | 8. Revisão focada em erros (US08); 9. Conferência da escolha por disciplina (US16); 10. Missões semanais, já em PR (US18); 11. Agendamento da verificação de inatividade (US20/US23); 12. Instrumentação das métricas de produto; 13. Validação integrada da R2 em homologação | Must (8, 9, 12 e 13) e Should (10 e 11) |

São **13 frentes** para uma capacidade de 11 a 22 issues. Mesmo na hipótese mínima de uma issue por frente, a demanda já supera a capacidade mínima (13 > 11) e ocupa mais da metade da capacidade esperada (13 de 22). Como várias frentes envolvem Web, BFF e serviço, a hipótese de uma issue por frente é otimista. **O escopo atual cabe na capacidade esperada somente se as frentes forem decompostas de forma enxuta e as entregas forem distribuídas ao longo das sprints.**

#### Decisão sobre o escopo

| Situação | Itens | Estado |
| --- | --- | --- |
| Mantidos | Frentes Must da R3 (1 a 5 e 7) e pendências Must da R2 (8, 9, 12 e 13), pois sustentam os critérios de saída da R2 e da R3 | Compromisso já registrado neste roadmap |
| Limitado a um item | Piloto avançado: OSCE (US13) **ou** chatbot (US11), nunca os dois | Já previsto em [Fora do MVP](#fora-do-mvp); escolha pendente dos POs |
| Mantidos se a capacidade permitir | Missões semanais (US18) e agendamento de inatividade (US20/US23), que já têm implementação em PR e exigem principalmente revisão e homologação | Proposta da equipe, pendente de aprovação |
| Propostos para adiamento | US21 e US22 (avatar na navegação, Should, pós-validação da R1) e missões mensais (sem aprovação conhecida) | **Proposta pendente de aprovação dos POs** |

Se, ao fim da segunda sprint, a vazão estiver próxima da referência mínima, o primeiro corte proposto é o dos itens Should restantes, preservando o piloto escolhido e os critérios de saída. Qualquer retirada segue a [governança de mudanças](#governanca-de-mudancas).

**Pendências para concluir o planejamento:**

1. Os POs escolherem o piloto avançado. Sem essa decisão, a frente 6 não pode ser decomposta.
2. A equipe decompor as 13 frentes em issues no backlog central e repetir a comparação com a faixa de 11 a 22 issues.
3. Os POs decidirem sobre os adiamentos propostos acima.

#### Riscos e acompanhamento

- **Tamanho das issues:** a contagem não mede esforço. Uma issue de documentação e uma de integração entre serviços valem o mesmo.
- **Repositórios de código fora da conta:** a vazão mede apenas o repositório Doc (documentação, DevOps e histórias). PRs e issues dos repositórios Web, BFF, Quiz-Service e Usuario-Service não estão incluídos.
- **Superestimação pela R2:** a média de 8,25 resulta de um pico final. Repetir esse padrão na R3 deixaria pouco tempo para a validação do MVP, prevista logo depois, de 30/11 a 14/12.
- **Dados de coleta:** a exportação das métricas ainda depende de merge ou acionamento manual ([#122](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/122)), o que pode atrasar a leitura semanal.

Metas intermediárias propostas, calculadas a partir da referência mínima (2,29 issues por semana, acumulado arredondado para baixo):

| Sprint | Período | Fechamentos acumulados mínimos |
| --- | --- | ---: |
| 1 | 26/10 a 01/11 | 2 |
| 2 | 02/11 a 08/11 | 4 |
| 3 | 09/11 a 15/11 | 6 |
| 4 | 16/11 a 22/11 | 9 |
| 5 | 23/11 a 29/11 | 11 |

A cada review de sprint, a equipe compara os fechamentos acumulados com essa tabela. Uma sprint sem fechamentos, ou mais de 40% dos fechamentos previstos deixados para a última sprint, aciona a repriorização descrita acima.

## Métricas de validação

| Ciclo | Métrica | Pergunta respondida |
| :--- | :--- | :--- |
| Aprendizagem | Taxa de conclusão dos quizzes | Os estudantes conseguem terminar a atividade? |
| Aprendizagem | Acerto inicial comparado ao acerto na revisão | O feedback e a revisão contribuem para melhorar o desempenho? |
| Retenção | Usuários ativos e retorno semanal | Os estudantes voltam a utilizar a plataforma? |
| Professor | Listas atribuídas e concluídas | O fluxo de acompanhamento está sendo utilizado? |
| Professor | Tópicos com maior incidência de erro | Os resultados ajudam a orientar novas atividades? |
| Conteúdo | Questões aprovadas e rejeitadas | A curadoria humana está funcionando? |
| Gamificação | Uso de XP, moedas, missões, ranking, loja e avatar | A progressão incentiva participação sem se desconectar da aprendizagem? |

## Fora do MVP

Os itens abaixo permanecem no roadmap do produto, mas não fazem parte do compromisso mínimo deste semestre:

- geração de imagens da onda 5;
- paciente virtual completo e geração aberta de casos;
- entrega simultânea de OSCE e chatbot como pilotos avançados;
- filtro por tipo de questão;
- expansões que não contribuam diretamente para os três ciclos de valor ou para a validação das hipóteses do MVP.

## Governança de mudanças

Mudanças que alterem o compromisso do MVP devem registrar: motivação, impacto nas releases, responsáveis, riscos, critério de aceite e decisão dos Product Owners. A inclusão de um item requer a retirada ou a repriorização explícita de outro quando houver impacto na capacidade da equipe.

A visão visual do recorte aprovado está no [Canvas MVP ampliado no FigJam](https://www.figma.com/board/IwsqM1gCmdrS2ZrR8HgRGz/Vis%C3%A3o-do-Produto-AnatoQuizUP-2026-2?node-id=17425-2220).

## Histórico de Versão

| Data | Versão | Descrição | Autor(es) | Revisor(es) |
| --- | --- | --- | --- | --- |
| 28/09/2026 | 1.0 | Criação do roadmap com base no escopo e replanejamento da Release 1 | [João Lucas](https://github.com/jlucasiqueira) | [Henrique Carvalho](https://github.com/henriquecarv3) ([PR #49](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/pull/49)) |
| 12/10/2026 | 1.1 | Alinhamento das Releases 1, 2 e 3 ao MVP ampliado e inclusão de critérios e métricas | [Leticia](https://github.com/leticiatmartins) | [Rafael Melo](https://github.com/rmatuda) ([PR #87](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/pull/87)) |
| 26/10/2026 | 1.2 | Planejamento de capacidade da R3 com a vazão real da R1 e da R2 | [Rafael Melo](https://github.com/rmatuda) | |