#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
discover.py — Fase 1 (Descubrimiento) del pipeline ILIA 2026.

Recorre sistemáticamente los canales A.0–A.11 por país y produce:
  · data/candidatos/candidatos.csv  — candidatos a extraer (Gate 1).
  · data/candidatos/search_frame.csv — frame sistemático país × canal (plan de
        búsqueda exhaustiva; las celdas A.1–A.11 quedan listas para ejecutar con
        fetch / Anexo B).
  · data/gates/gate1_report.md       — insumo del Gate 1 (triage humano).

Canal A.0 (re-verificación del baseline 2025) es 100 % reproducible desde la
BBDD. Los canales A.1–A.9 son operables sin Anexo B (generan celdas de búsqueda);
A.10/A.11 requieren el Anexo B (directorio de medios e instituciones por país).

NOTA (anti-paywall, §7): un hallazgo de prensa (A.10) solo genera CANDIDATO;
la verificación exige fuente institucional (es trabajo de la Fase 2).
"""
from __future__ import annotations
import csv
import datetime
import os
import re
import sys
import unicodedata

import openpyxl

_THIS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(_THIS, ".."))


# --------------------------------------------------------------------------- #
# Utilidades
# --------------------------------------------------------------------------- #
def cargar_config():
    import yaml
    with open(os.path.join(ROOT, "config.yaml"), encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _strip_acentos(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))


def slug(s: str, maxlen: int = 40) -> str:
    s = _strip_acentos(str(s)).lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:maxlen].strip("-")


def nombre_norm(s: str) -> str:
    return re.sub(r"\s+", " ", _strip_acentos(str(s)).lower()).strip()


def _join_urls(*vals):
    urls = []
    for v in vals:
        if v and str(v).strip() and str(v).strip().lower() != "none":
            urls.append(str(v).strip())
    return " | ".join(urls)


# --------------------------------------------------------------------------- #
# Canal A.0 — Re-verificación del baseline 2025 (desde la BBDD)
# --------------------------------------------------------------------------- #
def leer_baseline(cfg):
    ruta = os.path.join(ROOT, cfg["rutas"]["baseline_xlsx"])
    wb = openpyxl.load_workbook(ruta, data_only=True)
    activos, excluidos = [], []

    ws = wb[cfg["rutas"].get("baseline_sheet", "BBDD Casos")]
    for row in ws.iter_rows(min_row=2, max_row=ws.max_row, values_only=True):
        if not row[0] or not row[1]:
            continue
        if str(row[0]).strip() == "" or str(row[1]).strip() == "":
            continue
        activos.append({
            "pais": str(row[0]).strip(),
            "nombre": str(row[1]).strip(),
            "ano": row[2],
            "activo": str(row[3]).strip() if row[3] else "",
            "urls": _join_urls(row[20], row[21], row[22]),
        })

    ws = wb[cfg["rutas"].get("baseline_excluidos_sheet", "BBDD Casos Excluidos")]
    for row in ws.iter_rows(min_row=2, max_row=ws.max_row, values_only=True):
        if not row[1] and not row[2]:
            continue
        excluidos.append({
            "pais": str(row[1]).strip() if row[1] else "",
            "nombre": str(row[2]).strip() if row[2] else "",
            "motivo": str(row[0]).strip() if row[0] else "",
            "ano": row[4],
            "urls": _join_urls(row[5], row[6], row[7]),
        })
    return activos, excluidos


# --------------------------------------------------------------------------- #
# Plantillas de búsqueda por canal (seeds para A.1–A.11)
# --------------------------------------------------------------------------- #
SEED_TEMPLATES = {
    "A.1":  "site:participedia.net {pais_nombre} (inteligencia artificial OR IA)",
    "A.2":  "OGP IRM {pais_nombre} compromiso participación inteligencia artificial",
    "A.3":  "OCDE observatorio IA participación ciudadana {pais_nombre}",
    "A.4":  "({pais_nombre}) participación ciudadana \"inteligencia artificial\" (paper OR informe OR working paper)",
    "A.5":  "portal participación gobierno digital {pais_nombre} inteligencia artificial consulta",
    "A.6":  "Decidim {pais_nombre} inteligencia artificial",
    "A.7":  "(Polis OR CitizenLab OR \"Go Vocal\") {pais_nombre} participación IA",
    "A.8":  "red sociedad civil {pais_nombre} participación ciudadana IA",
    "A.9":  "(PNUD OR UNICEF OR CEPAL OR BID) {pais_nombre} participación ciudadana inteligencia artificial",
    "A.10": "[ANEXO B] medios {pais_nombre}: IA + participación ciudadana / consulta",
    "A.11": "[ANEXO B] institución de participación {pais_nombre}: uso de IA en procesos",
}

NOMBRE_PAIS = {
    "AR":"Argentina","BO":"Bolivia","BR":"Brasil","CL":"Chile","CO":"Colombia",
    "CR":"Costa Rica","CU":"Cuba","DO":"República Dominicana","EC":"Ecuador",
    "GT":"Guatemala","HN":"Honduras","JM":"Jamaica","MX":"México","PA":"Panamá",
    "PE":"Perú","PY":"Paraguay","SV":"El Salvador","UY":"Uruguay","VE":"Venezuela",
}


# --------------------------------------------------------------------------- #
# Construcción de candidatos y frame
# --------------------------------------------------------------------------- #
def construir(cfg, hoy):
    activos, excluidos = leer_baseline(cfg)
    paises = cfg["paises"]
    candidatos = []  # filas dict

    # Canal A.0: casos activos del baseline -> re-verificar actividad 2026.
    for c in activos:
        candidatos.append({
            "candidato_id": f"{c['pais']}-{slug(c['nombre'])}",
            "pais": c["pais"], "nombre_tentativo": c["nombre"], "urls": c["urls"],
            "canal_origen": "A.0", "fecha_hallazgo": hoy,
            "senal": f"Caso del baseline 2025 (estado registrado: {c['activo'] or 's/d'}). "
                     f"Re-verificar actividad y recodificar a esquema 2026.",
            "flag_canal_unico": 1, "tipo_baseline": "activo_2025",
            "estado": "a_reverificar",
            "notas": f"año baseline={c['ano']}",
        })

    # Canal A.0-excluidos: re-verificar si algo cambió (baja prioridad).
    for c in excluidos:
        if c["pais"] not in paises:   # filas LATAM/multipaís: se anotan aparte
            tag_pais = c["pais"] or "LATAM"
        else:
            tag_pais = c["pais"]
        candidatos.append({
            "candidato_id": f"{tag_pais}-EXC-{slug(c['nombre'])}",
            "pais": tag_pais, "nombre_tentativo": c["nombre"], "urls": c["urls"],
            "canal_origen": "A.0-excluidos", "fecha_hallazgo": hoy,
            "senal": f"Excluido en 2025 por: {c['motivo'] or 's/d'}. "
                     f"Re-verificar si cambió la elegibilidad 2026.",
            "flag_canal_unico": 1, "tipo_baseline": "excluido_2025",
            "estado": "reverificar_exclusion",
            "notas": f"año={c['ano']}",
        })

    # Garantizar cobertura de los 19 países: placeholder donde no hay candidato.
    con_candidato = {c["pais"] for c in candidatos if c["pais"] in paises}
    for p in paises:
        if p not in con_candidato:
            candidatos.append({
                "candidato_id": f"{p}-SIN-BASELINE",
                "pais": p, "nombre_tentativo": "(sin candidatos de baseline)",
                "urls": "", "canal_origen": "—", "fecha_hallazgo": hoy,
                "senal": "Sin casos en el baseline 2025. Cubrir vía canales "
                         "A.1–A.11 (requiere fetch / Anexo B).",
                "flag_canal_unico": 0, "tipo_baseline": "",
                "estado": "sin_candidatos_baseline",
                "notas": "",
            })

    # Unicidad de candidato_id (dos casos distintos pueden compartir slug).
    vistos = {}
    for c in candidatos:
        base = c["candidato_id"]
        if base in vistos:
            vistos[base] += 1
            c["candidato_id"] = f"{base}-{vistos[base]}"
        else:
            vistos[base] = 1

    # Frame sistemático país × canal (plan de búsqueda exhaustiva).
    frame = []
    canales = cfg["descubrimiento"]["canales"]
    for p in paises:
        for canal in canales:
            cid = canal["id"]
            operable = bool(canal.get("operable"))
            req_anexo = bool(canal.get("requiere_anexo_b"))
            if cid == "A.0":
                estado = "ejecutado"   # ya corrido arriba
                seed = "BBDD baseline 2025 (casos + excluidos)"
            elif req_anexo and not cfg["descubrimiento"].get("anexo_b_disponible"):
                estado = "bloqueado_anexo_b"
                seed = SEED_TEMPLATES.get(cid, "").format(pais_nombre=NOMBRE_PAIS[p])
            else:
                estado = "pendiente_fetch"
                seed = SEED_TEMPLATES.get(cid, "").format(pais_nombre=NOMBRE_PAIS[p])
            frame.append({
                "pais": p, "canal_id": cid, "canal_nombre": canal["nombre"],
                "operable": int(operable), "requiere_anexo_b": int(req_anexo),
                "seed_query": seed, "estado": estado, "notas": "",
            })

    return candidatos, frame, activos, excluidos


# --------------------------------------------------------------------------- #
# Escritura
# --------------------------------------------------------------------------- #
CAND_COLS = ["candidato_id","pais","nombre_tentativo","urls","canal_origen",
             "fecha_hallazgo","senal","flag_canal_unico","tipo_baseline","estado","notas"]
FRAME_COLS = ["pais","canal_id","canal_nombre","operable","requiere_anexo_b",
              "seed_query","estado","notas"]


def escribir_csv(ruta, cols, filas):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        for f in filas:
            w.writerow({k: f.get(k, "") for k in cols})


def detectar_duplicados(candidatos):
    """Duplicados probables: mismo país + nombre normalizado (o URL compartida)."""
    grupos = {}
    for c in candidatos:
        if c["tipo_baseline"] == "excluido_2025":
            continue
        grupos.setdefault((c["pais"], nombre_norm(c["nombre_tentativo"])), []).append(c["candidato_id"])
    return {k: v for k, v in grupos.items() if len(v) > 1}


def gate1_report(cfg, candidatos, frame, activos, excluidos, hoy):
    paises = cfg["paises"]
    n_activos = sum(1 for c in candidatos if c["tipo_baseline"] == "activo_2025")
    n_excl = sum(1 for c in candidatos if c["tipo_baseline"] == "excluido_2025")
    n_canal_unico = sum(1 for c in candidatos if c["flag_canal_unico"] == 1)
    por_pais = {p: 0 for p in paises}
    for c in candidatos:
        if c["pais"] in por_pais and c["estado"] in ("a_reverificar",):
            por_pais[c["pais"]] += 1
    dups = detectar_duplicados(candidatos)

    operables = [f for f in frame if f["estado"] == "pendiente_fetch"]
    bloqueados = [f for f in frame if f["estado"] == "bloqueado_anexo_b"]

    L = []
    L.append("# Gate 1 — Reporte de Triage (Fase 1: Descubrimiento)")
    L.append("")
    L.append(f"**Fecha de corrida:** {hoy}  ·  **Pipeline ILIA 2026 — Participación Ciudadana**")
    L.append("")
    L.append("> El Gate 1 es HUMANO. Este reporte prepara insumos; no autoaprueba "
             "candidatos. El operador decide qué pasa a Fase 2 (extracción).")
    L.append("")
    L.append("## 1. Resumen")
    L.append("")
    L.append(f"- Candidatos del baseline activo 2025 (canal A.0): **{n_activos}**")
    L.append(f"- Casos excluidos 2025 a re-verificar (canal A.0-excluidos): **{n_excl}**")
    L.append(f"- Candidatos marcados de canal único (`flag_canal_unico=1`): **{n_canal_unico}** "
             f"(esperable en esta corrida: solo se ejecutó A.0)")
    L.append(f"- Cobertura: **{len(paises)}/19** países representados en candidatos.csv")
    L.append("")
    L.append("## 2. Candidatos nuevos vs. baseline")
    L.append("")
    L.append("En esta corrida NO hay candidatos *nuevos* (canales A.1–A.11 aún no "
             "ejecutados con fetch / Anexo B). Todos los candidatos provienen del "
             "baseline 2025 (canal A.0). Los nuevos aparecerán al ejecutar el "
             "`search_frame.csv`.")
    L.append("")
    L.append("## 3. Candidatos del baseline ACTIVO 2025 por país (a re-verificar 2026)")
    L.append("")
    L.append("| País | N | Casos |")
    L.append("|---|---|---|")
    for p in paises:
        casos_p = [c["nombre_tentativo"] for c in candidatos
                   if c["pais"] == p and c["tipo_baseline"] == "activo_2025"]
        nombres = "; ".join(casos_p) if casos_p else "—"
        L.append(f"| {p} | {len(casos_p)} | {nombres} |")
    L.append("")
    L.append("## 4. Duplicados probables (mismo país + nombre normalizado)")
    L.append("")
    if dups:
        for (p, n), ids in dups.items():
            L.append(f"- **{p}** · «{n}» → {', '.join(ids)}")
    else:
        L.append("Ninguno detectado entre candidatos activos.")
    L.append("")
    L.append("## 5. Casos del baseline SIN señal de actividad 2026")
    L.append("")
    L.append("Todos los casos del baseline activo entran como `a_reverificar`: en "
             "esta corrida (sin fetch) NO se ha confirmado su actividad 2026. El "
             "Gate 1 debe priorizar la re-verificación de actividad antes de Fase 2.")
    L.append("")
    L.append("## 6. Estado de canales (frame de búsqueda)")
    L.append("")
    L.append(f"- Canal A.0 (baseline): **ejecutado**.")
    L.append(f"- Canales operables sin Anexo B, **pendientes de fetch**: "
             f"{len(operables)} celdas país×canal (A.1–A.9).")
    L.append(f"- Canales **bloqueados por falta de Anexo B** (A.10/A.11): "
             f"{len(bloqueados)} celdas. Pedir Anexo B al operador.")
    L.append("")
    L.append("Detalle por canal (celdas en el frame):")
    L.append("")
    L.append("| Canal | Nombre | Estado | Celdas |")
    L.append("|---|---|---|---|")
    canales = cfg["descubrimiento"]["canales"]
    for canal in canales:
        cid = canal["id"]
        celdas = [f for f in frame if f["canal_id"] == cid]
        estado = celdas[0]["estado"] if celdas else "—"
        L.append(f"| {cid} | {canal['nombre']} | {estado} | {len(celdas)} |")
    L.append("")
    L.append("## 7. Decisiones que requieren al operador")
    L.append("")
    L.append("1. **Anexo B** (directorio medios/instituciones por país): bloquea "
             "A.10/A.11. Sin él, la Fase 1 queda incompleta para esos canales.")
    L.append("2. **Ejecución del `search_frame.csv`**: requiere una corrida con "
             "fetch (web) para A.1–A.9. Define presupuesto y prioridad por país.")
    L.append("3. **Tratamiento de `flag_canal_unico`** y de los **49 excluidos** "
             "(¿re-verificar todos o muestrear?).")
    L.append("")
    return "\n".join(L)


def main(argv=None):
    cfg = cargar_config()
    hoy = datetime.date.today().isoformat()
    candidatos, frame, activos, excluidos = construir(cfg, hoy)

    ruta_cand = os.path.join(ROOT, cfg["rutas"]["candidatos"])
    ruta_frame = os.path.join(os.path.dirname(ruta_cand), "search_frame.csv")
    ruta_gate1 = os.path.join(ROOT, cfg["rutas"]["gates_dir"], "gate1_report.md")

    escribir_csv(ruta_cand, CAND_COLS, candidatos)
    escribir_csv(ruta_frame, FRAME_COLS, frame)
    os.makedirs(os.path.dirname(ruta_gate1), exist_ok=True)
    with open(ruta_gate1, "w", encoding="utf-8") as fh:
        fh.write(gate1_report(cfg, candidatos, frame, activos, excluidos, hoy))

    print(f"candidatos.csv   -> {ruta_cand}  ({len(candidatos)} filas)")
    print(f"search_frame.csv -> {ruta_frame} ({len(frame)} filas)")
    print(f"gate1_report.md  -> {ruta_gate1}")
    print(f"Cobertura: {len({c['pais'] for c in candidatos if c['pais'] in cfg['paises']})}/19 países")
    return 0


if __name__ == "__main__":
    sys.exit(main())
