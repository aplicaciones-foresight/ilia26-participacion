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

## Decisión metodológica y sensibilidad

- **Regla aplicada (registrada): inclusiva** — la IA presente en *cualquier* asignatura del
  currículo nacional vigente, **incluidas las electivas**, cuenta como «implementada».
- **Sensibilidad:** bajo una regla **estricta** (IA solo si es contenido *sustantivo* o de cursado
  *universal*), **Estonia y Singapur volverían a 4** y el promedio del grupo pasaría de **95 a 85**.

| Escenario | EE | SG | **Promedio grupo** |
|---|:--:|:--:|:--:|
| **Inclusiva** (elegida) | 5 | 5 | **95** |
| Estricta | 4 | 4 | **85** |

**Recomendación.** Reportar ambos valores (95 / 85) y, para comparabilidad, alinear la regla con
la convención que usó **SITEAL** en la calibración latinoamericana (en LatAm 2025, categoría 5 =
Brasil, Chile, Costa Rica, Ecuador, Rep. Dominicana, Uruguay; resto = 4).

> Detalle por país en `informe.md` y `fichas/`; trazabilidad de cada cita en
> `evidencias/evidencias.json` y `fuentes/_verify_report.json`.
