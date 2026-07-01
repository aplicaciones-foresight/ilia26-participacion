#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
export_detalle_casos.py — Planilla de DATOS BRUTOS por caso (Fase 2/3, ILIA 2026).

Una fila por caso (~51): baseline 2025 (reutilizado + reverificado + recodificado)
+ candidatos nuevos/dudosos + excluidos a reingreso (investigados en la web con
evidencia verbatim). NO calcula el indicador: solo consolida los datos necesarios
para calcular y clasificar, con marcado de huecos (gaps) y URLs para búsqueda manual.

Entrada : data/fichas/*_detalle.json  (una ficha por caso)
Salidas : data/gates/planilla_detalle_casos_ILIA2026.xlsx  (5 hojas)
          data/candidatos/detalle_casos_ILIA2026.csv        (hoja principal)
"""
from __future__ import annotations
import csv, glob, json, os, sys
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill, Border, Side
from openpyxl.utils import get_column_letter

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

AZUL   = PatternFill("solid", fgColor="1F4E78")
GRIS   = PatternFill("solid", fgColor="D9D9D9")
VERDE  = PatternFill("solid", fgColor="C6EFCE")
ROJO   = PatternFill("solid", fgColor="FFC7CE")
AMBAR  = PatternFill("solid", fgColor="FFEB9C")
AMBARH = PatternFill("solid", fgColor="FFF2CC")
WHITE_BOLD = Font(bold=True, color="FFFFFF")
WRAP   = Alignment(wrap_text=True, vertical="top")
CENTER = Alignment(horizontal="center", vertical="center", wrap_text=True)
TOPLEFT= Alignment(horizontal="left", vertical="top", wrap_text=True)
THIN   = Side(style="thin", color="BFBFBF")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)

BLOQUE_ORDER = {"1-nuevo": 0, "1-dudoso": 1, "4-descubrimiento-amplio": 2,
                "3-excluido-revisar": 3, "2-baseline": 4}
BLOQUE_LABEL = {
    "1-nuevo": "1. Nuevo",
    "1-dudoso": "1. Dudoso",
    "4-descubrimiento-amplio": "4. Descubrimiento amplio (hallazgo nuevo)",
    "3-excluido-revisar": "3. Excluido (revisar reingreso)",
    "2-baseline": "2. Baseline 2025",
}


def j(v):
    """lista -> 'a; b'; None -> ''."""
    if v is None:
        return ""
    if isinstance(v, list):
        return "; ".join(str(x) for x in v if x not in (None, ""))
    return str(v)


def load_fichas():
    out = []
    for f in sorted(glob.glob(os.path.join(ROOT, "data/fichas/*_detalle.json"))):
        try:
            d = json.load(open(f, encoding="utf-8"))
        except Exception as e:
            print(f"[WARN] JSON inválido {os.path.basename(f)}: {e}")
            continue
        d.setdefault("fuente_datos", "web_2026")
        out.append(d)
    out.sort(key=lambda d: (BLOQUE_ORDER.get(d.get("bloque", ""), 9),
                            str(d.get("pais") or ""), str(d.get("nombre_caso") or "")))
    return out


def urls_busqueda_manual(d):
    urls = []
    for g in d.get("gaps", []) or []:
        u = (g.get("url_para_buscar") or "").strip()
        if u and u not in urls:
            urls.append(u)
    for s in d.get("fuentes", []) or []:
        est = str(s.get("estado", "")).lower()
        if ("403" in est or "no-encontrado" in est or "error" in est):
            u = (s.get("url") or "").strip()
            if u and u not in urls:
                urls.append(u)
    return urls


# ---- columnas de la hoja principal --------------------------------------
MAIN_COLS = [
    ("Bloque",                 lambda d: BLOQUE_LABEL.get(d.get("bloque",""), d.get("bloque",""))),
    ("caso_id",                lambda d: d.get("caso_id","")),
    ("País",                   lambda d: d.get("pais") or ""),
    ("Caso",                   lambda d: d.get("nombre_caso") or ""),
    ("¿ENTRA? (tentativo)",    lambda d: d.get("entra_tentativo") or ""),
    ("Confianza",              lambda d: d.get("confianza") or ""),
    ("Justificación elegibilidad", lambda d: d.get("justificacion_elegibilidad") or ""),
    ("Proceso participativo",  lambda d: d.get("proceso_participativo") or ""),
    ("Año inicio",             lambda d: j(d.get("ano_inicio"))),
    ("Año cierre",             lambda d: j(d.get("ano_cierre"))),
    ("Estado actividad",       lambda d: d.get("estado_actividad") or ""),
    ("Evidencia actividad 2026", lambda d: d.get("evidencia_actividad_2026") or ""),
    ("Organización a cargo",   lambda d: d.get("organizacion_a_cargo") or ""),
    ("Tipo convocante (7-cat)", lambda d: j(d.get("tipo_convocante"))),
    ("Tipo organización",      lambda d: j(d.get("tipo_organizacion"))),
    ("Tipo de proceso",        lambda d: j(d.get("tipo_proceso"))),
    ("Etapas uso IA",          lambda d: j(d.get("etapas_uso_IA"))),
    ("Continuidad",            lambda d: j(d.get("continuidad"))),
    ("Nivel consolidación (0-3)", lambda d: "" if d.get("nivel_consolidacion") is None else d.get("nivel_consolidacion")),
    ("Sistema(s) de IA",       lambda d: d.get("sistema_IA") or ""),
    ("Tipos / familia de IA",  lambda d: j(d.get("tipos_IA_familia"))),
    ("Usa LLM generativa",     lambda d: d.get("usa_LLM_generativa") or ""),
    ("Función de la IA",       lambda d: d.get("funcion_IA") or ""),
    ("Rol IA (contenido/apoyo)", lambda d: d.get("rol_IA") or ""),
    ("Usa IA en el proceso",   lambda d: d.get("usa_IA_en_proceso") or ""),
    ("Tipo desarrollador IA",  lambda d: j(d.get("tipo_desarrollador_IA"))),
    ("Origen desarrollador",   lambda d: d.get("origen_desarrollador") or ""),
    ("Fuente de datos",        lambda d: d.get("fuente_datos","")),
    ("Nº gaps",                lambda d: len(d.get("gaps",[]) or [])),
    ("URLs para búsqueda manual", lambda d: "\n".join(urls_busqueda_manual(d))),
]

CRIT = ["pais","tipo_proceso","etapas_uso_IA","estado_actividad",
        "nivel_consolidacion","tipo_convocante","usa_IA_en_proceso","rol_IA"]


def style_header(ws, ncols, fill=AZUL, font=WHITE_BOLD, height=34):
    for c in range(1, ncols + 1):
        cell = ws.cell(row=1, column=c)
        cell.fill = fill; cell.font = font; cell.alignment = CENTER; cell.border = BORDER
    ws.row_dimensions[1].height = height
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = f"A1:{get_column_letter(ncols)}{ws.max_row}"


def main():
    fichas = load_fichas()
    wb = Workbook()

    # ---------- Hoja 1: Detalle casos ----------
    ws = wb.active; ws.title = "Detalle casos"
    ws.append([h for h, _ in MAIN_COLS])
    for d in fichas:
        ws.append([fn(d) for _, fn in MAIN_COLS])
    ncols = len(MAIN_COLS)
    style_header(ws, ncols)
    widths = [16,30,6,30,12,26,40,40,9,9,13,40,32,24,16,26,26,14,10,30,24,12,40,16,12,20,16,22,7,46]
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    col = {h: i+1 for i, (h, _) in enumerate(MAIN_COLS)}
    for r in range(2, ws.max_row + 1):
        for c in range(1, ncols + 1):
            ws.cell(row=r, column=c).alignment = WRAP; ws.cell(row=r, column=c).border = BORDER
        # color ENTRA
        ev = ws.cell(row=r, column=col["¿ENTRA? (tentativo)"])
        val = str(ev.value).upper()
        ev.alignment = CENTER
        if val.startswith("SI"): ev.fill = VERDE
        elif val == "NO": ev.fill = ROJO
        elif val == "DUDA": ev.fill = AMBAR
        # confianza shading
        cf = ws.cell(row=r, column=col["Confianza"])
        if str(cf.value).upper().startswith("BAJA"): cf.fill = ROJO
        elif str(cf.value).upper().startswith("MEDIA"): cf.fill = AMBARH
        elif str(cf.value).upper().startswith("ALTA"): cf.fill = VERDE
        # gaps / urls highlight
        gc = ws.cell(row=r, column=col["Nº gaps"]); gc.alignment = CENTER
        if isinstance(gc.value, int) and gc.value > 0: gc.fill = AMBARH
        uc = ws.cell(row=r, column=col["URLs para búsqueda manual"])
        if uc.value: uc.fill = AMBARH

    # ---------- Hoja 2: Evidencia verbatim ----------
    ws2 = wb.create_sheet("Evidencia (verbatim)")
    hdr2 = ["caso_id","País","Caso","¿ENTRA?"] + [f"EV: {c}" for c in CRIT]
    ws2.append(hdr2)
    for d in fichas:
        ev = d.get("evidencia_verbatim", {}) or {}
        ws2.append([d.get("caso_id",""), d.get("pais") or "", d.get("nombre_caso") or "",
                    d.get("entra_tentativo") or ""] + [ev.get(c) or "" for c in CRIT])
    style_header(ws2, len(hdr2))
    for i, w in enumerate([30,6,30] + [10] + [34]*len(CRIT), 1):
        ws2.column_dimensions[get_column_letter(i)].width = w
    for r in range(2, ws2.max_row + 1):
        for c in range(1, len(hdr2) + 1):
            ws2.cell(row=r, column=c).alignment = WRAP; ws2.cell(row=r, column=c).border = BORDER
            v = ws2.cell(row=r, column=c).value
            if c > 4 and (v is None or v == ""):
                ws2.cell(row=r, column=c).fill = AMBARH  # sin cita = revisar

    # ---------- Hoja 3: GAPS (buscar manual) ----------
    ws3 = wb.create_sheet("GAPS (buscar manual)")
    ws3.append(["caso_id","País","Caso","Campo faltante","Motivo","URL para buscar"])
    ngaps = 0
    for d in fichas:
        for g in d.get("gaps", []) or []:
            ws3.append([d.get("caso_id",""), d.get("pais") or "", d.get("nombre_caso") or "",
                        g.get("campo",""), g.get("motivo",""), g.get("url_para_buscar","")])
            ngaps += 1
    style_header(ws3, 6)
    for i, w in enumerate([30,6,28,22,52,46], 1):
        ws3.column_dimensions[get_column_letter(i)].width = w
    for r in range(2, ws3.max_row + 1):
        for c in range(1, 7):
            ws3.cell(row=r, column=c).alignment = WRAP; ws3.cell(row=r, column=c).border = BORDER

    # ---------- Hoja 4: Fuentes ----------
    ws4 = wb.create_sheet("Fuentes")
    ws4.append(["caso_id","País","Caso","URL","Estado fetch","Cita textual"])
    for d in fichas:
        for s in d.get("fuentes", []) or []:
            ws4.append([d.get("caso_id",""), d.get("pais") or "", d.get("nombre_caso") or "",
                        s.get("url",""), s.get("estado",""), s.get("cita","")])
    style_header(ws4, 6)
    for i, w in enumerate([30,6,26,46,16,60], 1):
        ws4.column_dimensions[get_column_letter(i)].width = w
    for r in range(2, ws4.max_row + 1):
        for c in range(1, 7):
            ws4.cell(row=r, column=c).alignment = WRAP; ws4.cell(row=r, column=c).border = BORDER
            est = str(ws4.cell(row=r, column=5).value).lower()
            if "403" in est or "error" in est or "no-encontrado" in est:
                ws4.cell(row=r, column=5).fill = AMBARH

    # ---------- Hoja 5: Alertas ----------
    ws5 = wb.create_sheet("Alertas")
    ws5.append(["caso_id","País","Caso","Alerta"])
    for d in fichas:
        for a in d.get("alertas", []) or []:
            ws5.append([d.get("caso_id",""), d.get("pais") or "", d.get("nombre_caso") or "", a])
    style_header(ws5, 4)
    for i, w in enumerate([30,6,28,90], 1):
        ws5.column_dimensions[get_column_letter(i)].width = w
    for r in range(2, ws5.max_row + 1):
        for c in range(1, 5):
            ws5.cell(row=r, column=c).alignment = WRAP; ws5.cell(row=r, column=c).border = BORDER

    # ---------- Hoja 6: Leyenda ----------
    ws6 = wb.create_sheet("Leyenda")
    leyenda = [
        ["PLANILLA DE DATOS BRUTOS POR CASO — ILIA 2026 (Participación Ciudadana)"],
        ["Fase 2/3: una fila por caso con los datos necesarios para CALCULAR y CLASIFICAR. NO incluye el cálculo del indicador."],
        [""],
        ["Columna '¿ENTRA? (tentativo)'", "SI = cumple criterio (IA sobre el CONTENIDO de aportes en proceso participativo) · NO = no cumple · DUDA = evidencia ambigua · SI* = entra en escenario A; revisar en escenario B"],
        ["Confianza", "ALTA = ≥2 fuentes independientes con cita en campos críticos · MEDIA = 1 fuente sólida · BAJA = indicios / prensa única / sin cita"],
        ["Celdas ámbar (Evidencia verbatim)", "campo crítico SIN cita textual: revisar / buscar manualmente"],
        ["Hoja 'GAPS (buscar manual)'", "cada dato que no se pudo conseguir, con la URL para que el equipo lo busque manualmente"],
        ["Hoja 'Fuentes'", "URLs consultadas + estado del fetch (403/error = bloqueada, contenido recuperado vía búsqueda) + cita"],
        [""],
        ["Taxonomías (valores válidos)"],
        ["tipo_proceso (5)", "Participación Digital | Gobernanza Colaborativa | Mini públicos | Referendos e Iniciativas Populares | Presupuestos Participativos"],
        ["etapas_uso_IA (4)", "Planificación | Implementación | Análisis | Traducción Política"],
        ["tipo_convocante (7)", "gobierno local | gobierno nacional | otra institución pública | empresa | universidad | sociedad civil | organización internacional"],
        ["nivel_consolidacion (0-3)", "0 sin evidencia/anuncio caducado · 1 anuncio/próximamente · 2 uso puntual o plataforma usada una vez · 3 permanente/recurrente (≥2 ediciones)"],
        ["rol_IA", "contenido (procesa aportes) | apoyo (logística/atención) | no-claro"],
        [""],
        ["Exclusiones FIRMES (config 2026, salen siempre)", "CO Descongestión Ingreso Solidario · MX Sufragio Seguro · PE Sistema de cómputo Elecciones 2026"],
        ["Escenario A/B (config)", "A mantiene DO CiudadanIA y CL 'Tenemos que hablar de Chile'; B los retira (marcados SI*)"],
        ["Datos del baseline 2025", "Reutilizados de la BBDD oficial del equipo (validada) + recodificación 2026 + reverificación de actividad 2026."],
    ]
    for row in leyenda:
        ws6.append(row)
    ws6.column_dimensions["A"].width = 42; ws6.column_dimensions["B"].width = 110
    ws6["A1"].font = Font(bold=True, size=13)
    for r in range(1, ws6.max_row + 1):
        for c in (1, 2):
            ws6.cell(row=r, column=c).alignment = TOPLEFT
        ws6.cell(row=r, column=1).font = Font(bold=True)

    dst = os.path.join(ROOT, "data/gates/planilla_detalle_casos_ILIA2026.xlsx")
    wb.save(dst)

    # ---------- CSV (hoja principal) ----------
    csv_dst = os.path.join(ROOT, "data/candidatos/detalle_casos_ILIA2026.csv")
    with open(csv_dst, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow([h for h, _ in MAIN_COLS])
        for d in fichas:
            w.writerow([fn(d) for _, fn in MAIN_COLS])

    # ---------- resumen consola ----------
    from collections import Counter
    cb = Counter(d.get("bloque","?") for d in fichas)
    ce = Counter((d.get("entra_tentativo") or "?").upper().rstrip("*") for d in fichas)
    print(f"[ok] {dst}")
    print(f"[ok] {csv_dst}")
    print(f"     casos: {len(fichas)}  | gaps totales: {ngaps}")
    print(f"     por bloque: {dict(cb)}")
    print(f"     por ENTRA:  {dict(ce)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
