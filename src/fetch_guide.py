#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fetch_guide.py — Genera la GUÍA DE FETCH para el operador (Fase 2).

En entornos donde el fetch automático está bloqueado (HTTP 403 en .gob/.gov,
prensa, arXiv…), el operador debe aportar el texto de las fuentes. Este script
arma, desde `candidatos.csv`, la lista priorizada de candidatos nuevos/dudosos
con sus URLs y el dato crítico a resolver, e indica el procedimiento exacto.

Salida: `data/gates/guia_fetch.md`.
"""
from __future__ import annotations
import csv
import os
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))


def cargar_config():
    import yaml
    with open(os.path.join(ROOT, "config.yaml"), encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _hint(notas: str) -> str:
    # notas suele ser "fuente=...; <pista de verificación>"
    partes = [p.strip() for p in notas.split(";")]
    partes = [p for p in partes if p and not p.lower().startswith("fuente=")]
    return "; ".join(partes) if partes else "—"


def main(argv=None):
    cfg = cargar_config()
    ruta = os.path.join(ROOT, cfg["rutas"]["candidatos"])
    with open(ruta, newline="", encoding="utf-8") as fh:
        rows = [r for r in csv.DictReader(fh) if str(r["tipo_baseline"]).startswith("nuevo")]

    solidos = [r for r in rows if r["tipo_baseline"] == "nuevo"]
    dudosos = [r for r in rows if r["tipo_baseline"] == "nuevo_dudoso"]

    L = ["# Guía de fetch para el operador (Fase 2)", "",
         "**Pipeline ILIA 2026 — Participación Ciudadana**", "",
         "El fetch automático está **bloqueado (HTTP 403)** para casi todas las "
         "fuentes institucionales en este entorno. Para extraer cada ficha hace "
         "falta el **texto de la fuente**. Procedimiento por candidato:", "",
         "1. Abrir la(s) URL(s) y copiar el texto relevante (descripción del caso, "
         "rol de la IA sobre los aportes, organización convocante, año/estado).",
         "2. Guardarlo en `data/fetched/<caso_id>/fuente_1.txt` (y `fuente_2.txt` "
         "para una 2ª fuente independiente) con este encabezado:",
         "",
         "   ```",
         "   ===== FUENTE 1 =====",
         "   URL: <url>",
         "   FETCH: <YYYY-MM-DD>",
         "   ESTADO: ok",
         "",
         "   <pega aquí el texto>",
         "   ```",
         "3. Rearmar el payload y validar/extraer:",
         "   ```bash",
         "   python src/extract.py --prepare <caso_id>        # rearma payloads A/B con el texto",
         "   # (correr la doble pasada en Claude -> guardar data/fichas/<caso_id>_{A,B}.json)",
         "   python src/extract.py --validate data/fichas/<caso_id>_A.json --texto data/fetched/<caso_id>",
         "   python src/reconcile.py <caso_id>",
         "   ```",
         "",
         "> Idealmente **2 fuentes independientes** por caso (≥2 dominios) para que "
         "la conciliación pueda alcanzar confianza ALTA. La prensa solo aporta "
         "señal; prioriza la fuente institucional.", ""]

    def tabla(titulo, lista):
        out = [f"## {titulo} ({len(lista)})", "",
               "| Prioridad | caso_id | País | URL(s) a fetchear | Qué resolver |",
               "|---|---|:---:|---|---|"]
        for i, r in enumerate(lista, 1):
            urls = (r["urls"] or "(buscar fuente institucional)").replace("|", " ;")
            out.append(f"| {i} | `{r['candidato_id']}` | {r['pais']} | {urls} | {_hint(r['notas'])} |")
        out.append("")
        return out

    L += tabla("A. NUEVOS sólidos — prioridad ALTA", solidos)
    L += tabla("B. DUDOSOS — resolver elegibilidad", dudosos)

    out = "\n".join(L)
    dst = os.path.join(ROOT, cfg["rutas"]["gates_dir"], "guia_fetch.md")
    with open(dst, "w", encoding="utf-8") as fh:
        fh.write(out)
    print(f"[ok] {dst}  ({len(solidos)} sólidos + {len(dudosos)} dudosos)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
