# Checklist de verificación manual — ILIA 2026 (Participación)

Qué revisar **a mano** para maximizar inclusión. Ordenado por probabilidad de
que el caso ENTRE. Para cada uno: qué buscar, dónde, y **qué evidencia lo
confirma** (regla: la IA debe procesar el CONTENIDO participativo —
analizar/clasificar/agrupar/resumir/sentimiento sobre los aportes ciudadanos).

> Contexto: muchos sitios oficiales (.gob/.gov/.cl/.cu) dan **403 a los bots**
> pero funcionan en un navegador normal — por eso varias verificaciones
> requieren que **tú abras el PDF/página** y busques los términos indicados.
> Estado actual del conjunto elegible (Escenario A): **25 casos** confirmados;
> lo de abajo puede subirlo.

---

## 🟢 A. Rescatables — muy probablemente INCLUIBLES si confirmas (2)

### A1 · CL — Plataforma UCampus / Proceso Constitucional 2023
- **Hallazgo:** la sistematización de las **1.136 audiencias públicas** la hizo
  **Unholster**: transcripción con **Whisper** (voz→texto) + procesamiento con
  Data Science y **"modelos de lenguaje natural"**, con clasificación automática
  de temas y buscador inteligente. → cumple IA-sobre-contenido.
- **Abrir a mano:** `secretariadeparticipacion.cl/wp-content/uploads/2023/12/AudienciasPublicas.pdf`
  y `.../2023/10/Informe-SPC-Final.pdf`. Buscar en el texto: **"Unholster",
  "Whisper", "modelos de lenguaje natural", "Data Science", "clasificación"**.
- **⚠ Antes de incluir — DESAMBIGUAR duplicado:** confirmar si "UCampus" es el
  MISMO proceso ya incluido como **"Participación Ciudadana Proceso
  Constitucional"** (baseline). Si es el mismo → NO duplicar (ya cuenta). Si
  UCampus es una plataforma/proceso distinto → incorporar.

### A2 · CU — Consulta Popular Código de las Familias (GEMA-CEN / Datys)
- **Hallazgo:** GEMA-CEN hizo **agrupamiento automático de las propuestas por
  similitud** + clasificación temática ("análisis inteligente de expedientes").
  Es procesamiento del contenido (clustering/IR), aunque las categorías las
  definen humanos → IA-sobre-contenido **parcial**.
- **Abrir a mano** (los .cu dan 403 a bots): `datys.cu/spa/site/product/15` y
  `datys.cu/spa/site/lines/11` (Minería de Datos). Buscar **"agrupamiento",
  "clasificación", "clustering", "aprendizaje", "recuperación de información"**.
- **Confirmar en paper:** `scielo.sld.cu` / *Revista Cubana de Ciencias
  Informáticas* / DSpace UCI → query: `GEMA Datys recuperación de información
  agrupamiento documentos` y `clasificación automática textos GEMA Cuba`.
- **Confirma inclusión si:** un documento técnico describe algoritmos de
  agrupamiento/clasificación automática (TF-IDF, k-means, similitud coseno)
  sobre el texto de las propuestas (no reglas manuales).

---

## 🟡 B. Dudosos rechazados — verificación pendiente (agentes cortados por límite de sesión) (7)

> Estos NO alcanzaron a verificarse en profundidad (se agotó el límite de
> sesión). Instrucciones para hacerlo a mano.

### B1 · CO — ISIDataInsights / Reto de Ciudad 'Datos con Historia' (SDP Bogotá)
- **Query:** `ISIDataInsights "Datos con Historia" SDP Bogotá Maloka inteligencia artificial`;
  `ISIDataInsights procesamiento documentos aportes ciudadanos`.
- **Dónde:** sitio de ISIDataInsights (empresa), Secretaría Distrital de
  Planeación (sdp.gov.co), Maloka, notas de prensa del concurso (oct-nov 2024).
- **Confirma inclusión si:** hay evidencia de que la herramienta se **aplicó
  operativamente** a un proceso participativo real analizando aportes ciudadanos
  (no solo ganar el concurso / prototipo).

### B2 · CL — Senador Virtual / CrowdLaw (GobLab UAI + IMFD)
- **Query:** `Senador Virtual NLP GobLab UAI IMFD aportes ciudadanos clasificación`;
  `CrowdLaw Chile inteligencia artificial proyectos de ley participación`.
- **Dónde:** GobLab UAI (goblab.uai.cl), IMFD, Senado (senado.cl), papers.
- **Confirma inclusión si:** el sistema de IA/NLP que analiza los aportes de
  Senador Virtual estuvo **en producción o piloto real** (no solo paper/seminario).

### B3 · CO — IA para participación en el POT de Bogotá (Control Visible/Auditoría)
- **Query:** `POT Bogotá inteligencia artificial aportes ciudadanos Auditoría General 2025 piloto`.
- **Dónde:** Revista de la Auditoría General (jun-2025), Veeduría Distrital.
- **Confirma inclusión si:** fue un **piloto implementado** sobre un proceso
  participativo real (no solo artículo académico / diseño metodológico).

### B4 · CO — 4 mini-públicos excluidos (procesos elegibles, falta IA sobre contenido)
- **"Pa' que veás" (Cali):** ¿la IA analiza el CONTENIDO de las quejas
  ciudadanas con NLP, o solo recopila/predice riesgos técnicos de obras?
  Query: `"Pa que veas" Cali inteligencia artificial análisis quejas ciudadanas`.
- **iLabs – Laboratorios de Inteligencia Colectiva:** ¿la IA procesa los aportes
  deliberativos? Query: `iLabs laboratorios inteligencia colectiva IA deliberación Colombia`.
- **Asamblea Ciudadana Itinerante (Concejo de Bogotá)** y **Mini-Public diálogo
  social (Procuraduría):** Query: `Asamblea Ciudadana Itinerante Concejo Bogotá IA sistematización`
  y `Procuraduría diálogo social minipúblico inteligencia artificial aportes`.
- **Confirma inclusión si:** IA/NLP sobre el contenido de los aportes (no solo
  ser un proceso participativo elegible).

### B5 · CO — Tenemos que hablar de Colombia (LEAD prometedor)
- **Lead:** podría usar el **mismo motor NLP** que "Tenemos que hablar de Chile"
  (Instituto de Argumentación, U. de Chile), que SÍ analiza el contenido. No se
  confirmó en fuente colombiana (el resultado que lo afirmaba citaba una fuente
  chilena — descartado).
- **Abrir a mano:** informe técnico **"Colombia a escala"** (ResearchGate /
  tenemosquehablarcolombia.co/resultados). Query: `"Tenemos que hablar de
  Colombia" informe técnico análisis NLP procesamiento lenguaje natural`.
- **Confirma inclusión si:** una fuente **colombiana** documenta que el análisis
  de las +374.000 palabras usó IA/NLP (no codificación cualitativa manual).
- *(Hoy cuenta como incluido pero marcado "por verificar".)*

### B6 · CO — DNP Diálogos Regionales Vinculantes
- **Verificado:** método = codificación cualitativa manual + estadística
  descriptiva; **sin IA confirmada** (confianza media). La "nota interna" de un
  modelo híbrido NLP **no se corroboró**.
- **Query para reabrir:** `"diálogos regionales vinculantes" DNP NLP OR "procesamiento
  de lenguaje natural" OR "minería de texto" OR "topic modeling"`; buscar tesis /
  proveedores / PDF metodológico en `colaboracion.dnp.gov.co`.
- **Confirma inclusión si:** aparece un documento técnico que describa NLP/ML
  clasificando/estructurando las +89.000 propuestas.

### B7 · VE — Plan de la Patria 7T (IA y Big Data)
- **Verificado:** solo afirmación de **prensa estatal** (Correo del Orinoco),
  sin descripción técnica ni corroboración; sistematización descrita como
  **humana** (33.780 reporteros). **No incluible** con lo hallado.
- **Query para reabrir:** `site:correodelorinoco.gob.ve Plan de la Patria 500 mil
  propuestas inteligencia artificial`; `CNTI OR Cendit OR CENDITEL sistematización
  propuestas Plan Patria algoritmo`.
- **Confirma inclusión si:** un proveedor/académico/doc técnico especifica un
  pipeline de IA/NLP sobre el **texto** de las propuestas.

---

## 🔴 C. Verificados FUERA con fuente primaria — baja probabilidad (12)

Cerrados con cita verbatim (ver hoja *Verificación profunda*). Sólo reabrir si
aparece la evidencia indicada:

| Caso | Por qué salió | Qué lo reabriría |
|---|---|---|
| CR dIAra | Visión por computador sobre imágenes de obras (repo CGR) | IA que analice el CONTENIDO de denuncias/aportes ciudadanos |
| CR U-Report | Chatbot de encuestas RapidPro (reglas/flujos) | NLP/ML clasificando las respuestas abiertas de los jóvenes |
| DO CiudadanIA | Asistente de atención/trámites (recolecta datos) | IA que analice contenido deliberativo/consultivo |
| HN RedPública+iVerify | iVerify = desinformación, aparte de las propuestas | Módulo de IA que analice las propuestas de RedPública |
| BR ParticipACT | ML sobre crowdsensing/sensores urbanos | IA sobre deliberación/opiniones (no sensores) |
| CL LXS 400 | IA solo para muestreo + logística | IA que analice el contenido deliberativo (el "informe de IA") |
| TT EngageTT | IA es capacidad de Go Vocal, no aplicada a la consulta | Doc que muestre Sensemaking aplicado a los aportes de la NDTS |
| MX Presupuesto CRECES | Chatbot 'Hola' = canal de voto/atención | IA que analice/priorice el contenido de las propuestas vecinales |
| CL Estrategia Gob. Digital | IA es el tema; aportes evaluados por criterios humanos | Informe que declare análisis automatizado de los 488 aportes |
| CL La voz de los nuevos votantes | Encuesta de terreno tradicional | Informe que declare NLP/minería sobre las respuestas |
| CL Jornada IPP-UNAB | Evento interno de lanzamiento | Informe que sistematice con IA intervenciones ciudadanas |
| CO DNP Diálogos | (ver B6) | (ver B6) |

---

## 🔎 D. Descubrimiento de casos nuevos — PENDIENTE (agentes cortados por límite)

Los 4 barridos de descubrimiento **no terminaron** (límite de sesión, resetea
~6:20 UTC). Relanzables. Mientras, búsqueda manual sugerida por país:

- **Vacíos (máx. prioridad): AR, UY, PY, SV, JM.** Query por país:
  `"inteligencia artificial" "participación ciudadana" <país> presupuesto participativo OR consulta pública 2024 2025`;
  revisar Decidim (`decidim.org/showcase`), Go Vocal/CitizenLab, PNUD/CEPAL.
- **Densos (posibles subnacionales): BR, CO, CL, MX, PE.**
  `orçamento participativo IA análise propostas` (BR);
  `plan de desarrollo municipal IA sistematización aportes` (CO/CL/MX);
  congresos/municipios + "procesamiento de lenguaje natural".
- **Resto: BO, EC, GT, HN, PA, CR, DO, CU, TT.** Consulta pública/popular +
  IA/NLP; organismos multilaterales por país.
- **Confirma inclusión** de cualquier hallazgo si la IA procesa el contenido de
  los aportes (no atención, no trámites, no visión de obras, no desinformación).

---

### Resumen de acciones (orden sugerido)
1. **A1 CL UCampus** — abrir los 2 PDF + desambiguar duplicado. *(alta ganancia)*
2. **A2 CU GEMA** — abrir Datys + buscar paper UCI. *(alta ganancia)*
3. **B5 CO TQH Colombia** — abrir informe "Colombia a escala". *(ya cuenta; confirmar)*
4. **B1–B4** — ISIDataInsights, Senador Virtual, POT Bogotá, 4 mini-públicos CO.
5. **D** — relanzar descubrimiento (o buscar manual por país) tras el reset del límite.
