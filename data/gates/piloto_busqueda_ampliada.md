# Piloto de búsqueda ampliada — AR · BR · CL

**Fecha:** 2026-06-05 · **Pipeline ILIA 2026 — Participación Ciudadana**

Piloto para evaluar **cuánto más rinde una búsqueda ampliada** (más términos, más
canales, operadores y *snowballing*) antes de decidir si se escala a los 20 países.

## 1. Método ampliado probado

- **Términos** cruzados participación × técnica, ES/PT/EN (ver `config.yaml →
  descubrimiento.terminos`).
- **Canales nuevos** (ahora en `config.yaml`): **A.12** compras/licitaciones
  públicas, **A.13** premios e innovación (Gobernarte-BID, OGP Awards, CLAD),
  **A.14** proveedores/herramientas (vendor-first).
- **Operadores**: `site:.gob/.gov`, `filetype:pdf`, rangos de fecha, frases exactas.
- **Snowballing**: desde cada caso, seguir desarrollador y financiador.
- **Ejecución**: 6 investigadores (2 por país: *gobierno+subnacional+licitaciones*
  y *proveedores+académico+sociedad civil*).

## 2. Incidente operativo

Los 6 agentes **alcanzaron el límite de sesión** (87-108 búsquedas c/u) y
terminaron **sin emitir la síntesis** final. Se **recuperaron sus pistas** desde
las transcripciones (notas intermedias) y se **verificaron a mano** los leads más
prometedores. Mitigación futura: lotes de 2-3 agentes y síntesis parcial temprana.

## 3. Hallazgos verificados

| País | Lead surgido (método ampliado) | Veredicto |
|---|---|---|
| AR | "ParticipIA" (vía JAIIO) | sin despliegue verificable (prototipo académico) → **descartado** |
| AR | CIIAR — Coalición de Ciudades por la IA | coalición/marco, no caso desplegado → **contexto, no candidato** |
| AR | Presupuestos participativos (RAPP, BAElige, Rosario) | sin NLP sobre el contenido → **no elegible** |
| CL | Escuchas Constitucionales (PNUD-IMFD) | **encuesta** de opinión (~500 resp.), no IA sobre aportes abiertos → **no elegible** |
| CL | OGP "lenguaje claro" / consulta Ley de IA | simplificación del lenguaje estatal / consulta **SOBRE** IA → **no elegible** |
| CL | "Measuring constitutional preferences" (2023) | análisis académico NLP de Cabildos 2016 (=baseline) → **no nuevo** |
| BR | Cátedra Brasil / Co:Lab USP (genAI en PP de São Paulo) | investigación en curso → **dudoso** (añadido) |
| BR | Gobernarte-BID 2025 (ganadores AR/BR/EC/MX) | IA para **servicios**/identidad digital, no participación → **no elegible** |
| BR | São Paulo, Brasil Participativo, e-Cidadania | **reconfirmados** (ya hallados en rondas 1-2) |

**Yield neto del piloto:** **1 candidato dudoso nuevo** (BR Cátedra Brasil) y
**0 nuevos elegibles** en AR y CL. Múltiples exclusiones por criterio.

## 4. Conclusión metodológica

La búsqueda ampliada **multiplica los *leads*** (encuestas, consultas SOBRE IA,
IA de servicios, coaliciones, prototipos), pero bajo **elegibilidad estricta** el
rendimiento marginal de casos **nuevos elegibles** en países ya flacos (AR, CL)
es **≈ 0**: confirma que son genuinamente escasos en este vector. El valor del
método ampliado se concentra en:
1. **Verificar/descartar con rigor** (resultado negativo informado).
2. **Países con despliegue real** (BR, y en menor medida CO/MX): ahí sí aparece
   densidad (subnacional + académico + plataformas).
3. **A.12 licitaciones** como canal de **alta señal** donde la compra pública esté
   digitalizada (SECOP-CO, ComprasNet-BR, Mercado Público-CL).

## 5. Recomendación de escalamiento (decisión del operador)

- **No** escalar el barrido ampliado **uniforme** a los 20 países: costo alto,
  yield bajo donde no hay despliegue.
- **Sí** aplicar el método ampliado **focalizado**: (a) profundizar BR, CO, MX
  por subnacional + A.12 licitaciones + académico; (b) usarlo como **verificación
  de los dudosos** (São Paulo, OPA Piauí, TT EngageTT, VE Plan de la Patria,
  Cátedra Brasil); (c) en los flacos, una pasada ligera A.12/A.13/A.14 y cerrar.
- Operacional: lotes pequeños de agentes con **síntesis parcial** para no perder
  trabajo ante límites de sesión.

> Los canales A.12–A.14 y el diccionario de términos quedaron **codificados en
> `config.yaml`** y reflejados en `search_frame.csv`, listos para futuras corridas.
