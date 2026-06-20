#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Una planilla .xlsx de GOBERNANZA por país (solo los 38 subindicadores de gobernanza),
con: puntaje propuesto, escala/rúbrica, POR QUÉ el puntaje (justificación + confianza) y
TODAS las URLs/fuentes. Fuente única: G + GOB_META (datos_gobernanza) y GOBDET (detalle)."""
import os, re
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from datos_gobernanza import G, st, GOB_META, COUNTRY_GIDX
from datos_gobernanza_detalle import GOBDET

HERE = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(HERE, "por_pais"), exist_ok=True)
ORDER = ["ES", "EE", "SG", "DE", "PT"]
PAIS = {"ES": "España", "EE": "Estonia", "SG": "Singapur", "DE": "Alemania", "PT": "Portugal"}
ASCII = {"ES": "Espana", "EE": "Estonia", "SG": "Singapur", "DE": "Alemania", "PT": "Portugal"}
FECHA = "2026-06-17"

OK = PatternFill("solid", fgColor="C6EFCE"); PART = PatternFill("solid", fgColor="FFEB9C")
MAN = PatternFill("solid", fgColor="FFC7CE"); HDR = PatternFill("solid", fgColor="1F4E78")
SEC = PatternFill("solid", fgColor="2E6FA7"); SUBF = PatternFill("solid", fgColor="DDEBF7")
WHITEB = Font(color="FFFFFF", bold=True, size=10); BOLD = Font(bold=True)
WRAP = Alignment(wrap_text=True, vertical="top"); THIN = Border(*[Side(style="thin", color="D9D9D9")] * 4)
FILLS = {"ok": OK, "partial": PART, "manual": MAN}

def gid(ind):
    m = re.search(r"\((\d+)\)", ind); return m.group(1) if m else ""
def gname(ind):
    return re.sub(r"\s*\(\d+\)\s*$", "", ind)

# Clasificación de cada URL: oficial/primaria (gobierno, BOE/DR, ISO/ITU, OCDE, dato primario)
# vs secundaria (prensa, despachos, agregadores). Las oficiales se listan primero.
_SECUNDARIA = ("cms.law", "publico.pt", "observador.pt", "eco.sapo.pt", "dig.watch", "news.err.ee",
               "statbase.org", "lirneasia.net", "medium.com", "wikipedia.org", "gleichstellungsbericht.de",
               "regulations.ai", "dlapiperdataprotection.com", "artificialintelligenceact.eu", "tiiny.site")
_OFICIAL = (".gov", ".gob.es", ".bund.de", "bundesnetzagentur.de", "bmas.de", "bundesregierung.de",
            "europa.eu", "boe.es", "diariodarepublica.pt", "iso.org", "itu.int", "worldbank.org",
            "networkreadinessindex.org", "global-index.ai", "globalcenter.ai", "ember-energy.org",
            "githubusercontent.com", "oecd.ai", "oecd.org", "unesco.org", "aki.ee", "riigiteataja.ee",
            "riigikantselei.ee", "valitsus.ee", "kratid.ee", "e-estonia.com", "incode2030.gov.pt",
            "anacom.pt", "cnpd.pt", "aepd.es", "bsc.es", "ki-strategie-deutschland.de",
            "plattform-lernende-systeme.de", "acatech.de", "knowledge4policy.ec.europa.eu", "asean.org")

def _tipo(url):
    if any(t in url for t in _SECUNDARIA): return "secundaria"
    if any(t in url for t in _OFICIAL): return "oficial"
    return "secundaria"

def _fuentes_txt(urls):
    ofi = [u for u in urls if _tipo(u) == "oficial"]
    sec = [u for u in urls if _tipo(u) == "secundaria"]
    if not (ofi or sec): return "—"
    return "\n".join([f"[oficial] {u}" for u in ofi] + [f"[secundaria] {u}" for u in sec])

def check_completo():
    """Aborta si falta justificación/fuente para algún subindicador de algún país."""
    ids = [gid(row[1]) for row in G]
    faltan = []
    for cc in ORDER:
        for idt in ids:
            d = GOBDET.get(cc, {}).get(idt)
            if not d or not d[0]:
                faltan.append(f"{cc}/{idt} (sin justificación)")
            elif idt not in ("117",) and not d[2]:
                # 117 (género NO ENCONTRADO) puede no tener URL; el resto debe tener fuente
                if "NO ENCONTRADO" not in (d[0] or "") and "NO se halló" not in (d[0] or ""):
                    faltan.append(f"{cc}/{idt} (sin URL)")
    if faltan:
        raise SystemExit("INCOMPLETO:\n  " + "\n  ".join(faltan))
    print(f"Completitud OK: {len(ids)} subindicadores × {len(ORDER)} países, todos con justificación y fuente.")

def write_xlsx(cc):
    gidx = COUNTRY_GIDX[cc]
    wb = Workbook(); ws = wb.active; ws.title = f"Gobernanza {cc}"[:31]
    ws.cell(1, 1, f"ILIA 2026 — GOBERNANZA — {PAIS[cc]} ({cc}): propuesta detallada por subindicador").font = \
        Font(bold=True, size=14, color="1F4E78")
    ws.cell(2, 1, "Puntaje propuesto por la rúbrica + por qué + fuentes. "
                  "Verde=listo · Ámbar=parcial/PRELIM/duda · Rojo=falta (extracción manual). "
                  f"Generado {FECHA}.").font = Font(size=9)
    ws.cell(3, 1, "Cada URL va etiquetada [oficial] (gobierno, BOE/Diário da República, ISO/ITU, OCDE, dato primario) "
                  "o [secundaria] (prensa, despacho, agregador). Compendio exhaustivo: gobernanza/FUENTES_gobernanza_EE_SG.md "
                  "(EE/SG) · gobernanza_<país>.md, gobernanza_estandares_*.md, etica_seguridad_*.md, energia_*.md (DE/ES/PT). "
                  "Rúbricas: gobernanza/RUBRICAS_gobernanza.md.").font = Font(size=8, italic=True, color="555555")
    headers = ["ID", "Subindicador", "Puntaje\npropuesto", "Escala / rúbrica",
               "Por qué el puntaje (justificación + confianza)", "Fuentes y URLs  ([oficial] primaria · [secundaria] corrobora)"]
    widths = [6, 30, 12, 44, 62, 60]
    hr = 5
    for c, (h, w) in enumerate(zip(headers, widths), 1):
        cell = ws.cell(hr, c, h); cell.fill = HDR; cell.font = WHITEB
        cell.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
        ws.column_dimensions[get_column_letter(c)].width = w
    ws.row_dimensions[hr].height = 30
    r = hr + 1
    for row in G:
        sub, ind, nota, val = row[0], row[1], row[8], row[gidx]
        if sub:
            ws.cell(r, 1, sub); ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=6)
            ws.cell(r, 1).font = BOLD; ws.cell(r, 1).fill = SUBF; ws.cell(r, 1).alignment = WRAP; r += 1
        idt = gid(ind); name = gname(ind)
        rubrica = GOB_META.get(idt, ("", ""))[0]
        just, conf, urls = GOBDET.get(cc, {}).get(idt, ("", "", []))
        porque = just + (f"  [confianza: {conf}]" if conf else "")
        fuentes = _fuentes_txt(urls)
        s = st(val)
        ws.cell(r, 1, idt); ws.cell(r, 2, name).font = BOLD
        ws.cell(r, 3, val).fill = FILLS[s]; ws.cell(r, 4, rubrica)
        ws.cell(r, 5, porque); ws.cell(r, 6, fuentes)
        for c in range(1, 7):
            ws.cell(r, c).border = THIN
            ws.cell(r, c).alignment = Alignment(wrap_text=True, vertical="top",
                                                horizontal="center" if c == 3 else "left")
        ws.row_dimensions[r].height = 56
        r += 1
    ws.freeze_panes = "A6"
    out = os.path.join(HERE, "por_pais", f"Gobernanza_{cc}_{ASCII[cc]}_ILIA2026.xlsx")
    wb.save(out); return out

if __name__ == "__main__":
    check_completo()
    for cc in ORDER:
        print("OK xlsx ->", write_xlsx(cc))
