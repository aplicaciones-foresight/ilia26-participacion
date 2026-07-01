# Planilla de datos brutos por caso — ILIA 2026 (Fase 2/3)

**Fecha:** 2026-06-30 · Pipeline ILIA 2026 — IA en Participación Ciudadana

Una **fila por caso** con **todos los datos brutos** necesarios para calcular el
indicador y clasificar. **No se calcula el indicador aquí** (esta etapa solo
consolida y valida los datos). Lo que no se pudo conseguir está **marcado como
gap con su URL** para búsqueda manual.

## Entregables

| Archivo | Contenido |
|---|---|
| `data/gates/planilla_detalle_casos_ILIA2026.xlsx` | **Planilla principal (6 hojas)**: Detalle casos · Evidencia (verbatim) · GAPS (buscar manual) · Fuentes · Alertas · Leyenda |
| `data/candidatos/detalle_casos_ILIA2026.csv` | Hoja principal en CSV (para el pipeline) |
| `data/fichas/<caso_id>_detalle.json` | Ficha por caso (datos + evidencia verbatim + fuentes + gaps) |
| `src/export_detalle_casos.py` | Script que compila las fichas → planilla |

## Universo: 55 casos en juego

| Bloque | SI | DUDA | NO | Total |
|---|:--:|:--:|:--:|:--:|
| 1. Nuevos | 6 | 1 | 3 | 10 |
| 1. Dudosos | 1 | 1 | 6 | 8 |
| 4. Descubrimiento amplio | 1 | 3 | 0 | 4 |
| 2. Baseline 2025 | 25 | 0 | 3 | 28 |
| 3. Excluidos (revisar reingreso) | 0 | 0 | 5 | 5 |
| **Total** | **33** | **5** | **17** | **55** |

> Actualizado tras la **2ª pasada** de los 8 DUDA (6→NO, 2→DUDA lean NO) y la
> **búsqueda amplia** (+4 casos nuevos: UY Pol.is = SI; CO Gaitana IA y CL Viña
> Decide = DUDA lean SI; CL Pudahuel = DUDA lean NO). Detalle en
> `descubrimiento_amplio_2026.md`. De los 5 DUDA actuales, 2 se inclinan a SI.

### Inventario COMPLETO (99 casos) — para validación de CENIA

Además de los 55 casos "en juego", la planilla incluye ahora los **44 casos
excluidos en 2025 que se mantienen fuera** (bloque **«5. Excluido 2025 (fuera del
índice)»**), con su **Motivo exclusión 2025** en columna dedicada. Así, los **49
casos que ya no entraban** están todos representados: **5** en «Excluido (revisar
reingreso)» (revisados → se mantienen NO) + **44** en el bloque 5.

| Bloque | Casos |
|---|:--:|
| 1. Nuevos + Dudosos | 18 |
| 4. Descubrimiento amplio | 4 |
| 2. Baseline 2025 | 28 |
| 3. Excluido (revisar reingreso) | 5 |
| 5. Excluido 2025 (fuera) | 44 |
| **Total inventario** | **99** |

> Los excluidos 2025 (bloque 5) **no se re-extrajeron** (están fuera del índice);
> se listan con País, Caso, Motivo de exclusión, descripción, año y URLs para que
> CENIA valide cada decisión de exclusión. Dos de ellos (BR «De ciudadano a
> senador» y BR «Participa+ Brasil») reingresaron conceptualmente como casos
> **nuevos** (e-Cidadania y Brasil Participativo), anotado en sus alertas.

### Reconciliación con la validación manual del equipo

Se integró la **validación manual** (Natalia/Nicole/Jose, todos «DE ACUERDO», 49
casos de `Casos_a_Profundizar.xlsx`). La planilla ahora tiene:
- **«¿ENTRA? (EQUIPO)»** = veredicto manual → **oficial** (impulsa las pestañas
  «Entran + Dudosos» y «Excluidos»).
- **«¿ENTRA? (evidencia)»** = mi veredicto por investigación (2ª opinión).
- **«Divergencia»** + hoja **«Divergencias»** (12 casos) con ambos veredictos, el
  comentario del equipo, mi evidencia y URLs para verificar.

**Resultado oficial (equipo): 43 entran/dudosos · 56 se excluyen.**

**12 divergencias:**
- *Equipo SI / yo NO-DUDA (9):* Cátedra Brasil, OPA Piauí, São Paulo, LXS 400,
  Citibeats+PNUD, DNP Diálogos, EngageTT + baseline **CO Descongestión** y **PE
  Sistema de cómputo ONPE** (que mi config traía como exclusión firme).
- *Yo SI-DUDA / equipo NO (3):* CU Código de las Familias, ISIDataInsights, y el
  **duplicado** CL Participación Constitucional (el equipo dedupe uno → NO).

Para discutir con evidencia a la vista: **LXS 400** (OCDE 2025: la IA gestiona
turnos, no contenido), **São Paulo** (ejercicio Escola do Parlamento, no oficial),
**Citibeats** (social listening), **Cátedra Brasil** (investigación), **OPA
Piauí** (processing). A favor del equipo (tienen fuente que yo no hallé): **DNP**
(Nicole: «modelo híbrido»), **EngageTT** (verificado). Conflicto factual: **CU**
(yo hallé la ficha técnica de GEMA/Datys = NLP; Jose no halló IA).

> La lista del equipo **no revisó CR dIAra ni DO CiudadanIA** (2 del baseline) ni
> los 4 del descubrimiento amplio → aparecen como **«(sin revisar)»** en la
> columna EQUIPO; su veredicto oficial usa mi evidencia hasta que el equipo decida.

> `SI`/`NO`/`DUDA` es **tentativo** (criterio: IA sobre el **CONTENIDO** de los
> aportes dentro de un proceso participativo). La decisión final es del equipo.
> `SI*` = entra en escenario A; revisar en escenario B (DO CiudadanIA, CL «Tenemos
> que hablar de Chile»). Exclusiones **firmes** del baseline (config): CO
> Descongestión Ingreso Solidario, MX Sufragio Seguro, PE Sistema de cómputo 2026.

## Hallazgos clave (candidatos nuevos)

**Nuevos que ENTRAN (7):**
- 🟢 ALTA — BR e-Cidadania (matching semántico de 145.993 ideas legislativas con PLs; distinto del baseline de audiencias)
- 🟢 ALTA — BR 5ª CNCTI (TDS Company usó IA para sistematizar ~4.000 h y aportes de 200+ etapas / 100.000+ personas)
- 🟢 ALTA — CL El Chile que Queremos / MinCiencia (RNN, Random Forest, LDA sobre texto libre; código público; distinto del baseline «dIAlogos»)
- 🟢 ALTA — CU Consulta Código de las Familias (ficha técnica de GEMA/Datys = NLP/minería de texto sobre el contenido, no conteo)
- 🟢 ALTA — PA Mansa Idea (sociedad civil; IA agrega 175.000+ propuestas del Pacto del Bicentenario)
- 🟡 MEDIA — BR Brasil Participativo (BERTopic+LLM sobre 10.000+ propuestas; producción oficial no 100% confirmada → nivel 2)
- 🟡 MEDIA — MX Guanajuato InteliGENTE (IA procesó 26.000+ aportes; **software concreto sin identificar** = gap)

**2ª pasada sobre los 8 DUDA — resueltos (ninguno pasó a SI):**
- 🔴 **NO** — BR São Paulo Participe Mais: la clasificación con Gemini **sí** procesa contenido, pero fue un **ejercicio formativo** (Escola do Parlamento / Agentes de Governo Aberto), no un despliegue oficial de la Prefeitura (la sistematización oficial fue manual/técnica).
- 🔴 **NO** — BR OPA Piauí: la IA (Colab+AWS) se documenta solo como **aceleración del «processamento»/infraestructura**, no análisis temático del contenido.
- 🔴 **NO** — CL Senador Virtual: el componente NLP (GobLab UAI + Harvard, CrowdLaw) es **investigación académica** (produce recomendaciones), no producción sobre los aportes.
- 🔴 **NO** — CO DNP Diálogos Regionales: la sistematización de las 89.788 propuestas usó **lectura + frecuencia/codificación**, sin evidencia de NLP/ML.
- 🔴 **NO** — CO POT Bogotá: es **únicamente un artículo académico** de factibilidad (Areandina/Auditoría), sin despliegue institucional sobre aportes reales.
- 🔴 **NO** — VE Plan de la Patria 7T: **sin corroboración técnica independiente** de la afirmación de prensa estatal; el contenido lo sistematizaron relatores humanos (34.491 propuestas).
- 🟠 **DUDA (lean NO)** — CO ISIDataInsights: diseñada para operar sobre contenido cualitativo, pero **sin evidencia de aplicación** a un proceso participativo concreto (sigue «en integración»). *Falta:* informe de uso 2025-2026 de la SDP Bogotá.
- 🟠 **DUDA (lean NO)** — TT EngageTT (Go Vocal): hallazgo nuevo — el módulo de IA/NLP «Sensemaking» de Go Vocal **no viene activo por defecto** y no se confirma que la instancia TT lo active. *Falta:* reporte de la consulta del NDTS que evidencie análisis automático.

**Excluidos revisados (5): todos mantienen la exclusión (NO).** No se halló IA
sobre el contenido de los aportes en UCampus, Asamblea Itinerante de Bogotá,
iLabs, Mini-Public de la Procuraduría ni «Pa' que veás». También **NO**: CO
Citibeats+PNUD (social listening de redes, no proceso participativo), CL LXS 400
(la IA gestiona turnos de habla, no el contenido — OCDE 2025), BR Cátedra/Co:Lab
USP (investigación en curso, sin despliegue).

## Validación anti-alucinación

- **Disciplina cita-o-gap:** cada campo crítico con valor está respaldado por una
  **cita textual** (hoja *Evidencia (verbatim)*) o marcado como **gap**.
  Verificación automática: **0 valores críticos sin respaldo** (ni cita ni gap).
- **Taxonomías:** todos los valores conformes al esquema (0 fuera de catálogo).
- **Fuentes:** 202 fuentes registradas con su estado de fetch. Muchas páginas de
  gobierno (`.gob`/`.gov`/`.leg`) devolvieron **HTTP 403** al fetch directo; su
  contenido se recuperó vía búsqueda web y la URL quedó anotada para verificación
  manual del cuerpo exacto.
- **Confianza:** ALTA 20 · MEDIA 30 · BAJA 1.

## Gaps (lo que falta — buscar manual)

**97 gaps, todos con URL** (hoja *GAPS (buscar manual)*). Campos más frecuentes:
`usa_IA_en_proceso` (14), `nivel_consolidacion` (11), `evidencia_actividad_2026`
(9), `tipos_IA_familia` (8), `estado_actividad` (8), `sistema_IA` (7). El gap
recurrente más importante es **identificar el software/técnica de IA concreto** y
**confirmar recurrencia** (para subir de nivel 2 a 3) en varios casos.

## Procedencia de los datos

- **Baseline (28):** datos brutos de la BBDD ILIA 2025 (validada por el equipo) +
  recodificación 2026 (convocante 7-cat, nivel 0-3 desde `recodificacion_2025.csv`)
  + reverificación de actividad 2026 (señal web donde existe; gap donde no).
- **Nuevos/dudosos/excluidos (23):** investigación web en vivo (junio 2026), con
  extracción de campos + cita verbatim por fuente.

## Próximos pasos sugeridos

1. Revisar los **8 DUDA** y fijar entra/no-entra (la duda central está por caso).
2. Resolver los **gaps con URL** (sobre todo software de IA y recurrencia/nivel).
3. Confirmar la recodificación 2026 (convocante/nivel) de los casos que entran.
4. Recién entonces, correr el cálculo del indicador (Fase 4).
