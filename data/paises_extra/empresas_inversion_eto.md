# Empresas de IA · Nº inversiones privadas · Valor inversión — IDs 70, 71, 72

> ❌ **Valores NO alcanzables desde este entorno.** Los 3 indicadores viven en ETO
> CAT, cuyos números por país se sirven dinámicamente desde una Cloud Function
> (`us-east1-gcp-cset-projects.cloudfunctions.net/cat-collab-eto`) y el dataset
> está en Zenodo (`cat.zip`). Ninguno es alcanzable: WebFetch da 403 en todo;
> `curl` solo permite `raw.githubusercontent.com` y `storage.googleapis.com` (el
> bucket GCS aloja la app pero **no** los datos por país; son dinámicos). Confirmado
> con ingeniería inversa de la app. **Valor = NO ENCONTRADO para los 5 países.**

## Definiciones EXACTAS confirmadas (alta confianza) + ventana temporal
Ventana = **"over the past decade"** (rolling ~10 años). Build actual: **11-dic-2025**;
dataset ETO/CSET "Country AI Activity Metrics" (Zenodo rec. 19103157, 2026). Fuente
subyacente: **Crunchbase** procesado por CSET/ETO.

| ILIA | Métrica exacta en CAT (dataset *Investment*) | Definición |
|---|---|---|
| (1) Empresas de IA | **"Companies"** | nº de empresas de IA del país (Crunchbase+CSET), última década |
| (2) Nº inversiones privadas | **"Number of investments received"** | nº de rondas VC + private equity + M&A con empresas objetivo del país, última década (solo equity) |
| (3) Valor total estimado inversión | **"Investment received (estimated total value in millions USD)"** | valor total **estimado** (incluye modelado de transacciones sin monto público). ⚠️ NO usar la variante "disclosed value" |

## Valores
| País | (1) Empresas IA | (2) Nº inversiones | (3) Valor estimado (M USD) |
|---|---|---|---|
| España, Estonia, Singapur, Alemania, Portugal | NO ENCONTRADO | NO ENCONTRADO | NO ENCONTRADO |

Contexto (cross-check, NO es el dato CAT, distinta ventana/base): Stanford HAI AI
Index cita financiación privada acumulada de IA de Alemania ≈ US$17,2 mil M (desde
2013) y Reino Unido ≈ US$34,1 mil M.

## Cómo obtenerlo manualmente (rápido)
1. **Navegador (30 s/país):** https://cat.eto.tech/?dataset=Investment&countries=Spain
   (repetir con Estonia, Singapore, Germany, Portugal) → panel **Summary metrics** →
   leer "Companies", "Number of investments received", "Investment received
   (estimated total value in millions USD)". Anotar el rango de años que muestre.
2. **API (1 llamada/país, desde red abierta):**
   `curl "https://us-east1-gcp-cset-projects.cloudfunctions.net/cat-collab-eto?dataset=Investment&countries=Spain"`
   (el JSON `result` trae las summary metrics).
3. **Fichero plano (los 5 de una vez):** https://zenodo.org/records/19103157 → `cat.zip`
   → CSVs de companies/investment, filtrar por país.
4. **Cross-check valor (3):** OWID https://ourworldindata.org/grapher/private-investment-in-artificial-intelligence-cset (CSV, `estimated_investment`, USD constantes 2021).

## Alternativa accesible por GitHub (proxy, NO equivalente)
`georgetown-cset/parat` (PARAT, ~1.311 empresas curadas) tiene datos por empresa en
GitHub (`curl`-able). Permitiría contar empresas por país, pero es un **universo
distinto y mucho menor** que el "Companies" de CAT (Crunchbase) → no comparable;
úsese solo si se quiere un proxy y se documenta el cambio de fuente.
