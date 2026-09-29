# Ambiente de homologação — evidência da R1

## Finalidade e escopo

O ambiente de homologação é a instalação integrada do AnatoQuizUp usada pela equipe para validar fluxos antes de uma demonstração ou de uma futura publicação em produção. Ele não substitui o ambiente local: alterações continuam sendo desenvolvidas e testadas localmente; após revisão e integração na `main`, a versão implantada em homologação é validada com os serviços reais.

O ambiente foi criado na issue [#41 — Criar ambiente de homologação](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/41). Seu objetivo atual é permitir a demonstração e os testes integrados dos fluxos essenciais de autenticação, questões, quiz, ATP, loja e inventário.

> **Classificação:** homologação. Não é um ambiente de produção e não deve receber dados pessoais reais, credenciais de usuários reais ou dados que precisem ser preservados.

## Relação com a Release Major 1

O plano de ensino de EPS estabelece que a R1 contempla planejamento, arquitetura, pipelines, *dashboard* v1, ambiente de implantação e visão do produto; além disso, as releases major devem estar implantadas em homologação na data da apresentação. Este documento registra especificamente a parte operacional dessa evidência: onde a versão integrada está acessível, como ela é atualizada, o que foi validado e quais riscos ou limitações permanecem.

Ele deve ser lido em conjunto com os demais artefatos da R1, e não como substituto deles:

| Evidência da R1 | Artefato relacionado |
| --- | --- |
| Visão, escopo e planejamento do produto | [Visão do Produto](../produto/visao.md), [Roadmap](../produto/roadmap.md), [EAP](../produto/EAP.md) e [Plano de Riscos](../produto/plano-de-riscos.md). |
| Arquitetura e decisões técnicas | [Visão de Arquitetura](../arquitetura/visao-geral.md), [Decisões Arquiteturais](../arquitetura/decisoes.md), [Banco de Dados](../arquitetura/banco-de-dados.md) e [Endpoints](../arquitetura/endpoints.md). |
| Indicadores de projeto, processo e produto | [Dashboard da R1](../dashboards.md). A automação/exportação do SonarCloud ainda é acompanhada na [issue #55](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/55). |
| Ambiente integrado, roteiro de teste e limitações | Esta página e a [issue #41](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/41). |

## Rastreabilidade de implementação

| Item | Evidência | Situação |
| --- | --- | --- |
| Criação do ambiente | [Issue #41](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/41) | Concluída. |
| Armazenamento de imagens opcional em homologação | [Quiz-Service PR #6](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Quiz-Service/pull/6) | Concluído; imagens permanecem desativadas neste ambiente. |
| Dados demonstrativos controlados | [Quiz-Service PR #7](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Quiz-Service/pull/7) e [PR #9](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Quiz-Service/pull/9) | Concluído; a execução exige comando e confirmação explícitos. |
| Compra de item | [Issue #35](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/35), [Web PR #3](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Web/pull/3) e [Quiz-Service PR #2](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Quiz-Service/pull/2) | Validado em homologação. |
| Uso de potencializador | [Issue #38](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/38), [Web PR #4](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Web/pull/4) e [Quiz-Service PR #3](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Quiz-Service/pull/3) | Validado em homologação para o Café do Foco. |
| Histórico, contratos e qualidade da loja | [Issue #40](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/40), [Web PR #6](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Web/pull/6), [BFF PR #3](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-BFF/pull/3) e [Quiz-Service PR #5](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Quiz-Service/pull/5) | Integrado e testado. |
| Divulgação do acesso no Web | [Web PR #10](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Web/pull/10) | Concluído. |

Os links acima permitem partir de uma funcionalidade demonstrada para a issue, os PRs e os repositórios que a modificaram. Eles não substituem a revisão humana nem a explicação do time sobre o código e as decisões tomadas.

## Acesso

| Recurso | Endereço | Uso |
| --- | --- | --- |
| Aplicação Web | <https://anatoquizup-homolog-2026-2.netlify.app> | Acesso de professores e alunos para os testes funcionais. |
| Health check do BFF | <https://minio-homolog.up.railway.app/health> | Verificação simples de disponibilidade da API pública. |

O endereço público do BFF contém `minio-homolog` por ser o domínio já associado ao serviço no Railway. Apesar do nome, ele atende o **BFF**, e não um servidor MinIO ativo. Uma alteração futura pode adotar um domínio com nome mais representativo, sem alterar a arquitetura.

## Arquitetura implantada

```text
Navegador
   |
   v
Web (Netlify)
   |  VITE_API_URL
   v
BFF (Railway, endereço público)
   |-------------------------------|
   v                               v
Usuário-Service (Railway, privado) Quiz-Service (Railway, privado)
   |                               |
   v                               v
PostgreSQL de usuários             PostgreSQL de quiz
```

- **Web:** interface React/Vite entregue pelo Netlify. Todas as chamadas da aplicação usam a variável de build `VITE_API_URL`, apontada para o prefixo `/api/v1` do BFF público.
- **BFF:** único ponto público de API. Valida o JWT, aplica CORS e encaminha as requisições para os serviços internos adequados. Ele não concentra as regras de negócio nem possui banco próprio.
- **Usuário-Service:** autenticação, perfis e dados de usuários. Seu banco PostgreSQL é independente do banco de quiz.
- **Quiz-Service:** questões, temas, respostas, ATP, loja, inventário, conquistas e turmas. Usa um PostgreSQL próprio e recebe chamadas do BFF pela rede privada do Railway.
- **Bancos:** os dois PostgreSQL são persistentes e separados por responsabilidade. Nunca usar o banco de homologação como mecanismo normal de crédito ou correção de dados; isso deve ocorrer via fluxo da aplicação ou scripts controlados pela equipe.

O Web não deve chamar os serviços privados diretamente. O fluxo é sempre **Web → BFF → serviço responsável**.

O diagrama mostra a arquitetura implantada para homologação. A justificativa das escolhas e os contratos de dados permanecem nos documentos de arquitetura ligados na seção anterior, evitando que este guia replique informações e fique desatualizado.

## Configuração operacional

Os valores abaixo são nomes de configuração; seus valores e segredos permanecem somente nas variáveis protegidas da plataforma de hospedagem.

### Web no Netlify

| Configuração | Finalidade |
| --- | --- |
| Repositório Web e branch `main` | Fonte da versão publicada. |
| `VITE_API_URL` | URL pública do BFF acrescida de `/api/v1`. É incorporada durante o build. |

Uma alteração em `VITE_API_URL` exige um novo build/deploy do Web, pois variáveis `VITE_*` são embutidas no bundle gerado.

### Serviços no Railway

| Serviço | Configurações relevantes |
| --- | --- |
| BFF | `BACKEND_URL`, `QUIZ_SERVICE_URL`, `JWT_SECRET_KEY`, `INTERNAL_TOKEN`, `CORS_ORIGINS`, `PORT`. |
| Usuário-Service | `DATABASE_URL`, `JWT_SECRET_KEY`, `INTERNAL_TOKEN`, `CORS_ORIGINS`, `PORT`. |
| Quiz-Service | `DATABASE_URL`, `JWT_SECRET_KEY`, `INTERNAL_TOKEN`, `CORS_ORIGINS`, `PORT`. |

Regras importantes:

1. `JWT_SECRET_KEY` deve ser idêntica no BFF e no Usuário-Service; caso contrário, tokens emitidos no login não serão aceitos.
2. `INTERNAL_TOKEN` deve ser o mesmo no BFF, Usuário-Service e Quiz-Service; ele protege a comunicação interna entre serviços.
3. `CORS_ORIGINS` deve conter a origem do site Netlify de homologação.
4. `BACKEND_URL` e `QUIZ_SERVICE_URL` devem usar os domínios privados fornecidos pelo Railway, e não endereços públicos ou `localhost`.
5. Nunca registrar no repositório valores de `DATABASE_URL`, tokens, chaves JWT ou senhas dos bancos.

## Deploy, dados e atualização

O deploy de homologação deve acontecer **após** a mudança passar por revisão e merge na `main` do repositório correspondente.

1. Confirmar que o PR foi integrado à `main`.
2. Verificar ou iniciar o novo deploy do serviço alterado na respectiva plataforma:
   - Web: Netlify;
   - BFF, Usuário-Service ou Quiz-Service: Railway.
3. Esperar o status de deploy bem-sucedido e verificar o health check público do BFF.
4. Fazer um teste rápido no navegador, pela URL de homologação, do fluxo afetado pela alteração.
5. Registrar falhas, evidências e limitações conhecidas na issue ou no PR relacionado; não corrigir dados manualmente como substituto de uma correção de código.

Quando o Quiz-Service é atualizado, suas migrations são aplicadas no processo de inicialização configurado para o serviço. Migrations alteram a **estrutura** do banco; elas não são, por si só, uma garantia de que haverá conteúdo de teste. O catálogo é sincronizado no deploy.

O cenário demonstrativo de questões, turmas e itens foi carregado por uma seed controlada, implementada no [PR #7](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Quiz-Service/pull/7) e corrigida no [PR #9](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Quiz-Service/pull/9) do Quiz-Service. Essa seed não é disparada no deploy normal: exige uma confirmação explícita e pode reinicializar dados de demonstração. Ela deve ser usada somente por alguém do time que entenda o impacto, após registrar a necessidade na issue ou no PR correspondente.

Em caso de regressão após um deploy, a equipe deve interromper a demonstração do fluxo afetado, registrar o problema e decidir humanamente entre corrigir e publicar uma nova versão ou retornar a uma versão estável na plataforma. Não existe, por enquanto, rollback automatizado documentado; esta é uma lacuna a ser tratada antes de tratar a homologação como pré-produção.

## Roteiro de validação integrado

Antes de uma demonstração, realizar ao menos os seguintes testes manuais:

| Fluxo | Resultado esperado |
| --- | --- |
| Health check do BFF | Resposta HTTP 200 com status `ok`. |
| Login de professor | Acesso às páginas de gestão de questões. |
| Criação de questão sem imagem | Questão persistida e disponível para o quiz. |
| Login de aluno | Acesso à área do aluno e leitura do saldo de ATP. |
| Escolha de tema e dificuldade | Questão ativa é apresentada. |
| Resposta correta | Feedback correto, registro de resolução e crédito de ATP conforme a dificuldade. |
| Loja e inventário | Compra desconta ATP; item aparece no inventário. |
| Café do Foco | Ao usar o item, o próximo acerto concede o ATP normal mais o bônus equivalente. |

Na validação realizada em 28/09/2026, foram confirmados: criação de questões sem imagem por professor; exibição dessas questões para aluno; crédito de 50 ATP por acerto difícil; compra e uso do Café do Foco; e crédito de 25 ATP do acerto médio mais 25 ATP adicionais do efeito do item. A evidência funcional está rastreada pelas [issues #35](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/35), [#38](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/38) e [#40](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/40).

Utilizar contas de teste gerenciadas pela equipe. As credenciais não pertencem a esta documentação e não devem ser publicadas em issues, PRs ou commits.

### Critério de aceite para uma demonstração

Antes de apresentar uma release, a pessoa responsável pelo fluxo deve executar os testes pertinentes, registrar o resultado no PR ou issue e comunicar limitações aos Product Owners. Para o contexto da disciplina, o ambiente implantado demonstra integração; ele não elimina a necessidade de validar requisitos, protótipos, testes e releases com as pessoas donas do produto.

Se uma ferramenta de IA for usada para rascunhar documentação, configuração ou testes, o conteúdo deve ser revisado criticamente por integrantes do time e a reflexão/evidência individual deve ser registrada no `MD_Template.md`, conforme a política da disciplina. A ferramenta não substitui a decisão humana, a revisão de código, a aprovação de PR ou a publicação validada de uma release.

## Limitações conhecidas

As limitações abaixo são conhecidas e devem ser comunicadas em demonstrações, sem apresentá-las como funcionalidades concluídas:

1. **Imagens de questões:** o armazenamento MinIO está temporariamente desativado na homologação, conforme a decisão implementada no [Quiz-Service PR #6](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Quiz-Service/pull/6). O fluxo de questões sem imagem funciona; para a demonstração, criar ou usar apenas questões sem imagem. A restauração de imagens exige configurar uma solução de armazenamento compatível e retestar upload, leitura e remoção de arquivos.
2. **Itens de loja:** o Café do Foco está integrado ao quiz e foi validado. Os demais itens consumíveis presentes no catálogo ainda não têm efeito de jogo integrado e não devem ser usados como demonstração de funcionalidade completa.
3. **Rotas internas da SPA:** a navegação pelo menu funciona. Recarregar diretamente uma rota interna ou abri-la por URL pode resultar em 404 no Netlify, pois o fallback de SPA ainda não foi configurado. Durante os testes, acessar as telas pelo menu a partir da página inicial.
4. **Dados de homologação:** saldos, questões e resoluções são dados de teste persistentes. Eles podem ser alterados por testes da equipe e não devem ser interpretados como métricas reais.

## Próximos passos

- Configurar e validar um armazenamento de objetos para restaurar o suporte a imagens de questões.
- Evoluir a seed de homologação para uma opção idempotente, restrita a dados demonstrativos e sem remoção de dados existentes.
- Configurar fallback de SPA no Netlify para suportar refresh e acesso direto às rotas internas.
- Implementar e testar o efeito dos demais itens consumíveis ou ocultá-los até que estejam funcionais.
- Definir uma rotina de deploy automatizado e de rollback documentada antes de usar o ambiente como pré-produção.
- Concluir a [issue #55](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/55) para fortalecer a rastreabilidade automática de métricas de qualidade no dashboard.
