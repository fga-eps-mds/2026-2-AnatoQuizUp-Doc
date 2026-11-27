"""Leitor de CI/CD (A2). Lê GitHub_API-Runs-*.json de analytics-raw-data/<repo>/."""
import json
import re
from pathlib import Path
import pandas as pd

PASTA = Path(__file__).resolve().parents[3] / "analytics-raw-data"
PADRAO = re.compile(r"GitHub_API-Runs-.*-(\d{4}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2})\.json$")

def ultima_captura(repo_dir: Path):
    # Alguns nomes antigos não têm data no final, então verificamos os dois padrões
    arquivos = list(repo_dir.glob("GitHub_API-Runs-*.json"))
    if not arquivos:
        return None
    # Pega o mais recente baseado na data de modificação do arquivo
    return max(arquivos, key=lambda a: a.stat().st_mtime)

def resumir(repo_dir: Path) -> dict | None:
    arquivo = ultima_captura(repo_dir)
    if arquivo is None:
        return None
    
    try:
        dados = json.loads(arquivo.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {"repositorio": repo_dir.name, "erro": "JSON inválido"}

    # O GitHub retorna um objeto com a chave "workflow_runs" ou direto uma lista
    runs = dados if isinstance(dados, list) else dados.get("workflow_runs", [])
    
    total = len(runs)
    sucesso = sum(1 for r in runs if r.get("conclusion") == "success")
    falha = sum(1 for r in runs if r.get("conclusion") == "failure")
    cancelado = sum(1 for r in runs if r.get("conclusion") == "cancelled")

    return {
        "repositorio": repo_dir.name,
        "coleta": arquivo.name.split("-")[-1].replace(".json", ""),
        "total_execucoes": total,
        "sucessos": sucesso,
        "falhas": falha,
        "cancelados": cancelado,
        "taxa_sucesso_%": round((sucesso / total * 100), 1) if total > 0 else 0
    }

def tabela() -> pd.DataFrame:
    linhas = [r for r in (resumir(d) for d in sorted(PASTA.iterdir()) if d.is_dir()) if r]
    return pd.DataFrame(linhas)

if __name__ == "__main__":
    print(tabela().to_string(index=False) or "Nenhuma captura de CI/CD encontrada.")