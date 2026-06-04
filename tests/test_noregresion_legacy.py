#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test de NO-REGRESIÓN del motor legacy 2025 (§8, §11).

Con la BBDD 2025 íntegra y la fórmula de 4 variables, compute_full() debe
reproducir el oficial 2025 en los 19 países con error ≤ 1 punto, en Sub1, Sub2
e Indicador. Si la BBDD no está, el test se marca como omitido (no falla).
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import calc_engine as ce  # noqa: E402

# Oficial 2025 (hoja "Indicador Normalizado" / "Gráfico - Índice" de la BBDD).
OFICIAL_SUB1 = {"AR":0,"BO":38,"BR":53,"CL":55,"CO":69,"CR":38,"CU":0,"DO":32,"EC":32,
                "GT":32,"HN":32,"JM":0,"MX":58,"PA":0,"PE":56,"PY":0,"SV":0,"UY":0,"VE":0,"TT":0}
OFICIAL_SUB2 = {"AR":0,"BO":23,"BR":100,"CL":59,"CO":100,"CR":53,"CU":0,"DO":28,"EC":18,
                "GT":33,"HN":52,"JM":0,"MX":37,"PA":0,"PE":51,"PY":0,"SV":0,"UY":0,"VE":0,"TT":0}
OFICIAL_IND = {"AR":0,"BO":30,"BR":76,"CL":57,"CO":85,"CR":46,"CU":0,"DO":30,"EC":25,
               "GT":32,"HN":42,"JM":0,"MX":47,"PA":0,"PE":53,"PY":0,"SV":0,"UY":0,"VE":0,"TT":0}
TOL = 1


def _bbdd_disponible():
    return os.path.exists(ce.DEFAULT_XLSX)


def test_noregresion_completa():
    if not _bbdd_disponible():
        print("  [OMITIDO] BBDD 2025 no disponible:", ce.DEFAULT_XLSX)
        return
    casos = ce.load_casos()
    assert len(casos) == 28, f"esperaba 28 casos, hay {len(casos)}"
    sub1, sub2, ind, rc = ce.compute_full(casos)
    errores = []
    for p in ce.PAISES:
        if abs(sub1[p]["v"] - OFICIAL_SUB1[p]) > TOL:
            errores.append(f"Sub1 {p}: {sub1[p]['v']} vs {OFICIAL_SUB1[p]}")
        if abs(sub2[p]["v"] - OFICIAL_SUB2[p]) > TOL:
            errores.append(f"Sub2 {p}: {sub2[p]['v']} vs {OFICIAL_SUB2[p]}")
        if abs(ind[p] - OFICIAL_IND[p]) > TOL:
            errores.append(f"Ind {p}: {ind[p]} vs {OFICIAL_IND[p]}")
    assert not errores, "Discrepancias > {}:\n  {}".format(TOL, "\n  ".join(errores))
    print(f"  [OK] 19/19 países, Sub1+Sub2+Indicador dentro de ±{TOL}")


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
