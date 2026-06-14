#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
export_planilla_validacion.py — Planilla SIMPLE de validación en equipo.

Una sola hoja, un caso por fila, en 3 bloques (columna "Bloque"):
  1. NUEVOS / dudosos  — hallazgos cuya elegibilidad hay que decidir.
  2. Baseline 2025     — casos del índice 2025: ratificar que siguen en 2026.
  3. Excluido (revisar) — excluidos en 2025 que podrían reingresar (ver
                          src/analizar_reingreso.py).
Una columna por revisor (SI/NO/DUDA) + "¿Coinciden?" (verde DE ACUERDO / rojo
DISCUTIR) para discutir solo los desacuerdos. Todos evalúan todos los casos.

Salida: data/gates/planilla_validacion_ILIA2026.xlsx
"""
from __future__ import annotations
import csv
import os
import sys
import unicodedata

import openpyxl
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


def _norm(s):
    s = "".join(c for c in unicodedata.normalize("NFKD", str(s)) if not unicodedata.combining(c))
    return s.lower().strip()


def _hint(notas):
    drop = ("fuente=", "año baseline", "año=")
    parts = [p.strip() for p in (notas or "").split(";")]
    parts = [p for p in parts if p and not any(p.lower().startswith(d) for d in drop)]
    return "; ".join(parts)


def _read_csv(path):
    p = os.path.join(ROOT, path)
    if not os.path.exists(p):
        return []
    with open(p, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def _bbdd_desc():
    """caso(normalizado) -> (descripción breve, link) desde la BBDD 2025."""
    wb = openpyxl.load_workbook(os.path.join(ROOT, "data/baseline/BBDD_IA_Participacion_2025.xlsx"), data_only=True)
    ws = wb["BBDD Casos"]
    out = {}
    for row in ws.iter_rows(min_row=2, max_row=ws.max_row, values_only=True):
        if not row[0] or not row[1]:
            continue
        caso = str(row[1]).strip()
        desc = str(row[4]).strip() if row[4] else ""
        link = ""
        for i in (21, 20, 22):
            if len(row) > i and row[i] and str(row[i]).strip():
                link = str(row[i]).strip(); break
        out[_norm(caso)] = (desc, link)
    return out


def construir_filas():
    cand = _read_csv("data/candidatos/candidatos.csv")
    desc = _bbdd_desc()
    filas = []  # (orden, Bloque, País, Caso, Tipo, Qué es, A verificar, Enlace)

    # Bloque 1: NUEVOS / dudosos
    for r in cand:
        tb = r["tipo_baseline"]
        if not str(tb).startswith("nuevo"):
            continue
        tipo = "NUEVO" if tb == "nuevo" else "dudoso"
        enlace = r["urls"].split("|")[0].strip() if r["urls"] else ""
        filas.append((0 if tb == "nuevo" else 1, "1. NUEVOS / dudosos", r["pais"],
                      r["nombre_tentativo"], tipo, r["senal"], _hint(r["notas"]), enlace))

    # Bloque 2: Baseline 2025 (activos)
    for r in cand:
        if r["tipo_baseline"] != "activo_2025":
            continue
        reverif = "reconfirmado web" in (r["notas"] or "")
        tipo = "Baseline (reverif. 2026)" if reverif else "Baseline 2025"
        d, link = desc.get(_norm(r["nombre_tentativo"]), ("", ""))
        quees = d or r["senal"]
        verificar = ("Ratificar que sigue activo en 2026 y recodificar (convocante/nivel). "
                     + ("Hay señal de actividad 2026." if reverif else "Falta señal de actividad 2026."))
        enlace = link or (r["urls"].split("|")[0].strip() if r["urls"] else "")
        filas.append((2, "2. Baseline 2025", r["pais"], r["nombre_tentativo"], tipo,
                      quees, verificar, enlace))

    # Bloque 3: Excluidos a revisar (reingreso)
    for r in _read_csv("data/candidatos/excluidos_revisar.csv"):
        quees = r.get("por_que_revisar", "")
        verificar = f"Motivo exclusión 2025: {r.get('motivo_2025','')}. Revisar si ahora hay IA sobre el contenido."
        filas.append((3, "3. Excluido (revisar)", r["pais"], r["caso"],
                      "Excluido 2025 (revisar)", quees, verificar, r.get("enlace", "")))

    filas.sort(key=lambda x: (x[0], x[2], x[3]))
    return filas


def main(argv=None):
    filas = construir_filas()
    wb = Workbook(); ws = wb.active; ws.title = "Validación"
    headers = ["Bloque", "País", "Caso", "Tipo", "Qué es y cómo usa IA (evidencia)",
               "A verificar", "Enlace"] + REVISORES + ["¿Coinciden?", "Comentarios para discutir"]
    ws.append(headers)
    for _, bloque, pais, caso, tipo, quees, verif, enlace in filas:
        ws.append([bloque, pais, caso, tipo, quees, verif, enlace, "", "", "", "", ""])
    n = ws.max_row

    # columnas: A Bloque B País C Caso D Tipo E Qué es F A verificar G Enlace
    #           H/I/J revisores  K ¿Coinciden?  L Comentarios
    rev_cols = ["H", "I", "J"]
    for c in range(1, len(headers) + 1):
        cell = ws.cell(row=1, column=c); letter = get_column_letter(c)
        if letter in rev_cols + ["K", "L"]:
            cell.fill = AMBAR; cell.font = DARK_BOLD
        else:
            cell.fill = AZUL; cell.font = WHITE_BOLD
        cell.alignment = CENTER
    ws.row_dimensions[1].height = 30

    widths = [20, 6, 38, 22, 58, 36, 32, 10, 10, 11, 15, 30]
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    for row in range(2, n + 1):
        for col in (3, 5, 6, 7, 12):
            ws.cell(row=row, column=col).alignment = WRAP

    ws.freeze_panes = "D2"
    ws.auto_filter.ref = f"A1:{get_column_letter(len(headers))}{n}"

    dv = DataValidation(type="list", formula1='"SI,NO,DUDA"', allow_blank=True)
    ws.add_data_validation(dv)
    for col in rev_cols:
        dv.add(f"{col}2:{col}{n}")

    for row in range(2, n + 1):
        ws.cell(row=row, column=11).value = (
            f'=IF(COUNTA(H{row}:J{row})<3,"(faltan votos)",'
            f'IF(AND(H{row}=I{row},I{row}=J{row}),"DE ACUERDO","DISCUTIR"))')
        ws.cell(row=row, column=11).alignment = Alignment(horizontal="center")
    ws.conditional_formatting.add(f"K2:K{n}", CellIsRule(operator="equal", formula=['"DISCUTIR"'],
                                  fill=PatternFill("solid", fgColor="FFC7CE")))
    ws.conditional_formatting.add(f"K2:K{n}", CellIsRule(operator="equal", formula=['"DE ACUERDO"'],
                                  fill=PatternFill("solid", fgColor="C6EFCE")))

    dst = os.path.join(ROOT, "data/gates/planilla_validacion_ILIA2026.xlsx")
    wb.save(dst)
    from collections import Counter
    cb = Counter(f[1] for f in filas)
    print(f"[ok] {dst}  ({n-1} casos)")
    for k in sorted(cb):
        print(f"     {k}: {cb[k]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
