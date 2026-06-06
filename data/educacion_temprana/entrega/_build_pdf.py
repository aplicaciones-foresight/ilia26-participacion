#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ensambla el documento final (Markdown -> HTML) para exportar a PDF/DOCX con LibreOffice.
Reúne portada + resumen ejecutivo + informe técnico + anexos (fichas, índice, verificación).
Uso:  python data/educacion_temprana/entrega/_build_pdf.py
Luego: soffice --headless --convert-to pdf/docx sobre el HTML resultante."""
import json, pathlib, markdown

BASE = pathlib.Path(__file__).resolve().parents[1]          # data/educacion_temprana
OUT = BASE / "entrega"
def rd(p): return (BASE / p).read_text(encoding="utf-8")
PB = '\n\n<div class="pb"></div>\n\n'                        # salto de página

cover = """# Educación temprana en IA — Subindicador (b) del ILIA

### Revisión curricular de cinco países benchmark
**Portugal · España · Estonia · Alemania · Singapur**

Replicación del subindicador **(b) «Educación temprana en IA»** del índice
**ILIA 2025 (CEPAL/CENIA)** — revisión del currículo escolar oficial vigente (secundaria).

**Resultado:** España, Alemania, Estonia y Singapur = **categoría 5 (100)**; Portugal = **categoría 4 (75)**.
**Promedio del grupo: 95/100** (regla inclusiva; **85** bajo regla estricta).

*Versión verificada verbatim · Fecha de consulta 2026-06-05 · Fecha de verbatim 2026-06-06*
"""

# Anexo C — tabla de verificación a partir del reporte automático
rep = json.loads(rd("fuentes/_verify_report.json"))
rows = ["| id | Cita (subcadena exacta del documento oficial) | Ubicación | Verif. |",
        "|---|---|---|:--:|"]
for it in rep["items"]:
    cita = it["cita"].replace("|", "/")
    cita = cita if len(cita) <= 95 else cita[:93] + "…"
    ub = it["ubicacion"].replace("|", "/")
    ub = ub if len(ub) <= 72 else ub[:70] + "…"
    rows.append(f"| {it['id']} | {cita} | {ub} | {'OK' if it['verbatim_ok'] else 'X'} |")
verif = ("# Anexo C — Verificación verbatim ({ok}/{tot} OK)\n\n"
         "Reporte automático (`fuentes/_verify_report.json`), reproducible con "
         "`python data/educacion_temprana/fuentes/_verify_run.py`.\n\n"
         ).format(ok=rep["ok"], tot=rep["total"]) + "\n".join(rows)

fichas = "\n\n<div class=\"pb\"></div>\n\n".join(rd(f"fichas/{c}.md") for c in ["ES","DE","EE","SG","PT"])

parts = [
    cover,
    rd("RESUMEN_EJECUTIVO.md"),
    rd("informe.md"),
    "# Anexo A — Fichas por país\n\n" + fichas,
    rd("INTEGRACION_INDICE.md"),
    verif,
]
md_text = PB.join(parts)

# Sustituir emojis por texto para evitar 'tofu' en LibreOffice
for a, b in {"🔴": "[A]", "🟡": "[B]", "🟢": "[B]", "✅": "OK", "⚠️": "(!)", "❌": "X", "→": "->"}.items():
    md_text = md_text.replace(a, b)

(OUT / "INFORME_FINAL_2026-06-06.md").write_text(md_text, encoding="utf-8")

body = markdown.markdown(md_text, extensions=["tables", "fenced_code", "sane_lists", "md_in_html"])
CSS = """
@page { size: A4; margin: 2cm; }
body { font-family: 'Liberation Sans','Arial',sans-serif; font-size: 10.5pt; line-height: 1.45; color:#1a1a1a; }
h1 { font-size: 18pt; color:#0b3d6b; border-bottom:2px solid #0b3d6b; padding-bottom:3px; }
h2 { font-size: 13pt; color:#0b3d6b; margin-top:1em; }
h3 { font-size: 11.5pt; color:#444; }
table { border-collapse:collapse; width:100%; margin:.6em 0; font-size:9.3pt; }
th,td { border:1px solid #b9b9b9; padding:4px 7px; vertical-align:top; }
th { background:#eef3f8; text-align:left; }
blockquote { border-left:3px solid #6c9bd2; margin:.5em 0; padding:.2em .9em; background:#f6f9fc; font-style:italic; }
code { background:#f0f0f0; padding:0 3px; }
pre { background:#f6f8fa; padding:8px; border:1px solid #e1e4e8; font-size:9pt; }
a { color:#0b5cad; text-decoration:none; }
hr { border:none; border-top:1px solid #ccc; margin:1em 0; }
.pb { page-break-before: always; }
"""
html = ("<!DOCTYPE html><html lang='es'><head><meta charset='utf-8'>"
        f"<style>{CSS}</style></head><body>{body}</body></html>")
(OUT / "INFORME_FINAL_2026-06-06.html").write_text(html, encoding="utf-8")
print(f"OK: md={len(md_text)} chars, html={len(html)} chars, verif={rep['ok']}/{rep['total']}")
