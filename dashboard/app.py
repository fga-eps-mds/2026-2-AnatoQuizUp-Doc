"""Dashboard de metricas do AnatoQuizUp (R1 e R2).

Fontes de dados, todas em analytics-raw-data/<repo>/ no repositorio de Doc:

1. SonarCloud: arquivos fga-eps-mds-<repo>-<data>-<versao>.json publicados pelo
   workflow "Export de metricas" (metricas.yml) de cada repositorio.
2. Jest (coleta manual complementar ao SonarCloud): arquivos
   jest-coverage-<repo>-<data>.json gerados a partir do
   coverage/coverage-summary.json de cada repositorio. Mostram a cobertura
   separada por tipo (linhas, instrucoes, funcoes e ramificacoes), que o
   SonarCloud apresenta combinada em um unico percentual.
3. GitHub (issues do repositorio de Doc): arquivos GitHub_API-Issues-*.json
   publicados pelo mesmo workflow. Alimentam os indicadores de gestao
   (velocity, burndown e EVM-Agil), junto com dashboard/config/gestao.json.
4. Plano de riscos: dashboard/config/riscos.json, copiado de
   docs/produto/plano-de-riscos.md, alimenta a matriz de riscos.

Executar localmente (na raiz do repositorio de Doc):
    pip install -r dashboard/requirements.txt
    streamlit run dashboard/app.py
"""

import json
import re
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

PASTA_DADOS = Path(__file__).resolve().parent.parent / "analytics-raw-data"
PASTA_CONFIG = Path(__file__).resolve().parent / "config"
META_COBERTURA = 85.0
FORMATO_DATA = "%m-%d-%Y-%H-%M-%S"
PADRAO_DATA = r"\d{2}-\d{2}-\d{4}-\d{2}-\d{2}-\d{2}"
# Fuso fixo: o Brasil nao tem horario de verao desde 2019.
FUSO_BRASILIA = timezone(timedelta(hours=-3), "BRT")
AVISO_FUSO = "Horários exibidos no horário de Brasília (UTC-3)."
# Escala do security_rating no SonarCloud.
NOTAS_SEGURANCA = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E"}

# Nome das metricas do SonarCloud -> rotulo exibido no dashboard.
METRICAS_SONAR = {
    "coverage": "Cobertura (%)",
    "tests": "Testes",
    "test_failures": "Falhas de teste",
    "test_errors": "Erros de teste",
    "ncloc": "Linhas de código",
    "files": "Arquivos",
    "functions": "Funções",
    "complexity": "Complexidade",
    "duplicated_lines_density": "Duplicação (%)",
    "comment_lines_density": "Comentários (%)",
    "security_rating": "Nota de segurança",
}

# Tipos de cobertura do Jest (coverage-summary.json) -> rotulo exibido.
METRICAS_JEST = {
    "lines": "Linhas (%)",
    "statements": "Instruções (%)",
    "functions": "Funções (%)",
    "branches": "Ramificações (%)",
}

# Cores dos graficos de gestao: serie principal e um tom mais claro do mesmo azul.
COR_SERIE = "#2a78d6"
COR_SERIE_CLARA = "#86b6ef"
# Cores das faixas de prioridade do plano de riscos (paleta de status: bom, atencao, serio, critico).
CORES_FAIXAS_RISCO = ["#0ca30c", "#fab219", "#ec835a", "#d03b3b"]
# Cor do texto sobre cada faixa, para manter contraste.
TEXTO_FAIXAS_RISCO = ["#ffffff", "#0b0b0b", "#0b0b0b", "#ffffff"]

# Ex.: fga-eps-mds-2026-2-AnatoQuizUp-BFF-09-28-2026-00-15-00-1.0.0.json
PADRAO_SONAR = re.compile(rf"^fga-eps-mds-(?P<repo>.+)-(?P<data>{PADRAO_DATA})-(?P<tag>[^-]+)\.json$")
# Ex.: jest-coverage-2026-2-AnatoQuizUp-BFF-09-28-2026-00-15-00.json
PADRAO_JEST = re.compile(rf"^jest-coverage-(?P<repo>.+)-(?P<data>{PADRAO_DATA})\.json$")


# Nome canônico de cada repositório, independente do prefixo e da caixa no arquivo.
NOMES_REPOSITORIOS = {
    "WEB": "Web",
    "BFF": "BFF",
    "QUIZ-SERVICE": "Quiz-Service",
    "USUARIO-SERVICE": "Usuario-Service",
}


def nome_curto(repo: str) -> str:
    """Aceita os nomes de projeto Sonar usados em setembro e outubro."""
    nome = re.sub(r"^2026[-_]2(?:_UNB)?-AnatoQuizUp-", "", repo)
    return NOMES_REPOSITORIOS.get(nome.upper(), nome)


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
    """Extrai medidas dos formatos antigo e novo do exportador SonarCloud."""
    brutas = conteudo.get("project_measures")
    if brutas is None:
        base = conteudo.get("baseComponent") or conteudo.get("component") or conteudo.get("data", {}).get("component", {})
        brutas = base.get("measures", [])
    medidas = {}
    for medida in brutas:
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


def momento_github(valor):
    """Datas da API do GitHub vem em UTC (ex.: 2026-09-28T00:35:15Z)."""
    try:
        return para_brasilia(datetime.fromisoformat(str(valor).replace("Z", "+00:00")))
    except ValueError:
        return None


@st.cache_data(ttl=300)
def carregar_issues(pasta: str):
    """Lê a captura datada mais recente das issues do repositório de Doc."""
    escolhido = None
    for arquivo in Path(pasta).rglob("GitHub_API-Issues-*.json"):
        itens = ler_json(arquivo)
        if not isinstance(itens, list):
            continue
        data_nome = re.search(rf"({PADRAO_DATA})\.json$", arquivo.name)
        if not data_nome:
            continue
        coleta = coleta_sonar(data_nome.group(1))
        if escolhido is None or coleta > escolhido[2]:
            escolhido = (itens, arquivo, coleta)
    if escolhido is None:
        return pd.DataFrame(), None, None
    itens, arquivo, coleta = escolhido
    linhas = [
        {
            "numero": item.get("number"),
            "titulo": item.get("title"),
            "estado": item.get("state"),
            "criada": momento_github(item.get("created_at")),
            "fechada": momento_github(item.get("closed_at")),
            "rotulos": [rotulo.get("name", "").lower() for rotulo in item.get("labels", []) if isinstance(rotulo, dict)],
        }
        for item in itens
        if isinstance(item, dict) and "pull_request" not in item
    ]
    issues = pd.DataFrame(linhas, columns=["numero", "titulo", "estado", "criada", "fechada", "rotulos"])
    issues["criada"] = pd.to_datetime(issues["criada"])
    issues["fechada"] = pd.to_datetime(issues["fechada"])
    return issues, f"{arquivo.parent.name}/{arquivo.name}", coleta


@st.cache_data(ttl=300)
def carregar_config(caminho: str):
    conteudo = ler_json(Path(caminho))
    return conteudo if isinstance(conteudo, dict) else None


def ler_gestao(config) -> dict | None:
    """Valida o gestao.json e converte as datas; None se faltar algum campo."""
    try:
        releases = {
            r["nome"]: {
                "inicio": date.fromisoformat(r["inicio"]),
                "fim": date.fromisoformat(r["fim"]),
                "orcamento": float(r["orcamento"]),
            }
            for r in config["releases"]
        }
        return {
            "releases": releases,
            "custo_recorrente_semanal": float(config["custo_recorrente_semanal"]),
            "custo_hardware": float(config["custo_hardware"]),
            "escopo_r1": [int(n) for n in config["escopo_r1"]],
            "duracao_sprint_dias": int(config["duracao_sprint_dias"]),
        }
    except (KeyError, TypeError, ValueError):
        return None


def calcular_velocity(issues: pd.DataFrame, coleta: datetime, duracao_dias: int) -> pd.DataFrame:
    """Issues fechadas por sprint. As sprints comecam na segunda-feira da semana da primeira issue."""
    inicio = issues["criada"].min().normalize()
    inicio -= timedelta(days=inicio.weekday())
    passo = timedelta(days=duracao_dias)
    fechadas = issues["fechada"].dropna()
    linhas = []
    comeco = inicio
    while comeco <= coleta:
        fim = comeco + passo
        linhas.append(
            {
                "comeco": comeco,
                "sprint": f"{comeco:%d/%m} a {fim - timedelta(days=1):%d/%m}",
                "fechadas": int(((fechadas >= comeco) & (fechadas < fim)).sum()),
                "situacao": "Sprint concluída" if fim <= coleta else "Sprint em andamento",
            }
        )
        comeco = fim
    return pd.DataFrame(linhas)


def calcular_burndown(issues: pd.DataFrame, escopo: list, inicio: date, fim: date, coleta: datetime) -> pd.DataFrame:
    """Itens do escopo abertos ao fim de cada dia (ou no momento da coleta, no dia da coleta)."""
    itens = issues[issues["numero"].isin(escopo)]
    linhas = []
    dia = inicio
    while dia <= min(fim, coleta.date()):
        instante = min(datetime.combine(dia + timedelta(days=1), datetime.min.time()), coleta)
        criados = itens[itens["criada"] <= instante]
        abertos = criados[criados["fechada"].isna() | (criados["fechada"] > instante)]
        linhas.append({"dia": dia, "abertos": len(abertos), "escopo": len(criados)})
        dia += timedelta(days=1)
    return pd.DataFrame(linhas)


def calcular_evm(release: dict, gestao: dict, concluidos: int, total: int, coleta: datetime) -> dict:
    referencia = min(coleta.date(), release["fim"])
    # Os intervalos do plano de custos incluem o último dia de cada release.
    semanas_totais = ((release["fim"] - release["inicio"]).days + 1) / 7
    semanas = max((referencia - release["inicio"]).days + 1, 0) / 7
    ppc = min(semanas / semanas_totais, 1.0)
    apc = concluidos / total
    pv = ppc * release["orcamento"]
    ev = apc * release["orcamento"]
    return {
        "referencia": referencia,
        "semanas": semanas,
        "semanas_totais": semanas_totais,
        "ppc": ppc,
        "apc": apc,
        "pv": pv,
        "ev": ev,
        # AC exige horas reais por integrante; orçamento não é custo realizado.
        "ac": None,
        "spi": ev / pv if pv > 0 else None,
        "cpi": None,
    }


def reais(valor: float) -> str:
    return "R$ " + f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def interpretar_indice(valor, acima: str, igual: str, abaixo: str) -> str:
    if valor is None:
        return "sem dados (denominador zero)"
    if round(valor, 2) > 1:
        return acima
    return igual if round(valor, 2) == 1 else abaixo


def sem_dados(indicador: str, motivo: str) -> None:
    st.info(f"**{indicador}: sem dados.** {motivo}")


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


def retrato_sonar(dados: pd.DataFrame, inicio: datetime, fim: datetime) -> pd.DataFrame:
    periodo = dados[(dados["coleta"] >= inicio) & (dados["coleta"] <= fim)]
    return mais_recente_por_repo(periodo) if not periodo.empty else pd.DataFrame()


def indice_qualidade(retrato: pd.DataFrame) -> pd.DataFrame:
    """Convenção analítica R2: cobertura 50%, segurança 25%, duplicação 25%."""
    resultado = retrato[["coverage", "security_rating", "duplicated_lines_density", "coleta"]].copy()
    resultado["cobertura_normalizada"] = resultado["coverage"].clip(0, 100)
    resultado["seguranca_normalizada"] = (125 - 25 * resultado["security_rating"]).clip(0, 100)
    resultado["duplicacao_normalizada"] = (100 - 10 * resultado["duplicated_lines_density"]).clip(0, 100)
    resultado["indice"] = (
        0.50 * resultado["cobertura_normalizada"]
        + 0.25 * resultado["seguranca_normalizada"]
        + 0.25 * resultado["duplicacao_normalizada"]
    )
    return resultado


def velocidade_periodo(issues: pd.DataFrame, inicio: datetime, fim: datetime) -> tuple[float | None, int]:
    """Média de issues fechadas por janela completa de sete dias."""
    semanas = (fim.date() - inicio.date()).days // 7
    if semanas < 1:
        return None, 0
    fim_completo = inicio + timedelta(days=7 * semanas)
    fechadas = issues["fechada"].between(inicio, fim_completo, inclusive="left").sum()
    return float(fechadas / semanas), int(fechadas)


def indice_processo(issues: pd.DataFrame, inicio: datetime, fim: datetime) -> dict | None:
    """Agrega atividade e distribuição dos fechamentos em semanas completas."""
    semanas = (fim.date() - inicio.date()).days // 7
    if semanas < 2:
        return None
    fechadas = issues["fechada"].dropna()
    contagens = [
        int(((fechadas >= inicio + timedelta(days=7 * i)) &
             (fechadas < inicio + timedelta(days=7 * (i + 1)))).sum())
        for i in range(semanas)
    ]
    total = sum(contagens)
    if total == 0:
        return None
    atividade = 100 * sum(n > 0 for n in contagens) / semanas
    distribuicao = 100 * (1 - max(contagens) / total) / (1 - 1 / semanas)
    return {
        "semanas": semanas,
        "contagens": contagens,
        "atividade": atividade,
        "distribuicao": distribuicao,
        "indice": 0.5 * atividade + 0.5 * distribuicao,
    }


st.set_page_config(page_title="AnatoQuizUp · Métricas R2", layout="wide")
st.title("AnatoQuizUp · Dashboard de métricas")
st.caption(AVISO_FUSO)

sonar = carregar_sonar(str(PASTA_DADOS))
jest = carregar_jest(str(PASTA_DADOS))

if sonar.empty and jest.empty:
    st.warning(
        f"Nenhum arquivo de métricas encontrado em `{PASTA_DADOS.name}/`. "
        "Verifique se o workflow metricas.yml rodou ou se os arquivos jest-coverage-*.json foram adicionados."
    )
    st.stop()

# ----- Comparação R1 × R2 -----
st.header("Comparação R1 × R2")
st.caption("R1: última coleta de 10/08 a 28/09. R2: última coleta de 29/09 a 26/10, por repositório. A data de cada medida aparece na tabela.")
inicio_r1 = datetime(2026, 8, 10)
fim_r1 = datetime(2026, 9, 28, 23, 59, 59)
inicio_r2 = datetime(2026, 9, 29)
fim_r2 = datetime(2026, 10, 26, 23, 59, 59)
if not sonar.empty:
    r1_sonar = retrato_sonar(sonar, inicio_r1, fim_r1)
    r2_sonar = retrato_sonar(sonar, inicio_r2, fim_r2)
    if not r1_sonar.empty and not r2_sonar.empty:
        pares = r1_sonar[["coverage", "coleta"]].add_suffix("_R1").join(
            r2_sonar[["coverage", "coleta"]].add_suffix("_R2"), how="outer"
        )
        pares["Variação (p.p.)"] = pares["coverage_R2"] - pares["coverage_R1"]
        st.subheader("Cobertura SonarCloud")
        st.dataframe(
            pares.rename(columns={"coverage_R1": "R1 (%)", "coverage_R2": "R2 (%)", "coleta_R1": "Coleta R1", "coleta_R2": "Coleta R2"})
            .rename_axis("Repositório"), width="stretch"
        )
        if set(r1_sonar.index) == set(r2_sonar.index) == {"BFF", "Quiz-Service", "Usuario-Service", "Web"}:
            q1 = indice_qualidade(r1_sonar)
            q2 = indice_qualidade(r2_sonar)
            indice = q1[["indice"]].add_suffix("_R1").join(q2[["indice"]].add_suffix("_R2"))
            indice["Variação"] = indice["indice_R2"] - indice["indice_R1"]
            st.subheader("Índice composto de qualidade de produto")
            st.caption(
                "Convenção de análise proposta: cobertura 50%, nota de segurança 25%, duplicação 25%. "
                "Cobertura já varia de 0 a 100; segurança A–E vira 100, 75, 50, 25, 0; "
                "duplicação vira máximo(0, 100 − 10 × percentual). Agregação: média simples dos quatro "
                "repositórios. Pesos e limiares precisam de validação do time e professor antes de orientar decisões."
            )
            st.dataframe(indice.rename(columns={"indice_R1": "R1", "indice_R2": "R2"}).round(1), width="stretch")
            st.metric("Índice agregado R2", f"{indice['indice_R2'].mean():.1f}/100", f"{indice['Variação'].mean():+.1f} frente à R1")
        else:
            st.warning("Não há quatro repositórios com dados nos dois períodos para agregar o índice.")
    else:
        st.info("Faltam coletas SonarCloud em uma das releases para comparação.")

issues_r2, arquivo_issues_r2, coleta_issues_r2 = carregar_issues(str(PASTA_DADOS))
if not issues_r2.empty:
    fim_observado = min(coleta_issues_r2, fim_r2)
    v1, total_v1 = velocidade_periodo(issues_r2, inicio_r1, fim_r1)
    # Sprints de segunda a domingo: 28/09–25/10. O recorte Sonar da R2
    # continua sendo 29/09–26/10 e é identificado separadamente acima.
    inicio_sprints_r2 = datetime(2026, 9, 28)
    v2, total_v2 = velocidade_periodo(issues_r2, inicio_sprints_r2, fim_observado)
    st.subheader("Velocidade observada no backlog")
    st.caption(
        "Proxy: issues fechadas por janela completa de sete dias; não representa story points nem aceitações "
        f"do cliente. Fonte: repositório Doc, captura de {coleta_issues_r2:%d/%m/%Y %H:%M}. "
        "R1: 10/08–27/09. Sprints da R2: 28/09–25/10, de segunda a domingo, conforme o plano de custos; "
        "o dia 26/10 ainda é parcial e fica fora desta média. O recorte de produto da R2 é 29/09–26/10."
    )
    st.dataframe(pd.DataFrame([
        {"Release": "R1", "Issues fechadas": total_v1, "Média por 7 dias": v1},
        {"Release": "Sprints R2 (28/09–25/10)", "Issues fechadas": total_v2, "Média por 7 dias": v2},
    ]), hide_index=True, width="stretch")
    p1 = indice_processo(issues_r2, inicio_r1, fim_r1)
    p2 = indice_processo(issues_r2, inicio_sprints_r2, fim_observado)
    st.subheader("Índice exploratório de processo")
    st.caption(
        "Atividade = 100 × semanas com ao menos um fechamento ÷ semanas completas. "
        "Distribuição = 100 × (1 − maior parcela semanal dos fechamentos) ÷ (1 − 1/número de semanas). "
        "Índice = 50% atividade + 50% distribuição; cada componente varia de 0 a 100. "
        "A agregação mede cadência de fechamento do backlog central, não produtividade individual, tamanho "
        "das entregas nem valor aceito pelo cliente. Sem fechamentos, o índice fica indisponível."
    )
    if p1 and p2:
        st.dataframe(pd.DataFrame([
            {"Período": "R1", "Semanas": p1["semanas"], "Atividade": p1["atividade"],
             "Distribuição": p1["distribuicao"], "Índice": p1["indice"]},
            {"Período": "Sprints R2", "Semanas": p2["semanas"], "Atividade": p2["atividade"],
             "Distribuição": p2["distribuicao"], "Índice": p2["indice"]},
        ]).round(1), hide_index=True, width="stretch")
    else:
        st.info("Sem dados suficientes para agregar o índice de processo nos dois períodos.")
    defeitos = issues_r2[issues_r2["rotulos"].map(lambda tags: "bug" in tags)]
    st.subheader("Defeitos registrados no backlog de Doc")
    st.dataframe(pd.DataFrame([
        {"Release (criação)": "R1", "Issues com rótulo bug": int(defeitos["criada"].between(inicio_r1, fim_r1).sum())},
        {"Release (criação)": "R2 até a coleta", "Issues com rótulo bug": int(defeitos["criada"].between(inicio_r2, fim_observado).sum())},
    ]), hide_index=True, width="stretch")
    st.warning(
        "Esta contagem inclui defeitos de documentação e DevOps. Não equivale a defeitos do produto: "
        "a coleta de issues dos quatro repositórios de código ainda não existe no dashboard. "
        "Não interprete ausência de registros como ausência de defeitos."
    )

st.subheader("Interpretação e decisões propostas")
st.markdown(
    """
1. **Confiabilidade dos dados:** conferir as coletas dos quatro repositórios após a mudança
   de formato do exportador, antes de usar o painel na apresentação.
2. **Capacidade da sprint:** investigar no ZenHub a variação de issues concluídas por semana
   e registrar estimativas para separar volume de trabalho de tamanho das tarefas.
3. **Qualidade:** examinar a nota C de segurança em Web e a queda de cobertura
   do Usuario-Service antes de repriorizar correções.

Estas são propostas para deliberação do time, com causa, evidência e ação detalhadas na
[análise R2](https://fga-eps-mds.github.io/2026-2-AnatoQuizUp-Doc/dashboard-r2/).
"""
)
with st.expander("Crítica aos resultados sugeridos por IA"):
    st.markdown(
        "**Aproveitado como hipótese verificável:** comparar releases por repositório e combinar "
        "métricas normalizadas; números conferidos nos JSONs. "
        "**Descartado:** interpretar as issues `bug` do repositório Doc como a contagem "
        "de defeitos do produto; elas incluem template, DevOps e o próprio dashboard. "
        "**Depende do julgamento do time:** pesos, limiares, causas da variação de velocidade "
        "e adoção das ações propostas."
    )

# ----- SonarCloud -----
if not sonar.empty:
    ultimas_sonar = mais_recente_por_repo(sonar)
    st.subheader(f"SonarCloud · cobertura x meta de {META_COBERTURA:.0f}%")
    st.caption("Gerado automaticamente pelo workflow metricas.yml de cada repositório.")
    cartoes_cobertura(
        ultimas_sonar,
        "coverage",
        lambda linha: f"Versão {linha['versao']} · coleta {linha['coleta']:%d/%m %H:%M} (horário de Brasília)",
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

    st.subheader("Métricas do SonarCloud (última coleta)")
    # Esconde metricas sem nenhum valor (ex.: testes, que o SonarCloud nao recebe).
    colunas_sonar = [m for m in METRICAS_SONAR if m in ultimas_sonar.columns and ultimas_sonar[m].notna().any()]
    tabela_sonar = ultimas_sonar[colunas_sonar].copy()
    if "security_rating" in tabela_sonar.columns:
        tabela_sonar["security_rating"] = tabela_sonar["security_rating"].map(nota_seguranca)
    st.dataframe(tabela_sonar.rename(columns=METRICAS_SONAR).rename_axis("Repositório"), width="stretch")

    if sonar.groupby("repositorio").size().max() > 1:
        st.subheader("Evolução ao longo das coletas")
        metrica = st.selectbox("Métrica", colunas_sonar, format_func=lambda m: METRICAS_SONAR[m])
        evolucao = px.line(
            sonar.sort_values("coleta"),
            x="coleta",
            y=metrica,
            color="repositorio",
            markers=True,
            labels={
                "coleta": "Coleta (horário de Brasília)",
                metrica: METRICAS_SONAR[metrica],
                "repositorio": "Repositório",
            },
        )
        if metrica == "security_rating":
            evolucao.update_yaxes(
                title_text="Nota de segurança (1=A ... 5=E)",
                tickvals=list(NOTAS_SEGURANCA),
                ticktext=[f"{n} ({letra})" for n, letra in NOTAS_SEGURANCA.items()],
                range=[0.5, 5.5],
            )
        st.plotly_chart(evolucao, width="stretch")
else:
    st.info(f"Nenhum dado do SonarCloud encontrado em {PASTA_DADOS.name}/.")

# ----- Cobertura via Jest (coleta complementar) -----
if not jest.empty:
    ultimas_jest = mais_recente_por_repo(jest)
    st.subheader(f"Cobertura de testes (Jest) x meta de {META_COBERTURA:.0f}%")
    st.caption(
        f"Coleta manual complementar, feita em {jest['coleta'].max():%d/%m} com `npm run test:ci` na `main` "
        "de cada repositório (arquivo coverage/coverage-summary.json). Mostra a cobertura separada por tipo "
        "(linhas, instruções, funções e ramificações), que o SonarCloud apresenta combinada em um único "
        "percentual. Percentual principal dos cartões: linhas."
    )
    cartoes_cobertura(
        ultimas_jest,
        "lines",
        lambda linha: f"{linha['branch'] or 'main'} @ {linha['commit'] or '?'} · {linha['coleta']:%d/%m %H:%M} (horário de Brasília)",
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

    st.dataframe(
        ultimas_jest[list(METRICAS_JEST)].rename(columns=METRICAS_JEST).rename_axis("Repositório"), width="stretch"
    )

# ----- Issues -----
issues, arquivo_issues, coleta_issues = carregar_issues(str(PASTA_DADOS))
if not issues.empty:
    st.subheader("Issues do repositório de Doc")
    c1, c2, c3 = st.columns(3)
    c1.metric("Total", len(issues))
    c2.metric("Fechadas", int((issues["estado"] == "closed").sum()))
    c3.metric("Abertas", int((issues["estado"] == "open").sum()))

# ----- Indicadores de gestão -----
st.header("Indicadores de gestão")
gestao_bruta = carregar_config(str(PASTA_CONFIG / "gestao.json"))
gestao = ler_gestao(gestao_bruta) if gestao_bruta else None
riscos_config = carregar_config(str(PASTA_CONFIG / "riscos.json"))

motivo_sem_gestao = None
if issues.empty:
    motivo_sem_gestao = (
        f"Nenhum arquivo GitHub_API-Issues-*.json com issues foi encontrado em `{PASTA_DADOS.name}/`. "
        "Esses arquivos são gerados pelo workflow de exportação de métricas."
    )
elif gestao is None:
    motivo_sem_gestao = (
        "O arquivo `dashboard/config/gestao.json` não foi encontrado ou está incompleto "
        "(releases, custos, escopo da R1 e duração da sprint)."
    )

if motivo_sem_gestao is None:
    st.caption(
        f"Issues do repositório de Doc lidas de `{arquivo_issues}` (pull requests ignorados). "
        f"Data de referência: {coleta_issues:%d/%m/%Y %H:%M} (horário de Brasília), extraída do "
        "nome do arquivo de captura. Releases, orçamento e escopo da R1 vêm de `dashboard/config/gestao.json`, com as "
        "fontes indicadas no próprio arquivo."
    )

# Velocity
st.subheader("Velocity por sprint")
if motivo_sem_gestao:
    sem_dados("Velocity", motivo_sem_gestao)
else:
    velocity = calcular_velocity(issues, coleta_issues, gestao["duracao_sprint_dias"])
    concluidas = velocity[velocity["situacao"] == "Sprint concluída"]
    st.caption(
        "Velocity por **quantidade de issues fechadas** em cada sprint, porque as issues não têm story "
        f"points. Sprint de {gestao['duracao_sprint_dias']} dias, de segunda a domingo (horário de "
        "Brasília), a partir da semana da primeira issue criada. A média considera só as sprints "
        "concluídas até a data de referência."
    )
    grafico_velocity = px.bar(
        velocity,
        x="sprint",
        y="fechadas",
        color="situacao",
        text_auto=True,
        color_discrete_map={"Sprint concluída": COR_SERIE, "Sprint em andamento": COR_SERIE_CLARA},
        labels={"sprint": "Sprint", "fechadas": "Issues fechadas", "situacao": ""},
    )
    if not concluidas.empty:
        media_velocity = concluidas["fechadas"].mean()
        grafico_velocity.add_hline(
            y=media_velocity, line_dash="dash", annotation_text=f"média {media_velocity:.1f} issues/sprint"
        )
        st.metric("Velocity média (sprints concluídas)", f"{media_velocity:.1f} issues/sprint")
    else:
        st.caption("Ainda não há sprint concluída para calcular a média.")
    st.plotly_chart(grafico_velocity, width="stretch")

# Burndown e EVM usam o escopo da R1
release_r1 = gestao["releases"].get("R1") if gestao else None
if gestao and release_r1 is None:
    motivo_sem_gestao = "A release R1 não está definida em `dashboard/config/gestao.json`."

st.subheader("Burndown da R1")
if motivo_sem_gestao:
    sem_dados("Burndown", motivo_sem_gestao)
elif coleta_issues.date() < release_r1["inicio"]:
    sem_dados("Burndown", "A coleta das issues é anterior ao início da R1.")
elif not issues["numero"].isin(gestao["escopo_r1"]).any():
    sem_dados("Burndown", "Nenhuma issue do escopo da R1 está no JSON de issues.")
else:
    escopo_r1 = gestao["escopo_r1"]
    ausentes = sorted(set(escopo_r1) - set(issues["numero"]))
    # O grafico comeca quando o primeiro item do escopo foi criado: antes disso nao ha o que acompanhar.
    primeiro_item = issues.loc[issues["numero"].isin(escopo_r1), "criada"].min().date()
    inicio_burndown = max(primeiro_item, release_r1["inicio"])
    burndown = calcular_burndown(issues, escopo_r1, inicio_burndown, release_r1["fim"], coleta_issues)
    st.caption(
        f"Itens do escopo da R1 ainda abertos ao fim de cada dia, de {inicio_burndown:%d/%m} a "
        f"{release_r1['fim']:%d/%m/%Y}. Um item conta como aberto do created_at até o closed_at; itens "
        "criados depois do início entram a partir do created_at (linha de escopo). A linha ideal vai "
        f"do escopo completo ({len(escopo_r1)} itens) a zero no fim da release. Pontos posteriores à "
        "data de referência não são desenhados, porque ainda não há dados."
    )
    if inicio_burndown > release_r1["inicio"]:
        st.caption(
            f"O backlog da R1 passou a ser registrado no GitHub em {inicio_burndown:%d/%m}; "
            "antes disso não há itens para acompanhar."
        )
    if ausentes:
        st.warning(
            "Issues do escopo da R1 que não estão no JSON (ficam fora do gráfico): "
            + ", ".join(f"#{n}" for n in ausentes)
        )
    grafico_burndown = go.Figure()
    grafico_burndown.add_scatter(
        x=[inicio_burndown, release_r1["fim"]],
        y=[len(escopo_r1), 0],
        name="Ideal",
        mode="lines",
        line={"dash": "dash", "color": "#898781", "width": 2},
    )
    grafico_burndown.add_scatter(
        x=burndown["dia"], y=burndown["escopo"], name="Escopo total", mode="lines", line_shape="hv",
        line={"width": 2, "dash": "dot", "color": COR_SERIE_CLARA},
    )
    grafico_burndown.add_scatter(
        x=burndown["dia"], y=burndown["abertos"], name="Itens abertos", mode="lines+markers", line_shape="hv",
        line={"width": 2, "color": COR_SERIE},
    )
    grafico_burndown.update_layout(
        xaxis_title="Dia (horário de Brasília)",
        xaxis_tickformat="%d/%m",
        xaxis_hoverformat="%d/%m/%Y",
        yaxis_title="Itens",
        yaxis_rangemode="tozero",
        hovermode="x unified",
    )
    st.plotly_chart(grafico_burndown, width="stretch")
    ultimo = burndown.iloc[-1]
    st.caption(
        f"Em {ultimo['dia']:%d/%m}: {ultimo['abertos']} de {ultimo['escopo']} itens do escopo ainda abertos."
    )

st.subheader("EVM-Ágil da R1")
if motivo_sem_gestao:
    sem_dados("EVM-Ágil", motivo_sem_gestao)
elif not gestao["escopo_r1"]:
    sem_dados("EVM-Ágil", "O escopo da R1 está vazio em `dashboard/config/gestao.json`.")
else:
    escopo_r1 = gestao["escopo_r1"]
    fim_r1_exclusivo = datetime.combine(release_r1["fim"] + timedelta(days=1), datetime.min.time())
    fechados_r1 = issues[
        issues["numero"].isin(escopo_r1)
        & issues["fechada"].notna()
        & (issues["fechada"] < fim_r1_exclusivo)
    ]
    evm = calcular_evm(release_r1, gestao, len(fechados_r1), len(escopo_r1), coleta_issues)
    st.caption(
        f"Data de referência: {evm['referencia']:%d/%m/%Y} (data da coleta das issues, limitada ao fim da R1). "
        "Item concluído = issue do escopo fechada até o fim da R1. PPC e APC usam respectivamente tempo "
        "decorrido e quantidade de issues; o APC é um proxy porque não há story points da R1. "
        "O orçamento segue o plano de custos v2.1. Sem horas reais registradas, AC e CPI são indisponíveis."
    )
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("SPI", f"{evm['spi']:.2f}" if evm["spi"] is not None else "sem dados")
    c2.metric("CPI", "indisponível")
    c3.metric("PPC", f"{evm['ppc']:.1%}")
    c4.metric("APC", f"{evm['apc']:.1%}")
    st.markdown(
        f"""
| Indicador | Fórmula | Cálculo | Valor |
| --- | --- | --- | --- |
| PPC (percentual planejado) | semanas decorridas ÷ semanas totais (máx. 100%) | {evm['semanas']:.2f} ÷ {evm['semanas_totais']:.2f} | {evm['ppc']:.1%} |
| APC (percentual concluído) | itens concluídos ÷ itens do escopo | {len(fechados_r1)} ÷ {len(escopo_r1)} | {evm['apc']:.1%} |
| PV (valor planejado) | PPC × orçamento da R1 | {evm['ppc']:.1%} × {reais(release_r1['orcamento'])} | {reais(evm['pv'])} |
| EV (valor agregado) | APC × orçamento da R1 | {evm['apc']:.1%} × {reais(release_r1['orcamento'])} | {reais(evm['ev'])} |
| AC (custo real) | horas reais × custo-hora | Horas da R1 não registradas | indisponível |
| SPI | EV ÷ PV | {reais(evm['ev'])} ÷ {reais(evm['pv'])} | {f"{evm['spi']:.2f}" if evm['spi'] is not None else "sem dados"} |
| CPI | EV ÷ AC | AC não medido | indisponível |
"""
    )
    st.markdown(
        "- **SPI:** "
        + interpretar_indice(
            evm["spi"],
            "maior que 1: avanço superior ao planejado.",
            "igual a 1: avanço conforme o planejado.",
            "menor que 1: avanço inferior ao planejado.",
        )
        + "\n- **CPI:** indisponível até que as horas reais por integrante sejam registradas."
    )
    if len(fechados_r1) < len(escopo_r1):
        abertos_r1 = sorted(set(escopo_r1) - set(fechados_r1["numero"]))
        st.caption("Itens do escopo não concluídos na coleta: " + ", ".join(f"#{n}" for n in abertos_r1))

# Matriz de riscos
st.subheader("Matriz de riscos")
riscos = None
if riscos_config:
    try:
        pesos_p = {k: int(v) for k, v in riscos_config["pesos_probabilidade"].items()}
        pesos_i = {k: int(v) for k, v in riscos_config["pesos_impacto"].items()}
        faixas = riscos_config["faixas"]
        riscos = pd.DataFrame(riscos_config["riscos"])
        riscos["p"] = riscos["probabilidade"].map(pesos_p)
        riscos["i"] = riscos["impacto"].map(pesos_i)
        config_valida = (
            sorted(pesos_p.values()) == sorted(pesos_i.values()) == [1, 2, 3, 4, 5]
            and len(faixas) == len(CORES_FAIXAS_RISCO)
            and all(any(f["min"] <= s <= f["max"] for f in faixas) for s in range(1, 26))
            and not riscos[["p", "i"]].isna().any().any()
        )
        if not config_valida:
            riscos = None
    except (KeyError, TypeError, ValueError, AttributeError):
        riscos = None

if riscos is None or riscos.empty:
    sem_dados(
        "Matriz de riscos",
        "O arquivo `dashboard/config/riscos.json` não foi encontrado ou está incompleto (riscos, pesos de "
        "probabilidade e impacto e faixas de prioridade de `docs/produto/plano-de-riscos.md`).",
    )
else:
    riscos["pontuacao"] = (riscos["p"] * riscos["i"]).astype(int)

    def faixa_da(pontuacao: int) -> int:
        return next(n for n, f in enumerate(faixas) if f["min"] <= pontuacao <= f["max"])

    riscos["faixa"] = riscos["pontuacao"].map(lambda p: faixas[faixa_da(p)]["nome"])
    st.caption(
        "Riscos, pesos (1 a 5) e faixas de prioridade copiados de `docs/produto/plano-de-riscos.md`. "
        "Pontuação = probabilidade × impacto. Faixas: "
        + "; ".join(f"{f['nome']} ({f['min']}–{f['max']})" for f in faixas)
        + "."
    )
    nomes_p = {v: k for k, v in pesos_p.items()}
    nomes_i = {v: k for k, v in pesos_i.items()}
    niveis = range(1, 6)
    grafico_riscos = go.Figure(
        go.Heatmap(
            x=[f"{nomes_i[i]} ({i})" for i in niveis],
            y=[f"{nomes_p[p]} ({p})" for p in niveis],
            z=[[faixa_da(p * i) for i in niveis] for p in niveis],
            customdata=[[[p * i, faixas[faixa_da(p * i)]["nome"]] for i in niveis] for p in niveis],
            hovertemplate="Probabilidade: %{y}<br>Impacto: %{x}<br>Pontuação: %{customdata[0]}"
            "<br>Faixa: %{customdata[1]}<extra></extra>",
            colorscale=[
                [limite, cor]
                for n, cor in enumerate(CORES_FAIXAS_RISCO)
                for limite in (n / len(CORES_FAIXAS_RISCO), (n + 1) / len(CORES_FAIXAS_RISCO))
            ],
            zmin=-0.5,
            zmax=len(CORES_FAIXAS_RISCO) - 0.5,
            showscale=False,
            xgap=2,
            ygap=2,
        )
    )
    for (p, i), grupo in riscos.groupby(["p", "i"]):
        grafico_riscos.add_annotation(
            x=f"{nomes_i[i]} ({i})",
            y=f"{nomes_p[p]} ({p})",
            text="<br>".join(sorted(grupo["id"])),
            showarrow=False,
            font={"color": TEXTO_FAIXAS_RISCO[faixa_da(p * i)], "size": 14},
        )
    grafico_riscos.update_layout(
        xaxis_title="Impacto", yaxis_title="Probabilidade", yaxis_automargin=True, yaxis_title_standoff=16, height=480
    )
    st.plotly_chart(grafico_riscos, width="stretch")
    st.dataframe(
        riscos.sort_values(["pontuacao", "id"], ascending=[False, True])[
            ["id", "risco", "categoria", "probabilidade", "impacto", "pontuacao", "faixa"]
        ].rename(
            columns={
                "id": "ID",
                "risco": "Risco",
                "categoria": "Categoria EAR",
                "probabilidade": "Probabilidade",
                "impacto": "Impacto",
                "pontuacao": "Pontuação (P×I)",
                "faixa": "Faixa de prioridade",
            }
        ),
        width="stretch",
        hide_index=True,
    )

with st.expander("Arquivos lidos"):
    lidos = pd.concat(
        [
            sonar.assign(fonte="SonarCloud")[["fonte", "repositorio", "coleta", "arquivo"]] if not sonar.empty else None,
            jest.assign(fonte="Jest")[["fonte", "repositorio", "coleta", "arquivo"]] if not jest.empty else None,
            pd.DataFrame(
                [{"fonte": "GitHub (issues)", "repositorio": "Doc", "coleta": coleta_issues, "arquivo": arquivo_issues}]
            )
            if arquivo_issues
            else None,
        ]
    )
    lidos = lidos.sort_values("coleta", ascending=False)
    lidos["coleta"] = lidos["coleta"].dt.strftime("%d/%m/%Y %H:%M:%S")
    st.dataframe(
        lidos.rename(
            columns={
                "fonte": "Fonte",
                "repositorio": "Repositório",
                "coleta": "Coleta (horário de Brasília)",
                "arquivo": "Arquivo",
            }
        ),
        width="stretch",
        hide_index=True,
    )
