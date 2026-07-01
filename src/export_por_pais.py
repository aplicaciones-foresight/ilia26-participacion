#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
export_por_pais.py — Planilla SIMPLE por país para validación con partners.

Un archivo con una pestaña por país. Cada fila = un caso, con lo mínimo para que
un partner valide: nombre, descripción breve, fuente (URL validada) y si se incluye.
Pensada para enviar por país; lo más simple posible.

Salida: data/gates/planilla_validacion_por_pais_ILIA2026.xlsx
"""
from __future__ import annotations
import glob, json, os, re, sys
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill, Border, Side
from openpyxl.utils import get_column_letter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import export_planilla_simple as eps  # reusa la clasificación (EXCLUIR, is_in, is_duda)

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

AZUL=PatternFill("solid",fgColor="1F4E78"); VERDE=PatternFill("solid",fgColor="C6EFCE")
ROJO=PatternFill("solid",fgColor="FFC7CE"); AMBAR=PatternFill("solid",fgColor="FFEB9C")
GRIS=PatternFill("solid",fgColor="D9D9D9")
WB=Font(bold=True,color="FFFFFF"); CEN=Alignment(horizontal="center",vertical="center",wrap_text=True)
TL=Alignment(horizontal="left",vertical="top",wrap_text=True)
TH=Side(style="thin",color="BFBFBF"); BOR=Border(left=TH,right=TH,top=TH,bottom=TH)

PAIS_NOMBRE={"AR":"Argentina","BO":"Bolivia","BR":"Brasil","CL":"Chile","CO":"Colombia",
 "CR":"Costa Rica","CU":"Cuba","DO":"Rep. Dominicana","EC":"Ecuador","GT":"Guatemala",
 "HN":"Honduras","JM":"Jamaica","MX":"México","PA":"Panamá","PE":"Perú","PY":"Paraguay",
 "SV":"El Salvador","TT":"Trinidad y Tobago","UY":"Uruguay","VE":"Venezuela","LATAM":"LATAM / Regional"}

URLRE=re.compile(r'^https?://', re.I)

# Universo ILIA: 20 países (aunque no tengan casos identificados este ciclo).
PAISES_ILIA=["AR","BO","BR","CL","CO","CR","CU","DO","EC","GT","HN","JM","MX","PA","PE","PY","SV","TT","UY","VE"]

# --- Limpieza de texto: motivos/descripciones en lenguaje normal (sin jerga interna) ---
_PAT=[
 (r'exclusi[oó]n firme\s*\(recodificaci[oó]n 2026\):?\s*',''),
 (r'\(recodificaci[oó]n 2026\)',''),
 (r'mantener (excluido|excluida)\.?\s*',''),
 (r'\bno entra\.?\s*',''),(r'\bs[ií] entra\.?\s*',''),
 (r'duda\s*\(lean[^)]*\):?\s*',''),(r'\bno\s*\(lean[^)]*\)\.?\s*',''),(r'\(lean[^)]*\)',''),
 (r'\blean (no|s[ií]|firme)\b',''),
 (r'\(\d+\)\s*',''),(r'\d+[ªa]\s*pasadas?',''),(r'tras\s+\d+[ªa]?\s*pasadas?',''),
 (r'\(verificado[^)]*\)',''),(r'\bverificado 2026\b',''),(r'\(verificado\)',''),
 (r',?\s*decisi[oó]n del equipo\.?',''),(r'\s*[—–-]?\s*confirmado por el equipo\.?',''),
 (r'\(bbdd oficial\)',''),(r'cita verbatim','evidencia'),
 (r"\s*\(?usa_IA_en_proceso\s*'?[^'.,;)]*'?\)?",''),(r"\s*\(?rol_IA\s*'?[^'.,;)]*'?\)?",''),
 (r'→\s*(entra|no|s[ií])\b',''),(r'\s*→\s*',' '),
 (r'\bla regla de reingreso\b','el criterio de inclusión'),(r'\bregla de reingreso\b','criterio de inclusión'),
]
# Siglas reales que se preservan al bajar mayúsculas (todo lo demás en GRITO se pasa a minúscula).
_KEEP={"IA","NLP","ML","LLM","PLN","OCR","AI","PDM","PND","PEN","COCODES","COMUDES","SEGEPLAN",
 "CNE","ONPE","TSE","INE","JNE","CDMX","NDTS","OGP","USP","UAI","UNAB","GEMA","UNICEF","UNESCO",
 "PNUD","UNDP","UNFPA","DNP","DPS","BID","CAF","ANTAI","DCI","CGU","CGR","SDP","POT","PPA","SECOP",
 "COVID","TIC","DPPA","IPP","LUC","UDELAR","SISBEN","ECHO","PAGA","MPAAI","ADIP","GENIA","ONU","UE",
 "EU","OCDE","OSF","BBDD","PLADECO","ODS","ECQQ","SGD","CIDE","AWS","API","PWA","SMS","FAQ","OP","PP"}
def limpiar(t):
    """Deja el texto en lenguaje normal para partners (sin 'lean no', 'Nª pasada', nombres de campo,
    mayúsculas gritadas ni jerga interna); respeta las siglas reales."""
    if not t: return ""
    t=re.sub(r'\s+',' ',str(t)).strip()
    for pat,rep in _PAT: t=re.sub(pat,rep,t,flags=re.I)
    t=re.sub(r'\b[A-ZÁÉÍÓÚÑ]{2,}\b',lambda m:m.group(0) if m.group(0) in _KEEP else m.group(0).lower(),t)
    t=re.sub(r'\s+',' ',t).strip(' .:;,-–—')
    t=re.sub(r'^[):.,;\s]+','',t)
    if t: t=t[0].upper()+t[1:]
    if t and not t.endswith(('.','!','?')): t+="."
    return t


def estado(d):
    cid=d["caso_id"]
    if cid in eps.EXCLUIR or not eps.is_in(d): return "NO"
    if cid in eps.RESCATE_ENTRA: return "SÍ"          # ENTRA explícito (aunque la ficha diga DUDA)
    if cid in eps.RECLASIF_DUDA or cid in eps.DUDA_REVISAR: return "DUDA"
    if eps.is_duda(d): return "DUDA"
    return "SÍ"


def motivo(d):
    cid=d["caso_id"]
    if cid in eps.EXCLUIR: return eps.EXCLUIR[cid]
    if cid in eps.RESCATE_ENTRA: return eps.RESCATE_ENTRA[cid]
    if not eps.is_in(d):
        return re.sub(r'\s+',' ',(d.get("motivo_exclusion_2025") or d.get("justificacion_elegibilidad") or "").strip())
    if cid in eps.DUDA_REVISAR: return eps.DUDA_REVISAR[cid]
    if cid in eps.RECLASIF_DUDA: return eps.RECLASIF_DUDA[cid]
    if eps.is_duda(d): return "Pendiente de validación: confirmar si hay IA en el proceso."
    if d.get("cuenta_como_iniciativa") is False:
        return "Cuenta junto con su par (no se suma como iniciativa aparte)."
    return ""


def descripcion(d):
    # texto completo (sin truncar), solo normalizando espacios en blanco
    p=(d.get("proceso_participativo") or d.get("justificacion_elegibilidad") or "").strip()
    return re.sub(r'\s+',' ',p)


def fuente(d):
    for s in (d.get("fuentes") or []):
        u=(s.get("url") or "").strip()
        if URLRE.match(u): return u
    return ""


def tab_name(pais):
    nom=PAIS_NOMBRE.get(pais,pais)
    n=f"{pais} - {nom}" if pais!="LATAM" else "LATAM - Regional"
    return n[:31]


def main():
    fichas=[json.load(open(f,encoding="utf-8")) for f in sorted(glob.glob(os.path.join(ROOT,"data/fichas/*_detalle.json")))]
    porpais={}
    for d in fichas: porpais.setdefault(str(d.get("pais")),[]).append(d)
    # los 20 países ILIA (con o sin casos). No se incluye LATAM/Regional (a pedido).
    paises=list(PAISES_ILIA)
    sin_casos=[p for p in PAISES_ILIA if not porpais.get(p)]

    wb=Workbook(); wb.remove(wb.active)

    # ---------- Portada / índice ----------
    ws=wb.create_sheet("Instrucciones")
    filas=[
     ["VALIDACIÓN POR PAÍS — IA en Participación Ciudadana (ILIA 2026)"],
     ["",""],
     ["Qué es","Inventario de casos por país. Una pestaña por país. Por favor valide los casos de su país."],
     ["Qué revisar","1) ¿El caso EXISTE y está bien descrito?  2) ¿La fuente es correcta?  3) ¿Está bien la decisión de incluir (SÍ) o no (NO)?  4) ¿Falta algún caso?"],
     ["Cómo responder","Use la última columna «Comentario / corrección» para confirmar («OK») o corregir. Puede agregar filas al final con casos nuevos."],
     ["Criterio de inclusión","ENTRA si es un proceso de participación ciudadana (consulta, presupuesto participativo, mini-público, referendo, gobernanza colaborativa) que usa IA en alguna etapa (incluido el apoyo logístico). NO entra: civic tech de servicio/reporte, atención ciudadana, o voto/conteo electoral."],
     ["Significado de la columna «¿Se incluye?»","SÍ = entra al indicador · NO = queda fuera (ver Motivo) · DUDA = pendiente de validar."],
     ["",""],
     ["Cobertura","Los 20 países del ILIA tienen pestaña. Los que no tienen casos identificados este ciclo se marcan «SIN CASOS» (por favor confirme si conoce alguno)."],
     ["",""],
     ["ÍNDICE (20 países ILIA + Regional)","País — casos (de los cuales SÍ / DUDA / NO)"],
    ]
    for row in filas: ws.append(row)
    for p in paises:
        cs=porpais.get(p,[])
        if not cs:
            ws.append([f"{p} — {PAIS_NOMBRE.get(p,p)}", "SIN CASOS identificados este ciclo"]); continue
        nsi=sum(1 for d in cs if estado(d)=="SÍ"); nd=sum(1 for d in cs if estado(d)=="DUDA"); nno=sum(1 for d in cs if estado(d)=="NO")
        ws.append([f"{p} — {PAIS_NOMBRE.get(p,p)}", f"{len(cs)} casos  (SÍ {nsi} · DUDA {nd} · NO {nno})"])
    if sin_casos:
        ws.append(["",""])
        ws.append(["Países SIN casos", ", ".join(f"{p} ({PAIS_NOMBRE.get(p,p)})" for p in sin_casos)])
    ws.column_dimensions["A"].width=34; ws.column_dimensions["B"].width=100
    for r in range(1,ws.max_row+1):
        ws.cell(row=r,column=1).font=Font(bold=True); ws.cell(row=r,column=1).alignment=TL; ws.cell(row=r,column=2).alignment=TL
    ws["A1"].font=Font(bold=True,size=13)

    # ---------- una pestaña por país ----------
    cols=["Caso","Descripción breve","Fuente (URL validada)","¿Se incluye?","Motivo (si NO/DUDA)","Comentario / corrección (partner)"]
    for p in paises:
        ws=wb.create_sheet(tab_name(p))
        ws.append(cols)
        casos_p=porpais.get(p,[])
        if not casos_p:
            ws.append(["(sin casos identificados este ciclo)",
                       "No se identificaron casos de IA en participación ciudadana para este país. Si conoce alguno, agréguelo en las filas de abajo.",
                       "", "—", "", ""])
        for d in sorted(casos_p, key=lambda x:(estado(x)!="SÍ", str(x.get("nombre_caso")))):
            ws.append([d.get("nombre_caso") or "", limpiar(descripcion(d)), fuente(d), estado(d), limpiar(motivo(d)), ""])
        # estilo cabecera
        for c in range(1,len(cols)+1):
            cell=ws.cell(row=1,column=c); cell.fill=AZUL; cell.font=WB; cell.alignment=CEN; cell.border=BOR
        ws.row_dimensions[1].height=30; ws.freeze_panes="A2"
        ws.auto_filter.ref=f"A1:{get_column_letter(len(cols))}{ws.max_row}"
        widths=[34,64,46,12,54,32]
        for i,w in enumerate(widths,1): ws.column_dimensions[get_column_letter(i)].width=w
        for r in range(2,ws.max_row+1):
            for c in range(1,len(cols)+1):
                ws.cell(row=r,column=c).alignment=TL; ws.cell(row=r,column=c).border=BOR
            inc=ws.cell(row=r,column=4); v=str(inc.value); inc.alignment=CEN; inc.font=Font(bold=True)
            inc.fill=VERDE if v=="SÍ" else ROJO if v=="NO" else AMBAR

    dst=os.path.join(ROOT,"data/gates/planilla_validacion_por_pais_ILIA2026.xlsx"); wb.save(dst)
    shown=[d for d in fichas if str(d.get("pais")) in PAISES_ILIA]   # sin LATAM
    tot=len(shown); nsi=sum(1 for d in shown if estado(d)=="SÍ"); nd=sum(1 for d in shown if estado(d)=="DUDA")
    print(f"[ok] {dst}")
    print(f"     {len(paises)} pestañas de país · {tot} casos mostrados (SÍ {nsi} · DUDA {nd} · NO {tot-nsi-nd}) · LATAM excluido")
    return 0


if __name__ == "__main__":
    sys.exit(main())
