# Backlog do Produto

## Objetivo

O backlog organiza tudo o que o AnatoQuizUp precisa entregar, do ponto de vista do usuário (**histórias de usuário**) e do time (**tarefas técnicas**), mantendo a rastreabilidade entre as funcionalidades levantadas na [Lean Inception](../produto/lean_inception.md), as releases do [Roadmap](../produto/roadmap.md), as issues do GitHub e os Pull Requests que as implementam.

O backlog é revisado ao final de cada sprint, considerando as entregas realizadas, os riscos materializados e o retorno dos Product Owners.

## Organização

| Nível | Descrição | Onde fica |
|---|---|---|
| **Épico** | Grande área de valor do produto, derivada da Lean Inception | Esta página |
| **História de usuário (US)** | Necessidade de uma persona, com critérios de aceitação | Esta página (visão geral) e página da release (detalhe) |
| **Tarefa técnica (TASK)** | Trabalho interno que sustenta uma ou mais US | Página da release |

| Release | Foco | Detalhamento |
|---|---|---|
| Release 1 | Identidade do estudante, avatar e loja virtual | [Release 1](release-major-1.md) |
| Release 2 | Ciclos de aprendizagem e gamificação, com base do acompanhamento pedagógico | A detalhar após refinamento com os Product Owners |
| Release 3 | Fechamento do ciclo da professora, curadoria e um piloto avançado | A detalhar após seleção do piloto com os Product Owners |

> **Base herdada:** o AnatoQuizUp é evoluído a partir do produto desenvolvido em 2026.1, que já possuía cadastro e autenticação, questões, quiz, turmas, listas, loja, inventário, conquistas e ranking. Este backlog registra o que é construído ou evoluído em 2026.2 e identifica as histórias herdadas.

## Recorte do MVP ampliado

Após a revisão do escopo, o MVP passou a abranger as **Ondas 1 a 4** do sequenciador e três ciclos de valor completos:

1. **Aprendizagem:** acessar, escolher tema e nível, responder quiz com imagem, receber explicação, revisar erros e acompanhar o próprio progresso.
2. **Gamificação:** concluir atividades, receber XP e moedas, cumprir missões, acompanhar o ranking, utilizar a loja e personalizar o avatar.
3. **Gestão pedagógica:** criar ou selecionar questões validadas, montar listas, aplicar às turmas e analisar os resultados.

Cadastro, autenticação, perfis, permissões, integração das funcionalidades herdadas e instrumentação das métricas são capacidades obrigatórias de apoio.

O MVP também prevê **um único piloto avançado**, ainda a ser selecionado com os Product Owners: caso OSCE pré-configurado ou chatbot contextual. Geração de questões com imagens, paciente virtual completo e execução simultânea dos dois pilotos permanecem fora do MVP atual.

O recorte visual está disponível no [Canvas MVP ampliado](https://www.figma.com/board/IwsqM1gCmdrS2ZrR8HgRGz/Vis%C3%A3o-do-Produto-AnatoQuizUP-2026-2?node-id=17425-2220).

## Padrão de escrita

**Histórias de usuário** seguem o formato:

```text
Como [persona]
Quero [ação ou necessidade]
Para [benefício esperado]
```

Os critérios de aceitação das histórias refinadas são escritos em **Gherkin** (Dado / Quando / Então); listas de cobertura registram status de implementação.

**Tarefas técnicas** descrevem um resultado verificável pelo time e possuem **critérios de conclusão** e **repositórios impactados**.

## Priorização

A prioridade segue a técnica **MoSCoW**:

| Prioridade | Significado |
|---|---|
| **Must** | Essencial para a release; sem ela a entrega não gera valor |
| **Should** | Importante, mas pode ser adiada sem comprometer a release |
| **Could** | Desejável, entra se houver capacidade |
| **Won't (agora)** | Fora do escopo da release atual |

Critérios considerados:

1. **Valor educacional**: o ciclo de aprendizagem precisa funcionar de ponta a ponta antes da ampliação dos recursos avançados.
2. **Fechamento do fluxo**: funcionalidades que permitem concluir os ciclos do estudante e da professora têm prioridade sobre recursos isolados.
3. **Dependência técnica**: itens que destravam outros vêm primeiro, como autenticação, permissões e registro de resultados.
4. **Esforço e risco**: riscos do [Plano de Riscos](../produto/plano-de-riscos.md), como curva de aprendizado, integração e prazo.
5. **Retorno dos Product Owners**.

## Épicos

| ID | Épico | Persona | Origem (Lean Inception) |
|---|---|---|---|
| **EP01** | Gamificação e identidade do estudante | Estudante | Avatar; pontos, moedas e ranking; loja virtual |
| **EP02** | Quizzes e aprendizagem | Estudante | Escolha de temas e nível; quizzes por tema; imagens radiológicas; explicações; revisão de erros |
| **EP03** | Gestão pedagógica | Professora | Listas de quizzes; resultados dos estudantes |
| **EP04** | Inteligência artificial | Estudante / Professora | Chatbot; explicações adaptativas; validação de conteúdo gerado por IA |
| **EP05** | Casos clínicos | Estudante | Casos OSCE; simulação com pacientes virtuais |
| **EP06** | Acesso e administração | Estudante / Professora / Administradora | Cadastro e autenticação; administração de usuários e permissões |

## Cobertura da Lean Inception

Todas as funcionalidades levantadas na Lean Inception estão associadas a um épico e a pelo menos uma história de usuário.

| Funcionalidade (Lean Inception) | Épico | História |
|---|---|---|
| Cadastro e autenticação de estudantes | EP06 | US15 |
| Escolha de disciplinas, temas e nível de conhecimento | EP02 | US16 |
| Resolução de quizzes organizados por tema | EP02 | US06 |
| Questões acompanhadas de imagens radiológicas | EP02 | US06 |
| Consulta às explicações das respostas | EP02 | US07 |
| Revisão de questões respondidas incorretamente | EP02 | US08 |
| Chatbot para esclarecimento de dúvidas | EP04 | US11 |
| Explicações adaptadas às dificuldades do estudante | EP04 | US11 |
| Criação e personalização de avatar | EP01 | US01, US02 |
| Pontos de experiência, moedas e ranking | EP01 | US03, US04, US05 |
| Missões diárias, semanais e mensais | EP01 | US18 |
| Loja virtual com itens para o avatar | EP01 | US03 |
| Visualização do próprio progresso | EP02 | US19 |
| Criação de listas de quizzes por professores | EP03 | US09 |
| Visualização dos resultados dos estudantes | EP03 | US10 |
| Validação de questões e imagens produzidas com apoio de IA | EP04 | US12 |
| Criação de casos clínicos baseados no modelo OSCE | EP05 | US13 |
| Simulação de consultas com pacientes virtuais | EP05 | US17 |
| Progressão de elo conforme XP acumulado | EP01 | US23 (#82) |
| Perda e recuperação de elo por inatividade | EP01 | US20 (#89) |
| Exibição consistente do avatar ativo | EP01 | US21 (#91) |
| Acesso visível à personalização do avatar | EP01 | US22 (#92) |
| Padronização de nomenclatura avatar/perfil (melhoria de UX) | EP01 | US01, US02, US21, US22 (#93) |
| Administração de usuários e permissões | EP06 | US14 |

## Backlog priorizado

| ID | Como | Quero | Para | Épico | Prioridade | Release | Status |
|---|---|---|---|---|---|---|---|
| US01 | estudante | possuir um avatar padrão | ter uma identidade na plataforma desde o primeiro acesso | EP01 | Must | R1 | Parcial |
| US02 | estudante | personalizar aparência, acessórios e roupas do meu avatar | me sentir representado e exibir os itens que conquistei | EP01 | Must | R1 | Parcial (Roupas adiada para a R2) |
| US03 | estudante | comprar e utilizar itens na loja virtual | usar minhas moedas para potencializar meu aprendizado | EP01 | Must | R1 | Concluída |
| US04 | estudante | ganhar pontos de experiência (XP) ao responder questões | acompanhar minha evolução | EP01 | Must | R2 | Repriorizada da R1 |
| US05 | estudante | ver minha posição no ranking geral, de amigos e da turma | me comparar com colegas e me manter engajado | EP01 | Should | R2 | Herdada de 2026.1 |
| US06 | estudante | responder quizzes por tema com imagens radiológicas | praticar anatomia aplicada à radiologia | EP02 | Must | R2 | Herdada de 2026.1 |
| US07 | estudante | ver a explicação da resposta após responder | entender o motivo do acerto ou erro | EP02 | Must | R2 | Herdada de 2026.1 |
| US08 | estudante | revisar as questões que errei | focar nas minhas dificuldades | EP02 | Must | R2 | Não iniciada |
| US09 | professora | criar listas de questões e aplicá-las às turmas | usar a plataforma em sala de aula | EP03 | Must | R2 | Herdada de 2026.1 |
| US10 | professora | visualizar os resultados dos estudantes da turma | identificar dificuldades e ajustar minhas aulas | EP03 | Must | R2 | Herdada de 2026.1 |
| US11 | estudante | tirar dúvidas com um chatbot durante o estudo | resolver dúvidas sem depender do horário da professora | EP04 | Should (piloto) | R3 | Candidato a piloto |
| US12 | professora | validar questões e imagens geradas com apoio de IA | garantir a qualidade do conteúdo | EP04 | Must | R3 | Não iniciada |
| US13 | estudante | praticar casos clínicos no modelo OSCE | treinar raciocínio clínico | EP05 | Should (piloto) | R3 | Candidato a piloto |
| US14 | administradora | gerenciar usuários e permissões | manter o acesso à plataforma seguro | EP06 | Must | Contínuo | Herdada de 2026.1 |
| US15 | estudante | me cadastrar e acessar a plataforma com e-mail e senha | ter meu progresso salvo | EP06 | Must | Contínuo | Herdada de 2026.1 |
| US16 | estudante | escolher disciplina, tema e nível de conhecimento antes do quiz | estudar no ritmo e no conteúdo de que preciso | EP02 | Must | R2 | Não iniciada |
| US17 | estudante | simular consultas com pacientes virtuais | praticar a anamnese e o raciocínio clínico | EP05 | Won't (MVP) | Incremento | Não iniciada |
| US18 | estudante | cumprir missões diárias, semanais e mensais | manter frequência e continuidade nos estudos | EP01 | Should | R2 | Não iniciada |
| US19 | estudante | visualizar meu progresso, resultados e temas com dificuldade | direcionar meus próximos estudos | EP02 | Must | R2 | Não iniciada |
| US20 | estudante | receber avisos de inatividade e recuperar um elo após voltar a estudar | manter uma rotina de estudos e continuar progredindo | EP01 | Should | R2 | Refinada (#89; depende de US23) |
| US21 | estudante | visualizar meu avatar ativo nas áreas que me representam | manter minha identidade visual consistente | EP01 | Should | Pós-validação R1 | Refinada (#91; vinculada a US01 e US02) |
| US22 | estudante | localizar a personalização do avatar na navegação principal | customizar minha identidade visual sem procurar pela interface | EP01 | Should | Pós-validação R1 | Refinada (#92; melhoria de UX #93) |
| US23 | estudante | evoluir de elo conforme o XP acumulado | acompanhar meu progresso e estabelecer objetivos | EP01 | Should | R2 | Proposta refinada (#82) |

> As histórias a partir da US04 são uma proposta derivada da Lean Inception e do MVP ampliado. As marcadas como "Herdada de 2026.1" já possuem implementação do semestre anterior e serão revisadas com os Product Owners para decidir se precisam de evolução. Somente um dos candidatos a piloto, US11 ou US13, deverá ser comprometido no MVP. Todas as histórias serão refinadas, estimadas e receberão critérios de aceitação antes de entrarem em uma sprint.

> As missões diárias da US18 fazem parte do escopo de gamificação da Release 2 definido no [Roadmap](../produto/roadmap.md). As regras diárias, o fluxo e o contrato estão em [Missões Diárias](../produto/missoes-diarias.md), validados pelo PO em 19/10/2026. A definição e o protótipo são tratados na [#83](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/83), e a implementação, na [#84](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/84). A extensão para missões semanais e mensais e a prioridade Should desta proposta ainda devem ser validadas com os Product Owners. A US19 trata do acompanhamento dos resultados e das dificuldades de aprendizagem. A US23 corresponde à progressão de elos da [#82](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/82), sem duplicar a história de ranking. As issues [#96](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/96) e [#97](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/97) são etapas técnicas da US11, não novas histórias.

## Legenda de status

| Status | Significado |
|---|---|
| Concluída | Todos os critérios de aceitação atendidos e integrados à `main` |
| Parcial | Parte das tarefas concluída; o restante está em andamento ou foi adiado |
| Repriorizada | Planejada para uma release e movida para outra |
| Herdada de 2026.1 | Funcionalidade já implementada no semestre anterior |
| Não iniciada | Ainda não iniciada |

## Definição de Pronto (DoR)

Uma história pode entrar em uma sprint quando:

- [ ] Está escrita no formato Como / Quero / Para.
- [ ] Possui critérios de aceitação verificáveis.
- [ ] Tem dependências identificadas.
- [ ] Tem protótipo no Figma, quando envolver interface.
- [ ] Foi discutida com o time na planning.

## Definição de Feito (DoD)

Uma história é considerada concluída quando:

- [ ] Todos os critérios de aceitação foram atendidos.
- [ ] O código foi revisado em Pull Request e integrado à `main`.
- [ ] O pipeline de CI passou (lint, build, testes e SonarCloud).
- [ ] A cobertura de testes se manteve em no mínimo 85%.
- [ ] A funcionalidade está disponível no ambiente de homologação.
- [ ] A issue foi fechada com link para os PRs.


## Histórico de Versão

| Data | Versão | Descrição | Autor(es) |
| :--- | :--- | :--- | :--- |
| 28/09/2026 | 1.0 | Criação do backlog do produto com épicos, cobertura da Lean Inception, histórias priorizadas, DoR e DoD | [Henrique Carvalho](https://github.com/henriquecarv3), [Rafael Melo](https://github.com/rmatuda) |
| 12/10/2026 | 1.1 | Alinhamento do backlog ao MVP ampliado, com ciclos completos, novas histórias e seleção de um piloto avançado | [Leticia Torres Soares](https://github.com/leticiatmartins) |
| 13/10/2026 | 1.2 | Inclusão da US19 (missões diárias) na Release 2, com referência às issues #83 e #84 | [Rafael Melo](https://github.com/rmatuda) |
| 18/10/2026 | 1.3 | Inclusão das US18 e US20–US22; vínculo das #96 e #97 à US11; preservação da US19 e registro da melhoria de UX #93 | [Letícia Torres](https://github.com/leticiatmartins) |
| 19/10/2026 | 1.4 | Registro da validação das regras da US19 (missões diárias) pelo PO | [Rafael Melo](https://github.com/rmatuda) e [Henrique Neves](https://github.com/henriquecarv3) |
