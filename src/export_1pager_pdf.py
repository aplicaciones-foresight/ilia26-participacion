#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
export_1pager_pdf.py — Genera el 1-pager de instrucciones de validación (PDF).

Salida: data/gates/INSTRUCCIONES_validacion_ILIA2026.pdf
Una sola página, para compartir con el equipo de validación (Gate 1/Gate 2).
"""
import os
import sys

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (ListFlowable, ListItem, Paragraph, SimpleDocTemplate,
                                Spacer, HRFlowable)

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
AZUL = colors.HexColor("#1F4E78")
AMBAR = colors.HexColor("#7F6000")

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
    story = []
    story.append(Paragraph("ILIA 2026 · Validación de casos de IA en Participación Ciudadana", H1))
    story.append(Paragraph("Guía rápida para <b>Natalia</b> y <b>Nicole</b> — planilla "
                           "<b>validacion_candidatos_ILIA2026</b> (Google Sheets)", SUB))
    story.append(HRFlowable(width="100%", thickness=1, color=AZUL, spaceAfter=4))

    story.append(Paragraph("1) Qué les pedimos", H2))
    story.append(Paragraph("Revisar los <b>candidatos</b> que encontró la búsqueda y decidir, caso por caso, "
                           "si el caso <b>ENTRA</b> al índice 2026. Empiecen por los <b>18 prioritarios</b>: en la "
                           "hoja <b>Candidatos</b>, filtren <b>Tipo = NUEVO</b> y <b>NUEVO (dudoso)</b>.", BODY))

    story.append(Paragraph("2) El criterio (lo único que decide)", H2))
    story.append(Paragraph("<b>ENTRA</b> si, <b>dentro de un proceso participativo</b> (consulta pública, plan de "
                           "desarrollo, presupuesto participativo, asamblea/cabildo, iniciativa o referendo, diálogo "
                           "ciudadano), se usa <b>IA sobre el CONTENIDO de los aportes</b> de la gente: recolectar, "
                           "<b>clasificar, analizar/agrupar por temas, sintetizar</b>, mediar o personalizar. El tema "
                           "del proceso da igual; lo que importa es que la IA procese lo que la ciudadanía aporta.", BODY))

    story.append(Paragraph("3) Qué NO entra (excluir)", H2))
    story.append(bullets([
        "Chatbots de <b>atención</b>, preguntas frecuentes o trámites.",
        "IA de <b>conteo o integridad electoral</b>.",
        "<b>Votación</b> entre opciones cerradas (sin texto libre que se analice).",
        "Herramientas o plataformas <b>sin IA</b>.",
        "Consultas <b>SOBRE</b> la IA que no usan IA en su proceso.",
        "<b>Encuestas</b> de opinión; y estudios o prototipos <b>no desplegados</b>.",
    ]))
    story.append(Paragraph("Regla de la prensa: una nota periodística es solo <b>señal</b> &#8594; marquen "
                           "<b>DUDA</b>; la evidencia firme es institucional.", NOTE))

    story.append(Paragraph("4) Cómo hacerlo (≈10–15 min por caso)", H2))
    story.append(Paragraph("En cada fila lean <b>“Señal / evidencia”</b>, <b>“Qué verificar”</b> y abran las "
                           "<b>URLs</b>. Luego completen las <b>columnas en ámbar</b>:", BODY))
    story.append(bullets([
        "<b>¿Elegible?</b>: SI / NO / DUDA.",
        "<b>Decisión</b>: Aprobar Fase 2 / Verificar / Descartar.",
        "<b>Nivel (0–3)</b>: 0 no hay · 1 anuncio · 2 caso puntual · 3 permanente (uso repetido en el tiempo).",
        "<b>Tipo convocante</b>: quién dirige el proceso (gobierno local/nacional, otra institución pública, "
        "empresa, universidad, sociedad civil, organización internacional).",
        "<b>Comentarios</b>: por qué, y qué falta confirmar.",
    ]))
    story.append(Paragraph("Si dudan, marquen <b>DUDA</b> + comentario; no fuercen un valor.", BODY))

    story.append(Paragraph("5) Cómo dividirse el trabajo", H2))
    story.append(Paragraph("Sugerencia: <b>Natalia</b> toma BR, CO, CL, MX; <b>Nicole</b> toma el resto (PA, CU, VE, "
                           "TT, etc.). Den un <b>segundo par de ojos</b> a los marcados DUDA.", BODY))

    story.append(Paragraph("6) Cuándo terminamos", H2))
    story.append(Paragraph("Cuando las <b>18 filas prioritarias</b> tengan ¿Elegible? + Decisión + Comentario. "
                           "Avísennos y seguimos con la <b>Fase 2</b> (extracción con evidencia textual) de los "
                           "aprobados. Dudas de criterio: escríbannos.", BODY))

    return story


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
