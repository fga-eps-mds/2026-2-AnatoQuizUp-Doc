# Backlog detalhado da Release 2

**Recorte:** desenvolvimento de 28/09 a 25/10/2026; marco de entrega e aceite em 26/10/2026. Este é um retrato de implementação e evidências, não um registro de aceite dos Product Owners. O [roadmap](../produto/roadmap.md) define os critérios de saída.

## Histórias e critérios verificáveis

| História | Prioridade | Critério de aceite da R2 | Estado em 26/10 | Evidência e pendência |
| --- | --- | --- | --- | --- |
| US04 — XP e nível | Must | Quiz concluído credita XP uma vez, atualiza nível, histórico e ranking. | Código integrado; homologação pendente | [Web #12](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Web/pull/12), [Quiz-Service #10](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Quiz-Service/pull/10) |
| US06 e US07 — quiz e feedback | Must | Aluno seleciona tema/dificuldade, responde questões e vê gabarito e explicação. | Fluxo herdado; aceite R2 pendente | Validar percurso integrado sem imagens radiológicas nesta entrega. |
| US08 — revisão de erros | Must | Após errar, aluno encontra suas questões erradas, vê sua resposta, gabarito e explicação e consegue revisar o conteúdo. | Parcial | O histórico mostra respostas e explicações, mas não oferece seleção exclusiva de erros; especificar e implementar o fluxo. |
| US09 e US10 — listas da professora | Must | Professora seleciona questões, atribui lista a turma e consulta resultados individuais e coletivos. | Funcionalidade herdada; aceite R2 pendente | Executar percurso integrado com professora e aluno e registrar evidências. |
| US16 — escolha do quiz | Must | Aluno escolhe disciplina, tema e dificuldade antes de começar; opções sem questões não iniciam um quiz inválido. | Parcial | Tema e dificuldade existem em [EscolhaQuizPage](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Web/blob/main/src/pages/quizAluno/ui/EscolhaQuizPage.tsx); disciplina e estado sem questões requerem conferência. |
| US18 — missões | Should | Progresso e recompensa vêm de atividades verificáveis, sem duplicidade, no período correto. | Diárias integradas; semanais em PR | [Quiz-Service #14](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Quiz-Service/pull/14), [BFF #10](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-BFF/pull/10), [Web #18](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Web/pull/18). A equipe confirmou em 26/10/2026 que escopo, metas e recompensas semanais foram aprovados pelos POs na semana anterior à entrega. Implementação semanal aguarda revisão e homologação. Mensais sem aprovação conhecida. |
| US19 — progresso do aluno | Must | Aluno consulta resultados e desempenho por tema para orientar o estudo. | Implementação existente; aceite R2 pendente | [DashboardAlunoPage](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Web/blob/main/src/pages/dashboardAluno/DashboardAlunoPage.tsx); conferir os dados com respostas reais em homologação. |
| US20 e US23 — elos | Should | XP total e XP de elo são distintos; avisos, perda, recuperação e ranking seguem os prazos aprovados. | Código integrado; rotina agendada e aceite pendentes | [Quiz-Service #17](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Quiz-Service/pull/17), [Web #22](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Web/pull/22), [#89](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/89). |

Os status acima distinguem **código integrado** de **critério aceito em homologação**. A descrição da [US18](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/84) ainda contém tarefas não marcadas e texto que exclui missões semanais; atualizar a issue ao registrar as regras aprovadas.

## Tarefas de fechamento e dependências

| Tarefa | Depende de | Conclusão verificável |
| --- | --- | --- |
| Especificar e implementar revisão focada em erros (Web, BFF e Quiz-Service conforme o contrato escolhido) | Histórico de respostas e US08 | Aluno acessa apenas os erros, mesmo após recarregar, e vê resposta, gabarito e explicação; teste integrado aprovado. |
| Especificar e implementar missões semanais | Registro de metas, XP, período, expiração e aceite dos POs | Catálogo, progresso, renovação e recompensa idempotente funcionam em serviço, BFF e Web; testes de virada de período. |
| Agendar a verificação de inatividade | Rotina administrativa de [Quiz-Service #17](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Quiz-Service/pull/17) | Agendamento autenticado executa a varredura e trata lotes pendentes; alertas chegam sem exigir acesso do aluno. |
| Instrumentar métricas de produto | Identidade e registros de tentativas | Conclusão, acerto e retorno têm definição, fonte, período e consulta reproduzível; dados de teste separados de dados reais. |
| Validar a R2 em homologação | Deploy dos PRs e migrações | Roteiro ponta a ponta executado; resultados, falhas, versão, evidências e decisão dos POs registrados. |

## Evidências para a decisão de saída

1. Registrar as versões implantadas de Web, BFF, Quiz-Service e Usuario-Service, bem como as migrações aplicadas.
2. Executar acesso → escolha → quiz → feedback → revisão de erros → progresso, incluindo repetição da conclusão para verificar XP e missões.
3. Executar professora → questão validada → lista atribuída → resposta do aluno → resultados individuais e da turma.
4. Conferir ATP, XP, missão diária e semanal, elo e ranking na mesma conta; testar isolamento entre contas.
5. Extrair conclusão, acerto e retorno dos estudantes em um período definido e conferir as contagens com os registros de origem.
6. Anexar evidências, defeitos e decisão explícita dos POs. Sem esses registros, o critério de saída permanece **pendente**, ainda que os PRs estejam integrados.

## Histórico de versão

| Data | Versão | Descrição | Autor | Revisor(es) |
| --- | --- | --- | --- | --- |
| 26/10/2026 | 0.1 | Primeiro recorte rastreável da R2; critérios pendentes de validação | Equipe AnatoQuizUp 2026.2 | Pendente |
