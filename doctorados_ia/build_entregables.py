#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera los entregables para traspaso (Nicole) a partir de clasificacion.csv:
  - entregables/Planilla_Doctorados_IA_QS2026.xlsx  (multi-hoja, con colores)
  - entregables/Informe_Doctorados_IA_QS2026.docx   (informe + pasos a seguir)
Los conteos se CALCULAN desde el CSV (nada a mano).
"""
import csv, os, datetime
from collections import defaultdict, OrderedDict

BASE = os.path.dirname(os.path.abspath(__file__))
CSV_CLAS = os.path.join(BASE, "clasificacion.csv")
CSV_UNIV = os.path.join(BASE, "universidades_qs2026.csv")
OUT = os.path.join(BASE, "entregables")
os.makedirs(OUT, exist_ok=True)

PAIS_ORDER = ["Alemania", "España", "Portugal", "Singapur", "Estonia"]

def read_csv(path):
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))

rows = read_csv(CSV_CLAS)
univ = read_csv(CSV_UNIV)

# ---- Conteos ----
counts = OrderedDict((p, {"CUMPLE":0,"PARCIAL":0,"NO_CUMPLE":0}) for p in PAIS_ORDER)
for r in rows:
    counts[r["pais"]][r["clasificacion"]] += 1
tot = {"CUMPLE":0,"PARCIAL":0,"NO_CUMPLE":0}
for p in PAIS_ORDER:
    for k in tot: tot[k]+=counts[p][k]
def forma(d): return d["CUMPLE"]+d["PARCIAL"]
N = len(rows)
print("=== CONTEOS (desde CSV) ===")
for p in PAIS_ORDER:
    c=counts[p]; print(f"{p:10s} CUMPLE={c['CUMPLE']:3d} PARCIAL={c['PARCIAL']:3d} NO={c['NO_CUMPLE']:2d} forma={forma(c)}")
print(f"{'TOTAL':10s} CUMPLE={tot['CUMPLE']:3d} PARCIAL={tot['PARCIAL']:3d} NO={tot['NO_CUMPLE']:2d} forma={forma(tot)} N={N}")

NO_CUMPLE_ROWS = [r for r in rows if r["clasificacion"]=="NO_CUMPLE"]

# =====================================================================
# 1) EXCEL
# =====================================================================
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

GREEN  = PatternFill("solid", fgColor="C6EFCE")
YELLOW = PatternFill("solid", fgColor="FFEB9C")
RED    = PatternFill("solid", fgColor="FFC7CE")
HEADF  = PatternFill("solid", fgColor="305496")
HEADFONT = Font(bold=True, color="FFFFFF")
TITLEFONT= Font(bold=True, size=14)
THIN = Border(*[Side(style="thin", color="D9D9D9")]*4)
def fill_for(c): return {"CUMPLE":GREEN,"PARCIAL":YELLOW,"NO_CUMPLE":RED}.get(c)

wb = Workbook()

# -- Hoja Resumen --
ws = wb.active; ws.title = "Resumen"
ws["A1"]="Indicador ILIA — Programas de doctorado de IA (paises extra, QS 2026)"; ws["A1"].font=TITLEFONT
ws["A2"]=f"Generado: {datetime.date.today().isoformat()}  ·  Metodo: solo busqueda web (sin acceso a paginas)  ·  Fuente de cada fila en hoja 'Clasificacion'"
ws["A2"].font=Font(italic=True, size=9)
ws["A4"]=f"CIFRA PRINCIPAL: de {N} universidades en QS 2026, {forma(tot)} tienen >=1 doctorado que forma competencias en IA"
ws["A4"].font=Font(bold=True, size=12)
ws["A5"]=f"  -  Conteo ESTRICTO (solo CUMPLE): {tot['CUMPLE']}     -  Conteo AMPLIO (CUMPLE+PARCIAL): {forma(tot)}     -  NO CUMPLE: {tot['NO_CUMPLE']}"
hdr=["Pais","Univ. QS 2026","CUMPLE","PARCIAL","NO CUMPLE","Forman compet. (C+P)"]
r0=7
for j,h in enumerate(hdr,1):
    c=ws.cell(r0,j,h); c.fill=HEADF; c.font=HEADFONT; c.alignment=Alignment(horizontal="center")
for i,p in enumerate(PAIS_ORDER):
    c=counts[p]; n=c["CUMPLE"]+c["PARCIAL"]+c["NO_CUMPLE"]
    vals=[p,n,c["CUMPLE"],c["PARCIAL"],c["NO_CUMPLE"],forma(c)]
    for j,v in enumerate(vals,1):
        cell=ws.cell(r0+1+i,j,v); cell.border=THIN
        if j>=3: cell.alignment=Alignment(horizontal="center")
trow=r0+1+len(PAIS_ORDER)
vals=["TOTAL",N,tot["CUMPLE"],tot["PARCIAL"],tot["NO_CUMPLE"],forma(tot)]
for j,v in enumerate(vals,1):
    cell=ws.cell(trow,j,v); cell.font=Font(bold=True); cell.fill=PatternFill("solid",fgColor="DDEBF7"); cell.border=THIN
    if j>=3: cell.alignment=Alignment(horizontal="center")
notes=[
 "", "Regla de clasificacion (uniforme en los 5 paises):",
 "   CUMPLE  = C1 (lineas de investigacion en IA) Y (C2 perfil/objetivos IA  O  C3 plan con >=3 cursos de IA)",
 "   PARCIAL = solo C1 (declara lineas de IA) pero sin C2/C3 verificable",
 "   NO CUMPLE = sin programa de doctorado Tec/Ing con lineas de IA",
 "",
 "PARCIAL no significa que NO forme competencias en IA: significa que la evidencia disponible (solo snippets de",
 "busqueda, sin abrir el plan de estudios) no permite confirmar C3 con el rigor exigido. Por eso el conteo AMPLIO",
 "(CUMPLE+PARCIAL) es la cifra robusta y comparable entre paises; el split CUMPLE/PARCIAL es provisional.",
 "",
 "DECISION PENDIENTE DEL OPERADOR: publicar la cifra ESTRICTA (solo CUMPLE) o AMPLIA (CUMPLE+PARCIAL).",
]
for k,t in enumerate(notes):
    cell=ws.cell(trow+2+k,1,t)
    if t.endswith(":") or t.startswith("DECISION"): cell.font=Font(bold=True)
ws.column_dimensions["A"].width=70
for col in "BCDEF": ws.column_dimensions[col].width=15

# -- Hoja Clasificacion (103 filas, coloreada) --
ws2=wb.create_sheet("Clasificacion")
cols=list(rows[0].keys())
for j,h in enumerate(cols,1):
    c=ws2.cell(1,j,h); c.fill=HEADF; c.font=HEADFONT; c.alignment=Alignment(horizontal="center",wrap_text=True)
ci=cols.index("clasificacion")
for i,r in enumerate(rows,2):
    for j,h in enumerate(cols,1):
        cell=ws2.cell(i,j,r[h]); cell.border=THIN; cell.alignment=Alignment(vertical="top",wrap_text=True)
    f=fill_for(r["clasificacion"])
    if f: ws2.cell(i,ci+1).fill=f
ws2.freeze_panes="A2"; ws2.auto_filter.ref=f"A1:{get_column_letter(len(cols))}{len(rows)+1}"
widths={"pais":10,"universidad":34,"qs_rank_2026":11,"facultad_escuela":34,"programa_doctorado":40,
        "c1_lineas_IA":8,"c2_objetivos_perfil":10,"c3_plan_min3_cursos":11,"c4_tesis_IA":8,
        "clasificacion":12,"forma_competencias_0_1":10,"confianza":11,"requiere_acceso_manual":48,"fuente_principal":46}
for j,h in enumerate(cols,1): ws2.column_dimensions[get_column_letter(j)].width=widths.get(h,16)

# -- Hoja Universo QS --
ws3=wb.create_sheet("Universo_QS2026")
ucols=list(univ[0].keys())
for j,h in enumerate(ucols,1):
    c=ws3.cell(1,j,h); c.fill=HEADF; c.font=HEADFONT
for i,r in enumerate(univ,2):
    for j,h in enumerate(ucols,1): ws3.cell(i,j,r[h]).border=THIN
ws3.freeze_panes="A2"
for j,h in enumerate(ucols,1): ws3.column_dimensions[get_column_letter(j)].width={"universidad":40,"fuente_rank":40,"confianza_rank":24}.get(h,14)

# -- Hoja Dudas / acceso manual --
ws4=wb.create_sheet("Dudas_AccesoManual")
ws4["A1"]="Items que requieren ACCESO MANUAL / verificacion (ver tambien columna 'requiere_acceso_manual')"; ws4["A1"].font=Font(bold=True)
dh=["Prioridad","Pais","Universidad","Que verificar","Efecto si cambia"]
for j,h in enumerate(dh,1):
    c=ws4.cell(3,j,h); c.fill=HEADF; c.font=HEADFONT
dudas=[
 ["ALTA","España","Universidad de Cantabria","Confirmar PERTENENCIA a QS World 2026 (aparece en by-subject); si no esta, sustituir","Cambia el universo de 38"],
 ["ALTA","Alemania","Cola QS (TUHH, RPTU, Augsburg, Bielefeld, Hohenheim)","Cotejar membresia/posicion en QS oficial; posible debut TU Hamburg-Harburg","Cambia el universo de 49"],
 ["MEDIA","(varias)","ES: UAB,UAM,UCM,UGR,UPF,UPV,UV,UNAV,EHU,US,USC,UDC,UNIOVI,UMA,UM,UIB,URJC; DE: las 19 CUMPLE","Abrir el plan de estudios / perfil de egreso para CONFIRMAR C2/C3 (ahora inferido de centro de IA)","CUMPLE<->PARCIAL"],
 ["MEDIA","España","12 reclasificadas (UNIZAR,URV,UCLM,UA,UVigo,UCO,ULL,ULPGC,URL,Comillas,Deusto,UJI)","Abrir perfil/actividades formativas: si declara IA o >=3 cursos -> sube a CUMPLE","PARCIAL->CUMPLE"],
 ["BAJA","(todos)","Ranks QS individuales (bandas >=600)","Fijar el puesto exacto en topuniversities.com ?countries=<de|es|pt|ee|sg>","Solo precision del rank"],
 ["INFO","Portugal","Universidade Catolica","VALIDADO: ICCD Braga solo grado/master, sin doctorado -> NO CUMPLE","(resuelto)"],
 ["INFO","España","IE University","VALIDADO: Sci-Tech solo grado/master; PhD solo en Business (excluido) -> NO CUMPLE","(resuelto)"],
 ["INFO","Alemania","Hohenheim","VALIDADO: AIDAHO es certificado, no doctorado -> NO CUMPLE","(resuelto)"],
]
for i,d in enumerate(dudas,4):
    for j,v in enumerate(d,1):
        cell=ws4.cell(i,j,v); cell.border=THIN; cell.alignment=Alignment(vertical="top",wrap_text=True)
ws4.column_dimensions["A"].width=10; ws4.column_dimensions["B"].width=12; ws4.column_dimensions["C"].width=34
ws4.column_dimensions["D"].width=60; ws4.column_dimensions["E"].width=26

xlsx_path=os.path.join(OUT,"Planilla_Doctorados_IA_QS2026.xlsx")
wb.save(xlsx_path); print("XLSX:", xlsx_path)

# =====================================================================
# 2) WORD
# =====================================================================
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc=Document()
st=doc.styles["Normal"]; st.font.name="Calibri"; st.font.size=Pt(10.5)

def H(t,l=1): doc.add_heading(t,level=l)
def P(t,bold=False,italic=False):
    p=doc.add_paragraph(); r=p.add_run(t); r.bold=bold; r.italic=italic; return p
def BUL(t): doc.add_paragraph(t, style="List Bullet")
def NUM(t): doc.add_paragraph(t, style="List Number")

title=doc.add_heading("Indicador ILIA — Programas de doctorado de IA (paises extra)",0)
P("Informe de resultados y guia de traspaso  ·  QS World University Rankings 2026  ·  "
  f"{datetime.date.today().strftime('%d-%m-%Y')}", italic=True)

H("1. Que es y alcance",1)
P("Indicador: cantidad de programas de doctorado que FORMAN COMPETENCIAS EN INTELIGENCIA ARTIFICIAL (IA) "
  "en las universidades incluidas en el QS World University Rankings 2026, para 5 paises de referencia "
  "(\"paises extra\"):")
BUL("Alemania (49 universidades), España (38), Portugal (9), Singapur (4), Estonia (3). Total: 103.")
P("Se revisan programas de doctorado de facultades de Tecnologia/Ingenieria (informatica, ciencia de datos, "
  "telecomunicaciones, etc.), excluyendo programas de Negocios/Economia.")

H("2. Metodologia (criterios y escala)",1)
P("Cada programa se evaluo con 4 criterios y se clasifico en 3 categorias:")
BUL("C1 - Lineas de investigacion en IA (criterio base).")
BUL("C2 - Objetivos / perfil de egreso que declaran competencias en IA.")
BUL("C3 - Plan de estudios con al menos 3 cursos de IA (criterio mas fuerte).")
BUL("C4 - Tesis orientadas a IA (criterio complementario opcional).")
P("Regla de clasificacion aplicada de forma UNIFORME a los 5 paises:", bold=True)
BUL("CUMPLE  = C1 Y (C2 o C3).")
BUL("PARCIAL = solo C1 (declara lineas de IA, pero sin C2/C3 verificable).")
BUL("NO CUMPLE = sin doctorado Tec/Ing con lineas de IA.")

H("3. Como se hizo esta corrida (y una limitacion importante)",1)
P("LIMITACION DE RAIZ:", bold=True)
P("El entorno de trabajo automatico NO pudo abrir paginas web (todas las descargas directas daban error 403). "
  "Se trabajo UNICAMENTE con BUSQUEDAS web (titulos, fragmentos y URLs). Consecuencia: el criterio C3 (>=3 cursos "
  "del plan de estudios) casi nunca es verificable sin abrir el plan -> muchos programas quedan en PARCIAL y la "
  "frontera CUMPLE/PARCIAL es PROVISIONAL. Por eso cada fila lleva su URL fuente, para verificacion manual.")
P("Trabajo realizado:")
BUL("Se fijo el universo QS 2026 por pais y se clasifico universidad por universidad con su evidencia y fuentes.")
BUL("Para los dos paises grandes (España y Alemania) se usaron agentes de investigacion en paralelo; su salida fue "
    "revisada y reconciliada. La clasificacion de España se NORMALIZO a la regla comun (12 casos pasaron de CUMPLE a "
    "PARCIAL por tener solo C1).")
BUL("Se hizo una ronda de VALIDACION dirigida que resolvio los casos limite (ver seccion 5).")

H("4. Resultados",1)
P(f"De {N} universidades, {forma(tot)} tienen al menos un doctorado que forma competencias en IA.", bold=True)
P(f"Cifra ESTRICTA (solo CUMPLE) = {tot['CUMPLE']}   ·   Cifra AMPLIA (CUMPLE+PARCIAL) = {forma(tot)}   ·   "
  f"NO CUMPLE = {tot['NO_CUMPLE']}.")
# tabla resumen
t=doc.add_table(rows=1, cols=6); t.style="Light Grid Accent 1"
for j,h in enumerate(["Pais","QS 2026","CUMPLE","PARCIAL","NO CUMPLE","Forman comp."]):
    t.rows[0].cells[j].paragraphs[0].add_run(h).bold=True
for p in PAIS_ORDER:
    c=counts[p]; n=c["CUMPLE"]+c["PARCIAL"]+c["NO_CUMPLE"]
    cells=t.add_row().cells
    for j,v in enumerate([p,n,c["CUMPLE"],c["PARCIAL"],c["NO_CUMPLE"],forma(c)]): cells[j].text=str(v)
cells=t.add_row().cells
for j,v in enumerate(["TOTAL",N,tot["CUMPLE"],tot["PARCIAL"],tot["NO_CUMPLE"],forma(tot)]):
    r=cells[j].paragraphs[0].add_run(str(v)); r.bold=True
P("")
P("Patron observado (coherente con la metodologia): Singapur y Portugal tienen doctorados con coursework "
  "estructurado -> se evidencia C3 -> CUMPLE. Alemania y Estonia son de modelo research-based (Promotion / "
  "investigacion individual) -> C1 casi universal via centros de IA, pero C3 rara vez publico -> predominio de "
  "PARCIAL. España es mixto (CUMPLE por programas dedicados de IA o perfil/centro de IA explicito).")

H("5. Casos validados y los 3 NO CUMPLE",1)
P("La ronda de validacion confirmo o reclasifico los casos limite:")
BUL("España - UEM (Univ. Europea de Madrid): SI tiene 'Doctorado en Ingenieria de Control y Sistemas Inteligentes' "
    "-> paso de NO CUMPLE a PARCIAL.")
BUL("Alemania - Potsdam (Hasso Plattner Institute): escuela doctoral con curriculo estructurado y research school de "
    "metodos de IA -> paso de PARCIAL a CUMPLE.")
BUL("España - UCAM: confirmado Doctorado en Ing. Informatica + grupo UKEIM (IA) -> PARCIAL.")
BUL("Estonia: confirmadas las 3 universidades del ranking general (Tartu, TalTech, Tallinn University); la Univ. de "
    "Ciencias de la Vida NO esta en el ranking general. TalTech rank = 635.")
P(f"Los {tot['NO_CUMPLE']} NO CUMPLE (validados) son:", bold=True)
for r in NO_CUMPLE_ROWS:
    BUL(f"{r['pais']} - {r['universidad']}: {r['requiere_acceso_manual'].replace('[Validado] ','').replace('[Validado] ','')}")

H("6. Que debe hacer Nicole (pasos siguientes)",1)
NUM("Decidir la cifra a publicar: ESTRICTA (solo CUMPLE = %d) o AMPLIA (CUMPLE+PARCIAL = %d). Recomendado: reportar "
    "ambas y elegir segun el criterio del indice." % (tot["CUMPLE"], forma(tot)))
NUM("Validar a mano los items de la hoja 'Dudas_AccesoManual' de la planilla, por prioridad. Cada fila de la hoja "
    "'Clasificacion' trae su URL fuente y la columna 'requiere_acceso_manual' con que abrir.")
NUM("Confirmar C3 (planes de estudio) de las CUMPLE marcadas (sobre todo Alemania y España): abrir el plan/curriculo "
    "y contar >=3 cursos de IA. Si no se confirma, esa universidad baja a PARCIAL.")
NUM("Confirmar membresias/posiciones dudosas en el QS oficial (topuniversities.com, filtro por pais): España - "
    "Universidad de Cantabria; Alemania - cola del ranking (posible debut TU Hamburg-Harburg).")
NUM("Revisar las 12 universidades españolas reclasificadas (CUMPLE->PARCIAL): si su perfil de egreso declara IA o "
    ">=3 cursos, suben a CUMPLE.")
NUM("Fijar los ranks QS individuales aproximados (bandas >=600) si se necesita precision por universidad.")

H("7. Archivos entregados",1)
BUL("Planilla_Doctorados_IA_QS2026.xlsx - hojas: Resumen, Clasificacion (103 filas con C1-C4, clasificacion, "
    "confianza, fuente y flag de acceso manual; coloreada por resultado), Universo_QS2026, Dudas_AccesoManual.")
BUL("Informe_Doctorados_IA_QS2026.docx - este documento.")
BUL("Repositorio (carpeta doctorados_ia/): METODOLOGIA.md, paises/*.md (evidencia y fuentes por universidad), "
    "clasificacion.csv, RESUMEN.md, DUDAS_ACCESO_MANUAL.md.")

H("Anexo. Clasificacion completa (103 universidades)",1)
P("Detalle, evidencia y fuentes en la planilla (hoja 'Clasificacion'). Resumen:")
ta=doc.add_table(rows=1, cols=4); ta.style="Light Grid Accent 1"
for j,h in enumerate(["Pais","Universidad","Programa de doctorado","Clasif."]):
    ta.rows[0].cells[j].paragraphs[0].add_run(h).bold=True
for r in rows:
    cells=ta.add_row().cells
    cells[0].text=r["pais"]; cells[1].text=r["universidad"]; cells[2].text=r["programa_doctorado"]; cells[3].text=r["clasificacion"]
for col_w,idx in [(0.8,0),(2.0,1),(2.6,2),(0.9,3)]:
    for row in ta.rows:
        row.cells[idx].width=Inches(col_w)

docx_path=os.path.join(OUT,"Informe_Doctorados_IA_QS2026.docx")
doc.save(docx_path); print("DOCX:", docx_path)
print("OK")
