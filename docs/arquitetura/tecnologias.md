# Tecnologias

## Stack por componente

| Componente | Tecnologias |
|---|---|
| **Web** | React 19, TypeScript, Vite, Tailwind CSS 4, React Router 7, Axios, Jest |
| **BFF** | Node.js 24, TypeScript, Express 5, Axios, Zod, jsonwebtoken, Multer, Pino, Helmet, CORS, Jest |
| **Usuario-Service** | Node.js 24, TypeScript, Express 5, Prisma, PostgreSQL, bcryptjs, jsonwebtoken, Zod, Brevo (e-mail), Pino, Helmet, CORS, Jest |
| **Quiz-Service** | Node.js 24, TypeScript, Express 5, Prisma, PostgreSQL, MinIO / AWS SDK S3, Multer, Puppeteer + EJS (PDF), jsonwebtoken, Zod, Pino, Helmet, CORS, Jest |

## Infraestrutura e ferramentas

| Categoria | Ferramenta | Uso |
|---|---|---|
| Containers | Docker (`node:24-alpine`) e Docker Compose | Execução local e testes E2E com `web`, `bff`, `backend-user`, `backend-quiz`, `db-user`, `db-quiz` e `minio` |
| Banco de dados | PostgreSQL 18 | Um banco por serviço |
| Armazenamento | MinIO (compatível com S3) | Imagens das questões e itens |
| CI | GitHub Actions | Lint, build, testes com cobertura mínima de 85% e análise no SonarCloud |
| Qualidade | SonarCloud | Cobertura, duplicação, complexidade e segurança |
| Segurança | `tcc-security-gate.yml` | Verificação de segurança nos PRs |
| Release | `release.yml` | Versionamento por tag semântica |
| Métricas | `metricas.yml` + `sonar_scripts/parser.py` | Exporta métricas `.json` para `analytics-raw-data/` no repositório de Doc |
| Documentação | MkDocs Material + GitHub Pages | Este site |
| Dashboard | Streamlit | Painel de métricas da release (`dashboard/app.py`) |
| Gestão | ZenHub, Figma, Microsoft Teams | Quadro, protótipos e comunicação |

## Justificativa das principais escolhas

- **TypeScript em todo o stack:** tipagem única entre frontend e backend e menor custo de troca de contexto para o time.
- **Express 5:** simples e com suporte nativo a handlers assíncronos. É conhecido pela maioria do time (ver quadro de conhecimento).
- **Prisma:** migrations versionadas e tipagem gerada a partir do schema, o que reduz erros de acesso a dados.
- **Zod:** validação de entrada declarativa, compartilhando o formato entre DTOs e mensagens de erro.
- **Puppeteer + EJS:** geração de PDF das listas a partir de HTML, reaproveitando o estilo das telas.

## Histórico de Versão

| Data | Versão | Descrição | Autor(es) |
| :--- | :--- | :--- | :--- |
| 28/09/2026 | 1.0 | Criação do documento de tecnologias de 2026.2 | [Henrique Carvalho](https://github.com/henriquecarv3), [Caio Habibe](https://github.com/CaioHabibe), [João Lucas](https://github.com/jlucasiqueira), [Rafael Melo](https://github.com/rmatuda) |