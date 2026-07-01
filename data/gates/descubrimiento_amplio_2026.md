# Descubrimiento amplio — ILIA 2026 (Participación Ciudadana)

**Fecha:** 2026-07-01 · Barrida amplia posterior a la Fase 2/3 y a la 2ª pasada de DUDA.

Objetivo: buscar **más ampliamente** casos elegibles que se hubieran pasado por
alto, abriendo la aperture a **todos los canales** (portales de gobierno,
licitaciones, premios, proveedores/herramientas, academia, multilaterales,
prensa 2023-2026) en los 20 países, con foco en los **vacíos** (AR, UY, PY, SV,
JM) y en los densos (BR, CO, MX, CL).

## Método

- **8 barridas por país/cluster** + **1 transversal por proveedor/herramienta** +
  **redes especializadas** (People Powered, Democracy R&D, OCDE, LATINNO, Ash
  Center/Stanford). ~150+ búsquedas dirigidas (ES/PT/EN).
- Mismo criterio estricto: IA (NLP/ML/LLM) sobre el **CONTENIDO** de los aportes
  ciudadanos dentro de un proceso participativo; con dedup contra los 51 casos ya
  conocidos y los 44 excluidos 2025.
- **Limitación de entorno:** el proxy de egress bloqueó **WebFetch** a la mayoría
  de dominios (403 de política; ~18+ hosts .gob/.gov/.org). La verificación se
  apoyó en **WebSearch** (snippets con texto citable) + repos accesibles. Las
  fuentes primarias bloqueadas quedan anotadas con su URL para lectura manual.
- Audit trail completo (candidatos evaluados + descartados con cita): `data/_discovery/*.json`.

## Resultado: 4 candidatos NUEVOS (ninguno confirmado SI salvo Pol.is UY)

| País | Caso | Veredicto | Nota |
|---|---|---|---|
| UY | **Pol.is — Referéndum de la LUC** (equipo UdelaR) | 🟢 **SI** (MEDIA) | Clustering ML de opiniones sobre 16.499 participantes/295.000 votos. Fuente primaria (Computational Democracy Project) + OCDE 2025. **Llena a UY** (antes 0). *Caveat temporal: 2021-2022.* |
| CO | **Gaitana IA** (resguardo Zenú) | 🟠 **DUDA (lean SI)** (MEDIA) | LLM DeepSeek resume propuestas/organiza consensos en un presupuesto participativo indígena; cobertura crítica cuestiona si es sustantivo o avatar electoral. |
| CL | **Viña Decide** (PP Viña del Mar, Go Vocal) | 🟠 **DUDA (lean SI)** (BAJA) | Presupuesto participativo sobre Go Vocal/CitizenLab (trae NLP 'Sensemaking'); activación sobre los aportes de Viña no confirmada. |
| CL | **Participa Pudahuel** (PP Pudahuel, Go Vocal) | 🟠 **DUDA (lean NO)** (BAJA) | Igual patrón que Viña/EngageTT: capacidad de plataforma sin confirmación de uso de la IA. |

> Patrón **Go Vocal/CitizenLab** (TT EngageTT + CL Viña + CL Pudahuel): la
> plataforma incorpora NLP de "Sensemaking", pero **no se confirma** que cada
> instancia lo active sobre los aportes. Basta **una** confirmación del
> proveedor/municipio para resolver los tres.

## Descartados relevantes (documentados con cita en `data/_discovery/`)

- **MX — PGD CDMX 2025-2045:** la IA **redactó** el documento del plan (denuncia del 30-45% de texto con IA), **no** analiza los aportes ciudadanos → NO.
- **MX — Foros PND 2025-2030** (53.621 personas, 10.526 propuestas): sistematización temática **manual** → NO.
- **PY — Paraguay 2050** (Decidim, +1.000 propuestas): agrupación por mesas temáticas, **sin evidencia de IA/NLP** → NO (revisar manual: sitio 403).
- **CO — CONPES 4144 Política Nacional de IA** (+1.000 comentarios): **no se pudo confirmar** procesamiento con IA/NLP de los comentarios (doc 403) → no elegible por falta de evidencia.
- **AR — Expresión BA (GCBA):** IA sobre **reseñas de Google**, no aportes de un proceso participativo → NO. **AR — PNUD 'IA Inteligencia Argentina' + Citibeats:** social listening/análisis de discurso → NO.
- **Consultas de estrategia de IA** (UY AGESIC, EC MINTEL, DO ENIA, GT, PA, CL MinCiencia): la IA es el **tema**; los aportes se sistematizan **manualmente** → NO.
- **"Political Watch + Min. de Juventud"** (IA que relaciona propuestas ciudadanas con articulados): es de **ESPAÑA**, fuera de LATAM → descartado (reaparecía en queries LATAM).

## Vacíos confirmados (0 casos elegibles, tras barrida amplia)

**AR, PY, SV, JM, PE** — sin ningún caso nuevo con IA sobre el contenido de
aportes en un proceso participativo. **UY** deja de estar vacío gracias a Pol.is.
El patrón regional persistente: la IA de gobierno se concentra en (a) chatbots de
atención, (b) sistemas de reclamos/incidentes, (c) consultas *sobre* IA con
síntesis manual — todas categorías excluidas.

## Efecto en la planilla

Universo **51 → 55 casos**. Tally tentativo: **SI 33 · NO 17 · DUDA(lean SI) 2 ·
DUDA(lean NO) 3**. Los 4 nuevos están en el bloque **«4. Descubrimiento amplio»**
de `planilla_detalle_casos_ILIA2026.xlsx`, con su evidencia verbatim y gaps.
