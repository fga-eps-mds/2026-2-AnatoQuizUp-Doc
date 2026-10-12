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
| **Release 2** | 28/09 a 25/10 | Ciclo de aprendizagem e progressão | Estudantes realizam quizzes por tema e nível, recebem feedback, revisam erros e acompanham o próprio progresso; XP, moedas, missões e ranking conectam estudo e gamificação. | Planejada / em execução |
| **Release 3** | 26/10 a 29/11 | Ciclo do professor e validação do MVP | Professores selecionam conteúdo validado, organizam listas, acompanham resultados e ajustam atividades; um piloto avançado é validado junto ao fluxo principal. | Planejada |

## Linha do tempo

| Período | Marco | Resultado |
| :--- | :--- | :--- |
| 10/08 | Kickoff e planejamento inicial | Alinhamento do problema, público e objetivos do semestre. |
| 17/08 a 27/09 | Release 1 | Fundação de identidade, avatar e loja. |
| 28/09 a 25/10 | Release 2 | Ciclo de aprendizagem integrado à progressão gamificada. |
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
- Execução de quiz com imagens radiológicas e questões previamente validadas.
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

| Data | Versão | Descrição | Autor(es) |
| :--- | :--- | :--- | :--- |
| [Data] | 1.0 | Criação do roadmap com base no escopo e replanejamento da Release 1 | [João Lucas](https://github.com/jlucasiqueira) |
| 12/10/2026 | 1.1 | Alinhamento das Releases 1, 2 e 3 ao MVP ampliado e inclusão de critérios e métricas | [Leticia](https://github.com/leticiatmartins) |
