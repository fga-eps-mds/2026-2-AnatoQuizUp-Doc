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

## DA-07 — IA no BFF, exceto a simulação OSCE (serviço dedicado)

**Contexto:** a rota `/ia` nasceu como reserva para um futuro "AI Service" (cliente `ai.client` + variável `AI_URL`, respondendo `503` enquanto não houvesse serviço). Quando a IA passou a ser construída de fato — dica, perguntas livres e a simulação OSCE —, a decisão de 26/10 foi manter tudo no BFF: nenhuma das três rotas tinha estado, banco ou orquestração que justificasse um serviço próprio.

**Decisão original** (ratificada com os Product Owners na [ata de 26/10/2026](../reunioes/reuniao-26-10-26.md), que definiu o Gemini como solução de curto prazo com integração desacoplada para permitir a troca futura do modelo)**:** o BFF **é** a camada de IA. Ele chama a Gemini direto pelo `gemini.client`, configurado por `GEMINI_API_KEY`/`GEMINI_MODEL`; `ai.client` e `AI_URL` foram removidos.

**Revisão — simulação OSCE extraída para o microsserviço ChatbotOSCE:** com os Product Owners, decidiu-se criar um microsserviço dedicado (`ChatbotOSCE`) só para a simulação de casos clínicos. `/ia/dica` e `/ia/perguntar` continuam no BFF, sem mudança — a exceção é só a estação OSCE (`/ia/osce/*`), que tem um escopo de prompt bem maior (interpretar paciente e depois examinador) e é a frente que vai crescer no roadmap (cadastro de casos pelo professor, novas estações). O BFF deixa de chamar a Gemini para essas rotas e passa a fazer proxy para o ChatbotOSCE, do mesmo jeito que já faz para o Quiz-Service e o Usuario-Service (`criarProxyHandler`); o `503` do catch-all de `/ia/*` permanece para sub-rota inexistente ou chave ausente nas rotas que seguem no BFF.

**Consequências:**
- (+) Dica e perguntas livres continuam simples, sem serviço a mais para subir, versionar e monitorar.
- (+) A simulação OSCE ganha um dono próprio para crescer (cadastro de casos, novas estações) sem inflar o BFF.
- (+) Sem estado de sessão: o histórico da conversa vive no front e é reenviado a cada chamada, como no chat de ajuda.
- (−) Mais um serviço para subir, versionar e monitorar, com seu próprio `GEMINI_API_KEY`/`GEMINI_MODEL`.
- (−) Se entrar RAG, geração de questões em lote ou fila de processamento (`OrigemQuestao.GERADA_POR_IA` já existe no modelo) nas rotas que ficaram no BFF, esta decisão deve ser reavaliada de novo.

A simulação OSCE **não persiste nada** (conversa e rubrica morrem com a página), o que é coerente com o DA-02 e não muda o [banco de dados](banco-de-dados.md). Essa escolha é também o que hoje impede derivar a nota de corte por *borderline regression* — ver a seção 5.6 do [documento da feature](chatbot-osce.md).

## DA-08 — Qualidade contínua

- Pipeline obrigatório em todo PR: lint, build, testes e SonarCloud.
- Cobertura mínima de **85%** (`coverageThreshold` do Jest), verificada no CI.
- Métricas exportadas em `.json` para o repositório de Doc e consumidas pelo dashboard Streamlit.

## Histórico de Versão

| Data | Versão | Descrição | Autor(es) | Revisor(es) |
| --- | --- | --- | --- | --- |
| 28/09/2026 | 1.0 | Registro das decisões arquiteturais de 2026.2 | [Henrique Carvalho](https://github.com/henriquecarv3), [Caio Habibe](https://github.com/CaioHabibe), [João Lucas](https://github.com/jlucasiqueira), [Rafael Melo](https://github.com/rmatuda) | [João Paulo Lima](https://github.com/jpaulohe4rt) ([PR #54](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/pull/54)) |
| 26/10/2026 | 1.1 | DA-07 reescrita: IA implementada no próprio BFF via Gemini, sem serviço dedicado | [João Paulo Lima](https://github.com/jpaulohe4rt), [Rafael Melo](https://github.com/rmatuda) | |
| 17/11/2026 | 1.2 | DA-07 revisada: simulação OSCE extraída para o microsserviço ChatbotOSCE, decidido com os Product Owners; `/ia/dica` e `/ia/perguntar` continuam no BFF | [João Paulo Lima](https://github.com/jpaulohe4rt) | |
