# Checklist de verificación manual — ILIA 2026 (Participación)

Qué revisar **a mano** para maximizar inclusión, tras la búsqueda ampliada
(rescate de excluidos/rechazados + descubrimiento de casos nuevos en los 20
países). Regla: la IA debe procesar el **CONTENIDO** participativo
(analizar/clasificar/agrupar/resumir/sentimiento sobre los aportes), no atención
de trámites, no visión de obras, no desinformación, no muestreo.

> Muchos sitios oficiales dan **403 a los bots** pero funcionan en un navegador
> normal — por eso varias verificaciones requieren que **tú** abras el PDF/página.

## Estado del conjunto elegible (Escenario A)
- **25 casos confirmados** (verificación profunda con cita verbatim).
- **+2 rescatables** por confirmar (§A) → hasta **27**.
- **8 candidatos de descubrimiento** (§B), todos *por verificar* — ninguno
  confirmado aún como IA-sobre-contenido desplegada.
- La búsqueda de rescate de los 7 dudosos rechazados dio **0 inclusiones**
  nuevas (§C): todos confirmados fuera con fuente primaria.

---

## 🟢 A. Rescatables — muy probablemente INCLUIBLES si confirmas (2)

### A1 · CL — Plataforma UCampus / Proceso Constitucional 2023
- **Hallazgo:** **Unholster** sistematizó las **1.136 audiencias públicas** con
  **Whisper** (voz→texto) + "modelos de lenguaje natural" (clasificación de temas,
  buscador inteligente). → IA sobre contenido.
- **Abrir a mano:** `secretariadeparticipacion.cl/wp-content/uploads/2023/12/AudienciasPublicas.pdf`
  y `.../2023/10/Informe-SPC-Final.pdf`. Buscar: **"Unholster", "Whisper",
  "modelos de lenguaje natural", "Data Science"**.
- **⚠ Antes de incluir:** confirmar si NO es el mismo proceso ya incluido como
  **"Participación Ciudadana Proceso Constitucional"** (evitar duplicado).

### A2 · CU — Consulta Popular Código de las Familias (GEMA-CEN / Datys)
- **Hallazgo:** GEMA-CEN **agrupó automáticamente las propuestas por similitud** +
  clasificación temática → IA sobre contenido (parcial; clustering/IR clásico).
- **Abrir a mano** (.cu dan 403): `datys.cu/spa/site/product/15` y `.../lines/11`.
  Confirmar en paper: `scielo.sld.cu` / *Rev. Cubana de Ciencias Informáticas* /
  DSpace UCI → `GEMA Datys recuperación de información agrupamiento documentos`.
- **Confirma inclusión si:** un doc técnico describe agrupamiento/clasificación
  automática (TF-IDF, k-means, similitud coseno) sobre el texto de las propuestas.

---

## 🔵 B. Candidatos de descubrimiento — nuevos, POR VERIFICAR (8)

Ninguno confirmado; todos requieren verificar el paso *IA-sobre-contenido*.
Detalle y fuentes en `busqueda_ampliada_2026_resultados.json`.

### B1 · PY — Consultas ciudadanas sobre IA (PNUD AccLab / Atlas IA "AILA") — *prioridad*
- Paraguay hoy es **país vacío**; este es el lead más valioso. Consultas
  (encuestas, grupos focales, entrevistas) en 3 ciudades (2024-25); aportes
  procesados para hallar percepciones/patrones. **Falta** confirmar si el
  análisis usó NLP/ML (tipo Citibeats) o codificación humana.
- **Verificar:** blog PNUD (`undp.org/es/paraguay/blog/consultas-ciudadanas-sobre-ia-en-paraguay...`)
  + PDF *AI Landscape Assessment Paraguay*; contactar AccLab PNUD PY / Innovación MITIC.

### B2 · BR — 3 proyectos UnB sobre Brasil Participativo *(⚠ posible doble conteo)*
Todos aplican IA al contenido de **Brasil Participativo** (plataforma **ya
incluida**), y son repos **académicos** (UnB): verificar despliegue oficial y no
duplicar el caso ya contado.
- **Lumina** (unb-mds/2024-2-Lumina): análisis de sentimiento sobre propuestas
  (con el MDS). ¿Ejercicio académico o adoptado?
- **BP-Classificador** (ResidenciaTICBrisa, UnB-FGA/LAPPIS): clasificación ML/NLP
  para integrarse a la plataforma. ¿Llegó a producción?
- **Participe+** (unb-mds/ParticipeMais): IA generativa que resume/organiza. ¿Va
  más allá de resumir? ¿desplegado?

### B3 · MX — Jalisco "¡Armemos un Plan!" (Plan Estatal 2024-2030)
- Consulta masiva (675K participaciones, **15.899 propuestas** agrupadas en 36
  temas). Jalisco tiene Política de IA. **Falta** confirmar si la agrupación usó IA/NLP.
- **Verificar:** anexo metodológico del PDF del Plan (`plan.jalisco.gob.mx`) →
  buscar "inteligencia artificial / PLN / minería de texto / clustering";
  contactar Secretaría de Planeación y Participación Ciudadana de Jalisco.

### B4 · Leads menores (baja confianza)
- **CO — Atlántico POD 2025-2050 / LITA:** plataforma con IA, pero parece
  geoespacial/técnica, no sobre aportes. Verificar en LITA si procesa texto de
  la participación.
- **UY — Consulta 'Infancia, entornos digitales e IA' (2026):** tiene fase de
  sistematización; verificar (post 10/09/2026) si usa NLP o análisis humano.
- **GT — SEGEPLAN + Red Ciudadana (IA generativa):** ¿sistematiza aportes de los
  Consejos de Desarrollo (COCODES/COMUDES) o es herramienta interna? Verificar en
  `portal.segeplan.gob.gt`.

---

## 🔴 C. Dudosos rechazados — RE-INVESTIGADOS y confirmados FUERA (7)

La segunda búsqueda de rescate **no rescató ninguno**. Qué los reabriría:

| Caso | Por qué quedó fuera | Qué lo reabriría |
|---|---|---|
| CL Senador Virtual (CrowdLaw) | NLP real pero **prototipo** de investigación; no en producción ni en el Repositorio de Algoritmos Públicos | Despliegue/piloto real sobre aportes de Senador/Congreso Virtual |
| CO POT Bogotá (Auditoría) | Estudio académico de **factibilidad/aceptación** (encuesta a 395), sin IA implementada | Prototipo/piloto que procese aportes reales del POT con NLP |
| CO ISIDataInsights (SDP) | **MVP** validado, "será integrada" (prospectivo); vínculo con Chatico temporalmente inconsistente | Evidencia de corrida operativa sobre un corpus real de aportes |
| CO "Pa' que veás" (Cali) | Es un **Monitor de Inversión** (BID MapaInversiones); reportes ciudadanos = a futuro | Módulo que aplique NLP al contenido de las quejas ciudadanas |
| CO iLabs (Ideemos) | IA/ML en la fase de **diagnóstico**, no sobre la deliberación | Caso aplicado con NLP/clustering sobre las transcripciones/aportes |
| CO Asamblea Itinerante (Concejo Bogotá) | Sistematización por **relatorías humanas** | Edición reciente que incorpore IA/NLP sobre los aportes |
| CO Mini-Public Procuraduría | **Sin caso discreto** documentado | La ficha original ILIA (nombre exacto, año, aliado técnico) + IA sobre aportes |

---

## ⚫ D. Verificados FUERA con fuente primaria — baja probabilidad (12)

Cerrados con cita verbatim (hoja *Verificación profunda*). Solo reabrir con la
evidencia indicada: CR dIAra (visión de obras) · CR U-Report (RapidPro reglas) ·
DO CiudadanIA (atención/trámites) · HN RedPública/iVerify (desinformación) ·
BR ParticipACT (crowdsensing) · CL LXS 400 (muestreo) · TT EngageTT (capacidad
no aplicada) · MX CRECES (chatbot de voto) · CL Estrategia Gob. Digital ·
CL La voz de los nuevos votantes · CL Jornada IPP-UNAB · CO DNP Diálogos.
→ En cada uno: cambiaría si aparece IA que analice el CONTENIDO de los aportes.

---

## Orden de acción sugerido
1. **A1 CL UCampus** y **A2 CU GEMA** — confirmar (alta ganancia, +2 → 27).
2. **B1 PY PNUD** — país vacío; alto valor si se confirma NLP.
3. **B5 CO TQH Colombia** (ver recodificación, nota pendiente) — confirmar si usa
   el motor NLP de TQH Chile.
4. **B2/B3** — BR (evitar doble conteo con Brasil Participativo) y MX Jalisco.
5. **B4** — leads menores (CO Atlántico, UY, GT) cuando haya tiempo.

*Datos crudos: `busqueda_ampliada_2026_resultados.json`. Resultados de la
verificación profunda: `verificacion_profunda_resultados.json` + hoja
"Verificación profunda" de la planilla.*
