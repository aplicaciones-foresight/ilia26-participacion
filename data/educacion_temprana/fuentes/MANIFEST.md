# MANIFEST de fuentes — qué necesito que descargues (shopping list)

El entorno de ejecución **bloquea la descarga directa** de los portales oficiales (`curl`,
`wget` y `WebFetch` → `403 "Host not in allowlist"`; solo funciona WebSearch). Por eso el
borrador (`informe.md`) se apoya en buscador y en portales oficiales **secundarios**, no aún
en el texto literal del boletín/decreto/Lehrplan.

**Para cerrar la verificación verbatim necesito los documentos primarios.** Cómo aportarlos:

1. Descarga el PDF/HTML desde la URL oficial.
2. Guárdalo en `data/educacion_temprana/fuentes/<PAÍS>/` (carpetas ya creadas: `PT ES EE DE SG`)
   con el nombre sugerido, y haz commit a la rama `claude/peaceful-ptolemy-SsMhN`.
3. **Alternativa** si el PDF es muy grande o difícil: pégame en el chat el texto de la
   sección relevante (la que nombra «inteligencia artificial / KI / IA») y yo verifico.

Con cada documento haré: extracción de la(s) mención(es) a TIC/IA con **cita textual +
ubicación**, **verificación verbatim** (subcadena exacta), y consolidación de la categoría.

> **Fecha de consulta de las URLs:** 2026-06-05. Si alguna falla, dímelo y busco la vigente.

---

## 🔴 Prioridad A — deciden si la categoría es 5 o 4 (España y Alemania)

Estos son los **más importantes**: las categorías 5 de España y Alemania dependen de que la IA
aparezca **literalmente** en el texto vinculante. Si el término no está, esos países bajan a 4.

### España (→ `fuentes/ES/`)

| # | Documento | URL oficial | Formato | Qué verificar |
|---|---|---|---|---|
| A1 | **RD 217/2022** (enseñanzas mínimas ESO) — **Anexo II, «Tecnología y Digitalización»** | https://www.boe.es/buscar/pdf/2022/BOE-A-2022-4975-consolidado.pdf | PDF grande (~500 pp.) | ¿Aparece «inteligencia artificial» en los saberes básicos? ¿En qué curso? ¿obligatoria/optativa? |
| A2 | **RD 243/2022** (enseñanzas mínimas Bachillerato) — **«Tecnología e Ingeniería I/II»** | https://www.boe.es/buscar/pdf/2022/BOE-A-2022-5521-consolidado.pdf | PDF grande | Confirmar verbatim «inteligencia artificial» en los saberes básicos (la cita de Educagob apunta a que sí). |

### Alemania (→ `fuentes/DE/`)

| # | Documento | URL oficial | Formato | Qué verificar |
|---|---|---|---|---|
| A3 | **LehrplanPLUS Bayern — Gymnasium Jhst. 11, Informatik** (Lernbereich «Künstliche Intelligenz») | https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/11/informatik/ntg | HTML (PDF desde el portal) | ¿El *Lernbereich* «Künstliche Intelligenz» es **obligatorio** (Pflicht), no electivo? Texto exacto. |
| A4 | **Kernlehrplan Informatik Sek II — NRW** (Inhaltsfeld «KI und maschinelles Lernen») | https://lehrplannavigator.nrw.de/system/files/media/document/file/klp_gost_informatik.pdf | PDF | Confirmar verbatim que «Künstliche Intelligenz und maschinelles Lernen» es Inhaltsfeld obligatorio. |
| A5 | *(contexto)* **KMK — Handlungsempfehlung KI** (10.10.2024) | https://kmk.org/fileadmin/veroeffentlichungen_beschluesse/2024/2024_10_10-Handlungsempfehlung-KI.pdf | PDF (~30-40 pp.) | ¿Instruye a los Länder a incorporar IA en los Lehrpläne, o es solo orientación de uso? |

---

## 🟡 Prioridad B — confirman la categoría 4 (Portugal, Estonia, Singapur)

Menor riesgo (la categoría 4 es robusta), pero cierran la verificación verbatim y descartan IA
explícita oculta en el currículo.

### Portugal (→ `fuentes/PT/`)

| # | Documento | URL oficial | Formato | Qué verificar |
|---|---|---|---|---|
| B1 | **Aprendizagens Essenciais — Aplicações Informáticas B (12.º)** | https://www.dge.mec.pt/sites/default/files/Curriculo/Projeto_Autonomia_e_Flexibilidade/12_aplicacoes_informaticas_b.pdf | PDF | ¿Alguna mención a IA en el texto vigente (2018)? (esperado: no) |
| B2 | **Portaria n.º 226-A/2018** (matrices curriculares del secundário) | https://files.dre.pt/1s/2018/08/15101/0000200018.pdf | PDF | Confirmar qué disciplinas TIC hay y si son obligatorias u optativas. |

### Estonia (→ `fuentes/EE/`)

| # | Documento | URL oficial | Formato | Qué verificar |
|---|---|---|---|---|
| B3 | **National Curriculum for Upper Secondary Schools** (Gümnaasiumi riiklik õppekava, EN) — **Anexo de Informaatika** | https://www.riigiteataja.ee/en/eli/529042024001/consolide | HTML (texto completo + anexos) | Buscar «artificial intelligence / tehisintellekt» en el syllabus de Informática (esperado: no como contenido obligatorio). |
| B4 | *(opcional)* **National Curriculum for Basic Schools** (EN) | https://www.riigiteataja.ee/en/eli/ee/529042024002/consolide/current | HTML | Competencia digital transversal + posible IA en grados 7-9. |

### Singapur (→ `fuentes/SG/`)

| # | Documento | URL oficial | Formato | Qué verificar |
|---|---|---|---|---|
| B5 | **Computing Syllabus 7155 — O-Level 2025** (SEAB) | https://www.seab.gov.sg/files/O%20Lvl%20Syllabus%20Sch%20Cddts/2025/7155_y25_sy.pdf | PDF | ¿Hay un tema/módulo explícito de IA/Machine Learning, o solo una pregunta puntual? |
| B6 | **Computing G3 Teaching & Learning Syllabus 2024** (MOE) | https://www.moe.gov.sg/-/media/files/secondary/fsbb/syllabus/2024-g3-computing-teaching-and-learning-syllabus.pdf | PDF | Learning outcomes detallados: ¿IA/ML como contenido de enseñanza? |

---

## Estado de descargas

| País | Documentos aportados | Pendientes |
|---|---|---|
| PT | — | B1, B2 |
| ES | — | **A1, A2** |
| EE | — | B3 (, B4) |
| DE | — | **A3, A4**, A5 |
| SG | — | B5, B6 |

*(Se actualizará a medida que se commiteen los archivos a `fuentes/<país>/`.)*

---

### Resumen rápido si quieres priorizar al máximo

Con **4 PDFs** se cierra lo más sensible (las dos categorías 5):
**A1** (RD 217/2022, ES) · **A2** (RD 243/2022, ES) · **A3** (LehrplanPLUS Bayern 11, DE) ·
**A4** (Kernlehrplan NRW Sek II, DE).
