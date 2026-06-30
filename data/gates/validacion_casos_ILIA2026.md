# Validación de los casos incluidos — ILIA 2026 (Participación)

Verificación web (búsqueda + fetch) de los **37 casos elegibles 2026** (24
baseline + 13 nuevos) para (a) descartar **alucinaciones**, y (b) confirmar una
**URL funcional** donde revisar cada caso. Resultados integrados en la hoja
*Validación* y en las columnas de validación de *Detalle consolidado* de
`Planilla_Consolidada_Casos_ILIA2026.xlsx`. Datos: `merge_validacion.py`.

> ⚠️ La ausencia de evidencia de IA en una búsqueda **no prueba** su ausencia.
> Las alertas marcan casos a **confirmar con fuente primaria (cita verbatim)**
> antes de incluirlos, según la regla del proyecto: *mejor `null` + alerta que
> un valor plausible*.

## Resultado global

| Dimensión | Resultado |
|---|---|
| **Existencia del caso** | **31 REAL_CONFIRMADO · 6 PARCIAL · 0 no verificable · 0 contradicho** → ningún caso es una alucinación completa |
| **URL funcional** | **37 / 37 tienen URL operativa** (0 a corregir). Muchas originales daban 403 a bots pero existen; se registró una URL funcional por caso |
| **IA sobre el contenido participativo** | **22 confirmada · 5 parcial/periférica · 10 NO verificada** |

**Conclusión:** no hay casos inventados, y todos tienen dónde revisarse. El
riesgo real no es la existencia del caso sino el **atributo "usa IA sobre el
contenido participativo"**: 10 casos son procesos de participación reales pero
sin evidencia (en esta búsqueda) de que la IA procese el contenido.

## 🔴 IA NO verificada sobre el contenido (10) — riesgo de inclusión indebida

Procesos reales, pero la búsqueda no halló evidencia de IA analizando el
contenido participativo. Bajo la regla metodológica (`rol_IA` debe ser
*contenido*; *apoyo*/sin-IA ⇒ excluido), estos casos podrían reclasificarse y
**salir**. Requieren confirmación con fuente primaria.

| País | Caso | Cat. | Hallazgo de la validación |
|---|---|---|---|
| MX | Presupuesto CRECES | 1 baseline | IA no hallada en el componente participativo; el único "IA" es el chatbot *Hola* de atención ciudadana (baches/multas), no específico de CRECES. |
| CL | Tenemos que hablar de Chile | 1 (Escenario) | La sistematización la hace el Instituto de Argumentación de la U. de Chile con **protocolo manual** de anotación; la relación con "IA" es contenido periodístico *sobre* IA. |
| CR | U-Report Costa Rica | 1 baseline | Chatbot de encuestas sobre **RapidPro (flujos por reglas)**, no IA analizando el contenido. Posible falso positivo por la palabra "chatbot". |
| DO | CiudadanIA | 1 (Escenario) | IA de **atención ciudadana** (asistente de trámites, se solapa con *Taína*); mayormente anuncio/piloto. No analiza contenido deliberativo. |
| CL | Estrategia de Gobierno Digital (2ª consulta) | 1 baseline | La IA es el **tema consultado** y una herramienta futura de atención, no el método de análisis de las respuestas. |
| CL | Jornada de Escucha IPP-UNAB | 1 baseline | Evento real (3 jornadas, 2022), pero ninguna fuente menciona IA/NLP sobre el contenido; la URL original es un dashboard Tableau. |
| BR | Plan Plurianual de Natal | 1 baseline | PPA Participativo real (713 propuestas), pero el procesamiento se describe como **absorción manual**; IA no mencionada. |
| CL | La voz de los nuevos votantes | 1 baseline | Estudio real (encuestas en San Bernardo); metodología = encuestas + mecanismos participativos, sin IA sobre el contenido. |
| CO | Tenemos que hablar de Colombia | 1 baseline | "Análisis de datos como eje transversal" de +374.000 palabras, pero ninguna fuente especifica IA/NLP (podría ser codificación cualitativa). |
| CO | DNP – Diálogos Regionales Vinculantes | 5 **nuevo** | +89.000 propuestas analizadas con "criterios técnicos, financieros y legislativos"; sin mención de IA. Real como participación, no verificado como caso de IA. |

## 🟡 IA parcial / periférica (5) — la IA no actúa sobre el contenido deliberativo

| País | Caso | Hallazgo |
|---|---|---|
| CR | dIAra | IA confirmada, pero sobre **monitoreo físico de obras** (visión por computador); vínculo con participación indirecto (control/transparencia). |
| HN | RedPública + iVerify | La IA confirmada (iVerify) opera sobre **desinformación**, no sobre las propuestas de RedPública. |
| BR | ParticipACT Brasil | ML sobre **crowdsensing/sensores urbanos** (reporte de problemas), no sobre deliberación. |
| CL | LXS 400 – Chile Delibera | IA usada para **muestreo/selección** de la muestra, no como motor de análisis del contenido. |
| TT | EngageTT (Go Vocal) | IA es **capacidad de la plataforma** (resumen/sentimiento); no documentado que se aplicara a esta consulta concreta. |

## 🟢 IA confirmada sobre el contenido (22)

BO Bolivia Conversa · BR Colab · BR e-Cidadania (marcado) · BR e-Cidadania
(matching) · BR Brasil Participativo · BR Cátedra Brasil/Co:Lab USP¹ · BR OPA
Piauí · BR São Paulo Participe Mais · BR 5ª CNCTI · CL Cabildos 2016 · CL Estudio
dIAlogos · CL Proceso Constitucional · CL Un encuentro (equidad/movilidad) · CL
El Chile que Queremos · CO Chatico · CO ECHO–HáblameD · CO Citibeats+PNUD · EC
PAGA IA² · GT Guatemala Joven Conversa · MX Guanajuato Inteligente · PE Consulta
PEN · PA Mansa Idea.

¹ Cátedra Brasil: en etapa de investigación/prototipo (verificar despliegue).
² PAGA IA: corroborado sobre todo por el sitio oficial (conviene fuente externa).

## Notas de URL

- **CL Estudio dIAlogos**: la URL candidata en español de fAIrLAC/BID no se
  confirmó indexada; usar `estudiodialogos.cl` o la ruta `/en/` del mismo
  dominio (ambas vivas).
- El resto de URLs originales que daban 403 son anti-bot (existen); la columna
  *URL funcional (verificada)* trae una alternativa operativa por caso.

## Implicación para el conjunto elegible

Si los 10 casos 🔴 no se confirman con fuente primaria y se reclasifican a
*apoyo*/sin-IA, el conjunto elegible bajo Escenario A bajaría de **37** hacia
**~27** (más los matices de los 5 🟡). **Decisión del operador** antes de cerrar
`config.yaml` / la recodificación.
