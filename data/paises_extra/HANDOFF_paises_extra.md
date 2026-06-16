# HANDOFF — ILIA 2026 · Indicadores para 5 países extra

**Para retomar en una sesión nueva.** Última actualización: 2026-06-16 · Rama: `claude/keen-pascal-VvcET`
**Operador:** aplicaciones@foresight.cl · **Todo el trabajo vive en** `data/paises_extra/`.

---

## 1. Propósito
Recolectar indicadores ILIA 2026 para **5 países extra** y dejar todo listo para que el
equipo valide/llene la **planilla oficial** a mano. Dos bloques:
- **A. Investigación, adopción y desarrollo** — **11 indicadores** × 5 países (España, Estonia, Singapur, Alemania, Portugal).
- **B. Gobernanza** — **38 subindicadores** × 5 países.

Definiciones/rúbricas salen del Excel del operador `Subindicadores_ILIA_2026_v_11.05.26.xlsx`
(hoja "Descripción y seguimiento subin"). Rúbricas de gobernanza copiadas en
`gobernanza/RUBRICAS_gobernanza.md`.

## 2. ⚠️ Entorno y restricciones (LEER PRIMERO)
- **Red del sandbox:** `curl` solo llega a `raw.githubusercontent.com` (+ codeload.github.com).
  **WebFetch da HTTP 403 en casi todo** (dashboards, APIs de datos, PDFs, hasta Wikipedia).
  **WebSearch funciona** (solo snippets).
- **Implicación:** lo que vive en **GitHub/datos crudos** se obtiene **determinístico**
  (GitHub Innovation Graph, OWID/EMBER, espejos); lo que vive en **dashboards/PDF**
  (ETO CAT, OECD.AI, UN egovkb, Hugging Face, Zenodo, GIRAI, ITU GCI, ISO, DLA Piper,
  NRI) **no es accesible** → queda como **extracción manual** (con ruta exacta).
- **Anti-alucinación:** ninguna cifra de memoria; cada dato lleva fuente+URL; lo no
  verificable se marca `NO ENCONTRADO`/`PEND`/`PRELIM`. Validación por agentes
  independientes + (donde se pudo) verificación red-team.
- **Git:** desarrollar y pushear SIEMPRE a `claude/keen-pascal-VvcET`. Antes de commitear:
  `git config user.email noreply@anthropic.com && git config user.name Claude`. Commits
  firmados con `--reset-author`. Push con reintentos (2/4/8/16s).
- **Libs Python** (reinstalar si el contenedor reinició): `pip install openpyxl pandas reportlab pymupdf`.
- **Si el operador sube un PDF/archivo** (estrategias, GCI 2024, OSI, ETO export, MCI):
  parsearlo con pandas/openpyxl/pymupdf (como se hizo con `MCI_data_2025.xlsx`) — esa es
  la vía para cerrar lo manual sin red.

## 3. Decisiones del operador (CONFIRMADAS — no re-preguntar)
1. **Gobierno digital = ID 92** (Online Service Index / OSI del UN E-Gov Survey 2024).
2. **Patentes = OECD.AI** — pero se descubrió que OECD.AI/CSET **solo publica FAMILIAS**;
   **aplicantes e inventores por país NO existen** allí → requieren **Espacenet/Lens** (cambio de fuente).
3. **Desarrollo de IA = nº de modelos por país en Hugging Face** (vía organizaciones).
4. **Año = último disponible** (documentado). Valor **bruto**; per cápita donde el índice normaliza.
5. **I+D/PIB = fuentes oficiales o multinacionales** (oficinas nacionales, Eurostat, OCDE, World Bank); descartar CEIC/SSTI/Statista/prensa.
6. **Relevancia de software (GitHub):** denominador = **repos acumulado total** (suma de los 24 trimestres); **dos versiones**: inbounds total y solo 2025.

## 4. Estado — Bloque A (económicos), 5 países
| Indicador (ID) | Estado | Valores / nota |
|---|---|---|
| Gasto I+D/PIB (73) | ✅ LISTO | ES 1,50%(2024) · EE 2,0%(2024) · SG 2,16%(2020)/~1,85%(2022) · DE 3,13%(Eurostat)/3,17%(Destatis 2024) · PT 1,73%(2024). Ver `gasto_id_pib.md`. SG: confirmar exacto en A*STAR. |
| Desarrollo de apps (76) | ✅ LISTO | Score 2024 "Locally developed apps per person": ES 89,30 · EE 96,73 · SG 100 · DE 94,75 · PT 86,24. Del archivo oficial MCI_data_2025.xlsx. Es score 0–100 (bruto per cápita es propietario). |
| Relevancia software (80) | ✅ LISTO | (total / 2025) ES 0,03189/0,00788 · EE 0,03571/0,00655 · SG 0,02589/0,00822 · DE 0,08960/0,01899 · PT 0,03280/0,00768. Determinístico (`github_relevancia_sw.py`). |
| Empresas de IA (70) | ❌ MANUAL | cat.eto.tech (Investment). No accesible. |
| Nº inversiones privadas (71) | ❌ MANUAL | cat.eto.tech. |
| Valor inversión privada (72) | ❌ MANUAL | cat.eto.tech. |
| Desarrollo de IA / HF (81) | ❌ MANUAL | Conteos no accesibles; **orgs identificadas por país** en `desarrollo_ia_hf_orgs.md`. API HF. |
| Familias patentes IA (82) | ⚠️ PARCIAL | SG 661 sol./297 conc. (2017-20); DE ~436 (FRÁGIL); ES/EE/PT no. cat.eto.tech. |
| Aplicantes patentes IA (83) | ❌ MANUAL | No en OECD.AI → Lens/Espacenet (país del solicitante). |
| Inventores patentes IA (84) | ❌ MANUAL | No en OECD.AI → Lens/Espacenet (país del inventor). |
| Gobierno digital OSI (92) | ❌ MANUAL | OSI no accesible. EGDI de contexto: EE 0,97274(#2) · SG 0,96912(#3) · PT 0,8415(#49) · DE top-20(~0,94) · ES "Very High". |

Detalle: `REPORTE_INDICADORES_5_PAISES.md` + un .md por indicador. Población per cápita: `poblacion_total_worldbank.csv`.

## 5. Estado — Bloque B (gobernanza), 5 países
Matriz consolidada: **`gobernanza/REPORTE_gobernanza_5paises.md`** y hoja "Gobernanza (5 países)" de la planilla.
Cobertura: **138 verde · 21 ámbar (PRELIM) · 31 rojo (manual)** de 190 celdas.
- ✅ **Listo** (con dato/puntaje): existencia/antigüedad/actualización/presupuesto/hoja de ruta, 8-9 tópicos, institucionalidad, coordinación, ISO, ley+autoridad de datos, acuerdos int'l, regulación IA, NRI (salvo ES), ERNC.
- ⚠️ **PRELIM** (sin texto primario de la estrategia): mecanismos de evaluación, género, sostenibilidad, participación ciudadana, multistakeholder, clasificación de riesgo (SG/PT).
- ❌ **Manual**: **GCI 5 pilares** (solo España completa: 20/20/20/19,74/20), **GIRAI 2 áreas** (los 5), **OSI**, NRI España.

Detalle/fuentes/dudas por país: `gobernanza_{estonia,singapur,alemania,espana,portugal}.md`,
`gobernanza_estandares_*` (ISO/datos/ciber), `etica_seguridad_*` (GIRAI/NRI/EGDI),
`energia_*` (ERNC), `FUENTES_gobernanza_EE_SG.md`, `INCERTIDUMBRES_gobernanza_EE_SG.md`.

**Diferencias por país a recordar:**
- 🇪🇸 ES: fuerte (AESIA 1ª agencia IA UE; 1er sandbox UE; EU AI Act + ley nacional; **Género=1**; GCI 5 pilares completos).
- 🇵🇹 PT: **nueva Agenda 2026-2030** (Antigüedad=4, >€400M, consulta con resultados=4, multistakeholder Gob+4=5); pero **ISO=Observador** (SC42=1/SC27=1), Género=0, Sostenibilidad=0.
- 🇩🇪 DE: KI-Strategie 2018→Aktionsplan 2023 (Antigüedad=3); €5.000M; EU AI Act+KI-MIG; GPAI fundador; Género=0; GCI total 97,85.
- 🇪🇪 EE: Antigüedad=4; **ISO SC42=0** (a verificar).
- 🇸🇬 SG: iniciativa legal=1 (soft law).

## 6. Pendientes priorizados (acción manual del equipo)
1. **ETO CAT** — Empresas, Nº y Valor de inversiones (70-72), 5 países → cat.eto.tech (Investment).
2. **OSI** (92), 5 países → UN Data Center / CSV World Bank Data360 `UN_EGDI_OSI_WIDEF.csv` / Technical Appendix 2024.
3. **GCI 5 pilares** (133-137) — EE/SG/DE/PT (ES ya) → World Bank Data360 (indicadores por pilar `ITU_GCI_*_SCORE`) o anexo PDF GCI 2024.
4. **GIRAI 2 áreas** (138-139), 5 países → portal global-index.ai.
5. **Patentes familias** (82) ES/EE/PT → cat.eto.tech (Patent). **Aplicantes/inventores** (83-84) → Lens/Espacenet (CPC G06N por país solicitante/inventor).
6. **HF modelos** (81), 5 países → API `huggingface.co/api/models?author=<ORG>` con orgs de `desarrollo_ia_hf_orgs.md`.
7. **NRI energía — España** (144) → networkreadinessindex.org/country/spain/.
8. **PDFs de estrategias** (para cerrar los PRELIM verbatim): krattAI/White Paper EE; NAIS 2.0 SG; KI-Strategie/Aktionsplan DE; Estrategia IA 2024 ES; ANIA 2026-2030 PT.

## 7. Decisiones metodológicas ABIERTAS (resolver con el operador)
- **EU AI Act como "iniciativa legal" (128)** en países UE (EE/DE/ES/PT): hoy se puntúa 3. ¿Se acepta el reglamento UE como iniciativa, o se exige ley nacional? (Afecta también 129/130.)
- **Singapur "Antigüedad" (104):** ¿el Update de may-2026 cuenta como estrategia nueva (→4) o se mantiene NAIS 2.0 2023 (→3)?
- **ISO SC 42 de Estonia (125)=0:** confirmar a mano en iso.org (confianza MEDIA).
- **ERNC (145) para ES y PT:** EMBER no separa gran/pequeña hidro. "% renovables total" vs "ERNC excl. gran hidro" difiere mucho (ES hidro ~12%, PT ~31%). Definir cuál usa ILIA.
- **Patentes:** definir la consulta de IA (CPC G06N narrow vs taxonomía WIPO amplia), atribución (país del solicitante vs del inventor) y ventana de años, **replicando lo que ILIA usó para los demás países**.
- **Definiciones "Aplicantes" vs "Inventores" están CRUZADAS en el Excel del operador** (la de "Aplicantes" describe inventores y viceversa) → fijar antes de contar.
- **Dos "Gobierno Digital" en el Excel** (ID 92 OSI = el elegido; ID 113 = tópico de estrategia, ya cubierto como #113).

## 8. Inventario de archivos (`data/paises_extra/`)
**Entregables principales:** `Planilla_ILIA2026_paises_extra.xlsx` (4 hojas: LÉEME, Económicos 5, Gobernanza 5, Pendientes) · `Indicadores_ILIA2026_por_pais.pdf` (PDF por país; **gobernanza solo EE/SG** — pendiente regenerar con DE/ES/PT) · `REPORTE_INDICADORES_5_PAISES.md`.
**Económicos (.md):** `gasto_id_pib.md`, `desarrollo_aplicaciones_gsma.md`, `empresas_inversion_eto.md`, `desarrollo_ia_hf_orgs.md`, `patentes_ia_oecdai.md`, `gobierno_digital_osi.md`. Datos: `relevancia_sw_resultados.csv`, `desarrollo_apps_gsma_mci2025.csv`, `poblacion_total_worldbank.csv`.
**Gobernanza (`gobernanza/`):** `REPORTE_gobernanza_5paises.md`, `RUBRICAS_gobernanza.md`, `gobernanza_{estonia,singapur,alemania,espana,portugal}.md`, `gobernanza_estandares_datos_ciber.md` (EE/SG), `gobernanza_estandares_DE_ES_PT.md`, `etica_seguridad_energia.md` (EE/SG), `etica_seguridad_DE_ES_PT.md`, `energia_DE_ES_PT.md`, `FUENTES_gobernanza_EE_SG.md`, `INCERTIDUMBRES_gobernanza_EE_SG.md`, `REPORTE_gobernanza_EE_SG.md`.
**Scripts reproducibles:** `github_relevancia_sw.py` (indicador 80), `generar_planilla.py` (xlsx + matriz md), `generar_pdf_indicadores.py` (PDF).

## 9. Cómo regenerar
```bash
cd data/paises_extra
python3 github_relevancia_sw.py     # recalcula indicador 80 desde GitHub (red: raw.githubusercontent)
python3 generar_planilla.py         # Planilla .xlsx (5 países) + REPORTE_gobernanza_5paises.md
python3 generar_pdf_indicadores.py  # PDF por país
```
Para editar valores de gobernanza: la fuente de verdad es la lista `G` en `generar_planilla.py`
(y `ECON`/`ECON_CELLS` para económicos en `generar_pdf_indicadores.py`).

## 10. Próximos pasos sugeridos para la nueva sesión
1. Si el operador sube **PDFs de estrategias** → parsearlos y cerrar los ítems **PRELIM** (verbatim) de gobernanza.
2. Si sube **export de GCI 2024 / OSI / ETO CAT** → parsear y rellenar el rojo.
3. **Regenerar el PDF** para incluir Gobernanza de DE/ES/PT (hoy solo EE/SG): extender `generar_pdf_indicadores.py` con datos de los 5 (o renderizar la matriz `G` de `generar_planilla.py`).
4. Preparar **consultas Lens/Espacenet** listas para pegar (aplicantes/inventores de patentes).
5. Resolver las **decisiones metodológicas abiertas** (§7) con el operador y re-puntuar lo afectado.
6. Pedir/confirmar la **metodología ILIA 2025** de patentes y de "Relevancia de software" (denominador/ventana) para asegurar comparabilidad.
