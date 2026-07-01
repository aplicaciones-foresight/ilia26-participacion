#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generar_planilla_para_analisis.py
==================================
Deriva una PLANILLA DE CASOS limpia y autocontenida para entregar al agente que
analiza los casos en detalle (Fase 2), de modo que verifique CONSISTENCIA con
las decisiones ya tomadas (inclusión/exclusión, rol_IA verificado, evidencia,
URL funcional).

Fuentes: data/gates/Planilla_Consolidada_Casos_ILIA2026.xlsx (hoja 'Detalle
consolidado', con validación + verificación profunda) y
data/gates/busqueda_ampliada_2026_resultados.json (rescates + descubrimiento).

Salida: data/gates/Planilla_Casos_para_Analisis_ILIA2026.xlsx
  - Hoja 'Casos (analizar)'  : INCLUIDOS + PENDIENTE + RESCATABLES + CANDIDATOS
  - Hoja 'Excluidos (razón)' : casos fuera con su razón (para chequeo cruzado)
  - Hoja 'Leyenda'           : definiciones, conteos y escenario
"""
import re
import json
import unicodedata
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

SRC = "data/gates/Planilla_Consolidada_Casos_ILIA2026.xlsx"
AMPL = "data/gates/busqueda_ampliada_2026_resultados.json"
OUT = "data/gates/Planilla_Casos_para_Analisis_ILIA2026.xlsx"


def norm_ascii(s):
    s = str(s or "")
    s = "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")
    return s


def slug(pais, caso):
    base = norm_ascii(caso).lower()
    base = re.sub(r"[^a-z0-9]+", "-", base).strip("-")
    return f"{pais}-{base[:40]}".strip("-")


wb = openpyxl.load_workbook(SRC, data_only=True)
wsd = wb["Detalle consolidado"]
H = [c.value for c in wsd[1]]
ci = {h: i for i, h in enumerate(H) if h}

def cell(row, name):
    return row[ci[name]] if name in ci else None

incluidos, pendientes, excluidos = [], [], []
for row in wsd.iter_rows(min_row=2, values_only=True):
    cat = str(cell(row, "Categoría") or "")
    pais = cell(row, "País"); caso = cell(row, "Caso")
    if not caso:
        continue
    _clean = lambda x: ("" if str(x or "").strip() in ("—", "-", "") else str(x).strip())
    rol_v = _clean(cell(row, "rol_IA verificado (prof.)"))
    rol_b = _clean(cell(row, "rol_IA"))
    decision = str(cell(row, "DECISIÓN CONSOLIDADA 2026") or "")
    origen = ("Baseline 2025" if cat.startswith("1.") or cat.startswith("2.")
              else "Nuevo 2026" if cat.startswith("5.") or cat.startswith("6.")
              else "Excluido 2025" if cat.startswith("3.") or cat.startswith("4.")
              else "")
    url = cell(row, "URL funcional (verificada)") or cell(row, "Enlace")
    desc = cell(row, "Qué es y cómo usa IA")
    evid = cell(row, "Cita verbatim (fuente primaria)") or cell(row, "Evidencia verificación")
    fuente_cita = cell(row, "Fuente de la cita") or ""
    conf = cell(row, "Confianza") or ""
    cuenta = cell(row, "Cuenta en indicador") or ""
    usa_ia_web = _clean(cell(row, "Usa IA en participación"))
    rol_final = rol_v or rol_b or usa_ia_web or ""
    rol_src = ("verificado" if rol_v else "borrador (recod)" if rol_b
               else "1ª pasada web" if usa_ia_web else "")
    rec = {
        "id": slug(pais, caso), "pais": pais, "caso": caso, "origen": origen,
        "cuenta": cuenta, "rol_IA": rol_final,
        "rol_verificado": rol_src,
        "confianza": conf, "desc": desc, "url": url, "evidencia": evid,
        "fuente": fuente_cita, "decision": decision,
        "razon": cell(row, "Razón consolidada") or "",
    }
    es_elegible = cat.startswith("1.") or cat.startswith("5.")
    if es_elegible and str(rol_v).lower() in ("apoyo", "sin_ia"):
        rec["estado"] = "EXCLUIDO (verif. profunda)"
        excluidos.append(rec)
    elif es_elegible and not rol_v and ("hablar de Colombia" in str(caso)):  # CO TQH Colombia: pendiente
        rec["estado"] = "PENDIENTE (por verificar)"
        pendientes.append(rec)
    elif es_elegible:
        rec["estado"] = "INCLUIDO"
        incluidos.append(rec)
    else:
        rec["estado"] = ("EXCLUIDO (baseline)" if cat.startswith("2.")
                         else "EXCLUIDO (nuevo no incorp.)" if cat.startswith("6.")
                         else "EXCLUIDO 2025")
        excluidos.append(rec)

# rescates + candidatos desde la búsqueda ampliada
ampl = json.load(open(AMPL, encoding="utf-8"))
rescatables, candidatos = [], []
for x in ampl.get("rescate_ronda1", []):
    if x.get("veredicto") == "INCLUIBLE":
        rescatables.append({
            "id": slug(x["pais"], x["caso"]), "pais": x["pais"], "caso": x["caso"],
            "origen": "Rescate (excluido 2025)", "cuenta": "Por confirmar",
            "rol_IA": x.get("usa_IA_contenido", ""), "rol_verificado": "por confirmar",
            "confianza": "", "desc": x.get("evidencia", ""), "url": x.get("fuente_url", ""),
            "evidencia": x.get("cita_verbatim", ""), "fuente": x.get("fuente_url", ""),
            "estado": "RESCATABLE (confirmar)", "decision": x.get("veredicto", ""),
            "razon": x.get("que_buscar_manual", ""),
        })
for x in ampl.get("descubrimiento", []):
    candidatos.append({
        "id": slug(x["pais"], str(x["caso"])), "pais": x["pais"], "caso": x["caso"],
        "origen": "Descubrimiento 2026", "cuenta": "Por confirmar",
        "rol_IA": x.get("usa_IA_contenido", ""), "rol_verificado": "por confirmar",
        "confianza": x.get("confianza", ""), "desc": x.get("descripcion", ""),
        "url": x.get("fuente_url", ""), "evidencia": "", "fuente": x.get("fuente_url", ""),
        "estado": "CANDIDATO (por verificar)", "decision": "",
        "razon": x.get("que_buscar_manual", ""),
    })

# ------- escribir -------
wbo = openpyxl.Workbook()
HDR = PatternFill("solid", fgColor="1F4E78"); HF = Font(bold=True, color="FFFFFF", size=11)
WRAP = Alignment(wrap_text=True, vertical="top"); CEN = Alignment("center", "center", wrap_text=True)
TH = Side(style="thin", color="BFBFBF"); BD = Border(left=TH, right=TH, top=TH, bottom=TH)
FILL = {"INCLUIDO": "E2EFDA", "PENDIENTE (por verificar)": "FFF2CC",
        "RESCATABLE (confirmar)": "DDEBF7", "CANDIDATO (por verificar)": "DDEBF7"}
ROLC = {"contenido": "548235", "si": "548235", "apoyo": "C00000", "sin_IA": "C00000",
        "parcial": "BF8F00", "no": "C00000", "no_claro": "BF8F00"}

COLS = [("id", 26), ("Estado", 20), ("País", 6), ("Caso", 44), ("Origen", 18),
        ("Cuenta indicador", 15), ("rol_IA", 12), ("rol_IA fuente", 12), ("Confianza", 10),
        ("Qué es y cómo usa la IA", 52), ("URL funcional", 40),
        ("Evidencia / cita verbatim", 60), ("Fuente de la cita", 34),
        ("Notas / a verificar", 46)]

def write_sheet(ws, rows, title, subtitle):
    ws["A1"] = title; ws["A1"].font = Font(bold=True, size=14, color="1F4E78")
    ws["A2"] = subtitle; ws["A2"].font = Font(italic=True, size=10, color="595959")
    hr = 4
    for j, (h, w) in enumerate(COLS, 1):
        c = ws.cell(row=hr, column=j, value=h)
        c.fill = HDR; c.font = HF; c.border = BD; c.alignment = CEN
        ws.column_dimensions[get_column_letter(j)].width = w
    r = hr + 1
    for rec in rows:
        vals = [rec["id"], rec["estado"], rec["pais"], rec["caso"], rec["origen"],
                rec["cuenta"], rec["rol_IA"], rec["rol_verificado"], rec["confianza"],
                rec["desc"], rec["url"], rec["evidencia"], rec["fuente"], rec["razon"]]
        for j, v in enumerate(vals, 1):
            c = ws.cell(row=r, column=j, value=v)
            c.border = BD; c.alignment = CEN if j in (2, 3, 6, 7, 8, 9) else WRAP
        if rec["estado"] in FILL:
            ws.cell(row=r, column=2).fill = PatternFill("solid", fgColor=FILL[rec["estado"]])
        rc = ROLC.get(str(rec["rol_IA"]))
        if rc:
            ws.cell(row=r, column=7).font = Font(bold=True, color=rc)
        r += 1
    ws.freeze_panes = "D5"
    ws.auto_filter.ref = f"A{hr}:{get_column_letter(len(COLS))}{r-1}"

ws1 = wbo.active; ws1.title = "Casos (analizar)"
principal = incluidos + pendientes + rescatables + candidatos
write_sheet(ws1, principal,
            "ILIA 2026 — Casos para análisis detallado (referencia de verdad)",
            "Verificar consistencia del análisis en detalle con estas decisiones. "
            "INCLUIDO=confirmado (rol_IA verificado con cita). PENDIENTE/RESCATABLE/"
            "CANDIDATO=aún por confirmar (ver 'Notas'). Escenario activo=A.")

ws2 = wbo.create_sheet("Excluidos (razón)")
write_sheet(ws2, excluidos,
            "ILIA 2026 — Casos EXCLUIDOS (con razón)",
            "Para chequeo cruzado: NO deben analizarse como casos válidos. "
            "rol_IA=apoyo/sin_IA => la IA no procesa el contenido participativo.")

# Leyenda
wl = wbo.create_sheet("Leyenda")
wl["A1"] = "Leyenda y conteos"; wl["A1"].font = Font(bold=True, size=14, color="1F4E78")
lines = [
    "", "Estados:",
    "  INCLUIDO — caso confirmado en el conjunto elegible 2026 (rol_IA verificado con cita verbatim de fuente primaria).",
    "  PENDIENTE (por verificar) — cuenta en el conjunto pero su rol_IA no se pudo verificar aún (CO Tenemos que hablar de Colombia).",
    "  RESCATABLE (confirmar) — excluido/rechazado que la búsqueda halló INCLUIBLE; falta confirmación manual (ver Notas).",
    "  CANDIDATO (por verificar) — caso nuevo descubierto; requiere confirmar que la IA procesa el CONTENIDO participativo.",
    "  EXCLUIDO (…) — fuera del conjunto; ver razón en 'Excluidos (razón)'.",
    "",
    "rol_IA (criterio de elegibilidad):",
    "  contenido — la IA analiza/clasifica/agrupa/resume/sentimiento sobre los aportes ciudadanos => ELEGIBLE.",
    "  apoyo — la IA cumple rol periférico (atención/trámites, muestreo, visión de obras, desinformación) => NO elegible.",
    "  sin_IA — no hay IA sobre el proceso (sistematización manual; IA solo como tema) => NO elegible.",
    "  'rol_IA fuente' = 'verificado' (verificación profunda con cita) o 'borrador' (recodificación 2025).",
    "",
    "Cuenta indicador: Sí · 'Sí bajo A · No bajo B' (casos de Escenario) · No · Por confirmar.",
    "Escenario activo = A. Bajo B sale CL 'Tenemos que hablar de Chile'.",
    "",
    "CONTEOS:",
    f"  INCLUIDOS confirmados: {len(incluidos)}",
    f"  PENDIENTE: {len(pendientes)}",
    f"  RESCATABLES (confirmar): {len(rescatables)}",
    f"  CANDIDATOS descubrimiento (por verificar): {len(candidatos)}",
    f"  EXCLUIDOS listados: {len(excluidos)}",
    f"  Conjunto elegible hoy (A) = {len(incluidos)+len(pendientes)}  (con rescatables confirmados hasta {len(incluidos)+len(pendientes)+len(rescatables)})",
    "",
    "Trazabilidad: la decisión de cada caso está en Planilla_Consolidada_Casos_ILIA2026.xlsx",
    "(hojas Detalle consolidado / Verificación profunda / Validación) y en",
    "recodificacion_2025.csv (rol_IA con cita). Candidatos y rescates:",
    "busqueda_ampliada_2026_resultados.json. Guía de verificación manual:",
    "checklist_verificacion_manual.md.",
]
for i, t in enumerate(lines, start=2):
    c = wl.cell(row=i, column=1, value=t)
    if t.endswith(":") and not t.startswith("  "):
        c.font = Font(bold=True, size=11, color="1F4E78")
    else:
        c.font = Font(size=10)
    c.alignment = WRAP
wl.column_dimensions["A"].width = 120

wbo.save(OUT)
print("OK ->", OUT)
print(f"INCLUIDOS={len(incluidos)} PENDIENTE={len(pendientes)} RESCATABLES={len(rescatables)} "
      f"CANDIDATOS={len(candidatos)} EXCLUIDOS={len(excluidos)}")
print(f"Elegible A = {len(incluidos)+len(pendientes)}")
