#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
simulate.py — Fase 4: tablas comparativas (§8).

Tabla país × {V2025 oficial · 2026 retrospectivo A · 2026 retrospectivo B} +
sensibilidad a `count_min_level`. SOLO ejecutable con la BBDD cargada.

REGLA DE ORO: ningún número sale de memoria. La columna 2025 se RECALCULA con el
motor legacy (no se copia del oficial; el oficial se muestra solo como control).

ATENCIÓN: las columnas 2026 usan la RECODIFICACIÓN BORRADOR (pre-Gate) de
data/baseline/recodificacion_2025.csv. Son DRAFT hasta validación humana.
"""
from __future__ import annotations
import copy
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import calc_engine as ce  # noqa: E402

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

OFICIAL_IND = {"AR":0,"BO":30,"BR":76,"CL":57,"CO":85,"CR":46,"CU":0,"DO":30,"EC":25,
               "GT":32,"HN":42,"JM":0,"MX":47,"PA":0,"PE":53,"PY":0,"SV":0,"UY":0,"VE":0}


def cargar_config():
    import yaml
    with open(os.path.join(ROOT, "config.yaml"), encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _cfg_variante(base, scenario, count_min_level):
    c = copy.deepcopy(base)
    c.setdefault("escenarios", {})["scenario_activo"] = scenario
    c.setdefault("cantidad", {})["count_min_level"] = count_min_level
    return c


def main(argv=None):
    cfg = cargar_config()
    xlsx = os.path.join(ROOT, cfg["rutas"]["baseline_xlsx"])
    if not os.path.exists(xlsx):
        print("BLOQUEADO: BBDD no disponible en", xlsx)
        print("simulate.py solo se ejecuta con la BBDD cargada (§8).")
        return 2

    casos = ce.load_casos(xlsx)
    recod_path = os.path.join(ROOT, cfg["rutas"]["recodificacion_2025"])
    recod = ce.load_recodificacion_csv(recod_path)
    recod_ok = len(recod) > 0

    # --- Control 2025: el motor legacy reproduce el oficial ---
    sub1_25, sub2_25, ind_25, _ = ce.compute_full(casos)
    max_delta = max(abs(ind_25[p] - OFICIAL_IND[p]) for p in ce.PAISES)

    # --- Variantes 2026 (DRAFT) ---
    A2 = ce.run_2026(casos, _cfg_variante(cfg, "A", 2), recod)
    A0 = ce.run_2026(casos, _cfg_variante(cfg, "A", 0), recod)
    B2 = ce.run_2026(casos, _cfg_variante(cfg, "B", 2), recod)

    L = []
    L.append("# Fase 4 — Simulación comparativa (motor v2026)")
    L.append("")
    L.append("> **Las columnas 2026 son BORRADOR.** Dependen de la recodificación "
             "pre-Gate (`data/baseline/recodificacion_2025.csv`): convocante derivado "
             "de la columna *Organización a cargo* y nivel de consolidación asignado "
             "de forma conservadora (Uso único/Plataforma → 2; 'Próximamente' → 1; "
             "nivel 3 solo con override + evidencia de recurrencia). NO publicar sin "
             "validación humana.")
    L.append("")
    L.append(f"- Recodificación cargada: {'sí' if recod_ok else 'NO (columnas 2026 vacías)'} "
             f"({len(recod)} filas)")
    L.append(f"- Redondeo: `{cfg.get('redondeo',{}).get('modo','legacy')}`  ·  "
             f"thresholds y count_min_level desde config.yaml")
    L.append("")
    L.append("## Control 2025 (motor legacy recalculado vs. oficial publicado)")
    L.append("")
    L.append(f"Desviación máxima |motor − oficial| = **{max_delta}** punto(s) "
             f"({'OK ≤1' if max_delta <= 1 else 'REVISAR'}).")
    L.append("")
    L.append("## Indicador final por país")
    L.append("")
    L.append("| País | 2025 oficial | 2025 motor | 2026-A (cml=2) | 2026-A (cml=0) | 2026-B (cml=2) |")
    L.append("|------|:---:|:---:|:---:|:---:|:---:|")
    for p in ce.PAISES:
        L.append(f"| {p} | {OFICIAL_IND[p]} | {ind_25[p]} | "
                 f"{A2[2][p]} | {A0[2][p]} | {B2[2][p]} |")
    L.append("")
    L.append("## Descomposición Sub1 (2026-A, cml=2) — DRAFT")
    L.append("")
    L.append("| País | Tipos | Etapas | Continuidad | Convocante | Cantidad | Sub1 | n | n_cant |")
    L.append("|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|")
    s1 = A2[0]
    for p in ce.PAISES:
        d = s1[p]
        if d["n"] == 0:
            continue
        L.append(f"| {p} | {d['tipos']:.0f} | {d['etapas']:.0f} | {d['cont']:.0f} | "
                 f"{d['conv']:.0f} | {d['cant']:.0f} | {d['v']:.0f} | {d['n']} | {d.get('n_cant','')} |")
    L.append("")
    L.append("_Sub2 (Desarrollo) es idéntico a 2025 por construcción (§4.3)._")
    L.append("")

    out = "\n".join(L)
    ruta = os.path.join(ROOT, cfg["rutas"]["gates_dir"], "simulacion_2026.md")
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "w", encoding="utf-8") as fh:
        fh.write(out)

    print(out)
    print(f"\n[ok] escrito {ruta}")
    print(f"[control] desviación máx 2025 motor vs oficial = {max_delta} (≤1 = OK)")
    return 0 if max_delta <= 1 else 1


if __name__ == "__main__":
    sys.exit(main())
