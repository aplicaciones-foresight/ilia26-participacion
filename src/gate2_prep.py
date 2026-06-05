#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gate2_prep.py — Prepara la cola priorizada del Gate 2 (§7 Fase 3 -> Gate 2).

Escanea las fichas conciliadas (`data/fichas/*_conciliada.json`) y arma la cola
de revisión humana:
  - TODAS las de confianza BAJA y MEDIA (revisión completa);
  - una MUESTRA aleatoria de las ALTA (config `muestreo.muestra_alta_pct`,
    `semilla_aleatoria`), reproducible.
Si el error en campos críticos de la muestra supera `umbral_escalamiento`, el
operador amplía la muestra (regla de escalamiento configurable).

Salida: `data/gates/gate2_cola.md`. Las decisiones se registran en `gate2_log.csv`.
"""
from __future__ import annotations
import glob
import json
import os
import random
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))


def cargar_config():
    import yaml
    with open(os.path.join(ROOT, "config.yaml"), encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def main(argv=None):
    cfg = cargar_config()
    fdir = os.path.join(ROOT, cfg["rutas"]["fichas_dir"])
    m = cfg.get("muestreo", {})
    pct = float(m.get("muestra_alta_pct", 0.10))
    semilla = int(m.get("semilla_aleatoria", 2026))
    umbral = float(m.get("umbral_escalamiento", 0.05))

    fichas = []
    for p in sorted(glob.glob(os.path.join(fdir, "*_conciliada.json"))):
        with open(p, encoding="utf-8") as fh:
            fichas.append(json.load(fh))

    por = {"ALTA": [], "MEDIA": [], "BAJA": []}
    for f in fichas:
        por.get(f.get("confianza", "BAJA"), por["BAJA"]).append(f)

    # Muestra reproducible de ALTA.
    rng = random.Random(semilla)
    n_muestra = max(1, round(len(por["ALTA"]) * pct)) if por["ALTA"] else 0
    muestra_alta = set()
    if por["ALTA"]:
        ids = sorted(f["caso_id"] for f in por["ALTA"])
        muestra_alta = set(rng.sample(ids, min(n_muestra, len(ids))))

    L = ["# Gate 2 — Cola de revisión (priorizada)", "",
         f"**Fecha:** generado por `gate2_prep.py` · Pipeline ILIA 2026", "",
         "> Gate 2 es HUMANO. Revisar BAJA y MEDIA completas + muestra de ALTA. "
         f"Si el error en campos críticos de la muestra supera **{umbral:.0%}**, "
         "ampliar la muestra (escalamiento). Registrar decisiones en `gate2_log.csv`.", "",
         "## Resumen", "",
         f"- Fichas conciliadas: **{len(fichas)}** "
         f"(BAJA {len(por['BAJA'])} · MEDIA {len(por['MEDIA'])} · ALTA {len(por['ALTA'])})",
         f"- Muestra de ALTA a revisar: **{len(muestra_alta)}** ({pct:.0%}, semilla {semilla})", ""]

    def fila(f, en_cola, motivo):
        c = f.get("conciliacion", {})
        conf = c.get("conflictos_criticos", []) or "—"
        return (f"| {f['caso_id']} | {f.get('confianza')} | {motivo} | "
                f"{conf} | {c.get('evidencia_verificada')} | "
                f"{c.get('n_fuentes_independientes')} |")

    L += ["## Cola de revisión", "",
          "| caso_id | confianza | en cola por | conflictos críticos | evidencia ok | fuentes |",
          "|---|---|---|---|:---:|:---:|"]
    for f in por["BAJA"]:
        L.append(fila(f, True, "BAJA (completa)"))
    for f in por["MEDIA"]:
        L.append(fila(f, True, "MEDIA (completa)"))
    for f in por["ALTA"]:
        if f["caso_id"] in muestra_alta:
            L.append(fila(f, True, "ALTA (muestra)"))
    L.append("")
    fuera = [f["caso_id"] for f in por["ALTA"] if f["caso_id"] not in muestra_alta]
    if fuera:
        L += [f"_ALTA fuera de muestra (no se revisan salvo escalamiento): {len(fuera)}_", ""]

    if not fichas:
        L += ["_(Aún no hay fichas conciliadas. Correr Fase 2 + `reconcile.py` primero.)_", ""]

    out = "\n".join(L)
    ruta = os.path.join(ROOT, cfg["rutas"]["gates_dir"], "gate2_cola.md")
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "w", encoding="utf-8") as fh:
        fh.write(out)
    print(out)
    print(f"\n[ok] {ruta}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
