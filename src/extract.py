#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
extract.py — Fase 2 (Extracción, doble pasada) del pipeline ILIA 2026.

La EXTRACCIÓN en sí corre en Claude (100 % Claude, §2): dos pasadas con prompts
independientes (v1.1-A / v1.1-B). Este script orquesta lo determinístico
alrededor de esa llamada:

  --prepare <candidato_id>   fetch de URLs (primario + secundarios) -> guarda el
                             texto en data/fetched/<caso_id>/ y arma los dos
                             payloads (prompt + texto) listos para Claude.
  --validate <ficha.json>    valida la ficha contra prompts/schema_ficha_v1.1.json
                             y, si se indica --texto, corre verify_verbatim.

Flujo por candidato aprobado en Gate 1:
  1) python src/extract.py --prepare BR-portal-e-cidadania
  2) (Claude) responder _payload_A.txt y _payload_B.txt -> guardar
     data/fichas/<caso_id>_A.json y _B.json
  3) python src/extract.py --validate data/fichas/<caso_id>_A.json \
         --texto data/fetched/<caso_id>
  4) python src/reconcile.py <caso_id>
"""
from __future__ import annotations
import argparse
import csv
import datetime
import json
import os
import re
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verify_verbatim as vv  # noqa: E402

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
SCHEMA_PATH = os.path.join(ROOT, "prompts", "schema_ficha_v1.1.json")
PROMPT_A = os.path.join(ROOT, "prompts", "prompt_extraccion_v1.1_A.txt")
PROMPT_B = os.path.join(ROOT, "prompts", "prompt_extraccion_v1.1_B.txt")


def cargar_config():
    import yaml
    with open(os.path.join(ROOT, "config.yaml"), encoding="utf-8") as fh:
        return yaml.safe_load(fh)


# --------------------------------------------------------------------------- #
# Fetch
# --------------------------------------------------------------------------- #
def html_a_texto(html: str) -> str:
    html = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", html)
    html = re.sub(r"(?s)<[^>]+>", " ", html)
    html = (html.replace("&nbsp;", " ").replace("&amp;", "&")
                .replace("&lt;", "<").replace("&gt;", ">").replace("&#39;", "'")
                .replace("&quot;", '"'))
    html = re.sub(r"[ \t]+", " ", html)
    html = re.sub(r"\n\s*\n\s*\n+", "\n\n", html)
    return html.strip()


def fetch_url(url: str, timeout: int = 25):
    """Devuelve (texto, error|None). Best-effort; no falla la corrida."""
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (ILIA2026-pipeline; +investigación)"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read()
        try:
            html = raw.decode("utf-8")
        except UnicodeDecodeError:
            html = raw.decode("latin-1", errors="replace")
        return html_a_texto(html), None
    except Exception as exc:  # noqa: BLE001
        return "", f"{type(exc).__name__}: {exc}"


def _candidato(candidato_id, cfg):
    ruta = os.path.join(ROOT, cfg["rutas"]["candidatos"])
    with open(ruta, newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            if r["candidato_id"] == candidato_id:
                return r
    return None


def prepare(candidato_id, cfg):
    cand = _candidato(candidato_id, cfg)
    if not cand:
        print(f"[error] candidato_id no encontrado: {candidato_id}", file=sys.stderr)
        return 1
    caso_dir = os.path.join(ROOT, cfg["rutas"]["fetched_dir"], candidato_id)
    os.makedirs(caso_dir, exist_ok=True)
    hoy = datetime.date.today().isoformat()

    urls = [u.strip() for u in (cand.get("urls") or "").split("|") if u.strip()]
    textos = []
    manifest = []
    for i, url in enumerate(urls, 1):
        texto, err = fetch_url(url)
        estado = "ok" if not err else f"ERROR ({err})"
        manifest.append({"n": i, "url": url, "estado": estado, "chars": len(texto)})
        cab = f"===== FUENTE {i} =====\nURL: {url}\nFETCH: {hoy}\nESTADO: {estado}\n\n"
        with open(os.path.join(caso_dir, f"fuente_{i}.txt"), "w", encoding="utf-8") as fh:
            fh.write(cab + texto)
        if texto:
            textos.append(cab + texto)

    with open(os.path.join(caso_dir, "_manifest.json"), "w", encoding="utf-8") as fh:
        json.dump({"candidato_id": candidato_id, "pais": cand.get("pais"),
                   "nombre": cand.get("nombre_tentativo"), "fecha": hoy,
                   "fuentes": manifest}, fh, ensure_ascii=False, indent=2)

    texto_full = "\n\n".join(textos) if textos else "(SIN TEXTO FETCHEADO — revisar URLs)"
    encabezado = (f"caso_id: {candidato_id}\npais_tentativo: {cand.get('pais')}\n"
                  f"nombre_tentativo: {cand.get('nombre_tentativo')}\n"
                  f"fecha_extraccion: {hoy}\n")
    for etiqueta, prompt_path in (("A", PROMPT_A), ("B", PROMPT_B)):
        with open(prompt_path, encoding="utf-8") as fh:
            prompt = fh.read()
        payload = (prompt + "\n\n" + "="*78 +
                   f"\nDATOS DEL CASO (pasada {etiqueta})\n" + "="*78 + "\n" +
                   encabezado + "\n----- TEXTO FETCHEADO -----\n\n" + texto_full + "\n")
        with open(os.path.join(caso_dir, f"_payload_{etiqueta}.txt"), "w", encoding="utf-8") as fh:
            fh.write(payload)

    ok = sum(1 for m in manifest if m["estado"] == "ok")
    print(f"[ok] {candidato_id}: {ok}/{len(urls)} fuentes con texto -> {caso_dir}")
    print(f"     payloads: _payload_A.txt, _payload_B.txt (listos para Claude)")
    if ok == 0:
        print("[aviso] ninguna fuente devolvió texto (¿red restringida / paywall?).",
              file=sys.stderr)
    return 0


# --------------------------------------------------------------------------- #
# Validación de ficha contra el schema (mini-validador, sin dependencias)
# --------------------------------------------------------------------------- #
def _check(node, schema, ruta, errs):
    if "enum" in schema:
        if node not in schema["enum"]:
            errs.append(f"{ruta}: valor {node!r} no está en enum {schema['enum']}")
        return
    tipos = schema.get("type")
    if tipos:
        tipos = tipos if isinstance(tipos, list) else [tipos]
        py = {"string": str, "integer": int, "number": (int, float),
              "array": list, "object": dict, "null": type(None)}
        oks = tuple(py[t] for t in tipos if t in py)
        # bool no es integer válido aquí
        if isinstance(node, bool) or not isinstance(node, oks):
            errs.append(f"{ruta}: tipo {type(node).__name__} no es {tipos}")
            return
    if node is None:
        return
    if isinstance(node, str) and "pattern" in schema:
        if not re.match(schema["pattern"], node):
            errs.append(f"{ruta}: {node!r} no cumple patrón {schema['pattern']}")
    if isinstance(node, (int, float)) and not isinstance(node, bool):
        if "minimum" in schema and node < schema["minimum"]:
            errs.append(f"{ruta}: {node} < min {schema['minimum']}")
        if "maximum" in schema and node > schema["maximum"]:
            errs.append(f"{ruta}: {node} > max {schema['maximum']}")
    if isinstance(node, list) and "items" in schema:
        for i, it in enumerate(node):
            _check(it, schema["items"], f"{ruta}[{i}]", errs)
    if isinstance(node, dict) and schema.get("type") == "object":
        for req in schema.get("required", []):
            if req not in node:
                errs.append(f"{ruta}: falta clave requerida {req!r}")
        props = schema.get("properties", {})
        ap = schema.get("additionalProperties")
        for k, v in node.items():
            if k in props:
                _check(v, props[k], f"{ruta}.{k}", errs)
            elif isinstance(ap, dict):
                _check(v, ap, f"{ruta}.{k}", errs)


def validar_ficha(ficha):
    with open(SCHEMA_PATH, encoding="utf-8") as fh:
        schema = json.load(fh)
    errs = []
    _check(ficha, schema, "ficha", errs)
    return errs


def validate_file(ficha_path, texto_dir, cfg, write=False):
    with open(ficha_path, encoding="utf-8") as fh:
        ficha = json.load(fh)
    errs = validar_ficha(ficha)
    print(f"== Validación de esquema: {os.path.basename(ficha_path)} ==")
    if errs:
        for e in errs:
            print("  ✗", e)
    else:
        print("  ✓ esquema OK")

    if texto_dir:
        texto = vv._cargar_texto(texto_dir)
        corregida, rep = vv.verificar_ficha(ficha, texto, cfg)
        print(f"== Verbatim: {rep['ok']} ok / {rep['fallidas']} fallidas / "
              f"{rep['cortas']} cortas ==")
        for d in rep["detalle"]:
            if d["estado"] == "fallida":
                print(f"  ✗ {d['clave']} -> anulado ({d.get('cita','')[:60]}...)")
        if write and not rep["aprobada"]:
            with open(ficha_path, "w", encoding="utf-8") as fh:
                json.dump(corregida, fh, ensure_ascii=False, indent=2)
            print("  [ok] ficha reescrita con campos no verificables anulados")
        return 0 if (not errs and rep["aprobada"]) else 1
    return 0 if not errs else 1


def main(argv=None):
    cfg = cargar_config()
    ap = argparse.ArgumentParser(description="Fase 2 — orquestación de extracción.")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--prepare", metavar="CANDIDATO_ID")
    g.add_argument("--validate", metavar="FICHA_JSON")
    ap.add_argument("--texto", default=None, help="dir/archivo con el texto fetcheado")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args(argv)

    if args.prepare:
        return prepare(args.prepare, cfg)
    return validate_file(args.validate, args.texto, cfg, write=args.write)


if __name__ == "__main__":
    sys.exit(main())
