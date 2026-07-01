#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Suite sintética del modo 2026 (§8). Casos construidos a mano, una variable a la
vez, con valores esperados explícitos. No requiere la BBDD.
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import calc_engine as ce  # noqa: E402

CFG = {
    "cantidad": {"count_min_level": 2, "thresholds": ce._default_thresholds()},
    "redondeo": {"modo": "solo_final"},
    "continuidad": {"caducidad_anuncio_anios": 2, "anio_referencia_ciclo": 2026},
    "escenarios": {"scenario_activo": "A", "exclusiones_firmes": [], "A": {"exclusiones_adicionales": []}},
}


def caso(pais="AR", nombre="c", tipo_proceso=None, etapa=None, convocante=None,
         nivel=2, ano=2024, desarrollador="", origen="", tipos_ia="", rol="contenido"):
    return {"pais": pais, "caso": nombre, "ano": ano,
            "tipo_proceso": tipo_proceso or [], "etapa": etapa or [],
            "tipo_convocante": convocante or [], "nivel_consolidacion": nivel,
            "rol_IA": rol, "desarrollador": desarrollador, "origen": origen,
            "tipos_ia": tipos_ia, "continuidad": "", "tipo_org": ""}


def _close(a, b, tol=0.5):
    return math.isclose(a, b, abs_tol=tol)


# ---- Tipos de Proceso -------------------------------------------------------
def test_tipos_proceso_un_tipo_20():
    s1, _, _, _ = ce.compute_2026([caso(tipo_proceso=["Gobernanza Colaborativa"])], CFG)
    assert _close(s1["AR"]["tipos"], 20.0)

def test_tipos_proceso_cinco_tipos_100():
    cinco = ["Participación Digital","Gobernanza Colaborativa","Mini públicos",
             "Referendos e Iniciativas Populares","Presupuestos Participativos"]
    s1, _, _, _ = ce.compute_2026([caso(tipo_proceso=cinco)], CFG)
    assert _close(s1["AR"]["tipos"], 100.0)

def test_tipos_proceso_tolera_variantes():
    # "governanza" y "referendos" (formas cortas/legacy) deben normalizar.
    s1, _, _, _ = ce.compute_2026([caso(tipo_proceso=["governanza", "referendos"])], CFG)
    assert _close(s1["AR"]["tipos"], 40.0)  # 2/5


# ---- Etapas -----------------------------------------------------------------
def test_etapas_una_25():
    s1, _, _, _ = ce.compute_2026([caso(etapa=["Análisis"])], CFG)
    assert _close(s1["AR"]["etapas"], 25.0)

def test_etapas_cuatro_100():
    s1, _, _, _ = ce.compute_2026([caso(etapa=["Planificación","Implementación","Análisis","Traducción Política"])], CFG)
    assert _close(s1["AR"]["etapas"], 100.0)


# ---- Continuidad por nivel máximo (§4.2) ------------------------------------
def test_continuidad_solo_anuncios_33():
    # país con solo anuncios -> nivel máx 1 -> 33
    s1, _, _, _ = ce.compute_2026([caso(nivel=1, ano=2026), caso(nombre="d", nivel=1, ano=2025)], CFG)
    assert _close(s1["AR"]["cont"], 33.0)

def test_continuidad_permanente_100():
    s1, _, _, _ = ce.compute_2026([caso(nivel=3)], CFG)
    assert _close(s1["AR"]["cont"], 100.0)

def test_continuidad_nivel_maximo_del_pais():
    # mezcla de niveles 1 y 3 -> toma el máximo (3) -> 100
    s1, _, _, _ = ce.compute_2026([caso(nivel=1, ano=2026), caso(nombre="d", nivel=3)], CFG)
    assert _close(s1["AR"]["cont"], 100.0)

def test_caducidad_anuncio_baja_a_cero():
    # nivel 1 con anuncio de 2020 (>2 años antes de 2026) -> caduca a 0
    s1, _, _, _ = ce.compute_2026([caso(nivel=1, ano=2020)], CFG)
    assert _close(s1["AR"]["cont"], 0.0)


# ---- Organización Convocante (3 sub-componentes: amplitud gub, no-gub, co-convocatoria) ----
# Metodología CENIA v2: conv = (amp_gub/3 + amp_nogub/4 + co_convoc_máx_relativo)/3 *100
def test_convocante_solo_gobierno_co():
    # 3 gubernamentales co-convocando 1 iniciativa -> amp_gub=1, amp_nogub=0,
    # co-convoc = 1 combinación / máx 1 = 1 -> (1 + 0 + 1)/3 *100 = 66.67
    s1, _, _, _ = ce.compute_2026(
        [caso(convocante=["gobierno local","gobierno nacional","otra institución pública"])], CFG)
    assert _close(s1["AR"]["conv"], 100*(1 + 0 + 1)/3)

def test_convocante_un_gub_sin_coconvocatoria():
    # 1 solo convocante -> sin combinación (co-convoc=0): (1/3 + 0 + 0)/3 *100 = 11.11
    s1, _, _, _ = ce.compute_2026([caso(convocante=["gobierno nacional"])], CFG)
    assert _close(s1["AR"]["conv"], 100*(1/3)/3)  # 11.11
    assert s1["AR"]["co_combos"] == 0

def test_convocante_mixto_co():
    # gob nacional + universidad + empresa -> amp_gub=1/3, amp_nogub=2/4, co-convoc=1
    s1, _, _, _ = ce.compute_2026(
        [caso(convocante=["gobierno nacional","universidad","empresa"])], CFG)
    assert _close(s1["AR"]["conv"], 100*((1/3)+(2/4)+1)/3)  # 61.11

def test_convocante_tolera_variantes():
    # "industria"->empresa, "academia"->universidad, "ong"->sociedad civil (3 no-gub, co-convocados)
    s1, _, _, _ = ce.compute_2026([caso(convocante=["industria","academia","ong"])], CFG)
    assert _close(s1["AR"]["conv"], 100*(0/3 + 3/4 + 1)/3)  # 58.33

def test_co_convocatoria_cuenta_combinaciones_dedup():
    # 2 iniciativas con la MISMA combinación {gob nacional, universidad} -> 1 combinación (deduplicada)
    casos = [caso(nombre="a", convocante=["gobierno nacional","universidad"]),
             caso(nombre="b", convocante=["universidad","gobierno nacional"])]
    s1, _, _, _ = ce.compute_2026(casos, CFG)
    assert s1["AR"]["co_combos"] == 1


# ---- Cantidad por umbrales + count_min_level (§6.1) -------------------------
def test_cantidad_diez_casos_100():
    casos = [caso(nombre=f"c{i}", nivel=2) for i in range(10)]
    s1, _, _, _ = ce.compute_2026(casos, CFG)
    assert _close(s1["AR"]["cant"], 100.0)
    assert s1["AR"]["n_cant"] == 10

def test_cantidad_tramos():
    for n, esperado in [(1,25),(3,25),(4,50),(6,50),(7,75),(9,75),(10,100)]:
        casos = [caso(nombre=f"c{i}", nivel=2) for i in range(n)]
        s1, _, _, _ = ce.compute_2026(casos, CFG)
        assert _close(s1["AR"]["cant"], esperado), f"n={n} -> {s1['AR']['cant']} != {esperado}"

def test_count_min_level_filtra_anuncios():
    # 3 anuncios (nivel 1). Con count_min_level=2 no cuentan -> N=0 -> cant=0.
    casos = [caso(nombre=f"c{i}", nivel=1, ano=2026) for i in range(3)]
    s1, _, _, _ = ce.compute_2026(casos, CFG)
    assert s1["AR"]["n_cant"] == 0
    assert _close(s1["AR"]["cant"], 0.0)
    # Con count_min_level=0 sí cuentan -> N=3 -> cant=25.
    cfg0 = {**CFG, "cantidad": {"count_min_level": 0, "thresholds": ce._default_thresholds()}}
    s1b, _, _, _ = ce.compute_2026(casos, cfg0)
    assert s1b["AR"]["n_cant"] == 3
    assert _close(s1b["AR"]["cant"], 25.0)


# ---- Escenarios y frontera apoyo --------------------------------------------
def test_escenario_excluye_caso():
    casos = [caso(nombre="Mantener", nivel=2), caso(nombre="Retirar", nivel=2)]
    cfg = {**CFG, "escenarios": {"scenario_activo": "B", "exclusiones_firmes": [],
            "B": {"exclusiones_adicionales": [{"pais": "AR", "caso": "Retirar"}]}}}
    filtrados, info = ce.aplicar_escenario(casos, cfg)
    assert len(filtrados) == 1 and filtrados[0]["caso"] == "Mantener"
    assert info["scenario"] == "B"

def test_apoyo_se_descarta():
    casos = [caso(nombre="ok", rol="contenido"), caso(nombre="apoyo", rol="apoyo")]
    filtrados, _ = ce.aplicar_escenario(casos, CFG)
    assert len(filtrados) == 1 and filtrados[0]["caso"] == "ok"


# ---- Sub2 idéntico al legacy (no se toca §4.3) ------------------------------
def test_sub2_identico_a_legacy():
    casos = [
        caso(pais="BR", nombre="x", desarrollador="Gobierno, Industria", origen="Nacional, Internacional", tipos_ia="LLM, NLP"),
        caso(pais="CL", nombre="y", desarrollador="Academia", origen="Nacional", tipos_ia="NLP - Tópicos"),
    ]
    _, sub2_26, _, _ = ce.compute_2026(casos, CFG)
    _, sub2_lg, _, _ = ce.compute_full(casos)
    for p in ("BR", "CL"):
        assert round(sub2_26[p]["v"]) == sub2_lg[p]["v"], p


# ---- País sin casos -> todo 0 ----------------------------------------------
def test_pais_vacio_cero():
    s1, s2, ind, _ = ce.compute_2026([caso(pais="BR")], CFG)
    assert s1["AR"]["v"] == 0 and s2["AR"]["v"] == 0 and ind["AR"] == 0


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
