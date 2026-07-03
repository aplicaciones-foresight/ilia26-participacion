# Análisis profundo de los casos que entran — ILIA 2026

*Revisión detallada de los 35 casos SÍ en tres niveles: (1) existencia, (2) corrección de
todos los datos, (3) interpretación bajo el criterio de elegibilidad. Análisis de contenido
realizado por el modelo principal; verificación factual web en paralelo con 3 agentes
(desarrolladores, convocantes, despliegue real, herramientas). Las URLs de método
citadas quedaron en las notas de verificación de cada ficha.*

## Resultado global

| Nivel | Resultado |
|---|---|
| **Existencia** | **35/35 existen** (ya verificados en la pasada anti-alucinaciones; esta pasada re-confirmó los hechos centrales de 20 casos con fuentes primarias). |
| **Corrección de datos** | **15 correcciones de campo aplicadas en 13 fichas** + 7 confirmaciones documentadas (ver §3). Todas con cita y URL en `notas_verificacion`. |
| **Interpretación** | 30/35 bien interpretados. **5 casos cuestionados** con evidencia (ver §2) — la decisión de excluirlos es del equipo. |

---

## §1 Veredicto caso por caso (35)

**✓ = existe, datos correctos (tras correcciones), bien interpretado.**

| # | Caso | Veredicto | Observación |
|---|---|---|---|
| 1 | BO Bolivia Conversa | ✓ (corregido) | Herramienta = **Remesh** (empresa EE.UU.), adoptada por ONU → desarrollador Gobierno→Privado. |
| 2 | BR 5ª CNCTI | ✓ (corregido) | Transcripción+síntesis confirmadas (TDS Company) → tipos_IA completado [Voz a Texto, NLP]. LLM: no confirmado. |
| 3 | BR Brasil Participativo (clustering) | ⚠ **cuestionado** | Investigación sobre 10.186 propuestas reales, en alianza con la Secretaria, PERO el README admite que la plataforma "não possui… processamento de linguagem natural" → **producción NO confirmada**. |
| 4 | BR Colab | ✓ (nota) | Brasileña (Recife 2013) confirmada. IA descrita de forma vaga ("optimizar análisis"); entra por decisión del equipo (módulos de ideas+voto). |
| 5 | BR Cátedra/Co:Lab USP | ⚠ **cuestionado fuerte** | "Pesquisas em andamento": revisión + entrevistas, **sin piloto con ciudadanos**. El criterio excluye estudios sin despliegue. |
| 6 | BR OPA Piauí | ⚠ **cuestionado** | La única IA explícita es **seguridad de conexiones** (CloudFront); la análise de propuestas la hacen "equipes técnicas" humanas. El "40%" es métrica operativa. Origen corregido Internacional→Nacional (Colab es brasileña). |
| 7 | BR PPA Natal | ✓ | Chatbot WhatsApp del PPA 2026-2029, verificado. |
| 8 | BR e-Cidadania (marcado audiencias) | ✓ | Verificado (Senado, mar-2025). |
| 9 | BR São Paulo Programa de Metas (Gemini) | ⚠ **cuestionado fuerte** | La sistematización oficial la hizo **SEPEP/SGM sin IA**; la herramienta Gemini se presentó en **oficinas formativas** (nov/dic-2025) meses después del cierre de la consulta (may-2025); paneles oficiales alimentados: no confirmado. Órgano y fechas corregidos en la ficha. |
| 10 | BR e-Cidadania (matching ideas) | ✓ | Verificado (Senado, ene-2026). Cuenta como 1 con el #8 (dedup). |
| 11 | CL Cabildos 2016 | ✓ (corregido ×2) | Convocó el **Gobierno de Chile** (Bachelet/SEGPRES), no la BCN (que archiva) → convocante corregido. Estado activo→cerrado. |
| 12 | CL El Chile que Queremos | ✓ | Repo público MinCiencia/ECQQ (RNN, Random Forest, LDA, emociones) — el caso mejor documentado técnicamente. |
| 13 | CL Estrategia Gobierno Digital | ✓ | Datos delgados ("probablemente NLP"): confirmar técnica con el informe (instrucción en planilla). |
| 14 | CL Estudio dIAlogos | ✓ (corregido) | **Merlin Research es chilena** (RUT 76151274-9) → origen Internacional→Nacional. |
| 15 | CL Jornada UNAB | ✓ | Ejecutado por el equipo; fuente pública débil (anotado). |
| 16 | CL LXS 400 | ✓ | Moderador automatizado Stanford = apoyo logístico en implementación — encaja exactamente en el criterio corregido. Co-convocatoria de 3 tipos capturada. |
| 17 | CL La voz de los nuevos votantes | ✓ | Ejecutado por el equipo. |
| 18 | CL Participación Constitucional | ✓ (corregido) | El análisis fue del **IMFD (U. Chile) + PUC** → desarrollador Privado→Academia. |
| 19 | CL Tenemos que hablar de Chile | ✓ | Consistente (UC+UCH, NLP tópicos). |
| 20 | CL Encuentro equidad de género | ✓ | Consistente (IPP-UNAB). |
| 21 | CO Chatico | ✓ (corregido) | Participación verificada: PP + Causas Ciudadanas + **147.000 aportes al Plan de Desarrollo**; renovado con IA generativa 2026. tipo_proceso: Referendos→Participación Digital (las causas no son referendos). |
| 22 | CO Citibeats+PNUD | ⚠ **cuestionado fuerte** | Es **escucha social** de redes (Twitter/Facebook) en el paro 2021 — no hay proceso participativo convocado. Misma lógica con la que se excluyó U-Report. |
| 23 | CO ECHO–HáblameD | ✓ (confirmado) | Desarrollada por el lab de innovación de **UNFPA Colombia** (cita verbatim) → desarrollador Gobierno(org.int.) correcto. |
| 24 | CO Gaitana IA | ✓ | Entra por decisión del equipo (LLM construye consensos). Confianza media: validar alcance técnico (instrucción en planilla). |
| 25 | CO Tenemos que hablar de Colombia | ✓ (corregido) | El análisis lo lideraron las **universidades** (EAFIT/DataPOL); FIP/SURA fueron apoyo → desarrollador Sociedad Civil→Academia. |
| 26 | CU Código de las Familias | ✓ | GEMA-CEN verificado (agrupamiento por similitud). Flag menor: 'Gobierno' como tercer desarrollador es débil (el CEN usó, no desarrolló). |
| 27 | EC PAGA IA | ✓ (confirmado) | Fundapi = ONG ecuatoriana; desarrollo conjunto con Gobierno Abierto. |
| 28 | GT Joven Conversa | ✓ (corregido ×3) | Herramienta = **Remesh** (cita verbatim DPPA) → desarrollador Gobierno→Privado; +etapa Análisis; se eliminó una cláusula contaminada de otro caso (dIAra). |
| 29 | HN RedPública+iVerify | ✓ | Flag menor: tipo_org 'Público' para PNUD+universidades es discutible (¿Mixto?). |
| 30 | MX Guanajuato InteliGENTE | ✓ | Gaps de técnica anotados (IA no especificada por nombre). |
| 31 | MX Presupuesto CRECES | ✓ (corregido) | Typo en sistema_IA arreglado. Chatbot facilita votación = apoyo en implementación (criterio corregido). |
| 32 | PA Mansa Idea | ✓ | "Basada en IA" sin técnica confirmada → tipos_IA se deja vacío (honesto) y resta en Sub-Desarrollo; validar con la fundación. |
| 33 | PE Consulta PEN | ✓ | Rótulo (¿PEN 2036?) pendiente de confirmar (nota previa). |
| 34 | TT EngageTT | ✓ (alineado) | Campos alineados con la decisión del equipo: etapas=[Implementación], rol=apoyo, usa_IA=sí; tipos_IA limitado al chatbot confirmado (Sensemaking queda como planeado y no cuenta en Sub-Desarrollo). |
| 35 | UY Pol.is LUC | ✓ (corregido) | Pol.is lo desarrolla **Computational Democracy Project** (EE.UU.); UdelaR operó la instancia → desarrollador queda [Sociedad Civil]. |

---

## §2 Los 5 casos cuestionados (decisión del equipo)

La verificación web independiente respalda **NO** en tres casos que el equipo había marcado SI
(en los tres, la ficha ya traía divergencia equipo-vs-evidencia), y deja otros dos en zona gris:

| Caso | Evidencia central | Mi recomendación |
|---|---|---|
| **BR Cátedra/Co:Lab USP** | "Pesquisas em andamento"; el investigador habla en futuro ("o que precisa ser desenvolvido é o treinamento dos modelos"); el paper es revisión+entrevistas. Sin despliegue con ciudadanos. | **Excluir** (estudio sin despliegue). |
| **BR São Paulo (Gemini)** | Sistematización oficial por SEPEP/SGM **sin IA**; la herramienta se mostró en talleres formativos meses después del cierre; paneles no confirmados. | **Excluir** (ejercicio formativo externo, no parte del proceso). |
| **CO Citibeats+PNUD** | Monitoreo de redes sociales abiertas durante el paro 2021; no hay convocatoria ni proceso estructurado. | **Excluir** (escucha social = misma regla que U-Report). |
| **BR OPA Piauí** | Proceso participativo real y consolidado (4ª edición), pero la única IA explícita es seguridad/infraestructura; el análisis de propuestas es humano. | **Excluir o DUDA** — entra solo si aceptan "IA de infraestructura del proceso" como apoyo, que a mi juicio estira el criterio. |
| **BR Brasil Participativo (clustering)** | La IA procesó 10.186 propuestas reales en alianza con la Secretaria, con miras a integrarse; pero la plataforma hoy **no tiene NLP en producción**. | **Mantener con nota o DUDA** — es el gris genuino: contenido real procesado, despliegue no confirmado. Reevaluar en 2027. |

### Impacto en el índice (preliminar, datos corregidos; prom. regional actual = 26)

| Escenario | n | Prom. regional | BR | CO |
|---|:--:|:--:|:--:|:--:|
| Actual (34 iniciativas) | 34 | **26** | 82 | 78 |
| A: salen Cátedra + SP-Gemini + Citibeats | 31 | 25 | 72 | 63 |
| B: A + OPA Piauí | 30 | 25 | 66 | 63 |
| C: B + BP-clustering (máximo rigor) | 29 | 24 | 54 | 63 |

*(BR es el más sensible: pasa de 8 a 4-7 iniciativas según el escenario; CO pierde su único caso de 'Participación Digital' pura y un convocante internacional si sale Citibeats.)*

---

## §3 Correcciones aplicadas (15, todas con cita+URL en la ficha)

| Ficha | Cambio |
|---|---|
| BO Bolivia Conversa | desarrollador Gobierno→**Privado** (Remesh); sistema_IA precisado. |
| GT Joven Conversa | desarrollador Gobierno→**Privado** (Remesh); **+etapa Análisis**; eliminada cláusula contaminada (era de dIAra). |
| CL Cabildos 2016 | convocante otra inst. pública→**gobierno nacional**; estado activo→**cerrado**; organización aclarada. |
| CL Estudio dIAlogos | origen Internacional→**Nacional** (Merlin Research es chilena). |
| CL Participación Constitucional | desarrollador Privado→**Academia** (IMFD+PUC). |
| CO Tenemos que hablar de Colombia | desarrollador Sociedad Civil→**Academia** (EAFIT/DataPOL). |
| CO Chatico | tipo_proceso Referendos→**Participación Digital**; descripción enriquecida con la participación verificada. |
| UY Pol.is LUC | desarrollador [Sociedad Civil, Academia]→**[Sociedad Civil]** (UdelaR operó, no desarrolló). |
| BR 5ª CNCTI | tipos_IA vacío→**[Voz a Texto, NLP]** (funcionalidad confirmada). |
| BR OPA Piauí | origen Internacional→**Nacional** (Colab es brasileña); advertencia sobre el "40%". |
| BR São Paulo (Gemini) | órgano corregido (**SEPEP/SGM**); fechas aclaradas; advertencia paneles. |
| MX CRECES | typo sistema_IA ("WhatsA´´"→WhatsApp). |
| TT EngageTT | alineación con decisión del equipo (etapas/rol/uso/tipos). |

**Confirmados sin cambio (con nota):** CO ECHO (desarrolló UNFPA), EC PAGA IA (Fundapi ONG),
BR Colab (brasileña), BR BP-clustering (producción no confirmada), CU (GEMA), CL casos UNAB (equipo).

## §4 Flags menores (no bloquean; quedan en «qué validar»)
- CU: 'Gobierno' como tercer desarrollador es débil (CEN usó, no desarrolló GEMA).
- HN: tipo_org 'Público' para PNUD+universidades — revisar (¿Mixto?).
- PA Mansa Idea: técnica de IA sin confirmar → tipos_IA vacío resta en Sub-Desarrollo.
- PE: confirmar rótulo exacto (PEN 2036).
- CL Estrategia Gob. Digital: técnica "probablemente NLP" — confirmar con el informe.
