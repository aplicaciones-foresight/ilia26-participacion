# SESSION_LOG — Pipeline ILIA 2026 (Participación Ciudadana)

## Sesión 2026-07-18/19 — Entregables post-validación (rama `claude/validated-excluded-cases-sheets-lohg7e`)

El operador entregó la planilla validada (`data/final/insumo_Validacion_Casos_1.xlsx`,
28 casos incluidos en 12 países · 79 excluidos). Con ella se generaron
(`src/build_entregables.py`, verificación en `src/verify_entregables.py`):

1. **`data/final/BBDD_casos_incluidos_ILIA2026.xlsx`** — pestaña 1: BBDD de los 28
   casos (narrativa + coding validado + columnas derivadas por FÓRMULA); pestaña 2:
   índice por país (metodología CENIA v2) 100 % por fórmulas auditables, con
   parámetros y grillas auxiliares visibles. Recalculado (2.452 fórmulas, 0 errores)
   y contrastado contra recomputación Python independiente (20 países × 13 métricas, 0 diferencias).
   Resultados (Indicador final): BR 91 · CL 73 · CO 53 · CU 33 · GT 28 · BO 27 ·
   PE 24 · EC/MX/UY 23 · PA 21 · VE 17 · resto 0.
2. **`data/final/Casos_excluidos_ILIA2026.xlsx`** — 79 casos con origen:
   12 estaban INCLUIDOS en la BBDD 2025 y salen en 2026 · 49 ya excluidos en 2025
   (reconfirmados) · 18 candidatos nuevos 2026 no incluidos. Conciliación completa
   con la BBDD 2025 (28 = 16 siguen + 12 salen; e-Cidadania 2025 quedó fusionado
   en la fila 2026; homónimo CL Proceso Constitucional: 1 sigue + 1 sale).

Notas: la caducidad de anuncios (config) deja BR-brasil-participativo con nivel
efectivo 0 (Año 2023) — sin impacto en el índice de BR; el «null» de PA Mansa Idea
cuenta 0 sistemas de IA (decisión documentada en la pestaña 1).

---

**Fecha:** 2026-06-04 · **Idioma:** español · **Rama:** `claude/funny-dirac-pq4TG`

Bitácora de la primera sesión: construcción de la infraestructura del pipeline y
arranque de la Fase 1. Sigue el plan de trabajo del handoff (§10).

---

## 1. Estado de prerrequisitos (§3)

| Insumo | Estado | Nota |
|---|---|---|
| `BBDD_IA_para_Participación_-_Entrega.xlsx` | ✅ **disponible** | copiada a `data/baseline/BBDD_IA_Participacion_2025.xlsx` (28 casos, 49 excluidos). Desbloquea Fases 4-5 y calibración. |
| `calc_engine.py` (2025) | ✅ disponible | base del motor; copia de referencia en `docs/`. |
| `prompt_extraccion_v1.txt` | ✅ disponible | conservado intacto en `prompts/`. |
| `Cambios_Variables…2026.docx` | ⚠️ no provisto | contenido normativo tomado del §4 del handoff. |
| `Propuesta…2026.docx` (v1.2) + **Anexo B** | ❌ **no provisto** | **bloquea canales A.10/A.11** (directorio de medios e instituciones por país). Pedir al operador. |

---

## 2. Entregables de la sesión (orden de prioridad del handoff §1)

1. ✅ **Repositorio estructurado** con scripts, esquemas y prompts versionados (ver `README.md`).
2. ✅ **Prompt de extracción v1.1** en doble pasada independiente
   (`prompts/prompt_extraccion_v1.1_A.txt` y `_B.txt`) + `schema_ficha_v1.1.json`.
3. ✅ **Motor v2026** (`src/calc_engine.py`): legacy intacto + `compute_2026`,
   con suite de tests y no-regresión en verde.
4. ✅ **Corrida de Fase 1**: `candidatos.csv` (20/20 países) + `search_frame.csv`
   + `gate1_report.md`.

## 3. Tests (todos en verde) — `pytest -q tests/` → **35 passed**

- `test_noregresion_legacy.py`: motor legacy reproduce el oficial 2025 en **19/19
  países** (Sub1+Sub2+Indicador, ±1). **Corrido ANTES de cualquier cálculo con datos.**
- `test_compute_2026.py`: **20** casos sintéticos (una variable a la vez):
  tipos, etapas, continuidad por nivel máximo, caducidad de anuncio, convocante a
  dos niveles, cantidad por tramos + `count_min_level`, escenarios A/B, frontera
  apoyo, Sub2 idéntico al legacy.
- `test_verify_verbatim.py` (**7**) y `test_extract_validacion.py` (**7**).

## 4. Cambios del prompt v1 → v1.1 (§5) — todos aplicados

1. `tipo_proceso`: Gobernanza Colaborativa para texto libre a planes de desarrollo.
2. `etapas_uso_IA`: “Análisis” solo con procesamiento posterior (con ejemplo negativo).
3. Refuerzo organización a cargo **vs** desarrollador.
4. **NUEVO** `rol_IA` (contenido/apoyo/no-claro) con verbatim; “apoyo” → excluidos.
5. **NUEVO** `tipo_convocante` (7 categorías) + se conserva `tipo_organizacion` 2025.
6. **NUEVO** `nivel_consolidacion` (0–3) con reglas de recurrencia/oficialidad +
   se conserva `estado_implementacion` 2025.
7. Campos críticos con verbatim obligatoria (`config.campos_criticos`).
8. Añadidos `model_version` y `fecha_extraccion`.

Las pasadas A (checklist/literal-first) y B (analítica/escéptica) usan redacción
distinta a propósito (mismo esquema), para que la conciliación detecte fragilidad
y no eco del prompt.

## 5. Fase 1 — descubrimiento (baseline + pasada web en vivo)

Corrida del baseline (canal A.0) **más descubrimiento web en vivo** en cuatro
oleadas con ~27 investigadores paralelos: (1) 6 regionales + 5 temáticos
transversales; (2) piloto ampliado AR/BR/CL; (3) método ampliado en los 15 países
con 0-1 caso; (4) método ampliado profundo en los densos CO/MX/BR/CL/CR. Detalle
en `descubrimiento_web.md`, `piloto_busqueda_ampliada.md`,
`descubrimiento_paises_flacos.md` y `descubrimiento_densos.md`.

- `candidatos.csv`: **97 filas, cobertura 20/20** — 28 activos del baseline + 49
  excluidos a re-verificar + **18 candidatos nuevos/dudosos de la web** + 2
  placeholders (solo **JM, SV** sin ninguna señal).
- **Directorio de medios A.10**: `data/baseline/directorio_medios.csv` — **60
  medios, 20/20 países** (Anexo B parcial; A.10 ya operable). A.11 (instituciones)
  sigue pendiente del Anexo B.
- **18 candidatos NUEVOS** (10 sólidos + 8 dudosos): MX Guanajuato; CO Citibeats+
  PNUD; **CO ISIDataInsights (SDP Bogotá)**; BR Brasil Participativo (con evidencia
  de producción), e-Cidadania matching, São Paulo Participe Mais, 5ª CNCTI;
  PA Mansa Idea; CL LXS 400; **CL El Chile que Queremos (MinCiencia)**; + dudosos
  BR OPA Piauí, BR Cátedra Brasil, TT EngageTT, VE Plan de la Patria, CU Código de
  las Familias, CO POT Bogotá, CO DNP Diálogos Regionales, CL Senador Virtual.
- **13 reverificaciones** del baseline (fusionadas `canal_origen="A.0; A.x"`,
  `flag_canal_unico=0`), incl. **PE/PEN 2036 verificado con fuente primaria
  (IBM Watson)**, **CL/Cabildos 2016 con evidencia NLP** y **EC/PAGA IA con duda
  de elegibilidad** para Fase 2.
- Canales ampliados **A.12 (licitaciones), A.13 (premios), A.14 (proveedores)** +
  diccionario de términos codificados en `config.yaml`. `search_frame.csv`: 300 celdas.
- Vacíos confirmados (0 riguroso): **AR, UY, PY, SV, JM**. Concentración real de
  casos en **BR, CO, CL** (+ MX). No se hallaron despliegues de Pol.is/Talk to the
  City/Remesh en la región.

## 6. Motor 2026 sobre la base recodificada (BORRADOR) — Fases 4-5

`simulate.py` y `reproduce.py` corren end-to-end (BBDD presente):
- **Control 2025**: el motor legacy reproduce el oficial (Δ máx = 1). ✅
- **2026 retrospectivo**: DRAFT — usa `recodificacion_2025.csv` (pre-Gate).
  `reproduce.py` confirma reproducibilidad (recálculo idéntico).
- Salidas: `data/gates/simulacion_2026.md`, `gate3_report.md`, `reproduce_manifest.json`.

> Los números 2026 son **provisionales**: el `nivel_consolidacion` es conservador
> (sin nivel 3 salvo override con evidencia) y el `tipo_convocante` se derivó del
> texto “Organización a cargo”. No publicar sin Gate.

---

## 7. Decisiones que requieren al OPERADOR (no resueltas a propósito)

**Decisiones abiertas (§6)** — parametrizadas en `config.yaml`, sin decidir:
1. `cantidad.count_min_level` (default 2; se reporta también 0).
2. `cantidad.thresholds` (1–3/4–6/7–9/10+) — validar contra base recodificada.
3. `escenarios.scenario_activo` A/B (CiudadanIA DO y TQHCH CL dentro/fuera).
4. `redondeo.modo` (legacy/solo_final), `politicas.no_evidencia`,
   `politicas.casos_compuestos`, muestreo ALTA, umbral de escalamiento.

**Bloqueos / pedidos:**
- **Anexo B** (medios + instituciones por país): desbloquea A.10/A.11.
- **Propuesta v1.2**: validar el catálogo de canales A.1–A.11 contra su Anexo B.
- **`model_version`**: fijar en `config.yaml` la versión real del modelo Claude
  por corrida (hoy es placeholder).

**Ratificaciones (Gate 0):**
- Lista de campos críticos con verbatim (`config.campos_criticos`).
- **Recodificación 2025 BORRADOR** (`data/baseline/recodificacion_2025.csv`):
  revisar `tipo_convocante` de casos con juicio (BCN, CNE, GENIA, ParticipAct) y
  decidir qué casos suben a `nivel_consolidacion` 3 (override + evidencia de
  recurrencia, p. ej. e-Cidadania, Colab, Chatico).

## 8. Próximos pasos sugeridos

1. Conseguir Anexo B y ejecutar `search_frame.csv` (A.1–A.9) con fetch para
   generar candidatos nuevos.
2. Gate 1 (humano) sobre `candidatos.csv`.
3. Fase 2 (doble pasada en Claude) sobre candidatos aprobados; `verify_verbatim`
   en cada ficha.
4. Validar la recodificación y los parámetros de `config.yaml` antes de publicar.

## 9. Criterios de “hecho” (§11)

- ✅ No-regresión legacy en verde (BBDD presente) y suite sintética 2026 en verde.
- ✅ `verify_verbatim.py` operativo y probado (toda cita = subcadena exacta).
- ✅ Ningún número fuera de tablas generadas por el motor.
- ✅ `candidatos.csv` cubre los 20 países y registra canal de origen.
- ✅ Toda decisión abierta vive en `config.yaml`, no hardcodeada.
