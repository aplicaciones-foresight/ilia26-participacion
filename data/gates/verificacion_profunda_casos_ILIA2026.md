# Verificación profunda de casos marcados — ILIA 2026 (Participación)

Segunda pasada (opción del operador) sobre los **15 casos marcados** en la
validación web, con estándar más alto: **fuentes primarias** (documentos
oficiales, repositorios, papers, plataformas) y **cita verbatim** para fijar el
`rol_IA`. Un verificador dedicado por caso.

**Regla de decisión:** `rol_IA = contenido` (la IA analiza/clasifica/agrupa/
resume el contenido participativo) ⇒ **elegible**. `rol_IA ∈ {apoyo, sin_IA}`
(la IA es periférica o no existe sobre el contenido) ⇒ **excluir**.

Resultados por caso en la hoja *Verificación profunda* del xlsx y en
`verificacion_profunda_resultados.json` (con cita + URL). El `rol_IA` verificado
quedó fijado en `recodificacion_2025.csv` con su cita.

## Resultado

| | N° | Efecto |
|---|---:|---|
| Verificados **EXCLUIR** (`apoyo`/`sin_IA`) | **12** | salen del conjunto |
| Verificados **INCLUIR** (`contenido`) | **3** | se mantienen |
| **Conjunto elegible** | **A = 25** (antes 37) · **B = 24** | 15 baseline + 10 nuevos |

## ✅ Rescatados — la IA SÍ procesa el contenido (3 → se mantienen)

| País | Caso | rol_IA | Conf. | Evidencia (verbatim resumida) |
|---|---|---|---|---|
| CL | Tenemos que hablar de Chile | contenido | media | El Instituto de Argumentación (U. de Chile) *«aplica un algoritmo de procesamiento de lenguaje natural»* sobre las opiniones, tras anotación manual (uchile.cl). Refuta la hipótesis de sistematización solo manual. |
| CO | Tenemos que hablar de Colombia | contenido | alta | Usa el **mismo motor NLP** transferido desde TQH Chile; las respuestas van a una *«plataforma de análisis de texto»* que halla tendencias, emociones y recurrencias (uchile.cl / ideaspaz.org). |
| BR | Plan Plurianual de Natal | contenido | media | El asistente con IA *«organiza essas contribuições por tema, por bairro e por perfil de quem enviou»* para los técnicos (natal.rn.gov.br). Clasificación de contenido. |

> La verificación profunda **evitó excluir por error** estos 3 casos legítimos
> que la búsqueda rápida no había podido confirmar.

## ❌ Confirmados fuera — la IA no procesa el contenido participativo (12)

**`rol_IA = apoyo`** (IA real, pero periférica):

| País | Caso | Conf. | Rol real de la IA |
|---|---|---|---|
| CR | dIAra | alta | Visión por computador sobre imágenes de obras (repo GitHub de la CGR). |
| HN | RedPública + iVerify | alta | iVerify actúa sobre **desinformación**, no sobre las propuestas (UNDP). |
| BR | ParticipACT Brasil | alta | ML de **crowdsensing**/sensores urbanos, no deliberación (paper UNIBO). |
| CL | LXS 400 – Chile Delibera | alta | IA para **muestreo**/selección de la muestra (Senado, Stanford CDD). |
| DO | CiudadanIA | media | Asistente de **atención/trámites** (tipo Taína); además Escenario A/B. |
| TT | EngageTT (Go Vocal) | media | IA es capacidad del producto; sin evidencia de uso en la consulta NDTS. |

**`rol_IA = sin_IA`** (no hay IA sobre el proceso):

| País | Caso | Conf. | Hallazgo |
|---|---|---|---|
| CR | U-Report Costa Rica | alta | Chatbot de encuestas sobre **RapidPro (reglas/flujos)**, no NLP. |
| CL | Jornada de Escucha IPP-UNAB | alta | Evento interno de lanzamiento; sin IA; dashboard Tableau manual. |
| CL | La voz de los nuevos votantes | alta | Encuesta de terreno tradicional; sin IA sobre el contenido. |
| MX | Presupuesto CRECES | alta | El chatbot 'Hola' es **canal de voto**/atención general, no analiza propuestas. |
| CL | Estrategia de Gobierno Digital | media | La IA es el **tema** consultado; los aportes se evaluaron por criterios humanos. |
| CO | DNP – Diálogos Regionales Vinculantes | media | Codificación cualitativa manual + estadística; la "nota interna" de NLP no se corroboró. |

## Cómo quedó reflejado

- **`recodificacion_2025.csv`**: `rol_IA` fijado a `apoyo`/`sin_IA` en los 9 casos
  baseline afectados, cada uno con su cita verbatim (cumple la regla del proyecto
  de que todo `rol_IA` crítico lleva verbatim). Los 3 `contenido` quedan
  confirmados; los 3 casos nuevos excluidos (TT, CL LXS 400, CO DNP) viven en la
  planilla/config.
- **`config.yaml › validacion_2026`**: `politica: verificado`, con
  `verificados_excluir` (12) y `verificados_incluir` (3).
- **Planilla**: columnas *rol_IA verificado*, *Recomendación final*, *Confianza*,
  *Cita verbatim*, *Fuente* en *Detalle consolidado* + hoja *Verificación profunda*.

## Salvedades (para el operador)

1. **5 verificaciones son de confianza `media`** (DO CiudadanIA, TT EngageTT,
   CL Estrategia GD, CO DNP; y de los rescatados, CL TQHCH y BR Natal): el hecho
   sustantivo está corroborado, pero varios dominios oficiales devuelven 403
   anti-bot / bloqueo de egress, por lo que algunas citas se reconstruyeron de la
   indexación de búsqueda y no se verificaron carácter a carácter. Si se requiere
   cerrar al 99%, conseguir el PDF/fuente primaria por un canal sin ese bloqueo.
2. **Escenario A/B**: con la verificación, DO CiudadanIA ya sale (apoyo). El único
   caso A/B que aún depende del escenario es **CL Tenemos que hablar de Chile**
   (dentro en A, fuera en B) ⇒ A = 25, B = 24.
3. Nada es irreversible: cualquier caso puede revertirse si aparece evidencia
   primaria adicional.
