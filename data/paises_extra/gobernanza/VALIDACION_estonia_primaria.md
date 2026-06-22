# Validación de Estonia con texto primario (Valge raamat 2024-2030 + Tegevuskava 2024-2026)

**Fecha:** 2026-06-17 · **Documentos:** *Andmete ja tehisintellekti valge raamat 2024-2030* (White Paper, 56 pp;
MKM + Justiitsministeerium + HTM + Riigikantselei) y *Tehisintellekti tegevuskava 2024-2026* (Plan de Acción, 47 pp).
**Método:** extracción verbatim con PyMuPDF + búsqueda por subindicador. Quita el estado PRELIM de Estonia
(antes codificado sin el texto primario). Citas en estonio + glosa en español y nº de página.

URLs públicas de los documentos: White Paper `https://regulations.ai/regulations/RAI-EE-NA-DAIWPXX-2024` ·
Plan de Acción `https://regulations.ai/regulations/RAI-EE-NA-ADAPKXX-2024` · portal Kratid `https://www.kratid.ee/en/kratt-visioon`.

---

## 1. Cambios de puntaje (2) y corrección

| ID | Subindicador | Antes | Después | Motivo (texto primario) |
|---|---|---|---|---|
| **119** | Particip. ciudadana (elaboración) | 2 | **4** | En la elaboración del plan se hicieron **2 encuestas ómnibus con 2150 residentes** (actitudes/expectativas/temores; resultado "**77%** Eesti elanikest suhtub pigem positiivselt", VR p.44) + **220 *kaasamisintervjuud*** (PA p.6). Mecanismo con resultados publicados → 4 (defendible **5**: >1 mecanismo). |
| **121** | Multistakeholder (elaboración) | 3 (Gob+2) | **4** (Gob+3) | El "Kaasatud osapooled" enumera Gob + sector privado (ITL, empresas, consorcios, parques científicos) + academia (universidades) + sociedad civil (*vabaühendused*) → Gob+3. |

> **Corrección 2026-06-17 — Sostenibilidad (118) = 1, NO 0.** En una primera lectura bajé 118 a 0 por una **búsqueda incompleta** (faltaron los sinónimos estonios `säästev/säästva`, `energiasäästlik`, `rohejalajälg`, `kestlikkuse tööriist`). La búsqueda exhaustiva confirma que la sostenibilidad/medioambiente **sí se aborda con acciones** (ver §3) → **118 = 1**. Por tanto el **único cambio de la validación es 121 (3→4)**; 118 vuelve a 1, ahora **confirmado** con texto primario (antes era "1 BAJA").

## 2. Confirmaciones (sin cambio de puntaje; se quita PRELIM)

| ID | Subindicador | Puntaje | Evidencia primaria |
|---|---|---|---|
| 103 | Existencia | 3 | El Tegevuskava 2024-26 "on ühtlasi Eesti riiklik tehisintellekti strateegia" (p.4). |
| 104 | Antigüedad | 4 | Valge raamat **2024**-2030. |
| 105 | Actualización | 3 | 3ª generación (2019→2022→2024). |
| 106 | Mec. de evaluación | 3 | Sección "Tegevuste elluviimine ja seire": *juhtrühmad* (MKM) dirigen y monitorean; metas y *tulemusmõõdikud* en "Eesti digiühiskond 2030" (p.12, 22). |
| 107 | Presupuesto | 3 | "2019–2021 … eelarve … 10 miljonit eurot, 2022–2023 … 20 miljonit eurot" (Tegevuskava p.4) + €85 M anunciados 2024-26. |
| 108 | Hoja de ruta | 3 | Plan de Acción con *tegevused* por área (público, privado, T&A, lengua, derecho, HPC). || 122 | Multistakeholder (impl.) | 4 | *juhtrühmad* (MKM + asutused + "avaliku sektori välised võtmepartnerid", p.12). |
| 123 | Institucionalidad | 5 | Autoría: MKM + Justiitsministeerium + HTM + Riigikantselei (>1 institución). |
| 124 | Coordinación interinst. | 3 | *juhtrühmad* interinstitucionales liderados por MKM (p.12). |
| 128 | Iniciativa legal | 3 | EU AI Act; el AP es la estrategia nacional EE "EL kooskõlastatud tegevuskava mõistes" (p.4). |
| 129 | Clasificación de riesgo | 1 | "Algoritmi mõjuhinnangu mudeli … väljatöötamine ja juurutamine" (p.52) + AI Act. |
| 130 | Sandbox | 1 | **Sandbox nacional propio**: "Tehisintellekti liivakasti pakkumine era- ja avaliku sektori asutustele" (p.52) + sandbox EE-FI. |

## 3. Citas textuales — subindicadores de TÓPICOS (109-118)

> Regla del tópico (binaria): 0 = no recogido · 1 = recogido **+ plan de acción**.

| ID | Tópico | Puntaje | Cita verbatim (estonio) + pág. | Glosa (es) |
|---|---|---|---|---|
| 109 | Ética y gobernanza | 1 | "…oleksid fookuses **usaldusväärsus ja inimkesksus**" (VR p.6); §6.3 "**Usaldusväärse ja inimkeskse tehisintellekti** arendamine ja kasutamine"; PA §5.5 "Usaldusväärse TI ja **õigusruumi** suunalised tegevused". | Confiabilidad y centrado en la persona como foco; sección + acciones de IA confiable y marco jurídico. |
| 110 | Infraestructura y tecnología | 1 | PA §6 "**Kõrgjõudlusega andmetöötluse** suunalised tegevused" (HPC); VR p.22 "Tulevikukindla andmemajanduse ökosüsteemi tugevdamine: Arendada … 2027 aastaks … koos **taristuliste lahendustega**". | Cómputo de alto rendimiento (HPC) y ecosistema de datos con soluciones de infraestructura (acciones a 2027). |
| 111 | Desarrollo de capacidades | 1 | VR p.22 "**Koolitus ja haridus**: Jätkata andmehalduse, -teaduse, ruumiandmete ja IT-valdkonna **hariduse edendamist** hariduses ning õppes"; PA §3 (conocimientos/expertos). | Formación y educación en gestión/ciencia de datos e TI; área de acción. |
| 112 | Datos | 1 | VR §6.1 "**Andmehaldus**", "Andmete kättesaadavaks tegemine"; p.4 "**andmekvaliteedi** tagamine". | Gestión, calidad y apertura de datos = eje central del documento. |
| 113 | Gobierno digital | 1 | VR p.17 "**Bürokrati** kontseptsiooni elluviimine käimas ning Bürokratt on kasutusel juba **kaheksas asutuses**"; PA p.8 "Bürokrati MVP on valmis … kasutusel 8 kliendi juures, realiseeritud on 6 teenust". | Bürokratt (asistentes virtuales del Estado) operativo en 8 organismos; área de acción "sector público". |
| 114 | Industria y emprendimiento | 1 | VR p.6 "jätkuv innovatsioon ja **kasvav konkurentsivõime erasektoris**"; PA §2.5 "**Erasektori** suunalised tegevused". | Innovación y competitividad del sector privado; área de acción dedicada. |
| 115 | I+D | 1 | VR §6.1.4/§6.2.5 "**Teadus- ja arendustegevus**"; PA §3.9 "**Teadus- ja arendustegevuse** ning hariduse ja kompetentside suunalised tegevused". | I+D como línea de desarrollo con acciones. |
| 116 | Cooperación reg./int'l | 1 | VR §6.3.5 "**Rahvusvaheline koostöö**"; PA p.4 "…on ühtlasi Eesti riiklik tehisintellekti strateegia **Euroopa Liidu kooskõlastatud** tehisintellekti tegevuskava mõistes". | Cooperación internacional como sección; alineado al Plan Coordinado de la UE. |
| 117 | Perspectiva de género | **0** | VR p.30 "**soolist võrdsust mõõdetakse** naiste ja meeste osakaaluna…" (única mención de igualdad, como métrica). Barrido exhaustivo: **solo 5 coincidencias** de género en ambos PDF; "diskrimineerimine" es genérica (riesgo p.20; proyecto algorítmico EE-LT p.55, no de género). | Género solo como **variable de medición**; sin proyecto/cuota/presupuesto/campaña de género. Inclusión vía accesibilidad/*erivajadused* y territorio. → 0 (validado, coincide con la revisión externa). |
| 118 | Sostenibilidad | **1** | PA p.16-17 "…panustamist nn **energiasäästliku ehk «rohelise» TI** arendamisse, eeskätt arvutusefektiivsete meetodite arendamise teel"; VR p.43 "…panust … ning **säästva arengu eesmärke**" (IA del sector público alineada a ODS); VR p.38 "Näide 2 (**kestlikkuse tööriist**)"; PA p.17 "digilahendused, mis aitavad kaasa **kestlikkusele energeetikas, ehituses ja transpordis**"; VR p.13 "**Globaalse rohejalajälje** vähendamise kontekstis…". | IA verde/eficiente, alineación con ODS, herramienta de sostenibilidad, soluciones de energía/edificación/transporte y gestión "verde" de datos → recogido **+ acciones = 1**. |

## 4. Cita de elaboración multistakeholder (119/121/122)

> VR p.8: "Andmete ja tehisintellekti valge raamat on loodud koostöös erinevate osapooltega. Selle loomisse on panustanud
> **ministeeriumid ja riigiasutused, ettevõtted, erialaliidud, haridus- ja teadusasutused ning vabaühendused**."
>
> VR p.12 ("Kaasatud osapooled"): "…täiendasid ja tagasisidestasid kõik ministeeriumid ning põhilised partnerorganisatsioonid,
> sealhulgas **Eesti Infotehnoloogia ja Telekommunikatsiooni Liit, ülikoolid, eraettevõtted, … konsortsiumid, teaduspargid** ja paljud teised."

→ Elaboración: Gob + sector privado + academia + sociedad civil = **Gob+3 (121=4)**. No es consulta ciudadana abierta
con resultados publicados → **119=2**.

## 5. Pendientes de Estonia NO cubiertos por estos PDF (siguen igual)
- **125 ISO SC 42 = 0 (DUDA)**: requiere verificación en iso.org (no está en estos documentos).
- **133-137 GCI**, **138-139 GIRAI**, **144 NRI**: fuentes externas (UIT/GIRAI/Portulans), no la estrategia.
