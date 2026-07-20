# HANDOFF PARA REDACCIÓN DEL REPORTE — Indicador de IA en Participación Ciudadana · ILIA 2026
## Cambios metodológicos 2025 → 2026, criterios de elegibilidad y dinámica de la base de casos

**Para:** la sesión de Claude que redactará el capítulo/reporte del indicador.
**Fecha de corte:** 2026-07-20 · **Origen:** pipeline ILIA 2026, repo `aplicaciones-foresight/ilia26-participacion`, rama `claude/validated-excluded-cases-sheets-lohg7e`.
**Respaldo de cada número:** `BBDD_casos_incluidos_ILIA2026.xlsx` (base 2026 + índice con fórmulas auditables + metodología en su pestaña 3), `Casos_excluidos_ILIA2026.xlsx` (los 80 excluidos con origen y motivo), `Comparacion_2025_2026_ILIA.xlsx` (2025 con ambas fórmulas vs 2026, con gráficos). Todos los valores de este documento fueron verificados por recomputación independiente y QA externo.

---

## 1 · Qué mide el indicador y qué NO cambió

El **Indicador de IA en Participación Ciudadana** mide, para 20 países de América Latina y el Caribe (AR, BO, BR, CL, CO, CR, CU, DO, EC, GT, HN, JM, MX, PA, PE, PY, SV, TT, UY, VE), el uso y desarrollo de inteligencia artificial dentro de **procesos reales de participación ciudadana**. Estructura estable entre ciclos:

- **Indicador = (Sub-Indicador de Uso + Sub-Indicador de Desarrollo) ÷ 2**, escala 0-100.
- **Sub2 · Desarrollo de IA: SIN CAMBIOS 2025→2026** (decisión explícita de comparabilidad). Promedio de: (a) V-Desarrollador = amplitud de tipos de desarrollador (Privado, Academia, Gobierno, Sociedad Civil) con origen Nacional y con origen Internacional, cada una normalizada por el máximo relativo entre países; (b) V-Tipos de IA = nº de sistemas/familias de IA distintos ÷ máximo relativo.
- Redondeo de publicación: igual que 2025 (Sub1 y Sub2 a enteros, luego el promedio a entero).
- La unidad de análisis sigue siendo el **caso/iniciativa** (1 fila = 1 iniciativa; despliegues múltiples de la misma iniciativa no se cuentan dos veces).

Lo que cambió es (i) la **fórmula del Sub-Indicador de Uso** (de 4 a 5 variables, con dos variables rediseñadas), (ii) el **criterio de elegibilidad** de casos, y (iii) el **estándar de evidencia** del proceso de construcción de la base. TT (Trinidad y Tobago) se incorporó al universo en 2026 (en 2025 no tenía baseline); quedó con 0 casos.

---

## 2 · Cambios de FÓRMULA en el Sub-Indicador de Uso (metodología CENIA v2, jun-2026)

| Variable | 2025 (fórmula antigua) | 2026 (CENIA v2) | Cambio |
|---|---|---|---|
| Tipos de proceso | nº de tipos distintos ÷ 5 | igual | sin cambio |
| Etapas de uso | nº de etapas distintas ÷ 4 | igual | sin cambio de fórmula; codificación refinada |
| Continuidad | nº de **modalidades** presentes {Uso único, Plataforma} ÷ 2 | **nivel MÁXIMO de consolidación** (0-3) ÷ 3, con **caducidad de anuncios** | rediseñada |
| Organización | nº de **tipos de organización** {Público, Privado, Mixto} ÷ 3 | **Organización Convocante**: 3 subcomponentes con taxonomía de 7 categorías (incluye co-convocatoria) | rediseñada |
| Cantidad de iniciativas | — (no existía) | nº de iniciativas elegibles → umbrales 0/25/50/75/100 | **nueva** |
| Agregación Sub1 | promedio simple de 4 | promedio simple de 5 | — |

### 2.1 Continuidad: de «modalidades» a «nivel máximo de consolidación»

- **Antes:** el país sumaba por tener casos de «Uso único» y casos de «Plataforma» (÷2). Un país con un solo caso puntual quedaba en 50; tener ambas modalidades — un hecho más bien compositivo que de mérito — daba 100.
- **Ahora:** escala ordinal de consolidación por caso (0 = sin señal · 1 = anuncio · 2 = uso puntual/implementado · 3 = permanente o recurrente) y el país puntúa por su **nivel máximo verificado** ÷ 3. Además, un **anuncio caduca a los 2 años sin implementación** (pasa a 0; año de referencia 2026).
- **Justificación:** la variable ahora mide lo que pretende medir — cuán consolidado está el uso de IA en participación — en lugar de premiar diversidad de formatos. La caducidad impide que anuncios antiguos jamás implementados sostengan puntaje indefinidamente, y el nivel 3 exige evidencia de recurrencia (no se asigna por defecto).

### 2.2 Organización: de «Público/Privado» a «Organización Convocante» con co-convocatoria

- **Antes:** tricotomía gruesa del titular del caso (Público/Privado/Mixto ÷ 3), donde «Mixto» era una categoría ambigua que además solapaba con las otras dos.
- **Ahora:** taxonomía de **7 categorías de convocante** — 3 gubernamentales (gobierno local · gobierno nacional · otra institución pública) y 4 no gubernamentales (empresa · universidad · sociedad civil · organización internacional) — combinadas en **3 subcomponentes co-iguales**: (a) amplitud gubernamental ÷ 3; (b) amplitud no gubernamental ÷ 4; (c) **co-convocatoria** = nº de combinaciones distintas de ≥2 tipos que co-convocan una misma iniciativa ÷ máximo relativo del ciclo. Se registran **todos** los convocantes de cada iniciativa, no solo el principal. Regla de codificación: universidades públicas cuentan como «Universidad» (no gubernamental), no como «otra institución pública».
- **Justificación:** mide la amplitud real del ecosistema que convoca procesos participativos con IA y premia la **colaboración multi-actor** (alianzas gobierno-academia-sociedad civil), que la tricotomía anterior no podía ver. Elimina la ambigüedad de «Mixto» convirtiéndola en información útil (la combinación concreta).

### 2.3 Cantidad de iniciativas (variable NUEVA)

- nº de iniciativas elegibles del país → 0 casos = 0 · 1-3 = 25 · 4-6 = 50 · 7-9 = 75 · 10+ = 100.
- **Justificación:** con 4 variables de amplitud, un país con 1 caso bien diversificado podía puntuar como uno con 9; el volumen de iniciativas elegibles es una señal directa de adopción que faltaba en la fórmula. Los umbrales por tramos evitan que el conteo bruto domine el subindicador. Los duplicados no suman (regla «Cuenta como iniciativa»).

### 2.4 Refinamientos de codificación (misma fórmula, criterio más exigente)

- **Etapa «Análisis»** solo se codifica si hubo **procesamiento posterior real** de los aportes (no basta recolectarlos).
- Distinción reforzada entre **organización a cargo** (convocante) y **desarrollador** de la IA (alimentan variables distintas).
- **Rol de la IA** codificado por caso (contenido / apoyo-logística / no claro) con evidencia textual.

### 2.5 Máximos relativos: implicación de lectura (importante para el reporte)

Tres normalizaciones usan el **máximo entre países del ciclo** (co-convocatoria, desarrolladores nacional/internacional, sistemas de IA), recalculado en cada corrida. Los máximos subieron con fuerza en 2026 (BR y CL elevaron el listón):

| Máximo relativo | ciclo 2025 | ciclo 2026 |
|---|---|---|
| Combinaciones de co-convocatoria | 2 | 2 (CL y CO) |
| Tipos de desarrollador nacionales | 3 | 4 (BR) |
| Tipos de desarrollador internacionales | 2 | 3 (BR) |
| Sistemas de IA distintos | 5 | 11 (BR y CL) |

**Consecuencia:** un país puede mantener su desempeño absoluto y aun así bajar en Sub2, porque el denominador creció (p. ej., CO conserva 5 sistemas de IA: en 2025 eso era 5/5 = 100; en 2026 es 5/11 ≈ 45). El reporte debe explicar esto al comentar caídas.

---

## 3 · El criterio de elegibilidad 2026 («criterio corregido»): qué entra y qué no

**Regla central:** un caso ENTRA solo si es **realmente un proceso de participación ciudadana** — consulta pública, presupuesto participativo, mini-público/deliberación, referendo o iniciativa popular, gobernanza colaborativa — **que usa IA en alguna de las 4 etapas** (Planificación, Implementación, Análisis, Traducción Política), **incluida la logística** del proceso (moderar, administrar turnos, preparar materiales, organizar). No se exige que la IA analice el contenido de los aportes.

El criterio se movió en dos direcciones a la vez:

**(a) Se AMPLIÓ en un eje** — el rol logístico de la IA ahora cuenta. El borrador inicial 2026 excluía los casos con IA de «apoyo»; la metodología final los admite. Tres casos entraron por esta vía: **CL LXS 400 – Chile Delibera** y **BR Meta Community Forum** (moderador automatizado de deliberación en la plataforma de Stanford) y **BR OPA Piauí** (IA que agiliza el flujo del presupuesto participativo).

**(b) Se ENDURECIÓ en todo lo demás** — seis exclusiones explícitas, aplicadas con verificación caso a caso:

1. **Civic tech que no es proceso participativo** (apps de reporte/servicio/monitoreo, fiscalización ciudadana, ciencia ciudadana de datos): sacó a ParticipACT Brasil y dIAra (que estaban INCLUIDOS en 2025), y dejó fuera a Pa' que veás, GeTAU (AR), Atlántico-LITA, entre otros.
2. **Atención ciudadana** (chatbots de trámites/información): ya era exclusión en 2025; se reconfirmó para ~20 casos y sacó a CiudadanIA (DO) y Descongestión Ingreso Solidario (CO), que en 2025 estaban incluidos.
3. **Votación/conteo electoral** (integridad del voto no es participación): sacó a Sufragio Seguro (MX) y al Sistema de cómputo de Elecciones 2026 (PE), ambos incluidos en 2025.
4. **«Solo opinión» sin proceso**: encuestas/paneles de percepción y escucha de redes sociales sin proceso participativo convocado ni incidencia: sacó a U-Report (CR, incluido en 2025) y dejó fuera a Citibeats+PNUD.
5. **IA como TEMA de la consulta** (consultar a la ciudadanía SOBRE IA no es usar IA en el proceso): dejó fuera las consultas de PY (PNUD AccLab) y UY (NNA y entornos digitales, además fuera de ventana temporal).
6. **Estudio/ejercicio sin despliegue oficial y duplicados**: investigación académica o pilotos sin adopción institucional no cuentan (Cátedra Brasil/USP, Participe+ UnB, Projeto Lumina, POT Bogotá, ISIDataInsights, Senador Virtual/CrowdLaw), y una misma iniciativa no se cuenta dos veces (BP-Classificador es parte de Brasil Participativo; Colab 2025 era el mismo despliegue que OPA Piauí; e-Cidadania consolidó sus dos herramientas en UNA fila).

**Además, subió el estándar de evidencia:** «IA disponible» dejó de bastar — se exige **uso verificado**. Plataformas cuyo software trae módulo de IA de fábrica pero sin traza de haberlo activado sobre los aportes quedaron fuera (Participa Pudahuel, Viña Decide, EngageTT-TT). Y donde el análisis fue manual o text-analytics trivial (nubes de palabras), tampoco cuenta (DNP Diálogos Regionales, Jalisco ¡Armemos un Plan!).

---

## 4 · Cambios en el PROCESO de construcción de la base (explican la calidad, no la fórmula)

1. **Búsqueda exhaustiva y sistemática**: 4 oleadas de descubrimiento web (~27 búsquedas paralelas), 15 canales codificados (baseline, prensa, licitaciones, premios, proveedores, etc.), marco de búsqueda de 300 celdas, directorio de 60 medios en 20/20 países. Resultado: 97 candidatos evaluados.
2. **Re-verificación del ciclo anterior completo**: los 28 incluidos 2025 fueron re-verificados con fuentes (13 con re-verificación web profunda) y los 49 excluidos 2025 fueron re-examinados bajo el criterio 2026 (5 en profundidad, con segunda pasada). **Ningún excluido 2025 reingresó directamente**; 2 reingresaron transformados en casos nuevos con IA ya desplegada (la propuesta «De ciudadano a senador» se materializó en el matching de ideias legislativas de e-Cidadania; «Participa+ Brasil» devino Brasil Participativo con clustering real).
3. **Doble extracción independiente + conciliación**: cada ficha se extrajo con dos prompts distintos por dos pasadas independientes y se concilió por script, con nivel de confianza por caso (ALTA/MEDIA/BAJA registrado en la base).
4. **Verificación verbatim**: todo campo crítico exige **cita textual exacta** de la fuente (verificada por software); si no hay cita, el campo queda nulo con alerta — «mejor null que un valor plausible».
5. **Validación humana final**: el equipo validó manualmente caso por caso (planilla de validación jul-2026), ajustó coding, eliminó 6 casos en esa pasada y resolvió los casos frontera.

---

## 5 · La aritmética de la base: por qué NO aumentaron los casos

**El titular: 28 casos incluidos en 2025 → 28 casos incluidos en 2026.** Pese a una búsqueda muchísimo más exhaustiva (97 candidatos evaluados), la base no creció, porque el criterio más estricto **depuró 12 falsos positivos del ciclo anterior** a la vez que admitió 12 casos nuevos que sí superan el estándar:

```
BBDD 2025 (28 incluidos)
 ├─ 16 sobreviven a la re-verificación 2026
 │    (15 idénticos + e-Cidadania, que ADEMÁS sumó una segunda herramienta y se
 │     consolidó en una sola fila)
 └─ 12 SALEN al aplicar el criterio 2026 y re-verificar la evidencia:
      · Atención/servicio, no participación ..... CiudadanIA (DO), Descongestión (CO)
      · Civic tech de reporte/monitoreo .......... ParticipACT (BR), dIAra (CR)
      · Electoral, no participación .............. Sufragio Seguro (MX), Cómputo 2026 (PE)
      · Solo encuesta de opinión ................. U-Report (CR)
      · Sin IA verificada al re-verificar ........ Estrategia Gob. Digital (CL),
                                                   RedPública+iVerify (HN), CRECES (MX)
      · Duplicado ................................ Colab (BR) (= OPA Piauí)
      · Homónimo depurado ........................ Part. Proceso Constitucional-audiencias (CL)

Candidatos NUEVOS 2026 (por descubrimiento + aportes del equipo)
 ├─ 12 ENTRAN: 5ª Conferência CT&I, Brasil Participativo, Meta Forum, OPA Piauí y
 │    São Paulo Participe+ (BR) · ECQQ y LXS 400 (CL) · Código de las Familias (CU) ·
 │    Guanajuato (MX) · Mansa Idea (PA) · Pol.is-LUC (UY) · Plan de la Patria 7T (VE)
 └─ 19 NO ENTRAN (estudio sin despliegue, IA disponible pero no usada, IA como tema,
      civic tech, doble conteo, análisis manual, fuera de ventana; incluye GeTAU AR)

TOTAL EXCLUIDOS DOCUMENTADOS 2026: 80 = 12 (estaban incluidos en 2025)
                                      + 49 (ya excluidos en 2025, reconfirmados)
                                      + 19 (nuevos identificados y no incluidos)
```

**Mensajes para el reporte (todos respaldados):**
- El nº igual de casos NO significa estancamiento del fenómeno: significa **recambio con estándar más alto**. De hecho la base se movió mucho: 43 % de los casos 2026 son nuevos.
- La cobertura geográfica **se redistribuyó**: de 11 a 12 países con casos. Debutan **CU, PA, UY y VE**; caen a cero **CR, DO y HN** (sus casos 2025 eran atención ciudadana, encuestas de opinión o civic tech — es una corrección de medición del ciclo anterior, no necesariamente un retroceso real de esos países).
- La concentración real del fenómeno está en **BR (7 casos) y CL (9 casos)**; CO queda con 3; los otros 9 países con casos tienen 1 cada uno. Vacíos confirmados con búsqueda rigurosa: AR, JM, PY, SV (y CR/DO/HN tras la depuración; TT sin casos elegibles).
- Cada caso 2026 tiene **evidencia verbatim verificada y validación humana** — la base es más chica de lo que la búsqueda sugería, pero mucho más defendible.

---

## 6 · Resultados: las tres lecturas y cómo descomponer los cambios

Para separar «efecto fórmula» de «cambio real» existen tres series (todas en `Comparacion_2025_2026_ILIA.xlsx`):

| País | 2025 fórmula antigua (≈oficial publicado) | 2025 fórmula NUEVA (misma base 2025, retrospectivo) | 2026 (fórmula nueva, base nueva) | Δ efecto fórmula | Δ real |
|---|---|---|---|---|---|
| BR | 77 | 75 | **91** | −2 | **+16** |
| CL | 57 | 57 | **73** | 0 | **+16** |
| CO | 85 | 82 | **53** | −3 | **−29** |
| CU | 0 | 0 | **33** | 0 | +33 |
| GT | 33 | 34 | **28** | +1 | −6 |
| BO | 31 | 32 | **27** | +1 | −5 |
| PE | 54 | 46 | **24** | −8 | −22 |
| EC | 25 | 27 | **23** | +2 | −4 |
| MX | 48 | 36 | **23** | −12 | −13 |
| UY | 0 | 0 | **23** | 0 | +23 |
| PA | 0 | 0 | **21** | 0 | +21 |
| VE | 0 | 0 | **17** | 0 | +17 |
| CR | 46 | 45 | **0** | −1 | −45 |
| DO | 30 | 32 | **0** | +2 | −32 |
| HN | 42 | 43 | **0** | +1 | −43 |
| AR·JM·PY·SV·TT | 0 | 0 | **0** | 0 | 0 |

(El recalculo con la fórmula antigua reproduce el oficial publicado 2025 en 19/19 países con diferencias ≤1 punto de redondeo; el retrospectivo «2025 fórmula nueva» usa la recodificación 2026 del baseline, que es **BORRADOR pre-Gate** — decirlo si se cita.)

**Lecturas clave:**
- **El cambio de fórmula por sí solo es moderado** (mediana |Δ| ≈ 1-2 puntos), salvo en **MX (−12)** y **PE (−8)**: ambos son castigados por el rediseño de **Organización Convocante** (convocantes únicos puntúan bajo en las 3 sub-dimensiones) y por la nueva variable **Cantidad** (con 2 casos quedan en 25); en MX además cae **Continuidad**, que antes sumaba 100 por tener ambas modalidades y ahora vale por el nivel máximo (66,7). La gran reordenación, sin embargo, viene de la **base de casos**, no de la aritmética.
- **BR 91 (1º)**: único país con los 5 tipos de proceso; 7 iniciativas; nivel 3 de consolidación (OPA Piauí); máximos en desarrolladores y sistemas de IA → Sub2 = 100.
- **CL 73 (2º)**: 9 iniciativas (la mayor cantidad), ecosistema convocante amplio (gobierno + 3 tipos no gubernamentales, 2 combinaciones de co-convocatoria), 11 sistemas de IA.
- **CO 85 → 53**: pasó de 4 a 3 iniciativas (banda de Cantidad 50→25) y, sobre todo, los máximos relativos del ciclo subieron (sus 5 sistemas de IA valían 100 en 2025 y ~45 en 2026). No perdió capacidades: el listón regional subió y su base se depuró (Descongestión salió por ser atención ciudadana).
- **Sub1 vs Sub2 por país** y las 7 variables están graficadas en la pestaña 4 de `BBDD_casos_incluidos_ILIA2026.xlsx` y en la pestaña 5 de la comparación.

---

## 7 · Advertencias de redacción (no sobreafirmar)

1. **No comparar 2025 oficial vs 2026 sin descomponer** (§6): siempre separar efecto fórmula / efecto base / efecto máximos relativos.
2. El retrospectivo «2025 con fórmula nueva» usa la **recodificación BORRADOR pre-Gate** del baseline (convocante 7-cat y niveles derivados de texto): sirve para ordenar magnitudes, no para publicar como serie oficial.
3. Las caídas a 0 de CR/DO/HN son **corrección de criterio**, no evidencia de retroceso; redactarlas como depuración de la medición.
4. **VE entra con confianza MEDIA-BAJA** (la IA de sistematización del Plan de la Patria 7T está afirmada solo por fuentes estatales, sin verificación técnica independiente — caveat registrado en la base). GT/BO/CL tienen varios casos «MEDIA (baseline 2025; sin señal web nueva)».
5. **PA Mansa Idea**: sin sistema de IA técnicamente especificado en las fuentes («null») → cuenta 0 sistemas; por eso Sub2 de PA = 6. La capa de IA la desarrolló sociedad civil SOBRE un corpus participativo convocado por el gobierno (2020-21): matiz que vale la pena narrar bien.
6. **BR Brasil Participativo** está codificado como «anuncio» (nivel 1) del componente de clustering, con nivel efectivo 0 por la regla de caducidad (año 2023); no afecta el puntaje de BR. No presentarlo como IA en producción.
7. Diferencias de **±1 punto** con el oficial 2025 publicado son redondeo (motor antiguo vs Excel), no discrepancias de datos.
8. **TT** se incorporó al universo en 2026 sin baseline 2025 (mostrar «s/d» para su 2025, no 0 histórico).
9. El documento normativo original de CENIA con el racional formal de cada cambio (v1.2 y anexo de cambios de variables) **no estuvo disponible para el pipeline**; las justificaciones de §2 son el racional operativo documentado en la metodología CENIA v2 y en la bitácora del proyecto. Si el equipo dispone del documento normativo, citarlo como fuente primaria del rediseño.
10. Cifras canónicas para el texto: **28 casos incluidos · 12 países con casos · 80 exclusiones documentadas (12+49+19) · 97 candidatos evaluados · 43 % de recambio de la base · 16 casos sobrevivientes del ciclo 2025**.

## 8 · Datos citables rápidos

- Ranking 2026: BR 91 · CL 73 · CO 53 · CU 33 · GT 28 · BO 27 · PE 24 · EC 23 · MX 23 · UY 23 · PA 21 · VE 17 · resto 0.
- Sub1/Sub2 2026 por país (redondeados): BR 81/100 · CL 69/77 · CO 56/50 · CU 34/31 · GT 39/17 · BO 40/13 · PE 30/17 · EC 35/11 · MX 30/15 · UY 29/17 · PA 35/6 · VE 23/11.
- Casos emblemáticos nuevos para narrar: e-Cidadania del Senado de Brasil (búsqueda semántica que incorpora ideas ciudadanas a proyectos de ley — participación con IA en «traducción política»); 5ª Conferência Nacional de CT&I (sistematización con IA de un proceso con >100 mil participantes); OPA Piauí (presupuesto participativo 100 % digital con IA, nivel 3 de consolidación); Consulta del Código de las Familias en Cuba (agrupamiento de propuestas de ~6,5 millones de participantes); LXS 400 y Meta Forum (moderación automatizada de deliberación — la vía «logística» que el criterio 2026 reconoce); Guanajuato InteliGENTE (planificación estatal con IA sobre 26.000 voces).
- Del lado de la exclusión, ejemplos ilustrativos del rigor: GaitanIA (CO) — candidatura con avatar de IA cuya mecánica participativa nunca operó; EngageTT (TT) — plataforma con módulo de IA de fábrica sin evidencia de uso; Senador Virtual (CL) — 16 años de participación digital real, pero la IA es investigación académica, no producción.
