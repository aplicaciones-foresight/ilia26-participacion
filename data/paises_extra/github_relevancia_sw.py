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

    # Latest available period -> current repository stock (denominator for BOTH versions)
    ly, lq = repos.sort_values(["year", "quarter"]).iloc[-1][["year", "quarter"]]
    ly, lq = int(ly), int(lq)
    rq = repos[(repos.year == ly) & (repos.quarter == lq)].set_index("iso2_code")["repositories"]

    # Two inbound windows requested by the operator:
    #   TOTAL  = all available history (2020Q1 .. latest)
    #   2025   = only year 2025 (sum of its quarters)
    p0 = f"{int(collab.year.min())}Q{int(collab[collab.year==collab.year.min()].quarter.min())}"
    print(f"# Repos stock (denominator) = {ly}Q{lq}")
    print(f"# inbounds TOTAL window = {p0}..{ly}Q{lq} ; inbounds 2025 window = 2025Q1..Q4\n")

    all_p = collab
    y2025 = collab[collab.year == 2025]

    def inb(df, c, exclude_eu=False):
        m = df.destination == c
        if exclude_eu:
            m &= df.source != "EU"
        return int(df[m]["weight"].sum())

    print(f"{'c':<4}{'repos':>11}{'inb_TOTAL':>12}{'inb_2025':>11}"
          f"{'REL_total':>11}{'REL_2025':>10}")
    rows = []
    for c in COUNTRIES:
        nrep = int(rq.get(c, 0))
        it, i25 = inb(all_p, c), inb(y2025, c)
        it_neu, i25_neu = inb(all_p, c, True), inb(y2025, c, True)
        rel_t = it / nrep if nrep else float("nan")
        rel_25 = i25 / nrep if nrep else float("nan")
        rows.append({
            "iso2": c, "repos_2025Q4": nrep,
            "inbounds_total_2020Q1_2025Q4": it, "inbounds_2025": i25,
            "relevancia_total": round(rel_t, 6), "relevancia_2025": round(rel_25, 6),
            "inbounds_total_noEU": it_neu, "inbounds_2025_noEU": i25_neu,
            "relevancia_total_noEU": round(it_neu / nrep, 6) if nrep else float("nan"),
            "relevancia_2025_noEU": round(i25_neu / nrep, 6) if nrep else float("nan"),
        })
        print(f"{c:<4}{nrep:>11,}{it:>12,}{i25:>11,}{rel_t:>11.5f}{rel_25:>10.5f}")

    # Note: 'EU' is a distinct GitHub economy code (EU-region IPs not resolved to a
    # member state); it coexists with member states and only affects SG here.
    pd.DataFrame(rows).to_csv("relevancia_sw_resultados.csv", index=False)
    print("\n# wrote relevancia_sw_resultados.csv (versions: total & 2025, with/without EU)")


if __name__ == "__main__":
    main()
