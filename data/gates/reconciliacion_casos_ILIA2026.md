# Planilla consolidada de casos ILIA 2026 — Participación Ciudadana

Reconciliación de **dos fuentes de decisión** frente al baseline 2025:

1. **Revisión humana** — `Casos_a_Profundizar.xlsx`, hoja *Lista Final*
   (votos Natalia / Nicole / Jose).
2. **Decisiones del operador** — `config.yaml` (escenario A/B,
   `exclusiones_firmes`) + **recodificación 2026** (`recodificacion_2025.csv`,
   campo `rol_IA` = contenido/apoyo).

Planilla: **`data/gates/Planilla_Consolidada_Casos_ILIA2026.xlsx`**
(hojas *Resumen*, *Detalle consolidado*, *Excluidos 2025 (universo)*).
Generada por `src/generar_planilla_decisiones.py`.

## Conjunto elegible 2026 (lo que cuenta en el indicador)

| Escenario | N° de casos | Composición |
|---|---:|---|
| **A (activo)** | **37** | 24 baseline + 13 nuevos |
| B | 35 | A − DO CiudadanIA − CL «Tenemos que hablar de Chile» |

## Reglas de reconciliación aplicadas

- **R1 — `rol_IA = apoyo` ⇒ EXCLUIDO firme.** La IA asiste el proceso pero **no
  procesa el contenido participativo**. Exclusión ya decidida en `config.yaml`
  (`exclusiones_firmes`) y en la recodificación 2026. Afecta a **CO Descongestión
  (Ingreso Solidario)**, **MX Sufragio seguro** y **PE Sistema de cómputo**. En
  Descongestión y PE los revisores votaron **`SI`**, pero ese voto ratifica
  **actividad**, no elegibilidad ⇒ **conflicto resuelto a favor de la
  metodología** (marcado para ratificar).
- **R2 — Escenario activo = A** (`config.yaml › escenarios.scenario_activo`).
  **DO CiudadanIA** y **CL «Tenemos que hablar de Chile»** se mantienen bajo A y
  salen bajo B (columna *Cuenta en indicador* = «Sí bajo A · No bajo B»).
- **R3 — Baseline reconfirmado con `rol_IA = contenido` se mantiene** aunque no
  esté en la lista de revisión ⇒ **CR dIAra** (reconfirmado por OGP 2025).
- **R4 — El voto de los revisores manda** en casos nuevos/dudosos y en el
  **duplicado** (CL «Participación Ciudadana Proceso Constitucional»: se conserva
  una copia, se elimina la otra).

## Conteo por categoría

| # | Categoría | N° |
|---|---|---:|
| 1 | Baseline que se mantiene | **24** |
| 2 | Baseline eliminado (y razones) | **4** |
| 3 | Eliminado 2025 incorporado | **0** |
| 4 | Eliminado 2025 que se mantiene eliminado | **49** |
| 5 | Nuevo que se incorpora | **13** |
| 6 | Nuevo que NO se incorpora (y razones) | **5** |

---

## 1. Baseline que se mantiene (24)

Incluye los 22 casos del baseline votados `SI` con `rol_IA = contenido`, más
**CR dIAra** (R3) y **DO CiudadanIA** (R2, bajo A). Dos casos dependen del
escenario: **CL Tenemos que hablar de Chile** y **DO CiudadanIA** (cuentan bajo
A, salen bajo B).

## 2. Baseline eliminado — con razones (4)

| País | Caso | Decisión | Razón |
|---|---|---|---|
| CL | Participación Ciudadana Proceso Constitucional | EXCLUIDO (duplicado) | Figura dos veces en el baseline; se conserva una copia. *(La recodificación los anotaba como homónimos distintos —autoconvocados vs audiencias—; ratificar.)* |
| MX | Sufragio seguro | EXCLUIDO (firme) | `rol_IA = apoyo` (integridad/proceso electoral, no contenido). Revisores también `NO`. |
| CO | Descongestión (Ingreso Solidario) | EXCLUIDO (firme) ⚠ | `rol_IA = apoyo` (atención, no contenido). **Conflicto:** revisores `SI` = solo actividad. |
| PE | Sistema de cómputo Elecciones 2026 | EXCLUIDO (firme) ⚠ | `rol_IA = apoyo` (conteo OCR de actas, no participación). **Conflicto:** revisores `SI` = solo actividad. |

## 3. Eliminado 2025 incorporado (0)

Ningún excluido de 2025 fue reincorporado.

## 4. Eliminado 2025 que se mantiene eliminado (49)

5 re-revisados en la lista final (todos `NO`): CL Plataforma UCampus · CO «Pa'
que veás» · CO Asamblea Ciudadana Itinerante · CO Mini-Public Procuraduría ·
CO iLabs. Los 44 restantes no se re-revisaron y se mantienen fuera por defecto
(detalle en la hoja *Excluidos 2025 (universo)*).

## 5. Nuevo caso que se incorpora (13)

BR: 5ª Conferencia CT&I · Brasil Participativo (clustering) · Cátedra Brasil/Co:Lab
USP · e-Cidadania (matching) · OPA Piauí · São Paulo Participe Mais. ·
CL: El Chile que Queremos · LXS 400. · CO: Citibeats+PNUD · DNP Diálogos
Regionales. · MX: Guanajuato Inteligente. · PA: Mansa Idea. · TT: EngageTT.

## 6. Nuevo caso que NO se incorpora — con razones (5)

| País | Caso | Razón (verbatim/ síntesis) |
|---|---|---|
| CL | Senador Virtual / CrowdLaw | *«No encontré que hayan usado IA finalmente»* / *«fue un seminario»*. |
| CO | IA para participación en el POT de Bogotá | *«Es solo una investigación, no algo implementado»*. |
| CU | Consulta Popular Código de las Familias | *«Según lo que busqué, no usaron IA»*. |
| VE | Plan de la Patria 7T – IA y Big Data | Fuente estatal única; *«no creo que cumpla con los criterios»*. |
| CO | ISIDataInsights / 'Datos con Historia' | No se pudo acceder a las URLs ni hallar evidencia operativa. |

---

## Puntos que aún requieren ratificación del operador

1. **Conflicto R1**: confirmar que **CO Descongestión** y **PE Sistema de
   cómputo** se excluyen pese al `SI` de actividad de los revisores (criterio
   `rol_IA = apoyo`). Si el operador decidiera incluirlos, el conjunto A sube a 39.
2. **Escenario A/B**: la base usa **A** (37). Con **B** son 35.
3. **Duplicado CL**: confirmar que es duplicado y no dos procesos distintos
   (autoconvocados vs audiencias), como sugería la recodificación.
