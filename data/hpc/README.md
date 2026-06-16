# Indicador HPC — 5 países extra (Alemania, España, Portugal, Estonia, Singapur)

Sub-módulo del Pipeline ILIA 2026 para el **indicador de HPC** (3 variables) en los
5 países de referencia fuera de América Latina. Misma disciplina que el resto del
proyecto: ningún número sale de memoria; toda cifra lleva fuente + cita + fecha; el
cálculo es determinístico y las decisiones abiertas se parametrizan.

## Las 3 variables
1. **Capacidad HPC (GPU+CPU)** = Σ Rpeak (TFLOP/s teóricos, FP64).
2. **Número de GPUs** por millón de habitantes.
3. **Capacidad GPU** (TFLOP/s) por millón de habitantes.

## Flujo
```
Planilla manual (censo) ─► Agentes de investigación (capacidad por sistema)
   data/hpc/raw/investigacion_<pais>.md
        │  (consolidación humana/script -> normalizar a un esquema)
        ▼
   data/hpc/sistemas_consolidado.csv      (1 fila por sistema/partición)
        │  + poblacion.csv + ref_aceleradores.csv
        ▼
   src/hpc_calc.py  ─►  3 variables (absolutas y per cápita) + compañeras IA
```

## Archivos
| Archivo | Contenido |
|---|---|
| `METODOLOGIA_revision.md` | Revisión crítica de la metodología + decisiones |
| `poblacion.csv` | Denominador per cápita (fuente/año por país) |
| `ref_aceleradores.csv` | Pico FP64/FP16 por tarjeta (anclaje reproducible) |
| `raw/investigacion_<pais>.md` | Investigación detallada por país (agentes) |
| `sistemas_consolidado.csv` | Censo + capacidad normalizados (a llenar) |
| `../../src/hpc_calc.py` | Motor de cálculo determinístico |

## Esquema de `sistemas_consolidado.csv`
`pais_iso, sistema, centro, ciudad, categoria, tier, estado, en_top500, rank_top500,
rmax_tf, rpeak_tf, cpu_modelo, acelerador_modelo, n_gpus, gpu_fp64_tf, gpu_fp16_tf,
incluir_capacidad, incluir_gpu, confianza, fuente, cita, fecha, nota`

- `incluir_capacidad` / `incluir_gpu` (1/0): permiten excluir comerciales/cuotas
  compartidas (p. ej. LUMI) del titular sin borrar la fila.
- Capacidades sólo si hay **fuente pública**; si no, `null` + nota a revisión manual.
