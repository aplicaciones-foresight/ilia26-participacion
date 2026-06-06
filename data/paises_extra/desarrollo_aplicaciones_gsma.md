# Desarrollo de aplicaciones (GSMA Mobile Connectivity Index) — ID 76

**Indicador exacto MCI:** "Apps developed per person" = *"Number of active mobile
apps developed per person"* (fuente subyacente: **Appfigures**; enabler *Content
and Services* → dimensión *Local Relevance*, peso ≈20%).

> ⚠️ **Dos límites importantes:**
> 1. El MCI publica **solo el SCORE normalizado 0–100**; el **valor bruto per
>    cápita** (nº de apps) es **propietario de Appfigures, no público**.
> 2. Desde este entorno solo fue accesible (vía espejo GitHub, `curl`) la
>    **edición MCI 2020 (datos 2019)**. Las ediciones 2023/2024/2025 dan 403.
>    → Los valores de abajo son **2019** (no el último). Para ILIA 2026 hay que
>    bajar el 2024/2025 manualmente (ruta abajo).

| País | Score "Apps developed per person" (0–100) | Año | Confianza |
|---|---|---|---|
| España (ES) | **92,13** | 2019 | ALTA (2019) / BAJA (ed. vigente) |
| Estonia (EE) | **94,28** | 2019 | ALTA / BAJA |
| Singapur (SG) | **100,00** (techo de escala) | 2019 | ALTA / BAJA |
| Alemania (DE) | **94,26** | 2019 | ALTA / BAJA |
| Portugal (PT) | **88,61** | 2019 | ALTA / BAJA |

Serie 2014–2019 disponible (p. ej. ES: 86,31→87,17→87,48→89,53→90,89→92,13).

**Fuente (determinística):** espejo oficial GitHub OCTO "Flat Data" del fichero
`MCI_Data_2020.xlsx` de GSMA →
https://raw.githubusercontent.com/githubocto/flat-demo-xlsx/main/mobile-connectivity.csv
(columna "Apps developed per person", filas ISO ESP/EST/SGP/DEU/PRT). Original GSMA:
https://www.mobileconnectivityindex.com/

**Cómo obtener el dato vigente (2024/2025) manualmente:**
- Dashboard: https://www.mobileconnectivityindex.com/ → país → Content and Services → Local Relevance → "Apps developed per person".
- Excel directo (probar en navegador): `https://www.mobileconnectivityindex.com/assets/excelData/MCI_data_2025.xlsx`.
- World Bank Data360, dataset `GSMA_MCI`: https://data360.worldbank.org/ (API `data360api.worldbank.org`, REF_AREA=ESP/EST/SGP/DEU/PRT).
- Metodología 2024/2025 (PDF): https://www.gsma.com/solutions-and-impact/connectivity-for-good/mobile-for-development/wp-content/uploads/2024/06/GSMA-MCI-Methodology-Report-2024.pdf
