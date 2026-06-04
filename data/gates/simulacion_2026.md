# Fase 4 — Simulación comparativa (motor v2026)

> **Las columnas 2026 son BORRADOR.** Dependen de la recodificación pre-Gate (`data/baseline/recodificacion_2025.csv`): convocante derivado de la columna *Organización a cargo* y nivel de consolidación asignado de forma conservadora (Uso único/Plataforma → 2; 'Próximamente' → 1; nivel 3 solo con override + evidencia de recurrencia). NO publicar sin validación humana.

- Recodificación cargada: sí (27 filas)
- Redondeo: `legacy`  ·  thresholds y count_min_level desde config.yaml

## Control 2025 (motor legacy recalculado vs. oficial publicado)

Desviación máxima |motor − oficial| = **1** punto(s) (OK ≤1).

## Indicador final por país

| País | 2025 oficial | 2025 motor | 2026-A (cml=2) | 2026-A (cml=0) | 2026-B (cml=2) |
|------|:---:|:---:|:---:|:---:|:---:|
| AR | 0 | 0 | 0 | 0 | 0 |
| BO | 30 | 30 | 30 | 30 | 30 |
| BR | 76 | 76 | 77 | 77 | 77 |
| CL | 57 | 57 | 58 | 58 | 58 |
| CO | 85 | 84 | 71 | 71 | 71 |
| CR | 46 | 46 | 46 | 46 | 46 |
| CU | 0 | 0 | 0 | 0 | 0 |
| DO | 30 | 30 | 32 | 32 | 0 |
| EC | 25 | 25 | 26 | 26 | 26 |
| GT | 32 | 32 | 32 | 32 | 32 |
| HN | 42 | 42 | 42 | 42 | 42 |
| JM | 0 | 0 | 0 | 0 | 0 |
| MX | 47 | 48 | 24 | 24 | 24 |
| PA | 0 | 0 | 0 | 0 | 0 |
| PE | 53 | 54 | 32 | 32 | 32 |
| PY | 0 | 0 | 0 | 0 | 0 |
| SV | 0 | 0 | 0 | 0 | 0 |
| TT | 0 | 0 | 0 | 0 | 0 |
| UY | 0 | 0 | 0 | 0 | 0 |
| VE | 0 | 0 | 0 | 0 | 0 |

## Descomposición Sub1 (2026-A, cml=2) — DRAFT

| País | Tipos | Etapas | Continuidad | Convocante | Cantidad | Sub1 | n | n_cant |
|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| BO | 20 | 50 | 67 | 29 | 25 | 38 | 1 | 1 |
| BR | 20 | 75 | 67 | 58 | 50 | 54 | 4 | 4 |
| CL | 20 | 50 | 67 | 71 | 75 | 56 | 9 | 9 |
| CO | 60 | 50 | 67 | 67 | 25 | 54 | 3 | 3 |
| CR | 20 | 50 | 67 | 29 | 25 | 38 | 2 | 2 |
| DO | 20 | 25 | 67 | 42 | 25 | 36 | 1 | 1 |
| EC | 20 | 25 | 67 | 29 | 25 | 33 | 1 | 1 |
| GT | 20 | 25 | 67 | 25 | 25 | 32 | 1 | 1 |
| HN | 20 | 25 | 67 | 25 | 25 | 32 | 1 | 1 |
| MX | 20 | 25 | 67 | 17 | 25 | 31 | 1 | 1 |
| PE | 20 | 25 | 67 | 17 | 25 | 31 | 1 | 1 |

_Sub2 (Desarrollo) es idéntico a 2025 por construcción (§4.3)._
