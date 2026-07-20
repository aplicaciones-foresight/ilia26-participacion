# HANDOFF — QA final de los entregables ILIA 2026 · IA en Participación Ciudadana

**Para:** una sesión de Claude en otra cuenta (escritorio), sin acceso al repositorio.
**Fecha de corte:** 2026-07-19 · **Origen:** repo `aplicaciones-foresight/ilia26-participacion`, rama `claude/validated-excluded-cases-sheets-lohg7e` (commits `ff773f3` y `55701fc`).
**Adjuntos esperados (4):** `BBDD_casos_incluidos_ILIA2026.xlsx` · `Casos_excluidos_ILIA2026.xlsx` · `Comparacion_2025_2026_ILIA.xlsx` · `qa_entregables.py`.

---

## 1 · Contexto en breve

El indicador ILIA de **IA en Participación Ciudadana** cubre 20 países (AR, BO, BR, CL, CO, CR, CU, DO, EC, GT, HN, JM, MX, PA, PE, PY, SV, TT, UY, VE). Para el ciclo 2026 el equipo hizo una búsqueda exhaustiva de casos, doble extracción con verificación verbatim y una **validación manual final** (planilla «Validación_Casos_1»), que dejó **28 casos incluidos** (12 países con casos) y **80 excluidos**. Con esa base validada se generaron los 3 archivos que aquí se auditan. La metodología del cálculo es la **CENIA v2 (jun-2026)**; el ciclo 2025 se publicó con una fórmula anterior («legacy»).

**Tu tarea:** QA final independiente de los 3 archivos. No corrijas nada por tu cuenta: verifica, y reporta cualquier discrepancia con celda exacta y valor esperado vs observado.

## 2 · Los 3 archivos

### A) `BBDD_casos_incluidos_ILIA2026.xlsx` — la base y el índice 2026 (v3: 4 pestañas)
- **Pestaña «1 · BBDD Casos incluidos»** (28 filas): identificación, narrativa, URLs, coding validado (texto azul = dato) y **columnas derivadas por fórmula** (texto negro): normalizaciones, flags 0/1 por taxonomía, «Nivel efectivo» (caducidad de anuncios), clave de combinación de convocantes y su 1ª aparición por país. Bajo la tabla, un puntero a la pestaña 3.
- **Pestaña «2 · Índice por país»** (20 países): TODO por fórmula. Estructura: N iniciativas → V1…V5 → Sub1 · desarrolladores/sistemas → Sub2 · redondeos → **Indicador final**. Debajo: parámetros (año de referencia 2026, caducidad 2 años, umbrales de Cantidad), máximos relativos (fórmulas MAX) y las grillas auxiliares que alimentan cada celda.
- **Pestaña «3 · Metodología y supuestos»** (pedida por el operador el 2026-07-20): sección A = metodología CENIA v2 completa (las 7 variables, subcomponentes, máximos relativos, redondeo, flujo del cálculo); sección B = los supuestos y decisiones que antes estaban como bloque de notas en la pestaña 1 (PA «null», caducidad BR-BP, tokens, fusión e-Cidadania, homónimo CL, escenarios, fuente). Verificar que coincida con §3 y §6 de este handoff.
- **Pestaña «4 · Gráficos»** (pedida por el operador el 2026-07-20): 4 barras agrupadas que leen la pestaña 2 — Indicador final (1 serie, sin leyenda) · Sub1 vs Sub2 (2 series) · V1–V5 de Uso (5 series) · las 2 variables de Desarrollo (2 series). Paleta categórica en orden fijo validada para daltonismo (#2A78D6 · #008300 · #E87BA4 · #EDA100 · #1BAF7A).

### B) `Casos_excluidos_ILIA2026.xlsx` — los 79 excluidos con su origen
Una sola pestaña (80 filas: 79 del insumo de validación + GeTAU AR, agregado el 2026-07-20) : País · Caso · **Origen del caso** (3 valores) · Detalles del caso (narrado, 1 celda) · URLs · Motivo y detalles de la exclusión (1 celda, texto íntegro). Los 3 orígenes:
1. «Base 2025 — estaba INCLUIDO, excluido en 2026» → **12 casos**
2. «Base 2025 — ya estaba EXCLUIDO, exclusión reconfirmada» → **49 casos**
3. «Nuevo 2026 — identificado en descubrimiento, no incluido» → **19 casos** (incluye GeTAU AR, agregado post-validación)

### C) `Comparacion_2025_2026_ILIA.xlsx` — efecto del cambio de fórmula
- «1 · BBDD 2025 (insumo)»: los 28 casos del baseline 2025 + recodificación 2026 (convocante 7-cat y nivel 0-3, **BORRADOR pre-Gate**) + flags por fórmula.
- «2 · Cálculo 2025 · f. antigua»: fórmula legacy (4 variables) con columna de control vs el **oficial publicado 2025** (pegado como dato desde la BBDD oficial).
- «3 · Cálculo 2025 · f. nueva»: CENIA v2 sobre la misma base 2025.
- «4 · Comparación»: indicadores y variables lado a lado + Δ efecto fórmula / Δ real / Δ total. La columna 2026 es **dato pegado** (sus fórmulas auditables viven en el archivo A).
- «5 · Gráficos»: 8 barras agrupadas (Indicador, Sub1, Sub2, V1–V5). Azul = 2025 f. antigua · Verde = 2025 f. nueva · Magenta = 2026.

## 3 · Metodología (lo que las fórmulas deben implementar)

**Indicador = (Sub1 + Sub2) / 2**, redondeo «legacy»: `Indicador = ROUND((ROUND(Sub1,0)+ROUND(Sub2,0))/2,0)`.

**Sub1 Uso — CENIA v2 (2026), promedio simple de 5 variables (0-100):**
1. **Tipos de proceso** = nº de tipos distintos del país ÷ 5 × 100. Taxonomía: Participación Digital, Gobernanza Colaborativa, Mini públicos, Referendos e Iniciativas Populares, Presupuestos Participativos.
2. **Etapas de uso** = nº distintas ÷ 4 × 100 (Planificación, Implementación, Análisis, Traducción Política; «Traducción» a secas cuenta como Traducción Política).
3. **Continuidad** = nivel MÁXIMO del país ÷ 3 × 100, con **nivel efectivo**: un Anuncio (nivel 1) caduca si (2026 − Año) > 2 → 0.
4. **Organización Convocante** = promedio de 3 subcomponentes: (nº tipos gubernamentales ÷ 3) + (nº tipos no gubernamentales ÷ 4) + (nº de **combinaciones** distintas ÷ máximo relativo entre países), todo ÷ 3 × 100. Una combinación = el conjunto de ≥2 tipos (de 7 categorías) que co-convocan una misma iniciativa; conjuntos idénticos se deduplican dentro del país.
5. **Cantidad** = nº de iniciativas elegibles: 0→0 · 1-3→25 · 4-6→50 · 7-9→75 · 10+→100.

**Sub2 Desarrollo (idéntico a 2025):** promedio de: **Desarrollador** = (tipos con origen Nacional ÷ máx. entre países + tipos con origen Internacional ÷ máx.) ÷ 2 × 100 — 4 tipos de actor; si un caso tiene varios tipos y varios orígenes se cruzan todos; y **Tipos de IA** = nº de sistemas distintos ÷ máx. × 100 — tokens textuales exactos separados por «;» («LLM» ≠ «LLM generativa» ≠ «NLP»).

**Fórmula antigua 2025 (solo archivo C, pestaña 2):** Sub1 = promedio de 4 variables: tipos÷5, etapas÷4, **modalidades de continuidad** presentes ({Uso único, Plataforma}) ÷ 2, y **tipos de organización** ({Público, Privado, Mixto}) ÷ 3, × 100. Sub2 igual al de arriba.

## 4 · QA automático (recomendado)

En la carpeta con los 3 .xlsx: `pip install openpyxl` y `python qa_entregables.py` (adjunto; también está embebido en el Apéndice). El script **recomputa todo en Python desde el coding crudo** (ignora las fórmulas), compara contra los valores calculados de los archivos y contra las tablas de referencia de la sección 5, y verifica la estructura del archivo B. Salida esperada: **«✓ QA COMPLETO EN VERDE»** y exit 0. No modifica los archivos.

## 5 · Tablas de referencia (deben reproducirse EXACTAMENTE)

### Índice 2026 (archivo A, pestaña 2)
| País | N | Sub1 red. | Sub2 red. | **Indicador** |   | País | N | Sub1 | Sub2 | **Ind.** |
|---|---|---|---|---|---|---|---|---|---|---|
| BR | 7 | 81 | 100 | **91** | | GT | 1 | 39 | 17 | **28** |
| CL | 9 | 69 | 77 | **73** | | BO | 1 | 40 | 13 | **27** |
| CO | 3 | 56 | 50 | **53** | | PE | 1 | 30 | 17 | **24** |
| CU | 1 | 34 | 31 | **33** | | EC | 1 | 35 | 11 | **23** |
| MX | 1 | 30 | 15 | **23** | | UY | 1 | 29 | 17 | **23** |
| PA | 1 | 35 | 6 | **21** | | VE | 1 | 23 | 11 | **17** |

AR, CR, DO, HN, JM, PY, SV, TT = 0 en todo (sin casos). **Máximos relativos 2026:** combinaciones 2 (CL y CO) · desarrolladores nacionales 4 (BR) · internacionales 3 (BR) · sistemas de IA 11 (BR y CL).

### 2025: fórmula antigua vs oficial publicado vs fórmula nueva (archivo C)
| País | Ind. f. antigua | Oficial 2025 | Ind. f. nueva |   | País | antigua | Oficial | nueva |
|---|---|---|---|---|---|---|---|---|
| CO | 85 | 85 | 82 | | GT | 33 | 32 | 34 |
| BR | 77 | 76 | 75 | | BO | 31 | 30 | 32 |
| CL | 57 | 57 | 57 | | DO | 30 | 30 | 32 |
| PE | 54 | 53 | 46 | | EC | 25 | 25 | 27 |
| MX | 48 | 47 | 36 | | TT | 0 | s/d | 0 |
| CR | 46 | 46 | 45 | | resto | 0 | 0 | 0 |
| HN | 42 | 42 | 43 | | | | | |

La columna de control del archivo C debe mostrar «✓» en los 19 países con baseline (la tolerancia ±1 es real: el motor 2025 redondeaba con *banker's rounding* de Python y el Excel usa ROUND *half-up*). **Máximos relativos 2025:** combinaciones 2 · dev. nacionales 3 · dev. internacionales 2 · sistemas 5.

### Excluidos (archivo B): 80 = 12 + 49 + 19
Los **12 del grupo 1** (estaban incluidos en la BBDD 2025): BR ParticipACT Brasil · BR Colab · CL Participación Ciudadana Proceso Constitucional (homónimo: el de audiencias sale, el de diálogos autoconvocados sigue incluido) · CL Estrategia de Gobierno Digital · CO Descongestión Ingreso Solidario · CR U-Report · CR dIAra · DO CiudadanIA · HN RedPública + iVerify · MX Sufragio seguro · MX Presupuesto CRECES · PE Sistema de cómputo Elecciones 2026.
Conciliación de la base anterior: 28 casos 2025 = 16 siguen incluidos (el caso e-Cidadania 2025 quedó **fusionado** dentro de la fila 2026 «Portal e-Cidadania… marcado automático + matching semántico», que cuenta como 1 iniciativa) + 12 pasan al grupo 1. Las 49 exclusiones 2025 están íntegras en el grupo 2.

## 6 · Decisiones intencionales — NO reportarlas como errores

1. **PA Mansa Idea**: «Tipos/familia IA» = «null» en la validación → cuenta **0 sistemas** (sin dato verificado; anotado en las NOTAS del archivo A). Por eso Sub2 de PA = 6.
2. **BR Brasil Participativo**: Anuncio (nivel 1) con Año 2023 → **nivel efectivo 0** por caducidad. Sin impacto: BR toma continuidad de OPA Piauí (nivel 3).
3. **BR OPA Piauí**: «Tipos/familia IA» vacío → 0 sistemas de ese caso (BR conserva 11 por los demás).
4. Diferencias de **±1 vs el oficial 2025** por el modo de redondeo (ver arriba).
5. En el archivo C, «Governanza Colaborativa» (grafía de la BBDD 2025) cuenta como Gobernanza Colaborativa.
6. El archivo B tiene 5 filas con país **«LATAM»** (exclusiones regionales de la base 2025) — correcto.
7. La columna 2026 del archivo C y el oficial 2025 son **datos pegados a propósito** (sus fuentes están citadas en el propio archivo); todo lo demás es fórmula.
8. El archivo B no tiene fórmulas (es una tabla documental) — correcto.
9. TT aparece como «s/d» en el control oficial 2025 (no estaba en el universo 2025).
10. En el archivo C, V1/V2 de la pestaña 3 **referencian las grillas de la pestaña 2**: la definición de esas dos variables no cambió entre fórmulas.
11. La recodificación 2026 del baseline (convocante/nivel del archivo C, pestaña 1) es **BORRADOR pre-Gate**: validado su cálculo, no su contenido.

## 7 · QA manual complementario (lo que el script NO cubre)

- **Muestreo de fórmulas en Excel** (auditabilidad real): en el archivo A, pestaña 2, elegir 2-3 países y rastrear precedentes (Ctrl+[): Indicador ← Sub1/Sub2 ← V1…V5 ← grillas ← flags de pestaña 1 ← celdas azules de coding. No debe aparecer ningún número «suelto» sin fórmula fuera de los datos azules y los parámetros amarillos.
- **Prueba de recálculo vivo**: cambiar temporalmente un dato azul (p. ej. borrar «Presupuestos Participativos» del caso OPA Piauí) y verificar que V1 de BR baja de 100 a 80 y el indicador de BR de 91 a 89; deshacer (Ctrl+Z).
- **Lectura humana del archivo B** (muestra ≥10 filas): que «Detalles del caso» describa el caso sin inventos, que «Motivo» sea autocontenido y que las URLs correspondan al caso. Revisar especialmente los 12 del grupo 1 y los motivos largos (CO GaitanIA ~1.800 caracteres, debe estar íntegro).
- **Gráficos del archivo C**: 8 gráficos, leyendas visibles, colores consistentes por serie (azul/verde/magenta), ejes 0-100, categorías = 20 países, y que los valores de barras coincidan a ojo con la pestaña 4 (BR 77/75/91, CO 85/82/53, MX 48/36/23).
- **Coherencia narrativa**: BR y CL dominan 2026 por amplitud (BR: 5/5 tipos de proceso; CL: 9 iniciativas); CO cae de 85 a 53 (pasó de 4 a 3 iniciativas y quedó lejos de los nuevos máximos relativos); CR/DO/HN caen a 0 (sus casos 2025 quedaron excluidos); CU/PA/UY/VE debutan con casos nuevos.

## 8 · Criterio de aprobación

**APROBADO** si: el script imprime «✓ QA COMPLETO EN VERDE» **y** el muestreo manual de fórmulas no encuentra valores pegados donde debía haber fórmula **y** la lectura del archivo B no encuentra contenido inventado o troncado. Cualquier otra cosa: **reportar sin corregir** — archivo, pestaña, celda, valor observado, valor esperado y por qué (contrastando con las secciones 5 y 6 antes de reportar, para no marcar decisiones intencionales como defectos).


## 9 · Reparaciones post-QA (2026-07-20) — qué cambió en el archivo B (v2)

El primer QA externo (2026-07-20) devolvió NO APROBADO por 14 motivos truncados en
el archivo B (los archivos A y C quedaron aprobados y NO fueron modificados: sus
SHA-256 se conservan). Reparaciones aplicadas en la v2 de `Casos_excluidos_ILIA2026.xlsx`:

1. **14 motivos truncados repuestos.** La causa raíz estaba en el insumo: la planilla
   de validación traía esas celdas capadas a 300 caracteres por un defecto del export
   de la sesión que la generó, y el texto completo no sobrevivía en ningún artefacto.
   Cada celda conserva VERBATIM el texto truncado y reconstruye el cierre solo con
   hechos documentados (reingreso de excluidos, candidatos, gates, URLs del caso);
   todas terminan con la etiqueta «[Cierre reconstruido: …; fuentes: …]».
2. **Observaciones menores corregidas:** «}» espurio de CO GaitanIA eliminado (texto
   íntegro); MX Sufragio seguro sin prefijo duplicado y con motivo autocontenido;
   BR Colab explicita el duplicado (mismo despliegue que OPA Piauí sobre Colab Gov);
   CL Proceso Constitucional explica el homónimo (audiencias sale, autoconvocados
   sigue) y su razón; detalles de CO Atlántico y UY Consulta NNA reescritos (traían
   un texto-plantilla erróneo por matching difuso); años sin decimal; caracteres de
   ancho cero y saltos de línea saneados.
3. **`qa_entregables.py` reforzado** (y su copia del Apéndice): ahora detecta la firma
   de truncamiento (~300 chars sin puntuación final), URLs rotas al final del motivo,
   caracteres de ancho cero, el texto-plantilla 2025 en casos del grupo 3, y exige
   exactamente 14 etiquetas de reconstrucción.

Para re-auditar la v2: correr el script actualizado y releer las 14+6 celdas listadas
en el informe previo. Los cierres reconstruidos NO son texto del validador original:
son recomposición documentada — si alguna reconstrucción se considera inexacta,
reportarla indicando la fuente que la contradiga.


## 10 · Alta post-validación (2026-07-20): GeTAU (AR) — grupo 3

El equipo aportó el caso **GeTAU** (Córdoba, AR: WebApp de IA + geolocalización +
participación vecinal para monitoreo del arbolado urbano; ONG Acción Ambiental + UNC).
Revisión (2ª opinión, coincide con el juicio del aportante): la participación es aporte
de datos/observaciones (censo/mapeo colaborativo) y la IA opera sobre los datos de los
árboles, no sobre aportes de un proceso participativo → **civic tech de monitoreo → NO
ENTRA** (análogo a ParticipACT, dIAra, Pa' que veás, Satellites On Fire). Se añadió al
archivo B como «Nuevo 2026», por lo que el total pasa de 79 a **80 = 12 + 49 + 19** (el
script del Apéndice ya espera estos conteos). La celda registra que el fetch directo de
las fuentes fue bloqueado por el proxy del entorno de generación.


## 11 · Ampliación del archivo A (2026-07-20, pedida por el operador) — v3

Se agregaron al archivo A las pestañas «3 · Metodología y supuestos» (metodología completa
+ supuestos movidos desde el bloque de notas de la pestaña 1) y «4 · Gráficos» (4 gráficos
de variables y subindicadores). Las pestañas 1 y 2 NO cambiaron en contenido ni fórmulas
(2.452 fórmulas, recalc 0 errores, valores idénticos verificados contra la recomputación);
el SHA-256 del archivo cambia por las pestañas nuevas. El QA automático no requiere cambios
(lee las pestañas 1 y 2 por nombre). Revisar: que la pestaña 3 coincida con §3/§6 y que los
4 gráficos coincidan con la tabla de la pestaña 2.

---

## Apéndice — `qa_entregables.py`

(El mismo script adjunto, por si solo recibes este documento.)

```python
# -*- coding: utf-8 -*-
# QA INDEPENDIENTE de los 3 entregables ILIA 2026 · Participación Ciudadana.
# Ejecutar en la carpeta que contiene los 3 .xlsx:  python qa_entregables.py
# Requiere: pip install openpyxl
# Recomputa TODO en Python desde el coding crudo (ignora las fórmulas) y
# compara contra los valores calculados de los archivos y contra las tablas
# de referencia del handoff. No modifica ningún archivo.
import sys
import unicodedata
import zipfile
from decimal import Decimal, ROUND_HALF_UP

from openpyxl import load_workbook

F1 = "BBDD_casos_incluidos_ILIA2026.xlsx"
F2 = "Casos_excluidos_ILIA2026.xlsx"
F3 = "Comparacion_2025_2026_ILIA.xlsx"
PAISES = ["AR","BO","BR","CL","CO","CR","CU","DO","EC","GT","HN","JM","MX","PA","PE","PY","SV","TT","UY","VE"]

# ---- Tablas de referencia (deben coincidir con los archivos) -------------
ESPERADO_2026 = {  # país: (N, Sub1 red., Sub2 red., Indicador final)
    "AR": (0,0,0,0), "BO": (1,40,13,27), "BR": (7,81,100,91), "CL": (9,69,77,73),
    "CO": (3,56,50,53), "CR": (0,0,0,0), "CU": (1,34,31,33), "DO": (0,0,0,0),
    "EC": (1,35,11,23), "GT": (1,39,17,28), "HN": (0,0,0,0), "JM": (0,0,0,0),
    "MX": (1,30,15,23), "PA": (1,35,6,21), "PE": (1,30,17,24), "PY": (0,0,0,0),
    "SV": (0,0,0,0), "TT": (0,0,0,0), "UY": (1,29,17,23), "VE": (1,23,11,17)}
ESPERADO_2025 = {  # país: (Ind fórmula antigua, Oficial publicado ('s/d' TT), Ind fórmula nueva)
    "AR": (0,0,0), "BO": (31,30,32), "BR": (77,76,75), "CL": (57,57,57),
    "CO": (85,85,82), "CR": (46,46,45), "CU": (0,0,0), "DO": (30,30,32),
    "EC": (25,25,27), "GT": (33,32,34), "HN": (42,42,43), "JM": (0,0,0),
    "MX": (48,47,36), "PA": (0,0,0), "PE": (54,53,46), "PY": (0,0,0),
    "SV": (0,0,0), "TT": (0,"s/d",0), "UY": (0,0,0), "VE": (0,0,0)}
MAX_2026 = dict(combos=2, dev_nac=4, dev_int=3, sistemas=11)
MAX_2025 = dict(combos=2, dev_nac=3, dev_int=2, sistemas=5)
GRUPO1 = {  # los 12 que estaban INCLUIDOS en la BBDD 2025 y salen en 2026
    ("BR","ParticipACT Brasil"), ("BR","Colab"),
    ("CL","Participación Ciudadana Proceso Constitucional"),
    ("CL","Estrategia de Gobierno Digital. Informe proceso participativo segunda consulta ciudadana"),
    ("CO","Descongestión de solicitudes diarias del programa Ingreso Solidario"),
    ("CR","U-Report Costa Rica – chatbot juvenil"), ("CR","dIAra"), ("DO","CiudadanIA"),
    ("HN","RedPública + iVerify"), ("MX","Sufragio seguro"), ("MX","Presupuesto CRECES"),
    ("PE","Sistema de cómputo con IA para las Elecciones Generales 2026")}

fallas = []
def check(ok, msg):
    if not ok:
        fallas.append(msg)
    return ok

def rhu(x):  # ROUND de Excel (half-up)
    return int(Decimal(str(x)).quantize(Decimal("1"), rounding=ROUND_HALF_UP))

def na(s):  # minúsculas sin acentos
    return "".join(c for c in unicodedata.normalize("NFD", str(s or "").lower())
                   if not unicodedata.combining(c)).strip()

def toks(s):
    return [t.strip() for t in str(s or "").replace(";", ",").split(",") if t.strip()]

def cerca(a, b, tol=0.05):
    try:
        return abs(float(0 if a is None else a) - float(b)) <= tol
    except (TypeError, ValueError):
        return str(a) == str(b)

def v_cant(n):
    return 0 if n == 0 else 25 if n <= 3 else 50 if n <= 6 else 75 if n <= 9 else 100

TIPOS5 = {"participacion digital":"PD","gobernanza colaborativa":"GC","governanza colaborativa":"GC",
          "mini publicos":"MP","referendos e iniciativas populares":"RIP","presupuestos participativos":"PP"}
GUB = {"gobierno local","gobierno nacional","otra institucion publica"}
NOGUB = {"empresa","universidad","sociedad civil","organizacion internacional"}

def etapa_id(t):
    t = na(t)
    for sub, k in (("planif","P"),("implement","I"),("analisis","A"),("traduccion","T")):
        if sub in t:
            return k
    return None

def motor(casos, anio_ref=2026, caducidad=2, con_null_pa=True):
    """Recomputa Sub1 CENIA v2 + Sub2 por país desde el coding crudo."""
    raw = {}
    for p in PAISES:
        cp = [c for c in casos if c["pais"] == p]
        tipos=set(); etapas=set(); gub=set(); nogub=set(); combos=set()
        dnac=set(); dint=set(); sis=set(); niveles=[]
        for c in cp:
            for x in c["proceso"]:
                m = TIPOS5.get(na(x)); check(m, f"tipo de proceso no reconocido: {x!r}")
                if m: tipos.add(m)
            for x in c["etapas"]:
                m = etapa_id(x); check(m, f"etapa no reconocida: {x!r}")
                if m: etapas.add(m)
            tt=set()
            for cv in c["conv"]:
                cvn = na(cv)
                if cvn in GUB: gub.add(cvn); tt.add(cvn)
                elif cvn in NOGUB: nogub.add(cvn); tt.add(cvn)
                else: check(False, f"convocante no reconocido: {cv!r}")
            if len(tt) >= 2: combos.add(frozenset(tt))
            niv = c["nivel"]
            if niv is not None and str(niv).strip() != "":
                niv = int(float(niv)); ano = c["ano"]
                if niv == 1 and ano not in (None,"") and (anio_ref - int(float(ano))) > caducidad:
                    niv = 0
                niveles.append(niv)
            has_nac = any(na(x) == "nacional" for x in c["origen"])
            has_int = any(na(x) == "internacional" for x in c["origen"])
            for d in c["dev"]:
                dn = na(d)
                if has_nac: dnac.add(dn)
                if has_int: dint.add(dn)
            sis.update(na(x) for x in c["sistemas"] if na(x) != "null")  # «null» = sin dato
        raw[p] = dict(n=len(cp), tipos=len(tipos), etapas=len(etapas), gub=len(gub),
                      nogub=len(nogub), combos=len(combos), dnac=len(dnac), dint=len(dint),
                      sis=len(sis), nivmax=max(niveles) if niveles else 0)
    mx = dict(combos=max(r["combos"] for r in raw.values()),
              dev_nac=max(r["dnac"] for r in raw.values()),
              dev_int=max(r["dint"] for r in raw.values()),
              sistemas=max(r["sis"] for r in raw.values()))
    res = {}
    for p in PAISES:
        d = raw[p]
        if d["n"] == 0:
            res[p] = dict(s1=0.0, s2=0.0, s1r=0, s2r=0, ind=0); continue
        v1=d["tipos"]/5*100; v2=d["etapas"]/4*100; v3=d["nivmax"]/3*100
        v4=(d["gub"]/3 + d["nogub"]/4 + (d["combos"]/mx["combos"] if mx["combos"] else 0))/3*100
        s1=(v1+v2+v3+v4+v_cant(d["n"]))/5
        dev=((d["dnac"]/mx["dev_nac"] if mx["dev_nac"] else 0)
             + (d["dint"]/mx["dev_int"] if mx["dev_int"] else 0))/2*100
        s2=(dev + (d["sis"]/mx["sistemas"] if mx["sistemas"] else 0)*100)/2
        res[p] = dict(s1=s1, s2=s2, s1r=rhu(s1), s2r=rhu(s2), ind=rhu((rhu(s1)+rhu(s2))/2))
    return res, raw, mx

# ==========================================================================
# 1) BBDD_casos_incluidos: recomputar el índice 2026 desde el coding crudo
# ==========================================================================
wb1 = load_workbook(F1, data_only=True)
w1 = wb1["1 · BBDD Casos incluidos"]
h1 = {w1.cell(1,c).value: c for c in range(1, w1.max_column+1)}
def celda(ws, h, r, name): return ws.cell(r, h[name]).value
casos26 = []
for r in range(2, 30):
    if not celda(w1, h1, r, "País (ISO-2)"): continue
    casos26.append(dict(
        pais=str(celda(w1,h1,r,"País (ISO-2)")).strip(),
        caso=str(celda(w1,h1,r,"Caso")).strip(),
        cuenta=na(celda(w1,h1,r,"Cuenta como iniciativa")),
        proceso=toks(celda(w1,h1,r,"Tipo de proceso")),
        etapas=toks(celda(w1,h1,r,"Etapas uso IA")),
        nivel=celda(w1,h1,r,"Nivel (0-3)"), ano=celda(w1,h1,r,"Año"),
        conv=toks(celda(w1,h1,r,"Convocante (7-cat)")),
        dev=toks(celda(w1,h1,r,"Tipo desarrollador IA")),
        origen=toks(celda(w1,h1,r,"Origen desarrollador")),
        sistemas=toks(celda(w1,h1,r,"Tipos/familia IA"))))
check(len(casos26) == 28, f"E1: se esperaban 28 casos, hay {len(casos26)}")
check(all(c["cuenta"] == "si" for c in casos26), "E1: hay casos con «Cuenta como iniciativa» ≠ sí")
res26, raw26, mx26 = motor(casos26)
for k, v in MAX_2026.items():
    check(mx26[k] == v, f"E1: máximo relativo {k}={mx26[k]}, esperado {v}")

w2i = wb1["2 · Índice por país"]
h2i = {w2i.cell(2,c).value: c for c in range(1, w2i.max_column+1)}
for i, p in enumerate(PAISES):
    r = 3 + i
    check(w2i.cell(r,1).value == p, f"E1 pestaña2: fila {r} no es {p}")
    e = res26[p]; ref = ESPERADO_2026[p]
    check(cerca(w2i.cell(r,h2i["N iniciativas"]).value, raw26[p]["n"]), f"E1 {p}: N")
    check(cerca(w2i.cell(r,h2i["Sub1 red."]).value, e["s1r"]), f"E1 {p}: Sub1 red. Excel≠py")
    check(cerca(w2i.cell(r,h2i["Sub2 red."]).value, e["s2r"]), f"E1 {p}: Sub2 red. Excel≠py")
    check(cerca(w2i.cell(r,h2i["Indicador final"]).value, e["ind"]), f"E1 {p}: Indicador Excel≠py")
    check((raw26[p]["n"], e["s1r"], e["s2r"], e["ind"]) == ref,
          f"E1 {p}: recomputado {(raw26[p]['n'], e['s1r'], e['s2r'], e['ind'])} ≠ tabla handoff {ref}")

# ==========================================================================
# 2) Casos_excluidos: conteos, grupos y consistencia
# ==========================================================================
wb2 = load_workbook(F2, data_only=True)
we = wb2.active
hr = next(r for r in range(1, 12) if we.cell(r,1).value == "País")
excl = []
for r in range(hr+1, we.max_row+1):
    if not we.cell(r,1).value: continue
    excl.append(dict(pais=str(we.cell(r,1).value).strip(), caso=str(we.cell(r,2).value).strip(),
                     origen=str(we.cell(r,3).value), det=str(we.cell(r,4).value or ""),
                     urls=str(we.cell(r,5).value or ""), motivo=str(we.cell(r,6).value or "")))
check(len(excl) == 80, f"E2: se esperaban 80 filas (79 del insumo + GeTAU AR), hay {len(excl)}")
g1 = [e for e in excl if "estaba INCLUIDO" in e["origen"]]
g2 = [e for e in excl if "ya estaba EXCLUIDO" in e["origen"]]
g3 = [e for e in excl if "Nuevo 2026" in e["origen"]]
check((len(g1), len(g2), len(g3)) == (12, 49, 19), f"E2: grupos {(len(g1),len(g2),len(g3))} ≠ (12,49,19)")
check({(e["pais"], e["caso"]) for e in g1} == GRUPO1, "E2: los 12 del grupo 1 no son los esperados")
check(all(len(e["det"]) >= 40 for e in excl), "E2: hay detalles narrados sospechosamente cortos (<40 chars)")
check(all(len(e["motivo"]) >= 10 for e in excl), "E2: hay motivos vacíos o casi vacíos")
# Guardas anti-truncamiento (hallazgo del QA externo 2026-07-20): el insumo de
# validación traía 14 motivos capados a 300 caracteres; fueron reconstruidos
# con etiqueta de procedencia. Ningún motivo puede terminar a mitad de palabra
# con la firma del capado (~300 chars sin puntuación final) ni en URL rota,
# ni contener caracteres de ancho cero; los detalles del grupo 3 no pueden
# traer el texto-plantilla de re-verificación 2025 (bug de matching difuso).
import re as _re
_FIN_OK = ".»\")!?]"
for e in excl:
    m, d = e["motivo"], e["det"]
    check(not (295 <= len(m) <= 305 and m[-1] not in _FIN_OK),
          f"E2 truncado?: {e['pais']} {e['caso'][:40]} (len={len(m)}, fin={m[-25:]!r})")
    check(not _re.search(r"https?://\S{0,14}$", m),
          f"E2 URL rota al final del motivo: {e['pais']} {e['caso'][:40]}")
    check(not any(ch in m + d for ch in "​‌‍﻿"),
          f"E2 caracteres de ancho cero: {e['pais']} {e['caso'][:40]}")
n_reconstruidos = sum(1 for e in excl if "[Cierre reconstruido" in e["motivo"])
check(n_reconstruidos == 14,
      f"E2: se esperaban 14 motivos con etiqueta de reconstrucción, hay {n_reconstruidos}")
check(not any("Excluido en 2025 por" in e["det"] for e in excl if "Nuevo 2026" in e["origen"]),
      "E2: detalle-plantilla 2025 en un caso del grupo 3 (Nuevo 2026)")
check(all("http" in e["urls"] for e in excl), "E2: hay filas sin URL")
nombres_incl = {(c["pais"], c["caso"]) for c in casos26}
solapes = nombres_incl & {(e["pais"], e["caso"]) for e in excl}
HOMONIMO = {("CL", "Participación Ciudadana Proceso Constitucional")}
# En la BBDD 2025 había DOS casos homónimos CL: el de diálogos autoconvocados
# sigue incluido y el de audiencias está excluido — es el ÚNICO solape legítimo.
check(solapes == HOMONIMO,
      f"E2: solapes incluidos∩excluidos inesperados: {solapes ^ HOMONIMO}")

# ==========================================================================
# 3) Comparación: recomputar 2025 con ambas fórmulas desde su pestaña 1
# ==========================================================================
wb3 = load_workbook(F3, data_only=True)
w31 = wb3["1 · BBDD 2025 (insumo)"]
casos25 = []
for r in range(2, 30):
    if not w31.cell(r,1).value: continue
    casos25.append(dict(
        pais=str(w31.cell(r,1).value).strip(), ano=w31.cell(r,3).value,
        tipo_org=str(w31.cell(r,6).value or ""), proceso=toks(w31.cell(r,7).value),
        etapas=toks(w31.cell(r,8).value), cont=str(w31.cell(r,9).value or ""),
        dev=toks(w31.cell(r,10).value), origen=toks(w31.cell(r,11).value),
        sistemas=toks(w31.cell(r,12).value), conv=toks(w31.cell(r,13).value),
        nivel=w31.cell(r,14).value))
check(len(casos25) == 28, f"E3: se esperaban 28 casos 2025, hay {len(casos25)}")

# fórmula nueva sobre 2025 (mismo motor)
res25n, raw25, mx25 = motor(casos25)
for k, v in MAX_2025.items():
    check(mx25[k] == v, f"E3: máximo 2025 {k}={mx25[k]}, esperado {v}")
# fórmula antigua (legacy 4 variables) sobre 2025
res25L = {}
for p in PAISES:
    cp = [c for c in casos25 if c["pais"] == p]
    if not cp:
        res25L[p] = 0; continue
    d = raw25[p]
    cont = set(); orgs = set()
    for c in cp:
        cc = na(c["cont"])
        if "unico" in cc: cont.add("UU")
        if "plataforma" in cc: cont.add("PL")
        o = na(c["tipo_org"])
        for sub in ("mixto","publico","privado"):
            if sub in o: orgs.add(sub); break
    s1 = (d["tipos"]/5*100 + d["etapas"]/4*100 + len(cont)/2*100 + len(orgs)/3*100)/4
    res25L[p] = rhu((rhu(s1) + res25n[p]["s2r"])/2)

w32 = wb3["2 · Cálculo 2025 · f. antigua"]
w33 = wb3["3 · Cálculo 2025 · f. nueva"]
w34 = wb3["4 · Comparación"]
for i, p in enumerate(PAISES):
    r = 3 + i
    refL, ref_of, refN = ESPERADO_2025[p]
    indN = res25n[p]["ind"] if raw25[p]["n"] else 0
    check(res25L[p] == refL, f"E3 {p}: legacy recomputado {res25L[p]} ≠ tabla {refL}")
    check(indN == refN, f"E3 {p}: nueva recomputada {indN} ≠ tabla {refN}")
    check(cerca(w32.cell(r,20).value, refL), f"E3 {p}: Ind legacy Excel={w32.cell(r,20).value} ≠ {refL}")
    check(cerca(w33.cell(r,20).value, refN), f"E3 {p}: Ind nueva Excel={w33.cell(r,20).value} ≠ {refN}")
    of = w32.cell(r,23).value
    if ref_of == "s/d":
        check(str(of) == "s/d", f"E3 {p}: oficial debería ser s/d")
    else:
        check(cerca(of, ref_of, 0.01) and abs(refL - float(of)) <= 1,
              f"E3 {p}: oficial {of} / legacy {refL} fuera de ±1")
    rc = hr = 6 + i  # pestaña 4: datos desde fila 6
    check(cerca(w34.cell(rc,2).value, refL), f"E3 {p}: comparación col B ≠ legacy")
    check(cerca(w34.cell(rc,3).value, refN), f"E3 {p}: comparación col C ≠ nueva")
    check(cerca(w34.cell(rc,4).value, ESPERADO_2026[p][3]), f"E3 {p}: comparación col D ≠ 2026")

with zipfile.ZipFile(F3) as z:
    n_charts = sum(1 for n in z.namelist() if n.startswith("xl/charts/chart") and n.endswith(".xml"))
check(n_charts == 8, f"E3: {n_charts}/8 gráficos")

# ==========================================================================
print("=" * 66)
if fallas:
    print(f"✗ QA FALLÓ — {len(fallas)} problema(s):")
    for f in fallas:
        print("   -", f)
    sys.exit(1)
print("✓ QA COMPLETO EN VERDE")
print("  E1: 28 casos · índice 2026 recomputado = Excel = tabla de referencia (20 países)")
print("  E2: 80 excluidos = 12 + 49 + 19 (incl. GeTAU AR) · grupo 1 exacto · sin solapes · celdas completas")
print("  E3: legacy 2025 = oficial ±1 (19/19) · fórmula nueva verificada · 2026 consistente · 8 gráficos")
print(f"  Máximos 2026 {mx26} · Máximos 2025 {mx25}")
```
