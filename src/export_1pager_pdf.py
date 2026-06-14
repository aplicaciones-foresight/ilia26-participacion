#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
export_1pager_pdf.py — 1-pager de instrucciones de validación (PDF, 1 página).

Acompaña a la planilla simple `planilla_validacion_ILIA2026.xlsx`: los 3 revisores
evalúan TODOS los casos de forma independiente y se discuten los desacuerdos.
Salida: data/gates/INSTRUCCIONES_validacion_ILIA2026.pdf
"""
import os
import sys

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (ListFlowable, ListItem, Paragraph, SimpleDocTemplate,
                                HRFlowable)

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
AZUL = colors.HexColor("#1F4E78")

H1 = ParagraphStyle("H1", fontName="Helvetica-Bold", fontSize=15, leading=17, textColor=AZUL, spaceAfter=2)
SUB = ParagraphStyle("SUB", fontName="Helvetica", fontSize=8.5, leading=11, textColor=colors.HexColor("#555555"), spaceAfter=4)
H2 = ParagraphStyle("H2", fontName="Helvetica-Bold", fontSize=10.5, leading=12, textColor=AZUL, spaceBefore=6, spaceAfter=2)
BODY = ParagraphStyle("BODY", fontName="Helvetica", fontSize=9, leading=11.5, spaceAfter=2)
BULL = ParagraphStyle("BULL", fontName="Helvetica", fontSize=9, leading=11.5)
NOTE = ParagraphStyle("NOTE", fontName="Helvetica-Oblique", fontSize=8.3, leading=10.5, textColor=colors.HexColor("#444444"), spaceBefore=2)


def bullets(items):
    return ListFlowable([ListItem(Paragraph(t, BULL), leftIndent=10, value="•") for t in items],
                        bulletType="bullet", start="•", leftIndent=12, spaceAfter=2)


def build():
    s = []
    s.append(Paragraph("ILIA 2026 · Validación de casos de IA en Participación Ciudadana", H1))
    s.append(Paragraph("Guía rápida para <b>Natalia</b>, <b>Nicole</b> y el <b>3er revisor</b> — planilla "
                       "<b>planilla_validacion_ILIA2026</b> (Google Sheets)", SUB))
    s.append(HRFlowable(width="100%", thickness=1, color=AZUL, spaceAfter=4))

    s.append(Paragraph("1) Qué les pedimos", H2))
    s.append(Paragraph("Cada uno de los <b>3 revisores evalúa, por su cuenta, TODOS los casos</b> de la planilla "
                       "(~18 filas) y decide si el caso <b>ENTRA</b> al índice 2026. Cada quien escribe en "
                       "<b>su propia columna</b> (Natalia / Nicole / 3er revisor). No hace falta repartirse: "
                       "todos miran todo; después discutimos solo donde no coincidamos.", BODY))

    s.append(Paragraph("2) El criterio (lo único que decide)", H2))
    s.append(Paragraph("<b>ENTRA</b> si, <b>dentro de un proceso participativo</b> (consulta pública, plan de "
                       "desarrollo, presupuesto participativo, asamblea/cabildo, iniciativa o referendo, diálogo "
                       "ciudadano), se usa <b>IA sobre el CONTENIDO de los aportes</b> de la gente: recolectar, "
                       "<b>clasificar, analizar/agrupar por temas, sintetizar</b>, mediar o personalizar. El tema "
                       "del proceso da igual; importa que la IA procese lo que la ciudadanía aporta.", BODY))

    s.append(Paragraph("3) Qué NO entra (excluir)", H2))
    s.append(bullets([
        "Chatbots de <b>atención</b>, preguntas frecuentes o trámites.",
        "IA de <b>conteo o integridad electoral</b>.",
        "<b>Votación</b> entre opciones cerradas (sin texto libre que se analice).",
        "Herramientas o plataformas <b>sin IA</b>.",
        "Consultas <b>SOBRE</b> la IA que no usan IA en su proceso.",
        "<b>Encuestas</b> de opinión; y estudios o prototipos <b>no desplegados</b>.",
    ]))
    s.append(Paragraph("Regla de la prensa: una nota periodística es solo <b>señal</b> &#8594; marquen "
                       "<b>DUDA</b>; la evidencia firme es institucional.", NOTE))

    s.append(Paragraph("4) Cómo votar cada caso (≈5–10 min)", H2))
    s.append(Paragraph("En cada fila lean <b>“Qué es y cómo usa IA”</b> y <b>“A verificar”</b>, y abran el "
                       "<b>Enlace</b>. Luego, en <b>su</b> columna, elijan del menú:", BODY))
    s.append(bullets([
        "<b>SI</b> = cumple el criterio (la IA procesa el contenido de los aportes).",
        "<b>NO</b> = cae en alguna exclusión.",
        "<b>DUDA</b> = falta evidencia para decidir (anoten por qué en “Comentarios”).",
    ]))
    s.append(Paragraph("Voten de forma independiente (sin mirar la columna del otro). Usen <b>Comentarios para "
                       "discutir</b> para dejar el porqué o qué falta confirmar.", BODY))

    s.append(Paragraph("5) Qué pasa con los desacuerdos", H2))
    s.append(Paragraph("La columna <b>¿Coinciden?</b> se calcula sola: queda en <b>verde “DE ACUERDO”</b> si los "
                       "3 votaron igual, o en <b>rojo “DISCUTIR”</b> si hay diferencias. En la reunión revisamos "
                       "solo las filas en rojo.", BODY))

    s.append(Paragraph("6) Cuándo terminamos", H2))
    s.append(Paragraph("Cuando los <b>3</b> hayan votado <b>todas</b> las filas. Avísennos y juntamos las "
                       "decisiones: los SI acordados pasan a la <b>Fase 2</b> (extracción con evidencia textual); "
                       "los “DISCUTIR” se resuelven en la reunión. Dudas de criterio: escríbannos.", BODY))
    return s


def main(argv=None):
    dst = os.path.join(ROOT, "data", "gates", "INSTRUCCIONES_validacion_ILIA2026.pdf")
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    doc = SimpleDocTemplate(dst, pagesize=A4, leftMargin=1.6*cm, rightMargin=1.6*cm,
                            topMargin=1.4*cm, bottomMargin=1.2*cm, title="ILIA 2026 — Validación")
    doc.build(build())
    print(f"[ok] {dst}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
