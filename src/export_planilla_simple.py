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

# --- Acciones manuales (de la verificación profunda del equipo / referencia) ---
EXCLUIR = {  # caso_id -> rol_IA reportado por el equipo
 "BR-participact-brasil":"apoyo", "CL-estrategia-de-gobierno-digital-informe-p":"sin_IA",
 "CL-jornada-de-escucha-lanzamiento-instituto":"sin_IA", "CL-la-voz-de-los-nuevos-votantes":"sin_IA",
 "CR-u-report-costa-rica-chatbot-juvenil":"sin_IA", "CR-diara":"apoyo", "DO-ciudadania":"apoyo",
 "HN-redpublica-iverify":"apoyo", "MX-presupuesto-creces":"sin_IA",
 "CO-descongestion-de-solicitudes-diarias-del":"apoyo", "PE-sistema-de-computo-con-ia-para-las-elecc":"apoyo",
 "CL-lxs-400-chile-delibera":"apoyo", "CO-dnp-dialogos-regionales-vinculantes-pnd":"sin_IA",
 "TT-engagett-plataforma-go-vocal":"apoyo",
}
RESCATE = {  # actualmente NO; su referencia los reconsidera
 "CL-EXC-ucampus":"Su referencia lo marca RESCATABLE (confirmar si hubo NLP sobre los aportes del proceso constituyente).",
 "CU-consulta-popular-codigo-de-las-familias":"Su referencia lo marca RESCATABLE; mi evidencia (ficha técnica Datys/GEMA = NLP) apoya SI.",
}
ROL_TXT = {"apoyo":"IA de apoyo/logística (no procesa el contenido de los aportes)",
           "sin_IA":"sin IA sobre el contenido de los aportes"}
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
    if cid in EXCLUIR: return f"➜ EXCLUIR — {ROL_TXT.get(EXCLUIR[cid])}"
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
    IN=[d for d in fichas if is_in(d)]
    OUT=[d for d in fichas if not is_in(d)]
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
        a=ws.cell(row=r,column=ci["Acción sugerida"])
        if str(a.value).startswith("➜ EXCLUIR"): a.fill=ROJO
        elif "DUDA" in str(a.value): a.fill=AMBAR
        elif "duplicado" in str(a.value): a.fill=GRIS
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
    # A) excluir
    for cid,rol in EXCLUIR.items():
        d=fmap.get(cid,{})
        ws2.append(["A. Excluir (verif. profunda)","Cambiar ¿ENTRA? a NO",d.get("pais",""),d.get("nombre_caso",cid),
                    "Confirmar exclusión y sacarlo del conteo", ROL_TXT.get(rol,rol), "\n".join(urls(d)[:2])])
    # B) DUDA
    for d in IN:
        if is_duda(d):
            ws2.append(["B. Resolver DUDA","Decidir SI o NO",d.get("pais",""),d.get("nombre_caso",""),
                        "Abrir la URL y confirmar si la IA procesa el CONTENIDO de los aportes",
                        (d.get("justificacion_elegibilidad") or "")[:220], "\n".join(urls(d)[:2])])
    # C) rescate
    for cid,nota in RESCATE.items():
        d=fmap.get(cid,{})
        ws2.append(["C. Revisar (posible rescate)","¿Reingresa? (SI/NO)",d.get("pais",""),d.get("nombre_caso",cid),
                    "Verificar si ahora hay IA sobre el contenido → posible SI", nota, "\n".join(urls(d)[:2])])
    # D) dedup
    ws2.append(["D. Dedup (confirmar)","Confirmar cuenta como 1","BR","e-Cidadania (Senado Federal)",
                "El 'matching de ideias' no se cuenta aparte del 'marcado de audiencias' (misma plataforma)",
                "'Duas ferramentas relacionadas' del mismo portal e-Cidadania (fuente Senado).",""])
    ws2.append(["D. Dedup (confirmar)","Confirmar 1 SI + 1 NO","CL","Participación Ciudadana Proceso Constitucional",
                "Homónimo duplicado: uno cuenta (SI), el otro NO","Ya resuelto en la planilla.",""])
    hdr(ws2,len(c2)); widths(ws2,[26,22,6,34,40,50,40]); body(ws2,len(c2))
    for r in range(2,ws2.max_row+1):
        g=str(ws2.cell(row=r,column=1).value)
        fill=ROJO if g.startswith("A") else AMBAR if g.startswith("B") else AMBARH if g.startswith("C") else GRIS
        ws2.cell(row=r,column=1).fill=fill

    # ---------- 3 · Excluidos ----------
    ws3=wb.create_sheet("3 · Excluidos")
    c3=["País","Caso","Bloque","Motivo / justificación","URL"]
    ws3.append(c3)
    BL={"1-nuevo":"Nuevo","1-dudoso":"Dudoso","2-baseline":"Baseline 2025","3-excluido-revisar":"Excluido (revisar)","4-descubrimiento-amplio":"Descubrimiento","5-excluido-2025":"Excluido 2025"}
    for d in OUT:
        motivo=d.get("motivo_exclusion_2025") or d.get("justificacion_elegibilidad") or ""
        u=(d.get("fuentes") or [{}])[0].get("url","") if d.get("fuentes") else ""
        ws3.append([d.get("pais") or "", d.get("nombre_caso") or "", BL.get(d.get("bloque"),d.get("bloque")), motivo[:300], u])
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

    dst=os.path.join(ROOT,"data/gates/planilla_ILIA2026_SIMPLE.xlsx"); wb.save(dst)

    # ---------- guía markdown ----------
    md=os.path.join(ROOT,"data/gates/GUIA_validacion_manual_ILIA2026.md")
    open(md,"w",encoding="utf-8").write(GUIA_MD(len(IN),len(OUT)))
    dup=sum(1 for d in fichas if d.get("cuenta_como_iniciativa") is False)
    print(f"[ok] {dst}")
    print(f"[ok] {md}")
    print(f"     entran+dudosos: {len(IN)} (iniciativas efectivas: {len(IN)-dup}) | excluidos: {len(OUT)} | acciones a mano: {len(EXCLUIR)+sum(1 for d in IN if is_duda(d))+len(RESCATE)+2}")
    return 0


def GUIA_ROWS(nin,nout):
    return [
     ["GUÍA — Validar los casos y pasar al cálculo (ILIA 2026)"],
     ["Qué tienes", f"Planilla con 5 pestañas. {nin} casos entran/dudosos · {nout} excluidos · 107 en total. Tras dedup e-Cidadania: 43 iniciativas."],
     ["Cómo navegar","Pestaña 1 = trabajo y cálculo · 2 = qué decidir a mano · 3 = excluidos (referencia) · 4 = evidencia/citas · 5 = esta guía."],
     ["",""],
     ["PASO 1 — Excluir (pestaña 2, grupo A)","14 casos que su verificación profunda marcó 'apoyo' o 'sin IA'. En la pestaña 1 tienen 'Acción sugerida = ➜ EXCLUIR'. Cambiar su ¿ENTRA? a NO."],
     ["PASO 2 — Resolver DUDAS (pestaña 2, grupo B)","4 casos (Jalisco, Gaitana, Viña Decide, Participa Pudahuel). Abrir la URL, ver si la IA procesa el CONTENIDO de los aportes, y marcar SI o NO."],
     ["PASO 3 — Revisar rescates (grupo C)","UCampus y CU Código de las Familias: su referencia los reconsidera. Confirmar si reingresan (SI)."],
     ["PASO 4 — Confirmar dedup (grupo D)","e-Cidadania cuenta como 1 (el 'matching' no se suma aparte). CL Participación Constitucional: 1 SI + 1 NO."],
     ["PASO 5 — Completar datos de cálculo","Para los que quedan en SI, revisar en la pestaña 1 que estén completos: Tipo de proceso, Etapas, Nivel (0-3), Convocante, Tipo org. Donde 'Nº gaps'>0, abrir la URL y completar."],
     ["PASO 6 — Validar evidencia (pestaña 4)","Revisar que cada campo crítico tenga cita textual. Celdas ámbar = falta cita → verificar con la fuente antes de dar por bueno."],
     ["PASO 7 — Calcular","Con la lista final de iniciativas y sus campos completos, correr el motor (Sub1 Uso + Sub2 Desarrollo). Ver config.yaml y src/calc_engine.py."],
     ["",""],
     ["Regla de elegibilidad","ENTRA si, dentro de un proceso participativo, la IA procesa el CONTENIDO de los aportes (recolectar/clasificar/analizar/agrupar/sintetizar). NO: atención ciudadana, IA como tema, geoespacial, logística, estudio sin despliegue, duplicado."],
     ["Qué alimenta el cálculo (metodología CENIA v2)","Sub1 (Uso): Tipos de proceso (÷5) · Etapas de uso (÷4) · Continuidad = nivel máximo del país (÷3) · Organización Convocante = 3 sub-componentes (amplitud gubernamental ÷3 + amplitud no gubernamental ÷4 + co-convocatoria por máx. relativo) · Cantidad = nº de iniciativas ELEGIBLES (todas, umbrales fijos). Sub2 (Desarrollo, = 2025): Desarrollador (nacional/internacional × 4 tipos, máx. relativo) · Tipos de IA."],
     ["IMPORTANTE — co-convocatoria","Anotar TODOS los convocantes de cada iniciativa (no solo el principal): si ≥2 tipos co-convocan, forman una 'combinación' que suma al tercer sub-componente de Organización Convocante."],
    ]


def GUIA_MD(nin,nout):
    return f"""# Guía: validar los casos y pasar al cálculo — ILIA 2026

**Archivo de trabajo:** `planilla_ILIA2026_SIMPLE.xlsx` (5 pestañas).
**Estado:** {nin} casos entran/dudosos · {nout} excluidos · 107 en total.
Tras el dedup de e-Cidadania → **43 iniciativas efectivas**.

## Las 5 pestañas
1. **Casos (entran+dudosos)** — el set de trabajo, con las columnas listas para calcular y una columna **«Acción sugerida»**.
2. **A validar a mano** — la lista concreta de decisiones (excluir / resolver DUDA / rescatar / dedup).
3. **Excluidos** — los que salen, con su motivo (referencia).
4. **Evidencia y fuentes** — la cita textual por campo crítico + URLs (para verificar que no hay alucinaciones).
5. **Instrucciones** — esta guía dentro del Excel.

## Pasos manuales (en orden)

### Paso 1 — Excluir los 14 de la verificación profunda  *(pestaña 2, grupo A)*
Su verificación profunda marcó 14 casos como **IA de apoyo** o **sin IA sobre el contenido**. En la pestaña 1 aparecen con **Acción sugerida = ➜ EXCLUIR**. Cambiar su `¿ENTRA?` a **NO**:
BR ParticipACT · CL Estrategia Gob. Digital · CL Jornada UNAB · CL Voz nuevos votantes · CR U-Report · CR dIAra · DO CiudadanIA · HN RedPública · MX Presupuesto CRECES · CO Descongestión · PE Sistema de cómputo ONPE · CL LXS 400 · CO DNP Diálogos · TT EngageTT.

### Paso 2 — Resolver las 4 DUDAS  *(pestaña 2, grupo B)*
Abrir la URL y confirmar si la IA procesa el **contenido** de los aportes → marcar **SI** o **NO**:
- **MX Jalisco «Armemos un Plan»** — el PDF del informe está bloqueado; si revela un pipeline de IA, sube a SI; si no, NO.
- **CO Gaitana IA** — confirmar profundidad real del análisis (cobertura crítica lo cuestiona).
- **CL Viña Decide** y **CL Participa Pudahuel** — confirmar con el municipio/Go Vocal si activaron el módulo de IA (NLP) sobre los aportes.

### Paso 3 — Revisar posibles rescates  *(pestaña 2, grupo C)*
- **CL UCampus** y **CU Código de las Familias** — su referencia los reconsidera. Confirmar si reingresan (SI). *Para CU, mi evidencia (ficha técnica Datys/GEMA = NLP) apoya SI.*

### Paso 4 — Confirmar el dedup  *(pestaña 2, grupo D)*
- **e-Cidadania**: cuenta como **1** (el «matching de ideas» no se suma aparte del «marcado de audiencias»; misma plataforma/convocante).
- **CL Participación Constitucional** (homónimo): **1 SI + 1 NO**.

### Paso 5 — Completar los datos del cálculo  *(pestaña 1)*
Para los casos que quedan en **SI**, revisar que estén completos: **Tipo de proceso · Etapas de uso · Nivel (0-3) · Convocante · Tipo de organización**. Donde `Nº gaps` > 0, abrir la URL de «URLs para verificar» y completar a mano.

### Paso 6 — Validar la evidencia  *(pestaña 4)*
Revisar que cada **campo crítico** tenga cita textual. Las celdas **ámbar** = falta cita → verificar con la fuente antes de darlo por bueno.

### Paso 7 — Calcular el indicador
Con la lista final de iniciativas y sus campos completos, correr el motor: **Sub1 (Uso)** + **Sub2 (Desarrollo)**. Ver `config.yaml` (decisiones abiertas: escenario A/B, cortes de cantidad, redondeo) y `src/calc_engine.py`.

---

## Recordatorio — regla de elegibilidad
**ENTRA** si, dentro de un **proceso participativo**, la IA procesa el **CONTENIDO** de los aportes ciudadanos (recolectar / clasificar / analizar / agrupar por temas / sintetizar). **NO ENTRA**: atención ciudadana, IA como *tema* de la consulta, IA geoespacial/administrativa, logística (turnos), estudio académico sin despliegue, o **duplicado** de un caso ya contado.

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
