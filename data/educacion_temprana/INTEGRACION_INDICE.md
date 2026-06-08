# Integración al índice — Subindicador (b) y puntajes

## Dónde vive (b) en la jerarquía ILIA

```
Factores Habilitantes → Talento Humano (30%) → Alfabetización en IA (40%)
   ├── (a) Educación temprana en ciencia   [PISA]      — fuera de este encargo
   ├── (b) Educación temprana en IA        [currículo] — ESTE análisis
   └── (c) Habilidad en inglés                          — fuera de este encargo
```

El subindicador (b) es **uno de los tres componentes** de «Alfabetización en IA». Aquí se calcula
**solo (b)**; (a) PISA y (c) inglés quedan fuera del encargo.

## Puntajes (b) por país

| País | ISO | Categoría (1–5) | Puntaje (b) |
|---|:--:|:--:|:--:|
| España | ES | 5 | 100 |
| Alemania | DE | 5 | 100 |
| Estonia | EE | 5 | 100 |
| Singapur | SG | 5 | 100 |
| Portugal | PT | 4 | 75 |
| **Promedio del grupo** | | | **95** |

Mapeo categoría→puntaje (Cuadro 2, p. 63 del ILIA): `1→0 · 2→25 · 3→50 · 4→75 · 5→100`. Sin
normalización (mapeo directo).

## Regla adoptada y nota sobre cursos electivos

**Regla adoptada (confirmada con el equipo del ILIA): inclusiva** — los **cursos electivos se
consideran** parte del currículo nacional. Por ello **Estonia y Singapur = 5**: su IA vive en una
asignatura **electiva** (Estonia: *Informaatika*; Singapur: *Computing 7155*) y aparece como
**subtema**; se documenta por transparencia.

A título **informativo** (sensibilidad, no adoptada), una lectura estricta dejaría a EE y SG en 4:

| Escenario | EE | SG | **Promedio grupo** |
|---|:--:|:--:|:--:|
| **Inclusiva** (adoptada, ILIA) | 5 (100) | 5 (100) | **95** |
| Estricta (solo informativa) | 4 (75) | 4 (75) | **85** |

España, Alemania y Portugal **no cambian** entre escenarios.

## Notas de integración

- Estos 5 son países **benchmark no latinoamericanos**: sirven de **referencia/comparación**, no
  entran en el ranking del índice LatAm.
- Datos legibles por máquina: `puntajes.csv` y `subindicador_b_puntajes.json`.
- **Reproducibilidad:** cada puntaje se deriva de evidencia citada y verificada *verbatim*
  (`fuentes/_verify_report.json`, 15/15 OK); ningún número de memoria (regla de oro del repo).
- **Coherencia:** el criterio «implementado vs propuesta» que separa el 4 del 5 se aplicó igual que
  en la calibración LatAm; los **cursos electivos se consideran (confirmado con el ILIA)**, con
  nota explícita para Estonia y Singapur.
