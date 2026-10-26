# Plano de Gamificação — AnatoQuizUp 2026.2

| Campo | Informação |
| --- | --- |
| Objetivo | Conectar prática de anatomia radiológica, feedback e progressão sem confundir recompensa com aprendizagem |
| Escopo | Estado do produto e decisões conhecidas em 26/10/2026; [issue #69](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/69) |
| Situação | Plano para revisão da equipe e dos Product Owners; decisões de escopo relatadas pela equipe estão identificadas separadamente |

## 1. Objetivo e princípios

O AnatoQuizUp usa elementos de jogos em um contexto de estudo: questões de anatomia radiológica, feedback, metas, progressão e personalização. Essa é a acepção de gamificação proposta por [Deterding et al. (2011)](https://doi.org/10.1145/2181037.2181040). O objetivo do produto é apoiar **participação recorrente com aprendizagem**, não maximizar pontos isoladamente. A [Visão do Produto](visao.md) e a [Lean Inception](lean_inception.md) já estabelecem esse vínculo.

A teoria da autodeterminação de [Ryan e Deci (2000)](https://selfdeterminationtheory.org/SDT/documents/2000_RyanDeci_SDT.pdf) orienta três cuidados de projeto: competência (feedback que ajuda a entender o erro e perceber avanço), autonomia (escolha de tema e dificuldade, metas compreensíveis) e vínculo social (comparação voluntária e respeitosa). São **critérios de desenho**, não efeitos já demonstrados no AnatoQuizUp. A revisão de [Hamari, Koivisto e Sarsa (2014)](https://doi.org/10.1109/HICSS.2014.377) encontrou resultados dependentes do contexto; a metanálise de [Sailer e Homner (2020)](https://doi.org/10.1007/s10648-019-09498-w) reforça a necessidade de medir resultados cognitivos, motivacionais e comportamentais separadamente. Portanto, acessos, XP e posição no ranking não servem, sozinhos, como prova de aprendizagem.

O ciclo pretendido é: **escolher conteúdo → responder → receber correção e explicação → concluir a rodada → receber XP → acompanhar progresso → voltar a estudar**. ATP e missões reforçam esse ciclo. Quando a revisão de erros estiver disponível, ela deverá ligar o feedback à próxima atividade de estudo; não se deve afirmar que esse trecho já está entregue.

## 2. Da proposta herdada à versão 2026.2

| Elemento | Base de 2026.1 | Evolução em 2026.2 |
| --- | --- | --- |
| ATP | Recompensa por acerto de questão e uso na loja, registrada nas [decisões DP22 e DP26](https://github.com/fga-eps-mds/2026-1-AnatoQuizUp-Doc/blob/main/docs/decisoes/decisoes.md) | Mantido como moeda de loja; saldo e transações rastreados no Quiz-Service. Não é o mesmo saldo que XP. |
| Loja e avatar | Cosméticos, conquistas e personalização constam da [Release Major 3 de 2026.1](https://github.com/fga-eps-mds/2026-1-AnatoQuizUp-Doc/blob/main/docs/backlog/release-major-3.md) | Loja e personalização do avatar foram o foco da R1 de 2026.2; itens cosméticos representam identidade, sem vantagem pedagógica automática. |
| Ranking | A comparação entre estudantes já existia, conforme o [backlog de 2026.1](https://github.com/fga-eps-mds/2026-1-AnatoQuizUp-Doc/blob/main/docs/backlog/release-major-3.md) | Ranking geral e de amigos passou a ordenar por XP total; o elo atual é exibido separadamente. Rankings de turma e lista têm regras próprias. |
| XP e nível | O mapa de conquistas e níveis era uma proposta no [levantamento de requisitos de 2026.1](https://github.com/fga-eps-mds/2026-1-AnatoQuizUp-Doc/blob/main/docs/backlog/requisitos.md) | Conclusão de rodada gera XP e nível calculado por curva explícita, com histórico e proteção contra crédito duplicado. |
| Missões e elos | Não havia uma regra integrada de missão diária ou elo no recorte herdado aqui analisado | Em 2026.2 foram definidos elos, perda/recuperação por inatividade e missões diárias. A equipe informou que os POs também validaram **missões semanais como escopo**; regras, implementação e evidência dessa decisão ainda precisam ser registradas. |

Essa comparação descreve os artefatos consultados, sem presumir que toda ideia anterior tenha sido implantada ou validada. As regras atuais abaixo se baseiam no código de 2026.2 e no documento [Missões Diárias](missoes-diarias.md).

## 3. Regras do produto

### 3.1 ATP: moeda de uso na loja

- O Quiz-Service concede **10 ATP** no primeiro acerto de uma questão fácil, **25 ATP** de uma média e **50 ATP** de uma difícil. Acertos repetidos da mesma questão não concedem a recompensa novamente. A regra está em [`quiz.service.ts`](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Quiz-Service/blob/main/src/modules/quiz/quiz.service.ts) e na persistência da resposta.
- Apenas o papel **ALUNO** recebe as recompensas do quiz livre. Respostas de listas de turma não geram ATP, XP ou progresso de missões diárias nas regras atuais.
- ATP compra itens na loja. A compra debita o saldo e registra uma transação; a aplicação não permite saldo insuficiente. O [Quiz-Service](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Quiz-Service/blob/main/src/modules/loja/loja.repository.ts) guarda saldo e extrato. ATP **não se converte em XP** por regra geral.
- O potencializador **Café do Foco** pode conceder ATP extra no primeiro acerto elegível após ativação. Esse bônus é de ATP, não de XP; a lógica atual está em [`uso-item.repository.ts`](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Quiz-Service/blob/main/src/modules/loja/uso-item.repository.ts). Os demais itens devem seguir suas regras específicas de catálogo, sem supor que todo item altera a pontuação.

### 3.2 XP, níveis e histórico

- Uma rodada tem até **10 questões**. Ao concluí-la com todas respondidas, o estudante recebe `5 × quantidade de questões` de XP base, mais **5/10/15 XP por acerto** em questão fácil/média/difícil. A função aceita um campo de bônus de potencializador, mas o plano não assume que haja hoje um item que conceda XP extra. Ver [`progressao.constants.ts`](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Quiz-Service/blob/main/src/modules/progressao/progressao.constants.ts) e [`progressao.regras.ts`](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Quiz-Service/blob/main/src/modules/progressao/progressao.regras.ts).
- O aluno começa no **nível 1**. Sair do nível `N` custa `100 × N` XP; o XP acumulado mínimo para alcançar o nível `N` é `100 × N × (N − 1) / 2`. O XP total permanece acumulado.
- Concluir novamente a mesma tentativa retorna o resultado já registrado e **não credita XP em duplicidade**. O histórico distingue a origem `QUIZ_CONCLUIDO` de `MISSAO_CONCLUIDA`. Consulta de progresso e histórico: `GET /api/v1/quiz/progresso` e `GET /api/v1/quiz/xp/historico`.
- XP indica atividade reconhecida pelo sistema. A qualidade da aprendizagem deve ser avaliada também por acertos, dificuldades, revisão e retorno ao estudo.

### 3.3 Elos e inatividade

| Elo | XP de elo mínimo | XP de elo máximo |
| --- | ---: | ---: |
| Curioso | 0 | 499 |
| Acadêmico | 500 | 1.499 |
| Interno | 1.500 | 2.999 |
| R1 | 3.000 | 5.999 |
| R3 | 6.000 | 9.999 |
| R6 | 10.000 | 14.999 |
| Staff do serviço | 15.000 | Sem limite |

O código distingue **XP total** (histórico permanente), **XP de elo** (base para o elo atual), **elo atual** e **maior elo já conquistado**. Uma queda por inatividade reduz o XP de elo até a faixa anterior; não apaga XP total nem o maior elo. A recuperação exige novos quizzes válidos até alcançar novamente a faixa. Missões também creditam XP total e XP de elo, mas **a recompensa da missão não reinicia a contagem de inatividade**: a atividade válida para isso é concluir um quiz que conceda XP. Ver [#82](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/82), [#89](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/89) e [`inatividade.regras.ts`](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Quiz-Service/blob/main/src/modules/progressao/inatividade.regras.ts).

**Prazos registrados na [#89](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/89) e implementados como padrão em 26/10:** aviso aos 7 dias sem quiz válido, estado de risco aos 8, primeiro rebaixamento aos 9 e novos rebaixamentos a cada 14 dias adicionais, respeitado o elo mínimo Curioso. Segundo a equipe, os POs validaram a regra com a redução do prazo para cair de elo; os números acima são os que constam da issue e do código. Prazos podem ser configurados por administrador. Indisponibilidades reconhecidas da plataforma são descontadas. Os cenários de aceite da #89 ainda contêm exemplos de 6 e 8 dias que precisam ser alinhados à tabela principal de prazos antes da homologação.

Avisos, risco, rebaixamento, retorno e recuperação devem usar mensagens que expliquem a ação possível e preservem o histórico do aluno. A percepção de desmotivação deve ser medida após a implantação; aprovação da regra não equivale a comprovação do efeito motivacional.

### 3.4 Ranking e privacidade

O **ranking geral e o de amigos** ordenam por XP total; os desempates são mais acertos, menos questões respondidas e atividade mais antiga. O elo mostrado é o **atual**, que pode ser inferior ao maior elo já conquistado após inatividade. Assim, duas pessoas podem ter o mesmo elo e posições diferentes, ou o elo cair sem apagar XP total. Ver [`ranking.service.ts` do Quiz-Service](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Quiz-Service/blob/main/src/modules/ranking/ranking.service.ts) e [`ranking.service.ts` do BFF](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-BFF/blob/main/src/modules/ranking/ranking.service.ts).

O BFF compõe pontuação com nome e avatar. Entre estudantes, deve respeitar a visibilidade do perfil; a própria posição pode ser mostrada ao titular. Rankings de **turma e lista** são visões pedagógicas com critérios e permissões próprios, não devem ser descritos como simples cópia do ranking geral. A interface deve indicar qual critério está sendo usado.

### 3.5 Missões

**Missões diárias — regra aprovada em 19/10/2026.** Cada aluno recebe 3 missões sorteadas de um catálogo fixo de 6. O catálogo implementado contém metas de responder 5 ou 10 questões, acertar 5 ou 8 questões e concluir 2 ou 3 quizzes com combinações diferentes de tema e dificuldade, com recompensas de **30, 50 ou 70 XP**. As três missões exibidas a cada dia dependem do sorteio; não se deve prometer 150 XP diários fixos. As entradas estão na [migração do Quiz-Service](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Quiz-Service/blob/main/prisma/migrations/20261022120000_missoes_diarias/migration.sql).

O período vira à meia-noite em `America/Sao_Paulo`. Só ações do quiz livre dentro do período contam; uma mesma questão pontua no máximo uma vez por dia e uma combinação de tema/dificuldade concluída conta uma vez para a missão correspondente. Missão não concluída expira sem recompensa. Conclusão e crédito de XP ocorrem de forma idempotente, com origem identificada no histórico. Há consulta autenticada em `GET /api/v1/missoes/minhas`. O [Quiz-Service #14](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Quiz-Service/pull/14) e o [BFF #10](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-BFF/pull/10) foram integrados; a [interface Web #18](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Web/pull/18) ainda estava em revisão na data deste plano. Para critérios de aceite e estados da interface, consulte [Missões Diárias](missoes-diarias.md).

**Missões semanais — escopo confirmado pela equipe como validado pelos POs.** A confirmação altera o recorte anteriormente registrado como “fora do MVP” no documento de missões diárias. Ainda faltam registro rastreável da decisão, quantidade, catálogo, metas, recompensa, início/fim da semana, fuso, expiração, prevenção de duplicidade e critérios de aceite. O código consultado implementa apenas `periodicidade: DIARIA`; portanto, a aprovação de escopo **não significa entrega técnica**. Atualizar [Missões Diárias](missoes-diarias.md), backlog, EAP e roadmap após detalhar a regra. Missões **mensais** não foram confirmadas neste levantamento.

### 3.6 Conquistas

Além das missões, o Quiz-Service acompanha conquistas por sequência de acertos, total de acertos, acertos por tema e percentual de acerto por tema. Os marcos usam os níveis **Bronze, Prata e Ouro** e podem conceder ATP e item configurado. O desbloqueio é registrado uma única vez por marco, evitando recompensa duplicada. Missão e conquista são mecanismos distintos: a mesma atividade elegível pode avançar os dois, conforme a decisão registrada em [Missões Diárias](missoes-diarias.md). Ver [`conquistas.service.ts`](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Quiz-Service/blob/main/src/modules/conquistas/conquistas.service.ts).

## 4. Critérios de integridade e experiência

1. Recompensas derivam de eventos de estudo verificáveis; abrir a página ou repetir a requisição não concede pontos.
2. Tentativa, transação de XP, transação de ATP e evento de missão devem permitir rastrear origem e evitar crédito duplicado. O aluno não pode alterar saldos ou progresso diretamente.
3. O feedback da questão deve continuar legível mesmo quando houver recompensa. O incentivo precisa conduzir ao conteúdo e à explicação, não apenas à próxima fonte de pontos.
4. Ranking e notificações de elo devem respeitar permissões e privacidade. Avisos de perda de elo não devem sugerir perda de XP histórico ou de título acadêmico real.
5. Ajustes de valores e prazos exigem registro de decisão, revisão dos testes e análise do efeito sobre estudantes. Mudança de regra não deve apagar histórico sem uma migração explícita.

## 5. Validação e evolução

| Pergunta | Indicador sugerido | Fonte/limite |
| --- | --- | --- |
| A gamificação acompanha o estudo? | Quizzes iniciados e concluídos; acertos por tema/dificuldade; retorno em 7 e 30 dias | Definir coorte, período e eventos; comparar com uso de XP e missões. |
| O feedback leva à correção de dificuldades? | Revisão de erros e mudança de acerto após revisão | Depende da entrega e instrumentação da US08; não usar XP como substituto. |
| As missões levam a ações educacionais? | Missões atribuídas, iniciadas e concluídas; quiz concluído após missão | Separar aluno ativo de missão disponível; conferir eventos únicos. |
| O ranking apoia ou prejudica? | Uso do ranking, visibilidade escolhida, retorno ao estudo, relatos dos alunos | Segmentar sem expor dados pessoais e combinar dados com pesquisa qualitativa. |
| A perda de elo afeta a permanência? | Avisos, rebaixamentos, recuperações, retorno e abandono após aviso | Comparar períodos e ouvir estudantes; avaliar a mudança de prazo aprovada pelos POs. |
| A economia está equilibrada? | ATP emitido, gasto, saldo e uso de itens; XP por quiz e missão | Identificar inflação, concentração e estratégias de repetição; não misturar ATP com XP. |

Antes do aceite da R2, registrar versão implantada, roteiro ponta a ponta, evidências, falhas e decisão do PO, conforme os [critérios de saída do roadmap](roadmap.md). O plano define como avaliar a gamificação; **não registra resultados de campo nem aceite que ainda não foram comprovados**.

### Próximas decisões e rastreabilidade

| Item | Situação | Evidência/ação |
| --- | --- | --- |
| XP, nível e elo | Implementados no código | [#63](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/63), [#82](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/82) e [#89](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/89); validar versão implantada. |
| ATP, loja, avatar e ranking | Implementados, com critérios distintos por tela | Conferir comportamento integrado e privacidade em homologação. |
| Missões diárias | Regras aprovadas; serviço e BFF integrados; Web em revisão | [#83](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/83), [#84](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/84), [Web #18](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Web/pull/18). |
| Missões semanais | Escopo validado segundo informação da equipe; regras e implementação por detalhar | Registrar decisão dos POs, especificar e abrir/atualizar issue de implementação. |
| Prazo menor para rebaixamento | Regra validada segundo informação da equipe; padrão da #89 e do código: aviso em 7 dias, risco em 8 e queda em 9 | Alinhar os exemplos divergentes da #89 e confirmar os valores no ambiente de homologação. |
| Revisão de erros e métricas de aprendizagem | Necessárias para avaliar o objetivo pedagógico | Refinar US08 e instrumentar a validação da R2. |

## Referências

- DETERDING, S.; DIXON, D.; KHALED, R.; NACKE, L. [From Game Design Elements to Gamefulness: Defining “Gamification”](https://doi.org/10.1145/2181037.2181040). *MindTrek*, 2011.
- RYAN, R. M.; DECI, E. L. [Self-Determination Theory and the Facilitation of Intrinsic Motivation, Social Development, and Well-Being](https://selfdeterminationtheory.org/SDT/documents/2000_RyanDeci_SDT.pdf). *American Psychologist*, 55(1), 68–78, 2000.
- HAMARI, J.; KOIVISTO, J.; SARSA, H. [Does Gamification Work? A Literature Review of Empirical Studies on Gamification](https://doi.org/10.1109/HICSS.2014.377). *HICSS*, 2014.
- SAILER, M.; HOMNER, L. [The Gamification of Learning: a Meta-analysis](https://doi.org/10.1007/s10648-019-09498-w). *Educational Psychology Review*, 32, 77–112, 2020.

## Histórico de versão

| Data | Versão | Descrição | Autor(es) | Revisor(es) |
| --- | --- | --- | --- | --- |
| 26/10/2026 | 1.0 | Consolidação da proposta anterior, das regras implementadas e das decisões ainda a registrar | Equipe AnatoQuizUp 2026.2 | A definir na revisão do PR |
