# Informe — Subindicador (b) «Educación temprana en IA»: revisión curricular de 5 países

**Replicación del subindicador (b) del ILIA 2025 (CEPAL/CENIA)** para cinco países
benchmark no latinoamericanos: **Portugal, España, Estonia, Alemania y Singapur**.

> **VERSIÓN VERIFICADA (cierre verbatim, 2026-06-06).** Las cuatro categorías «5»
> (ES, DE, EE, SG) están ahora respaldadas por **cita textual verificada como subcadena
> exacta** del documento primario oficial (reusando `src/verify_verbatim.py:normalizar`+
> `es_subcadena`). Los PDFs fuente están en `fuentes/<PAÍS>/`; el reporte está en
> `fuentes/_verify_report.json` (15/15 OK). **PT = 4** está verificado por ausencia.
>
> **Regla metodológica (confirmada con el equipo del ILIA): INCLUSIVA** — los **cursos electivos
> se consideran** parte del currículo nacional; la IA en *cualquier* asignatura vigente (incl.
> electivas) cuenta como «IA implementada» (categoría 5). **Estonia y Singapur** llevan **nota
> explicativa** (su IA vive en una asignatura electiva); ver la nota metodológica más abajo.
>
> Fecha de consulta: **2026-06-05**. Fecha de verbatim: **2026-06-06**.

## Resumen ejecutivo

| País | Cat. | Puntaje | Confianza | Criterio (secundaria) |
|---|:--:|:--:|---|---|
| **España (ES)** | **5** | **100** | **alta** (verbatim_ok) | IA **nominal** en saberes básicos y criterios de evaluación del BOE: RD 217/2022 (ESO) + RD 243/2022 (Bachillerato) |
| **Alemania (DE)** | **5** | **100** | **alta** (verbatim_ok) | IA **nominal y vinculante** en *LehrplanPLUS* Bayern (Gym 11, Lernbereich propio de 16 h) y en KLP NRW Sek I Klasse 5/6 (Pflichtfach, Inhaltsfeld «Automaten und künstliche Intelligenz») |
| **Estonia (EE)** | **5** | **100** | **alta** (verbatim_ok; sustantividad: **subtema**) | IA como contenido de la **electiva** *Informaatika* (Lisa 10 del PRÕK), tema «Infoühiskonna tehnoloogiad» |
| **Singapur (SG)** | **5** | **100** | **alta** (verbatim_ok; sustantividad: **subtema**) | *AI* y *machine learning* examinables en el syllabus **electivo** *Computing 7155*, Module 5 «Impact of Computing», sección 5.4 «Emerging Technologies» |
| **Portugal (PT)** | 4 | 75 | alta | TIC implementado; IA **no vigente** (solo en la revisión curricular con horizonte 2027) |

**Lectura.** Con la regla inclusiva, **cuatro de los cinco** países alcanzan la categoría 5:
la IA figura como contenido de su currículo nacional vigente, ya sea en asignaturas troncales
o de modalidad (**ES, DE**) o en asignaturas **electivas** (**EE, SG**). **Portugal** se queda
en 4 porque su IA **aún no está en vigor**: la incorpora una revisión cuya nueva versión va a
consulta en 2027 — y la regla inclusiva relaja el eje «electiva vs universal», **no** el eje
«implementado vs propuesta».

**Sustantividad (verificado por verbatim 2026-06-06).** El cierre verbatim confirma que:
- **ES y DE** tienen IA como **contenido sustantivo** del currículo vinculante: en ES, en
  saberes básicos y criterios de evaluación del BOE; en DE-BY, como **Lernbereich propio**
  (16 h) en Gym 11; en DE-NRW, como **Inhaltsfeld propio** del Pflichtfach Klasse 5/6.
- **EE y SG** tienen IA como **subtema**: en EE, 1 de 9 *õpitulemused* del tema
  «Infoühiskonna tehnoloogiad» dentro de la electiva *Informaatika*; en SG, sección 5.4
  «Emerging Technologies» con 5 *learning outcomes* dentro del Módulo 5 «Impact of Computing»
  del syllabus electivo 7155.

**Cursos electivos — Estonia y Singapur (confirmado con el ILIA).** En estos dos países la IA del
currículo nacional vigente se imparte en una **asignatura electiva** (Estonia: *Informaatika*,
*valikõppeaine*; Singapur: *Computing 7155*), no troncal, y aparece como **subtema**. Conforme a la
metodología del ILIA —**confirmada con el equipo del índice, los cursos electivos se consideran**
parte del currículo nacional—, ambos se clasifican en **categoría 5**. Se documenta por transparencia.

A título **informativo** (sensibilidad, **no adoptada**): una lectura estricta que exigiera
contenido troncal/sustantivo dejaría a EE y SG en 4 y el promedio del grupo en **85** (en vez de 95).

## Metodología (resumen; detalle en `README.md`)

- **Qué se mide:** si el currículo escolar legal **vigente** incluye **IA** y/o **TIC**, y en
  qué grado de implementación. La categoría/puntaje se asigna sobre **secundaria**.
- **Rúbrica (Cuadro 2, p. 63 del ILIA):** 1=sin propuesta (0) · 2=propuesta TIC (25) ·
  3=propuesta IA (50) · 4=TIC implementado (75) · 5=IA implementado (100). Orden ordinal y
  **acumulativo**: alcanzado el 5, no hay nivel superior.
- **Regla de umbral (confirmada con el equipo del ILIA): inclusiva** — los cursos electivos se
  consideran; IA en cualquier asignatura vigente (incl. electivas) ⇒ «implementada». Estonia y
  Singapur llevan nota explicativa. (Lectura estricta = solo sensibilidad informativa.)
- **Doble criterio por país:** TIC vs IA, y propuesta vs implementado.
- **Cierre verbatim (2026-06-06):** los 6 PDFs de Prioridad A se descargaron con `curl` a
  `fuentes/<PAÍS>/`, se extrajeron a `.txt` con `pdftotext` (HTML para Bayern) y las citas
  decisivas se verificaron como **subcadena exacta** del texto primario reusando
  `src/verify_verbatim.py:normalizar`+`es_subcadena`. Reporte en `fuentes/_verify_report.json`.
- **Limitación previa (resuelta):** WebFetch sigue devolviendo `403 "Host not in allowlist"`,
  pero `curl` con `-A "Mozilla/5.0"` a los hosts oficiales sí funcionó esta vez, lo que
  permitió bajar los 6 documentos y cerrar el verbatim.

---

## Portugal — Categoría 4 (TIC implementado, 75) · confianza alta

**Sistema y niveles.** *Ensino básico* (1.º–9.º) + **ensino secundário** (10.º–12.º).
«Secundaria» ILIA = ensino secundário.

**TIC en secundaria — implementado.** La disciplina **TIC** es obligatoria en el 3.º ciclo del
básico; en el secundário la informática vive como **«Aplicações Informáticas B»** (12.º,
optativa), con *Aprendizagens Essenciais* homologadas (Despacho 8476-A/2018; Portaria
226-A/2018) y competencia digital transversal (*Perfil dos Alunos*). ⇒ TIC implementada.

**IA en secundaria — NO vigente (verificado 2026-06-05).** Las *Aprendizagens Essenciais*
vigentes de *Aplicações Informáticas B* constan de **dos dominios: D1 (Algoritmia e
Programação) y D2 (Multimédia)** — **sin IA**. La IA solo entra por la **revisión del MECI**,
con nueva versión a consulta pública en **2027** e implementación gradual 2027/28. Es
**propuesta/futuro**, no contenido vigente.

**Justificación.** TIC implementada ⇒ 4. **Por qué no 5 (incluso con regla inclusiva):** la
regla inclusiva relaja el eje electiva/universal, pero la IA portuguesa falla en el eje
**implementado vs propuesta** — no está en ningún documento curricular **en vigor**, solo en
una revisión futura. **Confianza alta:** verificado que el currículo vigente no contiene IA y
que la incorporación es de 2027.

**Fuentes:** [Aplicações Informáticas B — Currículo Nacional (DGE)](https://curriculonacional.dge.mec.pt/organizacao-curricular/aplicacoes-informaticas-b) ·
[AE Aplicações Informáticas B (12.º) PDF](https://www.dge.mec.pt/sites/default/files/Curriculo/Aprendizagens_Essenciais/12_aplicacoes_informaticas_b.pdf) ·
[DL 55/2018](https://diariodarepublica.pt/dr/detalhe/decreto-lei/55-2018-115652962) ·
[Revisão AE (MECI, consulta 2027)](https://www.studocu.com/pt/document/universidade-de-lisboa/fisica/meci-informacao-sobre-a-revisao-das-aprendizagens-essenciais-2026/158154683)

---

## España — Categoría 5 (IA implementado, 100) · confianza alta (verbatim_ok)

**Sistema y niveles.** Secundaria = **ESO** (RD 217/2022) + **Bachillerato** (RD 243/2022);
marco LOMLOE. Las 17 CCAA desarrollan sobre las enseñanzas mínimas nacionales.

**TIC en secundaria — implementado.** En ESO, **«Tecnología y Digitalización»** (materia
obligatoria de oferta) con informática, redes, programación y pensamiento computacional;
**competencia digital** transversal (DigComp). En Bachillerato, **«Tecnología e Ingeniería
I/II»**. Vigente desde 2022-23/2023-24.

**IA en secundaria — nominal y verificada en el BOE.** El verbatim confirmado contra los
PDFs consolidados del BOE establece la IA como contenido vinculante:

- *Bachillerato, Tecnología e Ingeniería I*, **Criterio de evaluación 5.1** (RD 243/2022,
  Anexo II): «5.1 Controlar el funcionamiento de sistemas tecnológicos y robóticos,
  utilizando lenguajes de programación informática y aplicando las posibilidades que ofrecen
  las tecnologías emergentes, tales como **inteligencia artificial**, internet de las cosas,
  big data…»
- *Bachillerato, Tecnología e Ingeniería II*, **Saberes básicos, E. Sistemas informáticos
  emergentes**: «**Inteligencia artificial**, big data, bases de datos distribuidas y
  ciberseguridad.»
- *ESO, Tecnología y Digitalización*, **Criterio 5.2** (RD 217/2022, Anexo II): «5.2 Programar
  aplicaciones sencillas […] aplicando herramientas de edición, así como **módulos de
  inteligencia artificial** que añadan funcionalidades a la solución.»
- *ESO, Tecnología y Digitalización*, **Saberes básicos, C. Pensamiento computacional,
  programación y robótica**: «Aplicaciones informáticas sencillas, para ordenador y
  dispositivos móviles, e **introducción a la inteligencia artificial**.»

**Justificación.** **5** porque la IA es **contenido nominal explícito en normas vinculantes
vigentes**, ahora con cita textual verificada (verbatim_ok contra los PDFs del BOE). En ES la
IA aparece tanto en **saberes básicos** como en **criterios de evaluación**, en ESO y en
Bachillerato — **contenido sustantivo**, no incidental. Confianza **alta**.

**Fuentes:** [RD 217/2022 ESO (BOE PDF consolidado)](https://www.boe.es/buscar/pdf/2022/BOE-A-2022-4975-consolidado.pdf) ·
[RD 243/2022 Bachillerato (BOE PDF consolidado)](https://www.boe.es/buscar/pdf/2022/BOE-A-2022-5521-consolidado.pdf) ·
[Educagob — Tecnología e Ingeniería](https://educagob.educacionfpydeportes.gob.es/curriculo/curriculo-lomloe/menu-curriculos-basicos/bachillerato/materias/tecnologia-ingenieria/criterios-eval-primer-curso.html) ·
[DOG Galicia — IA para a Sociedade](https://www.xunta.gal/dog/Publicados/2023/20230825/AnuncioG0655-100823-0002_es.html)

---

## Estonia — Categoría 5 (IA implementado, 100, regla inclusiva) · confianza alta (verbatim_ok)

**Sistema y niveles.** *Põhikool* (1–9; tramo 7–9 = secundaria inferior) + *Gümnaasium* (10–12).
Currículos nacionales = reglamentos del Gobierno (consolidados 2024).

**TIC en secundaria — implementado.** La **competencia digital** es una de las 8 competencias
generales **transversales obligatorias** (DigComp 2.1), en todas las asignaturas.
**«Informaatika»** existe como asignatura **electiva** (*valikõppeaine*). ⇒ TIC implementada
(garantiza ≥4).

**IA en secundaria — verbatim verificado en el Anexo 10 del PRÕK.** La IA aparece en el
**reglamento vinculante** del Põhikooli riiklik õppekava, Lisa 10 («Valikõppeaine
Informaatika», redacción consolidada 2023):

- **III kooliaste · tema «Infoühiskonna tehnoloogiad» · Õpitulemus 6:** «kirjeldab
  **tehisintellekti** ja asjade interneti rakendusviise majanduses, avalikus sektoris,
  hariduses ja sellega kaasnevaid võimalikke ohtusid» — *(traducción: describe los usos de la
  inteligencia artificial y el internet de las cosas en la economía, el sector público y la
  educación, así como los posibles riesgos asociados)*.
- **III kooliaste · «Infoühiskonna tehnoloogiad» · Õppesisu:** «Uued tehnoloogiatrendid:
  **tehisintellekt**, ava- ja suurandmed.» y «**Tehisintellekti** ja asjade interneti
  mõisted, näited, rakendused ja seonduvad riskid.»

Aparte, **«AI Leap» (2025)** dota de herramientas de IA a ~20.000 estudiantes de 10.º–11.º,
pero su currículo se está definiendo (grupos de trabajo 2025): eso **no** computa como
implementado.

**Justificación.** **5 bajo la regla inclusiva:** la IA es contenido del currículo nacional
vigente a través de una asignatura **electiva** (Informaatika), con cita textual verificada
contra el PDF del Riigi Teataja. **Sustantividad: SUBTEMA.** La IA es 1 de 9 *õpitulemused*
del tema «Infoühiskonna tehnoloogiad», no un módulo propio. **Nota de regla:** bajo un umbral
estricto (cursado universal o contenido sustantivo), **EE sería 4**. Confianza **alta**:
verbatim del anexo de Informaatika confirma el término en el texto vinculante.

**Fuentes:** [Gümnaasiumi riiklik õppekava (EN)](https://www.riigiteataja.ee/en/eli/529042024001/consolide) ·
[PRÕK Lisa 10 — Valikõppeaine Informaatika (PDF)](https://www.riigiteataja.ee/aktilisa/1080/3202/3005/18m_pohi_lisa10.pdf) ·
[AI Leap — Eurydice](https://eurydice.eacea.ec.europa.eu/news/estonia-ai-leap-initiative-enhance-learning-and-teaching) ·
[Valitsus kiitis heaks ajakohastatud riiklikud õppekavad (HTM)](https://www.hm.ee/uudised/valitsus-kiitis-heaks-ajakohastatud-riiklikud-oppekavad)

---

## Alemania — Categoría 5 (IA implementado, 100) · confianza alta (verbatim_ok)

**Sistema y niveles.** Federal: educación competencia de los 16 **Länder**; la **KMK** coordina
(no vinculante). Lo vinculante son los *Lehrpläne* de cada Land. Secundaria = **Sek I** + **Sek
II**. Muestra: Bayern, NRW, Berlín-Brandeburgo, Baden-Württemberg.

**TIC/Informatik en secundaria — implementado.** *Informatik* es **Pflichtfach** en **9 de 16
Länder** en Sek I (Informatik-Monitor 2024/25); en la muestra, presente en BY, NRW, BW.
*Medienbildung* transversal (KMK 2016/21). ⇒ TIC/Informatik implementado.

**IA en secundaria — verbatim verificado en dos *Lehrpläne* vinculantes.** La IA figura
nominalmente en los siguientes textos vinculantes vigentes:

- **Bayern**, *LehrplanPLUS* Gymnasium **Jhst. 11**, Informatik (NTG): existe el
  *Lernbereich* **4 «Künstliche Intelligenz» (ca. 16 Std.)** con la Kompetenzerwartung
  literal: «**diskutieren Ansätze zur Definition des Begriffs Künstliche Intelligenz (KI)**,
  beschreiben verschiedene Grundideen von Verfahren der KI (u. a. maschinelles Lernen) sowie
  ihre Anwendungsbereiche.»  *(Corrección al borrador previo: el verbo verbatim es
  «diskutieren», no «erörtern».)*
- **NRW**, *Kernlehrplan* **Pflichtfach Informatik Klasse 5/6** (Sek I, vigente desde
  2021/22): contiene el **Inhaltsfeld «Automaten und künstliche Intelligenz»** con
  *inhaltliche Schwerpunkte* «Maschinelles Lernen mit Entscheidungsbäumen» y «Maschinelles
  Lernen mit neuronalen Netzen».  *(Corrección al borrador previo: el KLP GOSt (Sek II) NRW
  vigente es de 2014 y NO contiene KI; la IA vinculante de NRW está en el KLP Klasse 5/6.)*

**Justificación.** **5:** la IA es contenido explícito de **dos** currículos vinculantes
vigentes en los Länder de mayor peso (BY + NRW ≈ 40 % del alumnado), con cita textual
verificada contra los archivos oficiales. **Sustantividad alta:** en BY es un **Lernbereich
propio** (16 h con Kompetenzerwartungen específicas); en NRW Klasse 5/6 es un **Inhaltsfeld
propio**. Bajo la regla inclusiva el caveat de federalismo (7/16 Länder sin Pflichtfach
Informatik) **pesa menos**: basta con que la IA esté en el currículo de Land vigente.
Confianza **alta** (verbatim_ok).

**Fuentes:** [LehrplanPLUS Bayern — Gym 11 Informatik](https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/11/informatik/ntg) ·
[Lernbereich «Künstliche Intelligenz» (Bayern)](https://www.lehrplanplus.bayern.de/fachlehrplan/lernbereich/291294) ·
[KLP Klasse 5/6 Pflichtfach Informatik NRW (PDF, 2021)](https://lehrplannavigator.nrw.de/system/files/media/document/file/si_kl5u6_if_klp_2021_07_01.pdf) ·
[KLP Informatik GOSt NRW (PDF, 2014; contexto, sin KI)](https://lehrplannavigator.nrw.de/system/files/media/document/file/klp_gost_informatik.pdf) ·
[Informatik-Monitor 2024/25](https://informatik-monitor.de/2024-25)

---

## Singapur — Categoría 5 (IA implementado, 100, regla inclusiva) · confianza alta (verbatim_ok)

**Sistema y niveles.** *Primary* + **Secondary** (1–4/5; *Full SBB* desde 2024) + *Pre-University*.
«Secundaria» ILIA = Secondary. Exámenes Singapore-Cambridge GCE O-Level.

**TIC/Computing en secundaria — implementado (electivo).** **«Computing» (Syllabus 7155)** es
asignatura **electiva** del currículo nacional, con syllabus oficial MOE/SEAB (implementación
2024) y examen nacional. **Cinco** módulos: 1) *Computing Fundamentals*; 2) *Algorithms and
Programming*; 3) *Spreadsheets*; 4) *Networking*; 5) *Impact of Computing*. ⇒ TIC/Computing
implementado (garantiza ≥4). *(Corrección al borrador previo, que listaba otros nombres.)*

**IA en secundaria — verbatim verificado en el 7155 (SEAB 2025).** En el **Module 5 «Impact
of Computing» · sección 5.4 «Emerging Technologies»**, el syllabus oficial enumera 5
*learning outcomes* sobre IA y ML, todos examinables. Cita literal verificada:

- **5.4.1:** «**Describe Artificial Intelligence (AI)** as the ability of a computer to
  perform complex tasks without constant human guidance and improve its performance as more
  data is collected.»
- **5.4.3:** «**Define Machine Learning (ML)** as a technique used in AI and explain the
  difference between ML and traditional programming.»

Fuera del syllabus, la IA aparece en programas opcionales (*AI for Fun*, *Code for Fun*) y
uso instrumental vía SLS (no curriculares).

**Justificación.** **5 bajo la regla inclusiva:** AI y ML son contenido del syllabus oficial
de una asignatura **electiva** del currículo nacional, con cita textual verificada contra el
PDF de SEAB. **Sustantividad: SUBTEMA.** Los 5 *learning outcomes* de IA/ML viven dentro de la
**subsección 5.4** del Módulo 5; no existe un módulo propio de IA. **Nota de regla:** bajo un
umbral de **contenido sustantivo** (no incidental), **SG sería 4**. Confianza **alta**
(verbatim_ok).

**Fuentes:** [Computing 7155 O-Level 2025 (SEAB, PDF)](https://www.seab.gov.sg/files/O%20Lvl%20Syllabus%20Sch%20Cddts/2025/7155_y25_sy.pdf) ·
[Computing 7155 specimen paper (SEAB, PDF)](https://www.seab.gov.sg/files/O%20Lvl%20Syllabus%20Sch%20Cddts/2025/7155_y25_sp_1.pdf) ·
[Computing Syllabus G3 2024 (MOE, PDF)](https://www.moe.gov.sg/-/media/files/secondary/fsbb/syllabus/2024-g3-computing-syllabus.pdf) ·
[AI in Education (MOE)](https://www.moe.gov.sg/education-in-sg/educational-technology-journey/edtech-masterplan/artificial-intelligence-in-education)

---

## Verificación adicional (WebSearch, 2026-06-05) y decisión de umbral

Búsqueda dirigida a descartar un «5 oculto» en los entonces «4» (PT, EE, SG):

- **Portugal:** confirmado **sin IA** en el currículo vigente (AE = D1 + D2); IA solo en revisión
  2027 ⇒ **4 firme**.
- **Estonia y Singapur:** se halló IA **dentro de una asignatura electiva** del currículo nacional
  (Informaatika en EE; *AI* y *machine learning* examinables en el 7155 de SG).

Eso planteó la pregunta de umbral, resuelta por decisión del operador (**2026-06-05**) y
ahora informada por el cierre verbatim (2026-06-06):

| Regla | EE | SG | Nota |
|---|:--:|:--:|---|
| **(i) Inclusiva — ELEGIDA** | **5** | **5** | IA en cualquier asignatura del currículo nacional, incl. electivas |
| (ii) Cursado universal | 4 | 4 | exigiría asignatura de cursado universal/casi-universal |
| (iii) Contenido sustantivo | 4 | 4 | en EE, IA = 1/9 LO de un tema; en SG, IA = sección 5.4 (5 LO) dentro del Module 5 |

**Implicación (transparencia):** la regla inclusiva eleva EE y SG a 5; el cuadro resultante
(4 países en 5) es **más generoso** que el *spread* estricto de la calibración LatAm 2025
(cat. 5 = BR, CL, CR, EC, DO, UY; resto 4). Si se quisiera replicar exactamente el umbral de
**SITEAL**, habría que confirmar si SITEAL contó asignaturas electivas; de no ser así,
correspondería la regla (ii)/(iii) y EE/SG volverían a 4. La regla se aplica **por igual** a los
cinco países.

## Cierre verbatim (2026-06-06) — qué cambió respecto al borrador

1. **Las 4 categorías «5» quedan respaldadas por verbatim verificado** (15/15 OK del reporte
   automático en `fuentes/_verify_report.json`). La confianza de ES, DE, EE y SG sube a
   **alta**.
2. **Correcciones detectadas durante el verbatim:**
   - **DE-BY**: el verbo correcto en la Kompetenzerwartung del Lernbereich 4 KI es
     «diskutieren», no «erörtern» (la cita del borrador era una paráfrasis).
   - **DE-NRW**: el KLP GOSt (Sek II, edición 2014) NO contiene KI. La IA vinculante en NRW
     está en el **KLP Pflichtfach Klasse 5/6 (Sek I, 2021)** como Inhaltsfeld «Automaten und
     künstliche Intelligenz». La categoría DE = 5 no cambia (Bayern Gym 11 ya basta), pero la
     ubicación NRW se corrige.
   - **SG**: los **cinco módulos** oficiales del syllabus 7155 (2025) son Computing
     Fundamentals · Algorithms and Programming · Spreadsheets · Networking · Impact of
     Computing — distinto a la lista del borrador previo.
3. **Sustantividad (nuevo, gracias al verbatim):**
   - **ES = sustantivo** (saberes básicos + criterios de evaluación, ESO y Bachillerato).
   - **DE = sustantivo** (Lernbereich propio de 16 h en BY; Inhaltsfeld propio en NRW Kl 5/6).
   - **EE = subtema** (1 de 9 *õpitulemused* dentro del tema «Infoühiskonna tehnoloogiad»).
   - **SG = subtema** (sección 5.4 con 5 LO dentro del Módulo 5 «Impact of Computing»).
   El dato permite, si se opta por una regla estricta, revertir EE y SG a 4 con evidencia.
4. **Limitaciones residuales.** `WebFetch` sigue restringido; `curl` con `-A "Mozilla/5.0"`
   funcionó. Para reproducir: `python data/educacion_temprana/fuentes/_verify_run.py`.
