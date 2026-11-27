"""Leitor de PRs (A3). Lê GitHub_API-PRs-*.json de analytics-raw-data/<repo>/."""
import json
import re
from pathlib import Path

import pandas as pd

PASTA = Path(__file__).resolve().parents[3] / "analytics-raw-data"
PADRAO = re.compile(r"GitHub_API-PRs-.*-(\d{2}-\d{2}-\d{4}-\d{2}-\d{2}-\d{2})\.json$")

def ultima_captura(repo_dir: Path):
    arquivos = [a for a in repo_dir.glob("GitHub_API-PRs-*.json") if PADRAO.search(a.name)]
    return max(arquivos, key=lambda a: PADRAO.search(a.name).group(1), default=None)

def resumir(repo_dir: Path) -> dict | None:
    arquivo = ultima_captura(repo_dir)
    if arquivo is None:
        return None
    prs = json.loads(arquivo.read_text(encoding="utf-8"))
    return {
        "repositorio": repo_dir.name,
        "coleta": PADRAO.search(arquivo.name).group(1),
        "total": len(prs),
        "abertos": sum(p["state"] == "OPEN" for p in prs),
        "fechados_sem_merge": sum(p["state"] == "CLOSED" and not p.get("mergedAt") for p in prs),
        "mergeados": sum(bool(p.get("mergedAt")) for p in prs),
        "com_revisao": sum(bool(p.get("reviews")) for p in prs),
    }

def tabela() -> pd.DataFrame:
    linhas = [r for r in (resumir(d) for d in sorted(PASTA.iterdir()) if d.is_dir()) if r]
    return pd.DataFrame(linhas)

if __name__ == "__main__":
    print(tabela().to_string(index=False) or "Nenhuma captura de PRs encontrada.")