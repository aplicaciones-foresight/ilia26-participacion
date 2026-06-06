# CONTINUAR — cierre verbatim en un run LOCAL de Claude Code

Este análisis (`data/educacion_temprana/`) se hizo en **Claude Code on the web**, cuyo entorno
tiene una **red por allowlist** que bloquea la descarga de los portales oficiales (`curl`/`wget`/
`WebFetch` → `403 "Host not in allowlist"`; solo WebSearch). Por eso quedó **un único paso
pendiente** que un run **local** (con red abierta) puede cerrar sin fricción.

## Estado actual (no rehacer)

- **Categorías cerradas** (regla inclusiva, decisión 2026-06-05):
  **ES = DE = EE = SG = 5 (100)**, **PT = 4 (75, verificado)**. Ver `informe.md` / `puntajes.csv`.
- Por la lógica acumulativa, **las categorías NO cambian** con este paso. El verbatim solo
  **justifica con cita exacta** cada «5» (y, para EE/SG, mide la *sustantividad* de la IA por si
  se quisiera aplicar una regla más estricta).
- Lo único que falta: **descargar 6 PDFs primarios, extraer la cita de IA con su ubicación y
  verificarla verbatim**.

## Prompt para pegar en Claude Code local

> Continúa la tarea de `data/educacion_temprana/` en la rama `claude/peaceful-ptolemy-SsMhN`.
> Lee `data/educacion_temprana/fuentes/MANIFEST.md` y `informe.md`. Descarga los 6 documentos de
> prioridad A (A1–A6) a `data/educacion_temprana/fuentes/<PAÍS>/`. Para cada país «5» (ES, DE, EE,
> SG), localiza la mención literal a IA en el documento, extrae la **cita textual + ubicación**
> (documento, nivel, asignatura, sección/página) y **verifica que la cita es subcadena exacta**
> del texto (reusa `src/verify_verbatim.py`: `normalizar`/`es_subcadena`). Actualiza
> `evidencias/evidencias.json` (`verificacion: "verbatim_ok"`, con `ubicacion` y la cita exacta),
> sube la `confianza` a «alta» en `puntajes.csv`/`informe.md` donde el verbatim confirme, y marca
> en `MANIFEST.md` los documentos como aportados. Si algún término NO aparece literalmente, dilo y
> reevalúa esa categoría con evidencia. Para EE y SG anota si la IA es módulo propio o subtema
> (sustantividad). Commit + push.

## Pasos detallados

1. **Checkout:** `git fetch origin && git checkout claude/peaceful-ptolemy-SsMhN`
2. **Descargar** (UA de navegador; si un portal bloquea, baja el PDF desde el navegador y guárdalo
   con el mismo nombre). Filenames sugeridos:

   | # | País | Guardar como | URL |
   |---|---|---|---|
   | A1 | ES | `fuentes/ES/RD-217-2022-ESO.pdf` | https://www.boe.es/buscar/pdf/2022/BOE-A-2022-4975-consolidado.pdf |
   | A2 | ES | `fuentes/ES/RD-243-2022-Bachillerato.pdf` | https://www.boe.es/buscar/pdf/2022/BOE-A-2022-5521-consolidado.pdf |
   | A3 | DE | `fuentes/DE/LehrplanPLUS-Bayern-Gym11-Informatik.html` | https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/11/informatik/ntg |
   | A4 | DE | `fuentes/DE/KLP-Informatik-SekII-NRW.pdf` | https://lehrplannavigator.nrw.de/system/files/media/document/file/klp_gost_informatik.pdf |
   | A5 | EE | `fuentes/EE/PROK-Lisa-Informaatika.pdf` | https://www.riigiteataja.ee/aktilisa/1080/3202/3005/18m_pohi_lisa10.pdf |
   | A6 | SG | `fuentes/SG/Computing-7155-2025-SEAB.pdf` | https://www.seab.gov.sg/files/O%20Lvl%20Syllabus%20Sch%20Cddts/2025/7155_y25_sy.pdf |

3. **Extraer texto:** `pdftotext -layout archivo.pdf archivo.txt` (poppler-utils). Para HTML, guarda
   el render a texto. (Los PDFs del BOE son grandes: busca dentro por el término, no hace falta leer
   las ~500 págs enteras.)
4. **Localizar la cita de IA** por idioma:

   | País | Término a buscar | Ubicación esperada |
   |---|---|---|
   | ES (A1) | `inteligencia artificial` | RD 217/2022, Anexo II, «Tecnología y Digitalización» (ESO) |
   | ES (A2) | `inteligencia artificial` | RD 243/2022, «Tecnología e Ingeniería» (Bachillerato) |
   | DE (A3) | `Künstliche Intelligenz` | LehrplanPLUS Gym. 11, Informatik, Lernbereich KI |
   | DE (A4) | `Künstliche Intelligenz`, `maschinelles Lernen` | KLP Informatik Sek II, Inhaltsfeld KI/ML |
   | EE (A5) | `tehisintellekt` / `artificial intelligence` | anexo de Informaatika (asignatura electiva) |
   | SG (A6) | `machine learning`, `artificial intelligence` | syllabus 7155 (¿módulo o subtema?) |

5. **Verificar verbatim** (reusa el código del repo):
   ```python
   import sys; sys.path.insert(0, "src")
   from verify_verbatim import normalizar, es_subcadena
   texto = open("data/educacion_temprana/fuentes/ES/RD-217-2022-ESO.txt", encoding="utf-8").read()
   cita = "tecnologías emergentes incluyendo inteligencia artificial"   # ejemplo
   assert es_subcadena(cita, texto), "la cita NO es subcadena exacta del documento"
   ```
6. **Actualizar entregables:**
   - `evidencias/evidencias.json`: por cada «5», fija la `cita_o_snippet` a la cita verificada,
     añade `ubicacion` (doc/nivel/asignatura/sección o página) y pon `verificacion: "verbatim_ok"`.
   - `puntajes.csv` e `informe.md`: sube `confianza` a **alta** donde el verbatim confirme.
   - `fuentes/MANIFEST.md`: marca los documentos como aportados en «Estado de descargas».
7. **Commit + push** a `claude/peaceful-ptolemy-SsMhN`.

## Criterios de aceptación (definition of done)

- [ ] Los 6 PDFs/HTML en `fuentes/<país>/` (commiteados).
- [ ] Cada país «5» (ES, DE, EE, SG) tiene **≥1 cita de IA verificada verbatim** con ubicación en
      `evidencias.json` (`verbatim_ok`), reflejada en `informe.md`.
- [ ] `confianza` actualizada (alta donde el verbatim confirme).
- [ ] EE y SG: anotada la **sustantividad** (módulo propio vs subtema) por si se aplica una regla
      estricta en el futuro.
- [ ] Si algún término **no** aparece literalmente, queda **documentado** y la categoría afectada,
      reevaluada con evidencia (p. ej., si RD 217/2022 no nombra «inteligencia artificial», ES se
      sostiene por RD 243/2022; si tampoco, reconsiderar).
- [ ] (Opcional) PT: barrido negativo verbatim (B1/B2) que confirme ausencia de IA en el currículo
      vigente.

## Notas

- **No cambies las categorías** salvo que el verbatim contradiga la evidencia actual (en ese caso,
  documenta y ajusta). Este paso es de **justificación**, no de recálculo.
- Si decides cambiar la **regla de umbral** (de inclusiva a estricta), EE y SG volverían a 4: la
  sustantividad que anotes aquí es justo el dato para esa decisión.
- Mantén la disciplina del repo: «ningún número de memoria», cita verbatim verificada, mejor `null`
  + alerta que un valor no respaldado.
