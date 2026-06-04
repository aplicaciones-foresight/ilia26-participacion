#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests de verify_verbatim.py. Ejecutable con pytest o directamente."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import verify_verbatim as vv  # noqa: E402

TEXTO = (
    "El Senado Federal de Brasil implementó IA para marcar respuestas ciudadanas.\n"
    "Los   comentarios   se   agruparon  por  tópicos mediante NLP en la etapa de análisis.\n"
    "La plataforma opera de forma recurrente desde 2023."
)


def test_normalizar_colapsa_espacios():
    assert vv.normalizar("a   b\n\tc") == "a b c"
    assert vv.normalizar("  hola  ") == "hola"
    assert vv.normalizar("nbsp aqui") == "nbsp aqui"


def test_subcadena_exacta_y_normalizada():
    # coincidencia directa
    assert vv.es_subcadena("Senado Federal de Brasil", TEXTO)
    # coincide aunque el texto fuente tenga espacios múltiples
    assert vv.es_subcadena("Los comentarios se agruparon por tópicos", TEXTO)
    # case-insensitive por defecto
    assert vv.es_subcadena("senado federal de brasil", TEXTO)


def test_no_subcadena():
    assert not vv.es_subcadena("Cámara de Diputados", TEXTO)
    assert not vv.es_subcadena("", TEXTO)


def test_verificar_ficha_anula_campo_no_verificable():
    ficha = {
        "caso_id": "BR-test",
        "pasada": "A",
        "tipo_proceso": ["Gobernanza Colaborativa"],
        "rol_IA": "contenido",
        "nivel_consolidacion": 3,
        "evidencia_verbatim": {
            "tipo_proceso": "marcar respuestas ciudadanas",      # OK (subcadena)
            "rol_IA": "agruparon por tópicos mediante NLP",       # OK
            "nivel_consolidacion": "opera de forma trimestral",   # NO está -> anula
        },
        "alertas": [],
    }
    corregida, rep = vv.verificar_ficha(ficha, TEXTO)
    assert rep["ok"] == 2
    assert rep["fallidas"] == 1
    assert corregida["nivel_consolidacion"] is None
    assert any("verbatim_no_verificable:nivel_consolidacion" in a
               for a in corregida["alertas"])
    assert rep["aprobada"] is False
    # la ficha original no se muta
    assert ficha["nivel_consolidacion"] == 3


def test_verificar_ficha_aprobada():
    ficha = {
        "caso_id": "BR-ok",
        "tipo_proceso": ["Gobernanza Colaborativa"],
        "evidencia_verbatim": {"tipo_proceso": "etapa de análisis"},
        "alertas": [],
    }
    _, rep = vv.verificar_ficha(ficha, TEXTO)
    assert rep["aprobada"] is True
    assert rep["fallidas"] == 0


def test_cita_corta_genera_alerta_sin_anular():
    ficha = {
        "caso_id": "BR-corta",
        "rol_IA": "contenido",
        "evidencia_verbatim": {"rol_IA": "NLP"},  # subcadena pero <8 chars
        "alertas": [],
    }
    corregida, rep = vv.verificar_ficha(ficha, TEXTO, {"verbatim": {"min_chars": 8}})
    assert rep["cortas"] == 1
    assert corregida["rol_IA"] == "contenido"  # no se anula
    assert any("verbatim_cita_corta" in a for a in corregida["alertas"])


def test_campo_critico_sin_cita_alerta():
    ficha = {
        "caso_id": "BR-sincita",
        "tipo_convocante": ["gobierno nacional"],
        "evidencia_verbatim": {},  # falta la cita de tipo_convocante
        "alertas": [],
    }
    corregida, _ = vv.verificar_ficha(ficha, TEXTO)
    assert any("verbatim_faltante:tipo_convocante" in a for a in corregida["alertas"])


def _run_all():
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    fallos = 0
    for fn in fns:
        try:
            fn()
            print(f"  ✓ {fn.__name__}")
        except AssertionError as e:
            fallos += 1
            print(f"  ✗ {fn.__name__}: {e}")
    print(f"\n{len(fns)-fallos}/{len(fns)} tests OK")
    return 1 if fallos else 0


if __name__ == "__main__":
    raise SystemExit(_run_all())
