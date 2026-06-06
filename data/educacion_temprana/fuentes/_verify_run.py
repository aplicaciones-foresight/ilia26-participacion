#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifica las citas verbatim del cierre de educacion_temprana.

Reusa src/verify_verbatim.py (normalizar / es_subcadena).
"""
from __future__ import annotations
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "src"))

from verify_verbatim import normalizar, es_subcadena  # noqa: E402


CITAS = [
    # (id, archivo, cita, ubicacion)
    (
        "ES-A1-saberes-C",
        os.path.join(HERE, "ES", "A1.txt"),
        "Aplicaciones informáticas sencillas, para ordenador y dispositivos móviles, e introducción a la inteligencia artificial.",
        "RD 217/2022 (ESO) — Anexo II — «Tecnología y Digitalización» — Saberes básicos · C. Pensamiento computacional, programación y robótica",
    ),
    (
        "ES-A1-criterio-5.2",
        os.path.join(HERE, "ES", "A1.txt"),
        "5.2 Programar aplicaciones sencillas para distintos dispositivos (ordenadores, dispositivos móviles y otros) empleando los elementos de programación de manera apropiada y aplicando herramientas de edición, así como módulos de inteligencia artificial que añadan funcionalidades a la solución.",
        "RD 217/2022 (ESO) — Anexo II — «Tecnología y Digitalización» — Criterios de evaluación · Competencia específica 5",
    ),
    (
        "ES-A2-saberes-E",
        os.path.join(HERE, "ES", "A2.txt"),
        "Inteligencia artificial, big data, bases de datos distribuidas y ciberseguridad.",
        "RD 243/2022 (Bachillerato) — Anexo II — «Tecnología e Ingeniería II» — Saberes básicos · E. Sistemas informáticos emergentes",
    ),
    (
        "ES-A2-criterio-5.1",
        os.path.join(HERE, "ES", "A2.txt"),
        "5.1 Controlar el funcionamiento de sistemas tecnológicos y robóticos, utilizando lenguajes de programación informática y aplicando las posibilidades que ofrecen las tecnologías emergentes, tales como inteligencia artificial, internet de las cosas, big data",
        "RD 243/2022 (Bachillerato) — Anexo II — «Tecnología e Ingeniería I» — Criterios de evaluación · Competencia específica 5",
    ),
    (
        "DE-A3-lernbereich4-titulo",
        os.path.join(HERE, "DE", "A3.txt"),
        "Künstliche Intelligenz (ca. 16 Std.)",
        "LehrplanPLUS Bayern · Gymnasium · Jhst. 11 · Informatik (NTG) · Lernbereich 4",
    ),
    (
        "DE-A3-kompetenzerwartung-KI",
        os.path.join(HERE, "DE", "A3.txt"),
        "diskutieren Ansätze zur Definition des Begriffs Künstliche Intelligenz (KI), beschreiben verschiedene Grundideen von Verfahren der KI (u. a. maschinelles Lernen) sowie ihre Anwendungsbereiche.",
        "LehrplanPLUS Bayern · Gymnasium · Jhst. 11 · Informatik (NTG) · Lernbereich 4 «Künstliche Intelligenz» · Kompetenzerwartungen",
    ),
    (
        "DE-A4b-inhaltsfeld-KI",
        os.path.join(HERE, "DE", "A4b.txt"),
        "Automaten und künstliche Intelligenz",
        "KLP NRW · Sek I · Klasse 5/6 · Pflichtfach Informatik (Inkrafttreten 2021/22) · Inhaltsfeld",
    ),
    (
        "DE-A4b-schwerpunkte-ML",
        os.path.join(HERE, "DE", "A4b.txt"),
        "Maschinelles Lernen mit Entscheidungsbäumen",
        "KLP NRW · Sek I · Klasse 5/6 · Pflichtfach Informatik · Inhaltsfeld «Automaten und künstliche Intelligenz» · Inhaltliche Schwerpunkte",
    ),
    (
        "DE-A4b-schwerpunkte-NN",
        os.path.join(HERE, "DE", "A4b.txt"),
        "Maschinelles Lernen mit neuronalen Netzen",
        "KLP NRW · Sek I · Klasse 5/6 · Pflichtfach Informatik · Inhaltsfeld «Automaten und künstliche Intelligenz» · Inhaltliche Schwerpunkte",
    ),
    (
        "EE-A5-õpitulemus-6",
        os.path.join(HERE, "EE", "A5.txt"),
        "kirjeldab tehisintellekti ja asjade interneti rakendusviise majanduses, avalikus sektoris, hariduses ja sellega kaasnevaid võimalikke ohtusid",
        "Põhikooli riiklik õppekava · Lisa 10 · Valikõppeaine «Informaatika» · III kooliaste · Teema «Infoühiskonna tehnoloogiad» · Õpitulemus 6",
    ),
    (
        "EE-A5-õppesisu-trendid",
        os.path.join(HERE, "EE", "A5.txt"),
        "Uued tehnoloogiatrendid: tehisintellekt, ava- ja suurandmed.",
        "Põhikooli riiklik õppekava · Lisa 10 · Valikõppeaine «Informaatika» · III kooliaste · Teema «Infoühiskonna tehnoloogiad» · Õppesisu",
    ),
    (
        "EE-A5-õppesisu-IA-IoT",
        os.path.join(HERE, "EE", "A5.txt"),
        "Tehisintellekti ja asjade interneti mõisted, näited, rakendused ja seonduvad riskid.",
        "Põhikooli riiklik õppekava · Lisa 10 · Valikõppeaine «Informaatika» · III kooliaste · Teema «Infoühiskonna tehnoloogiad» · Õppesisu",
    ),
    (
        "SG-A6-5.4.1-AI",
        os.path.join(HERE, "SG", "A6_flow.txt"),
        "Describe Artificial Intelligence (AI) as the ability of a computer to perform complex tasks without constant human guidance and improve its performance as more data is collected.",
        "Computing 7155 O-Level Syllabus (SEAB, 2025) · Module 5 «Impact of Computing» · 5.4 Emerging Technologies · Learning outcome 5.4.1",
    ),
    (
        "SG-A6-5.4.3-ML",
        os.path.join(HERE, "SG", "A6_flow.txt"),
        "Define Machine Learning (ML) as a technique used in AI and explain the difference between ML and traditional programming.",
        "Computing 7155 O-Level Syllabus (SEAB, 2025) · Module 5 «Impact of Computing» · 5.4 Emerging Technologies · Learning outcome 5.4.3",
    ),
    (
        "SG-A6-modules",
        os.path.join(HERE, "SG", "A6.txt"),
        "The syllabus consists of five modules as follows:",
        "Computing 7155 O-Level Syllabus (SEAB, 2025) · Syllabus content · cinco módulos (no hay módulo de IA: la IA es subsección 5.4 dentro del Módulo 5 «Impact of Computing»)",
    ),
]


def main() -> int:
    total = ok = fail = 0
    rows = []
    for ident, ruta, cita, ubic in CITAS:
        total += 1
        with open(ruta, encoding="utf-8") as fh:
            texto = fh.read()
        verdict = es_subcadena(cita, texto, case_sensitive=False)
        if verdict:
            ok += 1
        else:
            fail += 1
        rows.append({
            "id": ident,
            "archivo": os.path.relpath(ruta, ROOT).replace("\\", "/"),
            "ubicacion": ubic,
            "cita": cita,
            "cita_norm_len": len(normalizar(cita)),
            "verbatim_ok": verdict,
        })

    reporte = {
        "total": total,
        "ok": ok,
        "fail": fail,
        "aprobada": fail == 0,
        "items": rows,
    }
    out = os.path.join(HERE, "_verify_report.json")
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(reporte, fh, ensure_ascii=False, indent=2)
    print(json.dumps({k: reporte[k] for k in ("total", "ok", "fail", "aprobada")}))
    for r in rows:
        flag = "OK" if r["verbatim_ok"] else "FAIL"
        print(f"  [{flag}] {r['id']}  ({r['cita_norm_len']} chars)")
    return 0 if reporte["aprobada"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
