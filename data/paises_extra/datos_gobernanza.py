#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fuente ÚNICA de la gobernanza (5 países) — la consumen generar_planilla.py y
generar_pdf_indicadores.py, para que la planilla .xlsx y el PDF nunca diverjan.

- `G`       : matriz consolidada 38 subindicadores × 5 países (puntaje propuesto por rúbrica).
- `st(v)`   : estado/color de una celda (ok/partial/manual) a partir de su texto.
- `GOB_META`: por ID -> (descripción/rúbrica, tipo de fuente) para enriquecer el PDF.
- `gov_sources(srckind, cc)` : URLs de fuente por indicador y país.

Para EDITAR puntajes de gobernanza: cambiar aquí la matriz `G` (única fuente de verdad).
Detalle/justificación/fuentes finas por país: gobernanza/gobernanza_<país>.md, FUENTES_*, INCERTIDUMBRES_*.
"""

# ---- Estado/color de una celda de gobernanza ----
def st(v):
    s = str(v).upper()
    if any(k in s for k in ["PEND", "NO OBT", "N/D", "NO ENC", "NE"]):
        return "manual"
    if any(k in s for k in ["PRELIM", "DUDA", "BAJA"]):
        return "partial"
    return "ok"

# ---- Matriz consolidada (subdim, indicador(ID), fuente, EE, SG, DE, ES, PT, nota) ----
G = [
 ("Visión e Institucionalidad", "Existencia de estrategia (103)", "Estrategia nac. + OECD.AI", "3","3","3","3","3",""),
 ("", "Antigüedad (104)", "Estrategia", "4","4","3","4","4","EE: White Paper 2024-30 · SG: Update NAIS may-2026 = estrategia vigente (decisión operador) · DE: Aktionsplan 2023 · ES: Estrategia 2024 · PT: ANIA 2026-30"),
 ("", "Actualización (105)", "Estrategia", "3","3","3","3","3",""),
 ("", "Mecanismos de evaluación (106)", "Estrategia", "3","3","3","3","3","SG: validado (NAIS se revisa 1.0→2.0→Update 2026; métricas de proyecto)"),
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
 ("", "Tópico: Sostenibilidad (118)", "Estrategia", "1","1","1 (PRELIM)","1","0 (PRELIM)","EE: validado (IA verde/ODS); SG: validado (resource-efficient/'green' AI, Green Data Centre Roadmap); PT: solo principio en EDN, no eje en ANIA"),
 ("", "Particip. ciudadana elaboración (119)", "Estrategia", "5","1","2","3 (PRELIM)","4","EE: >1 mecanismo (encuestas 2150 + 220 entrevistas); SG: sin mecanismo ciudadano (consulta solo a representantes del ecosistema → cuenta en 121); PT: consulta pública con resultados"),
 ("", "Multistakeholder elaboración (121)", "Estrategia", "5","4","4 (PRELIM)","4 (PRELIM)","5","EE: Gob+4 (privado+academia+ONG+público); SG: Gob+3 (industria+academia+non-profit; SCAI/RAISE.SG); PT: Gob+4"),
 ("", "Multistakeholder implementación (122)", "Estrategia", "4","4","4 (PRELIM)","4","4 (PRELIM)","SG: validado — Whole-of-Nation + Tripartite (Gob/NTUC/empleadores) + AI Verify Foundation (non-profit)"),
 ("", "Institucionalidad (123)", "Estrategia + OECD.AI", "5","5","5","5","5","ES: SEDIA+AESIA · DE: 3 min+PLS+BNetzA · PT: AMA+FCT+ANACOM"),
 ("", "Coordinación interinstitucional (124)", "Estrategia", "3","3","3","3","3",""),
 ("Vinculación Internacional", "ISO SC 42 / IA (125)", "iso.org/6794475", "0 (DUDA)","2","2","2","1","EE: no figura (verificar) · PT: Observador"),
 ("", "ISO SC 27 / Seguridad (126)", "iso.org/45306", "2","2","2","2","1","PT: Observador"),
 ("", "Acuerdos internacionales de IA (127)", "OECD/CEPAL", "2","2","2","2","2","GPAI: miembros DE/ES; EE/SG/PT no individual"),
 ("Regulación", "Iniciativa legal sobre IA (128)", "Legislación nac./UE", "3","1","3","3","3","UE: EU AI Act (EE/DE/ES/PT). SG: soft law=1. ES/DE: además ley nacional"),
 ("", "Clasificación de riesgo (129)", "Legislación/marco", "1","1","1","1","1","SG: validado — enfoque 'risk-based, tiered' (NAIS 2.0 p.59; Update p.17)"),
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
 ("", "% ERNC matriz eléctrica (145)", "EMBER 2025", "60,26%","5,49%","59,09%","74,65%","80,90%","Energía limpia = renovables + NUCLEAR (incl. hidro). EMBER 2025, determinístico (energia_limpia_ember2025.py). Solo ES tiene nuclear (18,79%). A confirmar con CENIA"),
]

# Índice de columna de cada país dentro de cada fila de G.
COUNTRY_GIDX = {"EE": 3, "SG": 4, "DE": 5, "ES": 6, "PT": 7}

# ---- Fuentes por indicador (URLs canónicas) ----
ISO42 = "https://www.iso.org/committee/6794475.html?view=participation"
ISO27 = "https://www.iso.org/committee/45306.html?view=participation"
GCI = "https://www.itu.int/epublications/publication/global-cybersecurity-index-2024"
GIRAI = "https://www.global-index.ai"
NRI = "https://networkreadinessindex.org"
EMBER = "https://ember-energy.org/data/electricity-data-explorer/"
OECDAIP = "https://oecd.ai/en/ai-principles"
def DLP(cc): return f"https://www.dlapiperdataprotection.com/?t=law&c={cc}"

# Estrategia / regulación: dominio/portal oficial por país (detalle fino en gobernanza_<país>.md).
ESTRATEGIA_URL = {
 "EE": "https://oecd.ai/en/dashboards/national/estonia",
 "SG": "https://www.smartnation.gov.sg/initiatives/national-ai-strategy/",
 "DE": "https://www.ki-strategie-deutschland.de",
 "ES": "https://www.lamoncloa.gob.es",
 "PT": "https://digital.gov.pt",
}

def gov_sources(srckind, cc):
    if srckind in ("estrategia", "reg"): return [ESTRATEGIA_URL[cc]]
    return {"iso42": [ISO42], "iso27": [ISO27], "acuerdos": [OECDAIP], "dla": [DLP(cc)],
            "gci": [GCI], "girai": [GIRAI], "nri": [NRI], "ember": [EMBER]}.get(srckind, [])

# ---- Metadatos por subindicador: (descripción/rúbrica, tipo de fuente) ----
_TOP = "Tópico de la estrategia (binario 0/1): el aspecto está recogido y con plan de acción. Aquí: "
GOB_META = {
 "103": ("Estrategia/política nacional de IA vigente, respaldada por institución pública. 1 No · 2 En proceso · 3 Tiene.", "estrategia"),
 "104": ("Año de publicación de la estrategia vigente. 1 No existe · 2 2019-2021 · 3 2022-2023 · 4 2024-2025.", "estrategia"),
 "105": ("¿Se ha actualizado la estrategia (o hay actualización planificada)? 1 No · 2 En proceso · 3 Actualizada/planificada.", "estrategia"),
 "106": ("¿Existe método de seguimiento de metas? 1 No · 2 Informal/parcial · 3 Claro.", "estrategia"),
 "107": ("¿Presupuesto asignado a la estrategia? 1 No menciona · 2 Menciona asignación · 3 Monto especificado.", "estrategia"),
 "108": ("¿Plan de acción / hoja de ruta? 1 No · 2 Menciona plan · 3 Plan especificado.", "estrategia"),
 "109": (_TOP + "Ética y gobernanza.", "estrategia"),
 "110": (_TOP + "Infraestructura y tecnología.", "estrategia"),
 "111": (_TOP + "Desarrollo de capacidades.", "estrategia"),
 "112": (_TOP + "Datos.", "estrategia"),
 "113": (_TOP + "Gobierno digital.", "estrategia"),
 "114": (_TOP + "Industria y emprendimiento.", "estrategia"),
 "115": (_TOP + "I+D.", "estrategia"),
 "116": (_TOP + "Cooperación regional/internacional.", "estrategia"),
 "117": (_TOP + "Perspectiva de género.", "estrategia"),
 "118": (_TOP + "Sostenibilidad.", "estrategia"),
 "119": ("Mecanismos de participación ciudadana en la ELABORACIÓN. 1 No · 2 Informal · 3 Mec. sin resultados publ. · 4 Mec. con resultados publ. · 5 >1 mecanismo.", "estrategia"),
 "121": ("Stakeholders en la ELABORACIÓN. 1 Solo gob · 2 Gob+1 · 3 Gob+2 · 4 Gob+3 · 5 Gob+4.", "estrategia"),
 "122": ("Stakeholders en la IMPLEMENTACIÓN. 1 Solo gob · 2 Gob+1 · 3 Gob+2 · 4 Gob+3 · 5 Gob+4.", "estrategia"),
 "123": ("Entidad pública con mandato de liderar/coordinar la política de IA. 1 No · 2 Fuera del Estado · 3 Ministerio · 4 Agencia independiente · 5 >1 institución.", "estrategia"),
 "124": ("Mecanismo de coordinación interinstitucional. 1 No · 2 Informal/preexistente · 3 Mecanismo claro.", "estrategia"),
 "125": ("Membresía nacional en ISO/IEC JTC 1/SC 42 (IA). 0 No participa · 1 Observador · 2 Participante.", "iso42"),
 "126": ("Membresía nacional en ISO/IEC JTC 1/SC 27 (Seguridad). 0 No participa · 1 Observador · 2 Participante.", "iso27"),
 "127": ("Incorporación a acuerdos/comités internacionales de IA (OECD AI Principles, GPAI, CoE, UNESCO…). 0 ninguno · 1 uno · 2 dos o más.", "acuerdos"),
 "128": ("Proyectos/leyes de IA. 1 No · 2 Planificación/borrador · 3 Sí tiene.", "reg"),
 "129": ("¿La iniciativa legal clasifica el riesgo de los sistemas de IA? 0 No · 1 Sí.", "reg"),
 "130": ("¿Se contempla exploración regulatoria / sandbox de IA? 0 No · 1 Sí.", "reg"),
 "131": ("¿Ley de protección de datos personales vigente? 0 No · 1 Sí.", "dla"),
 "132": ("¿Autoridad de protección de datos? 0 No · 1 Sí.", "dla"),
 "133": ("Ciberseguridad — pilar Legal (UIT GCI 2024; cada pilar /20).", "gci"),
 "134": ("Ciberseguridad — pilar Técnico (UIT GCI 2024; cada pilar /20).", "gci"),
 "135": ("Ciberseguridad — pilar Organizacional (UIT GCI 2024; cada pilar /20).", "gci"),
 "136": ("Ciberseguridad — pilar Desarrollo de capacidades (UIT GCI 2024; cada pilar /20).", "gci"),
 "137": ("Ciberseguridad — pilar Cooperación (UIT GCI 2024; cada pilar /20).", "gci"),
 "138": ("GIRAI — Protección de datos y privacidad (0–100; pilar Derechos Humanos).", "girai"),
 "139": ("GIRAI — Seguridad, precisión y confiabilidad (0–100; pilar Gobernanza de IA Responsable).", "girai"),
 "144": ("Energía limpia y asequible — indicador 'Affordable & clean energy' del Network Readiness Index.", "nri"),
 "145": ("% de generación eléctrica renovable en la matriz (EMBER). ERNC ≈ renovables.", "ember"),
}
