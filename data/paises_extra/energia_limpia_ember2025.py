#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Indicador 145 — % energía LIMPIA (= renovables + nuclear, incl. hidro) desde EMBER 2025.
Determinístico, reproducible. Fuente: ember_generacion_electrica_2025.csv (EMBER, año 2025).
Decisión del operador (2026-06-22): incluir nuclear e hidro; a confirmar con CENIA."""
import csv, os
HERE = os.path.dirname(os.path.abspath(__file__))
RENEW = {"Bioenergy", "Hydro", "Solar", "Wind", "Other renewables"}
NUCLEAR = {"Nuclear"}
FOSSIL = {"Coal", "Gas", "Other fossil"}
ES = {"Spain": "España", "Estonia": "Estonia", "Singapore": "Singapur", "Germany": "Alemania", "Portugal": "Portugal"}
ORDER = ["España", "Estonia", "Singapur", "Alemania", "Portugal"]

data = {}
with open(os.path.join(HERE, "ember_generacion_electrica_2025.csv")) as f:
    for row in csv.DictReader(f):
        data.setdefault(row["entity"], {})[row["series"]] = float(row["generation_twh"] or 0)

res = {}
for en, nice in ES.items():
    d = data[en]; tot = d["Total generation"]
    renew = sum(v for k, v in d.items() if k in RENEW)
    nuc = sum(v for k, v in d.items() if k in NUCLEAR)
    res[nice] = {"renov_pct": round(100*renew/tot, 2), "nuclear_pct": round(100*nuc/tot, 2),
                 "limpia_pct": round(100*(renew+nuc)/tot, 2), "hidro_pct": round(100*d.get("Hydro", 0)/tot, 2)}

if __name__ == "__main__":
    print(f"{'País':9} {'Renov%':>7} {'Nuclear%':>8} {'LIMPIA%':>8} {'Hidro%':>7}")
    for p in ORDER:
        r = res[p]; print(f"{p:9} {r['renov_pct']:6.2f}% {r['nuclear_pct']:7.2f}% {r['limpia_pct']:7.2f}% {r['hidro_pct']:6.2f}%")
    out = os.path.join(HERE, "energia_limpia_resultados_2025.csv")
    with open(out, "w", newline="") as f:
        w = csv.writer(f); w.writerow(["pais", "renovables_pct", "nuclear_pct", "limpia_pct", "hidro_pct"])
        for p in ORDER:
            r = res[p]; w.writerow([p, r["renov_pct"], r["nuclear_pct"], r["limpia_pct"], r["hidro_pct"]])
    print("OK ->", out)
