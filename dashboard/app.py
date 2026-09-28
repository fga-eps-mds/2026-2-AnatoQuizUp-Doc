"""Dashboard de metricas do AnatoQuizUp (R1).

Fontes de dados, todas em analytics-raw-data/<repo>/ no repositorio de Doc:

1. SonarCloud: arquivos fga-eps-mds-<repo>-<data>-<versao>.json publicados pelo
   workflow "Export de metricas" (metricas.yml) de cada repositorio.
2. Jest (plano B enquanto o SonarCloud nao esta configurado): arquivos
   jest-coverage-<repo>-<data>.json gerados a partir do
   coverage/coverage-summary.json de cada repositorio.

Executar localmente (na raiz do repositorio de Doc):
    pip install -r dashboard/requirements.txt
    streamlit run dashboard/app.py
"""

import json
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

PASTA_DADOS = Path(__file__).resolve().parent.parent / "analytics-raw-data"
META_COBERTURA = 85.0
FORMATO_DATA = "%m-%d-%Y-%H-%M-%S"
PADRAO_DATA = r"\d{2}-\d{2}-\d{4}-\d{2}-\d{2}-\d{2}"
# Fuso fixo: o Brasil nao tem horario de verao desde 2019.
FUSO_BRASILIA = timezone(timedelta(hours=-3), "BRT")
AVISO_FUSO = "Horarios exibidos no horario de Brasilia (UTC-3)."
# Escala do security_rating no SonarCloud.
NOTAS_SEGURANCA = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E"}

# Nome das metricas do SonarCloud -> rotulo exibido no dashboard.
METRICAS_SONAR = {
    "coverage": "Cobertura (%)",
    "tests": "Testes",
    "test_failures": "Falhas de teste",
    "test_errors": "Erros de teste",
    "ncloc": "Linhas de codigo",
    "files": "Arquivos",
    "functions": "Funcoes",
    "complexity": "Complexidade",
    "duplicated_lines_density": "Duplicacao (%)",
    "comment_lines_density": "Comentarios (%)",
    "security_rating": "Nota de seguranca",
}

# Tipos de cobertura do Jest (coverage-summary.json) -> rotulo exibido.
METRICAS_JEST = {
    "lines": "Linhas (%)",
    "statements": "Instrucoes (%)",
    "functions": "Funcoes (%)",
    "branches": "Ramificacoes (%)",
}

# Ex.: fga-eps-mds-2026-2-AnatoQuizUp-BFF-09-28-2026-00-15-00-1.0.0.json
PADRAO_SONAR = re.compile(rf"^fga-eps-mds-(?P<repo>.+)-(?P<data>{PADRAO_DATA})-(?P<tag>[^-]+)\.json$")
# Ex.: jest-coverage-2026-2-AnatoQuizUp-BFF-09-28-2026-00-15-00.json
PADRAO_JEST = re.compile(rf"^jest-coverage-(?P<repo>.+)-(?P<data>{PADRAO_DATA})\.json$")


def nome_curto(repo: str) -> str:
    return repo.replace("2026-2-AnatoQuizUp-", "")


def para_brasilia(momento: datetime) -> datetime:
    """Converte para o horario de Brasilia e remove o fuso (pandas/plotly exibem como esta)."""
    return momento.astimezone(FUSO_BRASILIA).replace(tzinfo=None)


def coleta_sonar(data_nome: str) -> datetime:
    """A data no nome dos arquivos do SonarCloud vem do GitHub Actions, em UTC."""
    return para_brasilia(datetime.strptime(data_nome, FORMATO_DATA).replace(tzinfo=timezone.utc))


def coleta_jest(data_nome: str, gerado_em) -> datetime:
    """Usa o gerado_em (com fuso explicito) se houver; senao, a data do nome ja e horario de Brasilia."""
    try:
        momento = datetime.fromisoformat(str(gerado_em))
        if momento.tzinfo is not None:
            return para_brasilia(momento)
    except ValueError:
        pass
    return datetime.strptime(data_nome, FORMATO_DATA)


def nota_seguranca(valor) -> str:
    return NOTAS_SEGURANCA.get(int(valor), str(valor)) if pd.notna(valor) else ""


def ler_json(arquivo: Path):
    try:
        return json.loads(arquivo.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None


def ler_medidas_sonar(conteudo: dict) -> dict:
    """Extrai as medidas do projeto, aceitando os formatos component e component_tree."""
    base = conteudo.get("baseComponent") or conteudo.get("component") or conteudo.get("data", {}).get("component", {})
    medidas = {}
    for medida in base.get("measures", []):
        try:
            medidas[medida["metric"]] = float(medida["value"])
        except (KeyError, TypeError, ValueError):
            continue
    return medidas


@st.cache_data(ttl=300)
def carregar_sonar(pasta: str) -> pd.DataFrame:
    linhas = []
    for arquivo in Path(pasta).rglob("fga-eps-mds-*.json"):
        casamento = PADRAO_SONAR.match(arquivo.name)
        conteudo = ler_json(arquivo) if casamento else None
        medidas = ler_medidas_sonar(conteudo) if isinstance(conteudo, dict) else {}
        if not medidas:
            continue
        linhas.append(
            {
                "repositorio": nome_curto(casamento["repo"]),
                "coleta": coleta_sonar(casamento["data"]),
                "versao": casamento["tag"],
                "arquivo": arquivo.name,
                **medidas,
            }
        )
    return pd.DataFrame(linhas)


@st.cache_data(ttl=300)
def carregar_jest(pasta: str) -> pd.DataFrame:
    """Le jest-coverage-*.json: um coverage-summary.json puro ou envolto em metadados."""
    linhas = []
    for arquivo in Path(pasta).rglob("jest-coverage-*.json"):
        casamento = PADRAO_JEST.match(arquivo.name)
        conteudo = ler_json(arquivo) if casamento else None
        if not isinstance(conteudo, dict) or not isinstance(conteudo.get("total"), dict):
            continue
        percentuais = {}
        for tipo in METRICAS_JEST:
            try:
                percentuais[tipo] = float(conteudo["total"][tipo]["pct"])
            except (KeyError, TypeError, ValueError):
                continue
        if not percentuais:
            continue
        linhas.append(
            {
                "repositorio": nome_curto(casamento["repo"]),
                "coleta": coleta_jest(casamento["data"], conteudo.get("gerado_em")),
                "commit": str(conteudo.get("commit", ""))[:7],
                "branch": conteudo.get("branch", ""),
                "arquivo": arquivo.name,
                **percentuais,
            }
        )
    return pd.DataFrame(linhas)


@st.cache_data(ttl=300)
def carregar_issues(pasta: str) -> pd.DataFrame:
    arquivos = sorted(Path(pasta).rglob("GitHub_API-Issues-*.json"), key=lambda p: p.stat().st_mtime)
    issues = ler_json(arquivos[-1]) if arquivos else None
    if not isinstance(issues, list):
        return pd.DataFrame()
    linhas = [
        {"numero": item.get("number"), "titulo": item.get("title"), "estado": item.get("state")}
        for item in issues
        if isinstance(item, dict) and "pull_request" not in item
    ]
    return pd.DataFrame(linhas)


def mais_recente_por_repo(df: pd.DataFrame) -> pd.DataFrame:
    return df.sort_values("coleta").groupby("repositorio").tail(1).set_index("repositorio").sort_index()


def cartoes_cobertura(ultimas: pd.DataFrame, coluna_cobertura: str, legenda) -> None:
    colunas = st.columns(len(ultimas))
    for coluna, (repo, linha) in zip(colunas, ultimas.iterrows()):
        cobertura = linha.get(coluna_cobertura)
        with coluna:
            st.metric(
                repo,
                f"{cobertura:.1f}%" if pd.notna(cobertura) else "sem dado",
                f"{cobertura - META_COBERTURA:+.1f} p.p. da meta" if pd.notna(cobertura) else None,
            )
            st.caption(legenda(linha))


def linha_meta(grafico) -> None:
    grafico.add_hline(y=META_COBERTURA, line_dash="dash", annotation_text=f"meta {META_COBERTURA:.0f}%")


st.set_page_config(page_title="AnatoQuizUp · Metricas R1", layout="wide")
st.title("AnatoQuizUp · Dashboard de metricas")
st.caption(AVISO_FUSO)

sonar = carregar_sonar(str(PASTA_DADOS))
jest = carregar_jest(str(PASTA_DADOS))

if sonar.empty and jest.empty:
    st.warning(
        f"Nenhum arquivo de metricas encontrado em `{PASTA_DADOS.name}/`. "
        "Verifique se o workflow metricas.yml rodou ou se os arquivos jest-coverage-*.json foram adicionados."
    )
    st.stop()

# ----- Cobertura via Jest (plano B) -----
if not jest.empty:
    ultimas_jest = mais_recente_por_repo(jest)
    st.subheader(f"Cobertura de testes (Jest) x meta de {META_COBERTURA:.0f}%")
    st.caption(
        "Coleta manual: `npm run test:ci` na main de cada repositorio, a partir do "
        "coverage/coverage-summary.json. Usada enquanto a integracao com o SonarCloud nao esta ativa. "
        "Percentual principal: linhas."
    )
    cartoes_cobertura(
        ultimas_jest,
        "lines",
        lambda linha: f"{linha['branch'] or 'main'} @ {linha['commit'] or '?'} · {linha['coleta']:%d/%m %H:%M} (horario de Brasilia)",
    )

    por_tipo = ultimas_jest[list(METRICAS_JEST)].reset_index().melt(
        id_vars="repositorio", var_name="tipo", value_name="percentual"
    )
    por_tipo["tipo"] = por_tipo["tipo"].map(METRICAS_JEST)
    grafico_jest = px.bar(
        por_tipo,
        x="repositorio",
        y="percentual",
        color="tipo",
        barmode="group",
        range_y=[0, 100],
        labels={"repositorio": "", "percentual": "Cobertura (%)", "tipo": "Tipo"},
    )
    linha_meta(grafico_jest)
    st.plotly_chart(grafico_jest, width="stretch")

    abaixo = ultimas_jest[ultimas_jest[list(METRICAS_JEST)].lt(META_COBERTURA).any(axis=1)]
    if not abaixo.empty:
        st.info("Abaixo da meta em pelo menos um tipo de cobertura: " + ", ".join(abaixo.index))

    st.dataframe(ultimas_jest[list(METRICAS_JEST)].rename(columns=METRICAS_JEST), width="stretch")

# ----- SonarCloud -----
if not sonar.empty:
    ultimas_sonar = mais_recente_por_repo(sonar)
    st.subheader(f"SonarCloud · cobertura x meta de {META_COBERTURA:.0f}%")
    st.caption("Gerado automaticamente pelo workflow metricas.yml de cada repositorio.")
    cartoes_cobertura(
        ultimas_sonar,
        "coverage",
        lambda linha: f"Versao {linha['versao']} · coleta {linha['coleta']:%d/%m %H:%M} (horario de Brasilia)",
    )
    grafico_sonar = px.bar(
        ultimas_sonar.reset_index(),
        x="repositorio",
        y="coverage",
        range_y=[0, 100],
        text_auto=".1f",
        labels={"repositorio": "", "coverage": "Cobertura (%)"},
    )
    linha_meta(grafico_sonar)
    st.plotly_chart(grafico_sonar, width="stretch")

    st.subheader("Metricas do SonarCloud (ultima coleta)")
    # Esconde metricas sem nenhum valor (ex.: testes, que o SonarCloud nao recebe).
    colunas_sonar = [m for m in METRICAS_SONAR if m in ultimas_sonar.columns and ultimas_sonar[m].notna().any()]
    tabela_sonar = ultimas_sonar[colunas_sonar].copy()
    if "security_rating" in tabela_sonar.columns:
        tabela_sonar["security_rating"] = tabela_sonar["security_rating"].map(nota_seguranca)
    st.dataframe(tabela_sonar.rename(columns=METRICAS_SONAR), width="stretch")

    if sonar.groupby("repositorio").size().max() > 1:
        st.subheader("Evolucao ao longo das coletas")
        metrica = st.selectbox("Metrica", colunas_sonar, format_func=lambda m: METRICAS_SONAR[m])
        evolucao = px.line(
            sonar.sort_values("coleta"),
            x="coleta",
            y=metrica,
            color="repositorio",
            markers=True,
            labels={
                "coleta": "Coleta (horario de Brasilia)",
                metrica: METRICAS_SONAR[metrica],
                "repositorio": "Repositorio",
            },
        )
        if metrica == "security_rating":
            evolucao.update_yaxes(
                title_text="Nota de seguranca (1=A ... 5=E)",
                tickvals=list(NOTAS_SEGURANCA),
                ticktext=[f"{n} ({letra})" for n, letra in NOTAS_SEGURANCA.items()],
                range=[0.5, 5.5],
            )
        st.plotly_chart(evolucao, width="stretch")
else:
    st.info("SonarCloud ainda sem dados: os projetos 2026-2 nao estao publicados no SonarCloud.")

# ----- Issues -----
issues = carregar_issues(str(PASTA_DADOS))
if not issues.empty:
    st.subheader("Issues do repositorio de Doc")
    c1, c2, c3 = st.columns(3)
    c1.metric("Total", len(issues))
    c2.metric("Fechadas", int((issues["estado"] == "closed").sum()))
    c3.metric("Abertas", int((issues["estado"] == "open").sum()))

with st.expander("Arquivos lidos"):
    lidos = pd.concat(
        [
            jest.assign(fonte="Jest")[["fonte", "repositorio", "coleta", "arquivo"]] if not jest.empty else None,
            sonar.assign(fonte="SonarCloud")[["fonte", "repositorio", "coleta", "arquivo"]] if not sonar.empty else None,
        ]
    )
    lidos = lidos.sort_values("coleta", ascending=False)
    lidos["coleta"] = lidos["coleta"].dt.strftime("%d/%m/%Y %H:%M:%S")
    st.dataframe(
        lidos.rename(columns={"coleta": "coleta (horario de Brasilia)"}), width="stretch", hide_index=True
    )
