# Endpoints

Todas as rotas públicas são expostas pelo **BFF** sob `/api/v1`. Exceto as de autenticação pública, todas exigem `Authorization: Bearer <JWT>`.

## Usuario-Service

| Prefixo | Método e rota | Descrição |
|---|---|---|
| `/autenticacao` | `POST /login`, `POST /atualizar-token`, `GET /usuario-atual`, `POST /sair` | Sessão |
| | `POST /cadastro`, `POST /cadastro/professor` | Cadastro de aluno e professor |
| | `GET /alunos/email-disponivel`, `GET /alunos/nickname-disponivel` | Validação de cadastro |
| | `POST /recuperar-senha`, `POST /redefinir-senha` | Recuperação de senha |
| | `GET /estados`, `GET /estados/:uf/cidades`, nacionalidades, opções acadêmicas | Dados de formulário |
| `/usuarios` | `GET /`, `GET /alunos`, `GET /visiveis`, `GET /meu-avatar`, `GET /:id` | Consulta de usuários |
| `/admin` | `GET /usuarios`, `GET /usuarios/:id`, `PATCH /usuarios/:id/status` | Gestão de usuários |
| `/amizade` | `GET /`, `GET /busca`, `POST /`, `DELETE /` | Amigos |
| | `GET /convites/recebidos`, `GET /convites/enviados`, `PATCH /aceitar`, `PATCH /recusar` | Convites |
| | `PATCH /visibilidade`, `GET /amigos/perfis` | Visibilidade e perfis |

## Quiz-Service

| Prefixo | Método e rota | Descrição |
|---|---|---|
| `/questoes` | `GET /`, `GET /busca`, `GET /:id`, `POST /`, `PUT /:id`, `DELETE /:id` | Banco de questões |
| `/quiz` | `GET /`, `POST /responder`, `GET /moedas`, `GET /quantidade_por_tema`, `GET /historico` | Quiz livre e moedas |
| `/turmas` | `GET /`, `GET /:id`, `POST /`, `PATCH /:id`, `DELETE /:id`, `GET/POST /:id/alunos`, `DELETE /:id/alunos/:alunoId` | Turmas |
| `/lista` | `POST /`, `GET /`, `GET /:id`, `PATCH /:id`, `DELETE /:id`, `GET /:id/pdf` | Listas |
| | `POST /:id/questoes`, `PATCH /:id/questoes/ordem`, `DELETE /:id/questoes/:questaoId` | Questões da lista |
| | `POST /:id/turmas`, `PATCH/DELETE /:id/turmas/:turmaId`, `GET /:id/estatisticas/turma/:turmaId` | Aplicação em turmas |
| `/listasAluno` | `GET /`, `GET /:id`, `POST /:id/autosave`, `POST /:id/submeter`, `GET /:listaTurmaId/pdf` | Resolução de listas |
| `/loja` | `GET /catalogo`, `GET /meu-inventario`, `POST /comprar`, `POST /usar`, `GET /meu-historico`, `GET /meu-historico-usos` | Loja |
| `/inventario` | `GET /meuInventario`, `GET /meuPerfil`, `PATCH /equipar`, `PATCH /desequipar` | Avatar e itens |
| `/conquistas` | `GET /`, `GET /:id`, `GET /minhas`, `GET /meu-progresso`, `GET /destaques`, `PATCH /desbloqueios/:id/destaque` | Conquistas |
| `/dashboardAluno` | `GET /` | Desempenho do aluno |
| `/turmasDashboard` | `GET /:id/macro`, `GET /:id/individual`, `GET /:id/listas`, `GET /:id/listas/:listaId` | Dashboard da turma |

## Rotas compostas no BFF

| Rota | Serviços consultados | Descrição |
|---|---|---|
| `GET /ranking/geral`, `/ranking/amigos`, `/ranking/turmas/:turmaId`, `/ranking/listas/:turmaId/:listaId` | Quiz + Usuário | Pontuação + nome e avatar dos usuários |
| `GET /perfis/:usuarioId/social` | Usuário + Quiz | Perfil público com avatar equipado e conquistas em destaque |
| `/ia/*` | AI Service | Reservado; responde `503` |

## Rotas internas (bloqueadas no BFF)

`/inventario/usuarios/equipados` e `/conquistas/usuarios/destaques` retornam **404** quando chamadas externamente. São usadas apenas pelo BFF para compor ranking e perfil social.

## Histórico de Versão

| Data | Versão | Descrição | Autor(es) |
| :--- | :--- | :--- | :--- |
| 28/09/2026 | 1.0 | Levantamento dos endpoints a partir do código dos serviços | [Henrique Carvalho](https://github.com/henriquecarv3), [Caio Habibe](https://github.com/CaioHabibe), [João Lucas](https://github.com/jlucasiqueira), [Rafael Melo](https://github.com/rmatuda) |