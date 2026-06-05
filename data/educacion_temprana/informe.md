# Informe — Subindicador (b) «Educación temprana en IA»: revisión curricular de 5 países

**Replicación del subindicador (b) del ILIA 2025 (CEPAL/CENIA)** para cinco países
benchmark no latinoamericanos: **Portugal, España, Estonia, Alemania y Singapur**.

> **BORRADOR (vía híbrida).** Las categorías se derivan de investigación con buscador
> (WebSearch) porque el entorno de ejecución **bloquea la descarga directa** de los
> documentos oficiales (ver `README.md`). Quedan **pendientes de confirmación verbatim**
> contra los documentos primarios listados en `fuentes/MANIFEST.md`. Las asignaciones de
> **categoría 5 (España, Alemania)** son las más sensibles a esa verificación.
>
> Fecha de consulta: **2026-06-05**.

## Resumen ejecutivo

| País | Cat. | Puntaje | Confianza | Criterio decisivo (secundaria) |
|---|:--:|:--:|---|---|
| **España (ES)** | **5** | **100** | media-alta | IA **explícita** en saberes básicos de RD 217/2022 (ESO) y RD 243/2022 (Bachillerato) |
| **Alemania (DE)** | **5** | **100** | media-alta | IA **explícita y vinculante** en *LehrplanPLUS* Bayern (Gym. 11) y *Kernlehrplan* NRW (Sek II) |
| **Portugal (PT)** | 4 | 75 | alta | TIC implementado; IA **solo** en revisión curricular (horizonte 2027/28) |
| **Estonia (EE)** | 4 | 75 | media-alta | Competencia digital transversal obligatoria; IA **solo** en iniciativa *AI Leap* (no curricular) |
| **Singapur (SG)** | 4 | 75 | media-alta | *Computing* electiva implementada; IA **solo** en programas extracurriculares (*AI for Fun*) |

**Lectura.** Dos países alcanzan la categoría máxima (5 = «IA implementada») porque la IA
figura **con nombre propio en documentos curriculares vinculantes y vigentes**: España
(Reales Decretos de enseñanzas mínimas) y Alemania (currículos de los Länder de la
muestra). Los otros tres tienen **TIC/computación implementada** (categoría 4) pero la IA
aún vive fuera del currículo obligatorio: en Portugal es una **revisión en curso** (2027+),
en Estonia una **iniciativa de dotación de herramientas** (*AI Leap*), y en Singapur
**programas opcionales de enriquecimiento** y uso instrumental de herramientas.

La distinción operativa que separa 75 de 100 es siempre la misma: **«IA explícita y vigente
en el currículo obligatorio» (5) vs. «estrategia / plan / iniciativa / piloto no
curricular» (≤4)**. Mantener esa disciplina evita sobrepuntuar a sistemas con gran
reputación digital pero sin IA todavía en su currículo (caso Estonia).

## Metodología (resumen; detalle en `README.md`)

- **Qué se mide:** si el currículo escolar legal **vigente** incluye **IA** y/o **TIC**, y
  en qué grado de implementación. La categoría/puntaje se asigna sobre **secundaria**.
- **Rúbrica (Cuadro 2, p. 63 del ILIA):** 1=sin propuesta (0) · 2=propuesta TIC (25) ·
  3=propuesta IA (50) · 4=TIC implementado (75) · 5=IA implementado (100). Orden ordinal:
  `0 < 25 < 50 < 75 < 100`.
- **Doble criterio por país:** TIC vs IA, y propuesta vs implementado.
- **Disciplina heredada del repo:** «ningún número de memoria»; cada categoría se apoya en
  evidencia citada con URL. Las citas decisivas se verificarán como **subcadena exacta** del
  documento primario (lógica de `src/verify_verbatim.py`) cuando se disponga del texto.
- **Limitación de red (transparente):** `curl/wget` y `WebFetch` devuelven `403 "Host not
  in allowlist"` para todos los portales oficiales; solo **WebSearch** está disponible. Por
  eso varias citas son **snippets de buscador o de portales oficiales secundarios**, no aún
  el texto literal del boletín/decreto. Esto se cierra con la *shopping list*.

---

## Portugal — Categoría 4 (TIC implementado, 75) · confianza alta

**Sistema y niveles.** *Ensino básico* (1.º–9.º, tres ciclos) + **ensino secundário**
(10.º–12.º; cursos científico-humanísticos y profesionais). «Secundaria» ILIA = ensino
secundário.

**TIC en secundaria — implementado.** La disciplina **TIC** es obligatoria en el 3.º ciclo
del básico (7.º–8.º). En el secundário, la informática vive como **«Aplicações Informáticas
B»** (12.º ano, optativa en cursos científico-humanísticos), con *Aprendizagens Essenciais*
homologadas por el **Despacho n.º 8476-A/2018** y reguladas por la **Portaria 226-A/2018**.
La competencia digital es dimensión transversal del *Perfil dos Alunos*. ⇒ TIC implementada
en el currículo nacional vigente (disciplina regulada + transversal).

**IA en secundaria — no vigente (propuesta en curso).** Las *Aprendizagens Essenciais*
homologadas (2018, marco en vigor) **no** contienen IA. Toda la evidencia sitúa la IA en
**revisión**: el MECI abrió consulta pública (2026) de las AE «incorporando as dimensões do
digital e da Inteligência Artificial», con nueva versión prevista para **2027** e
implementación gradual desde **2027/28**. El *Plano de Ação 2025-2026 da Estratégia Digital*
plantea revisar *Educação Tecnológica* para incluir «tecnologias emergentes, nomeadamente de
Inteligência Artificial» — plan, no currículo. La guía ANPRI 2025 y la página DGE «IA e
Educação» son **orientaciones pedagógicas voluntarias**.

**Justificación.** TIC implementada (regulada y homologada) supera las categorías de
«propuesta». No alcanza la 5 porque ningún documento curricular homologado vigente del
secundário menciona IA como contenido obligatorio; la IA es una revisión con horizonte
2027/28. **Por qué no 3:** la TIC ya está implementada, no es mera propuesta. **Confianza
alta:** la evidencia (DGE, Diário da República, MECI) es consistente.

**Fuentes:** [DL 55/2018](https://diariodarepublica.pt/dr/detalhe/decreto-lei/55-2018-115652962) ·
[Portaria 226-A/2018](https://diariodarepublica.pt/dr/detalhe/portaria/226-a-2018-115941646) ·
[AE Ensino Secundário (DGE)](https://www.dge.mec.pt/aprendizagens-essenciais-ensino-secundario) ·
[AE Aplicações Informáticas B (12.º) PDF](https://www.dge.mec.pt/sites/default/files/Curriculo/Projeto_Autonomia_e_Flexibilidade/12_aplicacoes_informaticas_b.pdf) ·
[Revisão AE 2026 (MECI)](https://www.studocu.com/pt/document/universidade-de-lisboa/fisica/meci-informacao-sobre-a-revisao-das-aprendizagens-essenciais-2026/158154683) ·
[IA no ensino secundário (NoticiasLX, 2026)](https://noticiaslx.pt/2026/01/23/a-inteligencia-artificial-no-ensino-secundario/)

---

## España — Categoría 5 (IA implementado, 100) · confianza media-alta

**Sistema y niveles.** Secundaria = **ESO** (4 cursos, 12–16; RD 217/2022) + **Bachillerato**
(2 cursos, 16–18; RD 243/2022). Marco: **LOMLOE** (LO 3/2020). Las 17 CCAA desarrollan el
currículo sobre las enseñanzas mínimas nacionales.

**TIC en secundaria — implementado.** En ESO, **«Tecnología y Digitalización»** (RD 217/2022,
Anexo II) es materia obligatoria de oferta (cursarla en ≥1 de los tres primeros cursos), con
saberes de informática, redes, programación y pensamiento computacional; «Digitalización»
optativa en 4.º. La **Competencia Digital** es competencia clave transversal (perfil de
salida, DigComp). En Bachillerato, **«Tecnología e Ingeniería I/II»** (RD 243/2022, modalidad
Ciencias y Tecnología). Vigente desde 2022-23/2023-24.

**IA en secundaria — explícita en norma vigente.** La IA aparece **nominalmente** en los
saberes básicos de los Reales Decretos (no solo en la Estrategia Nacional de IA):

- *Bachillerato*, «Tecnología e Ingeniería» (portal oficial **Educagob**, Ministerio):
  «…utilizando **tecnologías emergentes incluyendo inteligencia artificial**, Big data e
  Internet de las Cosas» y, en 2.º, «inteligencia artificial, big data, bases de datos
  distribuidas y ciberseguridad».
- *ESO*, «Tecnología y Digitalización»: materiales LOMLOE alineados al RD 217/2022 describen
  «introducción a módulos de **inteligencia artificial**» (evidencia de portales docentes;
  **más débil** que la de Bachillerato, pendiente de confirmación en el Anexo II del BOE).
- *Galicia* añadió la optativa de 4.º ESO **«Intelixencia Artificial para a Sociedade»**
  (2023-24), por encima del mínimo nacional.

**Justificación.** Se asigna **5** porque la IA figura como **contenido nominal explícito en
normas vinculantes vigentes** (RD 217/2022 y RD 243/2022), no como mera TIC genérica ni
estrategia no curricular. **Reservas que bajan la confianza a media-alta:** (a) la cita más
sólida procede del portal **Educagob** (oficial) y de materiales docentes, **no aún del texto
literal del BOE**; (b) las materias con IA no son de cursado **universal** (oferta
obligatoria en ESO; modalidad en Bachillerato). La verificación verbatim del Anexo II de
ambos RD es **decisiva** para confirmar el 5 (si el texto legal no nombra «inteligencia
artificial», caería a 4).

**Fuentes:** [RD 217/2022 ESO (BOE)](https://www.boe.es/buscar/act.php?id=BOE-A-2022-4975) ·
[RD 243/2022 Bachillerato (BOE)](https://www.boe.es/buscar/act.php?id=BOE-A-2022-5521) ·
[Educagob — Tecnología e Ingeniería, criterios 1.er curso](https://educagob.educacionfpydeportes.gob.es/curriculo/curriculo-lomloe/menu-curriculos-basicos/bachillerato/materias/tecnologia-ingenieria/criterios-eval-primer-curso.html) ·
[Educagob — Tecnología y Digitalización ESO](https://educagob.educacionfpydeportes.gob.es/curriculo/curriculo-lomloe/menu-curriculos-basicos/ed-secundaria-obligatoria/materias/tecno-digitali/competencias-especificas.html) ·
[DOG Galicia — IA para a Sociedade (4.º ESO)](https://www.xunta.gal/dog/Publicados/2023/20230825/AnuncioG0655-100823-0002_es.html)

---

## Estonia — Categoría 4 (TIC implementado, 75) · confianza media-alta

**Sistema y niveles.** *Põhikool* (básica, grados 1–9; el tramo 7–9 = secundaria inferior) +
*Gümnaasium* (secundaria superior, 10–12). Currículos nacionales vinculantes = reglamentos
del Gobierno (consolidados en abril 2024).

**TIC en secundaria — implementado.** La **competencia digital** es una de las 8 competencias
generales **transversales obligatorias** del currículo nacional vigente (alineada a DigComp
2.1), desarrollada en todas las asignaturas. **«Informaatika»** existe en el marco curricular
como **optativa** (*valikkursus*: programación, ciberseguridad, servicios digitales…), cuya
inclusión depende del 25 % de libre configuración del centro. ⇒ TIC implementada (transversal
obligatoria + asignatura optativa reglada).

**IA en secundaria — no curricular (iniciativa).** No se halla «tehisintellekt / artificial
intelligence» como contenido obligatorio explícito del reglamento curricular vigente. La IA
se concentra en **«AI Leap» (TI-Hüpe, 2025)**, programa nacional que dota de herramientas de
IA (ChatGPT Edu, Gemini) a ~20.000 estudiantes de 10.º–11.º y forma docentes — *«…around
20,000 upper secondary students (grades 10–11) will gain access to AI-powered learning
applications»* (Eurydice). Es **dotación + formación, no reforma del currículo**; los grupos
de trabajo de competencias/contenidos empezaron en 2025 y enfrentaron retrasos legales.

**Justificación.** TIC implementada (transversal obligatoria) ⇒ categoría 4. **Por qué no 5:**
*AI Leap* es una iniciativa de herramientas, no IA explícita vigente en el currículo
obligatorio; equivale a «propuesta/iniciativa», no «implementado curricular». **Por qué no 3:**
la competencia digital transversal ya está implementada como obligatoria. **Confianza
media-alta:** la transversal obligatoria está bien documentada; la ausencia de IA en el texto
curricular se infiere de no aparecer en ninguna fuente primaria revisada (texto del reglamento
no accesible; posible enmienda de dic-2025 a verificar).

**Fuentes:** [Gümnaasiumi riiklik õppekava (EN, consolide 2024)](https://www.riigiteataja.ee/en/eli/529042024001/consolide) ·
[Põhikooli riiklik õppekava (EN, current)](https://www.riigiteataja.ee/en/eli/ee/529042024002/consolide/current) ·
[AI Leap — Eurydice](https://eurydice.eacea.ec.europa.eu/news/estonia-ai-leap-initiative-enhance-learning-and-teaching) ·
[TI-Hüpe (programa oficial)](https://tihupe.ee/en/) ·
[Retrasos legales del despliegue — Digital Watch](https://dig.watch/updates/legal-barriers-and-low-interest-delay-estonias-ai-rollout-in-schools)

---

## Alemania — Categoría 5 (IA implementado, 100) · confianza media-alta

**Sistema y niveles.** Federal: la educación es competencia de los 16 **Länder**; la **KMK**
coordina pero sus documentos **no son vinculantes**. Lo vinculante son los *Lehrpläne /
Kernlehrpläne / Bildungspläne* de cada Land. Secundaria = **Sek I** (5–9/10) + **Sek II**
(10/11–12/13). Muestra: Bayern, NRW, Berlín-Brandeburgo, Baden-Württemberg.

**TIC/Informatik en secundaria — implementado.** *Informatik* es **Pflichtfach** (obligatoria)
en **9 de 16 Länder** en Sek I (Informatik-Monitor 2024/25). En la muestra: **Bayern**
(integrada y diferenciada en Gymnasium/Mittelschule), **NRW** (Pflichtfach Kl. 5–6 desde
2021/22; Wahlpflicht 7–10), **Baden-Württemberg** (nuevo Pflichtfach «Informatik und
Medienbildung» desde 2025/26). *Medienbildung* es mandato transversal (estrategia KMK 2016/21).

**IA en secundaria — explícita y vinculante (muestra).** La IA figura **nominalmente en
currículos de Land con rango normativo**:

- **Bayern**, *LehrplanPLUS* Gymnasium **Jhst. 11**, *Lernbereich* **«Künstliche
  Intelligenz»**: los alumnos «*erörtern Ansätze zur Definition des Begriffs Künstliche
  Intelligenz, beschreiben verschiedene grundlegende Ideen von KI-Verfahren (u. a.
  maschinelles Lernen)…*» (con *Handreichung* del ISB).
- **NRW**, *Kernlehrplan* Informatik **Sek II**, *Inhaltsfeld* **«Künstliche Intelligenz und
  maschinelles Lernen»**: «*Maschinelles Lernen als Teilgebiet der Künstlichen Intelligenz…*».
- La recomendación KMK sobre IA (10.10.2024) es **orientación no vinculante** (no eleva por sí
  sola la categoría, pero contextualiza la dirección nacional).

**Justificación.** Se asigna **5** porque en los Länder de mayor peso de la muestra (Bayern +
NRW ≈ 40 % del alumnado) la IA es **contenido explícito de currículos vinculantes vigentes**
(Sek II), no estrategia ni anuncio. **Reservas (confianza media-alta):** (a) federalismo — 7
de 16 Länder aún sin Pflichtfach Informatik; (b) la evidencia de IA es más sólida en **Sek II**
que en Sek I; (c) no se pudo leer el texto literal de los *Lehrpläne*. La verificación verbatim
del *LehrplanPLUS* BY Jhst. 11 y del *KLP* NRW Sek II es **decisiva**.

**Fuentes:** [LehrplanPLUS Bayern — Gym 11 Informatik (NTG)](https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/11/informatik/ntg) ·
[Lernbereich «Künstliche Intelligenz» (Bayern)](https://www.lehrplanplus.bayern.de/fachlehrplan/lernbereich/291294) ·
[KLP Informatik Sek II NRW (PDF)](https://lehrplannavigator.nrw.de/system/files/media/document/file/klp_gost_informatik.pdf) ·
[KMK — Handlungsempfehlung KI (2024, PDF)](https://kmk.org/fileadmin/veroeffentlichungen_beschluesse/2024/2024_10_10-Handlungsempfehlung-KI.pdf) ·
[Informatik-Monitor 2024/25](https://informatik-monitor.de/2024-25)

---

## Singapur — Categoría 4 (TIC implementado, 75) · confianza media-alta

**Sistema y niveles.** *Primary* (1–6) + **Secondary** (1–4/5; sistema *Full SBB* desde 2024,
grupos G1/G2/G3) + *Pre-University* (JC). «Secundaria» ILIA = Secondary. Exámenes
Singapore-Cambridge GCE O-Level.

**TIC/Computing en secundaria — implementado (electivo).** **«Computing» (Syllabus 7155)** es
asignatura **electiva** del currículo nacional, con *syllabus* oficial MOE/SEAB (implementación
2024), examen nacional y ~1.300 alumnos G3 en 60 escuelas (se amplía a G1/G2 en 2026). Sus
cuatro módulos: *Data and Information; Systems and Communications; Abstraction and Algorithms;
Programming*. El *pensamiento computacional* es competencia del *EdTech Masterplan 2030*,
transversal vía programas. ⇒ TIC/Computing implementado (electivo, no universal).

**IA en secundaria — no curricular (programas/uso instrumental).** La IA **no** es contenido
obligatorio explícito del *syllabus* de secundaria. Aparece en: **«AI for Fun»** y **«Code for
Fun»** (IMDA-MOE, módulos opcionales de 10 h, adopción voluntaria por escuela); **uso
instrumental** de herramientas IA vía SLS; y la actualización 2026 de *Cyber Wellness* (CCE,
formación ciudadana). El MOE confirmó en el Parlamento (2023) que el conocimiento de IA se
desarrolla *«through coding programmes, the Science curriculum and through their facilitated
use of AI through assignments»* — es decir, **vía programas, no un syllabus obligatorio de IA**.

**Justificación.** *Computing* implementado ⇒ categoría 4. **Por qué no 5:** las iniciativas de
IA son opcionales/extracurriculares o uso instrumental, no contenido curricular obligatorio.
**Por qué no 3:** *Computing* ya está implementado. **Incertidumbre relevante:** el *specimen
paper* del 7155 sugiere alguna pregunta de *machine learning*; si el PDF del *syllabus*
confirmara un módulo de IA/ML sustantivo, reforzaría el componente IA — pero al ser *Computing*
**electiva**, no constituiría currículo **obligatorio universal**, por lo que se mantiene en 4.
**Confianza media-alta.**

**Fuentes:** [Computing Syllabus G3 2024 (MOE, PDF)](https://www.moe.gov.sg/-/media/files/secondary/fsbb/syllabus/2024-g3-computing-syllabus.pdf) ·
[Computing 7155 O-Level 2025 (SEAB, PDF)](https://www.seab.gov.sg/files/O%20Lvl%20Syllabus%20Sch%20Cddts/2025/7155_y25_sy.pdf) ·
[AI for Fun (IMDA)](https://www.imda.gov.sg/how-we-can-help/code-for-fun/ai-for-fun-secondary) ·
[AI in Education (MOE)](https://www.moe.gov.sg/education-in-sg/educational-technology-journey/edtech-masterplan/artificial-intelligence-in-education) ·
[Parliamentary Reply — AI (2023)](https://www.moe.gov.sg/news/parliamentary-replies/20230109-artificial-intelligence)

---

## Coherencia con la calibración LatAm 2025

En el ILIA 2025, categoría 5 = **Brasil, Chile, Costa Rica, Ecuador, Rep. Dominicana,
Uruguay**; el resto, categoría 4. El criterio que allí da el 5 es **IA implementada en el
currículo**. Aplicado a los 5 benchmark:

- **ES y DE en 5** es coherente: ambos tienen IA **nominal en documentos curriculares
  vinculantes vigentes** (no solo estrategias).
- **PT, EE, SG en 4** es coherente y disciplinado: tienen TIC/computación implementada pero la
  IA está en **revisión (PT)**, **iniciativa (EE)** o **programas opcionales (SG)** — el mismo
  estándar «implementado vs propuesta» que separa el 4 del 5 en LatAm.

El riesgo de sobrepuntuar por reputación (Estonia, Singapur) se ha evitado exigiendo IA en el
**currículo obligatorio vigente**, no en su ecosistema de innovación.

## Limitaciones y próximos pasos (cierre verbatim)

1. **Citas no verbatim aún.** Varias evidencias son *snippets* de buscador o de portales
   oficiales secundarios (p. ej. Educagob, ISB, Eurydice), no el texto literal del
   boletín/decreto/Lehrplan. Se marcan como `pendiente_verbatim` en `evidencias/evidencias.json`.
2. **Las categorías 5 (ES, DE) son las más sensibles.** Dependen de que la IA aparezca
   **literalmente** en el texto vinculante (Anexo II de RD 217/2022 y RD 243/2022; *LehrplanPLUS*
   BY Jhst. 11 y *KLP* NRW Sek II). La *shopping list* (`fuentes/MANIFEST.md`) prioriza esos
   documentos: si se confirma el término, el 5 queda firme; si no, caería a 4.
3. **Cierre:** con los documentos primarios aportados a `fuentes/<pais>/`, se hará la
   extracción con cita textual + traducción y la **verificación verbatim** (subcadena exacta),
   y se elevará la confianza a «alta» o se ajustará la categoría según la evidencia.
