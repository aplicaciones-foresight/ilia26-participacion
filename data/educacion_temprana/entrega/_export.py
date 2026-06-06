#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Renderiza el documento final a PDF (fpdf2, pure-python) y DOCX (htmldocx).
LibreOffice/xhtml2pdf no son utilizables en este entorno; fpdf2 no lanza procesos
externos y usa fuentes Unicode (Liberation Sans + DejaVu Mono).
Uso: python data/educacion_temprana/entrega/_export.py  (tras _build_pdf.py)"""
import pathlib, re, markdown

OUT = pathlib.Path(__file__).resolve().parent
md = (OUT / "INFORME_FINAL_2026-06-06.md").read_text(encoding="utf-8")
EXT = ["tables", "fenced_code", "sane_lists"]

# ---------- DOCX (htmldocx, alta fidelidad, conserva formato en celdas) ----------
try:
    from htmldocx import HtmlToDocx
    from docx import Document
    doc = Document()
    HtmlToDocx().add_html_to_document(markdown.markdown(md, extensions=EXT), doc)
    p = OUT / "INFORME_FINAL_2026-06-06.docx"; doc.save(p)
    print(f"DOCX OK -> {p.name} ({p.stat().st_size} b)")
except Exception as e:
    print("DOCX FAIL:", e)

# ---------- PDF (fpdf2) ----------
md_pdf = md
for a, b in {"├──": "|- ", "└──": "`- ", "│": "|", "├": "|", "└": "`", "─": "-",
             "⇒": "=>", "≈": "~", "≤": "<=", "≥": ">="}.items():
    md_pdf = md_pdf.replace(a, b)

# fpdf2.write_html no admite tags anidados (<strong>/<em>/<code>/<a>) dentro de <td>/<th>:
# los quitamos SOLO dentro de celdas (el texto se conserva; el DOCX sí lleva el formato).
_CELL = re.compile(r"<(t[dh])(?:\s[^>]*)?>(.*?)</\1>", re.DOTALL)
_INLINE = re.compile(r"</?(?:strong|em|code|b|i|a)(?:\s[^>]*)?>")
def clean_cells(html):
    return _CELL.sub(lambda m: f"<{m.group(1)}>" + _INLINE.sub("", m.group(2)) + f"</{m.group(1)}>", html)

try:
    from fpdf import FPDF
    LIB = "/usr/share/fonts/truetype/liberation/"
    DJV = "/usr/share/fonts/truetype/dejavu/"
    pdf = FPDF(format="A4")
    pdf.set_margins(18, 15, 18)
    pdf.set_auto_page_break(True, margin=15)
    pdf.add_font("Lib", "",   LIB + "LiberationSans-Regular.ttf")
    pdf.add_font("Lib", "B",  LIB + "LiberationSans-Bold.ttf")
    pdf.add_font("Lib", "I",  LIB + "LiberationSans-Italic.ttf")
    pdf.add_font("Lib", "BI", LIB + "LiberationSans-BoldItalic.ttf")
    pdf.add_font("LibMono", "",  DJV + "DejaVuSansMono.ttf")
    pdf.add_font("LibMono", "B", DJV + "DejaVuSansMono-Bold.ttf")
    pdf.set_font("Lib", size=10)
    hs = {"h1": 17, "h2": 13, "h3": 11.5, "h4": 11, "h5": 10, "h6": 10}

    def render(html):
        try:
            pdf.write_html(html, font_family="Lib", pre_code_font="LibMono", heading_sizes=hs)
        except TypeError:
            pdf.write_html(html, font_family="Lib")

    import warnings; warnings.filterwarnings("ignore", category=DeprecationWarning)
    fails = 0
    for part in md_pdf.split('<div class="pb"></div>'):
        pdf.add_page()
        try:
            render(clean_cells(markdown.markdown(part, extensions=EXT)))
        except Exception as e:
            fails += 1; print("  section FAIL:", e)
    p = OUT / "INFORME_FINAL_2026-06-06.pdf"
    pdf.output(str(p))
    print(f"PDF OK -> {p.name} ({p.stat().st_size} b, {pdf.pages_count} pp, {fails} fallos)")
except Exception as e:
    import traceback; print("PDF FAIL:", e); traceback.print_exc()
