# Métricas de produto da Release 2

O [roadmap](produto/roadmap.md) exige coleta de conclusão, acerto e retorno para a saída da R2. O [dashboard gerencial R2](dashboard-r2.md) compara processo e qualidade técnica; esta página define as métricas de **uso do produto**. Nenhum valor de homologação é apresentado como resultado até que a versão implantada e o período sejam registrados.

## Fonte e consulta

O Quiz-Service registra início e conclusão de rodadas em `tentativas_quiz`, com total de questões e acertos. A consulta agregada proposta é `GET /api/v1/quiz/metricas-r2?inicio=...&fim=...`, acessível apenas ao papel `ADMINISTRADOR` pelo BFF. `inicio` e `fim` são instantes ISO 8601 com offset; `fim` é exclusivo e o intervalo máximo é de 90 dias. A resposta contém apenas contagens e taxas agregadas, sem identificadores de estudantes.

Para a R2, usar o período de desenvolvimento de **28/09/2026 00:00** até **26/10/2026 00:00** no horário de Brasília e registrar separadamente a coleta de 26/10 para o marco de entrega. Registrar URL de homologação, versão dos serviços, instante da extração e se a base contém apenas dados de teste.

| Indicador | Numerador | Denominador | Interpretação |
| --- | --- | --- | --- |
| Conclusão de quizzes | Rodadas iniciadas no período com status `CONCLUIDA` | Todas as rodadas iniciadas no período | Percentual de rodadas que chegaram à conclusão no instante da coleta. |
| Acerto | Soma de acertos das rodadas concluídas iniciadas no período | Soma das questões dessas rodadas | Percentual de acertos nas rodadas concluídas; não mede aprendizagem fora do produto. |
| Retorno em 7 dias | Estudantes elegíveis com outro quiz concluído entre 24 horas e 7 dias após o primeiro quiz concluído no período | Estudantes cujo primeiro quiz concluído no período ocorreu pelo menos 7 dias antes de `fim` | Evita classificar como não retornou quem ainda não teve sete dias de observação. |

Quando o denominador é zero, a taxa é `null` (indisponível), não 0%. A taxa de conclusão é um retrato: uma rodada ainda em andamento pode ser concluída depois da extração. Revisões de gabarito não mudam os totais de acertos salvos na conclusão da rodada. O retorno mede nova conclusão de quiz, não simples login.

## Evidência necessária para o aceite

1. Implantar o serviço e verificar que um administrador consulta os agregados e um estudante recebe 403.
2. Criar um conjunto de teste conhecido: quiz iniciado e abandonado, quiz concluído com acertos e retorno após pelo menos 24 horas. Comparar a API aos registros de origem.
3. Guardar a resposta agregada, período, versão implantada e data da coleta no registro de homologação da R2. Separar dados demonstrativos de qualquer estudo com estudantes reais.
4. Discutir os indicadores com os POs junto com feedback qualitativo. A existência do endpoint não equivale a resultado medido nem a aceite da release.

## Histórico de versão

| Data | Versão | Descrição | Autor | Revisor(es) |
| --- | --- | --- | --- | --- |
| 26/10/2026 | 0.1 | Definições e fonte de conclusão, acerto e retorno da R2 | Equipe AnatoQuizUp 2026.2 | Pendente |
