#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
reproduce.py — Fase 5 (Publicación reproducible) del pipeline ILIA 2026.

Script ÚNICO que regenera todos los números publicados desde la configuración y
los datos versionados, y verifica reproducibilidad (recálculo desde cero =
mismos números). Empaqueta también los hashes de los insumos (config, prompts,
recodificación, BBDD) para trazabilidad (§5 Fase 5).

Pasos:
  1. Verifica prerrequisitos (BBDD).
  2. Corre el test de no-regresión legacy (control 2025).
  3. Calcula el indicador 2026 para el escenario activo (DRAFT si la
     recodificación es pre-Gate).
  4. Genera gate3_report.md (comparativo por país + descomposición + alertas de
     cambio > umbral) y reproduce_manifest.json (números + hashes).
  5. Recalcula y comprueba que los números son idénticos (reproducibilidad).

Uso:  python src/reproduce.py
"""
from __future__ import annotations
import hashlib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import calc_engine as ce  # noqa: E402

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

OFICIAL_IND = {"AR":0,"BO":30,"BR":76,"CL":57,"CO":85,"CR":46,"CU":0,"DO":30,"EC":25,
               "GT":32,"HN":42,"JM":0,"MX":47,"PA":0,"PE":53,"PY":0,"SV":0,"TT":0,"UY":0,"VE":0}


def cargar_config():
    import yaml
    with open(os.path.join(ROOT, "config.yaml"), encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _sha256(path):
    if not os.path.exists(path):
        return None
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()[:16]


def _indicadores_2026(cfg):
    casos = ce.load_casos(os.path.join(ROOT, cfg["rutas"]["baseline_xlsx"]))
    recod = ce.load_recodificacion_csv(os.path.join(ROOT, cfg["rutas"]["recodificacion_2025"]))
    sub1, sub2, ind, _, info = ce.run_2026(casos, cfg, recod)
    return sub1, sub2, ind, info, len(recod)


def main(argv=None):
    cfg = cargar_config()
    xlsx = os.path.join(ROOT, cfg["rutas"]["baseline_xlsx"])
    if not os.path.exists(xlsx):
        print("BLOQUEADO: BBDD no disponible. Fase 5 requiere la BBDD (§3).")
        return 2

    # 2. Control legacy 2025.
    casos = ce.load_casos(xlsx)
    _, sub2_25, ind_25, _ = ce.compute_full(casos)
    max_delta_control = max(abs(ind_25[p] - OFICIAL_IND[p]) for p in ce.PAISES)
    control_ok = max_delta_control <= 1

    # 3. Indicador 2026 (escenario activo).
    sub1, sub2, ind, info, n_recod = _indicadores_2026(cfg)

    # 5. Reproducibilidad: recalcular y comparar.
    _, _, ind_b, _, _ = _indicadores_2026(cfg)
    reproducible = (ind == ind_b)

    umbral = cfg.get("gate3", {}).get("umbral_cambio", 15)
    scenario = info.get("scenario")
    es_draft = n_recod > 0  # la recodificación actual es BORRADOR pre-Gate

    # Hashes de insumos.
    hashes = {
        "config.yaml": _sha256(os.path.join(ROOT, "config.yaml")),
        "prompt_v1.1_A": _sha256(os.path.join(ROOT, "prompts", "prompt_extraccion_v1.1_A.txt")),
        "prompt_v1.1_B": _sha256(os.path.join(ROOT, "prompts", "prompt_extraccion_v1.1_B.txt")),
        "schema_v1.1": _sha256(os.path.join(ROOT, "prompts", "schema_ficha_v1.1.json")),
        "recodificacion_2025": _sha256(os.path.join(ROOT, cfg["rutas"]["recodificacion_2025"])),
        "BBDD_2025": _sha256(xlsx),
    }

    # gate3_report.md
    L = [f"# Gate 3 — Validación final (Fase 5)", "",
         f"**Escenario activo:** {scenario}  ·  **Redondeo:** "
         f"{cfg.get('redondeo',{}).get('modo')}  ·  **count_min_level:** "
         f"{cfg.get('cantidad',{}).get('count_min_level')}", ""]
    if es_draft:
        L += ["> ⚠️ **DRAFT**: los números 2026 dependen de la recodificación "
              "pre-Gate (`recodificacion_2025.csv`). No publicar sin validación humana.", ""]
    L += ["## Reproducibilidad", "",
          f"- Control legacy 2025 vs oficial: desviación máx **{max_delta_control}** "
          f"({'OK ≤1' if control_ok else 'REVISAR'}).",
          f"- Recálculo 2026 idéntico en dos corridas: **{'sí' if reproducible else 'NO'}**.",
          f"- `model_version` (corrida): `{cfg.get('corrida',{}).get('model_version')}`", "",
          "## Comparativo por país (Indicador) y alertas de cambio", "",
          f"Umbral de alerta: |Δ| > {umbral} puntos.", "",
          "| País | 2025 oficial | 2026 | Δ | Alerta |",
          "|---|:---:|:---:|:---:|:---:|"]
    for p in ce.PAISES:
        d = ind[p] - OFICIAL_IND[p]
        alerta = "⚠️" if abs(d) > umbral else ""
        L.append(f"| {p} | {OFICIAL_IND[p]} | {ind[p]} | {d:+d} | {alerta} |")
    L += ["", "## Descomposición Sub1 2026 por variable", "",
          "| País | Tipos | Etapas | Continuidad | Convocante | Cantidad | Sub1 | Sub2 |",
          "|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|"]
    for p in ce.PAISES:
        s = sub1[p]
        if s["n"] == 0:
            continue
        L.append(f"| {p} | {s['tipos']:.0f} | {s['etapas']:.0f} | {s['cont']:.0f} | "
                 f"{s['conv']:.0f} | {s['cant']:.0f} | {s['v']:.0f} | {sub2[p]['v']:.0f} |")
    L += ["", "## Hashes de insumos (trazabilidad)", "",
          "| Insumo | sha256[:16] |", "|---|---|"]
    for k, v in hashes.items():
        L.append(f"| {k} | `{v}` |")
    L += ["", "## Fichas con evidencia (verbatim)", ""]
    fdir = os.path.join(ROOT, cfg["rutas"]["fichas_dir"])
    conciliadas = [f for f in os.listdir(fdir) if f.endswith("_conciliada.json")] if os.path.isdir(fdir) else []
    L.append(f"- Fichas conciliadas presentes: {len(conciliadas)} "
             f"(en esta corrida: {'ninguna; Fases 2-3 aún no ejecutadas' if not conciliadas else ', '.join(conciliadas)})")
    reporte = "\n".join(L)

    out_md = os.path.join(ROOT, cfg["rutas"]["gates_dir"], "gate3_report.md")
    os.makedirs(os.path.dirname(out_md), exist_ok=True)
    with open(out_md, "w", encoding="utf-8") as fh:
        fh.write(reporte)

    manifest = {
        "escenario": scenario, "es_draft": es_draft,
        "control_legacy_ok": control_ok, "max_delta_control": max_delta_control,
        "reproducible": reproducible, "n_recodificacion": n_recod,
        "config": {"count_min_level": cfg.get("cantidad", {}).get("count_min_level"),
                   "redondeo": cfg.get("redondeo", {}).get("modo")},
        "indicador_2026": ind, "sub1_v": {p: round(sub1[p]["v"], 2) for p in ce.PAISES},
        "sub2_v": {p: round(sub2[p]["v"], 2) for p in ce.PAISES},
        "hashes": hashes,
    }
    out_json = os.path.join(ROOT, cfg["rutas"]["gates_dir"], "reproduce_manifest.json")
    with open(out_json, "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, ensure_ascii=False, indent=2)

    print(f"[control] legacy 2025 vs oficial: máx Δ = {max_delta_control} "
          f"({'OK' if control_ok else 'REVISAR'})")
    print(f"[2026] escenario {scenario} · reproducible={reproducible} · draft={es_draft}")
    print(f"[ok] {out_md}")
    print(f"[ok] {out_json}")
    return 0 if (control_ok and reproducible) else 1


if __name__ == "__main__":
    sys.exit(main())
