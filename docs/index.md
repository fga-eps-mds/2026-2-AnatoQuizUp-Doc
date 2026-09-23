<style>
/* Identidade visual aplicada apenas à página inicial.*/
.anato-logo { display: block; width: 300px; max-width: 100%; height: auto; margin: 0 auto 1.5rem; }
.anato-equipe { display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 24px 16px; margin: 24px 0; }
.anato-equipe .integrante { display: flex; flex-direction: column; align-items: center; gap: 10px; text-align: center; font-size: 14px; line-height: 1.4; }
.anato-equipe img { border-radius: 50%; object-fit: cover; width: 80px; height: 80px; }
[data-md-color-scheme="slate"]:has(.anato-inicio) .md-typeset a { color: #5de2cd; }
</style>

<div class="anato-inicio"></div>

# AnatoQuizUp

<img class="anato-logo"
     src="assets/images/anatoquizup-logo.png"
     alt="Logo do AnatoQuizUp"
     width="718"
     height="632">

## Sobre o projeto

O **AnatoQuizUp** é uma plataforma educacional voltada ao aprendizado de **anatomia radiológica**. Sua proposta combina questões, gamificação e apoio de chatbot para tornar os estudos mais interativos e auxiliar professores no acompanhamento da aprendizagem.

Este site reúne a documentação, o planejamento e os artefatos produzidos pela equipe ao longo do desenvolvimento do projeto.

## Equipe

<div class="anato-equipe">
  <a href="https://github.com/arthurfonsecaa" class="integrante"><img src="https://avatars.githubusercontent.com/u/169956243?v=4" alt="" width="80" height="80" loading="lazy"><span>Arthur Fonseca Vale</span></a>
  <a href="https://github.com/Brenno-Silva01" class="integrante"><img src="https://avatars.githubusercontent.com/u/117456300?v=4" alt="" width="80" height="80" loading="lazy"><span>Brenno da Silva Oliveira</span></a>
  <a href="https://github.com/caiohabibe" class="integrante"><img src="https://avatars.githubusercontent.com/u/117680471?v=4" alt="" width="80" height="80" loading="lazy"><span>Caio Falcao Habibe Costa</span></a>
  <a href="https://github.com/dudupaz" class="integrante"><img src="https://avatars.githubusercontent.com/u/122990784?v=4" alt="" width="80" height="80" loading="lazy"><span>Carlos Eduardo de Sousa Paz</span></a>
  <a href="https://github.com/gabrielfreitass1" class="integrante"><img src="https://avatars.githubusercontent.com/u/56280085?v=4" alt="" width="80" height="80" loading="lazy"><span>Gabriel Freitas Balbino</span></a>
  <a href="https://github.com/henriquecarv3" class="integrante"><img src="https://avatars.githubusercontent.com/u/134213039?v=4" alt="" width="80" height="80" loading="lazy"><span>Henrique Carvalho Neves</span></a>
  <a href="https://github.com/jlucasiqueira" class="integrante"><img src="https://avatars.githubusercontent.com/u/143570377?v=4" alt="" width="80" height="80" loading="lazy"><span>Joao Lucas Araujo Siqueira</span></a>
  <a href="https://github.com/jpaulohe4rt" class="integrante"><img src="https://avatars.githubusercontent.com/u/50640221?v=4" alt="" width="80" height="80" loading="lazy"><span>Joao Paulo Lima da Silva</span></a>
  <a href="https://github.com/Leonardo0o0" class="integrante"><img src="https://avatars.githubusercontent.com/u/82467659?v=4" alt="" width="80" height="80" loading="lazy"><span>Leonardo Sobrinho De Aguiar</span></a>
  <a href="https://github.com/leticiatmartins" class="integrante"><img src="https://avatars.githubusercontent.com/u/86434947?v=4" alt="" width="80" height="80" loading="lazy"><span>Letícia Torres Soares Martins</span></a>
  <a href="https://github.com/rmatuda" class="integrante"><img src="https://avatars.githubusercontent.com/u/134009750?v=4" alt="" width="80" height="80" loading="lazy"><span>Rafael Melo Matuda</span></a>
</div>

## Como executar a documentação

Com **Python 3.10 ou superior** e **pip** instalados, clone o repositório:

```bash
git clone https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc.git
cd 2026-2-AnatoQuizUp-Doc
python3 -m venv .venv
```

Ative o ambiente virtual com `source .venv/bin/activate` no macOS/Linux ou `.venv\Scripts\Activate.ps1` no PowerShell do Windows. No Windows, utilize `python` no lugar de `python3`.

```bash
python -m pip install -r requirements.txt
python -m mkdocs serve
```

Acesse **http://127.0.0.1:8000** no navegador. Esses comandos executam o site de documentação.

## Documentação do projeto

- [Visão do Produto](produto/visao.md)
- [Lean Inception](produto/lean_inception.md)
- [Plano de Gerenciamento de Custos](produto/plano-de-custos.md)
- [Como contribuir: política de Pull Requests](contribuicao/pull_requests.md)
- [Repositório no GitHub](https://github.com/fga-eps-mds/2026-2-AnatoQuizUp-Doc)
