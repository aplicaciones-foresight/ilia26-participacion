# ILIA 2026 — Recolección de indicadores para 5 países extra

**Países:** España (ES) · Estonia (EE) · Singapur (SG) · Alemania (DE) · Portugal (PT)
**Fecha:** 2026-06-06 · **Origen de definiciones:** `Subindicadores_ILIA_2026_v_11.05.26.xlsx`, hoja *"Descripción y seguimiento subin"*.

> **Método y garantía anti-alucinación.** Cada cifra se obtuvo por una de tres vías,
> declarada en cada caso: (a) **determinística** — descarga del dato crudo y cálculo
> con script; (b) **búsqueda + doble validación** — ≥2 fuentes independientes; (c)
> **verificación red-team** — un 2º agente independiente reconfirmó/― refutó las
> cifras de búsqueda. Donde un dato **no se pudo obtener** desde este entorno, se
> dice explícitamente (`NO ENCONTRADO` / `NO ACCESIBLE`) y se entrega la **ruta de
> extracción manual**. Ningún número proviene de memoria.

## Decisiones aplicadas (confirmadas por el operador)
1. **Gobierno digital** → ID 92 = **Online Service Index (OSI)** del UN E-Gov Survey 2024.
2. **Patentes** → fuente **OECD.AI** (curada).
3. **Desarrollo de IA** → **nº de modelos por país en Hugging Face** (vía organizaciones).
4. **Año de referencia** → **último disponible**, documentado. Valor **bruto** siempre;
   versión per cápita donde el índice normaliza.

## ⚠️ Restricción de acceso de este entorno (clave para leer la tabla)
La red del sandbox solo permite: **WebSearch** (snippets) y **`curl`/WebFetch a
`raw.githubusercontent.com` y `storage.googleapis.com`**. **WebFetch da HTTP 403 en
casi todo** (dashboards, APIs de datos, PDFs, incluso Wikipedia). Por eso:
- Lo que vive en **GitHub/datos crudos** se obtuvo **determinísticamente** (GitHub
  Innovation Graph; espejo del GSMA MCI; población World Bank).
- Lo que vive en **dashboards dinámicos** (ETO CAT, OECD.AI, cat.eto.tech, UN egovkb,
  Hugging Face, Zenodo, OWID) **no fue alcanzable** → se entrega ruta manual.

---

## TABLA MAESTRA

| # | Indicador (ID) | ES | EE | SG | DE | PT | Año | Fuente | Estado / confianza |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Empresas de IA (70) | — | — | — | — | — | última década | ETO CAT | ❌ No accesible · ruta manual |
| 2 | Nº inversiones privadas (71) | — | — | — | — | — | última década | ETO CAT (Crunchbase) | ❌ No accesible · ruta manual |
| 3 | Valor total est. inversión priv. (72) | — | — | — | — | — | última década | ETO CAT (Crunchbase) | ❌ No accesible · ruta manual |
| 4 | **Gasto I+D / PIB %** (73) | **1,50** | **1,84**¹ | **1,85**² | **3,17** | **1,73**³ | 2024 (SG 2022) | Nac./Eurostat/OCDE + WB | ✅ Verificado · ALTA |
| 5 | Desarrollo de aplicaciones (76) | **89,30** | **96,73** | **100,00** | **94,75** | **86,24** | **2024** | GSMA MCI 2025 (score 0–100) | ✅ Archivo oficial · ALTA |
| 6 | **Relevancia prod. software** (80) — *total · 2025* | 0,03189 · 0,00788 | 0,03571 · 0,00655 | 0,02589 · 0,00822 | 0,08960 · 0,01899 | 0,03280 · 0,00768 | 2020Q1–2025Q4 / 2025 | GitHub Innovation Graph | ✅ Determinístico · ALTA |
| 7 | Desarrollo de IA — modelos HF (81) | n/d | n/d | n/d | n/d | n/d | — | Hugging Face | ❌ Conteos no accesibles · inventario de orgs listo |
| 8 | Familias de patentes IA (82) | — | — | SG 661/297⁵ | DE ~436⚠️ | — | 2017-20 / ambiguo | OECD.AI/CSET | ⚠️ Parcial · BAJA-MEDIA |
| 9 | Aplicantes de patentes IA (83) | — | — | — | — | — | — | (no en OECD.AI) | ❌ No publicado · requiere EPO/Lens |
| 10 | Inventores de patentes IA (84) | — | — | — | — | — | — | (no en OECD.AI) | ❌ No publicado · requiere EPO/Lens |
| 11 | Gobierno digital — OSI (92) | — | — | — | — | — | 2024 | UN E-Gov Survey | ❌ OSI no accesible · EGDI como similar⁶ |

¹ Estonia: 1,84% (2023, sólido); ~2,0% (2024, provisional). · ² Singapur: 1,85% (2022); el WB da 2,16% pero es 2020. · ³ Portugal: ~1,73% (OCDE/CEIC) / 1,75% (DGEEC nacional), 2024. · ⁴ GSMA: dato 2024 del archivo oficial MCI 2025 (Index Scores); scores re-normalizados entre ediciones → no comparar con ediciones previas. · ⁵ Singapur: 661 solicitudes / 297 concedidas (ventana 2017-2020). · ⁶ EGDI 2024 verificado: Estonia 0,97274 (#2), Singapur 0,96912 (#3).

**Leyenda:** ✅ entregado · ⚠️ parcial/con reserva · ❌ no accesible desde el entorno (dato existe; ruta manual provista) · — sin valor · n/d sin conteo.

---

## DETALLE POR INDICADOR

### 4 ✅ Gasto en I+D como % del PIB (ID 73) — `gasto_id_pib.md`
- **Definición ILIA:** proporción del gasto en I+D respecto al PIB.
- **Valores (último disponible):** ES **1,50%** (2024) · EE **1,84%** (2023; ~2,0% 2024 prov.) · SG **1,85%** (2022) · DE **3,17%** (2024) · PT **~1,73–1,75%** (2024).
- **Método:** la fuente ILIA (CEPAL) no cubre estos países → oficinas nacionales (INE, Statistics Estonia, Destatis, DGEEC), Eurostat y OCDE, con World Bank `GB.XPD.RSDV.GD.ZS` como contraste. Doble fuente por país.
- **Validación independiente (red-team):** CONFIRMA todos. Correcciones: PT converge en ~1,73% (OCDE/CEIC); SG 1,85% es 2022 (no confundir con WB 2020 = 2,16%).
- **Confianza:** ALTA (ES, EE-2023, DE); MEDIA-ALTA (PT, EE-2024); MEDIA (SG).
- **Per cápita:** N/A (ya es un ratio sobre PIB).

### 5 ✅ Desarrollo de aplicaciones (ID 76) — `desarrollo_aplicaciones_gsma.md`
- **Definición ILIA:** nº de apps desarrolladas localmente, per cápita (GSMA Mobile Connectivity Index).
- **Indicador exacto MCI:** **"Locally developed apps per person"** (enabler *Content and Services* → dimensión *Local Relevance*; fuente Appfigures). El MCI publica **solo el score 0–100**; el bruto per cápita es propietario (no público).
- **Valores (score 0–100, 2024):** ES **89,30** · EE **96,73** · SG **100,00** · DE **94,75** · PT **86,24**.
- **Método:** lectura directa del archivo oficial **`MCI_data_2025.xlsx`** (hoja *Index Scores*, col. "Locally developed apps per person", Year = 2024), provisto por el operador.
- **Reserva:** los scores se re-normalizan entre ediciones → no comparar con ediciones previas. SG saturado en 100.
- **Confianza:** ALTA.

### 6 ✅ Relevancia de Producción de Software (ID 80) — `github_relevancia_sw.py`, `relevancia_sw_resultados.csv`
- **Definición ILIA:** proporción entre el total de *inbounds recibidos* y el total de repositorios por país en GitHub.
- **Dos versiones** (por ventana de inbounds; denominador común = **repos acumulado total** = suma de los 24 trimestres 2020 Q1–2025 Q4, según metodología ILIA):

  | País | repos acum. (24 trim.) | inbounds TOTAL | **REL total** | inbounds 2025 | **REL 2025** |
  |---|---|---|---|---|---|
  | ES | 87.092.474 | 2.777.625 | **0,03189** | 686.582 | **0,00788** |
  | EE | 6.156.090 | 219.851 | **0,03571** | 40.306 | **0,00655** |
  | SG | 79.025.220 | 2.045.930 | **0,02589** | 649.800 | **0,00822** |
  | DE | 153.809.309 | 13.781.473 | **0,08960** | 2.920.604 | **0,01899** |
  | PT | 22.260.641 | 730.046 | **0,03280** | 170.886 | **0,00768** |

  - **Versión total:** inbounds acumulados de toda la serie (24 trimestres) ÷ repos acumulado total.
  - **Versión 2025:** inbounds solo de 2025 ÷ repos acumulado total (mismo denominador).
  - **Singapur sin agregado "EU"** (único afectado): REL total **0,02358**, REL 2025 **0,00757**.
  - *Alternativa* (2025 inbounds ÷ repos acumulado de 2025, ventanas pareadas): ES 0,03083 · EE 0,02609 · SG 0,02627 · DE 0,07762 · PT 0,02944. Disponible en el CSV (`relevancia_2025_repos2025`) por si prefieres parear ventanas.
- **Método (determinístico):** descarga de `repositories.csv` y `economy_collaborators.csv` del GitHub Innovation Graph (CC0). El datasheet define collaborators como *git pushes + PRs de un dev [source] a un repo de [destination]* → **inbound recibido = Σ weight con destination = país**. Sin auto-bucles. Script `github_relevancia_sw.py` reproduce ambas versiones; CSV con todos los componentes.
- **Denominador:** **repos acumulado total** = Σ de los conteos trimestrales de repos (2020 Q1–2025 Q4), conforme tu metodología.
- **Confianza:** ALTA (dato crudo oficial).

### 1–3 ❌ Empresas de IA / Nº inversiones / Valor inversión (IDs 70-72) — `empresas_inversion_eto.md`
- **Estado:** **NO ACCESIBLE** desde el entorno. Los números por país de ETO CAT se sirven dinámicamente (Cloud Function `cat-collab-eto`) y el dataset está en Zenodo (`cat.zip`); ninguno entra en el allowlist de `curl` y WebFetch da 403.
- **Confirmado (alta confianza):** definiciones exactas (CAT "Companies", "Number of investments received", "Investment received (estimated total value in millions USD)") y ventana **"última década"** (build 11-dic-2025; fuente Crunchbase/CSET).
- **Ruta manual (30 s/país):** `https://cat.eto.tech/?dataset=Investment&countries=Spain` → panel *Summary metrics*. O API: `curl "https://us-east1-gcp-cset-projects.cloudfunctions.net/cat-collab-eto?dataset=Investment&countries=Spain"`. O Zenodo `https://zenodo.org/records/19103157` (`cat.zip`).
- **Per cápita:** cuando obtengas los conteos, usar `poblacion_total_worldbank.csv` (2024): ES 48.848.840 · EE 1.372.341 · SG 6.036.860 · DE 83.516.593 · PT 10.694.681.

### 8–10 ⚠️/❌ Patentes de IA (IDs 82-84) — `patentes_ia_oecdai.md`
- **Hallazgo clave:** OECD.AI/CSET **solo publica FAMILIAS** (nivel familia, país de primera presentación). **Aplicantes** e **Inventores por país NO existen** en esa fuente → requieren EPO PATSTAT / OECD STI / Lens / Espacenet (cambio de fuente y de base de conteo). Esto concuerda con que la planilla apuntaba a Espacenet para estos 3.
- **Familias (lo poco obtenible):** SG **661 solicitudes / 297 concedidas** (2017-2020, CSET — verificado literal); DE **~436** (⚠️ **frágil**: linaje CSET/WIPO vía AI Index 2024, métrica/año ambiguos — probable acumulado de familias, no "2024"). ES/EE/PT **NO ENCONTRADO** (ES solo: < 57).
- **Ruta manual:** familias actuales en `https://cat.eto.tech/?dataset=Patent&expanded=Summary-metrics` u OWID `artificial-intelligence-patents-submitted.csv`. Aplicantes/inventores en Lens.org o Espacenet (consulta CPC G06N + keywords, facetar por país del solicitante / del inventor).

### 7 ❌ Desarrollo de IA — Hugging Face (ID 81) — `desarrollo_ia_hf_orgs.md`
- **Estado:** conteos de modelos **NO ACCESIBLES** (HF da 403 en API, páginas y proxy; WebSearch no expone el contador "Models" de forma fiable). El agente **descartó** cifras de snippets no corroboradas (anti-alucinación).
- **Entregado:** inventario verificado de organizaciones nacionales en HF por país (el "denominador"): ES (BSC-LT, HPAI-BSC, PlanTL-GOB-ES, projecte-aina, HiTZ, clibrain…), EE (tartuNLP), SG (aisingapore, Sea AI Lab, NUS), DE (laion, Aleph-Alpha, DFKI, deepset, LeoLM, occiglot*), PT (PORTULAN). *occiglot es multinacional.
- **Ruta manual:** por cada org, `https://huggingface.co/api/models?author=<ORG>&limit=1000` y contar; sumar por país; congelar lista + fecha.

### 11 ❌ Gobierno digital — OSI (ID 92) — `gobierno_digital_osi.md`
- **Estado:** **OSI no accesible** (solo en el Technical Appendix PDF / data center / CSV de World Bank Data360, todos 403). Verificado por 2 agentes: el OSI no aparece en snippets; **no confundir con EGDI**.
- **Dato similar entregado (EGDI 2024, verificado):** Estonia **0,97274** (#2), Singapur **0,96912** (#3); Alemania ≈0,94 (#≈12, aprox.); España clase "Very High"; Portugal sin cifra.
- **Ruta manual (OSI):** CSV World Bank Data360 `UN_EGDI_OSI_WIDEF.csv`, o el UN Data Center (año 2024), o el Technical Appendix 2024 (PDF, tabla OSI por país).

---

## RESUMEN ACCIONABLE — lo que necesita extracción manual
Por el bloqueo de red del entorno, estos datos **existen** pero debes sacarlos tú
(rutas exactas en cada archivo): **(1) Empresas de IA, (2) Nº inversiones, (3) Valor
inversión** → cat.eto.tech (30 s/país); **(8) Familias de patentes** → cat.eto.tech;
**(9-10) Aplicantes/Inventores** → Lens/Espacenet (cambio de fuente); **(7) modelos
HF** → API de HF con la lista de orgs provista; **(11) OSI** → CSV World Bank Data360
o Technical Appendix UN. Entregados y verificados: **(4) Gasto I+D/PIB**, **(5)
Desarrollo de apps** (2024, archivo oficial MCI 2025) y **(6) Relevancia de software**.

## Archivos de esta entrega
- `REPORTE_INDICADORES_5_PAISES.md` (este) · `gasto_id_pib.md` · `desarrollo_aplicaciones_gsma.md`
- `github_relevancia_sw.py` + `relevancia_sw_resultados.csv` · `patentes_ia_oecdai.md`
- `empresas_inversion_eto.md` · `desarrollo_ia_hf_orgs.md` · `gobierno_digital_osi.md`
- `poblacion_total_worldbank.csv` (para per cápita)
