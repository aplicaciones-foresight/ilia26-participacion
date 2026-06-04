# Pipeline ILIA 2026 — Indicador de IA en Participación Ciudadana

Infraestructura para la **búsqueda exhaustiva y sistemática de casos** de IA
aplicada a participación ciudadana en América Latina (ciclo ILIA 2026) y el
cálculo determinístico de los dos subindicadores.

Universo: **19 países** (ISO-2): AR, BO, BR, CL, CO, CR, CU, DO, EC, GT, HN, JM,
MX, PA, PE, PY, SV, UY, VE.

## Reglas de oro

1. **Ningún número sale de memoria.** Todo cálculo proviene de la BBDD vía el
   motor (`src/calc_engine.py`). Si la BBDD no está, el cálculo se bloquea y se
   reporta; no se estima.
2. **100 % Claude.** La extracción corre en Claude, en **doble pasada** con
   prompts independientes (`prompts/prompt_extraccion_v1.1_A.txt` y `_B.txt`),
   conciliada por script determinístico. Se registra `model_version` por ficha.
3. **No inferir lo que no esté en el texto.** Toda celda crítica lleva **cita
   verbatim** verificada por `src/verify_verbatim.py`. Mejor `null` + alerta que
   un valor plausible.
4. **Los gates son humanos.** El pipeline prepara insumos; no autoaprueba, no
   cierra casos, no publica.
5. **Las decisiones abiertas no se resuelven en código.** Viven en `config.yaml`
   (escenario A/B, `count_min_level`, cortes de cantidad, muestreo, redondeo…).

## Arquitectura (5 fases, 3 gates)

```
Fase 1 DESCUBRIMIENTO ─► Gate 1 ─► Fase 2 EXTRACCIÓN (doble pasada)
 ─► Fase 3 CONCILIACIÓN ─► Gate 2 ─► Fase 4 CÁLCULO ─► Gate 3 ─► Fase 5 PUBLICACIÓN
```

| Fase | Script | Salida |
|---|---|---|
| 1 Descubrimiento | `src/discover.py` | `data/candidatos/candidatos.csv`, `search_frame.csv`, `data/gates/gate1_report.md` |
| 2 Extracción | `src/extract.py` | `data/fetched/<id>/`, `data/fichas/<id>_A.json`, `_B.json` |
| (verbatim) | `src/verify_verbatim.py` | citas = subcadenas exactas; campos no verificables → `null` + alerta |
| 3 Conciliación | `src/reconcile.py` | `data/fichas/<id>_conciliada.json` (+ `_diff.md`), confianza ALTA/MEDIA/BAJA |
| 4 Cálculo | `src/calc_engine.py`, `src/simulate.py` | tablas comparativas (`data/gates/simulacion_2026.md`) |
| 5 Publicación | `src/reproduce.py` | `data/gates/gate3_report.md`, `reproduce_manifest.json` |

## Metodología 2026 (resumen operativo)

**Subindicador de Uso (Sub1)** — 5 variables, promedio simple, máximo absoluto:

| Variable | Cálculo |
|---|---|
| Tipos de Proceso | nº de tipos distintos (de 5) ÷5 ×100 |
| Etapas de Uso | nº de etapas distintas (de 4) ÷4 ×100 |
| Continuidad | **nivel máximo del país** (0–3) ÷3 ×100 |
| Organización Convocante | (g/3 + ng/4)/2 ×100 (gubernamental 3 cat., no-gub. 4 cat.) |
| Cantidad de iniciativas | N de casos elegibles → umbrales fijos (config) |

**Subindicador de Desarrollo (Sub2)** — **idéntico a 2025** (§4.3): no se toca.

**Indicador** = (Sub1 + Sub2) / 2. Redondeo configurable (`redondeo.modo`).

## Cómo correr

```bash
pip install -r requirements.txt

# Tests (siempre primero)
python tests/test_noregresion_legacy.py     # legacy 2025 reproduce el oficial (±1)
python tests/test_compute_2026.py           # suite sintética 2026
python tests/test_verify_verbatim.py
python tests/test_extract_validacion.py
# o con pytest: pytest -q tests/

# Fase 1
python src/discover.py

# Fase 2 (por candidato aprobado en Gate 1)
python src/extract.py --prepare <candidato_id>     # fetch + arma payloads A/B
#   (Claude responde _payload_A.txt y _payload_B.txt -> guardar _A.json / _B.json)
python src/extract.py --validate data/fichas/<id>_A.json --texto data/fetched/<id>

# Fase 3
python src/reconcile.py <id>

# Fase 4 y 5 (requieren BBDD)
python src/simulate.py
python src/reproduce.py
```

## Decisiones abiertas (en `config.yaml`, NO en código)

- **Escenario A/B** (`escenarios.scenario_activo`): A mantiene DO CiudadanIA y
  CL «Tenemos que hablar de Chile»; B los retira. Exclusiones firmes (siempre
  fuera): CO Descongestión, MX Sufragio Seguro, PE Sistema de cómputo 2026.
- **Alcance de Cantidad** (`cantidad.count_min_level`): default 2 (solo nivel ≥
  2); reportar ambos (0 y 2).
- **Cortes de Cantidad** (`cantidad.thresholds`): 1–3/4–6/7–9/10+, a validar.
- **Redondeo** (`redondeo.modo`): `legacy` (subindicadores primero, como 2025) o
  `solo_final`.
- Muestreo ALTA (10–15 %), umbral de escalamiento (5 %), política de
  no-evidencia, casos compuestos.

## ⚠️ Recodificación 2025 → 2026 (BORRADOR, pre-Gate)

`data/baseline/recodificacion_2025.csv` mapea los 28 casos del baseline al
esquema 2026 (`tipo_convocante` 7-cat. + `nivel_consolidacion` 0–3). Es un
**borrador derivado de la columna “Organización a cargo”** de la BBDD, con
reglas conservadoras:

- `nivel_consolidacion`: Uso único / Plataforma → **2** (puntual); “Próximamente”
  → **1** (anuncio). El **nivel 3 (permanente) solo se asigna vía la columna
  `nivel_consolidacion_override`** con evidencia de recurrencia (decisión del
  Gate). Por eso las columnas 2026 de `simulacion_2026.md`/`gate3_report.md`
  llevan la marca **DRAFT** hasta validación humana.
- `tipo_convocante`: derivado del nombre textual del convocante; los casos con
  juicio (p. ej. BCN, CNE, GENIA, ParticipAct) van anotados en la columna `nota`.

## Estructura

```
config.yaml                     parámetros (todas las decisiones abiertas)
data/baseline/                  BBDD 2025 (solo lectura) + recodificación BORRADOR
data/candidatos/                candidatos.csv + search_frame.csv
data/fetched/<id>/              textos fetcheados (insumo verbatim)
data/fichas/<id>_*.json         fichas A/B/conciliada
data/gates/                     reportes de gates + logs + manifiestos
prompts/                        v1 (intacto) + v1.1-A/B + schema_ficha_v1.1.json
src/                            calc_engine, discover, extract, verify_verbatim,
                                reconcile, simulate, reproduce
tests/                          no-regresión legacy + sintéticos 2026 + verbatim
docs/                           calc_engine_2025_original.py (referencia)
```

Ver `SESSION_LOG.md` para el estado de la sesión y los pendientes del operador.
