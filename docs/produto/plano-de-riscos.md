# Plano de Gerenciamento de Riscos - AnatoQuizUp

## Histórico de Versão

| Data | Versão | Descrição | Autor |
| :---: | :---: | :--- | :--- |
| 17/09/2026 | 1.0 | Criação e estruturação do plano de riscos | [João Paulo Lima](https://github.com/jpaulohe4rt) |

---

O Plano de Gerenciamento de Riscos tem como objetivo perceber e tratar pequenos riscos de forma contínua para evitar que cresçam e inviabilizem o desenvolvimento da plataforma AnatoQuizUp. Um risco é um evento incerto calculado a partir da probabilidade de sua manifestação e do impacto gerado nos pilares de custo, tempo, escopo e qualidade do projeto. 

## 1. Estrutura Analítica de Riscos (EAR)

A Estrutura Analítica de Riscos (EAR) agrupa e organiza as possíveis fontes de risco em categorias e níveis hierárquicos[cite: 7]. Para o AnatoQuizUp, os riscos foram mapeados em quatro frentes principais:

*   **Técnico:** Riscos associados à definição de requisitos, adoção de novas tecnologias (modelos de IA, chatbots), complexidade arquitetural e qualidade do produto final.
*   **Externo:** Fatores fora do controle direto da equipe de desenvolvimento, como indisponibilidade de clientes/stakeholders, questões de saúde, paralisações na universidade e dependência de dados externos (termos de consentimento e LGPD de pacientes).
*   **Organizacional:** Riscos gerados por dependências estruturais, gerenciamento de recursos, priorização equivocada de histórias e nível de habilidade individual dos membros da equipe.
*   **Gerenciamento do Projeto:** Riscos que podem afetar o tempo de produção, envolvendo falhas de comunicação, estimativas equivocadas nas sprints, planejamento falho e execução de atividades.

---

## 2. Análise Quantitativa

A quantificação dos riscos é baseada na definição de pesos para a Probabilidade de ocorrência e para o Impacto no projeto.

### 2.1. Probabilidade
| **Probabilidade** | **Intervalo** | **Peso** |
| :---: | :---: | :---: |
| **Muito Alta** | 81% a 100% | 5 |
| **Alta** | 61% a 80% | 4 |
| **Média** | 41% a 60% | 3 |
| **Baixa** | 21% a 40% | 2 |
| **Muito Baixa** | 0% a 20% | 1 |
> Fonte dos intervalos e pesos.

### 2.2. Impacto
| **Impacto** | **Descrição** | **Peso** |
| :---: | :--- | :---: |
| **Muito Alto** | O impacto inviabiliza o projeto ou gera cancelamento. | 5 |
| **Alto** | Há grande impacto no desenvolvimento do projeto. | 4 |
| **Médio** | Possui certo impacto, porém é facilmente recuperado. | 3 |
| **Baixo** | Pouco impacto no desenvolvimento do projeto. | 2 |
| **Muito Baixo** | Impacto pouco expressivo no desenvolvimento. | 1 |
> Fonte das descrições de impacto[cite: 7].

### 2.3. Matriz de Prioridade (Probabilidade x Impacto)
A partir da multiplicação dos pesos de Probabilidade e Impacto, determina-se a urgência das ações de mitigação.

| **Probabilidade / Impacto** | **Muito Baixo (1)** | **Baixo (2)** | **Médio (3)** | **Alto (4)** | **Muito Alto (5)** |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Muito Alta (5)** | 5 | 10 | 15 | 20 | 25 |
| **Alta (4)** | 4 | 8 | 12 | 16 | 20 |
| **Média (3)** | 3 | 6 | 9 | 12 | 15 |
| **Baixa (2)** | 2 | 4 | 6 | 8 | 10 |
| **Muito Baixa (1)** | 1 | 2 | 3 | 4 | 5 |

**Faixas de Prioridade:**
*   **Muito Baixa:** 1 a 5.
*   **Baixa:** 6 a 10.
*   **Média:** 11 a 15.
*   **Alta / Muito Alta:** 16 a 25.

---

## 3. Identificação e Plano de Ação dos Riscos

Abaixo estão os principais riscos identificados para o ciclo de desenvolvimento do AnatoQuizUp, juntamente com suas estratégias de prevenção e contingência.

| ID | Risco | Categoria EAR | Prob. | Imp. | Prevenção (Mitigação) | Plano de Ação (Contingência) |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| **RN01** | Integrantes podem não estar familiarizados com as tecnologias adotadas (IA, LLMs, Chatbots)[cite: 7]. | Organizacional | Média | Alto | Promover treinamentos internos e incentivar programação em pares (pareamento). | Alocar os membros com mais conhecimento técnico em conjunto com os que possuem mais dificuldades. |
| **RN02** | Indisponibilidade do cliente para validação de requisitos ou envio de materiais (ex: planilhas e casos OSCE). | Externo | Alta | Muito Alto | Manter comunicação constante com o cliente e agendar validações periódicas. | Utilizar dados mockados e seguir o desenvolvimento da base da aplicação até a recepção dos dados reais. |
| **RN03** | Vazamento de dados não anonimizados de pacientes nos casos clínicos de simulação. | Externo | Baixa | Muito Alto | Adotar rigoroso processo de anonimização e exigir termos de consentimento antes da inserção na base. | Remover imediatamente os dados do ar, notificar stakeholders e aplicar scripts de limpeza no banco de dados. |
| **RN04** | Tarefas estimadas de forma equivocada, gerando atraso na execução da Sprint. | Gerenciamento | Alta | Médio | Quebrar tarefas muito grandes ou complexas em pequenas entregas durante a planning[cite: 7]. | Realocar tarefas como dívida técnica para a próxima Sprint e reforçar o pareamento. |
| **RN05** | Complexidade inesperada na automatização e integração do modelo de IA (DevOps/Arquitetura). | Técnico | Baixa | Muito Alto | Entender a capacidade e as limitações das tecnologias antes da implementação[cite: 7]. | Repriorizar o escopo do MVP junto ao cliente e, se necessário, utilizar um fluxo fixo de conversas em vez de um LLM treinado[cite: 7]. |
| **RN06** | A qualidade do software e dos quizzes não corresponder às expectativas educacionais do cliente. | Técnico | Média | Muito Alto | Validar constantemente os requisitos com o cliente e manter a qualidade do código com testes. | Realizar refatoração de código, ajustes de escopo nas questões e nova rodada de validação. |
| **RN07** | Um ou mais membros desistirem da disciplina ou ficarem ausentes temporariamente. | Organizacional | Alta | Alto | Conhecer as habilidades da equipe e entregar tarefas não blocantes para membros menos engajados[cite: 7]. | Realocar imediatamente as tarefas críticas entre os membros remanescentes. |