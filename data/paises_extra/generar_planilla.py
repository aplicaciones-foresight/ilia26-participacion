#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera la planilla de trabajo (.xlsx) con todo lo recolectado + pendientes."""
import os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from generar_pdf_indicadores import ECON, ECON_CELLS  # fuente única de verdad (económicos)

OK = PatternFill("solid", fgColor="C6EFCE")     # verde
PART = PatternFill("solid", fgColor="FFEB9C")   # ámbar
MAN = PatternFill("solid", fgColor="FFC7CE")    # rojo
HDR = PatternFill("solid", fgColor="1F4E78")
SUBF = PatternFill("solid", fgColor="DDEBF7")
WHITEB = Font(color="FFFFFF", bold=True, size=10)
BOLD = Font(bold=True); WRAP = Alignment(wrap_text=True, vertical="top")
THIN = Border(*[Side(style="thin", color="D9D9D9")]*4)
FILLS = {"ok": OK, "partial": PART, "manual": MAN, "na": MAN}

def style_header(ws, row, headers, widths):
    for c, (h, w) in enumerate(zip(headers, widths), 1):
        cell = ws.cell(row, c, h); cell.fill = HDR; cell.font = WHITEB
        cell.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
        ws.column_dimensions[get_column_letter(c)].width = w
    ws.row_dimensions[row].height = 26

wb = Workbook()

# ---------- Hoja 1: LÉEME ----------
ws = wb.active; ws.title = "LÉEME"
ws.column_dimensions["A"].width = 110
rows = [
 ("ILIA 2026 — Planilla de trabajo: indicadores para los países extra", 14, True),
 ("Generado 2026-06-14. Económicos: España, Estonia, Singapur, Alemania, Portugal. Gobernanza: Estonia y Singapur.", 10, False),
 ("", 6, False),
 ("Colores de las celdas de DATO:", 11, True),
 ("   Verde = listo (volcar directo) · Ámbar = parcial/PRELIM (usar con la nota) · Rojo = no obtenido (acción manual tuya).", 10, False),
 ("", 6, False),
 ("Hojas:", 11, True),
 ("   • 'Económicos (5 países)'  — 11 indicadores × 5 países.", 10, False),
 ("   • 'Gobernanza (EE-SG)'     — 38 subindicadores × Estonia/Singapur (con puntaje propuesto).", 10, False),
 ("   • 'Pendientes (acción tuya)' — lo que SÍ o SÍ debes hacer tú, con la ruta exacta.", 10, False),
 ("", 6, False),
 ("Nota: el entorno no pudo abrir dashboards/PDFs (HTTP 403); lo determinístico (GitHub, MCI, OWID/EMBER) está volcado;", 10, False),
 ("lo demás se buscó por WebSearch con doble validación. Detalle y todas las URLs en data/paises_extra/*.md.", 10, False),
 ("Nota planilla: la lista oficial incluye además 'Participación ciudadana en la implementación' (ID 120), que no estaba", 10, False),
 ("en tu lista; si lo necesitas se codifica análogo al 119.", 10, False),
]
r = 1
for txt, sz, bold in rows:
    c = ws.cell(r, 1, txt); c.font = Font(bold=bold, size=sz, color="1F4E78" if bold and sz>=11 else "000000")
    c.alignment = WRAP; r += 1

# ---------- Hoja 2: Económicos ----------
ws = wb.create_sheet("Económicos (5 países)")
headers = ["ID","Indicador","Fuente sugerida","España","Estonia","Singapur","Alemania","Portugal","Nota / pendiente"]
style_header(ws, 1, headers, [6,26,16,20,20,22,22,18,40])
order = ["España (ES)","Estonia (EE)","Singapur (SG)","Alemania (DE)","Portugal (PT)"]
r = 2
for idt, name, sugg, desc in ECON:
    ws.cell(r,1,idt); ws.cell(r,2,name).font=BOLD; ws.cell(r,3,sugg)
    note = ""
    for ci, country in enumerate(order):
        dato, status, fuentes, pend = ECON_CELLS[country][idt]
        cell = ws.cell(r, 4+ci, dato); cell.fill = FILLS[status]; cell.alignment = WRAP
        if pend and not note: note = pend
    ws.cell(r, 9, note).alignment = WRAP
    for c in range(1,10): ws.cell(r,c).border=THIN; ws.cell(r,c).alignment=WRAP
    ws.row_dimensions[r].height = 42; r += 1
ws.freeze_panes = "B2"

# ---------- Hoja 3: Gobernanza EE/SG ----------
ws = wb.create_sheet("Gobernanza (EE-SG)")
headers = ["Subdimensión","Indicador / Subindicador (ID)","Fuente","Estonia (dato · puntaje)","Coment. EE","Singapur (dato · puntaje)","Coment. SG"]
style_header(ws, 1, headers, [22,40,22,26,34,26,34])
P="PRELIM (sin texto primario; confirmar con PDF)"; NE="NO ENCONTRADO (extracción manual)"
PEND_GCI="5 pilares en anexo PDF GCI 2024 (403)"; PEND_GIRAI="puntaje por área en portal JS/PDF (403)"
# (subdim, indicador-subindicador, fuente, ee_dato, ee_status, ee_com, sg_dato, sg_status, sg_com)
GOVR = [
 ("Visión e Institucionalidad","Estrategia de IA — Existencia (103)","Estrategia nacional + OECD.AI","3 (Tiene)","ok","","3 (Tiene)","ok",""),
 ("","Estrategia de IA — Antigüedad (104)","Estrategia + OECD.AI","4 (White Paper 2024-2030)","ok","Si ILIA usa la gen. 2022-23 → 3","3 (NAIS 2.0 dic-2023)","ok","Si el Update may-2026 cuenta → 4"),
 ("","Estrategia de IA — Actualización (105)","Estrategia + OECD.AI","3","ok","","3","ok",""),
 ("","Mecanismos — Mecanismos de evaluación (106)","Estrategia","3","partial",P,"3","partial",P),
 ("","Mecanismos — Presupuesto (107)","Estrategia","3 (€85M 2024-26)","ok","","3 (>S$1.000M/5 años)","ok",""),
 ("","Mecanismos — Hoja de ruta (108)","Estrategia","3 (Action Plan Kratt)","ok","","3 (15 Acciones)","ok",""),
 ("","Tópico — Ética y gobernanza (109)","Estrategia","1","ok","","1","ok",""),
 ("","Tópico — Infraestructura y tecnología (110)","Estrategia","1","ok","","1","ok",""),
 ("","Tópico — Desarrollo de capacidades (111)","Estrategia","1","ok","","1","ok",""),
 ("","Tópico — Datos (112)","Estrategia","1","ok","","1","ok",""),
 ("","Tópico — Gobierno digital (113)","Estrategia","1","ok","","1","ok",""),
 ("","Tópico — Industria y emprendimiento (114)","Estrategia","1","ok","","1","ok",""),
 ("","Tópico — I+D (115)","Estrategia","1","ok","","1","ok",""),
 ("","Tópico — Cooperación reg./int'l (116)","Estrategia","1","ok","","1","ok",""),
 ("","Tópico — Perspectiva de género (117)","Estrategia","0","manual",NE+" (verificar en PDF)","0","manual",NE+" (verificar en PDF)"),
 ("","Tópico — Sostenibilidad (118)","Estrategia","1","partial",P+" (confianza BAJA)","1","partial",P),
 ("","Actores — Particip. ciudadana elaboración (119)","Estrategia","2","partial","Apoyado en debate 'kratt law' 2017-19 (previo)","1","partial","Consulta hallada fue del MGF GenAI, no NAIS 2.0"),
 ("","Actores — Multistakeholder elaboración (121)","Estrategia","3 (Gob+2)","partial",P,"3 (Gob+2)","partial",P),
 ("","Actores — Multistakeholder implementación (122)","Estrategia","4 (Gob+3)","partial",P,"4 (Gob+3)","partial",P),
 ("","Institucionalidad — Existencia (123)","Estrategia + OECD.AI","5 (MKM, Riigikantselei, RIA, Eesti.ai)","ok","","5 (SNDGG, IMDA, AISG, PDPC, AI Verify, NAIC)","ok","Verificar fecha/mandato NAIC (feb-2026)"),
 ("","Institucionalidad — Coordinación interinst. (124)","Estrategia","3","ok","","3","ok",""),
 ("Vinculación Internacional","Estándares — ISO SC 42 / IA (125)","iso.org/committee/6794475","0 (No participa)","manual","DUDA: no figura; confianza MEDIA → verificar en iso.org","2 (Participante)","ok",""),
 ("","Estándares — ISO SC 27 / Seguridad (126)","iso.org/committee/45306","2 (Participante)","ok","","2 (Participante)","ok",""),
 ("","Acuerdos internacionales de IA (127)","OECD/CEPAL","2 (OECD + EU Plan + CoE vía UE)","ok","GPAI: EE no miembro","2 (ASEAN + OECD + UNESCO)","partial","Verificar adhesión OECD AI Principles y GPAI"),
 ("Regulación","Regulación IA — Iniciativa legal (128)","Legislación nac./UE","3 (EU AI Act)","ok","Definir cómo puntúa el EU AI Act en países UE","1 (soft law, sin ley dura)","ok","No es debilidad; sugerir nota cualitativa"),
 ("","Regulación IA — Clasificación de riesgo (129)","Legislación/marco","1 (EU AI Act)","ok","","1 (en marco voluntario)","partial","Se sostiene en marco, no ley → confirmar criterio"),
 ("","Regulación IA — Exploración regulatoria (130)","Legislación/marco","1 (sandbox EE-FI)","ok","","1 (AI Verify)","ok",""),
 ("","Datos personales — Ley vigente (131)","DLA Piper","1 (GDPR + PDPA)","ok","","1 (PDPA 2012)","ok",""),
 ("","Datos personales — Autoridad (132)","DLA Piper","1 (AKI)","ok","aki.ee","1 (PDPC)","ok","pdpc.gov.sg"),
 ("IA Ética, Responsable y Segura","Ciberseguridad — Legal (133)","UIT GCI 2024","PEND","manual",PEND_GCI+" · Tier 1","PEND","manual",PEND_GCI+" · Tier 1"),
 ("","Ciberseguridad — Técnico (134)","UIT GCI 2024","PEND","manual",PEND_GCI,"PEND","manual",PEND_GCI),
 ("","Ciberseguridad — Organizacional (135)","UIT GCI 2024","PEND","manual",PEND_GCI,"PEND","manual",PEND_GCI),
 ("","Ciberseguridad — Desarrollo de capacidades (136)","UIT GCI 2024","PEND","manual",PEND_GCI,"PEND","manual",PEND_GCI),
 ("","Ciberseguridad — Cooperación (137)","UIT GCI 2024","PEND","manual",PEND_GCI,"PEND","manual",PEND_GCI),
 ("","Ética y Seguridad — Protección de datos y privacidad (138)","GIRAI","NO ENCONTRADO","manual",PEND_GIRAI,"NO ENCONTRADO","manual",PEND_GIRAI),
 ("","Ética y Seguridad — Seguridad, precisión y confiabilidad (139)","GIRAI","NO ENCONTRADO","manual",PEND_GIRAI,"NO ENCONTRADO","manual",PEND_GIRAI),
 ("","Sustentabilidad — Energía limpia y asequible (144)","NRI / Portulans","80,71 (ed. 2025)","ok","Confirmar edición","86,87 (ed. 2025)","ok","Confirmar edición"),
 ("","Sustentabilidad — % ERNC matriz (145)","EMBER","55,75 % (2024) / 59,57 % (2025)","ok","Determinístico","4,93 % (2024) / 5,49 % (2025)","ok","Determinístico"),
]
r = 2
for sub, ind, fte, ee, ees, eec, sg, sgs, sgc in GOVR:
    ws.cell(r,1,sub).font=BOLD; ws.cell(r,2,ind); ws.cell(r,3,fte)
    a=ws.cell(r,4,ee); a.fill=FILLS[ees]
    ws.cell(r,5,eec)
    b=ws.cell(r,6,sg); b.fill=FILLS[sgs]
    ws.cell(r,7,sgc)
    for c in range(1,8): ws.cell(r,c).border=THIN; ws.cell(r,c).alignment=WRAP
    if sub: ws.cell(r,1).fill=SUBF
    ws.row_dimensions[r].height = 30; r += 1
ws.freeze_panes = "C2"

# ---------- Hoja 4: Pendientes (acción tuya) ----------
ws = wb.create_sheet("Pendientes (acción tuya)")
headers = ["Prioridad","Qué falta","Países","Cómo obtenerlo (ruta exacta)"]
style_header(ws, 1, headers, [10,40,18,90])
PEND = [
 ("1","Empresas de IA · Nº inversiones · Valor inversión (70-72)","ES/EE/SG/DE/PT","cat.eto.tech → dataset 'Investment' → seleccionar país → leer Companies / Number of investments / Investment value. (o Zenodo cat.zip record 19103157)"),
 ("1","Gobierno Digital — OSI (92)","los 5","UN Data Center (publicadministration.un.org/egovkb → 2024) o CSV World Bank Data360 UN_EGDI_OSI_WIDEF.csv, o Technical Appendix 2024 (PDF). EGDI ya tengo: EE 0,97274 / SG 0,96912."),
 ("1","Ciberseguridad GCI — 5 pilares (133-137)","EE/SG","PDF GCI 2024 (itu.int) → anexo 'country dashboards' (5 barras /20), o ITU DataHub datahub.itu.int (indicador 90014 y pilares), o World Bank Data360 ITU_GCI. Ambos Tier 1."),
 ("1","GIRAI — 2 áreas (138-139)","EE/SG","global-index.ai → Explore data → país → dimensión 'Human rights & AI'/'Data protection & privacy' y 'Responsible AI governance'/'Safety, accuracy & reliability'. (SG también en Fig.19 informe LIRNEasia)."),
 ("2","Familias de patentes IA (82)","ES/EE/PT (DE reconfirmar; SG actualizar)","cat.eto.tech → dataset 'Patent' → país → 'AI patent applications/granted'. (o OWID artificial-intelligence-patents-submitted)."),
 ("2","Aplicantes e Inventores de patentes IA (83-84)","los 5","NO existen en OECD.AI. Lens.org o Espacenet: consulta CPC G06N (+ taxonomía WIPO), facetar por país del SOLICITANTE (aplicantes) y por país del INVENTOR (inventores), contar entidades distintas."),
 ("2","Desarrollo de IA — modelos Hugging Face (81)","los 5","API HF: https://huggingface.co/api/models?author=<ORG>&limit=1000 por cada org de la lista (ver hoja Económicos/notas), sumar por país, anotar fecha."),
 ("3","Verbatim de estrategia (ítems PRELIM 106,117,118,119,121,122,129)","EE/SG","Pasarme los PDF de las estrategias (krattAI/White Paper EE; NAIS 2.0 SG) → codifico verbatim definitivo."),
 ("3","Decisiones metodológicas","EE (y UE)","Definir: (a) cómo puntuar el EU AI Act como 'iniciativa legal' en países UE (afecta 128-130); (b) si el Update SG may-2026 cambia 'Antigüedad'; (c) confirmar ISO SC 42 de Estonia en iso.org."),
 ("3","Singapur — Gasto I+D/PIB valor oficial exacto (73)","SG","A*STAR National Survey of R&D (PDF) para el valor 2022/2023 exacto. Hoy: WB 2,16% (2020) / OCDE ~1,85% (2022)."),
]
r = 2
for pr, que, pa, como in PEND:
    ws.cell(r,1,pr); ws.cell(r,2,que).font=BOLD; ws.cell(r,3,pa); ws.cell(r,4,como)
    for c in range(1,5): ws.cell(r,c).border=THIN; ws.cell(r,c).alignment=WRAP
    ws.row_dimensions[r].height = 40; r += 1
ws.freeze_panes = "A2"

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Planilla_ILIA2026_paises_extra.xlsx")
wb.save(out); print("OK ->", out)
