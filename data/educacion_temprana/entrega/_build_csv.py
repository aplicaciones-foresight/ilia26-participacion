#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Informe comparado en CSV: dos escenarios (inclusivo/estricto) con sus argumentos,
la cita verbatim, el enlace a la fuente oficial y la PÁGINA del PDF donde validar.
Regla adoptada: INCLUSIVA, confirmada con el equipo ILIA (los cursos electivos se
consideran). El escenario estricto se reporta solo como sensibilidad informativa.
Reutiliza fuentes/_verify_report.json (15/15 verbatim_ok).
Salidas:
  data/educacion_temprana/informe_comparado.csv   (1 fila por cita + Portugal)
  data/educacion_temprana/calculo_comparado.csv    (1 fila por país + promedios)
"""
import csv, json, re, pathlib, shutil, subprocess

BASE = pathlib.Path(__file__).resolve().parents[1]   # data/educacion_temprana
REPORT = json.loads((BASE / "fuentes/_verify_report.json").read_text(encoding="utf-8"))

def alnum(s): return re.sub(r"[^0-9a-zÀ-ɏ]", "", (s or "").casefold())

_HAS_PDFTOTEXT = bool(shutil.which("pdftotext"))
_cache = {}
def pages_text(pdf_rel):
    if pdf_rel in _cache: return _cache[pdf_rel]
    pdf = str(BASE / pdf_rel); pages = []
    if _HAS_PDFTOTEXT:
        try:
            out = subprocess.run(["pdftotext", pdf, "-"], capture_output=True, timeout=120)
            pages = out.stdout.decode("utf-8", "ignore").split("\x0c")
        except Exception:
            pages = []
    if not pages:
        from pypdf import PdfReader
        pages = [(p.extract_text() or "") for p in PdfReader(pdf).pages]
    pages = [alnum(t) for t in pages]; _cache[pdf_rel] = pages; return pages

def find_page(pdf_rel, cita):
    if pdf_rel is None: return "HTML (sin paginación)"
    pages = pages_text(pdf_rel); t = alnum(cita)
    for probe in (t, t[:60], t[:40]):
        if not probe: continue
        for i, pg in enumerate(pages, 1):
            if probe in pg: return str(i)
    return "?"

def src_for(cid):
    return {"ES-A1": "fuentes/ES/A1_RD217-2022_BOE-A-2022-4975_consolidado.pdf",
            "ES-A2": "fuentes/ES/A2_RD243-2022_BOE-A-2022-5521_consolidado.pdf",
            "DE-A3": None,
            "DE-A4b": "fuentes/DE/A4b_KLP_NRW_SekI_Kl5u6_Informatik_2021.pdf",
            "EE-A5": "fuentes/EE/A5_PROK_Lisa10_Informaatika.pdf",
            "SG-A6": "fuentes/SG/A6_Computing_7155_OLvl_2025.pdf"}.get(
            next(k for k in ["ES-A1","ES-A2","DE-A3","DE-A4b","EE-A5","SG-A6"] if cid.startswith(k)))

NOTA_EE = ("Curso ELECTIVO: la IA de Estonia está en la asignatura electiva Informaatika "
           "(valikõppeaine). Conforme a la metodología del ILIA (confirmada con el equipo del "
           "índice), los cursos electivos se consideran parte del currículo nacional -> categoría 5; "
           "aparece como subtema.")
NOTA_SG = ("Curso ELECTIVO: la IA/ML de Singapur está en la asignatura electiva Computing 7155. "
           "Conforme a la metodología del ILIA (confirmada con el equipo del índice), los cursos "
           "electivos se consideran parte del currículo nacional -> categoría 5; aparece como "
           "subtema (sección 5.4).")

PAIS = {
 "ES": dict(pais="España", nivel="ESO (1.º–4.º) + Bachillerato (1.º–2.º)", chile="7º básico – 4º medio",
   ci=5, pi=100, ce=5, pe=100, nota="",
   ai="IA nominal en saberes básicos y criterios de evaluación de RD 217/2022 (ESO) y RD 243/2022 (Bachillerato), normas vinculantes vigentes.",
   ae="Se mantiene en 5: la IA está en «Tecnología y Digitalización» (ESO, materia obligatoria de oferta, cuasi-universal); no es subtema de electiva."),
 "DE": dict(pais="Alemania", nivel="Sek I (Kl. 5–10) + Sek II (Kl. 11–12/13)", chile="5º básico – 4º medio",
   ci=5, pi=100, ce=5, pe=100, nota="",
   ai="IA nominal y vinculante en LehrplanPLUS Bayern (Gym 11.º) y KLP NRW Sek I (Klasse 5/6).",
   ae="Se mantiene en 5: en Bayern la IA es un Lernbereich dedicado (≈16 h) = contenido sustantivo (caveat: obligatorio solo en parte de los Länder/vías)."),
 "EE": dict(pais="Estonia", nivel="Põhikool 7.º–9.º + Gümnaasium 10.º–12.º", chile="8º básico – 4º medio",
   ci=5, pi=100, ce=4, pe=75, nota=NOTA_EE,
   ai="Regla inclusiva (confirmada con ILIA: los cursos electivos se consideran): la IA es contenido del currículo nacional en la asignatura ELECTIVA Informaatika -> categoría 5.",
   ae="(Informativo, NO adoptado) Una lectura estricta lo bajaría a 4: la IA es subtema (1 de 9 õpitulemused) en asignatura electiva, no de cursado universal."),
 "SG": dict(pais="Singapur", nivel="Secondary 1–4/5", chile="8º básico – 3º medio",
   ci=5, pi=100, ce=4, pe=75, nota=NOTA_SG,
   ai="Regla inclusiva (confirmada con ILIA: los cursos electivos se consideran): IA/ML es contenido examinable del syllabus ELECTIVO Computing 7155 -> categoría 5.",
   ae="(Informativo, NO adoptado) Una lectura estricta lo bajaría a 4: IA/ML es subtema (sección 5.4, 5 learning outcomes) en asignatura electiva."),
 "PT": dict(pais="Portugal", nivel="Ensino secundário 10.º–12.º (+ 3.º ciclo 7.º–9.º)", chile="7º básico – 4º medio",
   ci=4, pi=75, ce=4, pe=75, nota="",
   ai="TIC implementado (Aplicações Informáticas B); IA NO vigente (solo en la revisión MECI con horizonte 2027).",
   ae="Igual a 4: sin IA en el currículo vigente; el TIC implementado fija la categoría."),
}

TR = {
 "DE-A3-lernbereich4-titulo": "Inteligencia Artificial (aprox. 16 h lectivas)",
 "DE-A3-kompetenzerwartung-KI": "discuten enfoques para definir el concepto de Inteligencia Artificial (IA), describen distintas ideas básicas de procedimientos de IA (entre otros, aprendizaje automático) y sus campos de aplicación.",
 "DE-A4b-inhaltsfeld-KI": "Autómatas e inteligencia artificial",
 "DE-A4b-schwerpunkte-ML": "Aprendizaje automático con árboles de decisión",
 "DE-A4b-schwerpunkte-NN": "Aprendizaje automático con redes neuronales",
 "EE-A5-õpitulemus-6": "describe la inteligencia artificial y los usos del internet de las cosas en la economía, el sector público y la educación, y los posibles riesgos asociados",
 "EE-A5-õppesisu-trendid": "Nuevas tendencias tecnológicas: inteligencia artificial, datos abiertos y big data.",
 "EE-A5-õppesisu-IA-IoT": "Conceptos, ejemplos, aplicaciones y riesgos asociados de la inteligencia artificial y el internet de las cosas.",
 "SG-A6-5.4.1-AI": "Describir la Inteligencia Artificial (IA) como la capacidad de un computador de realizar tareas complejas sin guía humana constante y mejorar su desempeño a medida que se recopilan más datos.",
 "SG-A6-5.4.3-ML": "Definir el Aprendizaje Automático (ML) como una técnica usada en IA y explicar la diferencia entre ML y la programación tradicional.",
 "SG-A6-modules": "El programa consta de cinco módulos, a saber:",
}
def meta(cid):
    if cid.startswith("ES-A1"): return ("ES","IA","RD 217/2022 (ESO) — Anexo II «Tecnología y Digitalización»","https://www.boe.es/buscar/pdf/2022/BOE-A-2022-4975-consolidado.pdf","fuentes/ES/A1_RD217-2022_BOE-A-2022-4975_consolidado.pdf")
    if cid.startswith("ES-A2"): return ("ES","IA","RD 243/2022 (Bachillerato) — Anexo II «Tecnología e Ingeniería»","https://www.boe.es/buscar/pdf/2022/BOE-A-2022-5521-consolidado.pdf","fuentes/ES/A2_RD243-2022_BOE-A-2022-5521_consolidado.pdf")
    if cid.startswith("DE-A3"): return ("DE","IA","LehrplanPLUS Bayern — Gymnasium Jhst. 11, Informatik (NTG)","https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/11/informatik/ntg","fuentes/DE/A3_LehrplanPLUS_Bayern_Gym11_Informatik_ntg.html")
    if cid.startswith("DE-A4b"): return ("DE","IA","KLP NRW — Sek I, Klasse 5/6, Pflichtfach Informatik (2021)","https://lehrplannavigator.nrw.de/system/files/media/document/file/si_kl5u6_if_klp_2021_07_01.pdf","fuentes/DE/A4b_KLP_NRW_SekI_Kl5u6_Informatik_2021.pdf")
    if cid.startswith("EE-A5"): return ("EE","IA","Põhikooli riiklik õppekava — Lisa 10, Valikõppeaine «Informaatika» (electiva)","https://www.riigiteataja.ee/aktilisa/1080/3202/3005/18m_pohi_lisa10.pdf","fuentes/EE/A5_PROK_Lisa10_Informaatika.pdf")
    if cid.startswith("SG-A6"):
        tipo = "IA" if cid in ("SG-A6-5.4.1-AI","SG-A6-5.4.3-ML") else "TIC/estructura"
        return ("SG",tipo,"Computing 7155 — O-Level Syllabus (SEAB, 2025)","https://www.seab.gov.sg/files/O%20Lvl%20Syllabus%20Sch%20Cddts/2025/7155_y25_sy.pdf","fuentes/SG/A6_Computing_7155_OLvl_2025.pdf")

cols = ["pais","iso2","cat_inclusiva","puntaje_inclusiva","cat_estricta","puntaje_estricta",
        "argumento_inclusiva","argumento_estricta","nota_curso_electivo","tipo","nivel_secundaria",
        "equivalente_chile","documento","ubicacion","pagina_pdf","cita_verbatim","traduccion_es",
        "url_fuente","archivo_local","verificacion"]
rows, miss = [], []
for it in REPORT["items"]:
    cid = it["id"]; iso, tipo, doc, url, loc = meta(cid); P = PAIS[iso]
    pg = find_page(src_for(cid), it["cita"])
    if pg == "?": miss.append(cid)
    rows.append({"pais":P["pais"],"iso2":iso,"cat_inclusiva":P["ci"],"puntaje_inclusiva":P["pi"],
        "cat_estricta":P["ce"],"puntaje_estricta":P["pe"],"argumento_inclusiva":P["ai"],"argumento_estricta":P["ae"],
        "nota_curso_electivo":P["nota"],"tipo":tipo,"nivel_secundaria":P["nivel"],"equivalente_chile":P["chile"],
        "documento":doc,"ubicacion":it["ubicacion"],"pagina_pdf":pg,"cita_verbatim":it["cita"],
        "traduccion_es":TR.get(cid,""),"url_fuente":url,"archivo_local":loc,"verificacion":"verbatim_ok"})

P = PAIS["PT"]
rows.append({"pais":"Portugal","iso2":"PT","cat_inclusiva":4,"puntaje_inclusiva":75,"cat_estricta":4,"puntaje_estricta":75,
    "argumento_inclusiva":P["ai"],"argumento_estricta":P["ae"],"nota_curso_electivo":P["nota"],"tipo":"IA ausente",
    "nivel_secundaria":P["nivel"],"equivalente_chile":P["chile"],
    "documento":"AE Aplicações Informáticas B (12.º) — Aprendizagens Essenciais vigentes",
    "ubicacion":"Dominios D1 (Algoritmia e Programação) + D2 (Multimédia) — sin mención de IA",
    "pagina_pdf":"n/a (verificado por ausencia)",
    "cita_verbatim":"(El currículo vigente no contiene «inteligência artificial»; la IA solo aparece en la revisión MECI con horizonte 2027.)",
    "traduccion_es":"","url_fuente":"https://www.dge.mec.pt/sites/default/files/Curriculo/Aprendizagens_Essenciais/12_aplicacoes_informaticas_b.pdf",
    "archivo_local":"(no descargado; B1 opcional)","verificacion":"verificado_por_ausencia"})

with open(BASE/"informe_comparado.csv","w",encoding="utf-8-sig",newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=cols); w.writeheader(); w.writerows(rows)

cols2 = ["iso2","pais","nivel_secundaria","equivalente_chile","cat_inclusiva","puntaje_inclusiva",
         "argumento_inclusiva","cat_estricta","puntaje_estricta","argumento_estricta","nota_curso_electivo"]
order = ["ES","DE","EE","SG","PT"]; s = []
for iso in order:
    P = PAIS[iso]
    s.append({"iso2":iso,"pais":P["pais"],"nivel_secundaria":P["nivel"],"equivalente_chile":P["chile"],
        "cat_inclusiva":P["ci"],"puntaje_inclusiva":P["pi"],"argumento_inclusiva":P["ai"],
        "cat_estricta":P["ce"],"puntaje_estricta":P["pe"],"argumento_estricta":P["ae"],"nota_curso_electivo":P["nota"]})
pi = sum(PAIS[i]["pi"] for i in order)/5; pe = sum(PAIS[i]["pe"] for i in order)/5
s.append({"iso2":"—","pais":"PROMEDIO DEL GRUPO","nivel_secundaria":"","equivalente_chile":"",
    "cat_inclusiva":"","puntaje_inclusiva":pi,"argumento_inclusiva":"Regla adoptada (ILIA): inclusiva — 4 de 5 países en categoría 5",
    "cat_estricta":"","puntaje_estricta":pe,"argumento_estricta":"Sensibilidad informativa (no adoptada): EE y SG bajan a 4",
    "nota_curso_electivo":"Cursos electivos SÍ se consideran (confirmado con ILIA); nota explícita para EE y SG"})
with open(BASE/"calculo_comparado.csv","w",encoding="utf-8-sig",newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=cols2); w.writeheader(); w.writerows(s)

print(f"informe_comparado.csv: {len(rows)} filas, {len(cols)} columnas")
print(f"calculo_comparado.csv: {len(s)} filas | promedio inclusiva={pi} estricta={pe}")
print("pdftotext:", "sí" if _HAS_PDFTOTEXT else "no -> pypdf")
if miss: print("NO HALLADAS:", miss)
