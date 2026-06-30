#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generar_planilla_decisiones.py
================================
Genera la PLANILLA CONSOLIDADA de decisiones de casos ILIA 2026
(Participación Ciudadana), reconciliando DOS fuentes:

  (a) Planilla final de revisión humana — `Casos_a_Profundizar.xlsx`,
      hoja "Lista Final" (votos Natalia/Nicole/Jose).
  (b) Decisiones del operador en `config.yaml` (escenario A/B,
      exclusiones_firmes) + recodificación 2026 (`recodificacion_2025.csv`,
      campo `rol_IA` contenido/apoyo).

frente a la BBDD baseline 2025 (`BBDD_IA_Participacion_2025.xlsx`:
28 casos activos + 49 excluidos).

----------------------------------------------------------------------------
REGLAS DE RECONCILIACIÓN (documentadas, no salen de memoria)
----------------------------------------------------------------------------
R1. Elegibilidad metodológica manda sobre actividad. Un caso con
    `rol_IA = apoyo` (la IA asiste el proceso pero NO procesa el contenido
    participativo) se EXCLUYE aunque los revisores confirmen que sigue activo:
    su "SI" ratifica actividad, no elegibilidad. Estas exclusiones ya están
    decididas en config.yaml (exclusiones_firmes) y en recodificacion_2025.csv
    ("Exclusión FIRME"). Afecta: CO Descongestión, MX Sufragio seguro,
    PE Sistema de cómputo. Se marca CONFLICTO cuando el voto fue "SI".
R2. Escenario activo = config.yaml › escenarios.scenario_activo (= "A").
    Bajo A se mantienen DO CiudadanIA y CL "Tenemos que hablar de Chile";
    bajo B ambos salen. Se anota la dependencia del escenario.
R3. Baseline reconfirmado con rol_IA = contenido se MANTIENE aunque no figure
    en la lista de revisión (CR dIAra).
R4. El voto de los revisores manda para casos nuevos/dudosos y para el
    duplicado (CL "Participación Ciudadana Proceso Constitucional": se conserva
    una copia, se elimina la otra). La recodificación considera los dos
    homónimos como procesos distintos (autoconvocados vs audiencias) -> anotar.

Salidas:
  data/gates/Planilla_Consolidada_Casos_ILIA2026.xlsx
"""
import os
import re
import csv
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
RECOD_CSV = "data/baseline/recodificacion_2025.csv"
OUT_XLSX = "data/gates/Planilla_Consolidada_Casos_ILIA2026.xlsx"
ESCENARIO_ACTIVO = "A"   # = config.yaml › escenarios.scenario_activo


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
base_idx = {}
for r in base_rows:
    if r[1] is None:
        continue
    base_idx.setdefault((r[0], norm(r[1])), {
        "pais": r[0], "caso": r[1], "anio": r[2], "activo": r[3],
        "desc": r[4], "link": r[21] or r[20],
    })

excl_rows = [r for r in wbb["BBDD Casos Excluidos"].iter_rows(values_only=True)][1:]
excl = []
for r in excl_rows:
    if r[2] is None:
        continue
    excl.append({"motivo": r[0], "pais": r[1], "titulo": r[2],
                 "desc": r[3], "anio": r[4], "link": r[5]})

# recodificación 2026: rol_IA + nota por (pais, norm_caso)
recod = {}
with open(RECOD_CSV, encoding="utf-8") as f:
    for row in csv.DictReader(f):
        recod[(row["pais"], norm(row["caso"]))] = {
            "rol_IA": (row.get("rol_IA") or "").strip(),
            "nota": (row.get("nota") or "").strip(),
        }


def recod_lookup(pais, caso):
    nc = norm(caso)
    for (p, c), d in recod.items():
        if p == pais and (nc[:22] in c or c[:22] in nc):
            return d
    return {"rol_IA": "", "nota": ""}


def base_estado(pais, caso):
    nc = norm(caso)
    for (p, c), d in base_idx.items():
        if p == pais and (nc[:22] in c or c[:22] in nc):
            return d["activo"]
    return None


# --- categorías --------------------------------------------------------------
CAT = {
    1: "1. Baseline que se mantiene",
    2: "2. Baseline eliminado (y razones)",
    3: "3. Eliminado 2025 incorporado (y razones)",
    4: "4. Eliminado 2025 que se mantiene eliminado",
    5: "5. Nuevo caso que se incorpora",
    6: "6. Nuevo caso que NO se incorpora (y razones)",
}

detalle = []


def add(cat, pais, caso, estado25, rol, senal_rev, senal_cfg, conflicto,
        decision, cuenta, razon, comentarios, tipo, desc, enlace):
    detalle.append({
        "cat": cat, "cat_lbl": CAT[cat], "pais": pais, "caso": caso,
        "estado25": estado25 or "", "rol": rol or "—",
        "senal_rev": senal_rev, "senal_cfg": senal_cfg, "conflicto": conflicto,
        "decision": decision, "cuenta": cuenta, "razon": razon or "",
        "comentarios": comentarios or "", "tipo": tipo or "",
        "desc": desc or "", "enlace": enlace or "",
    })


ESCENARIO_CASOS = {("DO", "ciudadania"), ("CL", "tenemos que hablar de chile")}


def es_escenario(pais, caso):
    nc = norm(caso)
    return any(p == pais and k in nc for p, k in ESCENARIO_CASOS)


# === 1/2) Bloque "2. Baseline 2025" de la lista final ========================
for r in fin_rows:
    if not str(r[0]).startswith("2"):
        continue
    pais, caso, tipo = r[1], r[2], r[3]
    estado25 = base_estado(pais, caso)
    si = voto_si(r[7], r[8], r[9])
    votos = fmt_votos(r[7], r[8], r[9])
    rc = recod_lookup(pais, caso)
    rol = rc["rol_IA"]
    senal_rev = "SI (mantener)" if si else "NO (eliminar)"

    # R1 — rol_IA = apoyo => exclusión firme, gane lo que gane el voto
    if rol == "apoyo":
        conflicto = "Sí — revisores 'SI' (solo actividad)" if si else "No"
        nota_det = re.sub(r"^Exclusión FIRME \(recodificación 2026\):\s*", "", rc["nota"])
        razon = (f"rol_IA = apoyo: la IA asiste el proceso pero NO procesa el "
                 f"contenido participativo. Exclusión FIRME ya decidida en "
                 f"config.yaml y recodificación 2026 ({nota_det}).")
        if si:
            razon += (" Los revisores votaron 'SI', pero ese voto ratifica que el "
                      "caso sigue activo, no su elegibilidad metodológica.")
        add(2, pais, caso, estado25, rol, senal_rev,
            "Exclusión FIRME (apoyo)", conflicto, "EXCLUIDO (firme)", "No",
            razon, r[11], tipo, r[4], r[6])
        continue

    # R4 — voto NO => eliminado (duplicado u otra razón del revisor)
    if not si:
        com = str(r[11]).strip() if r[11] else ""
        es_dup = "duplic" in com.lower() or "duplic" in norm(caso)
        razon = (("Duplicado: figura dos veces en el baseline; se conserva una "
                  "copia y se elimina ésta. " if es_dup else "")
                 + (com if com else "Revisores rechazan el caso (mayoría 'NO')."))
        if es_dup:
            razon += (" (La recodificación 2026 anotaba los dos homónimos como "
                      "procesos distintos —autoconvocados vs audiencias—; ratificar.)")
        add(2, pais, caso, estado25, rol, senal_rev, "—", "No",
            "EXCLUIDO (duplicado)" if es_dup else "EXCLUIDO (revisores)", "No",
            razon, r[11], tipo, r[4], r[6])
        continue

    # R2 — caso de escenario A/B
    if es_escenario(pais, caso):
        add(1, pais, caso, estado25, rol, senal_rev,
            f"Escenario {ESCENARIO_ACTIVO} (se mantiene)", "No",
            f"SE MANTIENE (Escenario {ESCENARIO_ACTIVO})", "Sí bajo A · No bajo B",
            ("Revisores ratifican el caso. Depende del escenario: bajo A "
             "(activo) se mantiene; bajo B sale. " + (str(r[11]).strip() if r[11] else "")).strip(),
            r[11], tipo, r[4], r[6])
        continue

    # caso baseline normal mantenido
    es_reverif = "reverif" in str(tipo).lower()
    razon = ("Re-verificación 2026: revisores ratifican actividad y elegibilidad "
             "(rol_IA = contenido)." if es_reverif else
             "Revisores ratifican el caso del baseline 2025; rol_IA = contenido.")
    add(1, pais, caso, estado25, rol, senal_rev, "—", "No",
        "SE MANTIENE", "Sí", razon, r[11], tipo, r[4], r[6])

# === R3) Baseline (Activo) ausente de la lista final =========================
fin_base_norm = [(r[1], norm(r[2])) for r in fin_rows if str(r[0]).startswith("2")]
for (p, c), d in base_idx.items():
    if any(fp == p and (c[:22] in fc or fc[:22] in c) for fp, fc in fin_base_norm):
        continue
    rc = recod_lookup(p, d["caso"])
    rol = rc["rol_IA"]
    if es_escenario(p, d["caso"]):          # DO CiudadanIA
        add(1, p, d["caso"], d["activo"], rol, "— (ausente de lista)",
            f"Escenario {ESCENARIO_ACTIVO} (se mantiene)", "Resuelto (R2)",
            f"SE MANTIENE (Escenario {ESCENARIO_ACTIVO})", "Sí bajo A · No bajo B",
            ("Baseline 2025 (Activo) ausente de la lista de revisión. Reverificación "
             "2026 sin evidencia nueva específica; rol_IA = contenido. Caso del "
             "Escenario A/B: bajo A (config activo) se mantiene; bajo B sale. " + rc["nota"]),
            "", "Baseline 2025", d["desc"], d["link"])
    else:                                    # CR dIAra
        add(1, p, d["caso"], d["activo"], rol, "— (ausente de lista)",
            "Baseline reconfirmado (R3)", "Resuelto (R3)",
            "SE MANTIENE", "Sí",
            ("Baseline 2025 (Activo) ausente de la lista de revisión, pero "
             "reconfirmado por web 2026 (OGP Open Gov Challenge) y con "
             "rol_IA = contenido: se mantiene. " + rc["nota"]),
            "", "Baseline 2025", d["desc"], d["link"])

# === 3/4) Bloque "3. Excluido (revisar)" + resto de excluidos 2025 ===========
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
    if si:
        add(3, pais, caso, "Excluido 2025", "—", "SI (incorporar)", "—", "No",
            "INCORPORADO", "Sí",
            f"Re-revisado y reincorporado por los revisores. Motivo exclusión 2025: {mot}",
            r[11], tipo, r[4], r[6])
    else:
        add(4, pais, caso, "Excluido 2025", "—", "NO (mantener fuera)", "—", "No",
            "SE MANTIENE ELIMINADO", "No",
            (f"Re-revisado en 2026; revisores mantienen la exclusión (mayoría 'NO'). "
             f"Motivo exclusión 2025: {mot}."),
            r[11], tipo, r[4], r[6])

for e in excl:
    nt = norm(e["titulo"])
    if any(rp == e["pais"] and (rk in nt or nt[:15] in rk) for rp, rk in revisados_keys):
        continue
    add(4, e["pais"], e["titulo"], "Excluido 2025", "—", "— (no re-revisado)", "—", "No",
        "SE MANTIENE ELIMINADO (no re-revisado)", "No",
        f"Excluido en 2025 por: {e['motivo']}. No re-revisado en 2026; se mantiene excluido por defecto.",
        "", "Excluido 2025", e["desc"], e["link"])

# === 5/6) Bloque "1. NUEVOS / dudosos" =======================================
for r in fin_rows:
    if not str(r[0]).startswith("1"):
        continue
    pais, caso, tipo = r[1], r[2], r[3]
    si = voto_si(r[7], r[8], r[9])
    estado25 = "Nuevo 2026" + (" (dudoso)" if "dudoso" in str(tipo).lower() else "")
    if si:
        add(5, pais, caso, estado25, "—", "SI (incorporar)", "—", "No",
            "INCORPORADO", "Sí",
            ("Caso nuevo identificado en 2026; revisores lo aprueban. "
             + (str(r[11]).strip() if r[11] else "")).strip(),
            r[11], tipo, r[4], r[6])
    else:
        razon = str(r[11]).strip() if r[11] else "Revisores rechazan el caso nuevo (mayoría 'NO')."
        add(6, pais, caso, estado25, "—", "NO (no incorporar)", "—", "No",
            "NO INCORPORADO", "No", razon, r[11], tipo, r[4], r[6])

# ordenar por categoría
detalle.sort(key=lambda d: (d["cat"], d["pais"], norm(d["caso"])))

# === conteos =================================================================
from collections import Counter
cnt = Counter(d["cat"] for d in detalle)
elegibles_A = sum(1 for d in detalle if d["decision"].startswith("SE MANTIENE")
                  and "ELIMINADO" not in d["decision"]) \
              + sum(1 for d in detalle if d["decision"] == "INCORPORADO" and d["cat"] == 5)
n_baseline_in = sum(1 for d in detalle if d["cat"] == 1)
n_nuevos_in = sum(1 for d in detalle if d["cat"] == 5)
n_escenario = sum(1 for d in detalle if "No bajo B" in d["cuenta"])
total_A = n_baseline_in + n_nuevos_in
total_B = total_A - n_escenario

# =============================================================================
# ESCRITURA DEL XLSX
# =============================================================================
wb = openpyxl.Workbook()
HDR_FILL = PatternFill("solid", fgColor="1F4E78")
HDR_FONT = Font(bold=True, color="FFFFFF", size=11)
TITLE_FONT = Font(bold=True, size=14, color="1F4E78")
WRAP = Alignment(wrap_text=True, vertical="top")
CENTER = Alignment(horizontal="center", vertical="center", wrap_text=True)
THIN = Side(style="thin", color="BFBFBF")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
CAT_FILL = {1: "E2EFDA", 2: "FCE4D6", 3: "DDEBF7", 4: "F2F2F2", 5: "E2EFDA", 6: "FCE4D6"}
DEC_COLOR = {"SE MANTIENE": "548235", "INCORPORADO": "548235",
             "EXCLUIDO": "C00000", "NO INCORPORADO": "C00000"}


def dec_color(dec):
    for k, v in DEC_COLOR.items():
        if dec.startswith(k):
            return v
    return None


# --- Hoja RESUMEN ------------------------------------------------------------
ws = wb.active
ws.title = "Resumen"
ws["A1"] = "Planilla consolidada de casos ILIA 2026 — Participación Ciudadana"
ws["A1"].font = TITLE_FONT
ws["A2"] = ("Reconciliación: revisión humana (Natalia/Nicole/Jose) ↔ config.yaml "
            "(escenario A/B, exclusiones firmes) + recodificación 2026 (rol_IA), vs. baseline 2025")
ws["A2"].font = Font(italic=True, size=10, color="595959")

ws["A4"] = "Conjunto elegible 2026 (lo que cuenta en el indicador)"
ws["A4"].font = Font(bold=True, size=12, color="1F4E78")
ws["A5"] = f"Escenario A (activo): {total_A} casos  =  {n_baseline_in} baseline + {n_nuevos_in} nuevos"
ws["A6"] = f"Escenario B: {total_B} casos  (salen DO CiudadanIA y CL «Tenemos que hablar de Chile»)"
ws["A5"].font = Font(bold=True, size=11)
ws["A6"].font = Font(size=11)

ws["A8"] = "Conteo por categoría"
ws["A8"].font = Font(bold=True, size=12)
for j, h in enumerate(["Categoría", "N° de casos"], 1):
    c = ws.cell(row=9, column=j, value=h)
    c.fill = HDR_FILL; c.font = HDR_FONT; c.border = BORDER; c.alignment = CENTER
rowi = 10
for k in [1, 2, 3, 4, 5, 6]:
    a = ws.cell(row=rowi, column=1, value=CAT[k])
    a.border = BORDER; a.alignment = WRAP
    a.fill = PatternFill("solid", fgColor=CAT_FILL[k])
    b = ws.cell(row=rowi, column=2, value=cnt.get(k, 0))
    b.border = BORDER; b.alignment = CENTER
    rowi += 1
ws.cell(row=rowi, column=1, value="TOTAL filas de detalle").font = Font(bold=True)
ws.cell(row=rowi, column=2, value=len(detalle)).font = Font(bold=True)
ws.cell(row=rowi, column=2).alignment = CENTER

notas = [
    "",
    "Reglas de reconciliación aplicadas",
    "R1 · rol_IA = apoyo ⇒ EXCLUIDO firme. La IA asiste el proceso pero no procesa el contenido participativo; la exclusión ya está decidida en config.yaml (exclusiones_firmes) y en recodificación 2026. Afecta a CO Descongestión, MX Sufragio seguro y PE Sistema de cómputo. El 'SI' de los revisores en Descongestión y PE ratifica ACTIVIDAD, no elegibilidad ⇒ se marcan como conflicto resuelto a favor de la metodología (ratificar).",
    "R2 · Escenario activo = A (config.yaml). DO CiudadanIA y CL «Tenemos que hablar de Chile» se mantienen bajo A y salen bajo B (columna 'Cuenta en indicador').",
    "R3 · Baseline reconfirmado con rol_IA = contenido se mantiene aunque no esté en la lista de revisión ⇒ CR dIAra (reconfirmado por OGP 2025).",
    "R4 · El voto de los revisores manda en casos nuevos/dudosos y en el duplicado (CL «Participación Ciudadana Proceso Constitucional»: se conserva una copia y se elimina la otra).",
    "",
    "Cómo leer la decisión consolidada",
    "• INCLUIDO / SE MANTIENE / INCORPORADO ⇒ el caso es elegible y cuenta en 2026 (ver 'Cuenta en indicador', sujeto al escenario).",
    "• EXCLUIDO (firme/duplicado/revisores) y SE MANTIENE ELIMINADO / NO INCORPORADO ⇒ fuera del conjunto 2026.",
    "• 'Cuenta en indicador' = Sí · No · «Sí bajo A · No bajo B» (casos de escenario).",
    "",
    "Puntos que aún requieren ratificación del operador",
    "• Conflicto R1: confirmar que CO Descongestión y PE Sistema de cómputo se excluyen pese al 'SI' de actividad de los revisores (criterio rol_IA = apoyo).",
    "• Escenario A/B: la base usa A. Si se decide B, restar DO CiudadanIA y CL «Tenemos que hablar de Chile».",
    "• Duplicado CL: la recodificación consideró los dos homónimos como procesos distintos (autoconvocados vs audiencias); confirmar que es duplicado y no dos casos.",
    "• Categoría 3 vacía: ningún excluido de 2025 fue reincorporado (los 5 re-revisados siguen fuera; 44 no se re-revisaron).",
]
for txt in notas:
    rowi += 1
    c = ws.cell(row=rowi, column=1, value=txt)
    if txt in ("Reglas de reconciliación aplicadas", "Cómo leer la decisión consolidada",
               "Puntos que aún requieren ratificación del operador"):
        c.font = Font(bold=True, size=12, color="1F4E78")
    else:
        c.font = Font(size=10)
    c.alignment = WRAP
ws.column_dimensions["A"].width = 125
ws.column_dimensions["B"].width = 14
ws.freeze_panes = "A9"

# --- Hoja DETALLE CONSOLIDADO ------------------------------------------------
wsd = wb.create_sheet("Detalle consolidado")
cols = [
    ("Categoría", 32), ("País", 6), ("Caso", 44), ("Estado 2025", 13),
    ("rol_IA", 10), ("Señal revisores", 16), ("Señal config/recod.", 20),
    ("¿Conflicto?", 18), ("DECISIÓN CONSOLIDADA 2026", 24),
    ("Cuenta en indicador", 16), ("Razón consolidada", 62),
    ("Comentarios revisores (verbatim)", 40), ("Qué es y cómo usa IA", 46), ("Enlace", 32),
]
for j, (h, w) in enumerate(cols, 1):
    c = wsd.cell(row=1, column=j, value=h)
    c.fill = HDR_FILL; c.font = HDR_FONT; c.border = BORDER; c.alignment = CENTER
    wsd.column_dimensions[get_column_letter(j)].width = w
for i, d in enumerate(detalle, start=2):
    vals = [d["cat_lbl"], d["pais"], d["caso"], d["estado25"], d["rol"],
            d["senal_rev"], d["senal_cfg"], d["conflicto"], d["decision"],
            d["cuenta"], d["razon"], d["comentarios"], d["desc"], d["enlace"]]
    for j, v in enumerate(vals, 1):
        c = wsd.cell(row=i, column=j, value=v)
        c.border = BORDER
        c.alignment = CENTER if j in (2, 4, 5, 6, 7, 8, 10) else WRAP
    wsd.cell(row=i, column=1).fill = PatternFill("solid", fgColor=CAT_FILL[d["cat"]])
    col = dec_color(d["decision"])
    if col:
        wsd.cell(row=i, column=9).font = Font(bold=True, color=col)
    if d["conflicto"].startswith("Sí"):
        wsd.cell(row=i, column=8).fill = PatternFill("solid", fgColor="FFE699")
        wsd.cell(row=i, column=8).font = Font(bold=True, color="9C5700")
wsd.freeze_panes = "C2"
wsd.auto_filter.ref = f"A1:{get_column_letter(len(cols))}{len(detalle)+1}"

# --- Hoja EXCLUIDOS 2025 (universo) ------------------------------------------
wse = wb.create_sheet("Excluidos 2025 (universo)")
ecols = [("País", 8), ("Título", 48), ("Motivo exclusión 2025", 46),
         ("Año", 8), ("¿Re-revisado 2026?", 18), ("Decisión 2026", 32), ("Link", 36)]
for j, (h, w) in enumerate(ecols, 1):
    c = wse.cell(row=1, column=j, value=h)
    c.fill = HDR_FILL; c.font = HDR_FONT; c.border = BORDER; c.alignment = CENTER
    wse.column_dimensions[get_column_letter(j)].width = w
ei = 2
for e in excl:
    nt = norm(e["titulo"])
    rev = any(rp == e["pais"] and (rk in nt or nt[:15] in rk) for rp, rk in revisados_keys)
    valores = [e["pais"], e["titulo"], e["motivo"], e["anio"], "Sí" if rev else "No",
               ("Se mantiene eliminado (revisores 'NO')" if rev
                else "Se mantiene eliminado (no re-revisado)"), e["link"]]
    for j, v in enumerate(valores, 1):
        cc = wse.cell(row=ei, column=j, value=v)
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
print(f"Conjunto elegible 2026: A={total_A} ({n_baseline_in} baseline + {n_nuevos_in} nuevos) · B={total_B}")
for k in [1, 2, 3, 4, 5, 6]:
    print(f"  {CAT[k]}: {cnt.get(k,0)}")
print(f"  TOTAL detalle: {len(detalle)}")
