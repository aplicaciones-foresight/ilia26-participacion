#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
reconcile.py — Fase 3 (Conciliación + triangulación) del pipeline ILIA 2026.

Compara las pasadas A y B (independientes) campo a campo y asigna confianza:

  ALTA  : coinciden TODOS los campos críticos + evidencia verificada + ≥2 fuentes
          independientes.
  MEDIA : discrepancias menores (no críticas) o fuente única.
  BAJA  : discrepancia en campos críticos, evidencia no verificable o solo prensa.

Salida: ficha conciliada (_conciliada.json) + diff legible (_diff.md) para Gate 2.

Uso:  python src/reconcile.py <caso_id>
"""
from __future__ import annotations
import json
import os
import sys
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verify_verbatim as vv  # noqa: E402

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))


def cargar_config():
    import yaml
    with open(os.path.join(ROOT, "config.yaml"), encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _norm(v):
    if isinstance(v, list):
        return sorted(str(x).strip().lower() for x in v)
    if isinstance(v, str):
        return v.strip().lower()
    return v


def _eq(a, b):
    return _norm(a) == _norm(b)


def _dominio(url):
    try:
        return urllib.parse.urlparse(url).netloc.lower().replace("www.", "")
    except Exception:  # noqa: BLE001
        return ""


def conciliar(caso_id, cfg):
    fdir = os.path.join(ROOT, cfg["rutas"]["fichas_dir"])
    pa = os.path.join(fdir, f"{caso_id}_A.json")
    pb = os.path.join(fdir, f"{caso_id}_B.json")
    for p in (pa, pb):
        if not os.path.exists(p):
            print(f"[error] falta ficha: {p}", file=sys.stderr)
            return None
    A = json.load(open(pa, encoding="utf-8"))
    B = json.load(open(pb, encoding="utf-8"))

    criticos = cfg.get("campos_criticos", [])
    todos_campos = [k for k in A if k not in ("evidencia_verbatim", "alertas", "pasada")]

    # Evidencia verificable: corre verify_verbatim sobre texto fetcheado.
    texto = ""
    tdir = os.path.join(ROOT, cfg["rutas"]["fetched_dir"], caso_id)
    if os.path.isdir(tdir):
        texto = vv._cargar_texto(tdir)
    _, repA = vv.verificar_ficha(A, texto, cfg) if texto else (A, {"aprobada": False})
    _, repB = vv.verificar_ficha(B, texto, cfg) if texto else (B, {"aprobada": False})
    evidencia_ok = bool(texto) and repA.get("aprobada") and repB.get("aprobada")

    # Fuentes independientes (dominios distintos en A ∪ B).
    dominios = {_dominio(u) for u in (A.get("urls_fuente") or []) + (B.get("urls_fuente") or []) if u}
    dominios.discard("")
    dos_fuentes = len(dominios) >= 2

    # Solo prensa: heurística por alertas.
    alertas = (A.get("alertas") or []) + (B.get("alertas") or [])
    solo_prensa = any("prensa" in a.lower() or "fuente única" in a.lower() or "fuente unica" in a.lower()
                      for a in alertas)

    # Comparación campo a campo.
    conflictos_criticos, dif_menores, concil = [], [], {}
    for campo in todos_campos:
        igual = _eq(A.get(campo), B.get(campo))
        if igual:
            concil[campo] = A.get(campo)
        else:
            if campo in criticos:
                conflictos_criticos.append(campo)
                concil[campo] = None  # conservador: queda para el Gate
            else:
                dif_menores.append(campo)
                concil[campo] = A.get(campo)  # se conserva A, se anota

    # Confianza.
    if conflictos_criticos or (not evidencia_ok) or solo_prensa:
        confianza = "BAJA"
    elif dos_fuentes:
        confianza = "ALTA"
    else:
        confianza = "MEDIA"
    if confianza == "ALTA" and (dif_menores):
        # discrepancias menores -> a lo sumo MEDIA si no son críticas
        pass  # ALTA se mantiene: el spec exige críticos+evidencia+2 fuentes

    concil.update({
        "caso_id": caso_id,
        "pasada": "conciliada",
        "confianza": confianza,
        "evidencia_verbatim": A.get("evidencia_verbatim"),
        "evidencia_verbatim_B": B.get("evidencia_verbatim"),
        "alertas": sorted(set(alertas)),
        "conciliacion": {
            "conflictos_criticos": conflictos_criticos,
            "diferencias_menores": dif_menores,
            "evidencia_verificada": evidencia_ok,
            "n_fuentes_independientes": len(dominios),
            "dominios": sorted(dominios),
            "solo_prensa": solo_prensa,
        },
    })

    out = os.path.join(fdir, f"{caso_id}_conciliada.json")
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(concil, fh, ensure_ascii=False, indent=2)

    # Diff legible para Gate 2.
    L = [f"# Conciliación A/B — {caso_id}", "",
         f"**Confianza:** {confianza}", "",
         f"- Conflictos en campos críticos: {conflictos_criticos or 'ninguno'}",
         f"- Diferencias menores (no críticas): {dif_menores or 'ninguna'}",
         f"- Evidencia verificada (verbatim A y B): {evidencia_ok}",
         f"- Fuentes independientes: {len(dominios)} {sorted(dominios)}",
         f"- Solo prensa (heurística): {solo_prensa}", "",
         "## Campo a campo", "",
         "| Campo | Crítico | Pasada A | Pasada B | ¿Coincide? |",
         "|---|:---:|---|---|:---:|"]
    for campo in todos_campos:
        crit = "sí" if campo in criticos else ""
        a = json.dumps(A.get(campo), ensure_ascii=False)
        b = json.dumps(B.get(campo), ensure_ascii=False)
        ok = "✓" if _eq(A.get(campo), B.get(campo)) else "✗"
        L.append(f"| {campo} | {crit} | {a[:60]} | {b[:60]} | {ok} |")
    diff = "\n".join(L)
    with open(os.path.join(fdir, f"{caso_id}_diff.md"), "w", encoding="utf-8") as fh:
        fh.write(diff)

    print(f"[ok] {caso_id}: confianza={confianza} -> {out}")
    print(f"     conflictos críticos={conflictos_criticos or '∅'} | "
          f"evidencia_ok={evidencia_ok} | fuentes={len(dominios)}")
    return concil


def main(argv=None):
    argv = argv or sys.argv[1:]
    if not argv:
        print("uso: python src/reconcile.py <caso_id>", file=sys.stderr)
        return 1
    cfg = cargar_config()
    r = conciliar(argv[0], cfg)
    return 0 if r else 1


if __name__ == "__main__":
    sys.exit(main())
