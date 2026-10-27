# Ata de Reunião — Arquitetura do Simulador OSCE e Chatbot

## Informações Gerais

| **Campo** | **Detalhes** |
| --- | --- |
| **Pauta** | Alinhamento funcional e técnico do simulador OSCE, definição da estratégia de uso de modelos de linguagem, avaliação por rubricas, casos clínicos e infraestrutura. |
| **Data** | 26/10/2026 |
| **Horário** | Não informado |
| **Tipo de reunião** | [x] Reunião semanal com Product Owners e alinhamento técnico |

## Participantes

| **Nome** | **Presença** |
| --- | --- |
| Brenno da Silva Oliveira | [x] Presente |
| Henrique Carvalho Neves | [x] Presente |
| Hugo de Verson Santana Camilo Jorge | [x] Presente |
| João Paulo Lima da Silva | [x] Presente |
| Leticia Torres Soares Martins | [x] Presente |
| Neysa Aparecida Tinoco Regattieri | [x] Presente |
| Vinicius de Carvalho Rispoli | [x] Presente |

## Discussões e Decisões

| **#** | **Tópico discutido** | **Principais pontos** | **Decisão tomada** |
| ---: | --- | --- | --- |
| 1 | Escopo do simulador OSCE | O simulador deverá permitir a escolha de estações clínicas, conduzir uma entrevista com um paciente virtual e gerar variações controladas dos casos sem descaracterizar o protocolo. | O chatbot será orientado por casos e protocolos estruturados, com liberdade limitada para variar persona, sintomas e contexto. |
| 2 | Protótipo com modelo de linguagem | Foi demonstrado um protótipo que usa Gemini para gerar a persona, conduzir a conversa e avaliar a consulta. A equipe já possuía uma implementação semelhante. | O Gemini será mantido no curto prazo para viabilizar a entrega da disciplina, com a integração desacoplada para permitir a troca futura do modelo. |
| 3 | Avaliação por rubricas | A precisão da avaliação foi apontada como risco. Foi proposto que cada caso contenha critérios objetivos, respostas esperadas e pontuação. | A avaliação será baseada em rubricas derivadas do protocolo OSCE, verificando itens como apresentação, cordialidade, perguntas realizadas e respostas corretas. |
| 4 | Arquitetura de dados e prompts | Foram discutidas alternativas como fine-tuning e RAG. Os casos clínicos e protocolos possuem estrutura definida. | Não será feito fine-tuning. Cada caso será representado como dado estruturado, preferencialmente em JSON, e enviado ao modelo com um prompt alinhado; a solução não dependerá de um RAG documental. |
| 5 | Alternativas ao Gemini | Foram avaliados Copilot e modelos abertos executados em infraestrutura própria. A licença institucional do Copilot não oferece API externa adequada para a integração. | O Copilot foi descartado para esta implementação. Modelos abertos e infraestrutura da STI permanecem como caminho de médio prazo. |
| 6 | Infraestrutura | Uma solução autônoma exigirá servidor com GPU. A obtenção de ambiente na STI pode ultrapassar o tempo restante da disciplina. | No curto prazo, o desenvolvimento seguirá com a API do Gemini; em médio prazo, será avaliada a implantação de um modelo interno na infraestrutura da UnB. |
| 7 | Casos clínicos e imagens | Os primeiros casos disponíveis incluíam materiais com e sem imagens. A geração de novas imagens exigiria outra solução técnica. | A primeira versão priorizará casos clínicos sem imagens. Aproximadamente três casos autorais serão usados como base para gerar variações na mesma linha. |
| 8 | População do banco e planilha de questões | A planilha anterior estava vazia e possuía campos que não eram necessários ao Product Owner. Também foi discutida a preparação do ambiente para implantação na Faculdade de Medicina. | A equipe do projeto não assumirá a população do banco; essa atividade ficará com a equipe da Faculdade de Medicina. A planilha será simplificada e compartilhada com Neysa e Hugo. |
| 9 | Empacotamento e implantação | Foi observado que alguns repositórios possuem Dockerfile, mas nem todos contam com Docker Compose. | A estrutura de containerização deverá ser revisada para apoiar a implantação pelo técnico da Faculdade de Medicina. |
| 10 | Comunicação técnica | Vinicius foi incluído no canal da equipe para apoiar dúvidas específicas sobre o modelo e a arquitetura. | As dúvidas serão encaminhadas pelo Discord e reuniões adicionais serão combinadas previamente quando necessário. |

## Ações e Próximos Passos

| **#** | **Ação** | **Responsável** | **Prazo** |
| ---: | --- | --- | --- |
| 1 | Enviar aproximadamente três casos OSCE autorais, com autorização de uso e, quando disponível, a respectiva rubrica de avaliação. | Hugo de Verson Santana Camilo Jorge | Até 28/10/2026 |
| 2 | Refinar os parâmetros já mapeados para os casos e implementar a avaliação por rubricas. | Equipe de desenvolvimento | Próxima entrega do projeto |
| 3 | Manter a integração com o Gemini desacoplada para permitir a substituição futura do modelo. | Equipe de desenvolvimento | Durante a implementação do simulador |
| 4 | Disponibilizar no Discord a referência do capítulo 14 utilizada como exemplo de estrutura OSCE. | Henrique Carvalho Neves | Não definido |
| 5 | Compartilhar com Neysa e Hugo a versão simplificada da planilha de questões. | Henrique Carvalho Neves | Não definido |
| 6 | Avaliar, com a STI, a disponibilidade futura de infraestrutura com GPU para hospedar um modelo aberto. | Neysa Aparecida Tinoco Regattieri e responsáveis pela infraestrutura | Médio prazo |
| 7 | Revisar Dockerfiles e a disponibilidade de Docker Compose nos repositórios necessários à implantação. | Equipe de desenvolvimento | Antes da implantação na Faculdade de Medicina |
| 8 | Realizar a próxima reunião de acompanhamento. | Equipe e Product Owners | 29/10/2026 às 19:30 |

## Observações Adicionais

- A reunião teve duração registrada de 54 minutos e 23 segundos.
- Hugo participou de parte da reunião devido às atividades no internato.
- A geração ou transformação de imagens clínicas não integra o escopo inicial do simulador.
- O uso do Gemini foi definido como solução de curto prazo para a entrega acadêmica, não como decisão definitiva de infraestrutura para produção.

## Histórico de Versão

| **Data** | **Versão** | **Descrição** | **Autor(es)** | **Revisor(es)** |
| --- | --- | --- | --- | --- |
| 26/10/2026 | 1.0 | Criação da ata a partir da transcrição da reunião. | [Leticia](https://github.com/leticiatmartins) | Gabriel |
