# Revisão de erros — US08

## Objetivo e alcance

A US08 permite que o estudante encontre as respostas incorretas registradas no próprio histórico e volte ao gabarito e à explicação. A primeira entrega reutiliza as resoluções existentes: não cria uma lista de exercícios nova, não altera a resposta já registrada e não concede XP ou ATP pela consulta. O fluxo proposto está implementado para revisão nos PRs [Quiz-Service #18](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Quiz-Service/pull/18) e [Web #25](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Web/pull/25); o aceite integrado permanece pendente.

## Fluxo do estudante

1. Após concluir um quiz com erro, escolher **Revisar erros**; a aplicação abre `/aluno/historico?aba=erros`. O estudante também pode selecionar a aba **Revisar erros** no histórico.
2. O histórico solicita apenas as resoluções incorretas da conta autenticada, da mais recente para a mais antiga. A aba permite filtro por tema e paginação de 50 registros por página.
3. Cada resposta apresenta tema, dificuldade, data, enunciado, resposta marcada, gabarito e explicação cadastrada. Quando não há explicação, a interface informa a ausência, sem inventar conteúdo.
4. Ao trocar de tema ou de aba, a listagem retorna à primeira página. Voltar à aba de prática mantém o histórico completo separado da seleção de erros.

## Estados e respostas esperadas

| Estado | Comportamento esperado |
| --- | --- |
| Carregando | Indicador de carregamento até a resposta da API. |
| Sem erros na conta ou no tema | Mensagem “Nenhum erro encontrado”; total igual a zero. |
| Com erros | Cartões com resposta do estudante, gabarito e explicação; total e paginação coerentes com o filtro. |
| Falha de rede ou serviço | Mensagem de erro e ação **Tentar novamente**, sem apresentar dados de outra conta. |
| Página além do fim | Lista vazia com total filtrado correto, para permitir retorno a uma página válida. |
| Sem sessão ou papel não autorizado | Acesso negado pelas regras de autenticação; nenhuma resolução é exposta. |

## Contrato e regras

`GET /api/v1/quiz/historico?somenteErros=true&page=1&limit=50` usa o token da sessão para identificar o estudante. O BFF encaminha a requisição ao Quiz-Service; o cliente não envia `usuarioId` para escolher de quem são os dados. `somenteErros` aceita `true` ou `false` e pode ser combinado com `tema`, `dificuldade` e `tipo`. O limite máximo é 100 por requisição.

Uma resolução entra na revisão quando sua resposta marcada difere do gabarito **atual** da questão. Resoluções e questões excluídas ou inativas não são exibidas. Cada tentativa incorreta permanece um registro distinto; a revisão não agrega tentativas da mesma questão. Se o gabarito for corrigido depois de uma resposta antiga, sua classificação pode mudar. Preservar o gabarito histórico por tentativa exigiria evolução do modelo de dados e decisão de produto própria.

## Critérios de aceite e evidências

| Critério | Evidência necessária |
| --- | --- |
| O estudante chega à revisão após errar e pelo histórico | Capturas da conclusão do quiz e da aba de erros na mesma versão implantada. |
| Apenas respostas incorretas da conta aparecem | Preparar um acerto e um erro em duas contas; conferir filtro e isolamento na UI e na API. |
| O conteúdo ajuda a compreender o erro | Conferir resposta marcada, gabarito e explicação de questão previamente conhecida. |
| Filtro, paginação e estados funcionam | Repetir com tema sem erros, mais de 50 erros, falha simulada e página além do total. |
| A revisão não muda saldo nem tentativa | Comparar histórico de XP/ATP e contagem de resoluções antes e depois de abrir a revisão. |

Testes de código e build dos PRs sustentam a implementação. O resultado ponta a ponta e o aceite dos Product Owners devem ser registrados no [roteiro de validação da R2 proposto no PR #117](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/pull/117), com SHA de deploy, data e evidências.

## Histórico de versão

| Data | Versão | Descrição |
| --- | --- | --- |
| 26/10/2026 | 1.0 | Fluxo, estados, contrato e critérios verificáveis da US08. |
