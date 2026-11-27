import streamlit as st
import sys
import os
import pandas as pd

# Adiciona o diretório raiz ao path para importar os módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from r3.ci import ler_prs, ler_ci

st.set_page_config(page_title="AnatoQuizUp · Dashboard R3", layout="wide")
st.title("AnatoQuizUp · Dashboard Analítico R3")

st.markdown("---")

# Seção de Pull Requests
st.header("Pull Requests (GitHub)")
prs = ler_prs.tabela()
if prs.empty:
    st.info("Nenhuma captura de PRs encontrada.")
else:
    st.dataframe(prs, hide_index=True, use_container_width=True)
    total_prs = prs['total'].sum()
    st.metric("Total de PRs no Projeto", total_prs)

st.markdown("---")

# Seção de CI/CD
st.header("Pipelines de CI/CD (GitHub Actions)")
ci = ler_ci.tabela()
if ci.empty:
    st.info("Nenhuma captura de CI/CD encontrada.")
else:
    st.dataframe(ci, hide_index=True, use_container_width=True)
    if 'taxa_sucesso_%' in ci.columns:
        taxa_media = ci['taxa_sucesso_%'].mean()
        st.metric("Taxa Média de Sucesso das Pipelines", f"{taxa_media:.1f}%")

st.markdown("---")

# Seção de Releases
st.header("Releases Geradas")
caminho_csv = os.path.join(os.path.dirname(__file__), 'config', 'releases.csv')
try:
    releases = pd.read_csv(caminho_csv)
    st.dataframe(releases, hide_index=True, use_container_width=True)
    total_major = len(releases[releases['tipo'] == 'major'])
    total_minor = len(releases[releases['tipo'] == 'minor'])
    col1, col2 = st.columns(2)
    col1.metric("Releases Major", total_major)
    col2.metric("Releases Minor", total_minor)
except FileNotFoundError:
    st.warning("Arquivo releases.csv não encontrado. Crie-o na pasta config.")

st.markdown("---")
st.caption("Dados coletados automaticamente via API do GitHub em 27/11/2026.")