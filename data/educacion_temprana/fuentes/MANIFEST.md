# MANIFEST de fuentes — documentos para el cierre verbatim

El entorno **bloquea la descarga directa** de los portales oficiales (`curl`, `wget`, `WebFetch`
→ `403 "Host not in allowlist"`; solo WebSearch). Por eso el borrador (`informe.md`) se apoya en
buscador y portales oficiales secundarios, no aún en el texto literal.

**Estado del análisis (2026-06-05):** categorías cerradas por la regla inclusiva →
**ES = DE = EE = SG = 5 (100)**, **PT = 4 (75, verificado)**. Por la lógica acumulativa, los
cuatro «5» **ya no cambian de categoría**; estos documentos sirven para **extraer y verificar la
cita textual que justifica cada 5** (y, si se optara por una regla más estricta, para medir la
sustantividad de la IA en EE/SG).

**Cómo aportarlos:** descarga el PDF/HTML y (a) guárdalo en `data/educacion_temprana/fuentes/<PAÍS>/`
con commit a la rama, **o** (b) pégame en el chat la sección que nombra la IA. Con cada documento
hago extracción de la mención a IA con **cita textual + ubicación** y **verificación verbatim**
(subcadena exacta).

> URLs consultadas el 2026-06-05. Si alguna falla, dímelo y busco la vigente.

---

## 🔴 Prioridad A — justificar con verbatim los cuatro «5»

### España (→ `fuentes/ES/`)

| # | Documento | URL oficial | Formato | Cita a localizar |
|---|---|---|---|---|
| A1 | **RD 217/2022** (ESO) — Anexo II, «Tecnología y Digitalización» | https://www.boe.es/buscar/pdf/2022/BOE-A-2022-4975-consolidado.pdf | PDF grande | «inteligencia artificial» en los saberes básicos (curso + literal) |
| A2 | **RD 243/2022** (Bachillerato) — «Tecnología e Ingeniería» | https://www.boe.es/buscar/pdf/2022/BOE-A-2022-5521-consolidado.pdf | PDF grande | confirmar «…incluyendo inteligencia artificial…» (cita de Educagob) |

### Alemania (→ `fuentes/DE/`)

| # | Documento | URL oficial | Formato | Cita a localizar |
|---|---|---|---|---|
| A3 | **LehrplanPLUS Bayern — Gymnasium Jhst. 11, Informatik** (Lernbereich «KI») | https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/11/informatik/ntg | HTML/PDF | «Künstliche Intelligenz» como Lernbereich (¿Pflicht?) |
| A4 | **Kernlehrplan Informatik Sek II — NRW** | https://lehrplannavigator.nrw.de/system/files/media/document/file/klp_gost_informatik.pdf | PDF | «Künstliche Intelligenz und maschinelles Lernen» (Inhaltsfeld) |

### Estonia (→ `fuentes/EE/`)

| # | Documento | URL oficial | Formato | Cita a localizar |
|---|---|---|---|---|
| A5 | **Anexo de Informaatika** (electiva) del currículo nacional (*PRÕK/GRÕK Lisa*) | https://www.riigiteataja.ee/aktilisa/1080/3202/3005/18m_pohi_lisa10.pdf | PDF | «tehisintellekt / artificial intelligence» en el syllabus electivo + cuán sustantivo |
| A5b | *(contexto)* Gümnaasiumi riiklik õppekava (EN) | https://www.riigiteataja.ee/en/eli/529042024001/consolide | HTML | confirmar Informaatika electiva en gümnaasium |

### Singapur (→ `fuentes/SG/`)

| # | Documento | URL oficial | Formato | Cita a localizar |
|---|---|---|---|---|
| A6 | **Computing Syllabus 7155 — O-Level 2025** (SEAB) | https://www.seab.gov.sg/files/O%20Lvl%20Syllabus%20Sch%20Cddts/2025/7155_y25_sy.pdf | PDF | «machine learning / artificial intelligence» en el contenido + si es módulo o subtema |
| A6b | *(detalle)* Computing G3 T&L Syllabus 2024 (MOE) | https://www.moe.gov.sg/-/media/files/secondary/fsbb/syllabus/2024-g3-computing-teaching-and-learning-syllabus.pdf | PDF | learning outcomes de IA/ML (mide sustantividad) |

---

## 🟢 Prioridad B — Portugal (ya verificado, opcional)

PT=4 está **confirmado por WebSearch** (AE vigente = D1 Algoritmia/Programação + D2 Multimédia,
sin IA; IA solo en la revisión 2027). Estos documentos solo sirven para dejar el verbatim del
«negativo» (barrido que confirma ausencia de IA en el currículo vigente).

| # | Documento | URL oficial | Formato |
|---|---|---|---|
| B1 | AE *Aplicações Informáticas B* (12.º) | https://www.dge.mec.pt/sites/default/files/Curriculo/Aprendizagens_Essenciais/12_aplicacoes_informaticas_b.pdf | PDF |
| B2 | Portaria n.º 226-A/2018 (matrices del secundário) | https://files.dre.pt/1s/2018/08/15101/0000200018.pdf | PDF |

---

## Estado de descargas

| País | Cat. | Documentos aportados | Pendientes (para verbatim) |
|---|:--:|---|---|
| ES | 5 | — | **A1, A2** |
| DE | 5 | — | **A3, A4** |
| EE | 5 | — | **A5** (, A5b) |
| SG | 5 | — | **A6** (, A6b) |
| PT | 4 | — | B1, B2 (opcional) |

*(Se actualizará al commitear los archivos a `fuentes/<país>/`.)*

### Mínimo para cerrar todo el verbatim
Los **6 PDFs de prioridad A** (A1, A2, A3, A4, A5, A6) justifican los cuatro «5» con cita exacta.
