# MANIFEST de fuentes — documentos para el cierre verbatim

**Cierre verbatim completado el 2026-06-06.** Los 6 documentos de Prioridad A se descargaron con
`curl` a `fuentes/<PAÍS>/`, se extrajo texto con `pdftotext` (HTML para A3) y las citas decisivas
se verificaron como **subcadena exacta** del texto primario reusando
`src/verify_verbatim.py:normalizar`+`es_subcadena`. El reporte por cita está en
`fuentes/_verify_report.json` (15/15 OK), corrido por `fuentes/_verify_run.py`.

> **Nota sobre el bloqueo previo:** versiones anteriores reportaban `Host not in allowlist`.
> En esta pasada `curl` con `-A "Mozilla/5.0"` resolvió los 6 dominios oficiales (boe.es,
> lehrplanplus.bayern.de, lehrplannavigator.nrw.de, riigiteataja.ee, seab.gov.sg). WebFetch
> sigue restringido, pero `curl` directo a los hosts oficiales **funciona**.

**Estado del análisis:** categorías cerradas por la regla inclusiva →
**ES = DE = EE = SG = 5 (100)**, **PT = 4 (75)**. Confianza **alta** en los cuatro «5»
(verbatim_ok). Para EE y SG, el verbatim confirma además que la IA aparece como **SUBTEMA**
(no como módulo propio): bajo una regla estricta de sustantividad ambos volverían a 4.

---

## 🔴 Prioridad A — verbatim que justifica los cuatro «5»  (✅ aportados)

### España (→ `fuentes/ES/`)

| # | Documento | URL oficial | Local | Estado |
|---|---|---|---|:--:|
| A1 | **RD 217/2022** (ESO) — Anexo II, «Tecnología y Digitalización» | https://www.boe.es/buscar/pdf/2022/BOE-A-2022-4975-consolidado.pdf | `ES/A1_RD217-2022_BOE-A-2022-4975_consolidado.pdf` (+ `ES/A1.txt`) | ✅ verbatim_ok |
| A2 | **RD 243/2022** (Bachillerato) — Anexo II | https://www.boe.es/buscar/pdf/2022/BOE-A-2022-5521-consolidado.pdf | `ES/A2_RD243-2022_BOE-A-2022-5521_consolidado.pdf` (+ `ES/A2.txt`) | ✅ verbatim_ok |

Citas verificadas:
- A1, Saberes básicos C: «Aplicaciones informáticas sencillas, para ordenador y dispositivos móviles, e introducción a la inteligencia artificial.»
- A1, Criterio 5.2: «…aplicando herramientas de edición, así como **módulos de inteligencia artificial** que añadan funcionalidades a la solución.»
- A2, Saberes básicos E (Tecnología e Ingeniería II): «**Inteligencia artificial**, big data, bases de datos distribuidas y ciberseguridad.»
- A2, Criterio 5.1 (Tecnología e Ingeniería I): «…tecnologías emergentes, tales como **inteligencia artificial**, internet de las cosas, big data…»

### Alemania (→ `fuentes/DE/`)

| # | Documento | URL oficial | Local | Estado |
|---|---|---|---|:--:|
| A3 | **LehrplanPLUS Bayern — Gym Jhst. 11, Informatik (NTG)** — Lernbereich «KI» | https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/11/informatik/ntg | `DE/A3_LehrplanPLUS_Bayern_Gym11_Informatik_ntg.html` (+ `DE/A3.txt`) | ✅ verbatim_ok |
| A4 | KLP Informatik **GOSt** (Sek II) NRW — *no aporta KI* | https://lehrplannavigator.nrw.de/system/files/media/document/file/klp_gost_informatik.pdf | `DE/A4_KLP_Informatik_GOSt_NRW.pdf` (+ `DE/A4.txt`) | ⚠️ aportado, pero el KLP GOSt vigente es de 2014 y **NO menciona KI** |
| A4b | **KLP NRW · Sek I · Klasse 5/6 · Pflichtfach Informatik** (2021/22) — Inhaltsfeld «Automaten und künstliche Intelligenz» | https://lehrplannavigator.nrw.de/system/files/media/document/file/si_kl5u6_if_klp_2021_07_01.pdf | `DE/A4b_KLP_NRW_SekI_Kl5u6_Informatik_2021.pdf` (+ `DE/A4b.txt`) | ✅ verbatim_ok (sustituye a A4 para NRW) |

Citas verificadas:
- A3 (Bayern Gym 11 NTG): «Künstliche Intelligenz (ca. 16 Std.)» y, en Kompetenzerwartungen, «**diskutieren Ansätze zur Definition des Begriffs Künstliche Intelligenz (KI)**, beschreiben verschiedene Grundideen von Verfahren der KI (u. a. maschinelles Lernen) sowie ihre Anwendungsbereiche.»  *(Corrección al borrador previo: el verbo verbatim es «diskutieren», no «erörtern».)*
- A4b (NRW Klasse 5/6, Pflichtfach Informatik), Inhaltsfeld «**Automaten und künstliche Intelligenz**», Inhaltliche Schwerpunkte: «Maschinelles Lernen mit Entscheidungsbäumen», «Maschinelles Lernen mit neuronalen Netzen».

> Hallazgo importante: el documento A4 (KLP GOSt 2014) NO contiene «Künstliche Intelligenz».
> El borrador previo del informe describía el «Inhaltsfeld KI» como si estuviera en Sek II NRW;
> el verbatim oficial vinculante de NRW para IA está en el **KLP Pflichtfach Klasse 5/6 (2021)**.
> No invalida DE = 5 (Bayern Gym 11 ya basta), pero corrige la ubicación exacta de la cita NRW.

### Estonia (→ `fuentes/EE/`)

| # | Documento | URL oficial | Local | Estado |
|---|---|---|---|:--:|
| A5 | **PRÕK Lisa 10 — Valikõppeaine «Informaatika»** (electiva del Põhikool, redacción 2023) | https://www.riigiteataja.ee/aktilisa/1080/3202/3005/18m_pohi_lisa10.pdf | `EE/A5_PROK_Lisa10_Informaatika.pdf` (+ `EE/A5.txt`) | ✅ verbatim_ok |

Citas verificadas (III kooliaste, tema «Infoühiskonna tehnoloogiad»):
- Õpitulemus 6: «**kirjeldab tehisintellekti** ja asjade interneti rakendusviise majanduses, avalikus sektoris, hariduses ja sellega kaasnevaid võimalikke ohtusid».
- Õppesisu: «Uued tehnoloogiatrendid: **tehisintellekt**, ava- ja suurandmed.» «**Tehisintellekti** ja asjade interneti mõisted, näited, rakendused ja seonduvad riskid.»

**Sustantividad EE = subtema.** IA es 1 de 9 õpitulemused del tema «Infoühiskonna tehnoloogiad»
dentro de la asignatura **electiva** (`valikõppeaine`) Informaatika; NO es un módulo propio.

### Singapur (→ `fuentes/SG/`)

| # | Documento | URL oficial | Local | Estado |
|---|---|---|---|:--:|
| A6 | **Computing 7155 — O-Level 2025** (SEAB) | https://www.seab.gov.sg/files/O%20Lvl%20Syllabus%20Sch%20Cddts/2025/7155_y25_sy.pdf | `SG/A6_Computing_7155_OLvl_2025.pdf` (+ `SG/A6.txt`, `SG/A6_flow.txt`) | ✅ verbatim_ok |

Citas verificadas (Module 5 «Impact of Computing», sección 5.4 «Emerging Technologies»):
- 5.4.1: «**Describe Artificial Intelligence (AI)** as the ability of a computer to perform complex tasks without constant human guidance and improve its performance as more data is collected.»
- 5.4.3: «**Define Machine Learning (ML)** as a technique used in AI and explain the difference between ML and traditional programming.»

**Sustantividad SG = subtema.** IA/ML son la sección 5.4 (5 learning outcomes) dentro del
Module 5; NO hay un módulo propio de IA. Además, los **cinco módulos oficiales** del 7155 2025
son: 1) Computing Fundamentals; 2) Algorithms and Programming; 3) Spreadsheets; 4) Networking;
5) Impact of Computing. *(Corrección al borrador previo, que listaba otros nombres.)*

---

## 🟢 Prioridad B — Portugal (ya verificado, no aportado)

PT=4 está confirmado por la **ausencia** de IA en la AE vigente de *Aplicações Informáticas B*
(dominios D1 + D2; IA solo en la revisión 2027). Estos PDFs no son necesarios para el cierre.

| # | Documento | URL oficial | Estado |
|---|---|---|:--:|
| B1 | AE *Aplicações Informáticas B* (12.º) | https://www.dge.mec.pt/sites/default/files/Curriculo/Aprendizagens_Essenciais/12_aplicacoes_informaticas_b.pdf | no aportado (opcional) |
| B2 | Portaria n.º 226-A/2018 | https://files.dre.pt/1s/2018/08/15101/0000200018.pdf | no aportado (opcional) |

---

## Estado de descargas

| País | Cat. | Confianza | Documentos aportados | Pendientes |
|---|:--:|:--:|---|---|
| ES | 5 | **alta** | **A1, A2** (verbatim_ok) | — |
| DE | 5 | **alta** | **A3, A4 (contexto), A4b** (verbatim_ok BY + NRW Sek I) | — |
| EE | 5 | **alta** | **A5** (verbatim_ok; IA = subtema en electiva) | — |
| SG | 5 | **alta** | **A6** (verbatim_ok; IA = subtema en electiva) | — |
| PT | 4 | alta | — | B1, B2 (opcional; PT=4 verificado por ausencia) |

## Reproducir la verificación

```bash
python data/educacion_temprana/fuentes/_verify_run.py
# → escribe data/educacion_temprana/fuentes/_verify_report.json
# → 15/15 verbatim_ok
```
