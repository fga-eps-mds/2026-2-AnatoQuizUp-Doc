# Política de Branches

## 1. Objetivo

Esta política define as convenções para criação, utilização e integração de branches no projeto.

O objetivo é organizar o desenvolvimento paralelo, reduzir conflitos entre alterações e estabelecer um fluxo controlado para a entrega de novas funcionalidades, correções e versões.

O projeto utiliza como referência o modelo **Git Flow**, adaptando suas práticas às necessidades do desenvolvimento.

## 2. Branches Principais

O repositório possui duas branches principais:

| Branch    | Finalidade                                                                                |
| --------- | ----------------------------------------------------------------------------------------- |
| `main`    | Mantém a versão estável do projeto, destinada às entregas e versões homologadas           |
| `develop` | Reúne as alterações que estão em desenvolvimento e serão incorporadas às próximas versões |

A branch `main` deve permanecer estável e não deve receber alterações diretamente durante o desenvolvimento normal.

## 3. Branches de Desenvolvimento

### 3.1 Feature

Utilizada para o desenvolvimento de novas funcionalidades ou melhorias.

**Padrão de nomenclatura:**

```text
feature/<nome-da-feature>
```

**Origem:** `develop`
**Destino:** `develop`

Exemplo:

```text
feature/question-ranking
feature/patient-simulation
feature/user-authentication
```

Após a conclusão do desenvolvimento, deve ser aberto um **Pull Request** para `develop`.

---

### 3.2 Release

Utilizada para preparar uma nova versão do projeto antes de sua disponibilização.

**Padrão de nomenclatura:**

```text
release/<versao>
```

**Origem:** `develop`
**Destino:** `main` e `develop`

Exemplo:

```text
release/1.0
release/2.0
```

Essa branch deve ser utilizada principalmente para:

* realização dos testes finais;
* correção de problemas encontrados durante a validação;
* ajustes necessários para a entrega;
* preparação da versão que será incorporada à `main`.

Após a aprovação da versão, as alterações devem ser integradas tanto à `main` quanto à `develop`.

---

### 3.3 Hotfix

Utilizada para correções urgentes que precisam ser aplicadas diretamente sobre uma versão estável.

**Padrão de nomenclatura:**

```text
hotfix/<nome-da-correcao>
```

**Origem:** `main`
**Destino:** `main` e `develop`

Exemplo:

```text
hotfix/fix-login-error
hotfix/correct-score-calculation
```

Após a correção e validação, o Hotfix deve ser integrado à `main` e posteriormente sincronizado com `develop`, evitando que a correção seja perdida no próximo ciclo de desenvolvimento.

## 4. Fluxo de Desenvolvimento

O fluxo padrão para uma nova funcionalidade é:

1. Atualizar a branch `develop`.
2. Criar uma branch `feature` a partir de `develop`.
3. Implementar e testar as alterações.
4. Manter a branch atualizada com `develop`, quando necessário.
5. Abrir um Pull Request para `develop`.
6. Realizar a revisão das alterações.
7. Integrar a branch após a aprovação.

De forma simplificada:

```text
main
  │
  └── develop
        │
        ├── feature/funcionalidade-a
        │
        ├── feature/funcionalidade-b
        │
        └── release/1.0.0
                  │
                  └── main
```

## 5. Convenção de Nomes

Os nomes das branches devem:

* utilizar o prefixo correspondente ao seu tipo;
* utilizar letras minúsculas;
* utilizar hífen (`-`) para separar palavras;
* ser curtos e descritivos;
* representar o objetivo principal da branch.

Exemplos:

```text
feature/question-bank
feature/ai-patient
feature/radiology-generator
release/1.0.0
hotfix/login-error
```

Deve-se evitar nomes genéricos como:

```text
feature/test
feature/new
branch-gabriel
correcao
```

## 6. Boas Práticas

* Não realizar commits diretamente em `main`.
* Criar novas `feature` sempre a partir de `develop`.
* Manter as branches de trabalho atualizadas.
* Evitar branches com escopo excessivamente amplo.
* Encerrar branches após a integração da alteração.
* Priorizar Pull Requests pequenos e fáceis de revisar.
* Evitar manter funcionalidades inacabadas diretamente em `main`.

## 7. Referência

A organização apresentada nesta política utiliza como referência o modelo de ramificação **Git Flow**, proposto por Vincent Driessen.

> DRIESSEN, Vincent. *A successful Git branching model*. 2010. Disponível em: https://nvie.com/posts/a-successful-git-branching-model/. Acesso em: 07 set. 2026.

## 9. Histórico de Versão

| Versão | Data       | Descrição                       | Autor(es)       | Revisor(es) |
| ------ | ---------- | ------------------------------- | --------------- | ----------- |
| 1.0    | 07/09/2026 | Criação da política de branches | [Gabriel Freitas](https://github.com/gabrielfreitass1) |             |
