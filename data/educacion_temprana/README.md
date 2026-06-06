# Educación temprana en IA — Subindicador (b), replicación ILIA para 5 países benchmark

Análisis **nuevo y autocontenido** que replica el subindicador **(b) "Educación
temprana en IA"** del índice **ILIA 2025 (CEPAL/CENIA)** para cinco países de
referencia **no latinoamericanos**: **Portugal (PT), España (ES), Estonia (EE),
Alemania (DE) y Singapur (SG)**.

Comparte la **metodología y el espíritu auditable** del resto del repo (pipeline de
participación ciudadana), pero vive aislado en esta carpeta y no toca el cálculo del
otro indicador.

> **Estado: BORRADOR (vía híbrida).** Las categorías de esta entrega se derivan de
> investigación con buscador (WebSearch) y se marcan para **confirmación verbatim**
> contra los documentos primarios decisivos (ver `fuentes/MANIFEST.md`). Ninguna
> categoría es definitiva hasta esa verificación.

## Qué mide el subindicador (b)

Dentro de la jerarquía del ILIA:

```
Factores Habilitantes → Talento Humano (30%) → Alfabetización en IA (40%)
   ├── (a) Educación temprana en ciencia        [PISA]      — NO en este encargo
   ├── (b) Educación temprana en IA             [currículo] — ESTE análisis
   └── (c) Habilidad en inglés                              — NO en este encargo
```

El subindicador (b) es una **revisión documental del currículo escolar oficial**: ¿el
currículo legal vigente incluye **IA** y/o **TIC**, y en qué grado de implementación?
La fuente original del ILIA (**SITEAL**) solo cubre América Latina; para estos 5 países
la categoría se apoya **enteramente en la revisión de sus currículos nacionales**.

## Rúbrica de categorización (Cuadro 2, p. 63 del ILIA) — mapeo directo a puntaje

| Cat. | Descripción | Puntaje |
|---|---|---|
| 1 | No tiene propuesta | 0 |
| 2 | Propuesta TIC | 25 |
| 3 | Propuesta IA | 50 |
| 4 | TIC implementado (tecnología, información y computación) | 75 |
| 5 | IA implementado | 100 |

- **"Propuesta"** = existe en lineamientos/estrategias pero **no** implementado en el
  currículo vigente. **"Implementado"** = vigente/obligatorio en el currículo nacional.
- **Orden ordinal** (relevante): `nada(0) < TIC-propuesta(25) < IA-propuesta(50) <
  TIC-implementada(75) < IA-implementada(100)`. El **estado de implementación** pesa más
  que "IA vs TIC", salvo en el tramo implementado.
- **Criterio del salto a 5 (100):** exige contenido de **IA explícito y vigente**
  (obligatorio / en el currículo en vigor), **no** mera competencia digital/TIC ni una
  estrategia/plan/piloto no curricular (eso último ⇒ "propuesta").
- **Calibración LatAm 2025** (referencia de coherencia): categoría 5 = Brasil, Chile,
  Costa Rica, Ecuador, Rep. Dominicana, Uruguay; el resto, categoría 4.
- **Decisión de umbral (2026-06-05): regla INCLUSIVA** — la IA presente en *cualquier*
  asignatura del currículo nacional vigente, **incluidas las electivas**, cuenta como «IA
  implementada» (cat. 5). Bajo esta regla, **EE y SG = 5**. (Reglas más estrictas —cursado
  universal o contenido sustantivo— devolverían EE y SG a 4; se aplica por igual a los cinco.)

### Términos de búsqueda por idioma (para IA explícita)
- ES: «inteligencia artificial», «IA»
- PT: «inteligência artificial», «IA»
- EE: «tehisintellekt», «tehisaru» (+ EN «artificial intelligence»)
- DE: «Künstliche Intelligenz», «KI»
- SG: «artificial intelligence», «AI», «machine learning»

## Alcance

- **Solo subindicador (b)** (revisión curricular). No incluye (a) PISA ni (c) inglés.
- **Todos los niveles** se documentan (infantil → primaria → secundaria → FP), pero la
  **categoría/puntaje se asigna sobre SECUNDARIA**, fiel a la definición del ILIA. Los
  demás niveles son evidencia de apoyo.
- **Sin normalización**: (b) es mapeo directo categoría→puntaje (no lleva min-max). La
  normalización, si se quiere, se hará después en el recálculo del ILIA 2026.

## Método (vía híbrida) y limitación de red — transparencia

Este entorno de ejecución tiene una **política de red por allowlist** que **bloquea la
descarga directa** de los portales oficiales (BOE, Diário da República, Riigi Teataja,
KMK/Länder, MOE/SEAB…): tanto `curl/wget` como `WebFetch` devuelven `403 "Host not in
allowlist"`. Solo **WebSearch** está disponible.

Por eso la entrega sigue una **vía híbrida**:

1. **Borrador con WebSearch** — investigación por país (un agente por país) que fija la
   estructura del sistema educativo, el estado curricular de TIC/IA en secundaria, una
   **categoría propuesta (1–5)** con justificación, y la lista de **documentos primarios
   decisivos**.
2. **Confirmación verbatim (pendiente)** — para las determinaciones que fijan el puntaje
   de secundaria, se leen a fondo los documentos primarios y cada cita se verifica como
   **subcadena exacta** del documento, con la misma lógica que `src/verify_verbatim.py`
   del repo. Esos documentos se listan en `fuentes/MANIFEST.md`; el operador los aporta
   (descarga + commit a `fuentes/<pais>/`, o pega el texto), ya que el entorno no puede
   descargarlos.

Reglas heredadas del repo:
- **«Ningún número de memoria»**: categoría y puntaje derivan de evidencia citada con
  URL, no de supuestos (aunque existan priores, p. ej. Estonia/Singapur).
- **Doble criterio** explícito por país: TIC vs IA, y propuesta vs implementado.
- **Confianza** marcada por país (alta/media/baja); mejor `null` + alerta que un valor
  no respaldado.

## Estructura de la carpeta

```
data/educacion_temprana/
├── README.md            este archivo (método, rúbrica, limitaciones)
├── informe.md           informe por país + tabla comparativa + limitaciones
├── puntajes.csv         pais, categoria, puntaje, nivel_evaluado, confianza, resumen
├── evidencias/          evidencia estructurada por país (TIC/IA, cita, traducción, URL)
│   └── evidencias.json
└── fuentes/
    ├── MANIFEST.md       inventario + "shopping list" de descargas manuales pendientes
    ├── PT/  ES/  EE/  DE/  SG/   (copias de documentos oficiales que aporte el operador)
```

## Reproducibilidad

- Cada categoría queda trazada a sus fuentes (URL) en `informe.md` y `evidencias/`.
- Tras la confirmación verbatim, cada cita decisiva será subcadena exacta del documento
  primario en `fuentes/<pais>/`, verificable con la utilidad de verbatim del repo.
- Chequeo de coherencia con la rúbrica y con la calibración LatAm 2025.
