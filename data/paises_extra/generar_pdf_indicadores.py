#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera un PDF de trabajo con los indicadores recolectados por país (ILIA 2026)."""
import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (Paragraph, SimpleDocTemplate, Spacer, HRFlowable,
                                KeepTogether, PageBreak)

DJ = "/usr/share/fonts/truetype/dejavu"
pdfmetrics.registerFont(TTFont("DJ", f"{DJ}/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DJ-B", f"{DJ}/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DJ-I", f"{DJ}/DejaVuSans.ttf"))  # no oblique TTF -> usar regular

AZUL = colors.HexColor("#1F4E78"); AMBAR = colors.HexColor("#9A6700")
VERDE = colors.HexColor("#1A7F37"); ROJO = colors.HexColor("#B42318"); GRIS = colors.HexColor("#555555")
H1 = ParagraphStyle("H1", fontName="DJ-B", fontSize=15, leading=18, textColor=AZUL, spaceBefore=4, spaceAfter=2)
H2 = ParagraphStyle("H2", fontName="DJ-B", fontSize=11, leading=13, textColor=AZUL, spaceBefore=8, spaceAfter=3)
H3 = ParagraphStyle("H3", fontName="DJ-B", fontSize=9.5, leading=12, textColor=colors.black, spaceBefore=5, spaceAfter=1)
DESC = ParagraphStyle("DESC", fontName="DJ-I", fontSize=8.2, leading=10, textColor=GRIS, spaceAfter=1)
BODY = ParagraphStyle("BODY", fontName="DJ", fontSize=8.6, leading=10.6, spaceAfter=1)
SRC = ParagraphStyle("SRC", fontName="DJ", fontSize=7.6, leading=9.6, textColor=colors.HexColor("#333333"),
                     wordWrap="CJK", spaceAfter=1)
SUB = ParagraphStyle("SUB", fontName="DJ", fontSize=8.5, leading=11, textColor=GRIS, spaceAfter=4)
NOTE = ParagraphStyle("NOTE", fontName="DJ-I", fontSize=8, leading=10, textColor=GRIS, spaceBefore=2)


def esc(t): return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
def link(url): return f'<a href="{esc(url)}" color="#1F4E78">{esc(url)}</a>'


def block(idtag, name, sugg, desc, dato, color, fuentes, pend):
    fs = " · ".join(link(u) for u in fuentes) if fuentes else "—"
    parts = [Paragraph(f'<b>[{esc(idtag)}] {esc(name)}</b>  <font size=7 color="#777777">— fuente: {esc(sugg)}</font>', H3),
             Paragraph(esc(desc), DESC),
             Paragraph(f'<b>Dato encontrado:</b> <font color="{color.hexval() if hasattr(color,"hexval") else color}">{esc(dato)}</font>', BODY),
             Paragraph(f'<b>Fuente(s):</b> {fs}', SRC)]
    if pend:
        parts.append(Paragraph(f'<b><font color="#9A6700">Pendiente / dudas:</font></b> {esc(pend)}', BODY))
    parts.append(Spacer(1, 3))
    return KeepTogether(parts)

C = {"ok": VERDE, "partial": AMBAR, "manual": ROJO, "na": ROJO}

# ---------- BLOQUE ECONÓMICO (11 indicadores) ----------
ECON = [
 ("70","Empresas de IA","ETO CAT","Nº de empresas de IA del país (en el índice, per millón hab.)."),
 ("71","Número de inversiones privadas","ETO/Crunchbase","Nº de transacciones de inversión privada (VC, PE, M&A) en empresas de IA; última década; per cápita."),
 ("72","Valor total estimado de la inversión privada","ETO/Crunchbase","Valor USD estimado de esas inversiones; última década; per cápita."),
 ("73","Gasto en I+D / PIB","CEPAL → oficial/multinacional","Gasto interno en I+D como % del PIB."),
 ("76","Desarrollo de aplicaciones","GSMA MCI","'Locally developed apps per person' (score 0–100; Content & Services / Local Relevance)."),
 ("80","Relevancia de Producción de Software","GitHub","Inbounds recibidos / repositorios (acumulado). Dos versiones: total y solo 2025."),
 ("81","Desarrollo de IA","Hugging Face","Nº de modelos públicos atribuibles al país (vía organizaciones)."),
 ("82","Familias de Patentes de IA","Espacenet / OECD.AI","Nº de familias de patentes de IA (nivel familia; país de primera presentación)."),
 ("83","Aplicantes de Patentes de IA","Espacenet","Nº de entidades (empresas/universidades/personas) solicitantes de patentes de IA."),
 ("84","Inventores de Patentes de IA","Espacenet","Nº de personas inventoras en patentes de IA."),
 ("92","Gobierno Digital (OSI)","ONU E-Gov","Online Service Index (OSI), componente del EGDI 2024 (0–1)."),
]
CAT="https://cat.eto.tech/"; HF="https://huggingface.co/"; LENS="https://www.lens.org/"
WBOSI="https://data360.worldbank.org/en/dataset/UN_EGDI"
GH="https://github.com/github/innovationgraph"; MCI="https://www.mobileconnectivityindex.com/"
def na(): return ("NO OBTENIBLE desde el entorno (extracción manual)","manual")
ECON_CELLS = {
 "España (ES)": {
  "70": na()+([CAT],"Extraer en cat.eto.tech → dataset Investment → país."),
  "71": na()+([CAT],"Idem (conteo de inversiones)."),
  "72": na()+([CAT],"Idem (valor estimado USD)."),
  "73": ("1,50 % (2024)","ok",["https://www.ine.es/dyngs/Prensa/en/IMASD2024.htm"],"Listo. Eurostat ~1,49–1,50 como contraste."),
  "76": ("89,30 (2024; score 0–100)","ok",[MCI],"Listo (archivo MCI 2025). Es score, no conteo bruto."),
  "80": ("total 0,03189 · 2025 0,00788","ok",[GH],"Listo (determinístico)."),
  "81": ("NO OBTENIBLE (conteo)","manual",[HF],"Contar modelos (API HF) de: BSC-LT, HPAI-BSC, PlanTL-GOB-ES, projecte-aina, HiTZ, clibrain."),
  "82": ("NO OBTENIDO (pista: < 57)","manual",[CAT],"Extraer en cat.eto.tech → Patent."),
  "83": ("N/D en OECD.AI","na",[LENS],"OECD.AI no publica aplicantes por país → consulta Lens/Espacenet (país del solicitante)."),
  "84": ("N/D en OECD.AI","na",[LENS],"Idem → consulta por país del inventor."),
  "92": ("OSI no obtenido; EGDI clase 'Very High'","manual",[WBOSI],"OSI exacto en Technical Appendix UN / CSV Data360."),
 },
 "Estonia (EE)": {
  "70": na()+([CAT],"Extraer en cat.eto.tech → Investment."),
  "71": na()+([CAT],"Idem."),
  "72": na()+([CAT],"Idem."),
  "73": ("2,0 % (2024)","ok",["https://www.stat.ee/en/node/4565"],"Listo (Statistics Estonia). Cifra redondeada a 1 decimal."),
  "76": ("96,73 (2024)","ok",[MCI],"Listo (MCI 2025)."),
  "80": ("total 0,03571 · 2025 0,00655","ok",[GH],"Listo."),
  "81": ("NO OBTENIBLE (conteo)","manual",[HF],"Org: tartuNLP (+ cuentas individuales)."),
  "82": ("NO OBTENIDO","manual",[CAT],"Extraer en cat.eto.tech (N probablemente pequeño)."),
  "83": ("N/D en OECD.AI","na",[LENS],"Consulta Lens/Espacenet (país del solicitante)."),
  "84": ("N/D en OECD.AI","na",[LENS],"Idem (país del inventor)."),
  "92": ("OSI no obtenido; EGDI 0,97274 (#2)","manual",[WBOSI],"OSI exacto en Technical Appendix UN / Data360."),
 },
 "Singapur (SG)": {
  "70": na()+([CAT],"Extraer en cat.eto.tech → Investment."),
  "71": na()+([CAT],"Idem."),
  "72": na()+([CAT],"Idem."),
  "73": ("2,16 % (2020, WB) / ~1,85 % (2022, OCDE)","partial",["https://data.worldbank.org/indicator/GB.XPD.RSDV.GD.ZS?locations=SG","https://www.a-star.edu.sg/News/national-survey-of-rie"],"Confirmar valor oficial exacto en A*STAR (PDF). Rebasing del PIB genera dispersión."),
  "76": ("100,00 (2024)","ok",[MCI],"Listo (MCI 2025). Saturado en el tope de escala."),
  "80": ("total 0,02589 · 2025 0,00822 (sin 'EU' 0,02358/0,00757)","ok",[GH],"Listo. Decidir si excluir el agregado 'EU'."),
  "81": ("NO OBTENIBLE (conteo)","manual",[HF],"Orgs: aisingapore, Sea AI Lab (sail), NUS."),
  "82": ("661 sol. / 297 conc. (2017-2020)","partial",["https://cset.georgetown.edu/publication/examining-singapores-ai-progress/"],"Dato antiguo (2017-2020); actualizar en cat.eto.tech."),
  "83": ("N/D en OECD.AI","na",[LENS],"Consulta Lens/Espacenet (país del solicitante)."),
  "84": ("N/D en OECD.AI","na",[LENS],"Idem (país del inventor)."),
  "92": ("OSI no obtenido; EGDI 0,96912 (#3)","manual",[WBOSI],"OSI exacto en Technical Appendix UN / Data360."),
 },
 "Alemania (DE)": {
  "70": na()+([CAT],"Extraer en cat.eto.tech → Investment."),
  "71": na()+([CAT],"Idem."),
  "72": na()+([CAT],"Idem."),
  "73": ("3,13 % (Eurostat) / 3,17 % (Destatis) 2024","ok",["https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20251204-2"],"Listo. Elegir Eurostat (comparable) o Destatis (nacional)."),
  "76": ("94,75 (2024)","ok",[MCI],"Listo (MCI 2025)."),
  "80": ("total 0,08960 · 2025 0,01899","ok",[GH],"Listo."),
  "81": ("NO OBTENIBLE (conteo)","manual",[HF],"Orgs: laion, Aleph-Alpha, DFKI(+SLT), deepset, LeoLM, occiglot* (multinacional)."),
  "82": ("~436 (FRÁGIL)","partial",["https://hai.stanford.edu/ai-index"],"Métrica/año ambiguos (linaje CSET/WIPO vía AI Index 2024). Reconfirmar en cat.eto.tech."),
  "83": ("N/D en OECD.AI","na",[LENS],"Consulta Lens/Espacenet (país del solicitante)."),
  "84": ("N/D en OECD.AI","na",[LENS],"Idem (país del inventor)."),
  "92": ("OSI no obtenido; EGDI ~0,94 (#~12, aprox.)","manual",[WBOSI],"OSI/EGDI exacto en Technical Appendix UN / Data360."),
 },
 "Portugal (PT)": {
  "70": na()+([CAT],"Extraer en cat.eto.tech → Investment."),
  "71": na()+([CAT],"Idem."),
  "72": na()+([CAT],"Idem."),
  "73": ("1,73 % (2024)","ok",["https://www.dgeec.medu.pt/api/ficheiros/694559aac82132f5733eb2da"],"Listo (DGEEC oficial)."),
  "76": ("86,24 (2024)","ok",[MCI],"Listo (MCI 2025)."),
  "80": ("total 0,03280 · 2025 0,00768","ok",[GH],"Listo."),
  "81": ("NO OBTENIBLE (conteo)","manual",[HF],"Org: PORTULAN. OJO: BERTimbau es de Brasil (no contar como PT)."),
  "82": ("NO OBTENIDO","manual",[CAT],"Extraer en cat.eto.tech."),
  "83": ("N/D en OECD.AI","na",[LENS],"Consulta Lens/Espacenet (país del solicitante)."),
  "84": ("N/D en OECD.AI","na",[LENS],"Idem (país del inventor)."),
  "92": ("OSI no obtenido; EGDI s/d","manual",[WBOSI],"OSI y EGDI exacto en fuente UN / Data360."),
 },
}

# ---------- BLOQUE GOBERNANZA (EE/SG) ----------
ISO42="https://www.iso.org/committee/6794475.html?view=participation"
ISO27="https://www.iso.org/committee/45306.html?view=participation"
DLP_EE="https://www.dlapiperdataprotection.com/?t=law&c=EE"; DLP_SG="https://www.dlapiperdataprotection.com/index.html?t=law&c=SG"
GCI="https://www.itu.int/epublications/publication/global-cybersecurity-index-2024"
GIRAI="https://www.global-index.ai"; NRI="https://networkreadinessindex.org"
EMBER="https://ember-energy.org/data/electricity-data-explorer/"
EE_STR=["https://oecd.ai/en/dashboards/national/estonia","https://regulations.ai/regulations/RAI-EE-NA-DAIWPXX-2024"]
SG_STR=["https://www.smartnation.gov.sg/initiatives/national-ai-strategy/","https://file.go.gov.sg/nais2023.pdf"]
PREL="codificado sin el texto primario (PDF 403) → confirmar verbatim con el PDF."
# id, name, desc, [sources], ee(val,status,pend), sg(val,status,pend)
GOV = [
 ("SUB","Visión e Institucionalidad",),
 ("103","Existencia de la estrategia","Estrategia/política nacional de IA vigente, respaldada por institución pública (1 No/2 En proceso/3 Tiene).",None,
   ("3 (Tiene)","ok",""),("3 (Tiene)","ok","")),
 ("104","Antigüedad","Año de publicación de la estrategia vigente (1 No/2 2019-21/3 2022-23/4 2024-25).",None,
   ("4 (White Paper 2024-2030)","ok","Depende de tomar el White Paper 2024-2030 como 'la estrategia'."),
   ("3 (NAIS 2.0 dic-2023)","ok","Si el Update may-2026 cuenta como estrategia nueva → 4.")),
 ("105","Actualización","¿La estrategia se ha actualizado? (1 No/2 En proceso/3 Actualizada o planificada).",None,
   ("3","ok",""),("3","ok","")),
 ("106","Mecanismos de evaluación","¿Método de seguimiento de metas? (1 No/2 Informal/3 Claro).",None,
   ("3","partial",PREL),("3","partial",PREL)),
 ("107","Presupuesto","¿Presupuesto asignado? (1 No/2 Menciona/3 Monto especificado).",None,
   ("3 (€85M 2024-26)","ok","Confirmar que cuenta como presupuesto de la estrategia."),
   ("3 (>S$1.000M/5 años)","ok","")),
 ("108","Hoja de ruta","¿Plan de acción? (1 No/2 Menciona/3 Plan especificado).",None,
   ("3 (Action Plan Kratt)","ok",""),("3 (15 Acciones)","ok","")),
 ("109-118","10 Tópicos de la estrategia (binario 0/1 c/u)","Ética y gobernanza · Infraestructura y tecnología · Desarrollo de capacidades · Datos · Gobierno digital · Industria y emprendimiento · I+D · Cooperación reg./int'l · Perspectiva de género · Sostenibilidad. (1 = recogido + plan de acción).",None,
   ("9 en 1 · Género=0 · Sostenibilidad=1(BAJA)","partial","Rúbrica exige 'aspecto + plan de acción' por tópico → confirmar plan por tópico en el PDF. Género=0 por ausencia de evidencia."),
   ("9 en 1 · Género=0 · Sostenibilidad=1","partial","Idem. Género=0 (búsqueda contaminada por homónimo).")),
 ("119","Participación ciudadana (elaboración)","Mecanismos de participación ciudadana en la creación de la política (1 No … 5 >1 mecanismo).",None,
   ("2 (informal)","partial","Se apoya en debate 'kratt law' 2017-19, anterior a la estrategia 2024."),
   ("1 (No)","partial","La consulta hallada fue del MGF GenAI, no de NAIS 2.0.")),
 ("121","Multistakeholder (elaboración)","Stakeholders en la creación (1 Solo gob … 5 Gob+4).",None,
   ("3 (Gob+2)","partial",PREL),("3 (Gob+2)","partial",PREL)),
 ("122","Multistakeholder (implementación)","Stakeholders en la implementación (1 Solo gob … 5 Gob+4).",None,
   ("4 (Gob+3)","partial",PREL),("4 (Gob+3)","partial",PREL)),
 ("123","Existencia de institucionalidad","Entidad pública con mandato de liderar/coordinar la política de IA (1 No … 5 >1 institución).",None,
   ("5 (MKM/MEAC, Riigikantselei, RIA, Eesti.ai)","ok",""),
   ("5 (SNDGG, IMDA, AISG, PDPC, AI Verify, NAIC)","ok","Verificar fecha/mandato del NAIC (feb-2026).")),
 ("124","Coordinación interinstitucional","Mecanismo de coordinación (1 No/2 Informal/3 Mecanismo claro).",None,
   ("3","ok",""),("3","ok","")),
 ("SUB","Vinculación Internacional",),
 ("125","ISO/IEC JTC 1/SC 42 (IA)","Membresía del organismo nacional (0 No/1 Observador/2 Participante).",[ISO42],
   ("0 (No participa)","partial","DUDA PRINCIPAL EE: no figura en la lista; confianza MEDIA → verificar en iso.org."),
   ("2 (Participante)","ok","")),
 ("126","ISO/IEC JTC 1/SC 27 (Seguridad)","Membresía (0/1/2).",[ISO27],
   ("2 (Participante)","ok",""),("2 (Participante)","ok","")),
 ("127","Acuerdos/comités internacionales de IA","Incorporación a acuerdos (0 ninguno/1 uno/2 dos o más).",None,
   ("2 (OECD AI Principles + EU Coordinated Plan + CoE vía UE)","ok","GPAI: EE no es miembro."),
   ("2 (ASEAN + OECD + UNESCO ref.)","ok","Verificar adhesión formal a OECD AI Principles y membresía GPAI.")),
 ("SUB","Regulación",),
 ("128","Iniciativa legal sobre IA","Proyectos/leyes de IA (1 No/2 Borrador/3 Sí tiene).",None,
   ("3 (EU AI Act)","ok","Decisión metodológica: cómo puntuar el EU AI Act en países UE (no hay ley nacional propia)."),
   ("1 (soft law, sin ley dura)","ok","Correcto por rúbrica, pero NO es debilidad: marcos voluntarios muy maduros. Sugerir nota cualitativa.")),
 ("129","Clasificación de riesgo de sistemas de IA","¿La iniciativa legal clasifica riesgo? (0 No/1 Sí).",None,
   ("1 (EU AI Act)","ok",""),("1 (en marco voluntario)","partial","Se sostiene sobre el marco, no una ley → confirmar criterio.")),
 ("130","Exploración regulatoria / sandbox","¿Se contempla sandbox? (0 No/1 Sí).",None,
   ("1 (sandbox EE-FI)","ok",""),("1 (AI Verify)","ok","")),
 ("131","Ley de protección de datos personales","¿Ley vigente? (0 No/1 Sí).",[DLP_EE,DLP_SG],
   ("1 (GDPR + PDPA)","ok",""),("1 (PDPA 2012)","ok","")),
 ("132","Autoridad de protección de datos","¿Autoridad de fiscalización? (0 No/1 Sí).",None,
   ("1 (AKI — aki.ee)","ok",""),("1 (PDPC — pdpc.gov.sg)","ok","")),
 ("SUB","IA Ética, Responsable y Segura",),
 ("133-137","Ciberseguridad — 5 pilares (GCI 2024)","Legal · Técnico · Organizacional · Desarrollo de capacidades · Cooperación (0–100 c/u; en GCI cada pilar /20).",[GCI],
   ("PENDIENTE (Tier 1; total ~95,04)","manual","Los 5 pilares por país están en el anexo PDF del GCI 2024 (403). Total de fuente secundaria."),
   ("PENDIENTE (Tier 1; total ~99,86)","manual","Idem.")),
 ("138","GIRAI — Protección de datos y privacidad","Puntaje 0–100 (pilar Derechos Humanos).",[GIRAI],
   ("NO ENCONTRADO","manual","En portal JS / figuras PDF → extracción manual (portal GIRAI)."),
   ("NO ENCONTRADO","manual","Idem. (SG también en Fig.19 informe LIRNEasia).")),
 ("139","GIRAI — Seguridad, precisión y confiabilidad","Puntaje 0–100 (pilar Gobernanza de IA Responsable).",[GIRAI],
   ("NO ENCONTRADO","manual","Extracción manual (portal GIRAI)."),
   ("NO ENCONTRADO","manual","Idem.")),
 ("144","Energía limpia y asequible (NRI)","Indicador 'Affordable & clean energy' del Network Readiness Index.",[NRI],
   ("80,71 (ed. 2025)","ok","Confirmar edición (2024 vs 2025)."),
   ("86,87 (ed. 2025)","ok","Confirmar edición.")),
 ("145","% ERNC en matriz eléctrica (EMBER)","% de generación eléctrica renovable (ERNC ≈ renovables; hidro ~0).",[EMBER],
   ("55,75 % (2024) / 59,57 % (2025)","ok","Determinístico. EMBER no separa 'no convencional'/gran hidro (marginal aquí)."),
   ("4,93 % (2024) / 5,49 % (2025)","ok","Determinístico.")),
]

def build():
    story = [Paragraph("ILIA 2026 — Indicadores recolectados por país", H1),
             Paragraph("Borrador de trabajo para llenar la planilla oficial · 2026-06-14 · "
                       "Países: España, Estonia, Singapur, Alemania, Portugal (económicos); "
                       "Estonia y Singapur (gobernanza). Detalle y más fuentes en data/paises_extra/.", SUB),
             Paragraph("Estados: <font color='#1A7F37'>verde</font>=listo · "
                       "<font color='#9A6700'>ámbar</font>=parcial/PRELIM · "
                       "<font color='#B42318'>rojo</font>=no obtenido / extracción manual.", SUB),
             HRFlowable(width="100%", color=AZUL, thickness=1.1, spaceAfter=4)]
    govd = {g[0]: g for g in GOV if g[0] != "SUB"}
    for ci, (country, cells) in enumerate(ECON_CELLS.items()):
        if ci: story.append(PageBreak())
        story.append(Paragraph(country, H1))
        story.append(Paragraph("A. Investigación, adopción y desarrollo (11 indicadores)", H2))
        for idt, name, sugg, desc in ECON:
            dato, status, fuentes, pend = cells[idt]
            story.append(block(idt, name, sugg, desc, dato, C[status], fuentes, pend))
        if country.startswith(("Estonia", "Singapur")):
            isEE = country.startswith("Estonia")
            story.append(Spacer(1, 4))
            story.append(Paragraph("B. Gobernanza (38 subindicadores)", H2))
            for g in GOV:
                if g[0] == "SUB":
                    story.append(Paragraph(g[1], H3)); continue
                idt, name, desc, src = g[1-1], g[1], g[2], g[3]
                idt = g[0]
                cell = g[4] if isEE else g[5]
                val, status, pend = cell
                fuentes = src if src else []
                story.append(block(idt, name, sugg="ver RUBRICAS/FUENTES", desc=desc,
                                   dato=val, color=C[status], fuentes=fuentes, pend=pend))
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Indicadores_ILIA2026_por_pais.pdf")
    SimpleDocTemplate(out, pagesize=A4, topMargin=1.2*cm, bottomMargin=1.2*cm,
                      leftMargin=1.4*cm, rightMargin=1.4*cm,
                      title="ILIA 2026 — Indicadores por país").build(story)
    print("OK ->", out)

if __name__ == "__main__":
    build()
