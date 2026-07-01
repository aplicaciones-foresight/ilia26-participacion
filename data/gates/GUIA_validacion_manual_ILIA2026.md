# Guía: validar los casos y pasar al cálculo — ILIA 2026

**Archivo de trabajo:** `planilla_ILIA2026_SIMPLE.xlsx` (6 pestañas · **criterio corregido**).
**Estado:** 34 casos entran/dudosos · 73 excluidos · 107 en total.
Tras el dedup de e-Cidadania → **33 iniciativas efectivas**.

## Las 6 pestañas
1. **Casos (entran+dudosos)** — el set de trabajo, con las columnas listas para calcular y una columna **«Acción sugerida»**.
2. **A validar a mano** — la lista concreta de decisiones por grupo (A excluir · B rescatados→ENTRA · C/D frontera civic-tech · E DUDAs de campo · F reingresos · G dedup).
3. **Excluidos** — los que salen, con su motivo (referencia).
4. **Evidencia y fuentes** — la cita textual por campo crítico + URLs (para verificar que no hay alucinaciones).
5. **Instrucciones** — esta guía dentro del Excel.
6. **Metodología (CENIA v2)** — la metodología final acordada, variable por variable, y qué columna alimenta cada una.

## Pasos manuales (en orden)

### Paso 1 — Confirmar las exclusiones  *(pestaña 2, grupo A)*
**4 casos** ya quedaron **FUERA** (en la pestaña 3) por no ser procesos de participación. Solo confirmar:
- **Voto/servicio:** PE Sistema de cómputo ONPE (conteo electoral) · CO Descongestión Ingreso Solidario (atención/triage de correos).
- **Civic tech:** BR ParticipACT (app de reporte urbano) · CR dIAra (app de fiscalización de obras).

### Paso 2 — Confirmar los rescatados → ENTRA  *(pestaña 2, grupo B)*
**7 casos ENTRAN** (son participación con IA en alguna etapa):
- **MX Presupuesto CRECES** — presupuesto participativo; la IA (chatbot) facilita la votación.
- **CL LXS 400 / Chile Delibera** — mini-público del Senado; la IA modera y administra turnos de palabra.
- **CL Estrategia de Gobierno Digital** — consulta ciudadana; la IA analiza los aportes.
- **HN RedPública** — plataforma de propuestas de ley ciudadanas.
- **CL La voz de los nuevos votantes** y **CL Jornada de Escucha UNAB** — procesos ejecutados por el equipo (confirmados).
- **CO Chatico** — tiene módulos de participación (aportes al Plan de Desarrollo de Bogotá).

### Paso 3 — Casos frontera *(RESUELTOS — no requieren acción)*
Ya decididos con investigación web (ver `casos_frontera_ILIA2026.md`):
- **Entraron:** TT EngageTT (chatbot AskNDTS = apoyo a la implementación) · CO Chatico (módulos de participación) · BR Colab (ideas + voto municipal).
- **Salieron:** DO CiudadanIA (solo servicio) · CO DNP Diálogos (análisis manual, sin NLP) · CR U-Report (encuestas de opinión) · BR ParticipACT y CR dIAra (civic tech).

### Paso 4 — Resolver las DUDAS de campo  *(pestaña 2, grupo E)*
Abrir la URL y confirmar si es participación con IA en alguna etapa → **SI** o **NO**:
- **MX Jalisco «Armemos un Plan»** — el PDF del informe está bloqueado.
- **CO Gaitana IA** — confirmar profundidad real del uso de IA.
- **CL Viña Decide** y **CL Participa Pudahuel** — confirmar con el municipio/Go Vocal si activaron el módulo de IA.

### Paso 5 — Reingresos y dedup  *(pestaña 2, grupos F y G)*
- **F (reingreso):** CL UCampus y CU Código de las Familias — su referencia los reconsidera.
- **G (dedup):** e-Cidadania cuenta como **1**; CL Participación Constitucional (homónimo): **1 SI + 1 NO**.

### Paso 6 — Completar los datos del cálculo  *(pestaña 1)*
Para los casos que quedan en **SI**, revisar que estén completos: **Tipo de proceso · Etapas de uso · Nivel (0-3) · Convocante · Tipo de organización**. Donde `Nº gaps` > 0, abrir la URL de «URLs para verificar» y completar a mano.

### Paso 7 — Validar la evidencia  *(pestaña 4)*
Revisar que cada **campo crítico** tenga cita textual. Las celdas **ámbar** = falta cita → verificar con la fuente antes de darlo por bueno.

### Paso 8 — Calcular el indicador
Con la lista final de iniciativas y sus campos completos, correr el motor: **Sub1 (Uso)** + **Sub2 (Desarrollo)**. Ver `config.yaml` (decisiones abiertas: escenario A/B, cortes de cantidad, redondeo) y `src/calc_engine.py`.

---

## Recordatorio — regla de elegibilidad (CRITERIO CORREGIDO)
Lo **decisivo** es si el caso es **realmente un proceso de participación ciudadana** (consulta, presupuesto participativo, mini-público, referendo/iniciativa popular, gobernanza colaborativa/deliberación) que **usa IA en alguna de las 4 etapas** — **incluida la logística** en Planificación/Implementación (modera, administra turnos, prepara materiales, organiza). **NO se exige que la IA analice el contenido de los aportes.**
**NO ENTRA:** una simple **app de civic tech** que no es un proceso participativo (reporte, servicio, monitoreo), **atención ciudadana**, **voto/conteo electoral por candidatos**, IA como *tema* de la consulta, estudio académico sin despliegue, o **duplicado** de un caso ya contado.

## Qué columna alimenta qué variable (metodología final CENIA v2, jun-2026)
**Sub-indicador de Uso (Sub1)** — promedio simple de 5 variables:
- **Tipos de proceso** (columna «Tipo de proceso») → nº de tipos presentes en el país ÷ 5.
- **Etapas de uso de IA** (columna «Etapas uso IA») → nº de etapas ÷ 4.
- **Continuidad** (columna «Nivel (0-3)») → **nivel máximo del país** ÷ 3.
- **Organización Convocante** (columna «Convocante (7-cat)») → **3 sub-componentes co-iguales**:
  1. *amplitud gubernamental* = nº de tipos gubernamentales distintos ÷ 3 (gobierno local · nacional · otra institución pública),
  2. *amplitud no gubernamental* = nº de tipos no gubernamentales distintos ÷ 4 (empresa · **universidad** · sociedad civil · organización internacional),
  3. *co-convocatoria* = nº de combinaciones de ≥2 tipos que co-convocan, por **máximo relativo móvil** (el país con más combinaciones = 1).
  El valor de la variable = (1 + 2 + 3) / 3.
- **Cantidad de iniciativas** (una fila = una iniciativa; no contar duplicados) → **TODAS las elegibles** del país (sin filtro de nivel), con los cortes 0→0 · 1-3→25 · 4-6→50 · 7-9→75 · 10+→100.

**Sub-indicador de Desarrollo (Sub2, idéntico a 2025):** Tipo de desarrollador (nacional/internacional × 4 tipos, máximo relativo) · Tipos de IA.

> **IMPORTANTE — co-convocatoria:** anotar **todos** los convocantes de cada iniciativa (no solo el principal). Si ≥2 tipos co-convocan, forman una «combinación» que alimenta el tercer sub-componente de Organización Convocante. Las **universidades públicas** cuentan como «Universidad» (no gubernamental), no como «otra institución pública».
