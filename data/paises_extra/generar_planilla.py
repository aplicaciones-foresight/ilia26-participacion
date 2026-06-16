#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Planilla de trabajo (.xlsx) + matriz md: económicos (5) y gobernanza (5 países)."""
import os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from generar_pdf_indicadores import ECON, ECON_CELLS  # económicos (fuente única)

OK = PatternFill("solid", fgColor="C6EFCE"); PART = PatternFill("solid", fgColor="FFEB9C")
MAN = PatternFill("solid", fgColor="FFC7CE"); HDR = PatternFill("solid", fgColor="1F4E78")
SUBF = PatternFill("solid", fgColor="DDEBF7")
WHITEB = Font(color="FFFFFF", bold=True, size=10); BOLD = Font(bold=True)
WRAP = Alignment(wrap_text=True, vertical="top"); THIN = Border(*[Side(style="thin", color="D9D9D9")]*4)
FILLS = {"ok": OK, "partial": PART, "manual": MAN, "na": MAN}

def st(v):
    s = str(v).upper()
    if any(k in s for k in ["PEND", "NO OBT", "N/D", "NO ENC", "NE"]): return "manual"
    if any(k in s for k in ["PRELIM", "DUDA", "BAJA"]): return "partial"
    return "ok"

def header(ws, headers, widths, row=1):
    for c, (h, w) in enumerate(zip(headers, widths), 1):
        cell = ws.cell(row, c, h); cell.fill = HDR; cell.font = WHITEB
        cell.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
        ws.column_dimensions[get_column_letter(c)].width = w
    ws.row_dimensions[row].height = 28

wb = Workbook()
# ---- LÉEME ----
ws = wb.active; ws.title = "LÉEME"; ws.column_dimensions["A"].width = 112
for r, (t, sz, b) in enumerate([
 ("ILIA 2026 — Planilla de trabajo: indicadores para los 5 países extra", 14, True),
 ("Generado 2026-06-16. Económicos: España, Estonia, Singapur, Alemania, Portugal. Gobernanza: los 5 (Estonia, Singapur, Alemania, España, Portugal).", 10, False),
 ("", 6, False),
 ("Colores de las celdas de DATO:  Verde = listo · Ámbar = parcial/PRELIM · Rojo = no obtenido (acción manual).", 11, True),
 ("PRELIM = codificado sin leer el texto primario de la estrategia (PDF 403) → confirmar verbatim con el PDF.", 9, False),
 ("", 6, False),
 ("Hojas: 'Económicos (5 países)' · 'Gobernanza (5 países)' (puntaje propuesto por la rúbrica) · 'Pendientes (acción tuya)'.", 10, False),
 ("Detalle, fuentes y dudas por país en data/paises_extra/gobernanza/*.md (gobernanza_<país>.md, FUENTES, INCERTIDUMBRES).", 9, False),
 ("", 6, False),
 ("Banderas destacadas: ES recoge Género (=1) y tiene ley nacional + AESIA; PT tiene NUEVA Agenda 2026-2030 (antigüedad=4);", 9, False),
 ("Estonia NO figura en ISO SC42 (=0, verificar); SG iniciativa legal=1 (soft law, no debilidad); GCI pilares solo completos para España.", 9, False),
], 1):
    cell = ws.cell(r, 1, t); cell.font = Font(bold=b, size=sz, color="1F4E78" if b and sz >= 11 else "000000"); cell.alignment = WRAP

# ---- Económicos (5 países) ----
ws = wb.create_sheet("Económicos (5 países)")
header(ws, ["ID", "Indicador", "Fuente sugerida", "España", "Estonia", "Singapur", "Alemania", "Portugal", "Nota / pendiente"],
       [6, 26, 16, 20, 20, 22, 22, 18, 40])
order = ["España (ES)", "Estonia (EE)", "Singapur (SG)", "Alemania (DE)", "Portugal (PT)"]
r = 2
for idt, name, sugg, desc in ECON:
    ws.cell(r, 1, idt); ws.cell(r, 2, name).font = BOLD; ws.cell(r, 3, sugg); note = ""
    for ci, country in enumerate(order):
        dato, status, fuentes, pend = ECON_CELLS[country][idt]
        cc = ws.cell(r, 4 + ci, dato); cc.fill = FILLS[status]
        if pend and not note: note = pend
    ws.cell(r, 9, note)
    for c in range(1, 10): ws.cell(r, c).border = THIN; ws.cell(r, c).alignment = WRAP
    ws.row_dimensions[r].height = 42; r += 1
ws.freeze_panes = "B2"

# ---- Gobernanza (5 países) ----
# (subdim, indicador(ID), fuente, EE, SG, DE, ES, PT, nota)
G = [
 ("Visión e Institucionalidad", "Existencia de estrategia (103)", "Estrategia nac. + OECD.AI", "3","3","3","3","3",""),
 ("", "Antigüedad (104)", "Estrategia", "4","3","3","4","4","EE: White Paper 2024-30 · SG: NAIS 2.0 2023 · DE: Aktionsplan 2023 · ES: Estrategia 2024 · PT: ANIA 2026-30"),
 ("", "Actualización (105)", "Estrategia", "3","3","3","3","3",""),
 ("", "Mecanismos de evaluación (106)", "Estrategia", "3 (PRELIM)","3 (PRELIM)","3","3","3",""),
 ("", "Presupuesto (107)", "Estrategia", "3","3","3","3","3","EE €85M · SG >S$1.000M · DE €5.000M · ES €1.500M · PT >€400M"),
 ("", "Hoja de ruta (108)", "Estrategia", "3","3","3","3","3",""),
 ("", "Tópico: Ética y gobernanza (109)", "Estrategia", "1","1","1","1","1",""),
 ("", "Tópico: Infraestructura y tecnología (110)", "Estrategia", "1","1","1","1","1",""),
 ("", "Tópico: Desarrollo de capacidades (111)", "Estrategia", "1","1","1","1","1",""),
 ("", "Tópico: Datos (112)", "Estrategia", "1","1","1","1","1",""),
 ("", "Tópico: Gobierno digital (113)", "Estrategia", "1","1","1","1","1",""),
 ("", "Tópico: Industria y emprendimiento (114)", "Estrategia", "1","1","1","1","1",""),
 ("", "Tópico: I+D (115)", "Estrategia", "1","1","1","1","1",""),
 ("", "Tópico: Cooperación reg./int'l (116)", "Estrategia", "1","1","1","1","1",""),
 ("", "Tópico: Perspectiva de género (117)", "Estrategia", "0","0","0","1 (PRELIM)","0","Solo ES recoge género (mención transversal); resto NO ENCONTRADO/0"),
 ("", "Tópico: Sostenibilidad (118)", "Estrategia", "1 (BAJA)","1 (PRELIM)","1 (PRELIM)","1","0 (PRELIM)","PT: solo principio en EDN, no eje en ANIA"),
 ("", "Particip. ciudadana elaboración (119)", "Estrategia", "2 (PRELIM)","1 (PRELIM)","2","3 (PRELIM)","4","PT: consulta pública con resultados"),
 ("", "Multistakeholder elaboración (121)", "Estrategia", "3 (PRELIM)","3 (PRELIM)","4 (PRELIM)","4 (PRELIM)","5","PT: Gob+4"),
 ("", "Multistakeholder implementación (122)", "Estrategia", "4 (PRELIM)","4 (PRELIM)","4 (PRELIM)","4","4 (PRELIM)",""),
 ("", "Institucionalidad (123)", "Estrategia + OECD.AI", "5","5","5","5","5","ES: SEDIA+AESIA · DE: 3 min+PLS+BNetzA · PT: AMA+FCT+ANACOM"),
 ("", "Coordinación interinstitucional (124)", "Estrategia", "3","3","3","3","3",""),
 ("Vinculación Internacional", "ISO SC 42 / IA (125)", "iso.org/6794475", "0 (DUDA)","2","2","2","1","EE: no figura (verificar) · PT: Observador"),
 ("", "ISO SC 27 / Seguridad (126)", "iso.org/45306", "2","2","2","2","1","PT: Observador"),
 ("", "Acuerdos internacionales de IA (127)", "OECD/CEPAL", "2","2","2","2","2","GPAI: miembros DE/ES; EE/SG/PT no individual"),
 ("Regulación", "Iniciativa legal sobre IA (128)", "Legislación nac./UE", "3","1","3","3","3","UE: EU AI Act (EE/DE/ES/PT). SG: soft law=1. ES/DE: además ley nacional"),
 ("", "Clasificación de riesgo (129)", "Legislación/marco", "1","1 (PRELIM)","1","1","1",""),
 ("", "Exploración regulatoria / sandbox (130)", "Legislación/marco", "1","1","1","1","1 (PRELIM)","ES: 1er sandbox UE"),
 ("", "Ley de protección de datos (131)", "DLA Piper", "1","1","1","1","1",""),
 ("", "Autoridad de protección de datos (132)", "DLA Piper", "1","1","1","1","1","AKI/PDPC/BfDI/AEPD/CNPD"),
 ("IA Ética, Responsable y Segura", "Ciberseguridad — Legal (133)", "UIT GCI 2024", "PEND","PEND","PEND","20","PEND","Solo ES con pilares; resto Tier 1, pilares en anexo PDF"),
 ("", "Ciberseguridad — Técnico (134)", "UIT GCI 2024", "PEND","PEND","PEND","20","PEND",""),
 ("", "Ciberseguridad — Organizacional (135)", "UIT GCI 2024", "PEND","PEND","PEND","20","PEND",""),
 ("", "Ciberseguridad — Desarrollo de capacidades (136)", "UIT GCI 2024", "PEND","PEND","PEND","19,74","PEND",""),
 ("", "Ciberseguridad — Cooperación (137)", "UIT GCI 2024", "PEND","PEND","PEND","20","PEND",""),
 ("", "GIRAI — Protección de datos y privacidad (138)", "GIRAI", "NE","NE","NE","NE","NE","Portal JS/PDF → extracción manual"),
 ("", "GIRAI — Seguridad, precisión y confiabilidad (139)", "GIRAI", "NE","NE","NE","NE","NE","Idem"),
 ("", "Energía limpia y asequible — NRI (144)", "NRI/Portulans", "80,71","86,87","86,44","PEND","88,16","ES: ver página país NRI"),
 ("", "% ERNC matriz eléctrica (145)", "EMBER", "55,75%","4,93%","58,64%","57,34%","85,19%","2024, renovables total. ES/PT/DE: ERNC excl. gran hidro es menor (ver energia_*.md)"),
]
ws = wb.create_sheet("Gobernanza (5 países)")
header(ws, ["Subdimensión", "Indicador (ID)", "Fuente", "EE", "SG", "DE", "ES", "PT", "Notas / banderas"],
       [22, 38, 18, 9, 9, 9, 9, 9, 46])
r = 2
for sub, ind, fte, ee, sg, de, es, pt, nota in G:
    if sub: ws.cell(r, 1, sub).font = BOLD; ws.cell(r, 1).fill = SUBF
    ws.cell(r, 2, ind); ws.cell(r, 3, fte)
    for ci, v in enumerate([ee, sg, de, es, pt]):
        cc = ws.cell(r, 4 + ci, v); cc.fill = FILLS[st(v)]
        cc.alignment = Alignment(wrap_text=True, vertical="top", horizontal="center")
    ws.cell(r, 9, nota)
    for c in range(1, 10):
        ws.cell(r, c).border = THIN
        if c in (1, 2, 3, 9): ws.cell(r, c).alignment = WRAP
    ws.row_dimensions[r].height = 30; r += 1
ws.freeze_panes = "D2"

# ---- Pendientes (acción tuya) ----
ws = wb.create_sheet("Pendientes (acción tuya)")
header(ws, ["Prioridad", "Qué falta", "Países", "Cómo obtenerlo (ruta exacta)"], [10, 42, 20, 88])
PEND = [
 ("1","Empresas de IA · Nº y Valor de inversiones (70-72)","los 5","cat.eto.tech → dataset 'Investment' → país → Companies / Number of investments / Investment value."),
 ("1","Gobierno Digital — OSI (92)","los 5","UN Data Center (egovkb, 2024) o CSV World Bank Data360 UN_EGDI_OSI_WIDEF.csv o Technical Appendix 2024. EGDI: EE 0,97274 · SG 0,96912 · PT 0,8415 · DE/ES Very High."),
 ("1","Ciberseguridad GCI — 5 pilares (133-137)","EE, SG, DE, PT","World Bank Data360 (indicadores por pilar: ITU_GCI_*_SCORE) o anexo PDF GCI 2024. España YA completa (20/20/20/19,74/20)."),
 ("1","GIRAI — 2 áreas (138-139)","los 5","global-index.ai → Explore data → país → dimensión/área (Data protection & privacy; Safety, accuracy & reliability)."),
 ("2","Familias de patentes IA (82)","ES/EE/PT (DE reconfirmar; SG actualizar)","cat.eto.tech → dataset 'Patent' → país (AI patent applications/granted)."),
 ("2","Aplicantes e Inventores de patentes IA (83-84)","los 5","NO existen en OECD.AI. Lens.org/Espacenet: CPC G06N facetado por país del SOLICITANTE / del INVENTOR."),
 ("2","Desarrollo de IA — modelos Hugging Face (81)","los 5","API HF: huggingface.co/api/models?author=<ORG> por org (ver notas Económicos), sumar por país."),
 ("2","NRI energía limpia — España (144)","ES","Página país https://networkreadinessindex.org/country/spain/ o PDF país 2025 (indicador 'Affordable & clean energy')."),
 ("3","Verbatim de estrategia (ítems PRELIM)","los 5","Pasarme los PDF de las estrategias (krattAI/White Paper EE; NAIS 2.0 SG; KI-Strategie/Aktionsplan DE; Estrategia IA 2024 ES; ANIA 2026-30 PT) → codificación verbatim."),
 ("3","Decisiones metodológicas","UE / SG","(a) cómo puntuar el EU AI Act como 'iniciativa legal' en países UE; (b) si el Update SG may-2026 cambia 'Antigüedad'; (c) confirmar ISO SC42 de Estonia (=0)."),
 ("3","I+D/PIB oficial exacto — Singapur (73, económico)","SG","A*STAR National Survey of R&D (PDF). Hoy: WB 2,16% (2020) / OCDE ~1,85% (2022)."),
]
r = 2
for pr, que, pa, como in PEND:
    ws.cell(r, 1, pr); ws.cell(r, 2, que).font = BOLD; ws.cell(r, 3, pa); ws.cell(r, 4, como)
    for c in range(1, 5): ws.cell(r, c).border = THIN; ws.cell(r, c).alignment = WRAP
    ws.row_dimensions[r].height = 42; r += 1
ws.freeze_panes = "A2"

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Planilla_ILIA2026_paises_extra.xlsx")
wb.save(out); print("OK xlsx ->", out)

# ---- Matriz consolidada md (gobernanza 5 países) ----
md = ["# ILIA 2026 — GOBERNANZA: matriz consolidada 5 países\n",
      "Puntaje propuesto por la rúbrica. PRELIM=sin texto primario · PEND=manual (403) · NE=no encontrado.\n",
      "Detalle/fuentes/dudas por país: gobernanza_<país>.md, FUENTES_*, INCERTIDUMBRES_*.\n",
      "\n| Subdim | Indicador (ID) | EE | SG | DE | ES | PT |", "|---|---|---|---|---|---|---|"]
for sub, ind, fte, ee, sg, de, es, pt, nota in G:
    md.append(f"| {sub} | {ind} | {ee} | {sg} | {de} | {es} | {pt} |")
mdout = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gobernanza", "REPORTE_gobernanza_5paises.md")
open(mdout, "w").write("\n".join(md) + "\n")
print("OK md ->", mdout)
