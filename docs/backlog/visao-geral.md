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
| Release Major 1 | Identidade do estudante (avatar) e loja virtual | [Release Major 1](release-major-1.md) |
| Release Major 2 | A definir após validação da R1 com os POs | — |
| Release Major 3 | A definir | — |

> **Base herdada:** o AnatoQuizUp é evoluído a partir do produto desenvolvido em 2026.1, que já possuía cadastro e autenticação, questões, quiz, turmas, listas, loja, inventário, conquistas e ranking. Este backlog registra o que é construído ou evoluído em 2026.2 e identifica as histórias herdadas.

## Padrão de escrita

**Histórias de usuário** seguem o formato:

```text
Como [persona]
Quero [ação ou necessidade]
Para [benefício esperado]
```

Os critérios de aceitação são escritos em **Gherkin** (Dado / Quando / Então) ou como checklist verificável.

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

1. **Valor para o estudante**: hipótese central do MVP de que a gamificação aumenta o engajamento.
2. **Dependência técnica**: itens que destravam outros vêm primeiro (ex.: avatar padrão antes da personalização).
3. **Esforço e risco**: riscos do [Plano de Riscos](../produto/plano-de-riscos.md), como curva de aprendizado e prazo.
4. **Retorno dos Product Owners**.

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
| Loja virtual com itens para o avatar | EP01 | US03 |
| Criação de listas de quizzes por professores | EP03 | US09 |
| Visualização dos resultados dos estudantes | EP03 | US10 |
| Validação de questões e imagens produzidas com apoio de IA | EP04 | US12 |
| Criação de casos clínicos baseados no modelo OSCE | EP05 | US13 |
| Simulação de consultas com pacientes virtuais | EP05 | US17 |
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
| US08 | estudante | revisar as questões que errei | focar nas minhas dificuldades | EP02 | Should | R2 | Não iniciada |
| US09 | professora | criar listas de questões e aplicá-las às turmas | usar a plataforma em sala de aula | EP03 | Must | R2 | Herdada de 2026.1 |
| US10 | professora | visualizar os resultados dos estudantes da turma | identificar dificuldades e ajustar minhas aulas | EP03 | Should | R2 | Herdada de 2026.1 |
| US11 | estudante | tirar dúvidas com um chatbot durante o estudo | resolver dúvidas sem depender do horário da professora | EP04 | Should | R3 | Não iniciada |
| US12 | professora | validar questões e imagens geradas com apoio de IA | garantir a qualidade do conteúdo | EP04 | Should | R3 | Não iniciada |
| US13 | estudante | praticar casos clínicos no modelo OSCE | treinar raciocínio clínico | EP05 | Could | R3 | Não iniciada |
| US14 | administradora | gerenciar usuários e permissões | manter o acesso à plataforma seguro | EP06 | Must | Contínuo | Herdada de 2026.1 |
| US15 | estudante | me cadastrar e acessar a plataforma com e-mail e senha | ter meu progresso salvo | EP06 | Must | Contínuo | Herdada de 2026.1 |
| US16 | estudante | escolher disciplina, tema e nível de conhecimento antes do quiz | estudar no ritmo e no conteúdo de que preciso | EP02 | Should | R2 | Não iniciada |
| US17 | estudante | simular consultas com pacientes virtuais | praticar a anamnese e o raciocínio clínico | EP05 | Could | R3 | Não iniciada |

> As histórias a partir da US04 são uma proposta inicial derivada da Lean Inception. As marcadas como "Herdada de 2026.1" já possuem implementação do semestre anterior e serão revisadas com os Product Owners para decidir se precisam de evolução. Todas serão refinadas, estimadas e receberão critérios de aceitação antes de entrarem em uma sprint.

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