# Análisis de casos ILIA 2026 vs. baseline 2025 — Participación Ciudadana

**Qué se hizo con cada caso.** Comparación de la **planilla final**
(`Casos_a_Profundizar.xlsx`, hoja *Lista Final* — revisión humana de
Natalia / Nicole / Jose) contra la **BBDD baseline 2025**
(`BBDD_IA_Participacion_2025.xlsx`: 28 casos activos + 49 excluidos).

> **Regla aplicada:** la decisión sale del **voto de los revisores** (mayoría
> `SI` ⇒ se mantiene/incorpora; `NO` ⇒ elimina/no incorpora). En los 49 casos
> revisados los tres coinciden (`DE ACUERDO`). Las razones son **verbatim** de
> la columna *Comentarios* + *A verificar* + el motivo de exclusión 2025; no se
> infiere nada fuera de las planillas.

Planilla detallada: **`data/gates/Analisis_Casos_2026_vs_2025.xlsx`** (hojas
*Resumen*, *Detalle por caso*, *Excluidos 2025 (universo)*).

## Conteo por categoría

| # | Categoría | N° |
|---|---|---:|
| 1 | Baseline que se mantuvo | **24** |
| 2 | Baseline eliminado (y razones) | **2** |
| 0 | Baseline ausente de la lista final (a confirmar) | **2** |
| 3 | Eliminado 2025 incorporado (y razones) | **0** |
| 4 | Eliminado 2025 que se mantiene eliminado | **49** |
| 5 | Nuevo caso que se incorpora | **13** |
| 6 | Nuevo caso que NO se incorpora (y razones) | **5** |

Universo revisado en la lista final = 49 filas (26 baseline + 5 excluidos +
18 nuevos/dudosos). El baseline 2025 tiene 28 casos: 24 se mantienen, 2 se
eliminan y **2 no aparecen** en la lista de revisión (categoría 0).

---

## 1. Baseline que se mantuvo (24)

11 son **re-verificaciones 2026** (ratificadas con evidencia web): BO Bolivia
Conversa · BR Plan Plurianual de Natal · BR e-Cidadania (marcado automático) ·
CL Cabildos 2016 · CO Chatico · CO ECHO–HáblameD · CR U-Report · EC PAGA IA ·
GT Guatemala Joven Conversa · HN RedPública+iVerify · PE Consulta Ciudadana (PEN).

13 se ratifican como baseline 2025: BR Colab · BR ParticipACT · CL Estrategia de
Gobierno Digital · CL Estudio dIAlogos · CL Jornada de Escucha UNAB · CL La voz
de los nuevos votantes · CL Participación Ciudadana Proceso Constitucional ·
CL Tenemos que hablar de Chile · CL Un encuentro (equidad de género/movilidad) ·
CO Descongestión Ingreso Solidario · CO Tenemos que hablar de Colombia ·
MX Presupuesto CRECES · PE Sistema de cómputo IA Elecciones 2026.

## 2. Baseline eliminado (2)

| País | Caso | Razón (verbatim/ síntesis) |
|---|---|---|
| CL | Participación Ciudadana Proceso Constitucional | **Duplicado** (figura dos veces en el baseline; se mantiene una copia, se elimina ésta). |
| MX | Sufragio seguro | Revisores votan `NO`. *«Me gustaría que discutamos bien si esto lo considerarían»* / *«me quedan dudas de lo que se implementó»*; usa ML/visión para microexpresiones de estrés — pertinencia como participación en duda. |

## 0. Baseline ausente de la lista final — a confirmar (2)

Casos del baseline 2025 (Activo) que **no se incluyeron en la lista de revisión**;
requieren decisión explícita del operador:

- **CR — dIAra**: reconfirmado por web 2026 (OGP Open Gov Challenge): visión
  computacional sobre alertas de inspectores ciudadanos en obras públicas. La
  nota interna lo califica de *«que sí entra»* ⇒ **probablemente se mantiene**.
- **DO — CiudadanIA**: reverificación 2026 **sin evidencia nueva** específica de
  la plataforma. Es el caso del **Escenario A/B** (`config.yaml`: A lo mantiene,
  B lo retira) ⇒ depende de la decisión de escenario.

## 3. Eliminado 2025 incorporado (0)

**Ningún** caso excluido en 2025 fue reincorporado. Los 5 excluidos que se
re-revisaron se mantienen fuera (ver §4); los 44 restantes no se re-revisaron.

## 4. Eliminado 2025 que se mantiene eliminado (49)

**5 re-revisados** en la lista final (todos `NO`, se mantienen fuera):

| País | Caso | Motivo 2025 | Nota 2026 |
|---|---|---|---|
| CL | Plataforma UCampus | No evidencia de uso de IA | Sin IA confirmada sobre el contenido. |
| CO | "Pa' que veás" | No evidencia de uso de IA | Suena más a veeduría que a participación; IA sobre el contenido sin confirmar. |
| CO | Asamblea Ciudadana Itinerante (Concejo Bogotá) | No se halló uso de IA | Proceso elegible, pero sin IA sobre el contenido. |
| CO | Mini-Public diálogo social (Procuraduría) | No se halló uso de IA | Ídem. |
| CO | iLabs – Laboratorios de Inteligencia Colectiva | No se halló uso de IA | Ídem. |

**44 no re-revisados** (mayoría chatbots de atención ciudadana / sin IA / no
participación): se mantienen excluidos por defecto. Listado completo en la hoja
*Excluidos 2025 (universo)*.

## 5. Nuevo caso que se incorpora (13)

BR: 5ª Conferencia Nacional CT&I · Brasil Participativo (clustering BERTopic+LLM)
· Cátedra Brasil/Co:Lab USP · e-Cidadania (matching de ideas) · OPA Piauí ·
São Paulo Participe Mais (Gemini). · CL: El Chile que Queremos (MinCiencia) ·
LXS 400 – Chile Delibera. · CO: Citibeats+PNUD · DNP Diálogos Regionales
Vinculantes. · MX: Guanajuato Inteligente 2024-2030. · PA: Mansa Idea. ·
TT: EngageTT (Go Vocal).

## 6. Nuevo caso que NO se incorpora — con razones (5)

| País | Caso | Razón (verbatim/ síntesis) |
|---|---|---|
| CL | Senador Virtual / CrowdLaw (GobLab UAI + IMFD) | *«No encontré que hayan usado IA finalmente»* / *«fue un seminario»*; investigación no verificada en producción. |
| CO | IA para participación en el POT de Bogotá | *«Es solo una investigación, no algo implementado»* (artículo académico). |
| CU | Consulta Popular Código de las Familias (GEMA-CEN) | *«Según lo que busqué, no usaron IA»*; falta confirmar si es NLP/ML o reglas. |
| VE | Plan de la Patria 7T – IA y Big Data | Fuente estatal única; *«no creo que cumpla con los criterios»*; ningún proveedor/académico corrobora. |
| CO | ISIDataInsights / 'Datos con Historia' (SDP Bogotá) | No se pudo acceder a las URLs ni hallar evidencia operativa. |

---

## Observaciones para el operador (no se resuelven aquí)

1. **Categoría 0 (dIAra, CiudadanIA)**: confirmar su destino; no fueron sometidos
   a voto.
2. **Discrepancia con `config.yaml › exclusiones_firmes`**: el config marca
   **CO Descongestión (Ingreso Solidario)** y **PE Sistema de cómputo Elecciones
   2026** como exclusiones *firmes* del cálculo 2026, pero los revisores los
   votaron `SI` (se mantienen) en la lista final. **MX Sufragio seguro** coincide
   (fuera en ambos). **Reconciliar lista final vs. config antes de calcular.**
3. **Duplicado CL**: confirmar cuál de las dos filas de "Participación Ciudadana
   Proceso Constitucional" se conserva.
4. "Eliminar" = retirar del conjunto elegible 2026; muchos casos siguen siendo
   reales pero no cumplen criterios (atención ciudadana, sin IA sobre el
   contenido, solo investigación/anuncio).

*Generado por `src/generar_planilla_decisiones.py`.*
