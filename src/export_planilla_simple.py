#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
export_planilla_simple.py — Planilla SIMPLE (5 pestañas) + guía de validación.

Reorganiza el detalle (data/fichas/*.json) en una planilla fácil de navegar:
  1 · Casos (entran + dudosos)   -> set de trabajo, columnas listas para calcular
  2 · A validar a mano           -> lista de acciones (excluir / resolver DUDA / rescatar / dedup)
  3 · Excluidos                  -> referencia (los que salen, con motivo)
  4 · Evidencia y fuentes        -> cita verbatim por campo crítico + URLs (anti-alucinación)
  5 · Instrucciones              -> guía paso a paso hasta el cálculo

Salidas: data/gates/planilla_ILIA2026_SIMPLE.xlsx
         data/gates/GUIA_validacion_manual_ILIA2026.md
"""
from __future__ import annotations
import glob, json, os, sys
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill, Border, Side
from openpyxl.utils import get_column_letter

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

AZUL=PatternFill("solid",fgColor="1F4E78"); VERDE=PatternFill("solid",fgColor="C6EFCE")
ROJO=PatternFill("solid",fgColor="FFC7CE"); AMBAR=PatternFill("solid",fgColor="FFEB9C")
AMBARH=PatternFill("solid",fgColor="FFF2CC"); GRIS=PatternFill("solid",fgColor="D9D9D9")
WB=Font(bold=True,color="FFFFFF"); WRAP=Alignment(wrap_text=True,vertical="top")
CEN=Alignment(horizontal="center",vertical="center",wrap_text=True)
TL=Alignment(horizontal="left",vertical="top",wrap_text=True)
TH=Side(style="thin",color="BFBFBF"); BOR=Border(left=TH,right=TH,top=TH,bottom=TH)

# --- Reclasificación bajo el CRITERIO CORREGIDO (jul-2026) --------------------
# La PUERTA de entrada es "¿es REALMENTE un proceso de participación ciudadana?",
# NO "¿la IA analiza el contenido?". Si es participación, la IA puede aportar en
# cualquier etapa (incl. logística en Planificación/Implementación: modera,
# administra turnos, prepara materiales, organiza). Se EXCLUYE lo que NO es
# participación: civic tech (reporte/servicio/monitoreo) o voto/conteo electoral.
#
# Los casos frontera (civic tech ↔ participación) son decisión del equipo; aquí
# van con mi recomendación y se pueden cambiar a mano.

# Excluidos CONFIRMADOS (no es proceso de participación / sin IA sobre el contenido):
EXCLUIR = {  # caso_id -> motivo bajo el criterio corregido
 "PE-sistema-de-computo-con-ia-para-las-elecc":"Conteo electoral (OCR de actas): votación política, no participación.",
 "CO-descongestion-de-solicitudes-diarias-del":"Atención ciudadana (triage de 10.000 correos/día): servicio, no participación.",
 "BR-participact-brasil":"Civic tech de reporte urbano (app para reportar problemas): no es un proceso participativo.",
 "CR-diara":"Civic tech de fiscalización de obras (control social vía app): no es un proceso participativo.",
 "DO-ciudadania":"Solo atención/servicio; la 'participación' es co-diseñar la IA aportando datos, no consulta pública. Sin módulo de participación (verificado). Decisión del equipo.",
 "CO-dnp-dialogos-regionales-vinculantes-pnd":"Participación real, pero el análisis fue manual/cualitativo; solo text-analytics ligero (nubes de palabras + tabulación), sin NLP sobre el contenido (verificado). Decisión del equipo.",
}
# Confirmados -> ENTRA (sí es participación; IA en alguna etapa, incl. logística):
RESCATE_ENTRA = {  # caso_id -> por qué entra
 "MX-presupuesto-creces":"Presupuesto participativo (Hermosillo); la IA (chatbot) facilita la votación (Implementación).",
 "CL-lxs-400-chile-delibera":"Mini-público del Senado; la IA modera y administra los turnos de palabra (Implementación/Planificación).",
 "CL-estrategia-de-gobierno-digital-informe-p":"Consulta ciudadana; la IA analiza los aportes (Análisis).",
 "HN-redpublica-iverify":"Plataforma de propuestas de ley ciudadanas (participación legislativa).",
 "CL-la-voz-de-los-nuevos-votantes":"Consulta a nuevos votantes con NLP — proceso ejecutado por el equipo (confirmado).",
 "CL-jornada-de-escucha-lanzamiento-instituto":"Jornada de escucha / diálogo — proceso ejecutado por el equipo (confirmado).",
 "CO-chatico":"Tiene módulos de participación (aportes al Plan de Desarrollo de Bogotá) — confirmado por el equipo.",
}
# DUDA con revisión de posible IA/participación (investigadas; recomendación + URL):
DUDA_REVISAR = {  # caso_id -> hallazgo + recomendación
 "TT-engagett-plataforma-go-vocal":"IA MIXTA: chatbot AskNDTS (IA) activo que ayuda a ENTENDER el NDTS (facilitación/info, no procesa aportes). El módulo Sensemaking de Go Vocal existe pero NO se confirma activado ni anunciado para TT. Ministerio ahora MPAAI (Public Admin + AI). → DUDA: ¿basta el chatbot explicador como 'IA en el proceso'? Ver mdt.gov.tt (EngageTT + AskNDTS).",
}
# DUDA de frontera (aún por decidir; participación-ish):
RECLASIF_DUDA = {  # caso_id -> qué confirmar
 "CR-u-report-costa-rica-chatbot-juvenil":"Plataforma de opinión juvenil (UNICEF): ¿consulta participativa o civic tech de sondeo?",
}
# Revisar entre los que ENTRAN hoy (decisión a mano):
REVISAR_ENTRA = {  # caso_id -> por qué revisar
 "BR-colab":"GovTech de reporte urbano + servicios (IA para gestión/servicios): ¿participación o civic tech?",
}
# Posible reingreso desde los excluidos (referencia del equipo; distinto del criterio nuevo):
RESCATE = {  # actualmente NO; su referencia los reconsidera
 "CL-EXC-ucampus":"Su referencia lo marca RESCATABLE (confirmar si hubo NLP sobre los aportes del proceso constituyente).",
 "CU-consulta-popular-codigo-de-las-familias":"Su referencia lo marca RESCATABLE; mi evidencia (ficha técnica Datys/GEMA = NLP) apoya SI.",
}
CRIT = ["pais","tipo_proceso","etapas_uso_IA","estado_actividad","nivel_consolidacion","tipo_convocante","usa_IA_en_proceso","rol_IA"]


def j(v):
    if v is None: return ""
    if isinstance(v,list): return "; ".join(str(x) for x in v if x not in (None,""))
    return str(v)

def off(d): return str(d.get("veredicto_equipo") or d.get("entra_tentativo") or "")
def is_in(d): return off(d).upper().startswith(("SI","DUDA"))
def is_duda(d): return off(d).upper().startswith("DUDA")

def urls(d):
    out=[]
    for g in (d.get("gaps") or []):
        u=(g.get("url_para_buscar") or "").strip()
        if u and u not in out: out.append(u)
    if not out:
        for s in (d.get("fuentes") or []):
            u=(s.get("url") or "").strip()
            if u and u not in out: out.append(u)
    return out

def accion(d):
    cid=d["caso_id"]
    if cid in RESCATE_ENTRA: return "➜ RESCATADO → ENTRA (criterio corregido)"
    if cid in DUDA_REVISAR: return "➜ DUDA — revisar posible IA/participación"
    if cid in RECLASIF_DUDA: return "➜ DUDA (frontera) — resolver a mano"
    if cid in REVISAR_ENTRA: return "➜ REVISAR — ¿es participación?"
    if d.get("cuenta_como_iniciativa") is False: return "➜ NO contar (duplicado)"
    if is_duda(d): return "➜ RESOLVER DUDA"
    return ""

def hdr(ws,n,h=30):
    for c in range(1,n+1):
        cell=ws.cell(row=1,column=c); cell.fill=AZUL; cell.font=WB; cell.alignment=CEN; cell.border=BOR
    ws.row_dimensions[1].height=h; ws.freeze_panes="A2"; ws.auto_filter.ref=f"A1:{get_column_letter(n)}{ws.max_row}"

def widths(ws,ws_list):
    for i,w in enumerate(ws_list,1): ws.column_dimensions[get_column_letter(i)].width=w

def body(ws,ncol):
    for r in range(2,ws.max_row+1):
        for c in range(1,ncol+1):
            ws.cell(row=r,column=c).alignment=WRAP; ws.cell(row=r,column=c).border=BOR


def main():
    fichas=[json.load(open(f,encoding="utf-8")) for f in sorted(glob.glob(os.path.join(ROOT,"data/fichas/*_detalle.json")))]
    fichas.sort(key=lambda d:(str(d.get("pais") or ""),str(d.get("nombre_caso") or "")))
    # Bajo el criterio corregido, los EXCLUIR confirmados salen del set de trabajo.
    IN=[d for d in fichas if is_in(d) and d["caso_id"] not in EXCLUIR]
    OUT=[d for d in fichas if not (is_in(d) and d["caso_id"] not in EXCLUIR)]
    wb=Workbook(); wb.remove(wb.active)

    # ---------- 1 · Casos (entran + dudosos) ----------
    ws=wb.create_sheet("1 · Casos (entran+dudosos)")
    cols=["Acción sugerida","País","Caso","¿ENTRA? equipo","¿ENTRA? evidencia","Cuenta como iniciativa","Confianza",
          "Tipo de proceso","Etapas uso IA","Nivel (0-3)","Continuidad","Convocante (7-cat)","Tipo org",
          "Rol IA","Tipo desarrollador IA","Origen desarr.","Tipos/familia IA","Usa LLM",
          "Proceso participativo","Organización a cargo","Año","Nº gaps","URLs para verificar","caso_id"]
    ws.append(cols)
    for d in IN:
        ws.append([accion(d), d.get("pais") or "", d.get("nombre_caso") or "",
                   d.get("veredicto_equipo") or "(sin revisar)", d.get("entra_tentativo") or "",
                   "NO (duplicado)" if d.get("cuenta_como_iniciativa") is False else "sí", d.get("confianza") or "",
                   j(d.get("tipo_proceso")), j(d.get("etapas_uso_IA")),
                   "" if d.get("nivel_consolidacion") is None else d.get("nivel_consolidacion"),
                   j(d.get("continuidad")), j(d.get("tipo_convocante")), j(d.get("tipo_organizacion")),
                   d.get("rol_IA") or "", j(d.get("tipo_desarrollador_IA")), d.get("origen_desarrollador") or "",
                   j(d.get("tipos_IA_familia")), d.get("usa_LLM_generativa") or "",
                   d.get("proceso_participativo") or "", d.get("organizacion_a_cargo") or "", j(d.get("ano_inicio")),
                   len(d.get("gaps",[]) or []), "\n".join(urls(d)[:3]), d.get("caso_id")])
    hdr(ws,len(cols)); widths(ws,[30,6,30,12,14,15,24,24,22,8,12,22,12,12,20,14,22,10,40,28,7,6,40,30]); body(ws,len(cols))
    ci={h:i+1 for i,h in enumerate(cols)}
    for r in range(2,ws.max_row+1):
        a=ws.cell(row=r,column=ci["Acción sugerida"]); av=str(a.value)
        if "RESCATADO" in av: a.fill=VERDE
        elif "REVISAR" in av: a.fill=AMBARH
        elif "DUDA" in av: a.fill=AMBAR
        elif "duplicado" in av: a.fill=GRIS
        for h in ("¿ENTRA? equipo","¿ENTRA? evidencia"):
            cc=ws.cell(row=r,column=ci[h]); v=str(cc.value).upper(); cc.alignment=CEN
            if v.startswith("SI"): cc.fill=VERDE
            elif v.startswith("NO"): cc.fill=ROJO
            elif v.startswith("DUDA"): cc.fill=AMBAR
        g=ws.cell(row=r,column=ci["Nº gaps"]); g.alignment=CEN
        if isinstance(g.value,int) and g.value>0: g.fill=AMBARH

    # ---------- 2 · A validar a mano ----------
    ws2=wb.create_sheet("2 · A validar a mano")
    c2=["Grupo","Acción","País","Caso","¿Qué decidir / hacer?","Motivo / evidencia","URL para verificar"]
    ws2.append(c2)
    fmap={d["caso_id"]:d for d in fichas}
    # A) excluir confirmado (criterio corregido: no es participación / sin IA)
    for cid,motivo in EXCLUIR.items():
        d=fmap.get(cid,{})
        ws2.append(["A. Excluir (criterio corregido)","Confirmar NO (ya fuera del conteo)",d.get("pais",""),d.get("nombre_caso",cid),
                    "No es un proceso de participación (o sin IA verificada) → excluido", motivo, "\n".join(urls(d)[:2])])
    # B) rescatados -> ENTRA bajo el criterio corregido
    for cid,motivo in RESCATE_ENTRA.items():
        d=fmap.get(cid,{})
        ws2.append(["B. Rescatado → ENTRA","Confirmar SI",d.get("pais",""),d.get("nombre_caso",cid),
                    "Sí es participación; la IA aporta en alguna etapa (incl. logística) → ENTRA", motivo, "\n".join(urls(d)[:2])])
    # C) DUDA — revisar posible IA/participación (el equipo cree que puede haber algo)
    for cid,motivo in DUDA_REVISAR.items():
        d=fmap.get(cid,{})
        ws2.append(["C. DUDA — revisar (posible IA)","Abrir URL y decidir SI/NO",d.get("pais",""),d.get("nombre_caso",cid),
                    "Revisar si hay/planea IA o módulo de participación", motivo, "\n".join(urls(d)[:3])])
    for cid,motivo in RECLASIF_DUDA.items():
        d=fmap.get(cid,{})
        ws2.append(["C. DUDA — revisar (posible IA)","Abrir URL y decidir SI/NO",d.get("pais",""),d.get("nombre_caso",cid),
                    "¿Proceso de participación o sondeo? Decidir", motivo, "\n".join(urls(d)[:3])])
    # D) revisar entre los que ENTRAN hoy (parecen no-participación)
    for cid,motivo in REVISAR_ENTRA.items():
        d=fmap.get(cid,{})
        ws2.append(["D. Revisar ¿participación?","¿Mantener SI o pasar a NO?",d.get("pais",""),d.get("nombre_caso",cid),
                    "Parece civic tech/atención; confirmar si es realmente participación", motivo, "\n".join(urls(d)[:2])])
    # E) DUDAs de campo previas (Jalisco, Gaitana, Viña Decide, Participa Pudahuel)
    for d in IN:
        if is_duda(d) and d["caso_id"] not in RECLASIF_DUDA:
            ws2.append(["E. Resolver DUDA de campo","Decidir SI o NO",d.get("pais",""),d.get("nombre_caso",""),
                        "Abrir la URL y confirmar si es participación con IA en alguna etapa",
                        (d.get("justificacion_elegibilidad") or "")[:220], "\n".join(urls(d)[:2])])
    # F) posible reingreso (referencia del equipo, distinto del criterio nuevo)
    for cid,nota in RESCATE.items():
        d=fmap.get(cid,{})
        ws2.append(["F. Posible reingreso","¿Reingresa? (SI/NO)",d.get("pais",""),d.get("nombre_caso",cid),
                    "Verificar si corresponde reingresarlo", nota, "\n".join(urls(d)[:2])])
    # G) dedup
    ws2.append(["G. Dedup (confirmar)","Confirmar cuenta como 1","BR","e-Cidadania (Senado Federal)",
                "El 'matching de ideias' no se cuenta aparte del 'marcado de audiencias' (misma plataforma)",
                "'Duas ferramentas relacionadas' del mismo portal e-Cidadania (fuente Senado).",""])
    ws2.append(["G. Dedup (confirmar)","Confirmar 1 SI + 1 NO","CL","Participación Ciudadana Proceso Constitucional",
                "Homónimo duplicado: uno cuenta (SI), el otro NO","Ya resuelto en la planilla.",""])
    hdr(ws2,len(c2)); widths(ws2,[26,24,6,34,40,50,40]); body(ws2,len(c2))
    GFILL={"A":ROJO,"B":VERDE,"C":AMBAR,"D":AMBARH,"E":AMBAR,"F":AMBARH,"G":GRIS}
    for r in range(2,ws2.max_row+1):
        g=str(ws2.cell(row=r,column=1).value)[:1]
        ws2.cell(row=r,column=1).fill=GFILL.get(g,GRIS)

    # ---------- 3 · Excluidos ----------
    ws3=wb.create_sheet("3 · Excluidos")
    c3=["País","Caso","Bloque","Motivo / justificación","URL"]
    ws3.append(c3)
    BL={"1-nuevo":"Nuevo","1-dudoso":"Dudoso","2-baseline":"Baseline 2025","3-excluido-revisar":"Excluido (revisar)","4-descubrimiento-amplio":"Descubrimiento","5-excluido-2025":"Excluido 2025"}
    for d in OUT:
        cid=d.get("caso_id")
        bloque="Excluido (criterio corregido)" if cid in EXCLUIR else BL.get(d.get("bloque"),d.get("bloque"))
        motivo=EXCLUIR.get(cid) or d.get("motivo_exclusion_2025") or d.get("justificacion_elegibilidad") or ""
        u=(d.get("fuentes") or [{}])[0].get("url","") if d.get("fuentes") else ""
        ws3.append([d.get("pais") or "", d.get("nombre_caso") or "", bloque, motivo[:300], u])
    hdr(ws3,len(c3)); widths(ws3,[6,34,20,70,46]); body(ws3,len(c3))

    # ---------- 4 · Evidencia y fuentes ----------
    ws4=wb.create_sheet("4 · Evidencia y fuentes")
    c4=["País","Caso","¿ENTRA?"]+[f"EV: {c}" for c in CRIT]+["Fuentes (URLs)"]
    ws4.append(c4)
    for d in IN:
        ev=d.get("evidencia_verbatim",{}) or {}
        fu="\n".join(s.get("url","") for s in (d.get("fuentes") or []) if s.get("url"))
        ws4.append([d.get("pais") or "", d.get("nombre_caso") or "", off(d)]+[ev.get(c) or "" for c in CRIT]+[fu])
    hdr(ws4,len(c4)); widths(ws4,[6,30,10]+[30]*len(CRIT)+[40]); body(ws4,len(c4))
    for r in range(2,ws4.max_row+1):
        for c in range(4,4+len(CRIT)):
            if not ws4.cell(row=r,column=c).value: ws4.cell(row=r,column=c).fill=AMBARH

    # ---------- 5 · Instrucciones ----------
    ws5=wb.create_sheet("5 · Instrucciones")
    for row in GUIA_ROWS(len(IN),len(OUT)):
        ws5.append(row)
    ws5.column_dimensions["A"].width=30; ws5.column_dimensions["B"].width=115
    for r in range(1,ws5.max_row+1):
        ws5.cell(row=r,column=1).font=Font(bold=True); ws5.cell(row=r,column=1).alignment=TL; ws5.cell(row=r,column=2).alignment=TL
    ws5["A1"].font=Font(bold=True,size=13)

    # ---------- 6 · Metodología (CENIA v2) ----------
    ws6=wb.create_sheet("6 · Metodología (CENIA v2)")
    for row in METODOLOGIA_ROWS(): ws6.append(row)
    widths(ws6,[26,34,58,24])
    for r in range(1,ws6.max_row+1):
        for c in range(1,5): ws6.cell(row=r,column=c).alignment=TL
    # título + fórmula
    ws6.merge_cells("A1:D1"); ws6["A1"].fill=AZUL; ws6["A1"].font=Font(bold=True,color="FFFFFF",size=12); ws6["A1"].alignment=CEN; ws6.row_dimensions[1].height=28
    ws6.merge_cells("A2:D2"); ws6["A2"].font=Font(bold=True,size=11)
    # cabecera de la tabla (fila 4)
    for c in range(1,5):
        cell=ws6.cell(row=4,column=c); cell.fill=AZUL; cell.font=WB; cell.alignment=CEN; cell.border=BOR
    for r in range(5,12):
        for c in range(1,5): ws6.cell(row=r,column=c).border=BOR
    # agrupar sub-indicador (Uso = 5 vars, Desarrollo = 2 vars)
    ws6.merge_cells("A5:A9"); ws6["A5"].alignment=Alignment(wrap_text=True,vertical="center"); ws6["A5"].font=Font(bold=True); ws6["A5"].fill=GRIS
    ws6.merge_cells("A10:A11"); ws6["A10"].alignment=Alignment(wrap_text=True,vertical="center"); ws6["A10"].font=Font(bold=True); ws6["A10"].fill=GRIS
    # bloque Organización Convocante
    ws6.merge_cells("A13:D13"); ws6["A13"].fill=AMBARH; ws6["A13"].font=Font(bold=True)
    for r in range(14,17):
        for c in range(1,5): ws6.cell(row=r,column=c).border=BOR
        ws6.cell(row=r,column=1).font=Font(bold=True)
    # notas + fuente (texto en col B, ancho hasta D)
    for r in list(range(18,24))+[25]:
        ws6.merge_cells(start_row=r,start_column=2,end_row=r,end_column=4)
    ws6["A18"].font=Font(bold=True); ws6["A25"].font=Font(bold=True)
    ws6.freeze_panes="A5"

    dst=os.path.join(ROOT,"data/gates/planilla_ILIA2026_SIMPLE.xlsx"); wb.save(dst)

    # ---------- guía markdown ----------
    md=os.path.join(ROOT,"data/gates/GUIA_validacion_manual_ILIA2026.md")
    open(md,"w",encoding="utf-8").write(GUIA_MD(len(IN),len(OUT)))
    dup=sum(1 for d in IN if d.get("cuenta_como_iniciativa") is False)
    dudas_campo=sum(1 for d in IN if is_duda(d) and d["caso_id"] not in RECLASIF_DUDA)
    print(f"[ok] {dst}")
    print(f"[ok] {md}")
    print(f"     entran+dudosos: {len(IN)} (iniciativas efectivas: {len(IN)-dup}) | excluidos: {len(OUT)}")
    print(f"     reclasif: excluidos={len(EXCLUIR)} rescatados→ENTRA={len(RESCATE_ENTRA)} "
          f"DUDA-revisar={len(DUDA_REVISAR)} DUDA-frontera={len(RECLASIF_DUDA)} revisar={len(REVISAR_ENTRA)} "
          f"DUDA-campo={dudas_campo} reingreso={len(RESCATE)}")
    return 0


def METODOLOGIA_ROWS():
    """Contenido de la pestaña 6 · Metodología (CENIA v2). 4 columnas."""
    return [
     ["METODOLOGÍA FINAL — IA en Participación Ciudadana (CENIA v2 · jun-2026)","","",""],
     ["Indicador = (Sub-Indicador de Uso + Sub-Indicador de Desarrollo) / 2","","",""],
     ["","","",""],
     ["Sub-indicador","Variable","Cómo se calcula (normalización)","Columna en pestaña 1"],
     ["Uso de IA\n(promedio simple\nde 5 variables)","Tipos de proceso","nº de tipos distintos ÷ 5 (máximo absoluto)","Tipo de proceso"],
     ["","Etapas de uso","nº de etapas distintas ÷ 4 (máximo absoluto)","Etapas uso IA"],
     ["","Continuidad","nivel MÁXIMO verificado del país ÷ 3 · un 'anuncio' caduca a los 2 años sin implementación","Nivel (0-3)"],
     ["","Organización Convocante","promedio de 3 sub-componentes co-iguales (ver detalle abajo)","Convocante (7-cat)"],
     ["","Cantidad de iniciativas","nº de TODAS las iniciativas elegibles del país · umbrales fijos 0→0 · 1-3→25 · 4-6→50 · 7-9→75 · 10+→100","1 fila = 1 iniciativa"],
     ["Desarrollo de IA\n(idéntico a 2025)","Desarrollador","nacional / internacional × 4 tipos de actor · máximo relativo","Tipo desarrollador IA · Origen"],
     ["","Tipos de IA","nº de sistemas de IA distintos · máximo relativo","Tipos/familia IA"],
     ["","","",""],
     ["ORGANIZACIÓN CONVOCANTE — 3 sub-componentes co-iguales · valor de la variable = (1 + 2 + 3) / 3","","",""],
     ["1 · Amplitud gubernamental","nº de tipos gubernamentales distintos ÷ 3","gobierno local · gobierno nacional · otra institución pública",""],
     ["2 · Amplitud no gubernamental","nº de tipos no gubernamentales distintos ÷ 4","empresa · universidad · sociedad civil · organización internacional",""],
     ["3 · Co-convocatoria","nº de combinaciones distintas (conjuntos de ≥2 tipos que co-convocan una misma iniciativa) ÷ máximo relativo móvil del ciclo","combinaciones DEDUPLICADAS · una co-convocatoria de 4 actores = 1 combinación",""],
     ["","","",""],
     ["Notas","• ELEGIBILIDAD (criterio corregido): un caso ENTRA si es realmente un proceso de PARTICIPACIÓN CIUDADANA que usa IA en alguna etapa (incl. logística: modera / administra turnos / prepara materiales / organiza). La IA NO necesita analizar el contenido. NO entra civic tech (reporte/servicio/monitoreo), atención ciudadana ni voto/conteo electoral.","",""],
     ["","• Universidades públicas → cuentan como 'Universidad' (no gubernamental), NO como 'otra institución pública'.","",""],
     ["","• Anotar TODOS los convocantes de cada iniciativa (no solo el principal): así se detecta la co-convocatoria.","",""],
     ["","• El máximo relativo de co-convocatoria se recalcula en cada corrida del motor — no se fija a mano.","",""],
     ["","• 'Cantidad' cuenta las iniciativas elegibles; los duplicados (Cuenta como iniciativa = NO) no se suman.","",""],
     ["","• El Sub-Indicador de Desarrollo es idéntico al de 2025 (no se modificó).","",""],
     ["","","",""],
     ["Fuente","metodologia_final_CENIA_v2.xlsx · detalle de conformidad en conformidad_metodologia_CENIA.md","",""],
    ]


def GUIA_ROWS(nin,nout):
    return [
     ["GUÍA — Validar los casos y pasar al cálculo (ILIA 2026)"],
     ["Qué tienes", f"Planilla con 6 pestañas (criterio corregido). {nin} casos entran/dudosos · {nout} excluidos · 107 en total. Tras dedup e-Cidadania: {nin-1} iniciativas."],
     ["Cómo navegar","Pestaña 1 = trabajo y cálculo · 2 = qué decidir a mano · 3 = excluidos (referencia) · 4 = evidencia/citas · 5 = esta guía · 6 = metodología CENIA v2."],
     ["",""],
     ["PASO 1 — Confirmar exclusiones (pestaña 2, grupo A)","4 casos ya FUERA: no son procesos de participación — PE conteo electoral · CO Descongestión (atención) · BR ParticipACT y CR dIAra (civic tech). Solo confirmar."],
     ["PASO 2 — Confirmar rescatados → ENTRA (grupo B)","7 casos que ENTRAN: MX Presupuesto CRECES · CL LXS 400 · CL Estrategia Gob. Digital · HN RedPública · CL Voz nuevos votantes · CL Jornada UNAB · CO Chatico. Confirmar SI."],
     ["PASO 3 — DUDAS a revisar con URL (grupos C y D)","C: TT EngageTT (¿IA planeada?), CO DNP Diálogos (¿usó NLP/ConTexto?), DO CiudadanIA (¿módulo de participación?), CR U-Report (¿participación o sondeo?). D: BR Colab (¿participación o civic tech?). Abrir la URL y decidir."],
     ["PASO 4 — Resolver DUDAS de campo (grupo E)","4 casos (Jalisco, Gaitana, Viña Decide, Participa Pudahuel). Abrir la URL y confirmar si es participación con IA en alguna etapa. Marcar SI o NO."],
     ["PASO 5 — Reingresos y dedup (grupos F y G)","F: UCampus y CU Código de las Familias (posible reingreso). G: e-Cidadania cuenta como 1; CL Participación Constitucional: 1 SI + 1 NO."],
     ["PASO 6 — Completar datos de cálculo","Para los que quedan en SI, revisar en la pestaña 1 que estén completos: Tipo de proceso, Etapas, Nivel (0-3), Convocante, Tipo org. Donde 'Nº gaps'>0, abrir la URL y completar."],
     ["PASO 7 — Validar evidencia (pestaña 4)","Revisar que cada campo crítico tenga cita textual. Celdas ámbar = falta cita → verificar con la fuente antes de dar por bueno."],
     ["PASO 8 — Calcular","Con la lista final de iniciativas y sus campos completos, correr el motor (Sub1 Uso + Sub2 Desarrollo). Ver config.yaml y src/calc_engine.py."],
     ["",""],
     ["Regla de elegibilidad (CRITERIO CORREGIDO)","Lo decisivo es si es REALMENTE un proceso de participación ciudadana (consulta, presupuesto participativo, mini-público, referendo/iniciativa popular, gobernanza colaborativa/deliberación) que usa IA en alguna de las 4 etapas — INCLUIDA la logística en Planificación/Implementación (modera, administra turnos, prepara materiales, organiza). NO se exige que la IA analice el contenido. NO ENTRA: civic tech que no es un proceso participativo (app de reporte/servicio/monitoreo), atención ciudadana, voto/conteo electoral por candidatos, IA como tema, estudio sin despliegue, o duplicado."],
     ["Qué alimenta el cálculo (metodología CENIA v2)","Sub1 (Uso): Tipos de proceso (÷5) · Etapas de uso (÷4) · Continuidad = nivel máximo del país (÷3) · Organización Convocante = 3 sub-componentes (amplitud gubernamental ÷3 + amplitud no gubernamental ÷4 + co-convocatoria por máx. relativo) · Cantidad = nº de iniciativas ELEGIBLES (todas, umbrales fijos). Sub2 (Desarrollo, = 2025): Desarrollador (nacional/internacional × 4 tipos, máx. relativo) · Tipos de IA."],
     ["IMPORTANTE — co-convocatoria","Anotar TODOS los convocantes de cada iniciativa (no solo el principal): si ≥2 tipos co-convocan, forman una 'combinación' que suma al tercer sub-componente de Organización Convocante."],
    ]


def GUIA_MD(nin,nout):
    return f"""# Guía: validar los casos y pasar al cálculo — ILIA 2026

**Archivo de trabajo:** `planilla_ILIA2026_SIMPLE.xlsx` (6 pestañas · **criterio corregido**).
**Estado:** {nin} casos entran/dudosos · {nout} excluidos · 107 en total.
Tras el dedup de e-Cidadania → **{nin-1} iniciativas efectivas**.

## Las 6 pestañas
1. **Casos (entran+dudosos)** — el set de trabajo, con las columnas listas para calcular y una columna **«Acción sugerida»**.
2. **A validar a mano** — la lista concreta de decisiones por grupo (A excluir · B rescatados→ENTRA · C/D frontera civic-tech · E DUDAs de campo · F reingresos · G dedup).
3. **Excluidos** — los que salen, con su motivo (referencia).
4. **Evidencia y fuentes** — la cita textual por campo crítico + URLs (para verificar que no hay alucinaciones).
5. **Instrucciones** — esta guía dentro del Excel.
6. **Metodología (CENIA v2)** — la metodología final acordada, variable por variable, y qué columna alimenta cada una.

## Pasos manuales (en orden)

### Paso 1 — Confirmar las exclusiones  *(pestaña 2, grupo A)*
**4 casos** ya quedaron **FUERA** (en la pestaña 3) por no ser procesos de participación. Solo confirmar:
- **Voto/servicio:** PE Sistema de cómputo ONPE (conteo electoral) · CO Descongestión Ingreso Solidario (atención/triage de correos).
- **Civic tech:** BR ParticipACT (app de reporte urbano) · CR dIAra (app de fiscalización de obras).

### Paso 2 — Confirmar los rescatados → ENTRA  *(pestaña 2, grupo B)*
**7 casos ENTRAN** (son participación con IA en alguna etapa):
- **MX Presupuesto CRECES** — presupuesto participativo; la IA (chatbot) facilita la votación.
- **CL LXS 400 / Chile Delibera** — mini-público del Senado; la IA modera y administra turnos de palabra.
- **CL Estrategia de Gobierno Digital** — consulta ciudadana; la IA analiza los aportes.
- **HN RedPública** — plataforma de propuestas de ley ciudadanas.
- **CL La voz de los nuevos votantes** y **CL Jornada de Escucha UNAB** — procesos ejecutados por el equipo (confirmados).
- **CO Chatico** — tiene módulos de participación (aportes al Plan de Desarrollo de Bogotá).

### Paso 3 — DUDAS a revisar con URL  *(pestaña 2, grupos C y D)*
Abrir la URL y decidir **SI o NO**. El equipo cree que puede haber IA/participación:
- **TT EngageTT** — ¿la IA de Go Vocal (Sensemaking) está activa o **planeada**? Si está planeada, ENTRA.
- **CO DNP Diálogos Regionales** — ¿se usó NLP (p. ej. **ConTexto** del DNP) para sistematizar las 89.788 propuestas?
- **DO CiudadanIA** — ¿tiene un **módulo de participación** (recoger aportes para decisiones), no solo atención?
- **CR U-Report** — ¿consulta participativa o civic tech de sondeo?
- **BR Colab** *(grupo D)* — ¿participación o GovTech de reporte/servicio?

### Paso 4 — Resolver las DUDAS de campo  *(pestaña 2, grupo E)*
Abrir la URL y confirmar si es participación con IA en alguna etapa → **SI** o **NO**:
- **MX Jalisco «Armemos un Plan»** — el PDF del informe está bloqueado.
- **CO Gaitana IA** — confirmar profundidad real del uso de IA.
- **CL Viña Decide** y **CL Participa Pudahuel** — confirmar con el municipio/Go Vocal si activaron el módulo de IA.

### Paso 5 — Reingresos y dedup  *(pestaña 2, grupos F y G)*
- **F (reingreso):** CL UCampus y CU Código de las Familias — su referencia los reconsidera.
- **G (dedup):** e-Cidadania cuenta como **1**; CL Participación Constitucional (homónimo): **1 SI + 1 NO**.

### Paso 6 — Completar los datos del cálculo  *(pestaña 1)*
Para los casos que quedan en **SI**, revisar que estén completos: **Tipo de proceso · Etapas de uso · Nivel (0-3) · Convocante · Tipo de organización**. Donde `Nº gaps` > 0, abrir la URL de «URLs para verificar» y completar a mano.

### Paso 7 — Validar la evidencia  *(pestaña 4)*
Revisar que cada **campo crítico** tenga cita textual. Las celdas **ámbar** = falta cita → verificar con la fuente antes de darlo por bueno.

### Paso 8 — Calcular el indicador
Con la lista final de iniciativas y sus campos completos, correr el motor: **Sub1 (Uso)** + **Sub2 (Desarrollo)**. Ver `config.yaml` (decisiones abiertas: escenario A/B, cortes de cantidad, redondeo) y `src/calc_engine.py`.

---

## Recordatorio — regla de elegibilidad (CRITERIO CORREGIDO)
Lo **decisivo** es si el caso es **realmente un proceso de participación ciudadana** (consulta, presupuesto participativo, mini-público, referendo/iniciativa popular, gobernanza colaborativa/deliberación) que **usa IA en alguna de las 4 etapas** — **incluida la logística** en Planificación/Implementación (modera, administra turnos, prepara materiales, organiza). **NO se exige que la IA analice el contenido de los aportes.**
**NO ENTRA:** una simple **app de civic tech** que no es un proceso participativo (reporte, servicio, monitoreo), **atención ciudadana**, **voto/conteo electoral por candidatos**, IA como *tema* de la consulta, estudio académico sin despliegue, o **duplicado** de un caso ya contado.

## Qué columna alimenta qué variable (metodología final CENIA v2, jun-2026)
**Sub-indicador de Uso (Sub1)** — promedio simple de 5 variables:
- **Tipos de proceso** (columna «Tipo de proceso») → nº de tipos presentes en el país ÷ 5.
- **Etapas de uso de IA** (columna «Etapas uso IA») → nº de etapas ÷ 4.
- **Continuidad** (columna «Nivel (0-3)») → **nivel máximo del país** ÷ 3.
- **Organización Convocante** (columna «Convocante (7-cat)») → **3 sub-componentes co-iguales**:
  1. *amplitud gubernamental* = nº de tipos gubernamentales distintos ÷ 3 (gobierno local · nacional · otra institución pública),
  2. *amplitud no gubernamental* = nº de tipos no gubernamentales distintos ÷ 4 (empresa · **universidad** · sociedad civil · organización internacional),
  3. *co-convocatoria* = nº de combinaciones de ≥2 tipos que co-convocan, por **máximo relativo móvil** (el país con más combinaciones = 1).
  El valor de la variable = (1 + 2 + 3) / 3.
- **Cantidad de iniciativas** (una fila = una iniciativa; no contar duplicados) → **TODAS las elegibles** del país (sin filtro de nivel), con los cortes 0→0 · 1-3→25 · 4-6→50 · 7-9→75 · 10+→100.

**Sub-indicador de Desarrollo (Sub2, idéntico a 2025):** Tipo de desarrollador (nacional/internacional × 4 tipos, máximo relativo) · Tipos de IA.

> **IMPORTANTE — co-convocatoria:** anotar **todos** los convocantes de cada iniciativa (no solo el principal). Si ≥2 tipos co-convocan, forman una «combinación» que alimenta el tercer sub-componente de Organización Convocante. Las **universidades públicas** cuentan como «Universidad» (no gubernamental), no como «otra institución pública».
"""


if __name__ == "__main__":
    sys.exit(main())
