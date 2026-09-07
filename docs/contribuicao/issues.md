# Política de Issues

## 1. Objetivo

Esta política estabelece as diretrizes para criação, organização e acompanhamento de **Issues** no projeto.

O objetivo é padronizar o registro das demandas da equipe, facilitar o acompanhamento das atividades e garantir a rastreabilidade entre os requisitos, tarefas, problemas identificados e alterações realizadas no repositório.

Cada Issue deve representar uma demanda clara e identificável, permitindo que os integrantes da equipe compreendam o que precisa ser realizado e acompanhem seu progresso.

## 2. Criação de Issues

Antes de criar uma nova Issue, deve-se verificar se já existe uma Issue relacionada ao mesmo assunto, evitando a duplicação de demandas.

Uma Issue deve apresentar informações suficientes para que a atividade possa ser compreendida e executada pela equipe.

Sempre que aplicável, a Issue deve conter:

* título objetivo;
* descrição da demanda;
* contexto ou justificativa;
* critérios de aceitação;
* responsável pela execução;
* Labels correspondentes;
* Milestone ou Sprint relacionada;
* referências ou Issues relacionadas.

## 3. Título

O título deve ser curto, objetivo e representar claramente a finalidade da Issue.

Deve-se evitar títulos genéricos que não permitam identificar a atividade.

### Exemplos

```text
Add question filtering
Fix authentication error
Create patient simulation screen
Update project documentation
```

Evitar:

```text
Bug
Problema
Alteração
Fazer tela
Arrumar código
```

Quando necessário, o tipo da demanda pode ser identificado por meio das **Labels**, evitando a necessidade de adicionar informações redundantes ao título.

## 4. Descrição

A descrição deve fornecer o contexto necessário para que outro integrante da equipe consiga compreender a demanda sem depender exclusivamente de explicações externas.

Recomenda-se utilizar uma estrutura semelhante a:

```markdown
## Descrição

Descrever de forma objetiva o que deve ser realizado.

## Contexto

Explicar o motivo ou problema que originou a demanda.

## Critérios de Aceitação

- [ ] Critério 1
- [ ] Critério 2
- [ ] Critério 3

## Observações

Informações adicionais relevantes para a execução da atividade.
```

Os critérios de aceitação devem ser utilizados principalmente quando a Issue representar uma funcionalidade ou atividade que possua condições específicas para ser considerada concluída.

## 5. Tipos de Issues

As Issues devem ser classificadas de acordo com sua finalidade.

Recomenda-se utilizar Labels para representar os diferentes tipos de demanda:

| Label           | Utilização                                                  |
| --------------- | ----------------------------------------------------------- |
| `feature`       | Desenvolvimento de uma nova funcionalidade                  |
| `bug`           | Identificação e correção de um comportamento incorreto      |
| `documentation` | Criação ou alteração de documentação                        |
| `enhancement`   | Melhoria de uma funcionalidade existente                    |
| `task`          | Atividade técnica ou operacional                            |
| `refactor`      | Alteração estrutural do código sem mudança de comportamento |

A equipe pode adicionar novas Labels quando houver necessidade de representar outros tipos de demanda.

## 6. Assignee

Sempre que uma Issue estiver pronta para execução, deve ser indicado um ou mais **Assignees** responsáveis pela atividade.

O responsável deve acompanhar a Issue durante sua execução e manter seu estado atualizado.

Quando houver mais de um integrante envolvido diretamente na implementação, os demais participantes podem ser adicionados como Assignees conforme a necessidade.

## 7. Labels

As Issues devem possuir Labels que permitam identificar sua natureza e facilitar sua organização.

As Labels devem ser utilizadas de maneira consistente em todo o projeto.

Exemplo:

```text
feature
documentation
priority-high
frontend
backend
```

Recomenda-se evitar a utilização excessiva de Labels que não acrescentem informações relevantes à Issue.

## 8. Milestones

Sempre que aplicável, a Issue deve ser associada à **Milestone** correspondente ao ciclo de desenvolvimento em que será executada.

Quando as Milestones forem utilizadas para representar Sprints, a Issue deve ser vinculada à Sprint correspondente.

Essa associação permite acompanhar o conjunto de atividades planejadas para cada ciclo de desenvolvimento.

## 9. Status da Issue

O estado da Issue deve refletir sua situação atual no processo de desenvolvimento.

Recomenda-se utilizar o fluxo:

```text
Aberta → Em desenvolvimento → Em revisão → Concluída
```

A equipe pode utilizar Labels, Projects ou outros recursos disponibilizados pelo GitHub para representar esses estados.

Uma Issue somente deve ser encerrada quando os critérios definidos para sua conclusão tiverem sido atendidos.

## 10. Relação entre Issue, Branch e Pull Request

As Issues devem estar relacionadas às alterações realizadas no código.

O fluxo recomendado é:

```text
Issue
  │
  ▼
Branch
  │
  ▼
Desenvolvimento
  │
  ▼
Pull Request
  │
  ▼
Revisão
  │
  ▼
Merge
  │
  ▼
Issue concluída
```

Quando uma Issue originar uma alteração de código, a branch correspondente deve permitir identificar a atividade que está sendo desenvolvida.

Exemplo:

```text
Issue #15 — Add question filtering

feature/question-filtering
```

O Pull Request deve, sempre que possível, estar vinculado à Issue correspondente.

Quando aplicável, podem ser utilizados comandos de fechamento automático do GitHub:

```text
Closes #15
```

Dessa forma, a conclusão do Pull Request pode resultar no encerramento automático da Issue relacionada.

## 11. Boas Práticas

Para manter as Issues organizadas, recomenda-se:

* verificar a existência de Issues semelhantes antes de criar uma nova;
* manter títulos objetivos e descritivos;
* fornecer contexto suficiente para a execução da atividade;
* definir critérios de aceitação quando necessário;
* utilizar Labels de forma consistente;
* associar a Issue à Milestone correspondente;
* manter o responsável pela atividade atualizado;
* evitar reunir várias demandas independentes em uma única Issue;
* manter a Issue atualizada durante o desenvolvimento;
* vincular Issues aos Pull Requests correspondentes.

## 12. Critérios para Conclusão

Uma Issue pode ser encerrada quando:

* a atividade descrita tiver sido realizada;
* os critérios de aceitação tiverem sido atendidos, quando existentes;
* os testes necessários tiverem sido realizados;
* as alterações correspondentes tiverem sido revisadas e integradas;
* não existirem pendências relacionadas à demanda.

Quando uma atividade não puder ser concluída dentro do escopo originalmente definido, recomenda-se atualizar a Issue ou criar uma nova Issue para tratar a demanda restante.

## 13. Checklist

Antes de considerar uma Issue pronta para execução, verificar:

* [ ] O título está claro e objetivo.
* [ ] A descrição apresenta o contexto da demanda.
* [ ] Os critérios de aceitação foram definidos, quando necessários.
* [ ] As Labels foram adicionadas.
* [ ] A Milestone correspondente foi definida.
* [ ] O responsável pela atividade foi indicado.
* [ ] Issues relacionadas foram vinculadas, quando aplicável.
* [ ] A Issue está pronta para ser associada a uma branch e/ou Pull Request.

## 14. Referências

> GITHUB. *About issues*. GitHub Docs. Disponível em: https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues. Acesso em: 07 set. 2026.

## 16. Histórico de Versão

| Versão | Data       | Descrição                     | Autor(es)       | Revisor(es) |
| ------ | ---------- | ----------------------------- | --------------- | ----------- |
| 1.0    | 07/09/2026 | Criação da política de Issues | [Gabriel Freitas](https://github.com/gabrielfreitass1) |             |
