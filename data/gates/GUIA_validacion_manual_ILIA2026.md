# Guía: validar los casos y pasar al cálculo — ILIA 2026

**Archivo de trabajo:** `planilla_ILIA2026_SIMPLE.xlsx` (5 pestañas).
**Estado:** 44 casos entran/dudosos · 63 excluidos · 107 en total.
Tras el dedup de e-Cidadania → **43 iniciativas efectivas**.

## Las 5 pestañas
1. **Casos (entran+dudosos)** — el set de trabajo, con las columnas listas para calcular y una columna **«Acción sugerida»**.
2. **A validar a mano** — la lista concreta de decisiones (excluir / resolver DUDA / rescatar / dedup).
3. **Excluidos** — los que salen, con su motivo (referencia).
4. **Evidencia y fuentes** — la cita textual por campo crítico + URLs (para verificar que no hay alucinaciones).
5. **Instrucciones** — esta guía dentro del Excel.

## Pasos manuales (en orden)

### Paso 1 — Excluir los 14 de la verificación profunda  *(pestaña 2, grupo A)*
Su verificación profunda marcó 14 casos como **IA de apoyo** o **sin IA sobre el contenido**. En la pestaña 1 aparecen con **Acción sugerida = ➜ EXCLUIR**. Cambiar su `¿ENTRA?` a **NO**:
BR ParticipACT · CL Estrategia Gob. Digital · CL Jornada UNAB · CL Voz nuevos votantes · CR U-Report · CR dIAra · DO CiudadanIA · HN RedPública · MX Presupuesto CRECES · CO Descongestión · PE Sistema de cómputo ONPE · CL LXS 400 · CO DNP Diálogos · TT EngageTT.

### Paso 2 — Resolver las 4 DUDAS  *(pestaña 2, grupo B)*
Abrir la URL y confirmar si la IA procesa el **contenido** de los aportes → marcar **SI** o **NO**:
- **MX Jalisco «Armemos un Plan»** — el PDF del informe está bloqueado; si revela un pipeline de IA, sube a SI; si no, NO.
- **CO Gaitana IA** — confirmar profundidad real del análisis (cobertura crítica lo cuestiona).
- **CL Viña Decide** y **CL Participa Pudahuel** — confirmar con el municipio/Go Vocal si activaron el módulo de IA (NLP) sobre los aportes.

### Paso 3 — Revisar posibles rescates  *(pestaña 2, grupo C)*
- **CL UCampus** y **CU Código de las Familias** — su referencia los reconsidera. Confirmar si reingresan (SI). *Para CU, mi evidencia (ficha técnica Datys/GEMA = NLP) apoya SI.*

### Paso 4 — Confirmar el dedup  *(pestaña 2, grupo D)*
- **e-Cidadania**: cuenta como **1** (el «matching de ideas» no se suma aparte del «marcado de audiencias»; misma plataforma/convocante).
- **CL Participación Constitucional** (homónimo): **1 SI + 1 NO**.

### Paso 5 — Completar los datos del cálculo  *(pestaña 1)*
Para los casos que quedan en **SI**, revisar que estén completos: **Tipo de proceso · Etapas de uso · Nivel (0-3) · Convocante · Tipo de organización**. Donde `Nº gaps` > 0, abrir la URL de «URLs para verificar» y completar a mano.

### Paso 6 — Validar la evidencia  *(pestaña 4)*
Revisar que cada **campo crítico** tenga cita textual. Las celdas **ámbar** = falta cita → verificar con la fuente antes de darlo por bueno.

### Paso 7 — Calcular el indicador
Con la lista final de iniciativas y sus campos completos, correr el motor: **Sub1 (Uso)** + **Sub2 (Desarrollo)**. Ver `config.yaml` (decisiones abiertas: escenario A/B, cortes de cantidad, redondeo) y `src/calc_engine.py`.

---

## Recordatorio — regla de elegibilidad
**ENTRA** si, dentro de un **proceso participativo**, la IA procesa el **CONTENIDO** de los aportes ciudadanos (recolectar / clasificar / analizar / agrupar por temas / sintetizar). **NO ENTRA**: atención ciudadana, IA como *tema* de la consulta, IA geoespacial/administrativa, logística (turnos), estudio académico sin despliegue, o **duplicado** de un caso ya contado.

## Qué columna alimenta qué variable
- **Sub-indicador de Uso (Sub1):** Tipos de proceso · Etapas de uso · Continuidad/Nivel · Convocante (Público/Privado) · Cantidad de iniciativas.
- **Sub-indicador de Desarrollo (Sub2, idéntico a 2025):** Tipo de desarrollador · Origen · Tipos de IA.
