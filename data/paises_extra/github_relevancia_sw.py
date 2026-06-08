#!/usr/bin/env python3
"""
Reproducible computation of the ILIA subindicator
"Relevancia de Producción de Software" (ID 80) for the 5 extra countries
(ES, EE, SG, DE, PT), from the GitHub Innovation Graph raw data.

Definition (ILIA 2025/2026, hoja "Descripción y seguimiento subin", ID 80):
  "Proporción entre el total de inbounds recibidos y el total de repositorios
   por país en GitHub. Mide cuán relevante para la comunidad de GitHub global
   son los repositorios publicados por los desarrolladores de un país."

Source: GitHub Innovation Graph (CC0-1.0)
  https://github.com/github/innovationgraph  (carpeta /data)

Datasheet (docs/datasheet.md), definition of `economy_collaborators`:
  "the volume of collaboration on software projects based on the sum of git
   pushes sent and pull requests opened by a developer [SOURCE economy] to a
   repository owned by another developer or organization [DESTINATION economy]
   during each quarter."
  => INBOUND recibido por un país X  =  sum(weight) donde destination == X
     (contribuciones que el resto del mundo hace a los repos de X).

`repositories` = number of public software projects of the economy
   (mode location of repo members with triage+ access), per quarter.

Run:  python3 github_relevancia_sw.py
Requires: pandas, and network access to raw.githubusercontent.com
"""
import io
import urllib.request
import pandas as pd

BASE = "https://raw.githubusercontent.com/github/innovationgraph/main/data"
COUNTRIES = ["ES", "EE", "SG", "DE", "PT"]


def fetch_csv(name: str) -> pd.DataFrame:
    url = f"{BASE}/{name}.csv"
    with urllib.request.urlopen(url, timeout=60) as r:
        return pd.read_csv(io.BytesIO(r.read()))


def main() -> None:
    repos = fetch_csv("repositories")
    collab = fetch_csv("economy_collaborators").dropna(subset=["source", "destination"])

    # Denominator (per ILIA methodology): TOTAL ACCUMULATED repositories of the
    # country = sum of the quarterly repo counts across the whole series.
    repos_acc = repos.groupby("iso2_code")["repositories"].sum()
    repos_acc_2025 = repos[repos.year == 2025].groupby("iso2_code")["repositories"].sum()
    n_q = repos.groupby("iso2_code")["repositories"].size()

    # Two inbound windows requested by the operator:
    #   TOTAL  = all available history (2020Q1 .. latest)
    #   2025   = only year 2025 (sum of its quarters)
    ymin = int(collab.year.min())
    p0 = f"{ymin}Q{int(collab[collab.year == ymin].quarter.min())}"
    ymax, qmax = int(repos.year.max()), int(repos[repos.year == repos.year.max()].quarter.max())
    print(f"# Denominator = TOTAL ACCUMULATED repos (sum of all quarters {p0}..{ymax}Q{qmax})")
    print(f"# inbounds TOTAL window = {p0}..{ymax}Q{qmax} ; inbounds 2025 = 2025Q1..Q4\n")

    all_p = collab
    y2025 = collab[collab.year == 2025]

    def inb(df, c, exclude_eu=False):
        m = df.destination == c
        if exclude_eu:
            m &= df.source != "EU"
        return int(df[m]["weight"].sum())

    print(f"{'c':<4}{'repos_acum':>13}{'inb_TOTAL':>12}{'inb_2025':>11}"
          f"{'REL_total':>11}{'REL_2025':>10}")
    rows = []
    for c in COUNTRIES:
        racc = int(repos_acc.get(c, 0))
        racc25 = int(repos_acc_2025.get(c, 0))
        it, i25 = inb(all_p, c), inb(y2025, c)
        it_neu, i25_neu = inb(all_p, c, True), inb(y2025, c, True)
        rel_t = it / racc if racc else float("nan")
        rel_25 = i25 / racc if racc else float("nan")
        rows.append({
            "iso2": c, "n_trimestres": int(n_q.get(c, 0)),
            "repos_acumulado_total": racc, "repos_acumulado_2025": racc25,
            "inbounds_total": it, "inbounds_2025": i25,
            "relevancia_total": round(rel_t, 6), "relevancia_2025": round(rel_25, 6),
            # alt: 2025 inbounds over 2025-accumulated repos (matched window)
            "relevancia_2025_repos2025": round(i25 / racc25, 6) if racc25 else float("nan"),
            "inbounds_total_noEU": it_neu, "inbounds_2025_noEU": i25_neu,
            "relevancia_total_noEU": round(it_neu / racc, 6) if racc else float("nan"),
            "relevancia_2025_noEU": round(i25_neu / racc, 6) if racc else float("nan"),
        })
        print(f"{c:<4}{racc:>13,}{it:>12,}{i25:>11,}{rel_t:>11.5f}{rel_25:>10.5f}")

    # Note: 'EU' is a distinct GitHub economy code (EU-region IPs not resolved to a
    # member state); it coexists with member states and only affects SG here.
    pd.DataFrame(rows).to_csv("relevancia_sw_resultados.csv", index=False)
    print("\n# wrote relevancia_sw_resultados.csv (denominador = repos acumulado total)")


if __name__ == "__main__":
    main()
