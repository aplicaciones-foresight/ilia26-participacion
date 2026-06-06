# Patentes de IA: Familias / Aplicantes / Inventores — IDs 82, 83, 84

## Hallazgo metodológico crítico (leer primero)
De las 3 métricas, **OECD.AI (y su linaje CSET CAT / OWID / Stanford HAI) solo
publica FAMILIAS** de patentes de IA. **Aplicantes** e **Inventores por país NO
existen** como serie publicada en esa fuente:
- El dataset CSET CAT "**focuses on countries, not organizations or individuals**".
- Atribuye cada familia al **país de primera presentación** (filing office),
  **no** al país del inventor ni del solicitante. (CSET dice que las métricas por
  nacionalidad del inventor son "trabajo futuro".)
- Evidencia: código del pipeline OWID `etl/.../artificial_intelligence/2026-04-27/
  cset.py` + `cset.meta.yml` (descargado de github.com/owid/etl): solo variables
  `num_patent_applications` y `num_patent_granted` (+ `_per_mil`). No hay variable
  de aplicantes ni de inventores.

➡️ **Implicación para ILIA:** los indicadores (2) Aplicantes y (3) Inventores
**deben cambiar de fuente** (EPO PATSTAT / OECD STI / Lens.org / Espacenet) y usar
otra base de conteo (país del solicitante y país del inventor, respectivamente).
Citarlos bajo "OECD.AI" sería incorrecto. Esto concuerda con la planilla, que para
estos 3 indicadores apuntaba a **Espacenet** (no OECD.AI) — pero requieren consulta
manual definida.

## Valores (acceso automático bloqueado: oecd.ai, OWID, cat.eto.tech, Zenodo → 403)

### (1) Familias de patentes de IA — base: familia, país de PRIMERA PRESENTACIÓN
> **Verificado por un 2º agente independiente.** Hallazgos:
| País | Valor | Año | Fuente | Confianza |
|---|---|---|---|---|
| Singapur (SG) | **661 solicitudes / 297 concedidas** | ventana 2017-2020 (informe 2023) | CSET "Examining Singapore's AI Progress" | MEDIA (cifra literal, pero antigua) |
| Alemania (DE) | **~436** (⚠️ dato FRÁGIL) | ambiguo | linaje CSET/WIPO vía Stanford AI Index **2024** (no 2026); Visual Capitalist | **BAJA — NO usar sin reconfirmar** |
| España (ES) | **NO OBTENIDO** (solo pista: < 57, por debajo de México) | — | — | BAJA |
| Estonia (EE) | **NO OBTENIDO** | — | — | BAJA |
| Portugal (PT) | **NO OBTENIDO** | — | — | BAJA |

> ⚠️ **Sobre el "436" de Alemania:** el número circula, pero la verificación detectó
> conflación: (a) la fuente real es CSET/WIPO recogido por el **AI Index 2024**, no
> el 2026; (b) la métrica/año son ambiguos (descrito como "2024" y como "acumulado";
> el ranking acompañante —China 25.177, EE.UU. 17.307— es **incompatible con un solo
> año**), por lo que **436 es casi seguro un conteo acumulado de familias, no
> "concedidas en 2024"**. → Extraer el valor correcto de cat.eto.tech (ruta abajo).

### (2) Aplicantes de patentes de IA  → **NO PUBLICADO** por OECD.AI/CSET (los 5 países). Confianza en "no disponible": ALTA.
### (3) Inventores de patentes de IA → **NO PUBLICADO** por OECD.AI/CSET (los 5 países). Confianza en "no disponible": ALTA.

## Cómo obtener los valores manualmente
**Familias (valores actuales por país):**
- cat.eto.tech: https://cat.eto.tech/?dataset=Patent&expanded=Summary-metrics → elegir ES/EE/SG/DE/PT → "AI patent applications"/"granted".
- OWID CSV: https://ourworldindata.org/grapher/artificial-intelligence-patents-submitted.csv?csvType=full
- CSET CAT bundle (Zenodo, último 2026-03-19): https://zenodo.org/records/19103157 (`cat.zip`, CSVs país×año con `num_patent_applications`/`num_patent_granted`).
- OECD.AI: https://oecd.ai/en/data (AI R&D → AI patents). Metodología: https://oecd.ai/en/methodology

**Aplicantes e Inventores (requieren fuente que los modele):**
- OECD STI / EPO PATSTAT: contar solicitantes distintos (país del solicitante) e
  inventores distintos (país del inventor) sobre familias de IA. Ref.: OECD
  "Identifying emerging AI technologies using patent data" (sept-2025)
  https://www.oecd.org/en/publications/identifying-emerging-ai-technologies-using-patent-data_d17e9a1a-en.html
- Lens.org / Espacenet: consulta de IA (CPC G06N + keywords) y facetar por país del
  solicitante / del inventor para contar entidades distintas.
- WIPO GenAI Patent Landscape (2024): familias por país del inventor, pero solo IA
  generativa: https://www.wipo.int/web/patent-analytics/generative-ai

## Cross-checks independientes consultados
- Stanford HAI AI Index 2026 (R&D): https://hai.stanford.edu/ai-index/2026-ai-index-report/research-and-development
- OWID: https://ourworldindata.org/grapher/artificial-intelligence-patents-submitted
- WIPO GenAI: https://www.wipo.int/web/patent-analytics/generative-ai
- Nota: OECD.AI, OWID y Stanford HAI comparten origen CSET → **no son
  estadísticamente independientes**; WIPO sí lo es pero cubre solo GenAI.
