# Metodologia

## Objetivo

Este documento descreve a **metodologia** de desenvolvimento escolhida pelo grupo e como ela define nossa orientação de trabalho, ritmo de entregas, papéis bem definidos, entre outros fatores.
> Seguir uma metodologia de desenvolvimento de software é fundamental para o sucesso dos projetos. No entanto, não basta escolher uma e começar a trabalhar, é preciso considerar qual modelo se adequará melhor às habilidades da sua equipe, ao estilo de trabalho e às necessidades do projeto.
---

## Metodologia adotada: Ágil com adaptações(Scrum + Kanban + XP)

O time aplica uma metodologia focada no **Ágil** onde:

- Do **Scrum**, herdamos o ritmo de iterações curtas, as cerimônias de planejamento e revisão, os papéis (Product Owner e Scrum Master) e o compromisso com entregas incrementais a cada sprint.
- Do **Kanban**, herdamos o fluxo visual contínuo de tarefas em um quadro e a transparência sobre o estado de cada item.
- Do **XP**, herdamos principalmente o pair programming, alem da integração e refatoração contínuas.

### Por que e como foi escolhido?

Foi realizado um heatmap na primeira semana da disciplina para identificar os horarios de trabalho do time. Ele pode ser encontrado aqui:

<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="100%" height="500" src="https://docs.google.com/spreadsheets/d/1vzA4bEQm_K49IRhpzVkVF_C3KajeAwC8VPWL_7339H8/edit?usp=sharing" allowfullscreen></iframe>

Se preferir abrir direto no Figma:

[Abrir Heatmap](https://docs.google.com/spreadsheets/d/1vzA4bEQm_K49IRhpzVkVF_C3KajeAwC8VPWL_7339H8/edit?usp=sharing)

Dado que sa
| Característica do projeto | Implicação na metodologia |
|---|---|
| Time acadêmico (13 integrantes), 100% remoto, com agendas heterogêneas | O Scrum puro exigiria sincronia diária inviável; o Kanban puro perderia o ritmo necessário para uma disciplina com prazos fechados. Scrumban concilia ritmo previsível com flexibilidade assíncrona. |
| Múltiplas frentes paralelas (backend, frontend, documentação e DevOps) com dependências cruzadas | Quadro Kanban único dá visibilidade a bloqueios entre frentes; sprints curtas forçam integração frequente. |
| Stakeholders externos (Product Owners) com janelas de validação restritas | Sprints curtas (1 semana) garantem ciclos de feedback rápidos, mantendo o PO próximo do produto. |
| Objetivo pedagógico de exercitar todos os papéis ágeis | Rotatividade de funções a cada sprint é compatível com o caráter incremental do Scrumban. |

---

## Valores e princípios ágeis aplicados

A metodologia se ancora no [Manifesto Ágil](https://agilemanifesto.org/iso/ptbr/manifesto.html). Cada valor se traduz em uma prática concreta no time:

| Valor ágil | Como o time aplica |
|---|---|
| **Indivíduos e interações** mais que processos e ferramentas | Reuniões síncronas semanais no Discord; decisões discutidas em canal aberto, não impostas por liderança fixa. |
| **Software em funcionamento** mais que documentação abrangente | Toda sprint deve produzir incremento integrado e deployado (Vercel + Railway). Documentação acompanha o código, não o substitui. |
| **Colaboração com o cliente** mais que negociação de contratos | Reuniões periódicas com os Product Owners no Microsoft Teams; backlog é repriorizado de forma colaborativa, não congelado. |
| **Responder a mudanças** mais que seguir um plano | Backlog da release é revisto a cada sprint; itens podem ser repriorizados, divididos ou removidos quando o aprendizado da sprint anterior justifica. |

Princípios do manifesto especialmente enfatizados:

- **Entrega contínua de valor**: toda sprint termina com algo deployado e validável pelo PO.
- **Reflexão e ajuste em intervalos regulares**: retrospectiva semanal alimenta ações concretas na sprint seguinte.
- **Simplicidade**: o time prefere reduzir escopo a inflar processos. Cerimônias são enxutas; documentação só vive se for consultada.
- **Times auto-organizados**: sem hierarquia técnica fixa, cada sprint redistribui responsabilidades.

---

## Práticas de Engenharia (Extreme Programming - XP)

Para complementar a gestão e garantir a qualidade técnica e de código, a equipe utiliza conceitos do **Extreme Programming (XP)**:

- **Pareamento (Pair Programming):** Realizado para nivelar o conhecimento da equipe, reduzir a chance de bugs e disseminar as regras de negócio em todas as frentes.
- **Integração Contínua (CI):** Validação constante do código integrado por meio de pipelines de verificação de testes, lint e build.
- **Refatoração Contínua:** Melhoria orgânica do código sem alteração do escopo do comportamento original.

---

## Estrutura de papéis

### Product Owners (fixos, externos ao time de desenvolvimento)

São stakeholders externos à equipe de desenvolvimento. Validam o produto, definem prioridades de release e participam das reuniões de revisão. Por serem externos, a comunicação é mediada pelo Scrum Master da sprint.

### Scrum Master (rotativo por sprint e feito em duplas)

Um membro do time assume o papel de SM por **duas sprints consecutivas** (≈ 2 semanas). É a janela mais longa entre os papéis rotativos para garantir continuidade no acompanhamento de impedimentos e na interlocução com os POs. Responsabilidades:

- Facilitar as cerimônias da sprint.
- Remover impedimentos levantados pelo time.
- Mediar a comunicação com os POs.
- Garantir que o quadro Kanban (ZenHub) reflita o estado real do trabalho.

### Equipe de desenvolvimento (integrantes, rotação total por sprint)

A cada sprint, todos os 9 integrantes podem migrar entre as frentes técnicas:

- **Frente Frontend** (React/Vite/FSD)
- **Frente Backend** (Node/Express/Prisma)
- **Frente Documentação** (MkDocs)
- **Frente DevOps/CI** (GitHub Actions, SonarCloud, deploy)

A rotação total é deliberadamente pedagógica: ao final da release, todos os integrantes terão tido contato com todas as frentes, evitando silos de conhecimento e cumprindo o objetivo formativo da disciplina EPS.

> A equipe iniciou o projeto com 12 integrantes e, ao longo das releases (12 → 10 → 9), passou a contar com 9 integrantes ativos. A rotação de papéis e o pareamento foram reforçados para absorver a redução sem criar silos de conhecimento.

---

## Cadência e cerimônias

A unidade de iteração é a **sprint de 1 semana**. As cerimônias são enxutas para caber no calendário acadêmico:

| Cerimônia | Frequência | Duração-alvo | Participantes | Objetivo |
|---|---|---|---|---|
| **Sprint Planning** | Início da sprint | ~1h | Time + SM | Selecionar itens do backlog da release, definir meta da sprint e distribuir frentes. |
| **Reunião com POs** | 1x por sprint | ~1h | SM + POs (time observa) | Apresentar incremento da sprint anterior, validar prioridades e capturar feedback. |
| **Sprint Review** | Fim da sprint | ~30min | Time + SM | Demonstrar o que foi entregue e medir aderência à meta da sprint. |
| **Retrospectiva** | Fim da sprint | ~30min | Time + SM | Identificar o que manter, o que mudar e definir 1–2 ações concretas para a próxima sprint. |
| **Sincronização assíncrona** | Diariamente | Contínua | Time | Substitui a daily formal. Atualizações de progresso e bloqueios via WhatsApp (interna) e Discord (com POs). |

> **Por que sem daily síncrona?** O custo de sincronizar 9 agendas diariamente em um time remoto e acadêmico é alto e o ganho é baixo: o quadro ZenHub e os canais assíncronos já dão visibilidade do progresso. A sincronia é reservada para os momentos de maior valor (planning, review, retro, reunião com PO). A daily acontece de forma **assíncrona e diária** pelos canais do time.

---

## Fluxo de trabalho (Kanban)

O fluxo de cada item segue um quadro Kanban no **ZenHub** (integrado ao GitHub). Estados típicos:

1. **Backlog**: itens da release ainda não puxados para a sprint.
2. **Sprint Backlog**: itens comprometidos para a sprint atual.
3. **Em Andamento**: alguém está ativamente trabalhando.
4. **Em Revisão**: PR aberto aguardando code review.
5. **Concluído**: merge na `main` + DoD atendida.

*(Nota: O diagrama visual foi simplificado para lista para evitar quebras de conflito)*

---

## Ferramentas de apoio

| Ferramenta | Uso |
|---|---|
| **GitHub** | Repositórios, issues, Pull Requests e CI (GitHub Actions). |
| **ZenHub** | Quadro Kanban da sprint, conectado às issues do GitHub. Fonte única da verdade sobre o estado do trabalho. |
| **WhatsApp** | Comunicação interna rápida e assíncrona apenas entre os 12 membros do time. |
| **Discord** | Reuniões síncronas internas do time (planning, review, retro) e comunicação assíncrona com os POs. |
| **Microsoft Teams** | Reuniões síncronas com os Product Owners. |

---

## Referências para práticas operacionais

Os documentos abaixo descrevem **métodos** específicos e padrões técnicos invocados por esta metodologia:

- [Política de Branches](../contribuicao/politica_branchs.md): modelo Git Flow adotado.
- [Política de Commits](../contribuicao/politica_commits.md): Conventional Commits.
- [Código de Conduta](../contribuicao/codigo_conduta.md): combinados de convivência.
- [Métricas e Qualidade](../qualidade/qualidade.md): CI, cobertura mínima e SonarCloud.
- [Matriz de Riscos](riscos.md): riscos monitorados a cada sprint.
- [Comunicação](comunicacao.md): canais, periodicidade e regras de uso.
- [Acompanhamento de Sprints](sprints.md): registros e métricas (EVM) de cada sprint.

---

## Histórico de Versão

| Data | Versão | Descrição | Autor(es) |
|---|---|---|---|
| 27/04/2026 | 1.0 | Criação da metodologia, fluxo de desenvolvimento e Definition of Done | [Miguel Moreira](https://github.com/miguelmsoliveira) |
| 03/05/2026 | 2.0 | Reescrita com foco em metodologia (Scrumban, valores ágeis, papéis, cadência); práticas operacionais movidas para documentos próprios | [Miguel Moreira](https://github.com/miguelmsoliveira) |
| 04/05/2026 | 2.1 | Adição do XP nas abordagens de trabalho | [Genilson Junior](https://github.com/GenilsonJrs) |
| 02/06/2026 | 2.2 | Atualização da composição da equipe (12 → 9 integrantes), ajuste das frentes de trabalho e detalhamento da daily assíncrona | [Miguel Moreira](https://github.com/EhOMiguel) |

## Referencias 
https://monday.com/blog/pt/desenvolvimento/metodologias-de-desenvolvimento-de-software/
