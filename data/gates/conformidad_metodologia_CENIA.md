# Conformidad con la metodología final CENIA (v2 · jun-2026)

**Referencia:** `metodologia_final_CENIA_v2.xlsx` (hoja «IA en Participación 2026»).
**Objeto:** verificar que los datos que construimos, la planilla de validación y el
motor de cálculo coinciden con la metodología final acordada con el CENIA.
**Resultado:** **conforme**. Los datos ya soportaban la metodología nueva; se
alinearon 2 puntos del motor de cálculo (Organización Convocante y Cantidad) y
se actualizó la guía. Suite de tests: **36/36 OK**.

---

## 1. Estructura general — conforme
- **Indicador = (Sub-Uso + Sub-Desarrollo) / 2.** ✔
- **Sub-Uso = promedio simple de 5 variables** (Tipos de proceso, Etapas de uso,
  Continuidad, Organización Convocante, Cantidad de iniciativas). ✔
- **Sub-Desarrollo idéntico a 2025** (desarrollador nacional/internacional ×4 tipos
  por máximo relativo + tipos de IA por máximo relativo). ✔ — código sin tocar
  (`test_sub2_identico_a_legacy` y no-regresión legacy 19/19 pasan).

## 2. Variable por variable

| Variable | Metodología CENIA v2 | Estado motor | Estado datos |
|---|---|---|---|
| Tipos de proceso | 5 tipos, máx. absoluto ÷5 | ✔ `len(tipos)/5` | ✔ taxonomía canónica |
| Etapas de uso | 4 etapas, máx. absoluto ÷4 | ✔ `len(etapas)/4` | ✔ |
| Continuidad | **nivel máximo verificado** del país ÷3; anuncio caduca a 2 años | ✔ `max(niveles)/3`; caducidad en `config.yaml` | ✔ nivel 0-3 por caso |
| Organización Convocante | **3 sub-componentes co-iguales** (ver §3) | ✔ **alineado** | ✔ co-convocatoria capturada |
| Cantidad de iniciativas | **todas** las elegibles; umbrales fijos 0→0·1-3→25·4-6→50·7-9→75·10+→100 | ✔ **alineado** (`count_min_level=0`) | ✔ 1 fila = 1 iniciativa |

## 3. Organización Convocante — el cambio principal

La metodología final la redefine como **tres sub-componentes co-iguales (⅓ c/u)**:

1. **Amplitud gubernamental** = nº de tipos gubernamentales distintos ÷ 3
   (gobierno local · gobierno nacional · otra institución pública).
2. **Amplitud no gubernamental** = nº de tipos no gubernamentales distintos ÷ 4
   (empresa · **universidad** · sociedad civil · organización internacional).
3. **Co-convocatoria** = nº de combinaciones distintas (conjuntos de ≥2 tipos que
   co-convocan una misma iniciativa, **deduplicadas**) ÷ **máximo relativo móvil**
   del ciclo.

`v_convocante = (amp_gub + amp_nogub + co_convocatoria) / 3 × 100`

- Antes teníamos un convocante a **2 niveles** (gubernamental/no-gubernamental).
  Se reescribió `compute_2026` a los **3 sub-componentes** con co-convocatoria por
  máximo relativo. Ver `src/calc_engine.py` (`CONV_GUB` / `CONV_NOGUB`, Pass-1/Pass-2).
- **Universidades públicas cuentan como «Universidad»** (no gubernamental), no como
  «otra institución pública» — tal como exige la nota metodológica. Auditamos las
  107 fichas: los 84 valores de convocante ya usan las 7 categorías canónicas y
  **ninguno** clasifica una universidad como institución pública. ✔

### Co-convocatoria en los datos actuales (antes de las exclusiones manuales)
Entre las iniciativas elegibles hay **10 casos co-convocados** (≥2 tipos), que
producen las siguientes combinaciones distintas por país:

| País | Combinaciones distintas | Ejemplo |
|---|---|---|
| BO | 1 | gobierno nacional + organización internacional |
| CL | 2 | (empresa+sociedad civil) · (gob. nacional+sociedad civil+universidad) |
| CO | 2 | (gob. local+org. internacional) · (empresa+sociedad civil+universidad) |
| DO | 1 | empresa + gobierno nacional + universidad |
| EC | 1 | gobierno nacional + sociedad civil |
| GT | 1 | organización internacional + sociedad civil |
| HN | 1 | organización internacional + universidad |
| PA | 1 | gobierno nacional + sociedad civil |

**Máximo relativo del ciclo (denominador de co-convocatoria) = 2.** *(Este número
se recalcula solo al aplicar las exclusiones manuales; el motor lo hace en cada
corrida — no hay que fijarlo a mano.)*

## 4. Cantidad de iniciativas — segundo ajuste
- Metodología final: **«número de iniciativas ELEGIBLES identificadas por país»**,
  sin filtro de nivel de consolidación.
- `config.yaml`: `count_min_level` **2 → 0** (cuenta todas las elegibles). Los cortes
  ya coincidían: 0→0 · 1-3→25 · 4-6→50 · 7-9→75 · 10+→100. ✔
- `reportar_ambos: true` se mantiene: `simulate.py` puede imprimir también el
  conteo con `count_min_level=2` como sensibilidad, pero el **oficial es 0**.

## 5. Principio de normalización — conforme
La metodología usa **escalas fijas** (máximo absoluto y umbrales) en todo el
Sub-Uso **salvo** el sub-componente de co-convocatoria, que usa **máximo relativo
móvil** (como el Sub-Desarrollo). El motor implementa exactamente esa excepción:
`amp_gub` y `amp_nogub` normalizan por máximo absoluto (÷3, ÷4); la co-convocatoria
por máximo relativo del ciclo. ✔

## 6. Qué cambió en el repo
| Archivo | Cambio |
|---|---|
| `src/calc_engine.py` | `compute_2026`: Organización Convocante a 3 sub-componentes con co-convocatoria (máx. relativo); Cantidad cuenta todas las elegibles. |
| `config.yaml` | `count_min_level: 2 → 0` (+ comentario CENIA v2). |
| `tests/test_compute_2026.py` | Tests de convocante a la fórmula de 3 sub-componentes + test de dedup de co-convocatoria. |
| `src/export_planilla_simple.py` | Guía (pestaña 5 + `.md`): explica los 3 sub-componentes, co-convocatoria y conteo de todas las elegibles. |
| `data/gates/metodologia_final_CENIA_v2.xlsx` | Copia de la metodología de referencia en el repo. |

## 7. Qué NO cambió (correctamente)
- **Sub-Desarrollo** (2025): intacto.
- **Regla de elegibilidad**: la IA procesa el CONTENIDO de los aportes dentro de un
  proceso participativo. Sin cambios.
- **Exclusiones manuales**: siguen siendo del equipo (no automatizadas), como pediste.
- **Taxonomías** (5 tipos de proceso, 4 etapas, 7 convocantes, niveles 0-3): ya
  coincidían con la metodología.

---

**Conclusión:** los pasos de validación manual y el cálculo posterior **coinciden con
la metodología final CENIA v2**. Las únicas dos divergencias estaban en el motor
(fórmula de convocante y alcance del conteo) y quedaron alineadas y testeadas.
