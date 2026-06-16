#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Motor de calculo del indicador HPC (3 variables) - ILIA 2026, paises extra.

REGLA DE ORO: ningun numero de pais vive hardcodeado aqui. El motor lee:
  - data/hpc/sistemas_consolidado.csv  (censo + capacidad por sistema/particion)
  - data/hpc/poblacion.csv             (denominador per capita)
y calcula las 3 variables oficiales (absolutas y per capita) + companeras de IA.

Las DECISIONES ABIERTAS se controlan en CONFIG (no en la logica):
  - scope:           "all_published" (toda ficha publica) | "top500_only"
  - var3_precision:  "fp64" | "fp16"   (precision principal de la var.3 GPU)
  - var1_percapita:  reportar tambien la var.1 normalizada por millon de hab.
  - incluir_no_operativos: contar sistemas no operativos (default: no)

Uso:
  python src/hpc_calc.py                      # usa rutas por defecto
  python src/hpc_calc.py --selftest           # prueba sintetica (sin ficheros)
"""
import csv
import argparse
import os

CONFIG = {
    "scope": "all_published",       # "all_published" | "top500_only"
    "var3_precision": "fp64",       # "fp64" | "fp16"
    "var1_percapita": True,
    "incluir_no_operativos": False,
}

DEF_SYS = os.path.join("data", "hpc", "sistemas_consolidado.csv")
DEF_POP = os.path.join("data", "hpc", "poblacion.csv")


def _f(x):
    """Float tolerante: '', null, 'no publicado' -> None; admite separador de miles."""
    x = ("" if x is None else str(x)).strip().replace(",", "")
    if x == "" or x.lower() in ("null", "na", "n/a", "no publicado", "-", "nd"):
        return None
    try:
        return float(x)
    except ValueError:
        return None


def _b(x):
    return str("" if x is None else x).strip().lower() in ("1", "true", "si", "sí", "yes", "y")


def is_operational(estado):
    e = ("" if estado is None else str(estado)).lower()
    return ("operativ" in e) or ("producci" in e) or ("en servicio" in e)


def load_pop(path):
    pop = {}
    with open(path, newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            iso = (row.get("pais_iso") or "").strip()
            if not iso or iso.startswith("#"):
                continue
            v = _f(row.get("poblacion"))
            if v:
                pop[iso] = v
    return pop


def load_systems(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            if not (row.get("sistema") or "").strip():
                continue
            if (row.get("pais_iso") or "").strip().startswith("#"):
                continue
            rows.append(row)
    return rows


def included(row, cfg):
    if cfg["scope"] == "top500_only" and not _b(row.get("en_top500")):
        return False
    if not cfg["incluir_no_operativos"] and not is_operational(row.get("estado")):
        return False
    return True


def compute(systems, pop, cfg=CONFIG):
    """Devuelve {iso: {metricas}}. No imprime; pura para poder testear."""
    out = {}
    for iso, pobl in pop.items():
        sel = [r for r in systems
               if (r.get("pais_iso") or "").strip() == iso and included(r, cfg)]
        cap = [r for r in sel if _b(r.get("incluir_capacidad"))]
        gpu = [r for r in sel if _b(r.get("incluir_gpu"))]

        sum_rpeak = sum(_f(r.get("rpeak_tf")) or 0 for r in cap)
        sum_rmax = sum(_f(r.get("rmax_tf")) or 0 for r in cap)
        sum_ngpu = sum(_f(r.get("n_gpus")) or 0 for r in gpu)
        sum_gfp64 = sum(_f(r.get("gpu_fp64_tf")) or 0 for r in gpu)
        sum_gfp16 = sum(_f(r.get("gpu_fp16_tf")) or 0 for r in gpu)

        p_mill = pobl / 1_000_000.0
        var3_num = sum_gfp64 if cfg["var3_precision"] == "fp64" else sum_gfp16

        rpeaks = sorted((_f(r.get("rpeak_tf")) or 0 for r in cap), reverse=True)
        top_share = (rpeaks[0] / sum_rpeak) if (rpeaks and sum_rpeak > 0) else None

        out[iso] = {
            "n_sistemas": len(sel),
            "n_con_rpeak": sum(1 for r in cap if _f(r.get("rpeak_tf")) is not None),
            # Variable 1
            "var1_cap_hpc_tf": sum_rpeak,
            "var1_cap_hpc_tf_pmill": (sum_rpeak / p_mill) if cfg["var1_percapita"] else None,
            "rmax_tf": sum_rmax,
            # Variable 2
            "var2_ngpu": sum_ngpu,
            "var2_ngpu_pmill": sum_ngpu / p_mill,
            # Variable 3
            "var3_gpu_tf": var3_num,
            "var3_gpu_tf_pmill": var3_num / p_mill,
            "gpu_fp16_tf": sum_gfp16,
            "gpu_fp16_tf_pmill": sum_gfp16 / p_mill,
            # Calidad
            "top_sistema_share_rpeak": top_share,
        }
    return out


def print_table(res, cfg):
    print("# Indicador HPC - resultados (cota inferior)")
    print("# CONFIG:", cfg)
    cols = [
        ("pais", "{:<5}"),
        ("nSis", "{:>4}"),
        ("V1 Rpeak TF", "{:>12}"),
        ("V1 TF/Mhab", "{:>11}"),
        ("V2 nGPU", "{:>8}"),
        ("V2 GPU/Mhab", "{:>11}"),
        ("V3 GPU TF/Mhab", "{:>14}"),
        ("top%", "{:>6}"),
    ]
    print(" | ".join(h.format(c) for c, h in cols))
    for iso, m in res.items():
        def g(k):
            v = m.get(k)
            return "-" if v is None else (f"{v:,.0f}" if abs(v) >= 100 else f"{v:,.2f}")
        share = m["top_sistema_share_rpeak"]
        share = "-" if share is None else f"{share*100:.0f}%"
        vals = [iso, m["n_sistemas"], g("var1_cap_hpc_tf"), g("var1_cap_hpc_tf_pmill"),
                g("var2_ngpu"), g("var2_ngpu_pmill"), g("var3_gpu_tf_pmill"), share]
        print(" | ".join(h.format(v) for v, (_, h) in zip(vals, cols)))


def selftest():
    pop = {"AA": 2_000_000, "BB": 10_000_000}
    sys_rows = [
        # AA: 1 sistema operativo TOP500 con GPUs
        {"pais_iso": "AA", "sistema": "Alpha", "estado": "Operativo", "en_top500": "1",
         "rpeak_tf": "1000", "rmax_tf": "800", "n_gpus": "100", "gpu_fp64_tf": "900",
         "gpu_fp16_tf": "9000", "incluir_capacidad": "1", "incluir_gpu": "1"},
        # AA: 1 sistema no operativo -> NO debe contar
        {"pais_iso": "AA", "sistema": "Old", "estado": "Retirado", "en_top500": "1",
         "rpeak_tf": "500", "n_gpus": "50", "gpu_fp64_tf": "400", "gpu_fp16_tf": "4000",
         "incluir_capacidad": "1", "incluir_gpu": "1"},
        # BB: sistema operativo NO top500, solo CPU (sin GPU)
        {"pais_iso": "BB", "sistema": "Beta", "estado": "Operativo", "en_top500": "0",
         "rpeak_tf": "200", "rmax_tf": "150", "n_gpus": "0", "gpu_fp64_tf": "0",
         "gpu_fp16_tf": "0", "incluir_capacidad": "1", "incluir_gpu": "1"},
        # BB: cuota compartida estilo LUMI -> incluir_capacidad=0, no cuenta
        {"pais_iso": "BB", "sistema": "Shared", "estado": "Operativo", "en_top500": "1",
         "rpeak_tf": "5000", "n_gpus": "1000", "gpu_fp64_tf": "4000", "gpu_fp16_tf": "40000",
         "incluir_capacidad": "0", "incluir_gpu": "0"},
    ]
    cfg = dict(CONFIG)
    r = compute(sys_rows, pop, cfg)
    # AA: solo "Alpha" cuenta (Old retirado fuera)
    assert r["AA"]["n_sistemas"] == 1, r["AA"]["n_sistemas"]
    assert r["AA"]["var1_cap_hpc_tf"] == 1000
    assert abs(r["AA"]["var1_cap_hpc_tf_pmill"] - 500.0) < 1e-9   # 1000 / 2
    assert r["AA"]["var2_ngpu"] == 100
    assert abs(r["AA"]["var2_ngpu_pmill"] - 50.0) < 1e-9          # 100 / 2
    assert abs(r["AA"]["var3_gpu_tf_pmill"] - 450.0) < 1e-9       # 900 / 2
    assert abs(r["AA"]["top_sistema_share_rpeak"] - 1.0) < 1e-9
    # BB: solo "Beta" en capacidad (Shared excluido por incluir_capacidad=0)
    assert r["BB"]["n_sistemas"] == 2          # Beta + Shared operativos
    assert r["BB"]["var1_cap_hpc_tf"] == 200   # Shared no suma capacidad
    assert r["BB"]["var2_ngpu"] == 0           # Shared no suma GPUs
    # scope top500_only: BB-Beta (no top500) sale; queda solo Shared (excluido cap) -> 0
    cfg2 = dict(CONFIG); cfg2["scope"] = "top500_only"
    r2 = compute(sys_rows, pop, cfg2)
    assert r2["BB"]["var1_cap_hpc_tf"] == 0
    assert r2["AA"]["var1_cap_hpc_tf"] == 1000
    # var3 en fp16
    cfg3 = dict(CONFIG); cfg3["var3_precision"] = "fp16"
    r3 = compute(sys_rows, pop, cfg3)
    assert abs(r3["AA"]["var3_gpu_tf_pmill"] - 4500.0) < 1e-9     # 9000 / 2
    print("selftest OK")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--systems", default=DEF_SYS)
    ap.add_argument("--pop", default=DEF_POP)
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--scope", choices=["all_published", "top500_only"])
    ap.add_argument("--var3", choices=["fp64", "fp16"])
    args = ap.parse_args()
    if args.selftest:
        selftest()
        return
    cfg = dict(CONFIG)
    if args.scope:
        cfg["scope"] = args.scope
    if args.var3:
        cfg["var3_precision"] = args.var3
    if not os.path.exists(args.systems):
        print(f"[aviso] No existe {args.systems}. Ejecuta --selftest o consolida los datos.")
        return
    systems = load_systems(args.systems)
    pop = load_pop(args.pop)
    res = compute(systems, pop, cfg)
    print_table(res, cfg)


if __name__ == "__main__":
    main()
