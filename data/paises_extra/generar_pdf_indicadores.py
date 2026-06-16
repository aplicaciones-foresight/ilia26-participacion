#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera un PDF de trabajo con los indicadores recolectados por país (ILIA 2026)."""
import os, re
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (Paragraph, SimpleDocTemplate, Spacer, HRFlowable,
                                KeepTogether, PageBreak)
from datos_gobernanza import G, st, GOB_META, gov_sources, COUNTRY_GIDX  # gobernanza 5 países (fuente única)

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


def block(idtag, name, sugg, desc, dato, color, fuentes, pend, notelabel="Pendiente / dudas"):
    fs = " · ".join(link(u) for u in fuentes) if fuentes else "—"
    parts = [Paragraph(f'<b>[{esc(idtag)}] {esc(name)}</b>  <font size=7 color="#777777">— fuente: {esc(sugg)}</font>', H3),
             Paragraph(esc(desc), DESC),
             Paragraph(f'<b>Dato encontrado:</b> <font color="{color.hexval() if hasattr(color,"hexval") else color}">{esc(dato)}</font>', BODY),
             Paragraph(f'<b>Fuente(s):</b> {fs}', SRC)]
    if pend:
        parts.append(Paragraph(f'<b><font color="#9A6700">{esc(notelabel)}:</font></b> {esc(pend)}', BODY))
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

# ---------- BLOQUE GOBERNANZA (5 países) ----------
# La matriz de gobernanza (38 subindicadores × 5 países) y sus metadatos viven en
# datos_gobernanza.py (fuente única que también alimenta la planilla .xlsx).

def build():
    story = [Paragraph("ILIA 2026 — Indicadores recolectados por país", H1),
             Paragraph("Borrador de trabajo para llenar la planilla oficial · 2026-06-16 · "
                       "Económicos (11 indicadores) y Gobernanza (38 subindicadores) para los 5 países: "
                       "España, Estonia, Singapur, Alemania, Portugal. Detalle y más fuentes en data/paises_extra/.", SUB),
             Paragraph("Estados: <font color='#1A7F37'>verde</font>=listo · "
                       "<font color='#9A6700'>ámbar</font>=parcial/PRELIM/duda · "
                       "<font color='#B42318'>rojo</font>=no obtenido / extracción manual.", SUB),
             HRFlowable(width="100%", color=AZUL, thickness=1.1, spaceAfter=4)]
    for ci, (country, cells) in enumerate(ECON_CELLS.items()):
        if ci: story.append(PageBreak())
        cc = country.split("(")[1].rstrip(")")          # "España (ES)" -> "ES"
        gidx = COUNTRY_GIDX[cc]
        story.append(Paragraph(country, H1))
        story.append(Paragraph("A. Investigación, adopción y desarrollo (11 indicadores)", H2))
        for idt, name, sugg, desc in ECON:
            dato, status, fuentes, pend = cells[idt]
            story.append(block(idt, name, sugg, desc, dato, C[status], fuentes, pend))
        story.append(Spacer(1, 4))
        story.append(Paragraph("B. Gobernanza (38 subindicadores)", H2))
        for row in G:
            sub, ind, nota, val = row[0], row[1], row[8], row[gidx]
            if sub:
                story.append(Paragraph(sub, H3))
            m = re.search(r"\((\d+)\)", ind)
            idt = m.group(1) if m else ""
            name = re.sub(r"\s*\(\d+\)\s*$", "", ind)
            desc, srckind = GOB_META.get(idt, (ind, "estrategia"))
            story.append(block(idt, name, sugg="rúbrica / detalle por país",
                               desc=desc, dato=val, color=C[st(val)],
                               fuentes=gov_sources(srckind, cc), pend=nota,
                               notelabel="Nota / banderas"))
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Indicadores_ILIA2026_por_pais.pdf")
    SimpleDocTemplate(out, pagesize=A4, topMargin=1.2*cm, bottomMargin=1.2*cm,
                      leftMargin=1.4*cm, rightMargin=1.4*cm,
                      title="ILIA 2026 — Indicadores por país").build(story)
    print("OK ->", out)

if __name__ == "__main__":
    build()
