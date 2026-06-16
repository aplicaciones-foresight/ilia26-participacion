# Revisión de la metodología HPC — 5 países extra (DE, ES, PT, EE, SG)

Revisión crítica de la metodología del equipo para el **indicador de HPC** del índice
ILIA 2026, alineada a las **3 variables oficiales**. Fecha de referencia: estado
operativo a **junio 2026**; rankings de la lista **TOP500 de noviembre 2025**.

## 0. Las 3 variables oficiales (lo que hay que calcular)

| # | Variable | Definición oficial | Insumo por sistema |
|---|---|---|---|
| 1 | **Capacidad de infraestructuras HPC (GPU+CPU)** | Σ de teraflops/s **teóricos** según la cantidad de HPC del país | **Rpeak** (FP64) total |
| 2 | **Número de GPUs** | nº de tarjetas GPU **o equivalente** por millón de hab. | **nº de aceleradores** |
| 3 | **Capacidad GPUs** | teraflops/s de las GPU por millón de hab. | **TFLOP/s GPU** (FP64) |

Las variables 2 y 3 son explícitamente **per cápita** (÷ población/1.000.000). La
variable 1 no lo dice; **decisión abierta**: reportar absoluta y per cápita.

> La metodología del equipo (bloques A/B de cobertura/capacidad, intensidad de
> aceleración B3, índice compuesto) es un **valor añadido analítico** útil, pero el
> **entregable** son estas 3 variables. Esta revisión las prioriza.

## 1. Lo sólido (mantener)
- Cascada de fuentes por fiabilidad + triangulación.
- Separar **censo** (conteo) de **capacidad** (medible) y declarar la capacidad como **cota inferior**.
- Excluir cuántica (no sumable en FLOPS) y privados sin specs verificables.
- No imputar cuota compartida (LUMI → Estonia).
- Evitar doble conteo de la potencia GPU entre indicadores.

## 2. Correcciones críticas (afectan el cálculo de las 3 variables)
1. **Rpeak vs Rmax.** La definición oficial dice "teraflops **teóricos**" → es **Rpeak**.
   Coherente, pero "teórico" ≠ "medido": usar var.1 = Σ Rpeak y reportar **Rmax**
   (HPL medido) como respaldo.
2. **La capacidad NO se limita al TOP500.** Muchos sistemas nacionales/regionales
   publican su pico teórico y nº de GPUs en sus fichas (RES, NHR alemanes,
   MACC/Deucalion, Tartu…). Limitar al TOP500 subestima de más → recolectar Rpeak y
   nº GPUs de **toda ficha pública**, declarando cota inferior.
3. **nº de GPUs (var.2).** El TOP500 da *accelerator cores*, no tarjetas. Derivar
   tarjetas (cores ÷ cores-por-tarjeta) o leerlo de la ficha del centro. Definir
   "GPU o equivalente" = **tarjeta aceleradora discreta** (NVIDIA/AMD/Intel/NEC…);
   **1 Grace-Hopper = 1 GPU Hopper**.
4. **Precisión de var.3 — decisión clave para un índice de IA.** Con FP64 (coherente
   con var.1) las *AI Factories* y GPUs modernas se ven débiles (su FP64 es una
   fracción de su FP16/FP8). Recomendación: **FP64 principal + FP16/BF16 tensor
   acompañante**. Se recogen ambas.
5. **Población.** Fijar **una** fuente y **un** año para los 5 (ver `poblacion.csv`).

## 3. Comparabilidad / robustez
6. **Unidad de conteo y umbral.** La lista alemana mezcla Tier-0→Tier-3 + comerciales
   + industriales; las demás son cortas. Rompe la comparabilidad de "densidad" e infla
   el denominador alemán. Definir "1 sistema", marcar tier y considerar umbral (Tier-2+
   / acceso nacional) para conteos comparables.
7. **Sesgo de país pequeño.** El per-cápita dispara a Estonia (~1,37 M) y Singapur
   (~6,04 M). Reportar también **absolutos** y, si se puede, **por PIB**. Con n=5,
   min-max es frágil; para capacidad (varios órdenes de magnitud) considerar **log**.
8. **Privados/comerciales = subconteo grande en var.2/var.3.** Alemania
   (Telekom-NVIDIA, Aleph Alpha, IONOS, Schwarz/StackIT, Northern Data) y Singapur (hub
   de datacenters) tienen enormes parques GPU comerciales fuera del cómputo. Correcto
   excluirlos del titular, pero **declararlo como subestimación material** en las
   variables de GPU.
9. **EuroHPC:** atribuir por **país anfitrión** (JUPITER→DE, MareNostrum 5→ES,
   Deucalion→PT) y anotar cofinanciación UE.
10. **Ventana temporal:** TOP500 Nov-2025 vs estado Jun-2026 (7 meses). Fijar
    "operativo a Jun-2026" y anotar dónde el TOP500 va por detrás (JUPITER a escala
    completa, nuevas AI Factories).

## 4. Detalle menor
- El nivel 6 cita **WIPO** (patentes): poco pertinente; mejor **Green500/HPCG** +
  prensa de fabricantes + registros de adjudicación EuroHPC.
- "MN5 ≈ 95 % de la capacidad nacional" hay que **derivarlo del dato**.
- Aplicar la **regla de oro** del proyecto: ningún número de memoria; **cita verbatim
  + URL + fecha** por cifra.

## 5. Defaults adoptados (parametrizados en `src/hpc_calc.py`)
- var.1 = Σ Rpeak FP64 (absoluta **y** per cápita).
- var.3 = FP64 principal + FP16/BF16 tensor compañera.
- Cobertura de capacidad = **toda ficha pública** (cota inferior), no solo TOP500.
- Comerciales/industriales **fuera del titular**, en anexo.
- Población: ver `poblacion.csv` (pendiente fijar fuente única).

## 6. Decisiones que requieren al operador
- ¿var.1 per cápita, absoluta, o ambas? (default: ambas)
- ¿var.3 en FP64 o FP16/BF16 como principal? (default: FP64 + compañera FP16)
- ¿Cobertura = TOP500 only o toda ficha pública? (default: toda ficha pública)
- Fuente/año de población única para los 5.
- Umbral de conteo para comparabilidad (Tier-2+ / acceso nacional).
