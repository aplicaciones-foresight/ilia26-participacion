# Fase 2 — Estado (extracción doble pasada)

**Fecha:** 2026-06-05 · **Pipeline ILIA 2026 — Participación Ciudadana**

## 1. Gate 1 → Fase 2

El Gate 1 aprobó los **18 candidatos nuevos/dudosos** (ver `gate1_decision.md`).
Se construyó la **cola de Fase 2** para los 18 con `extract.py --prepare`:
cada caso tiene `data/fetched/<id>/` con `_manifest.json` y los payloads de doble
pasada (`_payload_A.txt`, `_payload_B.txt`) listos para Claude.

## 2. Restricción operativa de fetch (importante)

En este entorno, el **fetch en vivo devuelve HTTP 403** en la mayoría de los
sitios `.gob.*`/`.gov.*`, prensa y arXiv —tanto con el fetcher determinístico
(`urllib` de `extract.py`) como con el fetcher robusto—. **Solo GitHub respondió.**

Consecuencia: la extracción en vivo de las fuentes institucionales **requiere un
fetcher autenticado/navegador o que el operador aporte el texto** (pegándolo en
`data/fetched/<id>/fuente_N.txt`). El pipeline (payloads + esquema + verbatim +
conciliación) está **listo**; el cuello de botella es el acceso a las fuentes.

## 3. Demostración end-to-end (caso real con fuente fetchable)

Caso **BR — Brasil Participativo** (`BR-brasil-participativo-clustering-semantic`),
con fuente GitHub fetcheada (BP-Classificador-de-Propostas, 6.853 chars):

1. **Doble pasada independiente** (dos instancias Claude, prompts v1.1-A y v1.1-B).
2. **Validación de esquema**: OK en ambas.
3. **Verificación verbatim** contra el texto fetcheado: 6/7 citas válidas; la cita
   no exacta se **anuló automáticamente** (rol_IA en A, usa_IA_en_proceso en B).
4. **Conciliación (Fase 3)** → **confianza BAJA**, por:
   - **conflicto en campo crítico `nivel_consolidacion`** (A=2 «uso real» vs B=1
     «prototipo») — la doble pasada detectó fragilidad de codificación real;
   - **fuente única** (arXiv 2509.21292 / 2511.01545 dieron 403; solo quedó GitHub);
   - evidencia no completamente verificada.

**Lectura:** ambas pasadas coinciden en que el caso **es elegible** (IA sobre el
contenido de las propuestas ciudadanas: `rol_IA=contenido`, `tipo_proceso=
Gobernanza Colaborativa`, `etapas=Análisis`, convocante `gobierno nacional`). La
duda real —¿nivel 1 prototipo o nivel 2 uso real?— queda **correctamente
escalada al Gate 2** (humano), que la resolverá con la fuente institucional
(papers arXiv + la propia plataforma Brasil Participativo).

Artefactos: `data/fichas/BR-brasil-participativo-clustering-semantic_A.json`,
`_B.json`, `_conciliada.json`, `_diff.md`.

## 4. Próximos pasos

1. **Fetch de fuentes** con acceso autenticado/operador para los 18 (prioridad:
   las 10 nuevas sólidas; secundarias independientes para subir confianza).
2. Correr la **doble pasada** en los 18 (los payloads ya están armados).
3. **Gate 2** (humano): resolver conflictos críticos (p. ej. `nivel_consolidacion`
   de Brasil Participativo), revisar la muestra de ALTA, registrar en `gate2_log.csv`.
4. Recodificar a esquema 2026 (`tipo_convocante`, `nivel_consolidacion`) en cada
   ficha conciliada para alimentar el motor (Fase 4).

> Nota: `model_version` en las fichas de demostración quedó como
> `(definir-en-corrida)`; el operador fija la versión real del modelo por corrida.
