#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Detalle de GOBERNANZA por país: por subindicador, POR QUÉ el puntaje (justificación
+ confianza) y URLs ESPECÍFICAS (varias fuentes por celda: documento oficial / anuncio /
fuente secundaria). Justificaciones transcritas de gobernanza/*.md; URLs específicas
localizadas y verificadas en resultados de búsqueda (jun-2026) + compendio FUENTES.

  GOBDET[cc][id] = (justificacion, confianza, [urls])

El puntaje y la rúbrica viven en datos_gobernanza.py (matriz G + GOB_META): una sola
fuente de verdad del puntaje. Aquí, el "por qué" y las fuentes.
Compendio exhaustivo: gobernanza/FUENTES_gobernanza_EE_SG.md y gobernanza_<país>.md."""

# ---- Canónicas / multinacionales ----
ISO42 = "https://www.iso.org/committee/6794475.html?view=participation"
ISO27 = "https://www.iso.org/committee/45306.html?view=participation"
JTC1_SC42 = "https://jtc1info.org/sd-2-history/jtc1-subcommittees/sc-42/"
GCI = "https://www.itu.int/epublications/publication/global-cybersecurity-index-2024"
GCI_D360 = "https://data360.worldbank.org/en/indicator/ITU_GCI_GCI_OVRL_SCRE"
GIRAI = "https://www.global-index.ai"
NRI = "https://networkreadinessindex.org"
EMBER = "https://ember-energy.org/data/electricity-data-explorer/"
OWID = "https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-data.csv"
OECDAIP = "https://oecd.ai/en/ai-principles"
GPAI = "https://oecd.ai/en/about/about-gpai"
UNESCO = "https://www.unesco.org/en/artificial-intelligence/recommendation-ethics"
AIACT = "https://eur-lex.europa.eu/eli/reg/2024/1689/oj"
def DLP(cc): return f"https://www.dlapiperdataprotection.com/?t=law&c={cc}"

# ---- Estonia (documentos/anuncios específicos; compendio en FUENTES_gobernanza_EE_SG.md) ----
EE_OECD = "https://oecd.ai/en/dashboards/national/estonia"
EE_WP = "https://regulations.ai/regulations/RAI-EE-NA-DAIWPXX-2024"
EE_AP = "https://regulations.ai/regulations/RAI-EE-NA-ADAPKXX-2024"
EE_2019 = "https://regulations.ai/regulations/RAI-EE-NA-ENAISXX-2019"
EE_NAIS2 = "https://oecd.ai/en/dashboards/policy-initiatives/national-ai-strategy-20-4102"
EE_KRATID = "https://www.kratid.ee/en/kratt-visioon"
EE_FACT = "https://e-estonia.com/wp-content/uploads/factsheet-ai-strategy.pdf"
EE_MOMENT = "https://e-estonia.com/ai-and-the-kratt-momentum/"
EE_K4P = "https://knowledge4policy.ec.europa.eu/sites/default/files/estonia-ai-strategy-report.pdf"
EE_DIGW = "https://dig.watch/resource/estonias-national-artificial-intelligence-strategy-kratt-strategy-for-2022-2023"
EE_ERR85 = "https://news.err.ee/1609250613/estonia-to-invest-85m-in-boosting-ai-uptake-across-public-private-sectors"
EE_RIIGI = "https://www.riigikantselei.ee/en/supporting-government-and-prime-minister/eestiai-initiative"
EE_VALITSUS = "https://www.valitsus.ee/en/news/government-launched-eestiai-initiative-together-leading-entrepreneurs"
EE_MEDIUM = "https://medium.com/e-residency-blog/estonia-starts-public-discussion-legalising-ai-166cb8e34596"
EE_ACT = "https://regulations.ai/regulations/RAI-EE-NA-E2AIAXX-2024"
EE_SANDBOX = "https://www.fairedih.fi/en/2026/05/20/finland-and-estonia-bet-on-ai-sandboxes-as-europes-small-states-seek-influence-over-digital-rules/"
EE_AKI = "https://www.aki.ee/en"
EE_RT = "https://www.riigiteataja.ee/en/eli/523012019001/consolide"
EE_OECDAIP = "https://oecd.ai/en/dashboards/policy-initiatives/oecd-ai-principles-9705"
EE_NRI = "https://networkreadinessindex.org/country/estonia/"

# ---- Singapur ----
SG_SN = "https://www.smartnation.gov.sg/initiatives/national-ai-strategy/"
SG_NAIS = "https://file.go.gov.sg/nais2023.pdf"
SG_MDDI = "https://www.mddi.gov.sg/newsroom/04122023/"
SG_UPD = "https://www.mddi.gov.sg/newsroom/update-to-singapore-s-national-ai-strategy--refreshed-priorities-to-harness-ai-for-the-public-good-factsheet/"
SG_PR = "https://www.sgpc.gov.sg/api/file/getfile/Press%20Release_NAIS%202_0%20and%20SCAI_4%20Dec.pdf"
SG_INFO = "https://www.smartnation.gov.sg/files/publications/infographic_nais2_0.pdf"
SG_OECD = "https://oecd.ai/en/dashboards/policy-initiatives/national-ai-strategy-20-6191"
SG_MGF = "https://www.pdpc.gov.sg/help-and-resources/2020/01/model-ai-governance-framework"
SG_AIV = "https://aiverifyfoundation.sg/"
SG_MGFGEN = "https://aiverifyfoundation.sg/wp-content/uploads/2024/06/Model-AI-Governance-Framework-for-Generative-AI-19-June-2024.pdf"
SG_IMDA = "https://www.imda.gov.sg"
SG_AISG = "https://aisingapore.org/"
SG_ASEAN = "https://asean.org/wp-content/uploads/2024/02/ASEAN-Guide-on-AI-Governance-and-Ethics_beautified_201223_v2.pdf"
SG_DLP = "https://www.dlapiperdataprotection.com/index.html?t=law&c=SG"
SG_SSO = "https://sso.agc.gov.sg/Act/PDPA2012"
SG_PDPC = "https://www.pdpc.gov.sg"
SG_LIRNE = "https://lirneasia.net/wp-content/uploads/2025/03/Draft-Version-for-Review_GIRAI-Report_LIRNEasia_20-March-2025.pdf"
SG_NRI = "https://networkreadinessindex.org/country/singapore/"

# ---- Alemania (localizadas en búsqueda jun-2026) ----
DE_KI2018 = "https://www.bundesregierung.de/resource/blob/997532/1550276/3f7d3c41c6e05695741273e78b8039f2/2018-11-15-ki-strategie-data.pdf"
DE_KI2020 = "https://www.bmas.de/DE/Service/Presse/Pressemitteilungen/2020/kabinett-beschliesst-fortschreibung-der-ki-strategie-der-bundesregierung.html"
DE_KISTRAT = "https://www.ki-strategie-deutschland.de/"
DE_AKT_PDF = "https://www.ki-strategie-deutschland.de/files/downloads/Aktionsplan_Kuenstliche_Intelligenz_2023.pdf"
DE_AKT_PAGE = "https://www.bmftr.bund.de/DE/Forschung/Schluesseltechnologien/KuenstlicheIntelligenz/KiAktionsplan/kiaktionsplan_node.html"
DE_AKT_EU = "https://www.eubuero.de/de/akutelles-efr-2023-11-20-3499.html"
DE_OECD = "https://www.oecd.org/en/publications/oecd-artificial-intelligence-review-of-germany_609808d6-en.html"
DE_OECD_WONK = "https://oecd.ai/en/wonk/review-germany-2024"
DE_EUPLAN = "https://www.oecd.org/en/publications/progress-in-implementing-the-european-union-coordinated-plan-on-artificial-intelligence-volume-1_6d530a88-en/germany_f00f3020-en.html"
DE_PLS = "https://www.plattform-lernende-systeme.de"
DE_PLS_ACA = "https://www.acatech.de/projekt/lernende-systeme-die-plattform-fuer-kuenstliche-intelligenz/"
DE_BNETZA = "https://www.bundesnetzagentur.de/DE/Fachthemen/Digitales/KI/start_ki.html"
DE_BNETZA_LAB = "https://www.bundesnetzagentur.de/DE/Fachthemen/Digitales/KI/5_Innovationen/start.html"
DE_KIMIG = "https://bmds.bund.de/service/gesetzgebungsverfahren/gesetz-zur-durchfuehrung-der-ki-verordnung"
DE_BFDI = "https://www.bfdi.bund.de"
DE_NRI = "https://networkreadinessindex.org/country/germany/"

# ---- España ----
ES_M24 = "https://www.lamoncloa.gob.es/consejodeministros/resumenes/paginas/2024/140524-rueda-de-prensa-ministros.aspx"
ES_D24 = "https://digital.gob.es/comunicacion/notas-prensa/secretaria-digitalizacion-e-inteligencia-artificial/2024/05/2024-05-14.html"
ES_P24 = "https://planderecuperacion.gob.es/noticias/gobierno-aprueba-estrategia-inteligencia-artificial-2024-prtr"
ES_ENIA_M = "https://www.lamoncloa.gob.es/presidente/actividades/Paginas/2020/021220-sanchezenia.aspx"
ES_ENIA_P = "https://planderecuperacion.gob.es/noticias/conoce-Estrategia-Nacional-Inteligencia-Artificial-ENIA-IA-prtr"
ES_ENIA_INF = "https://portal.mineco.gob.es/RecursosNoticia/mineco/prensa/noticias/2023/20230522_informe_enia.pdf"
ES_AESIA_BOE = "https://www.boe.es/buscar/doc.php?id=BOE-A-2023-18911"
ES_AESIA = "https://aesia.digital.gob.es"
ES_LEY_N = "https://digital.gob.es/comunicacion/notas-prensa/mtdfp/2025/03/2025-03-11"
ES_LEY_T = "https://avance.digital.gob.es/_layouts/15/HttpHandlerParticipacionPublicaAnexos.ashx?k=19128"
ES_SBX_BOE = "https://www.boe.es/diario_boe/txt.php?id=BOE-A-2023-22767"
ES_ALIA_AESIA = "https://aesia.digital.gob.es/en/presentalia"
ES_ALIA_BSC = "https://www.bsc.es/news/bsc-news/alia-europes-first-public-open-and-multilingual-ai-infrastructure"
ES_ALGV_M = "https://portal.mineco.gob.es/es-es/comunicacion/Paginas/algoritmos-verdes.aspx"
ES_ALGV = "https://algoritmosverdes.gob.es/es/recursos/programa-nacional-de-algoritmos-verdes"
ES_AEPD = "https://www.aepd.es"
ES_GCI = "https://espanadigital.gob.es"
ES_NRI = "https://networkreadinessindex.org/country/spain/"

# ---- Portugal ----
PT_DR = "https://diariodarepublica.pt/dr/detalhe/resolucao-conselho-ministros/2-2026-1000882016"
PT_DIGITAL = "https://digital.gov.pt/pt/documentos/resolucao-do-conselho-de-ministros-2-2026"
PT_GOV = "https://www.portugal.gov.pt/pt/gc25/comunicacao/noticia?i=inteligencia-artificial-governo-lanca-agenda-nacional-com-mais-de-400-milhoes-de-euros"
PT_OBS = "https://observador.pt/2026/01/08/publicada-agenda-nacional-de-inteligencia-artificial-e-respetivo-plano-de-acao-ate-2030/"
PT_AIP_OECD = "https://oecd.ai/en/dashboards/policy-initiatives/ai-portugal-2030-national-strategy-for-ai-1250"
PT_AIP_INCODE = "https://www.incode2030.gov.pt/en/estrategia-nacional-de-inteligencia-artificial-en/"
PT_AIP_RAI = "https://regulations.ai/regulations/RAI-PT-NA-AP2ENXX-2019"
PT_AUSC_D = "https://digital.gov.pt/noticias/roteiro-de-auscultacao-sobre-a-agenda-nacional-de-ia-arranca-em-janeiro"
PT_AUSC_G = "https://www.portugal.gov.pt/pt/gc24/comunicacao/noticia?i=auscultacao-para-a-agenda-nacional-de-inteligencia-artificial-inicia-se-esta-semana"
PT_COMPETE = "https://www.compete2030.gov.pt/comunicacao/portugal-prepara-agenda-nacional-de-inteligencia-artificial/"
PT_PUBLICO = "https://www.publico.pt/2025/09/19/ciencia/noticia/anacom-sera-reguladora-inteligencia-artificial-portugal-anuncia-governo-2147791"
PT_ANACOM = "https://www.anacom.pt/render.jsp?contentId=1824938"
PT_CMS = "https://cms.law/en/int/expert-guides/ai-regulation-scanner/portugal"
PT_CNPD = "https://www.cnpd.pt"
PT_AIACT57 = "https://artificialintelligenceact.eu/article/57"
PT_NRI = "https://networkreadinessindex.org/country/portugal/"

GOBDET = {}

# ================= ESTONIA =================
GOBDET["EE"] = {
 "103": ("Estrategia de datos+IA desde 2019; vigente el Valge raamat 2024-2030 + Tegevuskava 2024-26 (que 'on ühtlasi Eesti riiklik tehisintellekti strateegia', p.4). Validado en texto primario.", "ALTA", [EE_WP, EE_AP, EE_KRATID]),
 "104": ("Estrategia vigente publicada ene-2024 (White Paper 2024-2030) → tramo 2024-25.", "ALTA", [EE_WP, EE_OECD]),
 "105": ("3ª generación (2019→2022→2024) + iniciativa Eesti.ai (ene-2026).", "ALTA", [EE_2019, EE_NAIS2, EE_RIIGI]),
 "106": ("Sección 'Tegevuste elluviimine ja seire': juhtrühmad liderados por MKM dirigen y monitorean; metas y tulemusmõõdikud fijados en 'Eesti digiühiskond 2030'. Validado (Valge raamat p.12, 22).", "ALTA", [EE_WP, EE_AP]),
 "107": ("Tegevuskava con presupuesto por periodo: 10 M€ (2019-21), 20 M€ (2022-23); €85 M anunciados para 2024-26. Validado (Tegevuskava p.4).", "ALTA", [EE_ERR85, EE_RIIGI, EE_AP]),
 "108": ("Tegevuskava (Kratt) 2024-26 con tegevused por área (avalik sektor, erasektor, T&A, keeletehnoloogia, õigusruum, HPC). Validado en el Plan de Acción.", "ALTA", [EE_AP, EE_KRATID]),
 "109": ("IA 'human-centric/trustworthy'; alineada con el EU AI Act.", "ALTA", [EE_WP, EE_FACT]),
 "110": ("X-Road, infraestructura de datos (RIA), Bürokratt.", "ALTA", [EE_FACT, EE_MOMENT]),
 "111": ("Competence centres; 'Elements of AI' en estonio.", "ALTA", [EE_AP, EE_K4P]),
 "112": ("Eje explícito (es el White Paper 'de Data and AI').", "ALTA", [EE_WP, EE_OECD]),
 "113": ("Bürokratt y 30+ casos de uso de IA en el gobierno.", "ALTA", [EE_MOMENT, EE_FACT]),
 "114": ("Adopción en sector privado, PYMEs, deeptech.", "ALTA", [EE_AP, EE_K4P]),
 "115": ("Research & education; tecnología/corpus de lenguaje.", "ALTA", [EE_OECD, EE_K4P]),
 "116": ("EU Coordinated Plan; sandbox EE-FI; declaración báltica.", "ALTA", ["https://www.oecd.org/en/publications/progress-in-implementing-the-european-union-coordinated-plan-on-artificial-intelligence-volume-1_533c355d-en/full-report.html", EE_SANDBOX]),
 "117": ("Género NO es eje con plan → 0. Búsqueda exhaustiva: solo 5 menciones en ambos PDF — la métrica de igualdad (Valge raamat p.30 'soolist võrdsust mõõdetakse naiste ja meeste osakaaluna...') y 'diskrimineerimine' genérica (riesgo p.20; proyecto de discriminación algorítmica EE-LT p.55, no específico de género). Sin proyecto/cuota/presupuesto/campaña de género; la inclusión se estructura por accesibilidad/erivajadused y territorio.", "ALTA", [EE_WP]),
 "118": ("Sostenibilidad/medioambiente SÍ se aborda con acciones: IA verde/eficiente 'energiasäästliku ehk «rohelise» TI arendamine' (Tegevuskava p.16-17); IA del sector público alineada con 'säästva arengu eesmärgid' (ODS, Valge raamat p.43); 'kestlikkuse tööriist' (herramienta de sostenibilidad, p.38); soluciones para 'kestlikkusele energeetikas, ehituses ja transpordis' (AP p.17); datos selectivos por 'globaalse rohejalajälje vähendamine' (p.13). → 1.", "ALTA", [EE_AP, EE_WP]),
 "119": (">1 mecanismo de participación en la elaboración, con resultados publicados: 'kaks omnibussi uuringut, milles osales kokku 2150 Eesti elanikku' (2 encuestas ómnibus, 2150 residentes) + 'kaasamisintervjuusid, milles osales 220' (220 entrevistas) (Tegevuskava p.6); resultado p.ej. '77% Eesti elanikest suhtub pigem positiivselt' (Valge raamat p.44). 119 mide MECANISMOS (≥2 → 5); el nº de sectores va en 121.", "ALTA", [EE_AP, EE_WP]),
 "121": ("Sectores en la ELABORACIÓN (VR p.8/12, PA p.6): GOBIERNO + PRIVADO (eraettevõtted, ITL, consorcios, teaduspargid) + ACADEMIA (ülikoolid, Eesti Keele Instituut) + ONG/sin fines de lucro (vabaühendused, p.8) + PÚBLICO GENERAL (2150 residentes en 2 encuestas ómnibus + 220 entrevistas, PA p.6; el VR incorpora 'kodaniku perspektiive', p.8). Contando ONG y público como sectores distintos → Gob+4 = 5. (Si el 4º sector ILIA = organismos internacionales, sería 4: ninguno co-creó el documento.)", "ALTA", [EE_WP, EE_AP]),
 "122": ("Sectores en la IMPLEMENTACIÓN (VR p.12/33): GOBIERNO (juhtrühmad liderados por MKM + ministerios + RIA + Statistikaamet + gobiernos locales + centros de competencia) + PRIVADO (erasektor; empresas vía AIRE) + ACADEMIA (universidades asociadas vía AIRE; Eesti Keele Instituut); las juhtrühmad suman 'avaliku sektori välised võtmepartnerid' y rinden cuentas al público vía 'andmete võrgustiku avatud kohtumine'. → Gob+3 = 4 (estricto por sectores nombrados privado+academia: Gob+2 = 3).", "MEDIA-ALTA", [EE_WP, EE_AP]),
 "123": (">1 institución: MKM/MEAC + Government Office (Riigikantselei) + RIA + Eesti.ai.", "ALTA", [EE_RIIGI, EE_VALITSUS, EE_OECD]),
 "124": ("Steering group MKM/MEAC + grupo interministerial Eesti.ai.", "ALTA", [EE_DIGW, EE_RIIGI]),
 "125": ("Estonia NO figura en SC 42 (ni P ni O) según la lista oficial JTC1 → 0. Confianza MEDIA: verificar a mano en iso.org.", "MEDIA · DUDA", [ISO42, JTC1_SC42]),
 "126": ("Participante (P-member) en SC 27.", "ALTA", [ISO27]),
 "127": ("OECD AI Principles + EU Coordinated Plan + CoE Convention (vía UE) = 2+. GPAI: Estonia NO es miembro.", "ALTA", [EE_OECDAIP, OECDAIP]),
 "128": ("EU AI Act (Reg. UE 2024/1689); el Tegevuskava 2024-26 'on ühtlasi Eesti riiklik tehisintellekti strateegia EL kooskõlastatud tegevuskava mõistes' (p.4). Sin ley nacional propia de IA.", "ALTA", [EE_ACT, AIACT, EE_AP]),
 "129": ("EU AI Act = enfoque por riesgo; el Valge raamat prevé 'Algoritmi mõjuhinnangu mudel' (evaluación de impacto algorítmico) (p.52). → 1.", "ALTA", [AIACT, EE_WP]),
 "130": ("Estonia incluye un SANDBOX nacional de IA/datos en su estrategia: 'Tehisintellekti liivakasti pakkumine era- ja avaliku sektori asutustele' (Valge raamat p.52); + sandbox transfronterizo EE-FI. → 1.", "ALTA", [EE_WP, EE_SANDBOX]),
 "131": ("GDPR (UE) + Personal Data Protection Act (2018, vig. 15-ene-2019).", "ALTA", [DLP("EE"), EE_RT]),
 "132": ("Andmekaitse Inspektsioon (AKI) — Data Protection Inspectorate.", "ALTA", [EE_AKI, "https://www.dlapiperdataprotection.com/?t=authority&c=EE"]),
 "133": ("NO ENCONTRADO por pilar; GCI 2024 = Tier 1 (total ~95,04). Pilares solo en anexo PDF.", "MANUAL", [GCI, GCI_D360]),
 "134": ("NO ENCONTRADO por pilar (Tier 1).", "MANUAL", [GCI, GCI_D360]),
 "135": ("NO ENCONTRADO por pilar (Tier 1).", "MANUAL", [GCI, GCI_D360]),
 "136": ("NO ENCONTRADO por pilar (Tier 1).", "MANUAL", [GCI, GCI_D360]),
 "137": ("NO ENCONTRADO por pilar (Tier 1).", "MANUAL", [GCI, GCI_D360]),
 "138": ("NO ENCONTRADO; Estonia está cubierta por GIRAI, pero el puntaje por área se renderiza en portal JS/PDF.", "MANUAL", [GIRAI]),
 "139": ("NO ENCONTRADO (portal JS/PDF).", "MANUAL", [GIRAI]),
 "144": ("80,71 (80,7064) en 'Affordable & clean energy', NRI ed. 2025.", "MEDIA-ALTA", [EE_NRI]),
 "145": ("55,75 % (2024) / 59,57 % (2025) de generación renovable. Determinístico: 3,49/6,26 TWh = 55,75 %. ERNC ≈ renovables (hidro ~0,5 %).", "ALTA", [OWID, EMBER]),
}

# ================= SINGAPUR =================
GOBDET["SG"] = {
 "103": ("NAIS (2019) + NAIS 2.0 (2023) vigente.", "ALTA", [SG_SN, SG_NAIS, SG_MDDI]),
 "104": ("NAIS 2.0 = dic-2023; el Update de may-2026 (10 prioridades refrescadas) se cuenta como estrategia vigente nueva (decisión del operador 2026-06-16) → tramo 2024-25.", "ALTA · decisión operador", [SG_UPD, SG_MDDI]),
 "105": ("2019 → 2.0 (2023) → Update may-2026.", "ALTA", [SG_UPD, SG_OECD]),
 "106": ("Supervisión inter-agencias + métricas + NAIC. Sin texto primario íntegro → PRELIM.", "MEDIA · PRELIM", [SG_SN, SG_NAIS]),
 "107": ("'More than S$1 billion' en 5 años.", "ALTA", [SG_PR, SG_MDDI]),
 "108": ("3 sistemas, 10 enablers y 15 Acciones.", "ALTA", [SG_NAIS, SG_INFO]),
 "109": ("'Trusted & responsible AI'; Model AI Governance Framework + AI Verify.", "ALTA", [SG_NAIS, SG_MGF]),
 "110": ("Sistema 'Infrastructure'; cómputo.", "ALTA", [SG_NAIS, SG_INFO]),
 "111": ("Sistema 'Talent'; AI Singapore.", "ALTA", [SG_NAIS, SG_AISG]),
 "112": ("Enabler de datos; PDPC.", "ALTA", [SG_NAIS, SG_PDPC]),
 "113": ("Smart Nation / Digital Government.", "ALTA", [SG_SN]),
 "114": ("Enabler de industria; LLM nacional.", "ALTA", [SG_NAIS, SG_INFO]),
 "115": ("Enabler de investigación; A*STAR/AISG.", "ALTA", [SG_NAIS, SG_AISG]),
 "116": ("Enabler de partnerships internacionales; lidera el WG de ASEAN.", "ALTA", [SG_NAIS, SG_ASEAN]),
 "117": ("NO se halló componente de género con plan → 0.", "MEDIA · NO ENCONTRADO", [SG_NAIS]),
 "118": ("'Green AI'; Sustainable Tropical Data Centre Testbed.", "MEDIA · PRELIM", [SG_NAIS]),
 "119": ("No se halló consulta ciudadana en la elaboración de NAIS 2.0 (sí en el MGF GenAI, otro instrumento) → 1.", "MEDIA · NO ENCONTRADO", [SG_IMDA, SG_MGFGEN]),
 "121": ("Elaboración: Gob (SNDGG/MDDI) + industria + investigación (Gob+2).", "MEDIA · PRELIM", [SG_NAIS, SG_MDDI]),
 "122": ("Implementación: Gob + industria + academia + AI Verify Foundation (Gob+3).", "MEDIA · PRELIM", [SG_SN, SG_AIV]),
 "123": (">1 institución: SNDGG, IMDA, AISG, A*STAR, PDPC, AI Verify Fdn y NAIC (PM, feb-2026).", "ALTA", [SG_SN, SG_MDDI]),
 "124": ("NAIC + SNDGG + working groups.", "ALTA", [SG_SN]),
 "125": ("Participante (P-member) en SC 42.", "ALTA", [ISO42, JTC1_SC42]),
 "126": ("Participante (P-member) en SC 27.", "ALTA", [ISO27]),
 "127": ("OECD AI Principles + GPAI + ASEAN (lidera WG) + UNESCO ref. + Singapore Consensus 2025 = 2+.", "ALTA", [OECDAIP, SG_ASEAN]),
 "128": ("No tiene ley dura de IA; gobierna por soft law (MGF 2019/20, MGF GenAI 2024, Agentic 2026) → 1. (No es debilidad: marco voluntario muy maduro.)", "ALTA", [SG_MGF, SG_AIV]),
 "129": ("La clasificación de riesgo está en el marco voluntario (MGF GenAI: 9 dimensiones), no en una ley.", "MEDIA · PRELIM", [SG_MGFGEN]),
 "130": ("AI Verify; Global AI Assurance Pilot; GenAI Sandbox.", "ALTA", [SG_AIV]),
 "131": ("Personal Data Protection Act 2012 (+ enmienda 2020).", "ALTA", [SG_DLP, SG_SSO]),
 "132": ("Personal Data Protection Commission (PDPC).", "ALTA", [SG_PDPC]),
 "133": ("NO ENCONTRADO por pilar; GCI 2024 = Tier 1 (total ~99,86). Pilares solo en anexo PDF.", "MANUAL", [GCI, GCI_D360]),
 "134": ("NO ENCONTRADO por pilar (Tier 1).", "MANUAL", [GCI, GCI_D360]),
 "135": ("NO ENCONTRADO por pilar (Tier 1).", "MANUAL", [GCI, GCI_D360]),
 "136": ("NO ENCONTRADO por pilar (Tier 1).", "MANUAL", [GCI, GCI_D360]),
 "137": ("NO ENCONTRADO por pilar (Tier 1).", "MANUAL", [GCI, GCI_D360]),
 "138": ("NO ENCONTRADO; SG cubierto por GIRAI (score global 53,77). Por área: portal JS/PDF; alt. LIRNEasia Fig.19.", "MANUAL", [GIRAI, SG_LIRNE]),
 "139": ("NO ENCONTRADO (portal JS/PDF; alt. LIRNEasia).", "MANUAL", [GIRAI, SG_LIRNE]),
 "144": ("86,87 (86,8722) en 'Affordable & clean energy', NRI ed. 2025.", "MEDIA-ALTA", [SG_NRI]),
 "145": ("4,93 % (2024) / 5,49 % (2025) de generación renovable. Determinístico: 2,94/59,61 TWh = 4,93 %. Hidro 0 %.", "ALTA", [OWID, EMBER]),
}

# ================= ALEMANIA =================
GOBDET["DE"] = {
 "103": ("KI-Strategie 2018 + Fortschreibung 2020 + Aktionsplan KI 2023.", "ALTA", [DE_KI2018, DE_KI2020, DE_AKT_PDF]),
 "104": ("Documento vigente más reciente = Aktionsplan 2023 (base 2018/2020) → tramo 2022-23.", "ALTA", [DE_AKT_PDF, DE_AKT_PAGE]),
 "105": ("2018 → 2020 → 2023 + evaluación OCDE 2023-24.", "ALTA", [DE_KI2020, DE_OECD]),
 "106": ("Evaluación por 3 ministerios + benchmarking OCDE.", "ALTA", [DE_OECD, DE_OECD_WONK]),
 "107": ("€5.000 millones hasta 2025 (Fortschreibung 2020).", "ALTA", [DE_KI2020, DE_KISTRAT]),
 "108": ("Campos de acción con medidas (Aktionsplan: 11 campos, 50+20 medidas).", "ALTA", [DE_AKT_PDF, DE_AKT_PAGE]),
 "109": ("IA confiable, centrada en el ser humano; Plattform Lernende Systeme (ética).", "ALTA", [DE_KI2018, DE_PLS]),
 "110": ("Cómputo de IA (prioridad del Aktionsplan 2023).", "ALTA", [DE_AKT_PDF]),
 "111": ("Skills, cátedras de IA, formación profesional.", "ALTA", [DE_AKT_PDF, DE_KISTRAT]),
 "112": ("Campo de acción de datos/disponibilidad. Sin texto primario → PRELIM.", "MEDIA · PRELIM", [DE_KISTRAT, DE_AKT_PDF]),
 "113": ("Campo de sector público/administración digital. PRELIM.", "MEDIA · PRELIM", [DE_KISTRAT]),
 "114": ("'AI made in Germany'; Mittelstand/PYMEs.", "ALTA", [DE_AKT_PDF, DE_KISTRAT]),
 "115": ("Núcleo: investigación, centros de competencia, cátedras.", "ALTA", [DE_AKT_PDF, DE_OECD]),
 "116": ("'AI made in Europe'; Espacio Europeo de Investigación; EU Coordinated Plan.", "MEDIA", [DE_EUPLAN, DE_AKT_EU]),
 "117": ("Análisis externos: la estrategia 'apenas dio rol al género' → 0.", "MEDIA · PRELIM", ["https://www.gleichstellungsbericht.de", DE_KI2018]),
 "118": ("La Fortschreibung 2020 añade clima/medio ambiente. PRELIM.", "MEDIA · PRELIM", [DE_KI2020, DE_KISTRAT]),
 "119": ("Consulta a asociaciones/talleres (2018); sin mecanismo ciudadano con resultados publicados → 2.", "MEDIA · PRELIM", [DE_KI2018]),
 "121": ("Elaboración: Gob (3 min.) + academia + industria + sociedad civil (PLS, ~200 expertos) (Gob+3).", "MEDIA · PRELIM", [DE_PLS, DE_PLS_ACA]),
 "122": ("Implementación: PLS (acatech) academia + industria + sociedad civil + estados (Gob+3).", "MEDIA · PRELIM", [DE_PLS_ACA, DE_PLS]),
 "123": (">1 institución: 3 ministerios líderes + PLS + Bundesnetzagentur (autoridad EU AI Act).", "ALTA", [DE_OECD, DE_BNETZA, DE_PLS]),
 "124": ("3 ministerios + diálogo federación-estados.", "ALTA", [DE_OECD, DE_OECD_WONK]),
 "125": ("Participante (P-member, DIN) en SC 42.", "ALTA", [ISO42, JTC1_SC42]),
 "126": ("Participante (P-member, DIN; secretaría) en SC 27.", "ALTA", [ISO27]),
 "127": ("OECD AI Principles + GPAI (fundador) + UNESCO + CoE (vía UE) + Plan UE = 2+.", "ALTA", [GPAI, OECDAIP, DE_EUPLAN]),
 "128": ("EU AI Act + ley nacional de implementación KI-MIG (borrador del Gabinete feb-2026).", "ALTA", [DE_KIMIG, AIACT]),
 "129": ("EU AI Act (prohibido/alto/limitado/mínimo).", "ALTA", [AIACT]),
 "130": ("Bundesnetzagentur: KI-Reallabore (sandbox) + AI Service Desk (2025-26).", "ALTA", [DE_BNETZA_LAB, DE_BNETZA]),
 "131": ("GDPR + BDSG.", "ALTA", [DLP("DE"), DE_BFDI]),
 "132": ("BfDI + 16 autoridades de los Länder.", "ALTA", [DE_BFDI]),
 "133": ("NO ENCONTRADO por pilar; GCI 2024 = Tier 1 (total ~97,85). Pilares solo en anexo PDF.", "MANUAL", [GCI, GCI_D360]),
 "134": ("NO ENCONTRADO por pilar (Tier 1).", "MANUAL", [GCI, GCI_D360]),
 "135": ("NO ENCONTRADO por pilar (Tier 1).", "MANUAL", [GCI, GCI_D360]),
 "136": ("NO ENCONTRADO por pilar (Tier 1).", "MANUAL", [GCI, GCI_D360]),
 "137": ("NO ENCONTRADO por pilar (Tier 1; indicio: pilar más bajo de DE).", "MANUAL", [GCI, GCI_D360]),
 "138": ("NO ENCONTRADO; DE cubierto por GIRAI; puntaje por área en portal JS/PDF.", "MANUAL", [GIRAI]),
 "139": ("NO ENCONTRADO (portal JS/PDF).", "MANUAL", [GIRAI]),
 "144": ("86,44 en 'Affordable & clean energy', NRI ed. 2025.", "MEDIA-ALTA", [DE_NRI]),
 "145": ("58,64 % (2024) / 59,09 % (2025) renovable total. Excl. toda hidro 53,84 %; hidro 4,81 %. (ERNC excl. gran hidro: efecto menor.)", "ALTA", [OWID, EMBER]),
}

# ================= ESPAÑA =================
GOBDET["ES"] = {
 "103": ("Estrategia de IA 2024 (continúa la ENIA 2020).", "ALTA", [ES_M24, ES_D24, ES_ENIA_M]),
 "104": ("Estrategia de IA 2024 → tramo 2024-25.", "ALTA", [ES_M24, ES_P24]),
 "105": ("La de 2024 actualiza la ENIA 2020.", "ALTA", [ES_P24, ES_ENIA_P]),
 "106": ("Comisión Interministerial + Informe de avances ENIA 2023.", "MEDIA-ALTA", [ES_ENIA_INF]),
 "107": ("€1.500M (2024-25) + €600M (ENIA).", "ALTA", [ES_P24, ES_ENIA_M]),
 "108": ("3 ejes / 8 palancas (ENIA: 6 ejes/30 medidas).", "ALTA", [ES_D24, ES_P24]),
 "109": ("'Entorno de confianza'; AESIA; anteproyecto de ley.", "ALTA", [ES_AESIA, ES_LEY_N]),
 "110": ("Supercomputación (MareNostrum +€90M).", "ALTA", [ES_P24, ES_ALIA_BSC]),
 "111": ("Talento; pymes (Kit Digital/Consulting); AESIA.", "ALTA", [ES_P24, ES_AESIA]),
 "112": ("Eje de datos; Estrategia Nacional de Datos; modelo ALIA.", "ALTA", [ES_ALIA_AESIA, ES_ALIA_BSC]),
 "113": ("IA en las AAPP; GobTechLab.", "ALTA", [ES_M24, ES_D24]),
 "114": ("Productividad de empresas; pymes/startups; sandbox.", "ALTA", [ES_P24, ES_SBX_BOE]),
 "115": ("Estrategia de I+D+I en IA; centros (HiTZ, CiTIUS).", "ALTA", [ES_P24, ES_D24]),
 "116": ("Sandbox abierto a la UE; Plan Coordinado UE; GPAI; OCDE.", "ALTA", [ES_SBX_BOE, OECDAIP]),
 "117": ("La ENIA aborda la 'brecha de género en empleo y liderazgo' (mención transversal) → 1. PRELIM.", "MEDIA-ALTA · PRELIM", [ES_ENIA_P, ES_ENIA_M]),
 "118": ("'Crecimiento sostenible'; Programa Nacional de Algoritmos Verdes (2022).", "ALTA", [ES_ALGV_M, ES_ALGV]),
 "119": ("GobTechLab; audiencia pública del anteproyecto → 3. PRELIM.", "MEDIA · PRELIM", [ES_LEY_T, ES_LEY_N]),
 "121": ("Elaboración: Gob + GTIA/expertos + academia + UE (Gob+3).", "MEDIA · PRELIM", [ES_ENIA_P, ES_M24]),
 "122": ("Implementación: convenio con 15 instituciones + Comisión + privados (Gob+3).", "MEDIA-ALTA", [ES_M24, ES_D24]),
 "123": ("SEDIA + AESIA (1ª agencia de supervisión de IA de la UE; agencia independiente).", "ALTA", [ES_AESIA_BOE, ES_AESIA]),
 "124": ("Comisión Interministerial (preside SEDIA).", "ALTA", [ES_M24, ES_ENIA_INF]),
 "125": ("Participante (P-member, UNE) en SC 42.", "ALTA", [ISO42]),
 "126": ("Participante (P-member, UNE) en SC 27.", "ALTA", [ISO27]),
 "127": ("OECD AI Principles + GPAI + CoE (vía UE) + UNESCO + Plan UE = 2+.", "ALTA", [OECDAIP, GPAI]),
 "128": ("EU AI Act + ley nacional (anteproyecto mar-2025 → proyecto de ley may-2026).", "ALTA", [ES_LEY_N, ES_LEY_T, AIACT]),
 "129": ("EU AI Act (4 niveles); AESIA con sección de alto riesgo.", "ALTA", [ES_AESIA, AIACT]),
 "130": ("1er sandbox de IA de la UE (RD 817/2023; 2022→jun-2026; ~€4,3M; 44 solicitudes).", "ALTA", [ES_SBX_BOE]),
 "131": ("GDPR + LOPDGDD (LO 3/2018).", "ALTA", [DLP("ES"), ES_AEPD]),
 "132": ("AEPD.", "ALTA", [ES_AEPD]),
 "133": ("Legal = 20/20 (GCI 2024). Total 99,74 / Tier 1 (4º mundial).", "ALTA", [ES_GCI, GCI_D360]),
 "134": ("Técnico = 20/20 (GCI 2024).", "ALTA", [ES_GCI, GCI_D360]),
 "135": ("Organizacional = 20/20 (GCI 2024).", "ALTA", [ES_GCI, GCI_D360]),
 "136": ("Desarrollo de capacidades = 19,74/20 (GCI 2024).", "ALTA", [ES_GCI, GCI_D360]),
 "137": ("Cooperación = 20/20 (GCI 2024).", "ALTA", [ES_GCI, GCI_D360]),
 "138": ("NO ENCONTRADO; ES cubierta por GIRAI; puntaje por área en portal JS/PDF.", "MANUAL", [GIRAI]),
 "139": ("NO ENCONTRADO (portal JS/PDF).", "MANUAL", [GIRAI]),
 "144": ("NO OBTENIDO el subíndice (rank NRI global 25); leer en la página país / PDF 2025.", "MANUAL", [ES_NRI]),
 "145": ("57,34 % (2024) / 55,86 % (2025) renovable total. Excl. toda hidro 45,09 %; hidro 12,25 % → si ILIA excluyera gran hidro, baja bastante.", "ALTA", [OWID, EMBER]),
}

# ================= PORTUGAL =================
GOBDET["PT"] = {
 "103": ("ANIA 2026-2030 (+ AI Portugal 2030 previa).", "ALTA", [PT_DR, PT_AIP_OECD]),
 "104": ("ANIA publicada en enero 2026 → tramo 2024-26.", "ALTA", [PT_DR, PT_OBS]),
 "105": ("La ANIA actualiza AI Portugal 2030.", "ALTA", [PT_DIGITAL, PT_AIP_INCODE]),
 "106": ("'Modelo de monitorização'; Conselho para o Digital na AP.", "ALTA", [PT_DR]),
 "107": (">€400M hasta 2030 (+€25M sector público).", "ALTA", [PT_GOV, PT_OBS]),
 "108": ("PAANIA 2026-2030: 32 iniciativas con responsables.", "ALTA", [PT_DR, PT_DIGITAL]),
 "109": ("Eje 'Responsabilidade e Ética'; 'inovação responsável'.", "ALTA", [PT_DR, PT_COMPETE]),
 "110": ("Eje 'Infraestrutura e Dados' (AI Factory, supercomputación).", "ALTA", [PT_COMPETE, PT_DR]),
 "111": ("Eje 'Talento e Competências' (literacia, reskilling).", "ALTA", [PT_DR, PT_COMPETE]),
 "112": ("Eje 'Infraestrutura e Dados' (governança de datos).", "ALTA", [PT_DR]),
 "113": ("IA en la AP (compras, faturas, recrutamento); €25M.", "ALTA", [PT_GOV, PT_OBS]),
 "114": ("Eje 'Inovação e Adoção'; PME y startups.", "ALTA", [PT_COMPETE, PT_DR]),
 "115": ("'Proteger a investigação fundamental em IA'; FCT.", "ALTA", [PT_AIP_OECD, PT_AIP_INCODE]),
 "116": ("EU Coordinated Plan; AI Factory europea; bilateral (India).", "MEDIA-ALTA", [PT_DR, OECDAIP]),
 "117": ("No verificado como eje en la ANIA (solo principio en la EDN) → 0. PRELIM.", "MEDIA · PRELIM", [PT_DIGITAL, PT_DR]),
 "118": ("No verificado como eje en la ANIA (solo principio en la EDN) → 0. PRELIM.", "MEDIA · PRELIM", [PT_DIGITAL, PT_DR]),
 "119": ("3 sesiones públicas (Lisboa/Évora/Porto) + participa.gov.pt + consultalex; resultados incorporados → 4.", "ALTA", [PT_AUSC_D, PT_AUSC_G]),
 "121": ("Elaboración: Gob + academia + empresas/startups + AP + ciudadanos (Gob+4).", "ALTA", [PT_AUSC_G, PT_CMS]),
 "122": ("Implementación: universidades + centros I+D + empresas/startups + AP (Gob+3). PRELIM.", "MEDIA-ALTA · PRELIM", [PT_COMPETE]),
 "123": (">1 institución: AMA (coord.) + FCT + ANACOM (autoridad AI Act) + INCoDe.2030 + CNPD.", "ALTA", [PT_AIP_OECD, PT_PUBLICO, PT_CMS]),
 "124": ("Modelo de governança (RCM 2/2026); Conselho para o Digital na AP.", "ALTA", [PT_DR]),
 "125": ("Observador (O-member, IPQ) en SC 42 → 1.", "ALTA", [ISO42, JTC1_SC42]),
 "126": ("Observador (O-member, IPQ) en SC 27 → 1.", "ALTA", [ISO27]),
 "127": ("OECD AI Principles + UNESCO + EU Coordinated Plan (CoE vía UE) = 2+. GPAI: PT no es miembro individual.", "ALTA", [OECDAIP, UNESCO]),
 "128": ("EU AI Act; ANACOM designada autoridad (sept-2025); sin ley nacional autónoma.", "ALTA", [PT_PUBLICO, PT_CMS, AIACT]),
 "129": ("EU AI Act (inaceptable/alto/limitado/mínimo).", "ALTA", [AIACT]),
 "130": ("Obligación del EU AI Act (art. 57, ago-2026) bajo ANACOM. PRELIM.", "MEDIA-ALTA · PRELIM", [PT_AIACT57, PT_PUBLICO]),
 "131": ("GDPR + Lei 58/2019.", "ALTA", [DLP("PT"), PT_CNPD]),
 "132": ("CNPD.", "ALTA", [PT_CNPD]),
 "133": ("NO ENCONTRADO por pilar; GCI 2024 = Tier 1 (total ~99,86). Pilares solo en anexo PDF.", "MANUAL", [GCI, GCI_D360]),
 "134": ("NO ENCONTRADO por pilar (Tier 1).", "MANUAL", [GCI, GCI_D360]),
 "135": ("NO ENCONTRADO por pilar (Tier 1).", "MANUAL", [GCI, GCI_D360]),
 "136": ("NO ENCONTRADO por pilar (Tier 1).", "MANUAL", [GCI, GCI_D360]),
 "137": ("NO ENCONTRADO por pilar (Tier 1).", "MANUAL", [GCI, GCI_D360]),
 "138": ("NO ENCONTRADO; PT cubierto por GIRAI; puntaje por área en portal JS/PDF.", "MANUAL", [GIRAI]),
 "139": ("NO ENCONTRADO (portal JS/PDF).", "MANUAL", [GIRAI]),
 "144": ("88,16 en 'Affordable & clean energy' (overall NRI 61,54; rank 32), ed. 2025.", "MEDIA-ALTA", [PT_NRI]),
 "145": ("85,19 % (2024) / 80,95 % (2025) renovable total. Excl. toda hidro 53,69 %; hidro 31,50 % → si ILIA excluyera gran hidro, baja mucho.", "ALTA", [OWID, EMBER]),
}

# ---- Segundas fuentes verificadas (ninguna celda queda con una sola URL) ----
# URLs del compendio FUENTES_*.md y de búsqueda (jun-2026). Solo enlaces vistos en resultados.
AIACT_REF = "https://artificialintelligenceact.eu"
AIACT_SANDBOX = "https://artificialintelligenceact.eu/ai-regulatory-sandbox-approaches-eu-member-state-overview/"
WIKI_SC27 = "https://en.wikipedia.org/wiki/ISO/IEC_JTC_1/SC_27"
GIRAI_CORR = "https://girai-report-2024-corrected-edition.tiiny.site/"
GLOBALCENTER = "https://www.globalcenter.ai/"
NRI_FULL = "https://download.networkreadinessindex.org/reports/data/2025/nri-2025.pdf"
def DLPA(cc): return f"https://www.dlapiperdataprotection.com/?t=authority&c={cc}"

def _add(cc, idt, *urls):
    j, c, u = GOBDET[cc][idt]
    GOBDET[cc][idt] = (j, c, u + [x for x in urls if x not in u])

for _cc in GOBDET:                       # ISO SC 27: espejo con lista de miembros
    _add(_cc, "126", WIKI_SC27)
for _cc in ("EE", "DE", "ES", "PT"):     # GIRAI: edición corregida + editor (Global Center on AI)
    _add(_cc, "138", GIRAI_CORR); _add(_cc, "139", GLOBALCENTER)
_add("ES", "125", JTC1_SC42)
for _cc in ("SG", "DE", "ES", "PT"):     # Autoridad de datos: ficha DLA Piper (autoridad)
    _add(_cc, "132", DLPA(_cc))
_add("ES", "130", AIACT_SANDBOX); _add("EE", "130", AIACT_SANDBOX); _add("SG", "130", SG_MGFGEN)
_add("SG", "129", SG_AIV); _add("DE", "129", AIACT_REF); _add("PT", "129", AIACT_REF)
_add("ES", "106", ES_M24); _add("PT", "106", PT_DIGITAL); _add("PT", "112", PT_DIGITAL)
_add("PT", "124", PT_DIGITAL); _add("PT", "122", PT_CMS)
_add("DE", "110", DE_KISTRAT); _add("DE", "113", DE_AKT_PDF); _add("DE", "119", DE_KISTRAT)
_add("SG", "113", SG_NAIS); _add("SG", "118", SG_INFO); _add("SG", "124", SG_MDDI)
_add("EE", "117", EE_FACT); _add("SG", "117", SG_SN)   # género NO ENCONTRADO: 2ª fuente que tampoco lo recoge
_add("EE", "144", "https://download.networkreadinessindex.org/reports/countries/2025/estonia.pdf")
_add("SG", "144", "https://download.networkreadinessindex.org/reports/countries/2025/singapore.pdf")
_add("ES", "144", "https://download.networkreadinessindex.org/reports/countries/2025/spain.pdf")
_add("DE", "144", NRI_FULL); _add("PT", "144", NRI_FULL)
