# Decisões Arquiteturais

## DA-01 — Microsserviços com BFF

**Contexto:** o produto herdado de 2026.1 já havia migrado de um backend monolítico para serviços separados. Em 2026.2 surgem novos domínios (loja, avatar, conquistas, ranking) que dependem de dados de usuário e de quiz ao mesmo tempo.

**Decisão:** manter o BFF como único ponto de entrada público e os serviços de domínio privados.

**Consequências:**
- (+) O frontend depende de um único contrato (`/api/v1`).
- (+) Autenticação validada na borda e serviços isolados da internet.
- (+) Composição de dados entre serviços (ranking, perfil social) fica no BFF, sem acoplar os serviços entre si.
- (−) Uma chamada a mais por requisição; o BFF se torna ponto único de falha.

## DA-02 — Banco de dados por serviço

**Decisão:** cada serviço tem seu próprio PostgreSQL (Auth DB e Quiz DB), **sem chave estrangeira entre bancos**. O Quiz-Service guarda `usuarioId`, `alunoId`, `professorId` e `criadoPorId` como referências externas.

**Consequências:** schemas e migrations evoluem de forma independente. Dados de exibição (nome, avatar) são resolvidos via API, preferencialmente em lote no BFF.

## DA-03 — Segurança entre camadas

- O BFF valida o JWT e repassa a requisição com `X-Internal-Token` (segredo compartilhado) e os headers informativos `X-User-Id`, `X-User-Papel` e `X-User-Status`.
- Os serviços validam novamente o JWT. Os headers `X-User-*` **não são fonte de verdade**.
- Rotas de uso interno (`/inventario/usuarios/equipados`, `/conquistas/usuarios/destaques`) são **bloqueadas no BFF** (retornam 404) e só são consumidas entre serviços.
- Access token de curta duração + refresh token persistido e revogável; senhas com bcrypt.

## DA-04 — Arquitetura em camadas nos serviços

Cada serviço organiza o código **por domínio** em `src/modules/<dominio>/`, e dentro de cada módulo por camadas:

```text
Routes → Middlewares → Controllers → Services → Repositories → Prisma/PostgreSQL
```

A dependência é sempre de cima para baixo. Regras de negócio ficam nos `Services`; acesso a dados, nos `Repositories`.

```text
Quiz-Service/src/modules/
├── questoes/  quiz/  turma/  lista/  resolucaoLista/
├── loja/  inventario/  conquistas/  ranking/
└── dashboardAluno/  dashboardTurma/

Usuario-Service/src/modules/
├── auth/ (aluno, professor, sessao, recuperar-senha)
├── usuarios/  admin/  amizade/
```

## DA-05 — Feature-Sliced Design no Frontend

O Web segue o **Feature-Sliced Design**. Uma camada só importa camadas inferiores:

| Camada | Conteúdo no projeto |
|---|---|
| `app/` | Rotas, provedores e estilos globais |
| `pages/` | Composição das telas (aluno, professor, admin) |
| `widgets/` | Blocos compostos (ex.: `header`) |
| `features/` | Ações de negócio: `random-quiz`, `loja`, `profile-cosmetics`, `achievements`, `ranking`, `friendship`, `manage-questions`, `manage-lista`, `manage-turmas`, `resolucaoLista`, `auth-by-credencials`… |
| `entities/` | Modelos de dados: `user`, `usuarios`, `turmas`, `lista`, `resolucaoLista`, `dashboardTurma` |
| `shared/` | Componentes genéricos e cliente HTTP |

## DA-06 — Gamificação no Quiz-Service

**Decisão:** moedas, loja, inventário e conquistas ficam no mesmo serviço do quiz.

**Justificativa:** ganhar moedas e desbloquear conquistas acontece **na mesma transação** em que o aluno responde uma questão. Separar em outro serviço exigiria consistência eventual entre bancos para cada resposta.

**Consequência:** toda movimentação de moedas é registrada em `TransacaoMoeda` (acerto, conquista, compra, uso de potencializador), o que garante rastreabilidade do saldo.

## DA-07 — Serviço de IA reservado

O BFF já possui a rota `/ia` e o cliente `ai.client`, que respondem `503` enquanto `AI_URL` não estiver configurada. Isso permite habilitar geração de questões por IA em releases futuras (`OrigemQuestao.GERADA_POR_IA` já existe no modelo) sem mudar o contrato do frontend.

## DA-08 — Qualidade contínua

- Pipeline obrigatório em todo PR: lint, build, testes e SonarCloud.
- Cobertura mínima de **85%** (`coverageThreshold` do Jest), verificada no CI.
- Métricas exportadas em `.json` para o repositório de Doc e consumidas pelo dashboard Streamlit.

## Histórico de Versão

| Data | Versão | Descrição | Autor(es) |
| :--- | :--- | :--- | :--- |
| 28/09/2026 | 1.0 | Registro das decisões arquiteturais de 2026.2 | [Henrique Carvalho](https://github.com/henriquecarv3), [Caio Habibe](https://github.com/CaioHabibe), [João Lucas](https://github.com/jlucasiqueira), [Rafael Melo](https://github.com/rmatuda) |