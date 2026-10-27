# Validação integrada da Release 2

## Objetivo e critério de saída

Este roteiro verifica, na [homologação](https://anatoquizup-homolog-2026-2.netlify.app/), os [critérios de saída da R2](../produto/roadmap.md#criterios-de-saida): percurso completo do estudante até a revisão, recompensas ligadas a atividades verificáveis, atribuição e consulta de listas pelo professor e coleta de indicadores mínimos. A execução deve ocorrer **após o merge e o deploy** dos PRs correspondentes. Resultado local de teste automatizado não substitui resultado integrado.

Cada caso deve registrar data e hora com fuso, executor, SHA/deploy de Web, BFF, Quiz-Service e Usuário-Service, conta de teste (identificador anonimizado), resultado, captura ou log sem dados sensíveis e defeito vinculado. Os POs registram o aceite da release em issue ou ata depois de avaliar os resultados e limitações. Sem essa decisão, o aceite permanece pendente.

## Preparação

1. Confirmar deploys saudáveis e registrar seus identificadores. Abrir a Web, recarregar uma rota interna e conferir o health check do BFF.
2. Usar contas de teste autorizadas: dois estudantes, um professor e, para métricas, um administrador. Não publicar credenciais nem dados pessoais.
3. Preparar questões com gabarito, explicação, tema e dificuldade conhecidos; uma delas deve ter imagem de teste sem dados de paciente. Preparar uma lista atribuível a uma turma de teste.
4. Registrar saldos de ATP/XP, progresso de missão e histórico antes da execução. Para missão semanal, usar as regras publicadas e aprovadas pelos POs; enquanto as metas e recompensas do [rascunho de missões semanais](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/pull/115) não forem aprovadas, verificar apenas o comportamento implementado e marcar o aceite da regra como pendente.
5. Anotar se a janela de sete dias de retorno está completa. Uma janela incompleta não pode ser usada para concluir a taxa de retorno.

## Casos ponta a ponta

| Caso | Passos e resultado esperado | Critério coberto |
| --- | --- | --- |
| R2-01 — Quiz e feedback | Estudante entra, escolhe tema/dificuldade, inicia e conclui quiz com um acerto e um erro. Conferir enunciado, imagem quando houver, resposta, gabarito, explicação e persistência da tentativa após novo login. | Percurso do estudante |
| R2-02 — Revisão de erros (US08) | Na página de histórico, abrir a aba de erros. Conferir somente respostas incorretas do estudante, com sua resposta e gabarito; testar paginação, estado vazio e isolamento entre as duas contas. | Feedback e revisão |
| R2-03 — XP e ATP | Anotar saldos antes/depois de atividades elegíveis. Conferir lançamentos e quantias segundo o plano de gamificação; repetir a consulta para excluir duplicidade por recarga. | Ações verificáveis |
| R2-04 — Missões diárias | Executar ação que avança missão, conferir progresso, conclusão, crédito único de XP e renovação no período seguinte. | Missões |
| R2-05 — Missões semanais | Conferir catálogo e progresso semanal, ações de dias distintos, conclusão e crédito único. Repetir após virada de segunda-feira no fuso `America/Sao_Paulo`, incluindo semana que atravessa mudança de mês. Registrar regra aprovada pelo PO antes do aceite. | Missões |
| R2-06 — Ranking e elo | Conferir posição/elo e alterações decorrentes de XP. Para inatividade, validar aviso, rebaixamento e recuperação contra a decisão registrada na [issue #89](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/89). | Progressão |
| R2-07 — Professor e lista | Professor atribui lista a turma de teste; estudante a executa; professor consulta o resultado da lista sem visualizar dados de outra turma. | Fluxo do professor |
| R2-08 — Imagens | Professor cria e atualiza questão com PNG/JPEG de teste; URL HTTPS abre sem autenticação; estudante vê a imagem no quiz; reiniciar serviço e repetir a leitura. Conferir que a questão desativada não entra em novo quiz. | Conteúdo integrado |
| R2-09 — Métricas | Administrador consulta o período de teste. Reconciliar quizzes iniciados/concluídos, acertos e participantes com registros de teste; verificar recusa a estudante/professor. Registrar denominadores e janela completa para retorno em sete dias. | Eventos mínimos |
| R2-10 — Regressão e acesso | Repetir login, saída, isolamento entre contas, recarga de rota interna, compra/uso do Café do Foco e consulta do histórico. | Ausência de interrupções críticas |

Em cada caso, classificar como **aprovado**, **falhou**, **bloqueado** ou **não executado**. Um bloqueio exige causa objetiva e ação para desbloquear. Casos com falha exigem issue e reteste com novo SHA.

## Registro de execução em 26/10/2026

| Verificação | Resultado observado | Evidência e limite |
| --- | --- | --- |
| Acesso público à Web | Aprovado para abertura da página inicial e navegação até o formulário de login | [URL de homologação](https://anatoquizup-homolog-2026-2.netlify.app/); inspeção em 26/10/2026. Não comprova autenticação nem versão implantada dos serviços. |
| R2-01 a R2-10 | Não executados neste registro | Faltam contas de teste, SHAs dos deploys e confirmação de publicação dos PRs da R2. Não inferir resultado integrado a partir de testes locais. |
| Aceite dos POs | Pendente | A confirmação de **escopo** de missões semanais e a decisão sobre prazo de rebaixamento já foram comunicadas pela equipe; não equivalem ao aceite do conjunto da R2 nem aprovam as metas/recompensas semanais propostas. |

Os [resultados de testes anteriores](resultados-testes.md) cobrem a R1 entre 21 e 23/10 e não devem ser atribuídos à R2. Atualizar esta seção após cada rodada, preservando falhas, bloqueios, data, versões e links de evidência. A release só satisfaz o critério de saída quando os fluxos críticos forem aprovados na versão implantada e houver decisão registrada dos POs.

## Histórico de versão

| Data | Versão | Descrição |
| --- | --- | --- |
| 26/10/2026 | 1.0 | Plano de validação da R2 e registro inicial das observações públicas. |
