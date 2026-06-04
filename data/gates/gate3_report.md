# Gate 3 — Validación final (Fase 5)

**Escenario activo:** A  ·  **Redondeo:** legacy  ·  **count_min_level:** 2

> ⚠️ **DRAFT**: los números 2026 dependen de la recodificación pre-Gate (`recodificacion_2025.csv`). No publicar sin validación humana.

## Reproducibilidad

- Control legacy 2025 vs oficial: desviación máx **1** (OK ≤1).
- Recálculo 2026 idéntico en dos corridas: **sí**.
- `model_version` (corrida): `PENDIENTE: fijar versión del modelo Claude usada en la corrida`

## Comparativo por país (Indicador) y alertas de cambio

Umbral de alerta: |Δ| > 15 puntos.

| País | 2025 oficial | 2026 | Δ | Alerta |
|---|:---:|:---:|:---:|:---:|
| AR | 0 | 0 | +0 |  |
| BO | 30 | 30 | +0 |  |
| BR | 76 | 77 | +1 |  |
| CL | 57 | 58 | +1 |  |
| CO | 85 | 71 | -14 |  |
| CR | 46 | 46 | +0 |  |
| CU | 0 | 0 | +0 |  |
| DO | 30 | 32 | +2 |  |
| EC | 25 | 26 | +1 |  |
| GT | 32 | 32 | +0 |  |
| HN | 42 | 42 | +0 |  |
| JM | 0 | 0 | +0 |  |
| MX | 47 | 24 | -23 | ⚠️ |
| PA | 0 | 0 | +0 |  |
| PE | 53 | 32 | -21 | ⚠️ |
| PY | 0 | 0 | +0 |  |
| SV | 0 | 0 | +0 |  |
| UY | 0 | 0 | +0 |  |
| VE | 0 | 0 | +0 |  |

## Descomposición Sub1 2026 por variable

| País | Tipos | Etapas | Continuidad | Convocante | Cantidad | Sub1 | Sub2 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| BO | 20 | 50 | 67 | 29 | 25 | 38 | 22 |
| BR | 20 | 75 | 67 | 58 | 50 | 54 | 100 |
| CL | 20 | 50 | 67 | 71 | 75 | 56 | 59 |
| CO | 60 | 50 | 67 | 67 | 25 | 54 | 88 |
| CR | 20 | 50 | 67 | 29 | 25 | 38 | 53 |
| DO | 20 | 25 | 67 | 42 | 25 | 36 | 28 |
| EC | 20 | 25 | 67 | 29 | 25 | 33 | 18 |
| GT | 20 | 25 | 67 | 25 | 25 | 32 | 32 |
| HN | 20 | 25 | 67 | 25 | 25 | 32 | 52 |
| MX | 20 | 25 | 67 | 17 | 25 | 31 | 18 |
| PE | 20 | 25 | 67 | 17 | 25 | 31 | 32 |

## Hashes de insumos (trazabilidad)

| Insumo | sha256[:16] |
|---|---|
| config.yaml | `760c4fc661ad771b` |
| prompt_v1.1_A | `464fc0e0cf2f799f` |
| prompt_v1.1_B | `ba347b0d2d2395d2` |
| schema_v1.1 | `40d383789623e848` |
| recodificacion_2025 | `90ecc0e8fffc5643` |
| BBDD_2025 | `391207e78a00e73a` |

## Fichas con evidencia (verbatim)

- Fichas conciliadas presentes: 0 (en esta corrida: ninguna; Fases 2-3 aún no ejecutadas)