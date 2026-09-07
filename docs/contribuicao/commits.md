# Política de Commits

## 1. Objetivo

Esta política estabelece um padrão para a criação de commits no projeto, buscando manter o histórico do repositório organizado, padronizado e de fácil compreensão.

A adoção de uma estrutura consistente facilita a identificação das alterações realizadas, contribui para a rastreabilidade das mudanças e auxilia na manutenção do projeto ao longo do seu desenvolvimento.

## 2. Estrutura dos Commits 

A estrutura dos *commits* segue o seguinte padrão:

``` <type>: <description> ```

O campo `<type>` identifica a natureza da alteração, enquanto `<description>` apresenta, de forma breve e objetiva, o que foi realizado.

### 2.1 Tipos de Commits

São adotados os seguintes tipos:

| Tipo       | Utilização                                                                       |
| ---------- | -------------------------------------------------------------------------------- |
| `feat`     | Inclusão de uma nova funcionalidade no projeto                                   |
| `fix`      | Correção de bugs ou comportamentos incorretos                                    |
| `docs`     | Alterações relacionadas à documentação                                           |
| `style`    | Alterações de formatação ou estilo que não modificam a lógica do código          |
| `refactor` | Modificação da estrutura ou organização do código sem alteração de comportamento |
| `test`     | Inclusão, alteração ou remoção de testes                                         |
| `ci`       | Alterações relacionadas à integração e entrega contínuas                         |
| `build`    | Alterações relacionadas ao processo de build ou às dependências do projeto       |
| `perf`     | Alterações realizadas com o objetivo de melhorar o desempenho                    |
| `chore`    | Tarefas auxiliares de manutenção que não se enquadram nos demais tipos           |

## 3. Descrição

A descrição do commit deve:

* ser escrita em inglês;
* utilizar uma forma verbal consistente;
* ser curta e objetiva;
* representar claramente a alteração realizada;
* evitar informações desnecessárias;
* não terminar com ponto final.

Exemplo CORRETO:

```text
feat: add question filtering
```

Exemplo ERRADO:

```text
feat: added a filter for questions.
```
## 4. Regras Gerais

Para manter o histórico consistente, devem ser observadas as seguintes regras:

1. Cada commit deve representar uma alteração lógica específica.
2. O tipo do commit deve corresponder à natureza predominante da alteração.
3. A descrição deve permitir compreender o objetivo da alteração sem consultar imediatamente o código.
4. Alterações não relacionadas devem, sempre que possível, ser separadas em commits distintos.
5. Deve-se evitar commits excessivamente genéricos, como `update code` ou `fix stuff`.
6. Commits não devem conter informações desnecessárias ou temporárias.

## 5. Exemplos

### Nova funcionalidade

```text
feat: add question ranking
```

### Correção de bug

```text
fix: correct question score calculation
```

### Documentação

```text
docs: update installation guide
```

### Refatoração

```text
refactor: simplify authentication service
```

### Testes

```text
test: add tests for question service
```

## 6. Benefícios da Padronização

A padronização dos commits tem como principais objetivos:

* facilitar a leitura e compreensão do histórico do projeto;
* melhorar a rastreabilidade das alterações;
* facilitar a identificação de mudanças por categoria;
* auxiliar na revisão de código;
* estabelecer uma convenção comum entre os integrantes da equipe;
* possibilitar futuramente a utilização de ferramentas de automação baseadas no histórico de commits.

## 7. Referências

A estrutura adotada nesta política é baseada nos princípios definidos pela especificação **Conventional Commits**, que estabelece uma convenção para mensagens de commit legíveis por pessoas e ferramentas.

**Referência principal:**

> CONVENTIONAL COMMITS. *Conventional Commits Specification*. Disponível em: https://www.conventionalcommits.org/. Acesso em: 07 set. 2026.

# Histórico de Versão

| Versão | Data       | Descrição                                      | Autor               | Revisor               |
|--------|------------|------------------------------------------------|---------------------|-----------------------|
| 1.0    | 07/09/2026 | Criação do documento de Commits | [Gabriel Freitas](https://github.com/gabrielfreitass1) |  |




