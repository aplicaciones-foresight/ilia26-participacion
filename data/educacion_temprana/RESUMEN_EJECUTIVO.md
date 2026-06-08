# Resumen ejecutivo — Educación temprana en IA (subindicador *b*, ILIA) · 5 países benchmark

**Encargo.** Replicar el subindicador **(b) «Educación temprana en IA»** del índice **ILIA 2025
(CEPAL/CENIA)** para cinco países de referencia no latinoamericanos —**Portugal, España,
Estonia, Alemania y Singapur**— mediante revisión del **currículo escolar oficial vigente**
(¿incluye IA y/o TIC, y en qué grado de implementación?). El puntaje se asigna sobre **secundaria**.

## Resultado (verificado *verbatim*, 2026-06-06)

| País | Categoría | Puntaje | Confianza | Base de la IA en el currículo |
|---|:--:|:--:|:--:|---|
| **España** | **5** | **100** | alta | «inteligencia artificial» en RD 217/2022 (ESO) y RD 243/2022 (Bachillerato) — BOE |
| **Alemania** | **5** | **100** | alta | «Künstliche Intelligenz» en *LehrplanPLUS* Bayern (módulo de 16 h) y *KLP* NRW |
| **Estonia** | **5** | **100** | alta | «tehisintellekt» en la electiva *Informaatika* (Lisa 10 del PRÕK) |
| **Singapur** | **5** | **100** | alta | «Artificial Intelligence / Machine Learning» en el syllabus *Computing 7155* |
| **Portugal** | 4 | 75 | alta | TIC implementado; IA **aún no vigente** (revisión con horizonte 2027) |

### **Promedio del grupo: 95 / 100** (regla inclusiva)

## Hallazgos clave

- **4 de 5 países alcanzan la categoría máxima (5 = «IA implementada»).** Solo Portugal queda en
  4: su IA no está aún en vigor (la incorpora una revisión curricular prevista para 2027).
- **Todas las determinaciones están verificadas *verbatim*:** las 15 citas decisivas son
  **subcadena exacta** del documento oficial primario (BOE, *LehrplanPLUS*/*KLP*, Riigi Teataja,
  SEAB). Reporte reproducible en `fuentes/_verify_report.json` (15/15 OK).
- **Gradiente de robustez dentro de los «5»:** en **España y Alemania** la IA es contenido
  **sustantivo** del currículo vinculante (saberes y criterios del BOE; un *Lernbereich* propio de
  16 h en Baviera). En **Estonia y Singapur** la IA es un **subtema** dentro de una asignatura
  **electiva**.

## Regla metodológica y nota sobre cursos electivos

- **Regla aplicada (confirmada con el equipo del ILIA): inclusiva.** Los **cursos electivos se
  consideran** parte del currículo nacional; la IA en *cualquier* asignatura vigente —troncal o
  **electiva**— cuenta como «IA implementada» (categoría 5).
- **Nota — Estonia y Singapur (cursos electivos).** En estos dos países el contenido de IA del
  currículo nacional vigente se imparte en una **asignatura electiva** (Estonia: *Informaatika*,
  *valikõppeaine*; Singapur: *Computing 7155*), no troncal de cursado universal, y aparece como
  **subtema**. Por la regla del ILIA (electivos cuentan), ambos se clasifican en **categoría 5**;
  se documenta esta condición por transparencia.
- **Sensibilidad (informativa, no adoptada).** Una lectura estricta que exigiera contenido troncal
  o sustantivo dejaría a Estonia y Singapur en 4 y el promedio del grupo en **85** (en vez de 95).

| Escenario | EE | SG | **Promedio grupo** |
|---|:--:|:--:|:--:|
| **Inclusiva** (adoptada, ILIA) | 5 | 5 | **95** |
| Estricta (solo informativa) | 4 | 4 | **85** |

> Calibración LatAm 2025 (referencia): categoría 5 = Brasil, Chile, Costa Rica, Ecuador, Rep.
> Dominicana, Uruguay; resto = 4.

> Detalle por país en `informe.md` y `fichas/`; trazabilidad de cada cita en
> `evidencias/evidencias.json` y `fuentes/_verify_report.json`.
