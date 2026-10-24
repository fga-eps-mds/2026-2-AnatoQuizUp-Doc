# Roteiro de testes de sistema

## Apresentação

Este documento orienta a execução manual dos testes de sistema do AnatoQuizUp. Os procedimentos verificam o comportamento observado na aplicação Web, utilizando os serviços integrados do ambiente de homologação.

O roteiro pode ser repetido a cada versão publicada. Os resultados, as capturas e as limitações da primeira execução estão em [Resultados dos testes](resultados-testes.md).

## Escopo

Os testes cobrem os fluxos da [Release Major 1](../backlog/release-major-1.md): avatar padrão, personalização de aparência e acessórios, loja, uso de potencializadores e histórico. Autenticação e isolamento entre contas são verificados como apoio a esses fluxos.

Testes unitários, de integração, carga e segurança da API exigem verificações próprias. Esta execução pode apoiar o aceite do produto, mas não substitui a validação dos responsáveis pelo produto.

## Ambiente e preparação

Utilizar a [homologação do AnatoQuizUp](https://anatoquizup-homolog-2026-2.netlify.app), conforme o [guia do ambiente](../operacao/ambiente-homologacao.md).

Antes de executar:

1. Registrar data, responsável, navegador e versões dos componentes publicados. Se uma versão não estiver disponível, indicar essa limitação no resultado.
2. Separar duas contas de aluno para testes, identificadas como A e B, e uma conta de professor. Para o primeiro acesso, usar uma conta nova sem personalização anterior.
3. Preparar saldo, um item com preço conhecido, inventário e potencializador com regra de uso confirmada. Anotar os valores antes de alterar os dados.
4. Confirmar que as contas e os dados podem ser usados em testes. Não publicar senhas ou tokens nem modificar dados de usuários reais.

Os casos de compra e utilização deixam dados para a consulta do histórico. Ao repetir a execução, registrar o novo estado inicial. Não esgotar estoques ou editar bancos apenas para preparar uma condição de teste.

O avatar cérebro de **Meu avatar** é diferente da imagem e do fundo do cartão de perfil. Nos casos de avatar, utilizar o personagem cérebro.

## Organização dos casos

Os códigos identificam cada **caso de teste** e relacionam seus procedimentos aos resultados e às evidências. O formato adotado neste roteiro é `CT-GRUPO-NÚMERO`.

Por exemplo, **CT-AU-01** significa **Caso de Teste de Autenticação, número 01**. A numeração é sequencial dentro de cada grupo.

| Sigla | Significado |
|---|---|
| CT | Caso de teste |
| AU | Autenticação |
| AV | Avatar |
| LJ | Loja |
| PT | Potencializadores |
| HI | Histórico |
| AC | Controle de acesso |

| Identificador | Verificação |
|---|---|
| CT-AU-01 | Entrada, saída e acesso a páginas protegidas |
| CT-AV-01 | Avatar padrão no primeiro acesso |
| CT-AV-02 | Prévia e manutenção da personalização |
| CT-AV-03 | Restrição de item não adquirido |
| CT-AV-04 | Restauração do padrão e preservação do inventário |
| CT-LJ-01 | Compra com saldo suficiente |
| CT-LJ-02 | Cancelamento de compra |
| CT-LJ-03 | Compra sem saldo suficiente |
| CT-PT-01 | Uso de potencializador válido |
| CT-PT-02 | Tentativa de uso inválido |
| CT-HI-01 | Histórico de compras e utilizações |
| CT-AC-01 | Isolamento entre contas de aluno |
| CT-AC-02 | Permissão de acesso à edição do avatar |

## Procedimentos

Cada caso apresenta o requisito de referência, as condições necessárias e os passos com seus resultados esperados.

### CT-AU-01 — Entrar e encerrar a sessão

**Referência:** pré-condição dos fluxos da R1.

**Pré-condições:** conta de aluno de teste ativa; usuário deslogado.

1. Entrar com as credenciais válidas. **Esperado:** acesso à área autenticada da conta correta.
2. Encerrar a sessão. **Esperado:** retorno à área pública, sem acesso aos dados autenticados.
3. Tentar abrir diretamente uma página protegida e recarregá-la. **Esperado:** solicitação de autenticação, sem exibição de dados privados.

### CT-AV-01 — Avatar padrão no primeiro acesso

**Referência:** US01, [#27](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/27).

**Pré-condições:** conta nova de aluno, sem personalização anterior; forma de criação da conta confirmada.

1. Acessar a conta pela primeira vez e abrir o perfil. **Esperado:** exibição do avatar padrão definido para a versão, sem imagem quebrada.
2. Sair e entrar novamente sem personalizar. **Esperado:** manutenção do mesmo avatar padrão.

### CT-AV-02 — Pré-visualizar e manter a personalização entre sessões

**Referência:** US02, [#26](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/26).

**Pré-condições:** aluno A autenticado; opções de aparência e acessórios disponíveis no seu inventário.

1. Abrir a personalização e selecionar Aparência e Acessórios. **Esperado:** opções correspondentes a cada categoria.
2. Alterar a cor e equipar uma opção disponível. **Esperado:** pré-visualização atualizada antes de salvar.
3. Salvar, se houver controle explícito, e consultar novamente o avatar. **Esperado:** avatar com as escolhas salvas. Registrar a presença ou ausência de mensagem como observação de feedback; sua ausência, isoladamente, não reprova o requisito de persistência.
4. Sair, entrar novamente e consultar o perfil e a personalização. **Esperado:** escolhas mantidas após a nova sessão.

### CT-AV-03 — Impedir equipamento de item não adquirido

**Referência:** US02, #26.

**Pré-condições:** aluno autenticado; item de personalização não pertencente ao seu inventário identificado.

1. Localizar o item na personalização. **Esperado:** indicação de indisponibilidade e de aquisição na loja, conforme o requisito.
2. Tentar equipá-lo pelos controles disponíveis. **Esperado:** equipamento impedido.
3. Consultar o avatar salvo e o inventário. **Esperado:** item não equipado nem concedido; estado anterior preservado.

### CT-AV-04 — Restaurar o padrão preservando o inventário

**Referência:** US02, #26.

**Pré-condições:** aluno com avatar personalizado e itens adquiridos; inventário inicial registrado.

1. Restaurar a caracterização padrão e salvar. **Esperado:** avatar padrão exibido.
2. Sair e entrar novamente. **Esperado:** avatar padrão mantido.
3. Consultar o inventário. **Esperado:** itens adquiridos continuam disponíveis, sem perda decorrente da restauração.

### CT-LJ-01 — Comprar com saldo suficiente

**Referência:** US03, [#28](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/28), [#35](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/35).

**Pré-condições:** aluno autenticado; item e quantidade válidos; saldo suficiente; preço, saldo e inventário iniciais registrados.

1. Selecionar o item e a quantidade. **Esperado:** confirmação com item, quantidade e valor coerentes com o catálogo.
2. Confirmar uma única compra. **Esperado:** mensagem de sucesso; item ou quantidade adicionados ao inventário; desconto exatamente igual ao valor confirmado, uma única vez.
3. Recarregar a página e consultar o histórico. **Esperado:** saldo e inventário persistidos; um registro correspondente à compra.

### CT-LJ-02 — Cancelar uma compra

**Referência:** confirmação de compra da US03, #35.

**Pré-condições:** aluno autenticado; saldo, inventário e histórico iniciais registrados.

1. Selecionar um item e abrir a confirmação. **Esperado:** resumo da compra antes de sua efetivação.
2. Cancelar a operação. **Esperado:** nenhuma compra concluída.
3. Conferir saldo, inventário e histórico, inclusive após recarregar. **Esperado:** nenhum desconto, concessão de item ou registro de compra decorrente do cancelamento.

### CT-LJ-03 — Comprar sem saldo suficiente

**Referência:** US03, #28 e #35.

**Pré-condições:** aluno com saldo inferior ao preço da compra; valores iniciais registrados.

1. Tentar comprar o item. **Esperado:** operação impedida com indicação compreensível de saldo insuficiente.
2. Conferir saldo, inventário e histórico após recarregar. **Esperado:** nenhum débito ou concessão de item; nenhuma compra bem-sucedida registrada para a tentativa.

### CT-PT-01 — Utilizar um potencializador válido

**Referência:** US03, [#38](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/38).

**Pré-condições:** aluno com ao menos uma unidade de um potencializador; quantidade inicial registrada. Antes de executar, preencher: **item = ___; condição de uso = ___; efeito esperado observável = ___; fonte da regra = ___**. Sem esses dados, o caso fica bloqueado.

1. Acessar o contexto que atende à condição de uso e selecionar o potencializador. **Esperado:** possibilidade de uso conforme a regra registrada.
2. Confirmar uma utilização. **Esperado:** efeito registrado aplicado e quantidade reduzida em exatamente uma unidade.
3. Consultar inventário e histórico após recarregar. **Esperado:** consumo persistido e um registro correspondente ao uso.

### CT-PT-02 — Impedir utilização inválida

**Referência:** US03, #38.

**Pré-condições:** repetir o caso para cada situação aplicável: item sem unidades e item com condição de uso não atendida. Registrar a condição e a regra correspondente. Registrar inventário e estado inicial do efeito. Para Café do Foco, verificar a tentativa de nova ativação enquanto já existe um efeito ativo, antes do próximo acerto elegível. Executar a variante sem unidades com dados próprios, sem esgotar um estoque por repetição.

1. Tentar utilizar o item pelos controles disponíveis. **Esperado:** utilização impedida, com indicação do motivo.
2. Conferir inventário, efeito e histórico. **Esperado:** nenhuma quantidade negativa, efeito indevido ou utilização bem-sucedida registrada.

### CT-HI-01 — Consultar histórico de compras e utilizações

**Referência:** US03, [#40](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc/issues/40).

**Pré-condições:** aluno com uma compra e uma utilização bem-sucedidas desta execução, com dados e horários anotados.

1. Abrir o histórico. **Esperado:** presença dos registros de compra e utilização correspondentes às operações anotadas.
2. Comparar os dados apresentados com item, quantidade e valores registrados, quando aplicáveis ao tipo de operação. **Esperado:** coerência com as operações efetivadas.
3. Sair, entrar novamente e consultar o histórico. **Esperado:** registros mantidos e sem duplicações causadas pela consulta.

### CT-AC-01 — Preservar a personalização de outra conta

**Referência:** controle de acesso das US01 e US02, #27 e #26.

**Pré-condições:** contas de alunos A e B com aparências identificáveis e registradas; usar sessões separadas ou encerrar completamente uma sessão antes de trocar de conta.

1. Personalizar e salvar o avatar de A. **Esperado:** mudança aplicada a A.
2. Entrar como B e consultar sua própria personalização. **Esperado:** estado anterior de B preservado, sem herdar as escolhas de A.
3. Alterar e salvar B; voltar à conta A. **Esperado:** escolhas de A preservadas.

**Limite:** este caso verifica isolamento observado na interface. Não comprova sozinho a autorização da API contra requisições manipuladas; essa verificação deve ter caso e evidência próprios.

### CT-AC-02 — Restringir edição de avatar ao aluno autenticado

**Referência:** controle de acesso das US01 e US02, #27 e #26.

**Pré-condições:** URL da personalização identificada; conta de professor de teste disponível.

1. Sem autenticação, tentar abrir diretamente a personalização. **Esperado:** acesso à edição negado, sem alteração de avatar.
2. Entrar como professor e tentar acessar a mesma página. **Esperado:** edição de avatar de aluno indisponível, sem alteração de dados.
3. Entrar como aluno. **Esperado:** acesso à edição do próprio avatar permitido.

## Registro dos resultados

Para cada execução, criar um registro com ambiente, período, responsável e versão observada. Identificar o caso e descrever o resultado obtido, os valores antes e depois, as evidências e eventuais limitações.

| Resultado | Critério |
|---|---|
| Aprovado | O comportamento esperado foi observado no escopo executado e sustentado por evidência ou relato identificado. |
| Falhou | Houve diferença entre o comportamento esperado e o obtido. |
| Bloqueado | Uma condição de ambiente, acesso ou dados impediu concluir o teste. |
| Parcial | Somente parte do procedimento foi executada. |
| Não executado | O caso ainda não foi iniciado. |

Uma captura comprova o estado visível da tela, mas não comprova sozinha uma sequência de ações. Identificar quando a conclusão depende do relato de quem executou o teste. Uma página 404 da hospedagem não comprova o controle de permissão da aplicação.

Após uma correção ou nova publicação, repetir os casos afetados e registrar a nova execução, preservando o histórico anterior. Resultados aprovados na interface não comprovam, por si só, persistência remota nem segurança da API.


## Histórico de versão

| Data | Versão | Descrição | Autor(es) | Revisor(es) |
|---|---|---|---|---|
| 23/10/2026 | 1.0 | Procedimentos para os testes de sistema da R1 | [Brenno Oliveira](https://github.com/Brenno-Silva01) | Revisão pendente |
