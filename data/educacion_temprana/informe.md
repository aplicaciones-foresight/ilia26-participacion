# Informe — Subindicador (b) «Educación temprana en IA»: revisión curricular de 5 países

**Replicación del subindicador (b) del ILIA 2025 (CEPAL/CENIA)** para cinco países
benchmark no latinoamericanos: **Portugal, España, Estonia, Alemania y Singapur**.

> **BORRADOR (vía híbrida).** Las categorías se derivan de investigación con buscador
> (WebSearch) porque el entorno de ejecución **bloquea la descarga directa** de los
> documentos oficiales (ver `README.md`). Quedan **pendientes de confirmación/justificación
> verbatim** contra los documentos primarios listados en `fuentes/MANIFEST.md`.
>
> **Decisión metodológica fijada (2026-06-05): regla INCLUSIVA** — la IA presente en
> *cualquier* asignatura del currículo nacional vigente, **incluidas las electivas**, cuenta
> como «IA implementada» (categoría 5). Ver la sección de verificación.
>
> Fecha de consulta: **2026-06-05**.

## Resumen ejecutivo

| País | Cat. | Puntaje | Confianza | Criterio (secundaria) |
|---|:--:|:--:|---|---|
| **España (ES)** | **5** | **100** | media-alta | IA **explícita** en saberes básicos de RD 217/2022 (ESO) y RD 243/2022 (Bachillerato) |
| **Alemania (DE)** | **5** | **100** | media-alta | IA **explícita y vinculante** en *LehrplanPLUS* Bayern (Gym. 11) y *Kernlehrplan* NRW (Sek II) |
| **Estonia (EE)** | **5** | **100** | media | IA como contenido de la asignatura **electiva** *Informaatika* (regla inclusiva) |
| **Singapur (SG)** | **5** | **100** | media | *Machine learning* examinable en el syllabus **electivo** *Computing 7155* (regla inclusiva) |
| **Portugal (PT)** | 4 | 75 | alta | TIC implementado; IA **no vigente** (solo en la revisión curricular con horizonte 2027) |

**Lectura.** Con la regla inclusiva, **cuatro de los cinco** países alcanzan la categoría 5:
la IA figura como contenido de su currículo nacional vigente, ya sea en asignaturas troncales
o de modalidad (**ES, DE**) o en asignaturas **electivas** (**EE, SG**). **Portugal** se queda
en 4 porque su IA **aún no está en vigor**: la incorpora una revisión cuya nueva versión va a
consulta en 2027 — y la regla inclusiva relaja el eje «electiva vs universal», **no** el eje
«implementado vs propuesta».

Conviene tener presente que la regla inclusiva es **generosa**: produce más «5» que una lectura
estricta. Bajo reglas alternativas (IA solo en asignatura de cursado universal, o IA como
contenido **sustantivo** y no incidental), **EE y SG volverían a 4** (en SG, *machine learning*
es un subtema, no un módulo). La elección se registra abajo y debe aplicarse por igual a los
cinco para que el benchmark sea coherente.

## Metodología (resumen; detalle en `README.md`)

- **Qué se mide:** si el currículo escolar legal **vigente** incluye **IA** y/o **TIC**, y en
  qué grado de implementación. La categoría/puntaje se asigna sobre **secundaria**.
- **Rúbrica (Cuadro 2, p. 63 del ILIA):** 1=sin propuesta (0) · 2=propuesta TIC (25) ·
  3=propuesta IA (50) · 4=TIC implementado (75) · 5=IA implementado (100). Orden ordinal y
  **acumulativo**: alcanzado el 5, no hay nivel superior.
- **Decisión de umbral (2026-06-05): regla inclusiva** — IA en cualquier asignatura del
  currículo nacional vigente, incl. electivas, ⇒ «implementada». (Documentado para
  reproducibilidad; alternativas estrictas anotadas en cada país.)
- **Doble criterio por país:** TIC vs IA, y propuesta vs implementado.
- **Disciplina heredada del repo:** «ningún número de memoria»; cada categoría se apoya en
  evidencia citada con URL. Las citas decisivas se verificarán como **subcadena exacta** del
  documento primario (lógica de `src/verify_verbatim.py`) cuando se disponga del texto.
- **Limitación de red (transparente):** `curl/wget` y `WebFetch` devuelven `403 "Host not in
  allowlist"`; solo **WebSearch** está disponible. Por eso varias citas son *snippets* de
  buscador o de portales oficiales secundarios, no aún el texto literal del boletín/decreto.

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

## España — Categoría 5 (IA implementado, 100) · confianza media-alta

**Sistema y niveles.** Secundaria = **ESO** (RD 217/2022) + **Bachillerato** (RD 243/2022);
marco LOMLOE. Las 17 CCAA desarrollan sobre las enseñanzas mínimas nacionales.

**TIC en secundaria — implementado.** En ESO, **«Tecnología y Digitalización»** (materia
obligatoria de oferta) con informática, redes, programación y pensamiento computacional;
**competencia digital** transversal (DigComp). En Bachillerato, **«Tecnología e Ingeniería
I/II»**. Vigente desde 2022-23/2023-24.

**IA en secundaria — explícita en norma vigente.** La IA aparece **nominalmente** en los
saberes básicos de los RD (no solo en la Estrategia Nacional de IA):

- *Bachillerato*, «Tecnología e Ingeniería» (portal oficial **Educagob**): «…utilizando
  **tecnologías emergentes incluyendo inteligencia artificial**, Big data e Internet de las
  Cosas».
- *ESO*, «Tecnología y Digitalización»: materiales LOMLOE describen «introducción a módulos de
  **inteligencia artificial**» (evidencia más débil, pendiente de confirmar en el Anexo II del
  BOE).
- *Galicia*: optativa de 4.º ESO **«Intelixencia Artificial para a Sociedade»** (2023-24).

**Justificación.** **5** porque la IA es **contenido nominal explícito en normas vinculantes
vigentes**. Confianza **media-alta**: la cita más sólida procede de **Educagob** (oficial) y de
materiales docentes, **no aún del BOE literal**. La verificación verbatim del Anexo II de RD
217/2022 y RD 243/2022 **fija/justifica** el 5 (extracción de la cita; ya no decide categoría).

**Fuentes:** [RD 217/2022 ESO (BOE)](https://www.boe.es/buscar/act.php?id=BOE-A-2022-4975) ·
[RD 243/2022 Bachillerato (BOE)](https://www.boe.es/buscar/act.php?id=BOE-A-2022-5521) ·
[Educagob — Tecnología e Ingeniería](https://educagob.educacionfpydeportes.gob.es/curriculo/curriculo-lomloe/menu-curriculos-basicos/bachillerato/materias/tecnologia-ingenieria/criterios-eval-primer-curso.html) ·
[DOG Galicia — IA para a Sociedade](https://www.xunta.gal/dog/Publicados/2023/20230825/AnuncioG0655-100823-0002_es.html)

---

## Estonia — Categoría 5 (IA implementado, 100, regla inclusiva) · confianza media

**Sistema y niveles.** *Põhikool* (1–9; tramo 7–9 = secundaria inferior) + *Gümnaasium* (10–12).
Currículos nacionales = reglamentos del Gobierno (consolidados 2024).

**TIC en secundaria — implementado.** La **competencia digital** es una de las 8 competencias
generales **transversales obligatorias** (DigComp 2.1), en todas las asignaturas.
**«Informaatika»** existe como asignatura **electiva** (*valikõppeaine*). ⇒ TIC implementada
(garantiza ≥4).

**IA en secundaria — contenido del currículo electivo (verificado 2026-06-05).** La IA se
trata como «conceptos, ejemplos, aplicaciones y riesgos» **dentro de la asignatura electiva de
Informaatika**, que forma parte del currículo nacional. Aparte, **«AI Leap» (2025)** dota de
herramientas de IA a ~20.000 estudiantes de 10.º–11.º, pero su **currículo se está definiendo**
(grupos de trabajo 2025): eso **no** computa como implementado.

**Justificación.** **5 bajo la regla inclusiva:** la IA es contenido del currículo nacional
vigente a través de una asignatura **electiva** (Informaatika). **Confianza media:** la
evidencia distingue de forma imprecisa entre el **texto vinculante** del anexo de Informaatika
(*Lisa*) y los **materiales de apoyo**; *AI Leap* no se computa (en desarrollo). **Nota de
regla:** bajo un umbral estricto (cursado universal o contenido sustantivo), **EE sería 4**. La
verificación verbatim del anexo de Informaatika confirmaría el término en el texto vinculante.

**Fuentes:** [Gümnaasiumi riiklik õppekava (EN)](https://www.riigiteataja.ee/en/eli/529042024001/consolide) ·
[PRÕK Lisa — Valikõppeaine Informaatika (PDF)](https://www.riigiteataja.ee/aktilisa/1080/3202/3005/18m_pohi_lisa10.pdf) ·
[AI Leap — Eurydice](https://eurydice.eacea.ec.europa.eu/news/estonia-ai-leap-initiative-enhance-learning-and-teaching) ·
[Valitsus kiitis heaks ajakohastatud riiklikud õppekavad (HTM)](https://www.hm.ee/uudised/valitsus-kiitis-heaks-ajakohastatud-riiklikud-oppekavad)

---

## Alemania — Categoría 5 (IA implementado, 100) · confianza media-alta

**Sistema y niveles.** Federal: educación competencia de los 16 **Länder**; la **KMK** coordina
(no vinculante). Lo vinculante son los *Lehrpläne* de cada Land. Secundaria = **Sek I** + **Sek
II**. Muestra: Bayern, NRW, Berlín-Brandeburgo, Baden-Württemberg.

**TIC/Informatik en secundaria — implementado.** *Informatik* es **Pflichtfach** en **9 de 16
Länder** en Sek I (Informatik-Monitor 2024/25); en la muestra, presente en BY, NRW, BW.
*Medienbildung* transversal (KMK 2016/21). ⇒ TIC/Informatik implementado.

**IA en secundaria — explícita y vinculante.** La IA figura **nominalmente en currículos de
Land con rango normativo**:

- **Bayern**, *LehrplanPLUS* Gymnasium **Jhst. 11**, *Lernbereich* **«Künstliche
  Intelligenz»**: «*erörtern Ansätze zur Definition des Begriffs Künstliche Intelligenz…*».
- **NRW**, *Kernlehrplan* Informatik **Sek II**, *Inhaltsfeld* **«Künstliche Intelligenz und
  maschinelles Lernen»**: «*Maschinelles Lernen als Teilgebiet der Künstlichen Intelligenz…*».

**Justificación.** **5:** la IA es contenido explícito de currículos vinculantes vigentes en los
Länder de mayor peso (BY + NRW ≈ 40 % del alumnado). Bajo la **regla inclusiva**, el caveat de
federalismo (7/16 Länder sin Pflichtfach Informatik) **pesa menos**: basta con que la IA esté en
el currículo de Land vigente. **Confianza media-alta:** evidencia más sólida en **Sek II**; no se
pudo leer el texto literal. Verbatim del *LehrplanPLUS* BY 11 y del *KLP* NRW Sek II justifica el 5.

**Fuentes:** [LehrplanPLUS Bayern — Gym 11 Informatik](https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/11/informatik/ntg) ·
[Lernbereich «Künstliche Intelligenz» (Bayern)](https://www.lehrplanplus.bayern.de/fachlehrplan/lernbereich/291294) ·
[KLP Informatik Sek II NRW (PDF)](https://lehrplannavigator.nrw.de/system/files/media/document/file/klp_gost_informatik.pdf) ·
[Informatik-Monitor 2024/25](https://informatik-monitor.de/2024-25)

---

## Singapur — Categoría 5 (IA implementado, 100, regla inclusiva) · confianza media

**Sistema y niveles.** *Primary* + **Secondary** (1–4/5; *Full SBB* desde 2024) + *Pre-University*.
«Secundaria» ILIA = Secondary. Exámenes Singapore-Cambridge GCE O-Level.

**TIC/Computing en secundaria — implementado (electivo).** **«Computing» (Syllabus 7155)** es
asignatura **electiva** del currículo nacional, con syllabus oficial MOE/SEAB (implementación
2024) y examen nacional. Cuatro módulos: *Data and Information; Systems and Communications;
Abstraction and Algorithms; Programming*. ⇒ TIC/Computing implementado (garantiza ≥4).

**IA en secundaria — contenido examinable del syllabus electivo (verificado 2026-06-05).**
**Machine learning** está incluido y es **examinable** en el syllabus 7155 (specimen paper:
«*explain how a machine learning system will be different from traditional programming*»). Fuera
del syllabus, la IA aparece en programas opcionales (*AI for Fun*, *Code for Fun*) y uso
instrumental vía SLS (no curriculares).

**Justificación.** **5 bajo la regla inclusiva:** ML es contenido del syllabus oficial de una
asignatura **electiva** del currículo nacional. **Confianza media:** ML figura como **subtema**,
no como módulo propio (los 4 módulos no incluyen un bloque de IA). **Nota de regla:** bajo un
umbral de **contenido sustantivo** (no incidental), **SG sería 4**. La verificación verbatim del
7155 fija la profundidad exacta del contenido de IA/ML.

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
  (Informaatika en EE; *machine learning* examinable en el 7155 de SG).

Eso planteó la pregunta de umbral, resuelta por decisión del operador (**2026-06-05**):

| Regla | EE | SG | Nota |
|---|:--:|:--:|---|
| **(i) Inclusiva — ELEGIDA** | **5** | **5** | IA en cualquier asignatura del currículo nacional, incl. electivas |
| (ii) Cursado universal | 4 | 4 | exigiría asignatura de cursado universal/casi-universal |
| (iii) Contenido sustantivo | 4 | 4 | en SG, ML es subtema, no módulo |

**Implicación (transparencia):** la regla inclusiva eleva EE y SG a 5; el cuadro resultante
(4 países en 5) es **más generoso** que el *spread* estricto de la calibración LatAm 2025
(cat. 5 = BR, CL, CR, EC, DO, UY; resto 4). Si se quisiera replicar exactamente el umbral de
**SITEAL**, habría que confirmar si SITEAL contó asignaturas electivas; de no ser así,
correspondería la regla (ii)/(iii) y EE/SG volverían a 4. La regla se aplica **por igual** a los
cinco países.

## Limitaciones y próximos pasos (cierre verbatim)

1. **Citas no verbatim aún.** Varias evidencias son *snippets* de buscador o de portales
   oficiales secundarios (Educagob, ISB, Eurydice…), no el texto literal del documento. Se marcan
   `pendiente_verbatim`/`websearch_2026-06-05` en `evidencias/evidencias.json`.
2. **Lógica acumulativa:** los **cuatro «5» (ES, DE, EE, SG)** están cerrados en categoría; solo
   falta **extraer y verificar la cita** que cada uno usa para justificar el 5 (no cambia la
   categoría). **PT=4** está verificado.
3. **Documentos para el verbatim** (en `fuentes/MANIFEST.md`): ES (RD 217/2022, RD 243/2022),
   DE (*LehrplanPLUS* BY 11, *KLP* NRW Sek II), EE (anexo de Informaatika), SG (syllabus 7155).
   Para **EE y SG**, el verbatim además mide la **sustantividad** del contenido de IA: si se optara
   por una regla estricta, ese dato permitiría revertir a 4 con evidencia.
