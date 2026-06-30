#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generar_planilla_decisiones.py
================================
Compara la planilla FINAL de casos ("Casos a Profundizar", revisión humana
Natalia/Nicole/Jose) contra la BBDD baseline 2025 y produce una planilla que
detalla QUÉ SE HIZO CON CADA CASO, en las seis categorías pedidas:

  1. Baseline que se mantuvo
  2. Baseline eliminado (y razones)
  3. Eliminados (2025) incorporados (y razones)
  4. Eliminados que se mantienen eliminados de 2025
  5. Nuevos casos identificados que se incorporan
  6. Nuevos casos identificados que no se incorporan (y razones)

La clasificación se deriva del voto de los revisores (col. Natalia/Nicole/Jose)
en la planilla final: mayoría 'SI' => se mantiene/incorpora; 'NO' =>
elimina/no incorpora. Ningún juicio sale de memoria: razones = comentarios
verbatim de los revisores + 'A verificar' + motivo de exclusión 2025.

Salida: data/gates/Analisis_Casos_2026_vs_2025.xlsx
"""
import os
import re
import unicodedata
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# --- rutas -------------------------------------------------------------------
FINAL_XLSX = os.environ.get(
    "FINAL_XLSX",
    "/root/.claude/uploads/f142e11e-c75e-5a60-95ab-939ca0282af8/4e3436df-Casos_a_Profundizar.xlsx",
)
BASE_XLSX = "data/baseline/BBDD_IA_Participacion_2025.xlsx"
OUT_XLSX = "data/gates/Analisis_Casos_2026_vs_2025.xlsx"


def norm(s):
    if s is None:
        return ""
    s = str(s).strip().lower()
    s = "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def voto_si(nat, nic, jos):
    v = [str(x).strip().upper() for x in (nat, nic, jos)]
    return v.count("SI") >= 2


def fmt_votos(nat, nic, jos):
    f = lambda x: (str(x).strip().upper() if x not in (None, "") else "—")
    return f"N:{f(nat)} · Nic:{f(nic)} · J:{f(jos)}"


# --- carga -------------------------------------------------------------------
wbf = openpyxl.load_workbook(FINAL_XLSX, data_only=True)
fin_rows = [r for r in wbf["Lista Final"].iter_rows(values_only=True)][1:]
fin_rows = [r for r in fin_rows if any(c is not None for c in r)]
# cols: 0 Bloque 1 País 2 Caso 3 Tipo 4 Qué es 5 A verificar 6 Enlace
#       7 Natalia 8 Nicole 9 Jose 10 ¿Coinciden? 11 Comentarios

wbb = openpyxl.load_workbook(BASE_XLSX, data_only=True)
base_rows = [r for r in wbb["BBDD Casos"].iter_rows(values_only=True)][1:]
base_idx = {}  # (pais, norm_caso) -> dict
for r in base_rows:
    if r[1] is None:
        continue
    base_idx.setdefault((r[0], norm(r[1])), {
        "pais": r[0], "caso": r[1], "anio": r[2], "activo": r[3],
        "desc": r[4], "link": r[21] or r[20],
    })

excl_rows = [r for r in wbb["BBDD Casos Excluidos"].iter_rows(values_only=True)][1:]
excl = []  # motivo, pais, titulo, desc, anio, link
for r in excl_rows:
    if r[2] is None:
        continue
    excl.append({"motivo": r[0], "pais": r[1], "titulo": r[2],
                 "desc": r[3], "anio": r[4], "link": r[5]})


def base_estado(pais, caso):
    """Estado 2025 (Activo/Cerrado/Proximamente) del baseline, por (pais, caso)."""
    nc = norm(caso)
    for (p, c), d in base_idx.items():
        if p == pais and (nc[:22] in c or c[:22] in nc):
            return d["activo"]
    return None


# --- construir filas de detalle ---------------------------------------------
# cada fila: dict con campos para la planilla de salida
detalle = []


def add(cat, cat_lbl, pais, caso, estado25, bloque, tipo, decision,
        votos, coin, razon, comentarios, desc, enlace):
    detalle.append({
        "cat": cat, "cat_lbl": cat_lbl, "pais": pais, "caso": caso,
        "estado25": estado25 or "", "bloque": bloque or "", "tipo": tipo or "",
        "decision": decision, "votos": votos, "coin": coin or "",
        "razon": razon or "", "comentarios": comentarios or "",
        "desc": desc or "", "enlace": enlace or "",
    })


CAT = {
    1: "1. Baseline que se mantuvo",
    2: "2. Baseline eliminado (y razones)",
    3: "3. Eliminado 2025 incorporado (y razones)",
    4: "4. Eliminado 2025 que se mantiene eliminado",
    5: "5. Nuevo caso que se incorpora",
    6: "6. Nuevo caso que NO se incorpora (y razones)",
    0: "0. Baseline ausente de la lista final (a confirmar)",
}

# 1) y 2) Bloque "2. Baseline 2025" de la lista final
for r in fin_rows:
    if not str(r[0]).startswith("2"):
        continue
    pais, caso, tipo = r[1], r[2], r[3]
    estado25 = base_estado(pais, caso)
    si = voto_si(r[7], r[8], r[9])
    votos = fmt_votos(r[7], r[8], r[9])
    es_reverif = "reverif" in str(tipo).lower()
    if si:
        razon = ("Re-verificación 2026: revisores ratifican que sigue activo y elegible."
                 if es_reverif else
                 "Revisores ratifican el caso del baseline 2025; se mantiene en 2026.")
        add(1, CAT[1], pais, caso, estado25, r[0], tipo, "SE MANTIENE",
            votos, r[10], razon, r[11], r[4], r[6])
    else:
        # razón de eliminación: comentarios verbatim si existen
        razon = str(r[11]).strip() if r[11] else "Revisores rechazan el caso (mayoría 'NO')."
        add(2, CAT[2], pais, caso, estado25, r[0], tipo, "ELIMINADO",
            votos, r[10], razon, r[11], r[4], r[6])

# 0) Baseline 2025 (Activo) ausente de la lista final -> a confirmar
fin_base_norm = [(r[1], norm(r[2])) for r in fin_rows if str(r[0]).startswith("2")]
flag_notas = {
    ("CR", "diara"): ("Caso baseline 2025 (Activo). Reconfirmado por web 2026 "
                      "(OGP Open Gov Challenge): visión computacional procesa alertas "
                      "de inspectores ciudadanos sobre obras públicas. La nota interna "
                      "lo califica como 'que sí entra'. NO fue incluido en la lista de "
                      "revisión: confirmar si se mantiene (probable) o se elimina."),
    ("DO", "ciudadania"): ("Caso baseline 2025 (Activo). Reverificación 2026 sin evidencia "
                           "nueva específica de la plataforma 2025-2026 (OGTIC/GENIA/MINPRE "
                           "activos en agenda de IA). Es el caso del Escenario A/B "
                           "(config.yaml: A lo mantiene, B lo retira). NO aparece en la "
                           "lista de revisión: requiere decisión explícita."),
}
for (p, c), d in base_idx.items():
    if str(d["activo"]).strip().lower() not in ("activo", "proximamente", "cerrado"):
        pass
    found = any(fp == p and (c[:22] in fc or fc[:22] in c) for fp, fc in fin_base_norm)
    if not found:
        key = (p, c[:9])
        nota = None
        for (kp, kc), txt in flag_notas.items():
            if kp == p and kc in c:
                nota = txt
        add(0, CAT[0], p, d["caso"], d["activo"], "(ausente de lista final)", "Baseline 2025",
            "A CONFIRMAR", "—", "—", nota or "Baseline 2025 ausente de la lista de revisión; confirmar.",
            "", d["desc"], d["link"])

# 4) Bloque "3. Excluido (revisar)" de la lista final -> se mantienen eliminados
excl_idx = {(e["pais"], norm(e["titulo"])): e for e in excl}


def motivo_2025(pais, titulo):
    nt = norm(titulo)
    for (p, t), e in excl_idx.items():
        if p == pais and (nt[:15] in t or t[:15] in nt):
            return e["motivo"]
    return None


revisados_keys = set()
for r in fin_rows:
    if not str(r[0]).startswith("3"):
        continue
    pais, caso, tipo = r[1], r[2], r[3]
    mot = motivo_2025(pais, caso)
    revisados_keys.add((pais, norm(caso)[:15]))
    si = voto_si(r[7], r[8], r[9])
    votos = fmt_votos(r[7], r[8], r[9])
    if si:  # (no ocurre en estos datos, pero se contempla)
        add(3, CAT[3], pais, caso, "Excluido 2025", r[0], tipo, "INCORPORADO",
            votos, r[10], f"Re-revisado y reincorporado. Motivo exclusión 2025: {mot}", r[11], r[4], r[6])
    else:
        razon = (f"Re-revisado en 2026; revisores mantienen la exclusión (mayoría 'NO'). "
                 f"Motivo exclusión 2025: {mot}.")
        add(4, CAT[4], pais, caso, "Excluido 2025", r[0], tipo, "SE MANTIENE ELIMINADO",
            votos, r[10], razon, r[11], r[4], r[6])

# 4-bis) resto de excluidos 2025 NO re-revisados -> se mantienen por defecto
for e in excl:
    k = (e["pais"], norm(e["titulo"])[:15])
    if any(rp == e["pais"] and (rk in norm(e["titulo"]) or norm(e["titulo"])[:15] in rk)
           for rp, rk in revisados_keys):
        continue
    add(4, CAT[4], e["pais"], e["titulo"], "Excluido 2025", "(no re-revisado)", "Excluido 2025",
        "SE MANTIENE ELIMINADO (no re-revisado)", "—", "—",
        f"Excluido en 2025 por: {e['motivo']}. No fue re-revisado en 2026; se mantiene excluido por defecto.",
        "", e["desc"], e["link"])

# 5) y 6) Bloque "1. NUEVOS / dudosos"
for r in fin_rows:
    if not str(r[0]).startswith("1"):
        continue
    pais, caso, tipo = r[1], r[2], r[3]
    si = voto_si(r[7], r[8], r[9])
    votos = fmt_votos(r[7], r[8], r[9])
    estado25 = "Nuevo 2026" + (" (dudoso)" if "dudoso" in str(tipo).lower() else "")
    if si:
        razon = ("Caso nuevo identificado en 2026; revisores lo aprueban para incorporar. "
                 + (str(r[11]).strip() if r[11] else ""))
        add(5, CAT[5], pais, caso, estado25, r[0], tipo, "INCORPORADO",
            votos, r[10], razon.strip(), r[11], r[4], r[6])
    else:
        razon = str(r[11]).strip() if r[11] else "Revisores rechazan el caso nuevo (mayoría 'NO')."
        add(6, CAT[6], pais, caso, estado25, r[0], tipo, "NO INCORPORADO",
            votos, r[10], razon, r[11], r[4], r[6])

# ordenar por categoría (0 al final, junto a su bloque conceptual = 2)
orden = {1: 1, 2: 2, 0: 2.5, 3: 3, 4: 4, 5: 5, 6: 6}
detalle.sort(key=lambda d: (orden[d["cat"]], d["pais"], norm(d["caso"])))

# =============================================================================
# ESCRITURA DEL XLSX
# =============================================================================
wb = openpyxl.Workbook()

# estilos
HDR_FILL = PatternFill("solid", fgColor="1F4E78")
HDR_FONT = Font(bold=True, color="FFFFFF", size=11)
TITLE_FONT = Font(bold=True, size=14, color="1F4E78")
WRAP = Alignment(wrap_text=True, vertical="top")
CENTER = Alignment(horizontal="center", vertical="center", wrap_text=True)
THIN = Side(style="thin", color="BFBFBF")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
CAT_FILL = {
    1: "E2EFDA", 2: "FCE4D6", 0: "FFF2CC", 3: "DDEBF7",
    4: "F2F2F2", 5: "E2EFDA", 6: "FCE4D6",
}
DEC_FONT = {
    "SE MANTIENE": "548235", "ELIMINADO": "C00000", "A CONFIRMAR": "BF8F00",
    "INCORPORADO": "548235", "NO INCORPORADO": "C00000",
}

# --- Hoja RESUMEN ------------------------------------------------------------
ws = wb.active
ws.title = "Resumen"
ws["A1"] = "Análisis de casos ILIA 2026 — Participación Ciudadana"
ws["A1"].font = TITLE_FONT
ws["A2"] = "Qué se hizo con cada caso: planilla final (revisión Natalia/Nicole/Jose) vs. baseline 2025"
ws["A2"].font = Font(italic=True, size=10, color="595959")

from collections import Counter
cnt = Counter(d["cat"] for d in detalle)
ws["A4"] = "Conteo por categoría"
ws["A4"].font = Font(bold=True, size=12)
hdr = ["Categoría", "N° de casos"]
ws.append([])
for j, h in enumerate(hdr, 1):
    c = ws.cell(row=5, column=j, value=h)
    c.fill = HDR_FILL; c.font = HDR_FONT; c.border = BORDER; c.alignment = CENTER
rowi = 6
for k in [1, 2, 0, 3, 4, 5, 6]:
    ws.cell(row=rowi, column=1, value=CAT[k]).border = BORDER
    ws.cell(row=rowi, column=1).fill = PatternFill("solid", fgColor=CAT_FILL[k])
    ws.cell(row=rowi, column=1).alignment = WRAP
    ws.cell(row=rowi, column=2, value=cnt.get(k, 0)).border = BORDER
    ws.cell(row=rowi, column=2).alignment = CENTER
    rowi += 1
ws.cell(row=rowi, column=1, value="TOTAL filas de detalle").font = Font(bold=True)
ws.cell(row=rowi, column=2, value=len(detalle)).font = Font(bold=True)
ws.cell(row=rowi, column=2).alignment = CENTER

notas = [
    "",
    "Metodología",
    "• Fuente de la decisión: voto de los revisores (Natalia/Nicole/Jose) en la planilla final. Mayoría 'SI' = se mantiene/incorpora; 'NO' = elimina/no incorpora. En todos los casos los tres coinciden ('DE ACUERDO').",
    "• Las 'razones' son verbatim de los revisores (col. Comentarios) + 'A verificar' + motivo de exclusión 2025. No se infiere nada que no esté en las planillas.",
    "• Baseline 2025 = hoja 'BBDD Casos' (28 casos). Excluidos 2025 = hoja 'BBDD Casos Excluidos' (49 casos).",
    "",
    "Observaciones que requieren decisión del operador (no se resuelven aquí)",
    "• Categoría 0: CR dIAra y DO CiudadanIA son baseline 2025 (Activo) que NO aparecen en la lista de revisión. dIAra está reconfirmado por web ('que sí entra'); CiudadanIA es el caso del Escenario A/B (config.yaml: A lo mantiene, B lo retira). Confirmar su destino explícitamente.",
    "• Discrepancia con config.yaml 'exclusiones_firmes': el config marca CO 'Descongestión de solicitudes…Ingreso Solidario' y PE 'Sistema de cómputo…Elecciones 2026' como exclusiones firmes del cálculo 2026, pero los revisores los votaron 'SI' (se mantienen) en la lista final. MX 'Sufragio seguro' coincide (fuera en ambos). Reconciliar lista final vs. config antes de calcular.",
    "• Duplicado: CL 'Participación Ciudadana Proceso Constitucional' aparece dos veces en el baseline 2025; en 2026 se mantiene una copia y se elimina la otra (categoría 2).",
    "• Categoría 3 vacía: ningún excluido de 2025 fue reincorporado. Los 5 excluidos re-revisados se mantienen fuera; los 44 restantes no se re-revisaron.",
    "• 'Eliminar' aquí significa retirar del conjunto de casos elegibles 2026; varios casos siguen siendo reales pero no cumplen criterios (p. ej. atención ciudadana, sin IA sobre el contenido, solo investigación/anuncio).",
]
for txt in notas:
    rowi += 1
    c = ws.cell(row=rowi, column=1, value=txt)
    if txt in ("Metodología", "Observaciones que requieren decisión del operador (no se resuelven aquí)"):
        c.font = Font(bold=True, size=12, color="1F4E78")
    else:
        c.font = Font(size=10)
    c.alignment = WRAP
ws.column_dimensions["A"].width = 120
ws.column_dimensions["B"].width = 14
ws.freeze_panes = "A5"

# --- Hoja DETALLE ------------------------------------------------------------
wsd = wb.create_sheet("Detalle por caso")
cols = [
    ("Categoría", 34), ("País", 6), ("Caso", 46), ("Estado 2025", 14),
    ("Decisión 2026", 16), ("Votos (revisores)", 20), ("Razón / fundamento", 60),
    ("Comentarios revisores (verbatim)", 46), ("Tipo (lista final)", 20),
    ("Qué es y cómo usa IA", 50), ("Enlace", 34),
]
for j, (h, w) in enumerate(cols, 1):
    c = wsd.cell(row=1, column=j, value=h)
    c.fill = HDR_FILL; c.font = HDR_FONT; c.border = BORDER; c.alignment = CENTER
    wsd.column_dimensions[get_column_letter(j)].width = w
for i, d in enumerate(detalle, start=2):
    vals = [d["cat_lbl"], d["pais"], d["caso"], d["estado25"], d["decision"],
            d["votos"], d["razon"], d["comentarios"], d["tipo"], d["desc"], d["enlace"]]
    for j, v in enumerate(vals, 1):
        c = wsd.cell(row=i, column=j, value=v)
        c.border = BORDER
        c.alignment = CENTER if j in (2, 4, 5, 6) else WRAP
    wsd.cell(row=i, column=1).fill = PatternFill("solid", fgColor=CAT_FILL[d["cat"]])
    dec = wsd.cell(row=i, column=5)
    base_dec = d["decision"].split(" (")[0]
    if base_dec in DEC_FONT:
        dec.font = Font(bold=True, color=DEC_FONT[base_dec])
wsd.freeze_panes = "A2"
wsd.auto_filter.ref = f"A1:{get_column_letter(len(cols))}{len(detalle)+1}"

# --- Hoja EXCLUIDOS 2025 (universo completo) ---------------------------------
wse = wb.create_sheet("Excluidos 2025 (universo)")
ecols = [("País", 8), ("Título", 48), ("Motivo exclusión 2025", 46),
         ("Año", 8), ("¿Re-revisado 2026?", 18), ("Decisión 2026", 30), ("Link", 36)]
for j, (h, w) in enumerate(ecols, 1):
    c = wse.cell(row=1, column=j, value=h)
    c.fill = HDR_FILL; c.font = HDR_FONT; c.border = BORDER; c.alignment = CENTER
    wse.column_dimensions[get_column_letter(j)].width = w
ei = 2
for e in excl:
    nt = norm(e["titulo"])
    rev = any(rp == e["pais"] and (rk in nt or nt[:15] in rk) for rp, rk in revisados_keys)
    wse.cell(row=ei, column=1, value=e["pais"])
    wse.cell(row=ei, column=2, value=e["titulo"])
    wse.cell(row=ei, column=3, value=e["motivo"])
    wse.cell(row=ei, column=4, value=e["anio"])
    wse.cell(row=ei, column=5, value="Sí" if rev else "No")
    wse.cell(row=ei, column=6, value=("Se mantiene eliminado (revisores 'NO')" if rev
                                      else "Se mantiene eliminado (no re-revisado)"))
    wse.cell(row=ei, column=7, value=e["link"])
    for j in range(1, 8):
        cc = wse.cell(row=ei, column=j)
        cc.border = BORDER
        cc.alignment = CENTER if j in (1, 4, 5) else WRAP
        if rev:
            cc.fill = PatternFill("solid", fgColor="FFF2CC")
    ei += 1
wse.freeze_panes = "A2"
wse.auto_filter.ref = f"A1:G{ei-1}"

os.makedirs(os.path.dirname(OUT_XLSX), exist_ok=True)
wb.save(OUT_XLSX)
print(f"OK -> {OUT_XLSX}")
print("Conteo por categoría:")
for k in [1, 2, 0, 3, 4, 5, 6]:
    print(f"  {CAT[k]}: {cnt.get(k,0)}")
print(f"  TOTAL detalle: {len(detalle)}")
