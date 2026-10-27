# Missões semanais — proposta de regras para a R2

| Campo | Informação |
| --- | --- |
| Relação | Extensão de [Missões Diárias](missoes-diarias.md) e da US18 |
| Decisão conhecida | A equipe informou que os Product Owners aprovaram **o escopo de missões semanais**. A [#84](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/84) documenta somente as missões diárias. |
| Situação das regras abaixo | **Proposta técnica para revisão dos Product Owners**; metas, XP e horários não têm aceite registrado. |

## Objetivo

Incentivar estudo distribuído ao longo da semana sem exigir presença diária. A recompensa é consequência de respostas e quizzes verificáveis; ela não substitui o feedback pedagógico nem comprova aprendizagem.

## Regras propostas

- O período é a semana civil de **segunda-feira, 00:00, a segunda-feira seguinte, 00:00**, no fuso `America/Sao_Paulo`. Missão não concluída expira sem recompensa.
- Cada aluno recebe **três missões sorteadas** de um catálogo fixo de seis no primeiro acesso do período. A atribuição fica estável durante a semana. O sorteio e as metas são independentes das missões diárias.
- Apenas ações no quiz livre contam. Responder a mesma questão mais de uma vez na semana conta uma única vez; para a missão de quizzes, a combinação de tema e dificuldade concluída conta uma vez. Listas de turma não contam.
- Uma ação pode avançar missões diárias e semanais simultaneamente. Cada missão concluída credita XP uma única vez, na mesma transação que registra a conclusão; o histórico identifica a origem `MISSAO_CONCLUIDA`.
- O estudante consulta somente suas missões pelo BFF em `GET /api/v1/missoes/minhas/semanais`. Professor e administrador não recebem missões. Alterações diretas de progresso e recompensa não são expostas.
- A tela mostra meta, progresso, XP, estado concluído/em andamento, resumo da semana, próximo horário de renovação e estados de carregamento, erro e ausência de missões.

### Catálogo inicial proposto

| Código | Meta na semana | Recompensa proposta |
| --- | --- | ---: |
| `CONSTANCIA_SEMANAL` | Responder 20 questões diferentes | 100 XP |
| `EXPLORACAO_SEMANAL` | Responder 30 questões diferentes | 150 XP |
| `PRECISAO_SEMANAL` | Acertar 15 questões diferentes | 140 XP |
| `ACERTOS_SEMANAIS` | Acertar 25 questões diferentes | 180 XP |
| `VARIEDADE_SEMANAL` | Concluir 4 quizzes com combinações diferentes de tema e dificuldade | 180 XP |
| `RITMO_SEMANAL` | Concluir 6 quizzes com combinações diferentes de tema e dificuldade | 220 XP |

Os valores são **parâmetros propostos**, não resultados de validação pedagógica. Antes do merge da implementação, os POs devem confirmar ou alterar: quantidade de missões, metas, recompensas, dia e horário de renovação, expiração e tratamento de listas de turma. A equipe deve registrar a decisão na issue ou ata e verificar se há questões e combinações suficientes para tornar cada meta alcançável.

## Critérios de aceite para a implementação

1. Uma consulta autenticada atribui três missões semanais ao aluno e consultas repetidas retornam a mesma seleção; outro aluno não vê essas atribuições.
2. Respostas e quizzes válidos avançam as missões correspondentes uma vez por questão ou combinação; repetir requisição não duplica progresso.
3. Ao atingir a meta, o XP aparece uma vez no histórico, no nível, no elo e no ranking; falha transacional não deixa progresso e XP divergentes.
4. A semana muda no horário de Brasília, inclusive em viradas de ano e mudanças históricas de horário de verão; eventos anteriores não avançam a nova semana.
5. O aluno consegue acompanhar as missões na Web e recebe aviso de conclusão durante o quiz.
6. O aceite final inclui teste com PostgreSQL, BFF e Web em homologação, com registro de versão implantada e decisão dos POs sobre as regras.

## Histórico de versão

| Data | Versão | Descrição | Autor | Revisor(es) |
| --- | --- | --- | --- | --- |
| 26/10/2026 | 0.1 | Proposta de regras semanais para revisão; escopo confirmado pela equipe | Equipe AnatoQuizUp 2026.2 | Pendente |
