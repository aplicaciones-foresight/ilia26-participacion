#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_verbatim.py — Fase 2 del pipeline ILIA 2026.

Verifica que toda cita en el bloque `evidencia_verbatim` de una ficha sea una
SUBCADENA EXACTA del texto fetcheado, normalizando ÚNICAMENTE espacios en blanco
(§3 Regla de oro, §7 Fase 2).

Regla operativa: cita no verificable  ->  el campo crítico asociado se pone a
`null` y se agrega una alerta automática. Mejor null + alerta que un valor que
el texto no respalda.

Uso CLI:
    python src/verify_verbatim.py --ficha data/fichas/BR-x_A.json \
        --texto data/fetched/BR-x/ --config config.yaml [--write]

API:
    normalizar(s) -> str
    es_subcadena(cita, texto, *, case_sensitive=False) -> bool
    verificar_ficha(ficha, texto, config) -> (ficha_corregida, reporte)
"""
from __future__ import annotations
import argparse
import json
import os
import re
import sys

# Mapa: clave en evidencia_verbatim  ->  campo(s) de la ficha a anular si falla.
# Las claves replican los campos críticos (§5.7 / config.campos_criticos).
EVIDENCIA_A_CAMPO = {
    "pais": "pais",
    "tipo_proceso": "tipo_proceso",
    "etapas_uso_IA": "etapas_uso_IA",
    "estado_actividad": "estado_actividad",
    "nivel_consolidacion": "nivel_consolidacion",
    "tipo_convocante": "tipo_convocante",
    "usa_IA_en_proceso": "usa_IA_en_proceso",
    "rol_IA": "rol_IA",
}

_WS = re.compile(r"\s+", re.UNICODE)


def normalizar(s: str) -> str:
    """Normaliza SOLO espacios en blanco: NBSP->espacio, runs de espacios->uno,
    y strip. No altera acentos, mayúsculas ni puntuación."""
    if s is None:
        return ""
    s = str(s).replace(" ", " ")  # espacio duro -> espacio normal
    return _WS.sub(" ", s).strip()


def es_subcadena(cita: str, texto: str, *, case_sensitive: bool = False) -> bool:
    """True si `cita` (normalizada) es subcadena de `texto` (normalizado)."""
    c = normalizar(cita)
    t = normalizar(texto)
    if c == "":
        return False
    if not case_sensitive:
        c = c.casefold()
        t = t.casefold()
    return c in t


def _cargar_texto(ruta: str) -> str:
    """Carga texto desde un archivo o concatena todos los .txt/.md de un dir
    (típicamente data/fetched/{caso_id}/)."""
    if os.path.isdir(ruta):
        partes = []
        for nombre in sorted(os.listdir(ruta)):
            if nombre.lower().endswith((".txt", ".md", ".html")):
                with open(os.path.join(ruta, nombre), encoding="utf-8") as fh:
                    partes.append(fh.read())
        return "\n\n".join(partes)
    with open(ruta, encoding="utf-8") as fh:
        return fh.read()


def verificar_ficha(ficha: dict, texto: str, config: dict | None = None):
    """Verifica el bloque evidencia_verbatim de `ficha` contra `texto`.

    Devuelve (ficha_corregida, reporte). La ficha de entrada NO se muta.
    Por cada cita que NO sea subcadena exacta, anula el campo crítico asociado y
    agrega una alerta. Citas más cortas que `verbatim.min_chars` generan alerta
    (warning) sin anular.
    """
    cfg = (config or {}).get("verbatim", {}) if config else {}
    case_sensitive = bool(cfg.get("case_sensitive", False))
    min_chars = int(cfg.get("min_chars", 8))

    ficha = json.loads(json.dumps(ficha))  # copia profunda barata
    ficha.setdefault("alertas", [])
    evid = ficha.get("evidencia_verbatim", {}) or {}

    reporte = {
        "caso_id": ficha.get("caso_id"),
        "pasada": ficha.get("pasada"),
        "total": 0, "ok": 0, "fallidas": 0, "cortas": 0,
        "detalle": [],
    }

    for clave, campo in EVIDENCIA_A_CAMPO.items():
        cita = evid.get(clave)
        # Sin cita pero con valor en campo crítico no nulo -> alerta.
        if cita is None or normalizar(cita) == "":
            if ficha.get(campo) not in (None, [], ""):
                ficha["alertas"].append(
                    f"verbatim_faltante:{clave} (campo crítico sin cita)")
                reporte["detalle"].append({"clave": clave, "estado": "sin_cita"})
            continue

        reporte["total"] += 1
        ok = es_subcadena(cita, texto, case_sensitive=case_sensitive)
        if ok:
            reporte["ok"] += 1
            if len(normalizar(cita)) < min_chars:
                reporte["cortas"] += 1
                ficha["alertas"].append(
                    f"verbatim_cita_corta:{clave} (<{min_chars} chars)")
                reporte["detalle"].append({"clave": clave, "estado": "ok_corta"})
            else:
                reporte["detalle"].append({"clave": clave, "estado": "ok"})
        else:
            reporte["fallidas"] += 1
            ficha[campo] = None
            ficha["alertas"].append(
                f"verbatim_no_verificable:{clave} -> {campo}=null")
            reporte["detalle"].append({
                "clave": clave, "estado": "fallida",
                "cita": normalizar(cita)[:120],
            })

    reporte["aprobada"] = reporte["fallidas"] == 0
    return ficha, reporte


def _cargar_config(ruta: str | None) -> dict:
    if not ruta:
        return {}
    try:
        import yaml
        with open(ruta, encoding="utf-8") as fh:
            return yaml.safe_load(fh) or {}
    except Exception as exc:  # pragma: no cover - solo CLI
        print(f"[aviso] no se pudo leer config {ruta}: {exc}", file=sys.stderr)
        return {}


def main(argv=None):
    ap = argparse.ArgumentParser(description="Verifica citas verbatim de una ficha.")
    ap.add_argument("--ficha", required=True, help="JSON de la ficha")
    ap.add_argument("--texto", required=True, help="archivo o dir con el texto fetcheado")
    ap.add_argument("--config", default=None, help="config.yaml (opcional)")
    ap.add_argument("--write", action="store_true",
                    help="reescribe la ficha con los campos no verificables anulados")
    args = ap.parse_args(argv)

    with open(args.ficha, encoding="utf-8") as fh:
        ficha = json.load(fh)
    texto = _cargar_texto(args.texto)
    config = _cargar_config(args.config)

    corregida, reporte = verificar_ficha(ficha, texto, config)
    print(json.dumps(reporte, ensure_ascii=False, indent=2))

    if args.write and not reporte["aprobada"]:
        with open(args.ficha, "w", encoding="utf-8") as fh:
            json.dump(corregida, fh, ensure_ascii=False, indent=2)
        print(f"[ok] ficha reescrita con {reporte['fallidas']} campo(s) anulado(s).",
              file=sys.stderr)

    return 0 if reporte["aprobada"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
