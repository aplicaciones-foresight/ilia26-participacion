#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_entregables.py — Pipeline ILIA 2026 (IA en Participación Ciudadana)
==========================================================================
Construye, de forma DETERMINÍSTICA y reproducible, los dos entregables
post-validación a partir de los insumos del repositorio:

  1) data/final/BBDD_casos_incluidos_ILIA2026.xlsx
       Pestaña «1 · BBDD Casos incluidos»  (28 casos, coding + columnas
       derivadas por FÓRMULA auditable)
       Pestaña «2 · Índice por país»        (20 países, índice CENIA v2,
       TODA celda por fórmula que referencia la pestaña 1 y las grillas)

  2) data/final/Casos_excluidos_ILIA2026.xlsx
       Pestaña «Casos excluidos»            (79 casos, clasificados por
       origen, con detalles narrados sólo desde los insumos)

REGLAS DE ORO respetadas:
  - Ningún número sale de memoria: todo se lee de los insumos.
  - Los cálculos del Excel son FÓRMULAS (nunca valores pegados).
  - No se infiere nada que no esté en el texto de los insumos.

Fuente principal (5 pestañas):
  scratchpad/validacion_casos_1.xlsx  (copiada al repo como
  data/final/insumo_Validacion_Casos_1.xlsx para trazabilidad).

Uso:  python src/build_entregables.py
Requisitos: openpyxl. Tras generar, correr recalc.py sobre ambos archivos.
"""
import os, shutil, unicodedata
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# --------------------------------------------------------------------------
# 0. Rutas
# --------------------------------------------------------------------------
REPO = "/home/user/ilia26-participacion"
SCRATCH = ("/tmp/claude-0/-home-user-ilia26-participacion/"
           "c95dac1c-c408-576c-8cbf-91ad1ddcb801/scratchpad")
INSUMO_SRC = os.path.join(SCRATCH, "validacion_casos_1.xlsx")
FINAL_DIR = os.path.join(REPO, "data", "final")
INSUMO_REPO = os.path.join(FINAL_DIR, "insumo_Validacion_Casos_1.xlsx")
BASE_XLSX = os.path.join(REPO, "data", "baseline", "BBDD_IA_Participacion_2025.xlsx")
CANDIDATOS = os.path.join(REPO, "data", "candidatos", "candidatos.csv")
HALLAZGOS = os.path.join(REPO, "data", "candidatos", "hallazgos_web.csv")
PLANILLA_VAL = os.path.join(REPO, "data", "gates", "planilla_validacion_ILIA2026.xlsx")

OUT1 = os.path.join(FINAL_DIR, "BBDD_casos_incluidos_ILIA2026.xlsx")
OUT2 = os.path.join(FINAL_DIR, "Casos_excluidos_ILIA2026.xlsx")

# --------------------------------------------------------------------------
# 1. Constantes de metodología (CENIA v2) — todo desde config/insumo
# --------------------------------------------------------------------------
PAISES = ["AR","BO","BR","CL","CO","CR","CU","DO","EC","GT",
          "HN","JM","MX","PA","PE","PY","SV","TT","UY","VE"]
ANIO_REF = 2026            # config.yaml continuidad.anio_referencia_ciclo
CADUCIDAD = 2              # config.yaml continuidad.caducidad_anuncio_anios
# Umbrales de Cantidad (config.yaml redondeo/thresholds): 0→0,1-3→25,4-6→50,7-9→75,10+→100
THRESHOLDS = [(0,0,0),(1,3,25),(4,6,50),(7,9,75),(10,None,100)]

# Taxonomías (tokens en minúscula, tal como aparecen normalizados)
TP_TOKENS = ["participación digital","gobernanza colaborativa","mini públicos",
             "referendos e iniciativas populares","presupuestos participativos"]
TP_LABEL = ["Participación Digital","Gobernanza Colaborativa","Mini públicos",
            "Referendos e Iniciativas Populares","Presupuestos Participativos"]
ET_LABEL = ["Planificación","Implementación","Análisis","Traducción Política"]
# 7 categorías de convocante en orden canónico + código
CONV = [("gobierno local","GL"),("gobierno nacional","GN"),
        ("otra institución pública","OIP"),("empresa","EMP"),
        ("universidad","UNI"),("sociedad civil","SC"),
        ("organización internacional","OI")]
CONV_GUB = [0,1,2]        # índices gubernamentales (GL,GN,OIP)
CONV_NOGUB = [3,4,5,6]    # índices no gubernamentales (EMP,UNI,SC,OI)
DEV_TOKENS = ["privado","academia","gobierno","sociedad civil"]
DEV_LABEL = ["Privado","Academia","Gobierno","Sociedad Civil"]

# --------------------------------------------------------------------------
# 2. Estilos (Arial en todo)
# --------------------------------------------------------------------------
def F(bold=False, color="000000", size=10, italic=False):
    return Font(name="Arial", size=size, bold=bold, color=color, italic=italic)
BLUE = "0000FF"   # dato validado (input)
BLACK = "000000"  # fórmula
WHITE = "FFFFFF"
def fill(hexc): return PatternFill("solid", fgColor=hexc)
FILL_A = fill("1F4E79")   # Identificación (azul oscuro)
FILL_B = fill("385723")   # Detalle narrativo (verde oscuro)
FILL_C = fill("833C00")   # Coding validado (marrón)
FILL_D = fill("404040")   # Derivadas (gris)
FILL_PARAM = fill("FFF2CC")   # amarillo suave (supuestos/parámetros)
FILL_HL = fill("FCE4D6")      # resaltado indicador final
FILL_GRIDHDR = fill("D9E1F2")
FILL_TITLE = fill("1F4E79")
thin = Side(style="thin", color="BFBFBF")
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)
WRAP = Alignment(wrap_text=True, vertical="top")
CENTER = Alignment(horizontal="center", vertical="center")
CTOP = Alignment(horizontal="center", vertical="top")

def strip_accents(s):
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))
def norm_key(s):
    s = strip_accents(str(s or "").lower())
    for ch in "\"'’“”().,:;/+-–—": s = s.replace(ch, " ")
    return " ".join(s.split())

# --------------------------------------------------------------------------
# 3. Lectura de insumos
# --------------------------------------------------------------------------
def read_incluidos():
    """28 casos vigentes de «1 · Casos (incluidos)» (excluye 'Caso eliminado')."""
    wb = openpyxl.load_workbook(INSUMO_SRC, data_only=True)
    ws = wb["1 · Casos (incluidos)"]
    casos = []
    for r in range(2, ws.max_row+1):
        pais = ws.cell(r,3).value
        caso = ws.cell(r,4).value
        if not pais or not caso:            # filas 'Caso eliminado' → vacías
            continue
        def g(c):
            v = ws.cell(r,c).value
            return "" if v is None else v
        anio_raw = str(g(20)).strip()
        try: anio = int(float(anio_raw))
        except Exception: anio = anio_raw
        niv_raw = g(9)
        try: niv = int(float(niv_raw))
        except Exception: niv = niv_raw
        tia = g(16)
        tia = "" if str(tia).strip().lower() == "null" else tia   # PA: 'null' = 0 sistemas (se guarda literal 'null' abajo)
        casos.append(dict(
            pais=str(pais).strip(), caso=str(caso).strip(),
            accion=str(g(1)).strip(), confianza=str(g(6)).strip(),
            cuenta=str(g(5)).strip(), tipo_proceso=str(g(7)).strip(),
            etapas=str(g(8)).strip(), nivel=niv, continuidad=str(g(10)).strip(),
            convocante=str(g(11)).strip(), tipo_org=str(g(12)).strip(),
            rol_ia=str(g(13)).strip(), tipo_dev=str(g(14)).strip(),
            origen=str(g(15)).strip(), tipos_ia=str(g(16)).strip(),
            usa_llm=str(g(17)).strip(), proceso=str(g(18)).strip(),
            org=str(g(19)).strip(), anio=anio, urls=str(g(21)).strip(),
            caso_id=str(g(22)).strip(), comentarios=str(g(23)).strip(),
        ))
    return casos

def read_excluidos():
    """79 filas de «2 · Excluidos»: País|Caso|Bloque|Motivo|URL."""
    wb = openpyxl.load_workbook(INSUMO_SRC, data_only=True)
    ws = wb["2 · Excluidos"]
    rows = []
    for r in range(2, ws.max_row+1):
        pais = ws.cell(r,1).value; caso = ws.cell(r,2).value
        if not pais and not caso: continue
        rows.append(dict(
            pais=str(pais).strip() if pais else "",
            caso=str(caso).strip() if caso else "",
            bloque=str(ws.cell(r,3).value or "").strip(),
            motivo=str(ws.cell(r,4).value or "").strip(),
            url=str(ws.cell(r,5).value or "").strip(),
            _row=r))
    return rows

def read_evidencia():
    """Pestaña «3 · Evidencia y fuentes» → dict (pais,normcaso)->campos EV."""
    wb = openpyxl.load_workbook(INSUMO_SRC, data_only=True)
    ws = wb["3 · Evidencia y fuentes"]
    d = {}
    for r in range(2, ws.max_row+1):
        pais = ws.cell(r,1).value; caso = ws.cell(r,2).value
        if not pais or not caso: continue
        d[(str(pais).strip(), norm_key(caso))] = dict(
            usa_ia=str(ws.cell(r,9).value or "").strip(),
            rol_ia=str(ws.cell(r,10).value or "").strip(),
            etapas=str(ws.cell(r,5).value or "").strip(),
            convocante=str(ws.cell(r,8).value or "").strip(),
        )
    return d

def read_bbdd_casos():
    """28 casos incluidos 2025 (con 2 homónimos CL). Lista de dicts."""
    wb = openpyxl.load_workbook(BASE_XLSX, data_only=True)
    ws = wb["BBDD Casos"]
    out = []
    for r in range(2, ws.max_row+1):
        p = ws.cell(r,1).value; caso = ws.cell(r,2).value
        if not p or not caso: continue
        anio = ws.cell(r,3).value
        try: anio = int(float(anio)) if anio not in (None,"") else None
        except Exception: pass
        out.append(dict(pais=str(p).strip(), caso=str(caso).strip(),
                        anio=anio, desc=str(ws.cell(r,5).value or "").strip(),
                        org=str(ws.cell(r,6).value or "").strip(), _row=r))
    return out

def read_bbdd_excluidos():
    """49 exclusiones 2025. Lista de dicts."""
    wb = openpyxl.load_workbook(BASE_XLSX, data_only=True)
    ws = wb["BBDD Casos Excluidos"]
    out = []
    for r in range(2, ws.max_row+1):
        mot = ws.cell(r,1).value; p = ws.cell(r,2).value; tit = ws.cell(r,3).value
        if not p or not tit: continue
        anio = ws.cell(r,5).value
        out.append(dict(motivo=str(mot or "").strip(), pais=str(p).strip(),
                        caso=str(tit).strip(), desc=str(ws.cell(r,4).value or "").strip(),
                        anio=anio, _row=r))
    return out

def read_csv_simple(path):
    import csv
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))

def read_planilla_val():
    """dict (pais,normcaso)->'Qué es y cómo usa IA (evidencia)'."""
    wb = openpyxl.load_workbook(PLANILLA_VAL, data_only=True)
    ws = wb["Validación"]
    d = {}
    for r in range(2, ws.max_row+1):
        p = ws.cell(r,2).value; caso = ws.cell(r,3).value
        if not p or not caso: continue
        d[(str(p).strip(), norm_key(caso))] = str(ws.cell(r,5).value or "").strip()
    return d

# --------------------------------------------------------------------------
# 4. Clasificación de los 79 excluidos por ORIGEN (grupos 1/2/3)
# --------------------------------------------------------------------------
# Grupo 1: estaba INCLUIDO en la BBDD 2025 y se excluye en 2026 (12).
G1_KEYS = [("BR","participact"),("BR","colab"),
           ("CL","participacion ciudadana proceso constitucional"),
           ("CL","estrategia de gobierno digital"),
           ("CO","descongestion"),("CR","diara"),("CR","u-report"),
           ("DO","ciudadania"),("HN","redpublica"),("MX","sufragio seguro"),
           ("MX","presupuesto creces"),("PE","sistema de computo")]
ORIGEN = {
    1: "Base 2025 — estaba INCLUIDO, excluido en 2026",
    2: "Base 2025 — ya estaba EXCLUIDO, exclusión reconfirmada",
    3: "Nuevo 2026 — identificado en descubrimiento, no incluido",
}
def classify_group(row):
    b = row["bloque"]
    if b in ("Excluido 2025", "Excluido (revisar)"):
        return 2
    nk = norm_key(row["caso"])
    for p, kw in G1_KEYS:
        if row["pais"] == p and norm_key(kw) in nk:   # normalizar también la clave
            return 1
    return 3

# --------------------------------------------------------------------------
# 5. Motor de flags/normalización en PYTHON (sólo para el catálogo de
#    sistemas y para verificación de valores de control; el Excel usa fórmulas)
# --------------------------------------------------------------------------
def norm_field(s):
    s = str(s or "")
    s = s.replace("; ", ";").replace(", ", ";").replace(",", ";")
    return ";" + s.lower() + ";"

def sistemas_tokens(cell):
    """Tokens de 'Tipos/familia IA' (minúscula), excluye vacío y 'null'."""
    out = []
    for t in str(cell or "").replace("; ", ";").replace(", ", ";").replace(",", ";").split(";"):
        t = t.strip().lower()
        if t and t != "null":
            out.append(t)
    return out

def build_sistemas_catalog(casos):
    cat = []
    for c in casos:
        for t in sistemas_tokens(c["tipos_ia"]):
            if t not in cat: cat.append(t)
    return cat   # orden de primera aparición

# --------------------------------------------------------------------------
# 6. ENTREGABLE 1
# --------------------------------------------------------------------------
SH1 = "'1 · BBDD Casos incluidos'"
SH2 = "'2 · Índice por país'"

# Mapa de columnas de la pestaña 1 (1-indexado)
# Grupo A (5) | B (5) | C coding (12) | D derivadas (6 norm + 22 flags + 3)
COLS = []
def addcol(name, group):
    COLS.append((name, group)); return len(COLS)  # devuelve índice 1-based
# A Identificación
c_pais   = addcol("País (ISO-2)", "A")
c_caso   = addcol("Caso", "A")
c_casoid = addcol("caso_id", "A")
c_anio   = addcol("Año", "A")
c_conf   = addcol("Confianza", "A")
# B Detalle narrativo
c_desc   = addcol("Descripción del proceso", "B")
c_org    = addcol("Organización a cargo", "B")
c_notas  = addcol("Notas de validación", "B")
c_com    = addcol("Comentarios", "B")
c_urls   = addcol("URLs", "B")
# C Coding validado (azul)
c_cuenta = addcol("Cuenta como iniciativa", "C")
c_tp     = addcol("Tipo de proceso", "C")
c_et     = addcol("Etapas uso IA", "C")
c_niv    = addcol("Nivel (0-3)", "C")
c_cont   = addcol("Continuidad (etiqueta)", "C")
c_conv   = addcol("Convocante (7-cat)", "C")
c_torg   = addcol("Tipo org", "C")
c_rol    = addcol("Rol IA", "C")
c_dev    = addcol("Tipo desarrollador IA", "C")
c_orig   = addcol("Origen desarrollador", "C")
c_tia    = addcol("Tipos/familia IA", "C")
c_llm    = addcol("Usa LLM", "C")
# D Derivadas — normalización (fórmula, negro)
c_nproc  = addcol("norm · Tipo de proceso", "D")
c_netap  = addcol("norm · Etapas", "D")
c_nconv  = addcol("norm · Convocante", "D")
c_ndev   = addcol("norm · Tipo desarrollador", "D")
c_norig  = addcol("norm · Origen desarrollador", "D")
c_nsis   = addcol("norm · Tipos/familia IA", "D")
# D flags Tipo de proceso (5)
c_tp_flag = [addcol(f"TP: {TP_LABEL[i]} (0/1)", "D") for i in range(5)]
# D flags Etapa (4)
c_et_flag = [addcol(f"ET: {ET_LABEL[i]} (0/1)", "D") for i in range(4)]
# D flags Convocante (7)
c_cv_flag = [addcol(f"CV: {CONV[i][0]} [{CONV[i][1]}] (0/1)", "D") for i in range(7)]
# D flags Desarrollador (4)
c_dev_flag = [addcol(f"DEV: {DEV_LABEL[i]} (0/1)", "D") for i in range(4)]
# D flags Origen (2)
c_org_nac = addcol("ORG: Nacional (0/1)", "D")
c_org_int = addcol("ORG: Internacional (0/1)", "D")
# D derivadas finales
c_nivef  = addcol("Nivel efectivo", "D")
c_clave  = addcol("Clave combinación convocantes", "D")
c_comb1  = addcol("Combinación 1ª aparición (país)", "D")

NCOLS = len(COLS)
def L(i): return get_column_letter(i)

def build_entregable1(casos, catalog):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "1 · BBDD Casos incluidos"
    nrows = len(casos)
    R0, R1 = 2, 1 + nrows        # datos filas 2..R1  (R1=29 con 28 casos)

    GFILL = {"A": FILL_A, "B": FILL_B, "C": FILL_C, "D": FILL_D}
    # --- encabezados (fila 1) con bandas de color por grupo ---
    for i, (name, grp) in enumerate(COLS, start=1):
        cell = ws.cell(1, i, name)
        cell.font = F(bold=True, color=WHITE, size=9)
        cell.fill = GFILL[grp]
        cell.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
        cell.border = BORDER

    # --- filas de datos ---
    for k, c in enumerate(casos):
        r = R0 + k
        # A Identificación
        ws.cell(r, c_pais, c["pais"]).font = F()
        ws.cell(r, c_caso, c["caso"]).font = F()
        ws.cell(r, c_casoid, c["caso_id"]).font = F(size=8)
        ce = ws.cell(r, c_anio, c["anio"]); ce.font = F(); ce.number_format = "0"
        ws.cell(r, c_conf, c["confianza"]).font = F(size=8)
        # B Detalle narrativo
        ws.cell(r, c_desc, c["proceso"]).font = F(size=8)
        ws.cell(r, c_org, c["org"]).font = F(size=8)
        ws.cell(r, c_notas, c["accion"]).font = F(size=8)
        ws.cell(r, c_com, c["comentarios"]).font = F(size=8)
        ws.cell(r, c_urls, c["urls"]).font = F(size=7, color="1155CC")
        # C Coding validado (azul)
        coding = [(c_cuenta,c["cuenta"]),(c_tp,c["tipo_proceso"]),(c_et,c["etapas"]),
                  (c_niv,c["nivel"]),(c_cont,c["continuidad"]),(c_conv,c["convocante"]),
                  (c_torg,c["tipo_org"]),(c_rol,c["rol_ia"]),(c_dev,c["tipo_dev"]),
                  (c_orig,c["origen"]),(c_tia,c["tipos_ia"]),(c_llm,c["usa_llm"])]
        for col, val in coding:
            cc = ws.cell(r, col, val); cc.font = F(color=BLUE, size=9)
            if col == c_niv: cc.number_format = "0"
        # D Derivadas — normalización (fórmula)
        norm_pairs = [(c_nproc,c_tp),(c_netap,c_et),(c_nconv,c_conv),
                      (c_ndev,c_dev),(c_norig,c_orig),(c_nsis,c_tia)]
        for ncol, scol in norm_pairs:
            f = (f'=";"&LOWER(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE({L(scol)}{r},'
                 f'"; ",";"),", ",";"),",",";"))&";"')
            ws.cell(r, ncol, f).font = F(size=7)
        # flags Tipo de proceso (exact token sobre norm proceso)
        for i in range(5):
            f = f'=IF(ISNUMBER(SEARCH(";{TP_TOKENS[i]};",{L(c_nproc)}{r})),1,0)'
            ce = ws.cell(r, c_tp_flag[i], f); ce.font = F(size=8); ce.alignment = CENTER
        # flags Etapa: planificación/implementación/análisis exactos; traducción = subcadena
        et_search = [";planificación;",";implementación;",";análisis;","traducción"]
        for i in range(4):
            f = f'=IF(ISNUMBER(SEARCH("{et_search[i]}",{L(c_netap)}{r})),1,0)'
            ce = ws.cell(r, c_et_flag[i], f); ce.font = F(size=8); ce.alignment = CENTER
        # flags Convocante (7 tokens exactos)
        for i in range(7):
            f = f'=IF(ISNUMBER(SEARCH(";{CONV[i][0]};",{L(c_nconv)}{r})),1,0)'
            ce = ws.cell(r, c_cv_flag[i], f); ce.font = F(size=8); ce.alignment = CENTER
        # flags Desarrollador (4 tokens exactos)
        for i in range(4):
            f = f'=IF(ISNUMBER(SEARCH(";{DEV_TOKENS[i]};",{L(c_ndev)}{r})),1,0)'
            ce = ws.cell(r, c_dev_flag[i], f); ce.font = F(size=8); ce.alignment = CENTER
        # flags Origen (token exacto obligatorio: 'nacional' es subcadena de 'internacional')
        for col, tok in [(c_org_nac,";nacional;"),(c_org_int,";internacional;")]:
            f = f'=IF(ISNUMBER(SEARCH("{tok}",{L(c_norig)}{r})),1,0)'
            ce = ws.cell(r, col, f); ce.font = F(size=8); ce.alignment = CENTER
        # Nivel efectivo (anuncio caducado → 0)
        f = (f'=IF(AND({L(c_niv)}{r}=1,({SH2}!$B$25-{L(c_anio)}{r})>{SH2}!$B$26),'
             f'0,{L(c_niv)}{r})')
        ce = ws.cell(r, c_nivef, f); ce.font = F(size=9); ce.alignment = CENTER
        # Clave de combinación de convocantes (orden canónico GL,GN,OIP,EMP,UNI,SC,OI)
        flags = ",".join(f"{L(c_cv_flag[i])}{r}" for i in range(7))
        parts = "".join(
            f'IF({L(c_cv_flag[i])}{r}=1,"{CONV[i][1]}+","")&' for i in range(7))
        f = f'=IF(SUM({L(c_cv_flag[0])}{r}:{L(c_cv_flag[6])}{r})<2,"",{parts[:-1]})'
        ce = ws.cell(r, c_clave, f); ce.font = F(size=8); ce.alignment = CENTER
        # Combinación 1ª aparición (país) — rangos expansivos $A$1:A(r-1)
        f = (f'=IF({L(c_clave)}{r}="",0,IF(COUNTIFS('
             f'${L(c_pais)}$1:${L(c_pais)}{r-1},{L(c_pais)}{r},'
             f'${L(c_clave)}$1:${L(c_clave)}{r-1},{L(c_clave)}{r})=0,1,0))')
        ce = ws.cell(r, c_comb1, f); ce.font = F(size=8); ce.alignment = CENTER

    # --- freeze / autofilter / anchos ---
    ws.freeze_panes = "C2"
    ws.auto_filter.ref = f"A1:{L(NCOLS)}{R1}"
    widths = {c_pais:6,c_caso:34,c_casoid:24,c_anio:6,c_conf:16,c_desc:46,
              c_org:34,c_notas:34,c_com:30,c_urls:34,c_cuenta:10,c_tp:22,
              c_et:16,c_niv:7,c_cont:12,c_conv:20,c_torg:9,c_rol:9,c_dev:16,
              c_orig:14,c_tia:26,c_llm:8}
    for i in range(1, NCOLS+1):
        ws.column_dimensions[L(i)].width = widths.get(i, 12)
    for r in range(2, R1+1):
        ws.row_dimensions[r].height = 46

    # --- bloque NOTAS Y SUPUESTOS ---
    nr = R1 + 3
    ws.cell(nr, 1, "NOTAS Y SUPUESTOS").font = F(bold=True, size=11, color="1F4E79")
    notas = [
        "· Leyenda de colores: AZUL = dato validado (coding, pestaña 1). NEGRO = fórmula (columnas derivadas). "
        "Las columnas del grupo D se calculan; no se pegan valores.",
        "· PA · Mansa Idea: la celda «Tipos/familia IA» del insumo contiene «null» (sin sistema de IA técnicamente verificado). "
        "Decisión: se cuenta como 0 sistemas de IA para ese caso; «null» no forma parte del catálogo de tokens.",
        "· OPA Piauí (BR): «Tipos/familia IA» vacío → 0 sistemas para ese caso (BR conserva 11 sistemas por los otros casos).",
        f"· Caducidad de anuncios (config.yaml): un «anuncio» (Nivel=1) caduca a los {CADUCIDAD} años sin implementación "
        f"(año de referencia {ANIO_REF}). BR · Brasil Participativo (Nivel 1, Año 2023): nivel efectivo = 0 por caducidad; "
        "no afecta el índice de BR porque OPA Piauí tiene nivel 3. VE · Plan de la Patria 7T (Nivel 1, Año 2025): 2026−2025=1 ≤ 2 → nivel efectivo se mantiene en 1.",
        "· Tipos/familia IA se comparan como tokens textuales exactos separados por «;»: «LLM» ≠ «LLM generativa», "
        "«NLP» ≠ «NLP - Tópicos» (no se fusionan; idéntico al motor 2025). «Otros(no especificado)» de MX sí cuenta como token.",
        "· Códigos de combinación de convocantes: GL=gobierno local · GN=gobierno nacional · OIP=otra institución pública · "
        "EMP=empresa · UNI=universidad · SC=sociedad civil · OI=organización internacional. Una combinación = conjunto de ≥2 "
        "tipos que co-convocan una misma iniciativa; se deduplican conjuntos idénticos dentro del país (orden canónico por columna).",
        "· Origen del desarrollador: se compara con token exacto («;nacional;» / «;internacional;») porque «nacional» es subcadena de «internacional».",
    ]
    for j, t in enumerate(notas):
        cell = ws.cell(nr+1+j, 1, t); cell.font = F(size=8); cell.alignment = WRAP
        ws.merge_cells(start_row=nr+1+j, start_column=1, end_row=nr+1+j, end_column=11)
        ws.row_dimensions[nr+1+j].height = 30

    # ======================================================================
    # PESTAÑA 2 — Índice por país
    # ======================================================================
    ix = wb.create_sheet("2 · Índice por país")
    P1 = SH1
    # rangos de la pestaña 1 (columnas por letra)
    RA = f"{P1}!${L(c_pais)}${R0}:${L(c_pais)}${R1}"      # país
    Rcuenta = f"{P1}!${L(c_cuenta)}${R0}:${L(c_cuenta)}${R1}"
    Rnivef = f"{P1}!${L(c_nivef)}${R0}:${L(c_nivef)}${R1}"
    Rcomb1 = f"{P1}!${L(c_comb1)}${R0}:${L(c_comb1)}${R1}"
    Rnsis  = f"{P1}!${L(c_nsis)}${R0}:${L(c_nsis)}${R1}"

    # --- título ---
    ix.cell(1,1,"Índice ILIA 2026 — IA en Participación Ciudadana (por país · metodología CENIA v2)")
    ix.cell(1,1).font = F(bold=True, size=12, color="1F4E79")

    # --- cabecera tabla principal (fila 2) ---
    main_hdr = ["País","N iniciativas","nº tipos","V1 Tipos de proceso","nº etapas",
                "V2 Etapas de uso","nivel máx (efectivo)","V3 Continuidad","nº tipos gub",
                "nº tipos no-gub","nº combinaciones","V4 Convocante","V5 Cantidad",
                "Sub1 Uso","dev nac","dev int","V-Desarrollador","nº sistemas IA",
                "V-Tipos de IA","Sub2 Desarrollo","Sub1 red.","Sub2 red.",
                "Indicador final","Indicador sin redondear"]
    for i, h in enumerate(main_hdr, start=1):
        cell = ix.cell(2, i, h); cell.font = F(bold=True, color=WHITE, size=8)
        cell.fill = FILL_TITLE; cell.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
        cell.border = BORDER
    # columnas de la tabla principal (letras)
    M = dict(pais="A", n="B", ntp="C", v1="D", net="E", v2="F", nmax="G", v3="H",
             ngub="I", nnog="J", ncomb="K", v4="L", v5="M", sub1="N", devn="O",
             devi="P", vdev="Q", nsis="R", vtia="S", sub2="T", s1r="U", s2r="V",
             indf="W", indr="X")
    MR0 = 3                # primera fila de países
    MR1 = MR0 + len(PAISES) - 1   # 22

    # ---- posiciones de bloques auxiliares (parámetros y grillas) ----
    # PARÁMETROS
    PR = MR1 + 2                       # fila título parámetros
    # celdas fijas referenciadas por fórmulas:
    #   B25 = año ref ; B26 = caducidad ; C30..C33 = máx umbral ; D30..D34 = valor umbral
    #   B37 = máx combinaciones ; B38 = máx dev nac ; B39 = máx dev int ; B40 = máx sistemas
    # (se fuerzan esas filas explícitamente para que las referencias absolutas sean estables)
    AÑOREF_C = "B25"; CAD_C = "B26"
    UMBRAL_R0 = 30                     # filas 30..34 tabla de umbrales
    MAXCOMB_C="B37"; MAXNAC_C="B38"; MAXINT_C="B39"; MAXSIS_C="B40"

    # ---- GRILLAS (debajo de parámetros) ----
    GR = 43
    def grid_block(start, title, headers):
        ix.cell(start,1,title).font = F(bold=True, size=10, color="385723")
        for j,h in enumerate(headers):
            c = ix.cell(start+1, 1+j, h); c.font=F(bold=True,size=8); c.fill=FILL_GRIDHDR
            c.alignment=CENTER; c.border=BORDER
        return start+2   # fila de datos (país i → start+2+i)

    g_proc = GR
    g_proc_d = grid_block(g_proc, "GRILLA — Presencia de Tipos de Proceso (20 países × 5)",
                          ["País"]+TP_LABEL)
    g_etap = g_proc_d + len(PAISES) + 2
    g_etap_d = grid_block(g_etap, "GRILLA — Presencia de Etapas de uso (20 × 4)",
                          ["País"]+ET_LABEL)
    g_gub = g_etap_d + len(PAISES) + 2
    g_gub_d = grid_block(g_gub, "GRILLA — Convocante gubernamental (20 × 3)",
                         ["País","gobierno local","gobierno nacional","otra institución pública"])
    g_nog = g_gub_d + len(PAISES) + 2
    g_nog_d = grid_block(g_nog, "GRILLA — Convocante no gubernamental (20 × 4)",
                         ["País","empresa","universidad","sociedad civil","organización internacional"])
    g_devn = g_nog_d + len(PAISES) + 2
    g_devn_d = grid_block(g_devn, "GRILLA — Desarrollador NACIONAL (20 × 4)", ["País"]+DEV_LABEL)
    g_devi = g_devn_d + len(PAISES) + 2
    g_devi_d = grid_block(g_devi, "GRILLA — Desarrollador INTERNACIONAL (20 × 4)", ["País"]+DEV_LABEL)
    # grilla sistemas: tokens (filas) × países (columnas)
    g_sis = g_devi_d + len(PAISES) + 2
    ix.cell(g_sis,1,f"GRILLA — Sistemas de IA ({len(catalog)} tokens × 20 países) · TOTAL por país = nº sistemas").font=F(bold=True,size=10,color="385723")
    ix.cell(g_sis+1,1,"Token / sistema").font=F(bold=True,size=8); ix.cell(g_sis+1,1).fill=FILL_GRIDHDR
    for i,p in enumerate(PAISES):
        c = ix.cell(g_sis+1, 2+i, p); c.font=F(bold=True,size=8); c.fill=FILL_GRIDHDR; c.alignment=CENTER; c.border=BORDER
    g_sis_d = g_sis + 2               # fila token 0
    g_sis_tot = g_sis_d + len(catalog)   # fila TOTAL

    # ================== escribir GRILLAS ==================
    def flagcol(letter): return f"{P1}!${letter}${R0}:${letter}${R1}"
    # proceso / etapa / gub / nogub → presencia (COUNTIFS país + flag=1 > 0)
    def write_presence(dstart, flag_indices, flag_letters):
        for i,p in enumerate(PAISES):
            r = dstart + i
            ix.cell(r,1,f"={M['pais']}{MR0+i}").font=F(size=8)   # país ref a tabla principal
            for j,fl in enumerate(flag_letters):
                f = (f"=IF(COUNTIFS({RA},$A{r},{flagcol(fl)},1)>0,1,0)")
                c = ix.cell(r,2+j,f); c.font=F(size=8); c.alignment=CENTER; c.border=BORDER
    write_presence(g_proc_d, range(5), [L(c) for c in c_tp_flag])
    write_presence(g_etap_d, range(4), [L(c) for c in c_et_flag])
    write_presence(g_gub_d, range(3), [L(c_cv_flag[i]) for i in CONV_GUB])
    write_presence(g_nog_d, range(4), [L(c_cv_flag[i]) for i in CONV_NOGUB])
    # desarrollador nacional / internacional (COUNTIFS país + devflag=1 + origen=1)
    def write_dev(dstart, orig_letter):
        for i,p in enumerate(PAISES):
            r = dstart + i
            ix.cell(r,1,f"={M['pais']}{MR0+i}").font=F(size=8)
            for j in range(4):
                f = (f"=IF(COUNTIFS({RA},$A{r},{flagcol(L(c_dev_flag[j]))},1,"
                     f"{flagcol(orig_letter)},1)>0,1,0)")
                c = ix.cell(r,2+j,f); c.font=F(size=8); c.alignment=CENTER; c.border=BORDER
    write_dev(g_devn_d, L(c_org_nac))
    write_dev(g_devi_d, L(c_org_int))
    # sistemas: token × país
    for ti,tok in enumerate(catalog):
        r = g_sis_d + ti
        ix.cell(r,1,tok).font=F(size=8)
        for pi,p in enumerate(PAISES):
            col = 2+pi
            # COUNTIFS con comodín "*;token;*" sobre la norma de sistemas
            f = (f'=IF(COUNTIFS({RA},{L(col)}${g_sis+1},{Rnsis},'
                 f'"*;"&$A{r}&";*")>0,1,0)')
            c = ix.cell(r,col,f); c.font=F(size=7); c.alignment=CENTER; c.border=BORDER
    # TOTAL por país (columna)
    ix.cell(g_sis_tot,1,"TOTAL (nº sistemas)").font=F(bold=True,size=8)
    for pi,p in enumerate(PAISES):
        col=2+pi
        f=f"=SUM({L(col)}{g_sis_d}:{L(col)}{g_sis_tot-1})"
        c=ix.cell(g_sis_tot,col,f); c.font=F(bold=True,size=8); c.alignment=CENTER; c.border=BORDER

    # ================== PARÁMETROS ==================
    ix.cell(PR,1,"PARÁMETROS DEL CICLO (celdas de entrada en azul; máximos por fórmula)").font=F(bold=True,size=10,color="1F4E79")
    def paramcell(addr, label_col, label, value, is_formula=False, blue=False):
        # label a la izquierda, valor en addr
        col = openpyxl.utils.cell.coordinate_from_string(addr)[0]
        row = openpyxl.utils.cell.coordinate_from_string(addr)[1]
        lc = ix.cell(row, 1, label); lc.font=F(size=9)
        vc = ix.cell(row, openpyxl.utils.column_index_from_string(col), value)
        vc.font = F(color=(BLUE if blue else BLACK), size=9, bold=True)
        vc.fill = FILL_PARAM; vc.alignment=CENTER; vc.border=BORDER
        return vc
    paramcell(AÑOREF_C,1,"Año de referencia del ciclo", ANIO_REF, blue=True)
    paramcell(CAD_C,1,"Caducidad de anuncio (años)", CADUCIDAD, blue=True)
    # tabla de umbrales
    ix.cell(28,1,"Umbrales de Cantidad de iniciativas").font=F(bold=True,size=9,color="1F4E79")
    for j,h in enumerate(["tramo","mín (N)","máx (N)","valor"]):
        c=ix.cell(29,1+j,h); c.font=F(bold=True,size=8); c.fill=FILL_PARAM; c.alignment=CENTER; c.border=BORDER
    for i,(mn,mx,val) in enumerate(THRESHOLDS):
        r=UMBRAL_R0+i
        for j,v in enumerate([i, mn, (mx if mx is not None else "—"), val]):
            c=ix.cell(r,1+j,v); c.font=F(color=BLUE,size=9); c.fill=FILL_PARAM; c.alignment=CENTER; c.border=BORDER
    # máximos relativos del ciclo (FÓRMULAS MAX sobre la tabla principal / grilla)
    ix.cell(36,1,"Máximos relativos del ciclo (fórmulas MAX)").font=F(bold=True,size=9,color="1F4E79")
    paramcell(MAXCOMB_C,1,"Máx. combinaciones", f"=MAX({M['ncomb']}{MR0}:{M['ncomb']}{MR1})")
    paramcell(MAXNAC_C,1,"Máx. desarrolladores nacionales", f"=MAX({M['devn']}{MR0}:{M['devn']}{MR1})")
    paramcell(MAXINT_C,1,"Máx. desarrolladores internacionales", f"=MAX({M['devi']}{MR0}:{M['devi']}{MR1})")
    paramcell(MAXSIS_C,1,"Máx. sistemas de IA", f"=MAX({M['nsis']}{MR0}:{M['nsis']}{MR1})")

    # ================== TABLA PRINCIPAL (fórmulas) ==================
    for i,p in enumerate(PAISES):
        r = MR0 + i
        ix.cell(r, 1, p).font = F(bold=True, size=9)   # país (clave de fila)
        gp = g_proc_d + i; ge = g_etap_d + i; gg = g_gub_d + i
        gn = g_nog_d + i; gdn = g_devn_d + i; gdi = g_devi_d + i
        sis_col = L(2+i)   # columna del país en la grilla de sistemas
        def setf(key, formula, fmt="0.0", hl=False, bold=False):
            c = ix.cell(r, openpyxl.utils.column_index_from_string(M[key]), formula)
            c.font = F(size=9, bold=bold); c.number_format = fmt; c.alignment=CENTER; c.border=BORDER
            if hl: c.fill = FILL_HL
            return c
        # N iniciativas
        setf("n", f'=COUNTIFS({RA},$A{r},{Rcuenta},"sí")', "0")
        # nº tipos y V1
        setf("ntp", f"=SUM(B{gp}:F{gp})", "0")
        setf("v1", f"={M['ntp']}{r}/5*100")
        # nº etapas y V2
        setf("net", f"=SUM(B{ge}:E{ge})", "0")
        setf("v2", f"={M['net']}{r}/4*100")
        # nivel máx (efectivo) y V3
        setf("nmax", f"=_xlfn.MAXIFS({Rnivef},{RA},$A{r})", "0")
        setf("v3", f"={M['nmax']}{r}/3*100")
        # nº tipos gub / no-gub / combinaciones y V4
        setf("ngub", f"=SUM(B{gg}:D{gg})", "0")
        setf("nnog", f"=SUM(B{gn}:E{gn})", "0")
        setf("ncomb", f"=SUMIFS({Rcomb1},{RA},$A{r})", "0")
        setf("v4", (f"=({M['ngub']}{r}/3+{M['nnog']}{r}/4+"
                    f"IF(${MAXCOMB_C}=0,0,{M['ncomb']}{r}/${MAXCOMB_C}))/3*100"))
        # V5 Cantidad (IF anidado sobre la tabla de umbrales)
        setf("v5", (f"=IF({M['n']}{r}<=$C${UMBRAL_R0},$D${UMBRAL_R0},"
                    f"IF({M['n']}{r}<=$C${UMBRAL_R0+1},$D${UMBRAL_R0+1},"
                    f"IF({M['n']}{r}<=$C${UMBRAL_R0+2},$D${UMBRAL_R0+2},"
                    f"IF({M['n']}{r}<=$C${UMBRAL_R0+3},$D${UMBRAL_R0+3},$D${UMBRAL_R0+4}))))"))
        # Sub1 = promedio simple de V1..V5
        setf("sub1", f"=AVERAGE({M['v1']}{r},{M['v2']}{r},{M['v3']}{r},{M['v4']}{r},{M['v5']}{r})")
        # dev nac / int (suma de la fila de grilla) y V-Desarrollador
        setf("devn", f"=SUM(B{gdn}:E{gdn})", "0")
        setf("devi", f"=SUM(B{gdi}:E{gdi})", "0")
        setf("vdev", (f"=(IF(${MAXNAC_C}=0,0,{M['devn']}{r}/${MAXNAC_C})+"
                      f"IF(${MAXINT_C}=0,0,{M['devi']}{r}/${MAXINT_C}))/2*100"))
        # nº sistemas (TOTAL de la grilla de sistemas para el país) y V-Tipos IA
        setf("nsis", f"={sis_col}{g_sis_tot}", "0")
        setf("vtia", f"=IF(${MAXSIS_C}=0,0,{M['nsis']}{r}/${MAXSIS_C}*100)")
        # Sub2 = promedio(V-Desarrollador, V-Tipos IA)
        setf("sub2", f"=AVERAGE({M['vdev']}{r},{M['vtia']}{r})")
        # redondeos (modo legacy) e indicador final
        setf("s1r", f"=ROUND({M['sub1']}{r},0)", "0")
        setf("s2r", f"=ROUND({M['sub2']}{r},0)", "0")
        setf("indf", f"=ROUND(({M['s1r']}{r}+{M['s2r']}{r})/2,0)", "0", hl=True, bold=True)
        setf("indr", f"=({M['sub1']}{r}+{M['sub2']}{r})/2", "0.0")

    # --- freeze / anchos / leyenda ---
    ix.freeze_panes = "B3"
    ix.column_dimensions["A"].width = 22
    for i in range(2, 25):
        ix.column_dimensions[L(i)].width = 10
    # leyenda debajo de las grillas
    lg = g_sis_tot + 3
    ix.cell(lg,1,"LEYENDA Y NOTAS DE CÁLCULO").font=F(bold=True,size=11,color="1F4E79")
    leyenda = [
        "· Indicador país = (Sub1 Uso + Sub2 Desarrollo) / 2. Sub1 = promedio simple de V1..V5 (todas 0-100). Sub2 = promedio(V-Desarrollador, V-Tipos de IA).",
        "· V1 Tipos de proceso = nº tipos ÷ 5 × 100 · V2 Etapas = nº etapas ÷ 4 × 100 · V3 Continuidad = nivel máx (efectivo) ÷ 3 × 100.",
        "· V4 Convocante = (amplitud gub ÷3 + amplitud no-gub ÷4 + combinaciones ÷ máx. relativo) ÷ 3 × 100 (co-convocatoria=0 si el máximo del ciclo es 0).",
        "· V5 Cantidad = nº de iniciativas elegibles (Cuenta como iniciativa = «sí») aplicado a los umbrales fijos 0→0 / 1-3→25 / 4-6→50 / 7-9→75 / 10+→100.",
        "· V-Desarrollador = (dev nac ÷ máx nac + dev int ÷ máx int) ÷ 2 × 100 · V-Tipos de IA = nº sistemas ÷ máx sistemas × 100 (máximos relativos del ciclo).",
        "· Redondeo modo legacy (config.yaml): Sub1 red.=ROUND(Sub1;0), Sub2 red.=ROUND(Sub2;0), Indicador final=ROUND((Sub1 red.+Sub2 red.)/2;0). "
        "Nota: ROUND de Excel redondea .5 hacia arriba. La última columna muestra el indicador sin redondear (1 decimal).",
        "· Todas las celdas numéricas son fórmulas que referencian la pestaña 1 o las grillas/parámetros de esta pestaña; guardas anti división por cero en V4, V-Desarrollador y V-Tipos de IA.",
    ]
    for j,t in enumerate(leyenda):
        c=ix.cell(lg+1+j,1,t); c.font=F(size=8); c.alignment=WRAP
        ix.merge_cells(start_row=lg+1+j,start_column=1,end_row=lg+1+j,end_column=12)
        ix.row_dimensions[lg+1+j].height=28

    wb.save(OUT1)
    return dict(R0=R0, R1=R1, MR0=MR0, MR1=MR1)

# --------------------------------------------------------------------------
# 7. ENTREGABLE 2 — Casos excluidos
# --------------------------------------------------------------------------
def match_source(pais, caso, source_rows, name_key):
    """Devuelve la fila de source_rows (mismo país) con más solape de palabras."""
    target = set(norm_key(caso).split())
    best, bestscore = None, 0
    for s in source_rows:
        if s.get("pais","") != pais and s.get("_pais","") != pais: continue
        nm = s.get(name_key) or s.get("nombre_tentativo") or s.get("nombre") or s.get("caso") or ""
        words = set(norm_key(nm).split())
        if not words: continue
        score = len(target & words)
        if score > bestscore:
            best, bestscore = s, score
    return best if bestscore >= 2 else None

def build_entregable2(excluidos, bbdd_casos, bbdd_excl, evid, cand, hall, planilla):
    # clasificar
    for row in excluidos:
        row["grupo"] = classify_group(row)
    counts = {1:0,2:0,3:0}
    for row in excluidos: counts[row["grupo"]] += 1

    # índices de fuentes
    # BBDD casos por (pais, normcaso) — homónimos CL en lista
    bc_idx = {}
    for c in bbdd_casos:
        bc_idx.setdefault((c["pais"], norm_key(c["caso"])), []).append(c)
    be_idx = {}
    for e in bbdd_excl:
        be_idx.setdefault((e["pais"], norm_key(e["caso"])), []).append(e)
    # planilla dict (pais, normcaso)->evidencia ; construir lista para fuzzy
    pl_rows = [dict(pais=k[0], caso=k[1], evid=v) for k,v in planilla.items()]

    ENRICH6 = {("BR","colab"),("CL","estrategia de gobierno digital"),
               ("HN","redpublica"),("MX","presupuesto creces"),
               ("CO","gaitania"),("TT","engagett")}
    def is_enrich6(pais, caso):
        nk = norm_key(caso)
        for p,kw in ENRICH6:
            if pais==p and kw in nk: return True
        return False

    def find_evid(pais, caso):
        """Evidencia pestaña 3 por (pais, fuzzy caso)."""
        best,score=None,0
        for (p,nk),v in evid.items():
            if p!=pais: continue
            s=len(set(norm_key(caso).split()) & set(nk.split()))
            if s>score: best,score=v,s
        return best if score>=2 else None

    def match_bbdd_casos(pais, caso):
        cand_list = bc_idx.get((pais, norm_key(caso)), [])
        if cand_list:
            # homónimo CL: elegir 'audiencias' para el excluido baseline
            if pais=="CL" and "proceso constitucional" in norm_key(caso):
                for c in cand_list:
                    if "audiencia" in norm_key(c["desc"]): return c
            return cand_list[0]
        # fuzzy
        return match_source(pais, caso, bbdd_casos, "caso")

    def match_bbdd_excl(pais, caso):
        cand_list = be_idx.get((pais, norm_key(caso)), [])
        if cand_list: return cand_list[0]
        return match_source(pais, caso, bbdd_excl, "caso")

    def detalle_g1(row):
        c = match_bbdd_casos(row["pais"], row["caso"])
        parts=[]
        if c:
            if c["desc"]: parts.append(c["desc"].rstrip("."))
            meta=[]
            if c["org"]: meta.append(f"Organización a cargo: {c['org']}")
            if c["anio"]: meta.append(f"año {c['anio']}")
            if meta: parts.append(". ".join(meta))
        if is_enrich6(row["pais"], row["caso"]):
            ev = find_evid(row["pais"], row["caso"])
            if ev and ev.get("usa_ia"):
                parts.append(f"Evidencia de validación 2026: {ev['usa_ia'].rstrip('.')}")
        if not parts:
            parts.append(f"Caso incluido en la BBDD 2025. Ver motivo de exclusión.")
        return ". ".join(p for p in parts if p).strip() + "."

    def detalle_g2(row):
        e = match_bbdd_excl(row["pais"], row["caso"])
        if e and e["desc"]:
            txt = e["desc"].rstrip(".")
            if e.get("anio") not in (None, "", "None"):
                txt += f" (Año: {e['anio']})"
            return txt + "."
        # sin descripción en BBDD 2025
        base = "Sin descripción registrada en la BBDD 2025."
        if e and e.get("motivo"):
            base += f" Motivo 2025: {e['motivo'].rstrip('.')}."
        return base

    def detalle_g3(row):
        parts=[]
        ev_pl = None
        pr = match_source(row["pais"], row["caso"], pl_rows, "caso")
        if pr and pr.get("evid"): ev_pl = pr["evid"]
        cr = match_source(row["pais"], row["caso"], cand, "nombre_tentativo")
        hr = match_source(row["pais"], row["caso"], hall, "nombre")
        if ev_pl:
            parts.append(ev_pl.rstrip("."))
        elif cr and cr.get("senal"):
            parts.append(cr["senal"].rstrip("."))
        elif hr and hr.get("senal"):
            parts.append(hr["senal"].rstrip("."))
        if is_enrich6(row["pais"], row["caso"]):
            ev = find_evid(row["pais"], row["caso"])
            if ev:
                extra = ev.get("usa_ia") or ev.get("rol_ia") or ""
                if extra and norm_key(extra) not in norm_key(" ".join(parts)):
                    parts.append(f"Evidencia (validación): {extra.rstrip('.')}")
        if not parts:
            parts.append(f"«{row['caso']}». Caso identificado en el descubrimiento 2026 y no incluido; "
                         f"la descripción técnica y la razón de no inclusión se detallan en la columna «Motivo y detalles de la exclusión»")
        return ". ".join(p for p in parts if p).strip() + "."

    def motivo_final(row):
        base = row["motivo"]
        if row["grupo"] == 1:
            return "Estaba incluido en la BBDD 2025. " + base
        if row["grupo"] == 2:
            e = match_bbdd_excl(row["pais"], row["caso"])
            m2025 = e["motivo"] if e else ""
            if m2025 and norm_key(m2025) != norm_key(base):
                return f"Motivo 2025: «{m2025.rstrip('.')}» · Reconfirmación 2026: {base}"
            return base
        return base

    # construir filas finales, ordenadas: G1 (por país), luego G3, luego G2
    def sort_key(row): return (row["pais"], row["_row"])
    ordered = ( sorted([r for r in excluidos if r["grupo"]==1], key=sort_key)
              + sorted([r for r in excluidos if r["grupo"]==3], key=sort_key)
              + sorted([r for r in excluidos if r["grupo"]==2], key=sort_key) )

    out_rows = []
    for row in ordered:
        g = row["grupo"]
        det = detalle_g1(row) if g==1 else (detalle_g2(row) if g==2 else detalle_g3(row))
        out_rows.append(dict(pais=row["pais"], caso=row["caso"], origen=ORIGEN[g],
                             grupo=g, detalle=det, urls=row["url"],
                             motivo=motivo_final(row)))

    # ---- escribir workbook ----
    wb = openpyxl.Workbook(); ws = wb.active; ws.title = "Casos excluidos"
    ws.cell(1,1,"Casos excluidos — ILIA 2026 (IA en Participación Ciudadana)").font=F(bold=True,size=13,color="1F4E79")
    ws.cell(2,1,(f"Total: {len(out_rows)} casos  ·  "
                 f"Base 2025 incluidos→excluidos: {counts[1]}  ·  "
                 f"Base 2025 exclusión reconfirmada: {counts[2]}  ·  "
                 f"Nuevos 2026 no incluidos: {counts[3]}")).font=F(bold=True,size=10)
    # leyenda de colores de origen
    ORIG_FILL = {1: fill("FCE4D6"), 3: fill("E2EFDA"), 2: fill("DDEBF7")}
    leg = [(1,"Base 2025 → excluido 2026"),(3,"Nuevo 2026 (no incluido)"),(2,"Exclusión 2025 reconfirmada")]
    ws.cell(3,1,"Origen:").font=F(bold=True,size=9)
    for j,(g,lab) in enumerate(leg):
        c=ws.cell(3,2+j,lab); c.font=F(size=8); c.fill=ORIG_FILL[g]; c.border=BORDER; c.alignment=CENTER
    HDR_ROW = 5
    headers = ["País","Caso","Origen del caso","Detalles del caso (narrado)","URLs","Motivo y detalles de la exclusión"]
    for i,h in enumerate(headers, start=1):
        c=ws.cell(HDR_ROW,i,h); c.font=F(bold=True,color=WHITE,size=10); c.fill=FILL_TITLE
        c.alignment=CENTER; c.border=BORDER
    for k,row in enumerate(out_rows):
        r = HDR_ROW+1+k
        vals=[row["pais"],row["caso"],row["origen"],row["detalle"],row["urls"],row["motivo"]]
        for i,v in enumerate(vals, start=1):
            c=ws.cell(r,i,v); c.font=F(size=9); c.alignment=WRAP; c.border=BORDER
        ws.cell(r,3).fill = ORIG_FILL[row["grupo"]]
        ws.cell(r,1).alignment = CTOP
    ws.freeze_panes = f"A{HDR_ROW+1}"
    ws.auto_filter.ref = f"A{HDR_ROW}:F{HDR_ROW+len(out_rows)}"
    W={1:6,2:40,3:30,4:92,5:46,6:92}
    for i,w in W.items(): ws.column_dimensions[L(i)].width=w
    wb.save(OUT2)
    return counts, out_rows

# --------------------------------------------------------------------------
# 8. main
# --------------------------------------------------------------------------
def main():
    os.makedirs(FINAL_DIR, exist_ok=True)
    shutil.copyfile(INSUMO_SRC, INSUMO_REPO)   # trazabilidad
    casos = read_incluidos()
    assert len(casos)==28, f"Se esperaban 28 casos incluidos, hay {len(casos)}"
    catalog = build_sistemas_catalog(casos)
    print(f"[incluidos] {len(casos)} casos · catálogo de sistemas IA: {len(catalog)} tokens")
    print("  tokens:", catalog)
    meta = build_entregable1(casos, catalog)
    print(f"[entregable 1] escrito → {OUT1}  (datos filas {meta['R0']}..{meta['R1']})")

    excluidos = read_excluidos()
    assert len(excluidos)==79, f"Se esperaban 79 excluidos, hay {len(excluidos)}"
    bbdd_casos = read_bbdd_casos()
    bbdd_excl = read_bbdd_excluidos()
    evid = read_evidencia()
    cand = read_csv_simple(CANDIDATOS)
    hall = read_csv_simple(HALLAZGOS)
    planilla = read_planilla_val()
    counts, out_rows = build_entregable2(excluidos, bbdd_casos, bbdd_excl, evid, cand, hall, planilla)
    print(f"[entregable 2] escrito → {OUT2}")
    print(f"  conteos por origen: G1={counts[1]}  G2={counts[2]}  G3={counts[3]}  total={sum(counts.values())}")
    assert counts=={1:12,2:49,3:18}, f"Conteos inesperados: {counts}"
    print(f"[insumo] copiado → {INSUMO_REPO}")

if __name__ == "__main__":
    main()
