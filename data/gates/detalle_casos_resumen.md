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

## Universo: 51 casos en juego

| Bloque | SI | DUDA | NO | Total |
|---|:--:|:--:|:--:|:--:|
| 1. Nuevos | 6 | 2 | 2 | 10 |
| 1. Dudosos | 1 | 6 | 1 | 8 |
| 2. Baseline 2025 | 25 | 0 | 3 | 28 |
| 3. Excluidos (revisar reingreso) | 0 | 0 | 5 | 5 |
| **Total** | **32** | **8** | **11** | **51** |

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

**8 DUDA — requieren decisión del equipo (la duda central está en la planilla):**
- BR São Paulo Participe Mais (Gemini) — uso oficial vs taller del programa Agentes de Gobierno Abierto
- BR OPA Piauí — IA acelera «processamento»/seguridad, sin evidencia de análisis temático del contenido
- CL Senador Virtual / GobLab — IA es investigación académica, no producción sobre los aportes
- CO DNP Diálogos Regionales — sistematización por frecuencia/codificación, sin evidencia de NLP/ML
- CO POT Bogotá (Auditoría) — artículo académico que propone/evalúa una herramienta, sin despliegue real
- CO ISIDataInsights — herramienta ganadora de concurso «en implementación», sin aplicación a un proceso concreto
- TT EngageTT (Go Vocal) — la plataforma trae NLP, pero no se confirma que la instancia TT lo active
- VE Plan de la Patria 7T — afirmación de prensa estatal sin corroboración técnica (contradice la cifra oficial de 34.491 propuestas sistematizadas por relatores humanos)

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
