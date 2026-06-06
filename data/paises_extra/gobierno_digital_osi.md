# Gobierno Digital (Online Service Index, OSI) — ID 92

> ❌ **OSI NO obtenible desde este entorno.** El sub-componente OSI requiere la
> tabla/CSV/PDF de la fuente, y todos los hosts (UN egovkb, World Bank Data360,
> sus CSV, PDFs del Survey, Wikipedia, QoG, Statista) dan **HTTP 403** a WebFetch;
> `curl` solo permite `raw.githubusercontent.com` (sin mirror del dataset). El
> buscador solo devuelve el **EGDI compuesto**, no el OSI.
>
> ✅ Como **dato similar / contexto** sí se confirmó el **EGDI 2024** (del cual el
> OSI es un tercio) con varias fuentes concordantes:

| País | OSI (2024) — headline ILIA | EGDI (2024) — similar/contexto | Rank EGDI | Confianza |
|---|---|---|---|---|
| Estonia (EE) | **NO OBTENIDO** | **0,97274** | #2 | EGDI: ALTA |
| Singapur (SG) | **NO OBTENIDO** | **0,96912** | #3 | EGDI: ALTA |
| Alemania (DE) | **NO OBTENIDO** | ≈0,94 (aprox., 2ª fuente) | ≈#12 | EGDI: MEDIA |
| España (ES) | **NO OBTENIDO** | s/v exacto (clase "Very High") | s/v | BAJA |
| Portugal (PT) | **NO OBTENIDO** | NO OBTENIDO | s/v | BAJA |

⚠️ Un snippet atribuyó "OSI=0,97274" a Estonia: **es el EGDI, no el OSI** — rechazado.

**Cómo obtener el OSI manualmente (rápido):**
- CSV oficial (World Bank Data360, restatement directo UN): `https://data360files.worldbank.org/data360-data/data/UN_EGDI/UN_EGDI_OSI_WIDEF.csv` (filas ISO3 ESP/EST/SGP/DEU/PRT, columna año 2024).
- UN Data Center (interactivo): https://publicadministration.un.org/egovkb/en-us/data-center → año 2024 → exportar columnas OSI/HCI/TII/EGDI/rank.
- Perfiles país UN (incluyen OSI): Estonia /id/57, Singapur /id/154, Alemania /id/65 en https://publicadministration.un.org/egovkb/en-us/Data/Country-Information
- Technical Appendix 2024 (PDF, tabla OSI completa): https://desapublications.un.org/sites/default/files/publications/2024-09/Technical%20Appendix%20(Web%20version)%201292024.pdf

Fuentes EGDI (contexto): Government Transformation https://www.government-transformation.com/en/citizen-experience/uk-rises-and-denmark-leads-in-2024-un-e-government-rankings · ComplexDiscovery (Estonia) https://complexdiscovery.com/estonias-digital-strategy-shines-in-the-2024-un-e-government-report/ · UN press release https://www.un.org/sustainabledevelopment/blog/2024/09/press-release-e-government-survey/
