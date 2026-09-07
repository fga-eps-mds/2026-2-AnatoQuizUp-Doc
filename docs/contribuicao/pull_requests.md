# Política de Pull Requests

## 1. Objetivo

Esta política estabelece as diretrizes para criação, revisão e integração de **Pull Requests (PRs)** no projeto.

O objetivo é padronizar o processo de submissão de alterações, facilitar a revisão do código e garantir maior rastreabilidade entre as atividades desenvolvidas, suas respectivas *issues* e as alterações realizadas no repositório.

## 2. Criação do Pull Request

Todo Pull Request deve estar relacionado a uma **Issue** previamente criada, sempre que a alteração estiver associada a uma atividade ou requisito do projeto.

O Pull Request deve apresentar informações suficientes para que os demais integrantes da equipe compreendam:

* qual alteração foi realizada;
* qual Issue está sendo atendida;
* quais funcionalidades ou tarefas foram desenvolvidas;
* quais testes ou validações foram realizados;
* quais pontos ainda precisam de atenção.

## 3. Título

O título do Pull Request deve identificar a **Issue** relacionada e apresentar, de forma breve, o objetivo principal da alteração.

### Formato

```text
#<número-da-issue> <descrição>
```

### Exemplo

```text
#1 Create Rich Picture
```

A descrição deve ser objetiva e permitir que a finalidade do Pull Request seja compreendida sem a necessidade de abrir imediatamente as alterações.

## 4. Descrição

A descrição do Pull Request deve apresentar um resumo das alterações realizadas e das validações executadas.

Recomenda-se utilizar uma estrutura objetiva, como:

```text
Neste Pull Request foram realizadas:

- Implementação da US 01
- Validação da funcionalidade
- Criação dos testes
- Correção de bug relacionado a ...
```

Quando aplicável, também devem ser informadas:

* decisões técnicas relevantes;
* limitações conhecidas;
* pontos que exigem atenção do revisor;
* instruções necessárias para testar a alteração.

## 5. Reviewer

Todo Pull Request deve possuir pelo menos **um Reviewer** responsável pela análise das alterações.

O Reviewer deve avaliar, conforme aplicável:

* qualidade e organização do código;
* aderência aos padrões definidos pelo projeto;
* funcionamento da implementação;
* existência e adequação dos testes;
* possíveis impactos ou problemas introduzidos pela alteração.

Pelo menos um integrante da equipe deve ser indicado como Reviewer.

A integração do Pull Request deve ocorrer somente após a aprovação da revisão.

## 6. Assignees

O campo **Assignees** deve identificar os integrantes responsáveis pela implementação das alterações presentes no Pull Request.

Devem ser adicionados como *Assignees* os membros que efetivamente participaram do desenvolvimento da alteração.

Dessa forma, o campo permite identificar os responsáveis pela execução da atividade, enquanto o **Reviewer** representa o responsável pela análise e aprovação da alteração.

## 7. Labels

Todo Pull Request deve possuir **Labels** que representem sua natureza ou finalidade.

Sempre que possível, as Labels utilizadas devem ser compatíveis com as adotadas na **Issue correspondente**.

Exemplos:

```text
feature
bug
documentation
enhancement
```

A utilização das Labels facilita a organização, filtragem e identificação das alterações realizadas no projeto.

## 8. Milestone

O Pull Request deve estar associado à **Milestone** correspondente ao ciclo de desenvolvimento em que a alteração está sendo realizada.

Quando o projeto utilizar Milestones para representar Sprints, deve ser indicada a Sprint correspondente à execução da atividade.

## 9. Issue relacionada

Todo Pull Request deve estar vinculado à **Issue correspondente**.

Após a criação do Pull Request, a Issue deve ser associada por meio dos recursos disponibilizados pelo GitHub.

Quando apropriado, podem ser utilizados comandos de fechamento automático, como:

```text
Closes #1
```

Dessa forma, após o merge do Pull Request, a Issue relacionada poderá ser encerrada automaticamente.

## 10. Checklist antes do Merge

Antes da integração do Pull Request, o responsável deve verificar:

* [ ] O título identifica a Issue correspondente.
* [ ] A descrição apresenta as principais alterações realizadas.
* [ ] Os testes necessários foram executados.
* [ ] A Issue correspondente está vinculada.
* [ ] As Labels foram adicionadas.
* [ ] A Milestone correspondente foi definida.
* [ ] Os Assignees foram definidos.
* [ ] Pelo menos um Reviewer foi indicado.
* [ ] O Pull Request foi aprovado pelo Reviewer.
* [ ] Não existem conflitos pendentes com a branch de destino.

## 11. Boas Práticas

Para manter o processo de revisão organizado, recomenda-se:

* manter Pull Requests pequenos e focados em uma alteração lógica;
* evitar misturar funcionalidades diferentes no mesmo Pull Request;
* fornecer uma descrição clara das alterações;
* realizar os testes antes de solicitar a revisão;
* manter a branch atualizada com a branch de destino quando necessário;
* responder aos comentários e solicitações realizadas durante a revisão;
* evitar realizar alterações não relacionadas ao objetivo original do Pull Request;
* garantir que o Pull Request esteja pronto para revisão antes de solicitar aprovação.

## 12. Referências

> GITHUB. *About pull requests*. GitHub Docs. Disponível em: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests. Acesso em: 07 set. 2026.

## 14. Histórico de Versão

| Versão | Data       | Descrição                            | Autor(es)                                                         | Revisor(es)  |
| ------ | ---------- | ------------------------------------ | ----------------------------------------------------------------- | ------------ |
| 1.0    | 07/09/2026 | Criação da política de Pull Requests | [Gabriel Freitas](https://github.com/gabrielfreitass1) |  |
