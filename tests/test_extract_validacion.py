#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests del mini-validador de esquema de extract.py."""
import copy
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import extract  # noqa: E402

FICHA_VALIDA = {
    "caso_id": "BR-x", "pais": "BR", "nombre_caso": "Caso X",
    "ano_inicio": "2024", "ano_cierre": None, "estado_actividad": "activo",
    "organizacion_a_cargo": "Senado Federal",
    "tipo_convocante": ["gobierno nacional"],
    "tipo_organizacion": ["Público"],
    "tipo_desarrollador_IA": ["Gobierno"],
    "origen_desarrollador": "Nacional",
    "metodologia_participacion": "Consulta.",
    "tipo_proceso": ["Gobernanza Colaborativa"],
    "etapas_uso_IA": ["Análisis"],
    "familia_IA": ["NLP"],
    "usa_LLM_generativa": "no",
    "funcion_IA": "Agrupa aportes.",
    "rol_IA": "contenido",
    "continuidad": ["Plataforma"],
    "nivel_consolidacion": 2,
    "estado_implementacion": 0.75,
    "usa_IA_en_proceso": "sí",
    "tipo_pogrebinschi": None,
    "model_version": "claude-x",
    "fecha_extraccion": "2026-06-04",
    "pasada": "A",
    "evidencia_verbatim": {
        "pais": "Brasil", "tipo_proceso": "plan", "etapas_uso_IA": "análisis",
        "estado_actividad": "activo", "nivel_consolidacion": "recurrente",
        "tipo_convocante": "Senado", "usa_IA_en_proceso": "IA", "rol_IA": "contenido",
    },
    "urls_fuente": ["https://senado.leg.br/x"],
    "alertas": [],
}


def test_ficha_valida_sin_errores():
    assert extract.validar_ficha(FICHA_VALIDA) == []


def test_enum_invalido_rol_IA():
    f = copy.deepcopy(FICHA_VALIDA); f["rol_IA"] = "otro"
    errs = extract.validar_ficha(f)
    assert any("rol_IA" in e for e in errs)


def test_nivel_fuera_de_rango():
    f = copy.deepcopy(FICHA_VALIDA); f["nivel_consolidacion"] = 5
    errs = extract.validar_ficha(f)
    assert any("nivel_consolidacion" in e for e in errs)


def test_tipo_proceso_item_invalido():
    f = copy.deepcopy(FICHA_VALIDA); f["tipo_proceso"] = ["Inventado"]
    errs = extract.validar_ficha(f)
    assert any("tipo_proceso" in e for e in errs)


def test_falta_clave_critica_en_evidencia():
    f = copy.deepcopy(FICHA_VALIDA); del f["evidencia_verbatim"]["rol_IA"]
    errs = extract.validar_ficha(f)
    assert any("evidencia_verbatim" in e and "rol_IA" in e for e in errs)


def test_pais_patron():
    f = copy.deepcopy(FICHA_VALIDA); f["pais"] = "Brasil"
    errs = extract.validar_ficha(f)
    assert any("pais" in e for e in errs)


def test_fecha_patron():
    f = copy.deepcopy(FICHA_VALIDA); f["fecha_extraccion"] = "04/06/2026"
    errs = extract.validar_ficha(f)
    assert any("fecha_extraccion" in e for e in errs)


def _run_all():
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    fallos = 0
    for fn in fns:
        try:
            fn(); print(f"  ✓ {fn.__name__}")
        except AssertionError as e:
            fallos += 1; print(f"  ✗ {fn.__name__}: {e}")
    print(f"\n{len(fns)-fallos}/{len(fns)} tests OK")
    return 1 if fallos else 0


if __name__ == "__main__":
    raise SystemExit(_run_all())
