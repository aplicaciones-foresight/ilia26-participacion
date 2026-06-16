# Indicador ILIA — Cantidad de programas de doctorado de IA (países extra)

Identificación y conteo de **programas de doctorado que forman competencias en
inteligencia artificial (IA)** en cinco países de referencia ("países extra"):
**Alemania, España, Portugal, Singapur y Estonia.**

> Este indicador es **distinto** del de Participación Ciudadana que vive en el
> resto del repositorio; se aísla en la carpeta `doctorados_ia/`. Comparte, eso
> sí, las **reglas de oro** del proyecto: ningún dato sale de memoria, toda
> celda crítica lleva su **fuente verificable**, y es preferible marcar
> `PENDIENTE`/duda que afirmar un valor plausible no comprobado.

---

## 1. Fuente de datos y cobertura

El análisis se basa en la revisión sistemática de los programas de doctorado
ofrecidos por las universidades incluidas en el **QS World University Rankings
2026**, considerando cinco países:

| País | Cód. | Universidades en QS 2026 (esperado) |
|---|---|---|
| Alemania | DE | 49 |
| España | ES | 38 |
| Portugal | PT | 9 |
| Singapur | SG | 4 |
| Estonia | EE | 3 |
| **Total** | | **103** |

La consulta se realiza directamente sobre las páginas web oficiales de cada
institución (fichas de programas doctorales, líneas de investigación, planes de
estudio y publicaciones). **Limitación inherente declarada por la metodología:**
la información en línea puede estar desactualizada, incompleta o publicada en el
idioma local.

## 2. Criterio de inclusión de programas

Se prioriza la búsqueda dentro de **facultades de Tecnología e Ingeniería**,
**excluyendo** programas adscritos a facultades de **Negocios o Economía**.
Dentro de ese universo, la selección se guía por palabras clave: ciencias de la
computación, ciencia de datos, informática, estadística, ciencias de la
ingeniería y conceptos directamente vinculados a la IA.

## 3. Criterios de evaluación (en orden de prioridad)

- **Criterio 1 — Líneas de investigación (base):** presencia explícita de líneas
  de investigación en IA dentro del programa.
- **Criterio 2 — Objetivos / perfil de egreso:** declaración explícita de que el
  programa forma profesionales con competencias en IA.
- **Criterio 3 — Plan de estudio con ≥3 cursos (el más fuerte):** ≥3 asignaturas
  complementarias entre cursos preparativos y específicos de IA.
- **Criterio 4 — Trabajos de titulación (opcional):** tesis orientadas a IA, como
  refuerzo complementario.

Para ser incluido, un programa debe cumplir **al menos uno**, con peso especial
en C1 y C3.

## 4. Tipología de cursos

- **Cursos preparativos** (fundamentos): Álgebra Lineal, Probabilidad,
  Optimización Matemática, Ciencia de Datos, Métodos Numéricos, etc.
- **Cursos específicos** (técnicas/modelos/aplicaciones de IA): Aprendizaje
  Automático, Aprendizaje Profundo, PLN, Visión por Computadora, IA Generativa, etc.

## 5. Escala de evaluación

- **CUMPLE:** C1 + C3 (líneas IA + ≥3 cursos) **o** C1 + C2 (líneas IA +
  objetivos/perfil), con líneas declaradas de forma clara y verificable.
- **PARCIAL:** sólo C1 (declara líneas de investigación en IA) pero **sin plan de
  estudios público** que permita identificar ≥3 cursos. Responde a una limitación
  estructural del contexto europeo: la mayoría de los doctorados en Alemania,
  Portugal y Estonia son *research-based* (orientados casi exclusivamente a la
  investigación, con escaso *coursework* formal documentado). PARCIAL **no**
  implica que el programa no forme competencias en IA, sino que la evidencia
  disponible no permite confirmarlo con el rigor exigido.
- **NO CUMPLE:** no satisface ningún criterio.

---

## 6. Adaptación operativa de esta corrida (IMPORTANTE — leer)

### 6.1 Restricción del entorno de ejecución
Este entorno **no tiene salida de red directa**: `WebFetch` y `curl` devuelven
**HTTP 403** contra cualquier dominio (incluidas las webs oficiales de las
universidades, Wikipedia y QS/topuniversities). **Sólo funciona `WebSearch`**
(buscador proxy), que entrega **títulos, fragmentos (snippets) y URLs**, pero
**no** el contenido completo de las páginas.

**Consecuencia sobre la metodología:**
- C1 (líneas de investigación) y C2 (objetivos/perfil): a menudo verificables por
  los fragmentos de búsqueda.
- **C3 (≥3 cursos del plan de estudios): normalmente NO verificable por snippets**
  porque requiere abrir el plan de estudios. Esto empuja legítimamente muchos
  casos a **PARCIAL** y genera la marca **`requiere_acceso_manual`**.
- C4 (tesis): verificable de forma parcial (repositorios indexados).

Por eso cada fila lleva: las **URLs fuente** (para verificación manual del
equipo), un **nivel de confianza** (ALTA/MEDIA/BAJA) y una marca
**`requiere_acceso_manual`** indicando exactamente qué falta comprobar
(típicamente: abrir el plan de estudios para confirmar C3 y resolver
CUMPLE-vs-PARCIAL).

### 6.2 Unidad de conteo
El indicador es "cantidad de **programas** de doctorado de IA". La unidad es el
**programa doctoral** (una universidad puede tener más de uno; cada uno es una
fila). Se reporta también el nº de **universidades con ≥1 programa** que forma
competencias en IA.

### 6.3 Regla de conteo (decisión del operador, parametrizable)
Siguiendo la filosofía del proyecto ("reportar ambos"), se informan **tres
cifras** por país y total:
- `n_CUMPLE`
- `n_PARCIAL`
- `n_forma_competencias = n_CUMPLE + n_PARCIAL` (programas que **forman**
  competencias en IA según la escala; PARCIAL no niega la formación, sólo la
  evidencia).

**Pendiente de decisión del operador:** si el indicador publicado cuenta sólo
`CUMPLE` o `CUMPLE + PARCIAL`. No se resuelve en este documento.

### 6.4 Esquema de salida (columnas de `clasificacion.csv`)
`pais, universidad, qs_rank_2026, facultad_escuela, programa_doctorado,
c1_lineas_IA, c2_objetivos_perfil, c3_plan_min3_cursos, c4_tesis_IA,
clasificacion, cuenta(0/1 por regla), fuentes(URLs ; separadas),
confianza, requiere_acceso_manual, notas`

Valores:
- `c1`,`c2`,`c4`: `Si` / `No` / `Indicio` (evidencia parcial en snippet).
- `c3`: `Si` / `No` / `NoVerificable` (plan no accesible por snippets).
- `clasificacion`: `CUMPLE` / `PARCIAL` / `NO_CUMPLE` / `PENDIENTE`.
- `confianza`: `ALTA` / `MEDIA` / `BAJA`.
- `requiere_acceso_manual`: `No` o breve texto de qué abrir.

---

## 7. Estado de la corrida

Ver `SESSION_LOG.md` (bitácora, blockers y plan de continuación) y
`universidades_qs2026.csv` (universo QS 2026 con cobertura y fuentes).
Resultados por país en `paises/<cod>.md` y consolidado en `clasificacion.csv`.
