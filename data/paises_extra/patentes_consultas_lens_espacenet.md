# Patentes de IA — consultas Lens/Espacenet listas para los consultores

**Indicadores que cierra:** 82 (Familias de patentes de IA) · 83 (Aplicantes) · 84 (Inventores), para
España, Estonia, Singapur, Alemania y Portugal.
**Por qué Lens/Espacenet:** OECD.AI/CSET solo publica **familias** (no aplicantes/inventores por país).
La atribución por país del **solicitante** y del **inventor** se obtiene en Lens.org (facetas/Analysis por
país de la parte) o Espacenet/PATSTAT.

> ⚠️ **Anti-alucinación / verificar en plataforma:** abajo doy la sintaxis con la que tengo confianza
> (códigos CPC, campos `cpc`/`pa`/`in`/`pd` de Espacenet, `class_cpc.symbol` de Lens). Donde un nombre de
> faceta/campo puede variar según la versión de la plataforma lo marco **(verificar etiqueta)**. No inventes
> resultados: si una faceta no existe tal cual, usa la pestaña *Analysis* o el filtro de país equivalente.

---

## 0. Decisiones a FIJAR antes de contar (§7 del handoff) — bloquean comparabilidad

| # | Decisión | Opciones | Recomendación (a confirmar con el operador / método ILIA 2025) |
|---|---|---|---|
| D1 | **Definición de "IA" (CPC)** | (a) Núcleo **G06N** (+ subgrupos); (b) Taxonomía **amplia WIPO/OECD** (añade G06F, G06T/G06V visión, G10L voz, G06Q, A61B…) | **Replicar EXACTAMENTE lo que ILIA 2025 usó para los demás países.** Si no consta, usar (a) G06N como base reproducible y documentar. |
| D2 | **Atribución por país** | País del **solicitante** (applicant) vs país del **inventor** | 83 = **país del solicitante**; 84 = **país del inventor**. ⚠️ Ver D2-bis. |
| D2-bis | **Definiciones CRUZADAS en el Excel del operador** | La definición de "Aplicantes" describe inventores y viceversa | **Fijar el mapeo 83↔solicitante / 84↔inventor antes de contar.** No contar hasta resolver. |
| D3 | **Ventana de años** | p. ej. última década; por fecha de **prioridad** vs **publicación** | Replicar ILIA 2025. Por defecto: **2015–2025 por fecha de publicación** (`pd`), y reportar también prioridad. |
| D4 | **Nivel de conteo / dedup** | Familia simple vs documento; entidades **distintas** vs apariciones | 82 = **familias** (simple family). 83/84 = **entidades/personas DISTINTAS** (deduplicadas), no apariciones. |

**Mientras D1–D4 no estén fijadas, estas consultas quedan como BORRADOR ejecutable, no como dato final.**

---

## 1. Definición de IA por CPC (para D1)

- **Núcleo reproducible (recomendado por defecto):** clase **`G06N`** = *Computing arrangements based on specific
  computational models* (IA/ML). Subgrupos reales relevantes: `G06N3/00` (modelos biológicos / redes neuronales),
  `G06N5/00` (modelos basados en conocimiento), `G06N7/00` (modelos matemáticos), `G06N20/00` (machine learning).
  *(Opcional excluir `G06N10/00` = computación cuántica si ILIA no la cuenta como IA.)*
- **Amplia (WIPO/OECD):** además de G06N añade aplicaciones de IA en otras clases (visión `G06T`/`G06V`, voz `G10L`,
  datos/negocio `G06Q`, salud `A61B`, etc.). **No fijo aquí la lista completa**: úsese la lista CPC/IPC EXACTA que
  ILIA 2025 empleó (pedirla al operador). PATSTAT/OECD-REGPAT es la vía canónica si se busca paridad metodológica.

---

## 2. Espacenet — familias por CPC (indicador 82) · cross-check de 70-72 ETO

**Búsqueda inteligente (Smart search), pegar y ajustar la ventana de años:**

```
cpc = "G06N" AND pd within "2015-2025"
```

- Sirve para el **volumen de documentos/familias por jurisdicción**; Espacenet agrupa por *simple family*.
- **Limitación:** Espacenet (UI pública) **no filtra de forma fiable por país del solicitante/inventor** →
  para 83/84 usar Lens (§3). Espacenet es buen **cross-check** del número de **familias** (82), que el handoff
  toma primero de ETO CAT (cat.eto.tech → Patent).
- Para acotar a un país como **oficina** (no como país de la parte), añade la jurisdicción, p. ej. `pn = ES` /
  `pn = EP` — pero eso es país de *publicación*, no de origen; **no** confundir con la atribución de D2.

---

## 3. Lens.org — aplicantes (83) e inventores (84) por país

### 3.1 Consulta base (pegar en *Patents → Structured Search / Query*)
Ajusta la ventana de años (campo de fecha: `date_published`; alternativa `earliest_priority_date` — **verificar**):

```
class_cpc.symbol:(G06N*) AND date_published:[2015-01-01 TO 2025-12-31]
```

> Para la definición **amplia** (D1-b), sustituye `(G06N*)` por la lista CPC completa de ILIA 2025, p. ej.
> `class_cpc.symbol:(G06N* OR G06V* OR G10L* OR ...)` (rellenar con el set exacto).

### 3.2 Obtener el conteo por país de la parte
1. Ejecuta la consulta base.
2. Abre la pestaña **Analysis** (o el panel de **Filtros** a la izquierda).
3. **Aplicantes (83):** filtra/segmenta por **país del solicitante** *(verificar etiqueta: "Applicant Country" /
   filtro de país en la faceta "Applicants")*. El **nº de aplicantes DISTINTOS** del país = indicador 83.
4. **Inventores (84):** ídem por **país del inventor** *(verificar etiqueta)*. El **nº de inventores DISTINTOS** = 84.
5. Repite para cada país. Países: **España, Estonia, Singapur, Alemania, Portugal**.

> Si la plataforma da "apariciones" en vez de "entidades distintas", usa la lista deduplicada de
> aplicantes/inventores (Analysis → Applicants/Inventors) y cuenta entidades únicas (D4).

### 3.3 Atajo por país (filtro de país de la parte, si la UI lo permite como campo)
Plantilla **candidata** (verificar el nombre exacto del campo de país en el *query builder* de Lens):

```
# Aplicantes en España (83):
class_cpc.symbol:(G06N*) AND date_published:[2015-01-01 TO 2025-12-31] AND applicant.address.country:ES
# Inventores en España (84):
class_cpc.symbol:(G06N*) AND date_published:[2015-01-01 TO 2025-12-31] AND inventor.address.country:ES
```

Códigos ISO de país a sustituir: **ES** (España), **EE** (Estonia), **SG** (Singapur), **DE** (Alemania), **PT** (Portugal).
*(Si `applicant.address.country` / `inventor.address.country` no son válidos en tu versión de Lens, cae al método
de facetas/Analysis de §3.2 — ese siempre funciona.)*

---

## 4. Tabla de resultados (rellenar; un valor por celda + fecha de extracción)

| País | 82 Familias (ETO/Espacenet) | 83 Aplicantes distintos (Lens) | 84 Inventores distintos (Lens) | Def. CPC usada (D1) | Ventana (D3) | Fecha extracción |
|---|---|---|---|---|---|---|
| España (ES) |  |  |  |  |  |  |
| Estonia (EE) |  |  |  |  |  |  |
| Singapur (SG) |  |  |  |  |  |  |
| Alemania (DE) |  |  |  |  |  |  |
| Portugal (PT) |  |  |  |  |  |  |

Pistas previas (NO finales): SG ≈ 661 solicitudes / 297 concedidas (2017-2020, CSET); DE ≈ 436 familias (frágil,
linaje CSET/WIPO vía AI Index 2024); ES < 57 (pista ETO). Reemplazar por la extracción reproducible.

---

## 5. Notas de comparabilidad
- **Mismo método en los 5 países** y, si es posible, **el mismo que ILIA aplicó al resto** (D1–D4). Documentar la
  consulta exacta y la fecha (las bases se actualizan).
- **Familias ≠ documentos:** 82 cuenta familias; no sumar publicaciones de la misma familia.
- **Doble atribución:** una familia con co-solicitantes de 2 países cuenta en ambos (decidir si fraccional o por
  conteo entero — replicar ILIA 2025).
- **Alternativa canónica:** OECD-REGPAT / PATSTAT atribuye por residencia del inventor/solicitante (estándar OECD
  STI). Si se busca paridad estricta con OECD.AI, es la vía; Lens/Espacenet es el proxy operativo aquí.
