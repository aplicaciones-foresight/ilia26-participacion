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

    # Latest available period
    ly, lq = repos.sort_values(["year", "quarter"]).iloc[-1][["year", "quarter"]]
    ly, lq = int(ly), int(lq)
    print(f"# Latest period: {ly} Q{lq}\n")

    cq = collab[(collab.year == ly) & (collab.quarter == lq)]
    rq = repos[(repos.year == ly) & (repos.quarter == lq)].set_index("iso2_code")["repositories"]

    print(f"{'country':<8}{'repos':>12}{'inbound':>12}{'inbound_noEU':>14}"
          f"{'relevancia':>12}{'relev_noEU':>12}")
    rows = []
    for c in COUNTRIES:
        inbound = int(cq[cq.destination == c]["weight"].sum())
        inbound_noeu = int(cq[(cq.destination == c) & (cq.source != "EU")]["weight"].sum())
        nrep = int(rq.get(c, 0))
        rel = inbound / nrep if nrep else float("nan")
        rel_noeu = inbound_noeu / nrep if nrep else float("nan")
        rows.append((c, nrep, inbound, inbound_noeu, rel, rel_noeu))
        print(f"{c:<8}{nrep:>12,}{inbound:>12,}{inbound_noeu:>14,}"
              f"{rel:>12.5f}{rel_noeu:>12.5f}")

    # Note: 'EU' is a distinct GitHub economy code (EU-region IPs not resolved to
    # a member state); it coexists with member states and only affects SG here.
    out = pd.DataFrame(rows, columns=["iso2", "repositories", "inbound",
                                      "inbound_noEU", "relevancia",
                                      "relevancia_noEU"])
    out.insert(1, "period", f"{ly}Q{lq}")
    out.to_csv("relevancia_sw_resultados.csv", index=False)
    print("\n# wrote relevancia_sw_resultados.csv")


if __name__ == "__main__":
    main()
