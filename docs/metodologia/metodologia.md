# Metodologia

## Objetivo

Este documento descreve a **metodologia** de desenvolvimento escolhida pelo grupo e como ela define nossa orientação de trabalho, ritmo de entregas, papéis bem definidos, entre outros fatores.
> Seguir uma metodologia de desenvolvimento de software é fundamental para o sucesso dos projetos. No entanto, não basta escolher uma e começar a trabalhar, é preciso considerar qual modelo se adequará melhor às habilidades da sua equipe, ao estilo de trabalho e às necessidades do projeto.[1]
---

## Metodologia adotada: Ágil com adaptações(Scrum + Kanban + XP)

O time aplica uma metodologia focada no **Ágil** onde:

- Do **Scrum**, herdamos o ritmo de iterações curtas, os eventos(Sprint, Sprint Plannin, Daily Assincrona e Sprint Review), os papéis de (Product Owner, Scrum Master e Developers) e o compromisso com entregas incrementais a cada sprint.
- Do **Kanban**, herdamos o fluxo visual contínuo de tarefas em um quadro e a transparência sobre o estado de cada item.
- Do **XP**, herdamos principalmente o pair programming, alem da integração e refatoração contínuas.

### Por que e como foi escolhido?

Foi realizado um heatmap na primeira semana da disciplina para identificar os horarios de trabalho do time. Ele pode ser encontrado aqui:

<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="100%" height="500" src="https://docs.google.com/spreadsheets/d/1vzA4bEQm_K49IRhpzVkVF_C3KajeAwC8VPWL_7339H8/edit?usp=sharing" allowfullscreen></iframe>

Ele tambem pode ser encontrado aqui:

[Abrir Heatmap](https://docs.google.com/spreadsheets/d/1vzA4bEQm_K49IRhpzVkVF_C3KajeAwC8VPWL_7339H8/edit?usp=sharing)

Como pode ser observado, os horarios semelhantes de trabalho ficam para o periodo da noite, porem ainda é dificil conciliar ou dar certeza de trabalho diario dado a divergencia de rotinas ou imprevisibilidade.

| Características do time | Inferencia da metodologia no time |
|---|---|
| Time com 11 integrantes, 100% remoto, agendas dificeis de conciliar | O Scrum puro exigiria sincronia diária inviável; o Kanban puro perderia o ritmo necessário para uma disciplina com prazos fechados. Scrumban concilia ritmo previsível com flexibilidade assíncrona. |
| Múltiplas frentes paralelas (backend, frontend, documentação e DevOps) com dependências cruzadas | Quadro Kanban permite organizar melhor multiplas frentes de trabalho mesmo que elas sejam dependentes em algum momento ou não; Permite melhor visualização dessas frentes de trabalho |
| Stakeholders externos (Product Owners) com janelas de validação restritas | Sprints curtas (1 semana) garantem ciclos de feedback rápidos, mantendo o PO próximo do produto. |
| Objetivo pedagógico de exercitar todos os papéis ágeis | Rotatividade de funções a cada sprint é compatível com o caráter incremental do Scrumban. |
| Diversas Stacks trabalhadas ao mesmo tempo(Js, python, infra , docs) | Com o XP podemos realizar pareamentos adequados para juntar membros que dominam mais a tecnologia com o que menos domina e assim terem uma troca de conhecimento alem de não atrapalharem os prazos estabelecidos |
---

## Valores e princípios ágeis aplicados

A metodologia se ancora no [Manifesto Ágil](https://agilemanifesto.org/iso/ptbr/manifesto.html). Cada valor se traduz em uma prática concreta no time:

| Valor ágil | Como o time aplica |
|---|---|
| **Indivíduos e interações** mais que processos e ferramentas | Reuniões síncronas semanais no Discord; decisões discutidas em canal aberto, não impostas por liderança fixa. |
| **Software em funcionamento** mais que documentação abrangente | Toda sprint deve produzir incremento integrado e deployado (Railway). Documentação acompanha o código, não o substitui. |
| **Colaboração com o cliente** mais que negociação de contratos | Reuniões periódicas com os Product Owners no Microsoft Teams; backlog é repriorizado de forma colaborativa, não congelado. |
| **Responder a mudanças** mais que seguir um plano | Backlog da release é revisto a cada sprint; itens podem ser repriorizados, divididos ou removidos quando o aprendizado da sprint anterior justifica. |

Princípios do manifesto especialmente enfatizados:

- **Entrega contínua de valor**: toda sprint termina com algo deployado e validável pelo PO.
- **Reflexão e ajuste em intervalos regulares**: retrospectiva semanal alimenta ações concretas na sprint seguinte.
- **Simplicidade**: o time prefere reduzir escopo a inflar processos. Cerimônias são enxutas; documentação só vive se for consultada.
- **Times auto-organizados**: sem hierarquia técnica fixa, cada sprint redistribui responsabilidades.

---

## Metodologia considerada

Dado as primeiras reuniões com os PO's, foi levantado varios recursos sobre Inteligencia Artificial e melhorias em gameficação que não sao stacks predominantes do time. Dado o risco e talvez possiveis insatisfações, foi pensado em utilizar uma metodologia voltada a protótipos onde o time poderia sempre testar coisas novas para aprendizado proprio e com o objetivo de satisfazer as expectativas dos PO's. Porem como o tempo da disciplina é pouco esse tipo de abordagem entregaria muito pouco e fazia o time ter muito retrabalho semanalmente então foi desconsiderado.

## Estrutura de papéis

### Product Owners (fixos, externos ao time de desenvolvimento)

São stakeholders externos à equipe de desenvolvimento, os clientes do produto final. Validam o produto, definem as prioridades a serem entregadas e participam das reuniões de revisão. Por serem externos, a comunicação é mediada pelo Scrum Master da sprint.

### Scrum Master (rotativo por sprint e feito em duplas)

Dois membros do time assumem o papel de SM por **sprint**. O tempo é relativamente curto porem faz todos exercitarem, buscar aprender sobre o produto semana a semana e terem mais contato com os PO's. São esponsabilidades do SM:

- Facilitar as cerimônias da sprint;
- Remover impedimentos levantados pelo time;
- Mediar a comunicação com os POs;
- Garantir que o quadro Kanban (ZenHub) reflita o estado real do trabalho;
- Iniciar Planning e Reviews;
- Mediar comunicação entre os membros do time;
- Dividir o trabalho adequadamente;

### Equipe de desenvolvimento (rotativo por sprint)

A cada sprint, todos os 11 integrantes podem migrar entre as frentes técnicas:

- **Frente Frontend** (React/Vite/FSD)
- **Frente Backend** (Node/Express/Prisma)
- **Frente Documentação** (MkDocs)
- **Frente DevOps/CI** (GitHub Actions, SonarCloud, deploy)
- **Frente de IA** (majoritariamente python)

A rotação total é deliberadamente pedagógica: ao final da release, todos os integrantes terão tido contato com todas as frentes, evitando silos de conhecimento e cumprindo o objetivo formativo da disciplina EPS.

---

## Cadência e cerimônias

A unidade de iteração é a **sprint** que tem duração de **uma semana**. As cerimônias são enxutas para caber no calendário acadêmico:
> Scrum combina quatro eventos formais para inspeção e adaptação, contidos dentro de um
evento, a Sprint. Esses eventos funcionam porque implementam os pilares empíricos do
Scrum: transparência, inspeção e adaptação.[2]

| Cerimônia | Frequência | Duração-alvo | Participantes | Objetivo |
|---|---|---|---|---|
| **Sprint Planning** | Início da sprint | ~1h | Time + SM | Selecionar itens do backlog da release, definir meta da sprint e distribuir frentes. |
| **Reunião com POs** | 1x por sprint | ~1:30h | SM + POs (time observa) | Apresentar incremento da sprint anterior, validar prioridades e capturar feedback. |
| **Sprint Review** | Fim da sprint | ~1h | Time + SM | Demonstrar o que foi entregue e medir aderência à meta da sprint. |
| **Retrospectiva** | Fim da sprint | ~1h | Time + SM | Identificar o que manter, o que mudar e definir 1–2 ações concretas para a próxima sprint. |
| **Sincronização assíncrona** | Diariamente | Contínua | Time + SM | Substitui a daily formal. Atualizações de progresso e bloqueios via WhatsApp (interna) e Discord (com POs). |

> **Por que sem daily síncrona?** O custo de sincronizar 11 agendas diariamente em um time remoto e acadêmico é alto e o ganho é baixo: o quadro ZenHub e os canais assíncronos já dão visibilidade do progresso. A sincronia é reservada para os momentos de maior valor (planning, review, retro, reunião com PO). A daily acontece de forma **assíncrona e diária** pelos canais do time.

---

## Fluxo de trabalho (Kanban)

O fluxo de cada item segue um quadro Kanban no **ZenHub** (integrado ao GitHub). Estados típicos:

1. **Backlog**: itens da release ainda não puxados para a sprint.
2. **Sprint Backlog**: itens comprometidos para a sprint atual.
3. **Em Andamento**: alguém está ativamente trabalhando.
4. **Em Revisão**: PR aberto aguardando code review.
5. **Concluído**: merge na `main` + DoD atendida.

---

## Ferramentas de apoio

| Ferramenta | Uso |
|---|---|
| **GitHub** | Repositórios, issues, Pull Requests e CI (GitHub Actions). |
| **ZenHub** | Quadro Kanban da sprint, conectado às issues do GitHub. Fonte única da verdade sobre o estado do trabalho. |
| **WhatsApp** | Comunicação interna rápida e assíncrona apenas entre os 11 membros do time. |
| **Discord** | Reuniões síncronas internas do time (planning, review, retro) e comunicação assíncrona com os POs. |
| **Microsoft Teams** | Reuniões síncronas com os Product Owners. |

---

## Referências para práticas operacionais

Os documentos abaixo descrevem **métodos** específicos e padrões técnicos invocados por esta metodologia:

- [Política de Branches](../contribuicao/politica_branchs.md): modelo Git Flow adotado.
- [Política de Commits](../contribuicao/politica_commits.md): Conventional Commits.
- [Código de Conduta](../contribuicao/codigo_conduta.md): combinados de convivência.
- [Matriz de Riscos](riscos.md): riscos monitorados a cada sprint.
- [Comunicação](comunicacao.md): canais, periodicidade e regras de uso.

---

## Histórico de Versão

| Data | Versão | Descrição | Autor(es) | Reviso(es) |
|---|---|---|---|---|
| 18/09/2026 | 1.0 | Definição das Metodologias utilizadas, Definição dos papeis, Eventos e fluxo de trabalho | [Gabriel Freitas](https://github.com/gabrielfreitass1) | --- |


## Referencias 
- [1] https://monday.com/blog/pt/desenvolvimento/metodologias-de-desenvolvimento-de-software/
- [2] O Guia Definitivo para o Scrum: As Regras do Jogo, Ken Schwaber e Jeff Sutherland, 2020.
