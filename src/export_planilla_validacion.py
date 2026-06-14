#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
export_planilla_validacion.py — Planilla SIMPLE de validación en equipo.

Una sola hoja: un caso por fila, una columna por revisor (SI/NO/DUDA) y una
columna "¿Coinciden?" que marca DISCUTIR donde los 3 no están de acuerdo.
Pensada para subir a Google Drive y que los 3 evalúen TODOS los casos.

Salida: data/gates/planilla_validacion_ILIA2026.xlsx
Revisores por defecto: Natalia, Nicole, "Revisor 3" (renombrable en la planilla).
"""
from __future__ import annotations
import csv
import os
import sys

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
REVISORES = ["Natalia", "Nicole", "Revisor 3"]

AZUL = PatternFill("solid", fgColor="1F4E78")
AMBAR = PatternFill("solid", fgColor="FFE699")
WHITE_BOLD = Font(bold=True, color="FFFFFF")
DARK_BOLD = Font(bold=True, color="7F6000")
WRAP = Alignment(wrap_text=True, vertical="top")
CENTER = Alignment(horizontal="center", vertical="center", wrap_text=True)


def _hint(notas: str) -> str:
    drop = ("fuente=", "año baseline", "año=")
    parts = [p.strip() for p in (notas or "").split(";")]
    parts = [p for p in parts if p and not any(p.lower().startswith(d) for d in drop)]
    return "; ".join(parts)


def main(argv=None):
    src = os.path.join(ROOT, "data", "candidatos", "candidatos.csv")
    with open(src, newline="", encoding="utf-8") as fh:
        rows = [r for r in csv.DictReader(fh) if str(r["tipo_baseline"]).startswith("nuevo")]

    def tipo(r):
        return "NUEVO" if r["tipo_baseline"] == "nuevo" else "dudoso"
    rows.sort(key=lambda r: (0 if r["tipo_baseline"] == "nuevo" else 1, r["pais"], r["nombre_tentativo"]))

    wb = Workbook()
    ws = wb.active; ws.title = "Validación"

    headers = ["País", "Caso", "Tipo", "Qué es y cómo usa IA (evidencia)", "A verificar",
               "Enlace"] + REVISORES + ["¿Coinciden?", "Comentarios para discutir"]
    ws.append(headers)

    for r in rows:
        enlace = (r["urls"].split("|")[0].strip() if r["urls"] else "")
        ws.append([r["pais"], r["nombre_tentativo"], tipo(r), r["senal"],
                   _hint(r["notas"]), enlace, "", "", "", "", ""])
    n = ws.max_row

    # columnas: A País B Caso C Tipo D Qué es E A verificar F Enlace
    #           G/H/I revisores  J ¿Coinciden?  K Comentarios
    rev_cols = ["G", "H", "I"]
    # estilo de encabezado
    for c in range(1, len(headers) + 1):
        cell = ws.cell(row=1, column=c)
        letter = get_column_letter(c)
        if letter in rev_cols + ["J", "K"]:
            cell.fill = AMBAR; cell.font = DARK_BOLD
        else:
            cell.fill = AZUL; cell.font = WHITE_BOLD
        cell.alignment = CENTER
    ws.row_dimensions[1].height = 30

    widths = [6, 40, 9, 60, 38, 34, 11, 11, 11, 16, 34]
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    for row in range(2, n + 1):
        for col in (2, 4, 5, 6, 11):
            ws.cell(row=row, column=col).alignment = WRAP

    ws.freeze_panes = "C2"
    ws.auto_filter.ref = f"A1:{get_column_letter(len(headers))}{n}"

    # menús desplegables SI/NO/DUDA para los 3 revisores
    dv = DataValidation(type="list", formula1='"SI,NO,DUDA"', allow_blank=True,
                        showDropDown=False)
    ws.add_data_validation(dv)
    for col in rev_cols:
        dv.add(f"{col}2:{col}{n}")

    # ¿Coinciden? — fórmula (nombres de función en inglés para compatibilidad xlsx/Sheets)
    for row in range(2, n + 1):
        ws.cell(row=row, column=10).value = (
            f'=IF(COUNTA(G{row}:I{row})<3,"(faltan votos)",'
            f'IF(AND(G{row}=H{row},H{row}=I{row}),"DE ACUERDO","DISCUTIR"))')
        ws.cell(row=row, column=10).alignment = Alignment(horizontal="center")

    # resaltar acuerdos/desacuerdos
    ws.conditional_formatting.add(
        f"J2:J{n}", CellIsRule(operator="equal", formula=['"DISCUTIR"'],
                               fill=PatternFill("solid", fgColor="FFC7CE")))
    ws.conditional_formatting.add(
        f"J2:J{n}", CellIsRule(operator="equal", formula=['"DE ACUERDO"'],
                               fill=PatternFill("solid", fgColor="C6EFCE")))

    # nota corta arriba (fila congelada aparte no; usamos un comentario en A1)
    ws["A1"].comment = None

    dst = os.path.join(ROOT, "data", "gates", "planilla_validacion_ILIA2026.xlsx")
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    wb.save(dst)
    print(f"[ok] {dst}  ({n-1} casos · revisores: {', '.join(REVISORES)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
