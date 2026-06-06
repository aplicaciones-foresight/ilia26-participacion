# Desarrollo de IA (Hugging Face) — inventario de organizaciones por país

> **Estado del dato:** ⚠️ **Conteo de modelos NO obtenible desde este entorno.**
> Hugging Face devuelve **HTTP 403** en API (`huggingface.co/api/...`), páginas de
> organización y proxies; `curl` está restringido a `raw.githubusercontent.com`.
> Solo funcionó WebSearch, que **no** expone de forma fiable el contador "Models".
> No se reportan conteos para no incurrir en alucinación. Lo verificado y
> defendible es la **identidad y el país de cada organización** (contrastado con
> fuentes reales: universidades, gobierno, empresas). Confianza numérica: **BAJA**.
> Fecha de inventario: 2026-06-06.

## Organizaciones verificadas (país confirmado)

### España (ES)
- **BSC-LT** — Language Technologies Lab @ Barcelona Supercomputing Center — https://huggingface.co/BSC-LT (familia Salamandra/ALIA, MareNostrum 5)
- **HPAI-BSC** — High Performance AI @ BSC — https://huggingface.co/HPAI-BSC (familia Aloe, salud)
- **PlanTL-GOB-ES** — Plan de Tecnologías del Lenguaje, Gobierno de España — https://huggingface.co/PlanTL-GOB-ES (RoBERTa-bne)
- **projecte-aina** — Projecte Aina, Generalitat de Catalunya — https://huggingface.co/projecte-aina
- **HiTZ** — HiTZ/IXA, Universidad del País Vasco (UPV/EHU) — https://huggingface.co/HiTZ (Latxa, euskera)
- **clibrain** — CliBrAIn (empresa, Madrid) — https://huggingface.co/clibrain (Lince)
- *(plausibles, verificar: CiTIUS, CENID, IIC del ecosistema ILENIA)*

### Estonia (EE)
- **tartuNLP** — NLP group, Institute of Computer Science, University of Tartu — https://huggingface.co/tartuNLP (EstBERT, Llammas)
- *(cola de cuentas individuales de investigadores; verificar)*

### Singapur (SG)
- **aisingapore** — AI Singapore (programa nacional, NUS / NRF) — https://huggingface.co/aisingapore (SEA-LION)
- **sail** — Sea AI Lab (Sea Ltd.) — https://huggingface.co/sail (Sailor)
- **NationalUniversityofSingapore** — NUS — https://huggingface.co/NationalUniversityofSingapore
- *(verificar: SUTD, NTU, DSO)*

### Alemania (DE)
- **laion** — LAION e.V. (ONG) — https://huggingface.co/laion (CLIP, LAION-5B)
- **LeoLM** — LAION + Hessian.AI — https://huggingface.co/LeoLM
- **Aleph-Alpha** — Aleph Alpha (Heidelberg) — https://huggingface.co/Aleph-Alpha (Pharia)
- **DFKI** (y DFKI-SLT, dfki-av) — German Research Center for AI — https://huggingface.co/DFKI
- **deepset** — deepset GmbH (Berlín) — https://huggingface.co/deepset (GBERT, GermanQuAD)
- **occiglot** — colectivo europeo coordinado desde DFKI/Hessian.AI/TU Darmstadt — https://huggingface.co/occiglot — ⚠️ multinacional (socios BE/ES) → atribución parcial
- *(plausibles, verificar: T-Systems/Telekom, flair/Humboldt, LLäMmlein/U. Würzburg)*

### Portugal (PT)
- **PORTULAN** — PORTULAN CLARIN / grupo NLX, Universidade de Lisboa (+ U. Porto), FCT — https://huggingface.co/PORTULAN (Albertina, Gervásio, Serafim) — ⚠️ publica variantes PT-PT y PT-BR
- *(verificar: Unbabel. OJO: BERTimbau es de NeuralMind, Brasil → NO contar como PT)*

## Cómo obtener los conteos manualmente (fiable)
Desde una red sin bloqueo a `huggingface.co`, por cada org:
- **API:** `https://huggingface.co/api/models?author=<ORG>&limit=1000&full=false` → contar el array (paginar si llega a 1000). Sumar por país con la lista de arriba.
- **Web:** abrir `https://huggingface.co/<ORG>` y leer el número de la pestaña **"Models"** (anotar fecha).
- Congelar la lista de orgs por país y la **fecha de captura** (el conteo cambia a diario).
