#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cruce_inventario_ia_latam.py — Canal A.15 (cruce con inventario externo).

Cruza un inventario general de IA en el sector público de América Latina
(BD_IA_LATAM, p. ej. Gutiérrez et al.) contra los casos que el pipeline YA
identificó (`candidatos.csv` + baseline 2025), para detectar casos de IA en
participación ciudadana que se hayan escapado en las primeras rondas de
búsqueda (Fase 1).

Idea: el inventario es un universo amplio y ruidoso (vigilancia, atención
ciudadana, salud, etc.). La participación es una porción pequeña, así que:
  1) se filtra el inventario por SEÑALES de participación combinando
       · la clasificación BID "Participación ciudadana e interacción con
         ciudadanos" (¡incluye atención!, por eso no basta sola),
       · la clasificación JRC nivel II "Gestión de la participación",
       · términos de participación deliberativa/propositiva en texto;
  2) se restringe a los 20 países del universo (config.paises);
  3) se descartan los que ya están en el conjunto conocido (match por nombre);
  4) lo que queda se reporta para triage humano (Gate 1). El script NO decide
     elegibilidad: "Participación ciudadana e interacción con ciudadanos" mezcla
     participación con atención, de modo que la mayoría del pool son chatbots de
     servicio / PQRS / biometría electoral que el Gate suele excluir.

El inventario NO se versiona en el repo (archivo grande, externo). Colócalo en
`data/external/BD_IA_LATAM.xlsx` o pásalo con `--inventario RUTA`.

Salidas:
  · data/candidatos/cruce_inventario_ia_latam.csv — pool con señal y clasificación
  · data/gates/cruce_inventario_ia_latam.md       — reporte legible para el Gate

Uso:
  python src/cruce_inventario_ia_latam.py [--inventario RUTA] [--hoja NOMBRE]
"""
from __future__ import annotations
import argparse
import csv
import os
import re
import sys
import unicodedata

import openpyxl

_THIS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(_THIS, ".."))

INVENTARIO_DEFAULT = os.path.join("data", "external", "BD_IA_LATAM.xlsx")
HOJA_DEFAULT = "Sistemas de IA en ALC"

# País (texto del inventario) -> ISO-2 del universo (20 países).
PAIS_ISO = {
    "argentina": "AR", "bolivia": "BO", "brasil": "BR", "chile": "CL",
    "colombia": "CO", "costa rica": "CR", "cuba": "CU",
    "republica dominicana": "DO", "ecuador": "EC", "guatemala": "GT",
    "honduras": "HN", "jamaica": "JM", "mexico": "MX", "panama": "PA",
    "peru": "PE", "paraguay": "PY", "el salvador": "SV",
    "trinidad y tobago": "TT", "uruguay": "UY", "venezuela": "VE",
}

# Señal por clasificación propia del inventario (normalizada).
RE_BID_PARTICIP = re.compile(r"participacion ciudadana e interaccion")
RE_JRC_PARTICIP = re.compile(r"gestion de la part")  # tolera el typo "partipacion"

# Señal por texto: participación deliberativa/propositiva (recall amplio).
RE_TEXTO_PARTICIP = re.compile(
    r"participaci|participativ|presupuesto participativo|orcamento participativo|"
    r"consulta (publica|ciudadana|popular)|consulta popular|audiencia publica|"
    r"\bcabildo|mesa de dialogo|\bdeliberaci|deliberativ|mini publico|"
    r"iniciativa popular|conferencia nacional|"
    r"sistematizacion de (aportes|propuestas|contribuciones)|"
    r"propuestas ciudadanas|aportes ciudadanos|contribuciones ciudadanas|"
    r"ideas (legislativas|ciudadanas)|crowdlaw|senador virtual|"
    r"opiniones (ciudadanas|de los ciudadanos)|comentarios de los ciudadanos|"
    r"argumentos a favor o en contra|dialogos (ciudadan|regional|social)|decidim"
)

# NÚCLEO de participación (alta precisión): IA sobre el CONTENIDO de aportes
# ciudadanos en procesos deliberativos/propositivos. Es el discriminador real
# frente a atención ciudadana / PQRS / biometría. Lo que matchee aquí es lo que
# de verdad merece revisión del Gate.
RE_NUCLEO_PARTICIP = re.compile(
    r"presupuesto participativo|orcamento participativo|"
    r"consulta (ciudadana|popular)|consulta popular|audiencia publica|"
    r"\bcabildo|\bdeliberaci|deliberativ|mini publico|iniciativa popular|"
    r"conferencia nacional|sistematizacion de (aportes|propuestas|contribuciones)|"
    r"propuestas ciudadanas|aportes ciudadanos|contribuciones ciudadanas|"
    r"ideas (legislativas|ciudadanas)|crowdlaw|senador virtual|"
    r"opiniones (ciudadanas|de los ciudadanos)|comentarios de los ciudadanos|"
    r"argumentos a favor o en contra|dialogos (ciudadan|regional|social)|decidim"
)

# Pistas de "fuera de alcance" para anotar el triage (NO excluye por sí solo).
RE_ATENCION = re.compile(
    r"atencion ciudadan|atencion al ciudadano|\btramite|resolver (dudas|consultas)|"
    r"preguntas frecuentes|servicio al ciudadano|asistente virtual|chatbot"
)
RE_PQRS = re.compile(r"\bpqrs?\b|peticiones quejas|quejas reclamos|reclamacion")
RE_ELECTORAL_SEG = re.compile(
    r"biometric|reconocimiento facial|suplantacion|fraude|censo electoral|"
    r"centros de votacion|autenticacion|identidad de los votantes"
)


# --------------------------------------------------------------------------- #
# Utilidades (coherentes con discover.py)
# --------------------------------------------------------------------------- #
def cargar_config():
    import yaml
    with open(os.path.join(ROOT, "config.yaml"), encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _strip_acentos(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))


def slug(s: str, maxlen: int = 45) -> str:
    s = _strip_acentos(str(s)).lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:maxlen].strip("-")


def nombre_norm(s) -> str:
    # insensible a acentos, mayúsculas y puntuación.
    s = re.sub(r"[^a-z0-9]+", " ", _strip_acentos(str(s)).lower())
    return re.sub(r"\s+", " ", s).strip()


# Palabras vacías para el match de nombres (genéricas del dominio).
_STOP = {
    "de", "la", "el", "los", "las", "del", "con", "para", "y", "e", "en",
    "ia", "inteligencia", "artificial", "sistema", "plataforma", "chatbot",
    "nacional", "gobierno", "ministerio", "secretaria", "del", "un", "una",
}


# --------------------------------------------------------------------------- #
# Conjunto conocido (lo ya identificado por el pipeline)
# --------------------------------------------------------------------------- #
def cargar_conocidos(cfg) -> set[str]:
    nombres: set[str] = set()

    cand = os.path.join(ROOT, cfg["rutas"]["candidatos"])
    if os.path.exists(cand):
        with open(cand, encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                if row.get("nombre_tentativo"):
                    nombres.add(nombre_norm(row["nombre_tentativo"]))

    base = os.path.join(ROOT, cfg["rutas"]["baseline_xlsx"])
    if os.path.exists(base):
        wb = openpyxl.load_workbook(base, data_only=True, read_only=True)
        for hoja, col in (
            (cfg["rutas"].get("baseline_sheet", "BBDD Casos"), "Caso"),
            (cfg["rutas"].get("baseline_excluidos_sheet", "BBDD Casos Excluidos"), "Titulo"),
        ):
            if hoja not in wb.sheetnames:
                continue
            ws = wb[hoja]
            filas = ws.iter_rows(values_only=True)
            cab = [str(c).strip() if c is not None else "" for c in next(filas)]
            try:
                idx = cab.index(col)
            except ValueError:
                continue
            for fila in filas:
                if idx < len(fila) and fila[idx]:
                    nombres.add(nombre_norm(fila[idx]))

    nombres.discard("")
    return nombres


def es_conocido(nombre: str, conocidos: set[str]) -> str | None:
    """Devuelve el nombre conocido que matchea, o None. Match por substring o
    por solapamiento de tokens significativos (Jaccard sobre no-stopwords)."""
    n = nombre_norm(nombre)
    nt = set(n.split()) - _STOP
    if not nt:
        return None
    for k in conocidos:
        if n and min(len(n), len(k)) > 6 and (n in k or k in n):
            return k
        kt = set(k.split()) - _STOP
        if not kt:
            continue
        sig = nt & kt
        if len(sig) >= 2 and len(sig) / len(nt) >= 0.5:
            return k
    return None


# --------------------------------------------------------------------------- #
# Lectura del inventario externo
# --------------------------------------------------------------------------- #
def leer_inventario(ruta: str, hoja: str):
    wb = openpyxl.load_workbook(ruta, data_only=True, read_only=True)
    if hoja not in wb.sheetnames:
        sys.exit(f"ERROR: la hoja '{hoja}' no existe. Hojas: {wb.sheetnames}")
    ws = wb[hoja]
    filas = ws.iter_rows(values_only=True)
    cab = [str(c).replace("\n", " ").strip() if c is not None else "" for c in next(filas)]

    def idx(sub):
        for i, c in enumerate(cab):
            if sub.lower() in c.lower():
                return i
        return None

    col = {
        "id": idx("ID"), "pais": idx("País"), "nombre": idx("Nombre del sistema"),
        "entidad": idx("Entidad pública"), "kw": idx("Palabra clave"),
        "resumen": idx("Resumen del sistema"), "estado": idx("Estado conocido"),
        "bid": idx("Clasificación BID"), "jrc2": idx("nivel II JRC"),
    }
    registros = []
    for fila in filas:
        if col["id"] is None or col["id"] >= len(fila) or fila[col["id"]] is None:
            continue
        def g(k):
            i = col[k]
            return fila[i] if (i is not None and i < len(fila)) else None
        registros.append({
            "id": g("id"), "pais": g("pais"), "nombre": g("nombre"),
            "entidad": g("entidad"), "kw": g("kw"), "resumen": g("resumen"),
            "estado": g("estado"), "bid": g("bid"), "jrc2": g("jrc2"),
        })
    return registros


# --------------------------------------------------------------------------- #
# Cruce
# --------------------------------------------------------------------------- #
def cruzar(registros, paises_universo, conocidos):
    pool = []
    for r in registros:
        iso = PAIS_ISO.get(nombre_norm(r["pais"]))
        if iso not in paises_universo:
            continue
        blob = nombre_norm(f"{r['nombre']} {r['kw']} {r['resumen']}")
        senales = []
        if RE_BID_PARTICIP.search(nombre_norm(r["bid"])):
            senales.append("BID")
        if RE_JRC_PARTICIP.search(nombre_norm(r["jrc2"])):
            senales.append("JRC-gestión-particip")
        if RE_TEXTO_PARTICIP.search(blob):
            senales.append("texto")
        if not senales:
            continue
        match = es_conocido(r["nombre"], conocidos)
        # Anotación de triage (orientativa, NO decide elegibilidad). El núcleo de
        # participación manda: si la IA actúa sobre el contenido de aportes
        # ciudadanos, se marca REVISAR aunque también dispare patrones de "fuera".
        if RE_NUCLEO_PARTICIP.search(blob):
            triage = "REVISAR (núcleo de participación)"
        elif RE_PQRS.search(blob):
            triage = "fuera (PQRS/gestión de quejas)"
        elif RE_ELECTORAL_SEG.search(blob):
            triage = "fuera (biometría/seguridad electoral/fraude)"
        elif RE_ATENCION.search(blob):
            triage = "fuera (atención ciudadana / servicio)"
        else:
            triage = "revisar (señal débil)"
        pool.append({
            "id": r["id"], "iso": iso, "nombre": str(r["nombre"]).strip(),
            "entidad": str(r["entidad"]).strip(), "estado": str(r["estado"]).strip(),
            "bid": str(r["bid"]).strip(), "jrc2": str(r["jrc2"]).replace("\n", " ").strip(),
            "kw": str(r["kw"]).strip(), "resumen": str(r["resumen"]).strip(),
            "senales": "+".join(senales),
            "match_conocido": match or "",
            "triage": "YA IDENTIFICADO" if match else triage,
        })
    pool.sort(key=lambda x: (x["match_conocido"] != "", x["iso"], x["id"]))
    return pool


# --------------------------------------------------------------------------- #
# Salidas
# --------------------------------------------------------------------------- #
def escribir_csv(pool, ruta):
    campos = ["id", "iso", "nombre", "entidad", "estado", "bid", "jrc2", "kw",
              "senales", "match_conocido", "triage", "resumen"]
    with open(ruta, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=campos)
        w.writeheader()
        for p in pool:
            w.writerow(p)


def escribir_reporte(pool, ruta, total_inv, total_universo):
    nuevos = [p for p in pool if not p["match_conocido"]]
    revisar = [p for p in nuevos if p["triage"].startswith("REVISAR")]
    ya = [p for p in pool if p["match_conocido"]]
    L = []
    L.append("# Canal A.15 — Cruce con inventario IA-LATAM\n")
    L.append("Cruce del inventario externo (BD_IA_LATAM) contra el conjunto ya "
             "identificado (`candidatos.csv` + baseline 2025).\n")
    L.append(f"- Sistemas en el inventario: **{total_inv}**")
    L.append(f"- En los 20 países del universo: **{total_universo}**")
    L.append(f"- Con señal de participación: **{len(pool)}** "
             f"(ya identificados: {len(ya)}; nuevos: {len(nuevos)})")
    L.append(f"- De los nuevos, a **REVISAR** (posible participación): **{len(revisar)}**\n")
    L.append("> La categoría BID «Participación ciudadana e interacción con "
             "ciudadanos» mezcla participación con **atención**; por eso la mayoría "
             "del pool son chatbots de servicio / PQRS / biometría electoral. La "
             "columna `triage` es orientativa: la elegibilidad la decide el Gate.\n")

    def bloque(titulo, items):
        L.append(f"\n## {titulo} ({len(items)})\n")
        for p in items:
            L.append(f"### ID {p['id']} · {p['iso']} · {p['estado']} · señal: {p['senales']}")
            L.append(f"- **{p['nombre']}**")
            L.append(f"- Entidad: {p['entidad']}")
            L.append(f"- BID: {p['bid']} | JRC-II: {p['jrc2']} | triage: _{p['triage']}_")
            if p["match_conocido"]:
                L.append(f"- match conocido: `{p['match_conocido']}`")
            L.append(f"- {p['resumen'][:400]}\n")

    bloque("A revisar — núcleo de participación no identificado", revisar)
    bloque("Resto del pool (nuevos: señal débil o fuera de alcance)",
           [p for p in nuevos if not p["triage"].startswith("REVISAR")])
    bloque("Ya identificados (match con conjunto conocido)", ya)
    with open(ruta, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")


def main():
    ap = argparse.ArgumentParser(description="Cruce inventario IA-LATAM (canal A.15).")
    ap.add_argument("--inventario", default=INVENTARIO_DEFAULT,
                    help=f"ruta al xlsx del inventario (def: {INVENTARIO_DEFAULT})")
    ap.add_argument("--hoja", default=HOJA_DEFAULT, help="hoja de sistemas")
    args = ap.parse_args()

    cfg = cargar_config()
    paises = set(cfg["paises"])

    ruta_inv = args.inventario if os.path.isabs(args.inventario) else os.path.join(ROOT, args.inventario)
    if not os.path.exists(ruta_inv):
        print("El inventario externo no está versionado en el repo (archivo grande).")
        print(f"Colócalo en '{INVENTARIO_DEFAULT}' o pásalo con --inventario RUTA.")
        print(f"  (buscado en: {ruta_inv})")
        sys.exit(2)

    registros = leer_inventario(ruta_inv, args.hoja)
    conocidos = cargar_conocidos(cfg)
    total_universo = sum(1 for r in registros if PAIS_ISO.get(nombre_norm(r["pais"])) in paises)
    pool = cruzar(registros, paises, conocidos)

    out_csv = os.path.join(ROOT, "data", "candidatos", "cruce_inventario_ia_latam.csv")
    out_md = os.path.join(ROOT, "data", "gates", "cruce_inventario_ia_latam.md")
    escribir_csv(pool, out_csv)
    escribir_reporte(pool, out_md, len(registros), total_universo)

    nuevos = [p for p in pool if not p["match_conocido"]]
    revisar = [p for p in nuevos if p["triage"].startswith("REVISAR")]
    print(f"Inventario: {len(registros)} sistemas | universo (20 países): {total_universo}")
    print(f"Pool con señal de participación: {len(pool)} "
          f"(ya identificados: {len(pool) - len(nuevos)}; nuevos: {len(nuevos)})")
    print(f"A REVISAR (posible participación no identificada): {len(revisar)}")
    for p in revisar:
        print(f"  - ID {p['id']} [{p['iso']}] {p['nombre'][:60]}")
    print(f"\nSalidas:\n  {out_csv}\n  {out_md}")


if __name__ == "__main__":
    main()
