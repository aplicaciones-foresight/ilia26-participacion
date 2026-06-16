# Investigación HPC — ESTONIA (indicador ILIA 2026)

**País:** Estonia · **Fecha de referencia:** estado operativo a **junio 2026**; rankings **TOP500 noviembre 2025**.
**Fecha de acceso a las fuentes:** 2026-06-16 · **Idioma de trabajo:** español · **Fuentes:** estonio/inglés.
**Analista:** investigación automatizada (agente ILIA) · **Variables objetivo por sistema:**
(1) Rpeak FP64 (TFLOP/s, capacidad HPC CPU+GPU); (2) nº de GPUs / aceleradores; (3) capacidad GPU teórica (TFLOP/s FP64);
acompañantes: Rmax (HPL FP64), modelo y nº de CPU, modelo de acelerador, pico GPU FP16/BF16 Tensor (métrica IA).

> **Nota metodológica crítica sobre el acceso a fuentes:** en este entorno la herramienta de descarga directa de páginas (WebFetch) y el `curl` del sandbox estuvieron **bloqueados** (HTTP 403 / "host not in allowlist") para TODOS los dominios objetivo (hpc.ut.ee, docs.hpc.ut.ee, docs.hpc.taltech.ee, docs.hep.kbfi.ee, etais.ee, top500.org, web.archive.org). Por tanto, **todas las citas verbatim provienen de los resúmenes/snippets del buscador web (WebSearch)**, no del texto íntegro renderizado de cada página. Esto baja la confianza de las cifras exactas (especialmente conteos por nodo) y obliga a una **lista de REVISIÓN MANUAL** con la URL exacta a abrir para cada dato frágil. **No se ha inventado ningún número.**

---

## RESUMEN EJECUTIVO

- **TOP500 Nov-2025:** Estonia **no tiene ningún sistema** físicamente instalado en la lista. Su único vínculo es la **cuota en LUMI** (Finlandia, CSC), que **NO se imputa como capacidad nacional** (ver Anexo LUMI).
- **Sistemas nacionales (ETAIS):** **Rocket** (Univ. de Tartu / UTHPC, Tartu) — claramente el sistema **dominante**; **TalTech HPC** (Tallinn); **NICPB/KBFI** (Tallinn, Tier-2 WLCG, mayoritariamente CPU).
- **Hecho determinante (junio 2026):** el centro HPC de la Univ. de Tartu ejecutó en **febrero de 2026** una gran ampliación de IA (12× H200, 24× B200, 40× RTX Pro 6000 Blackwell), declarando un agregado de **"164 GPUs, 21.520 CPU threads y 118 TB de memoria"** (cloud + Kubernetes + clúster). Esto domina el per-cápita estonio.
- **Ningún centro publica un Rpeak FP64 agregado y actual.** La única cifra oficial de Rpeak encontrada (59 TFLOP/s, Rocket) es **de la era original ~2014 y está obsoleta**. → Rpeak total del país: ver "Totales país"; gran parte va a **REVISIÓN MANUAL**.

---

## (a) TABLA POR SISTEMA

Leyenda confianza: **A**=alta · **M**=media · **B**=baja · **n/p**=no publicado / no encontrado.
TFLOP/s = FP64 salvo indicación. "GPU FP64 (TF)" y "GPU FP16 (TF)" son **sumas teóricas derivadas de datasheet** (ver tabla de aceleradores) sobre el nº de tarjetas confirmadas.

| Sistema | Centro | Ciudad | Categoría | Estado (jun-2026) | Rank TOP500 Nov-25 | Rmax FP64 (TF) | Rpeak FP64 (TF) | CPU (modelo, sockets/cores) | Acelerador (modelo) | nº GPUs | GPU FP64 (TF) | GPU FP16/BF16 (TF) | Fuente(s) | Confianza |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Rocket — clúster Slurm** | Univ. de Tartu HPC (UTHPC) / ETAIS | Tartu | HPC académico nacional | Operativo | No listado | n/p | **n/p** (59 TF oficial pero OBSOLETO, era ~2014) | CPU: ~40 nodos 2× AMD EPYC 7702/7763 64C (128 c/nodo) "ares/artemis"; GPU-nodos: Intel Xeon E5-2650 v4 (Falcon), AMD EPYC 7642/7713/9575F | NVIDIA Tesla **V100** (16/32GB) + **A100-40** + **A100-80** + **H200-141** (gres confirmados) | **≈64–68** (ver desglose) | **≈590–860** (cota; ver cálculo) | **≈8.700** (cota; A100+H200) | hpc.ut.ee/Rocket(-harware); docs.hpc.ut.ee gpu_computing; etais.ee; ut.ee press | conteo M / Rpeak n/p |
| **UTHPC — centro completo (agregado)** | Univ. de Tartu HPC / ETAIS | Tartu | HPC+nube+K8s nacional | Operativo (tras ampliación feb-2026) | No listado | n/p | **n/p** | "21.520 CPU threads" (agregado; sin modelo único) | V100 + A100 + H200 + **B200** + **RTX Pro 6000 Blackwell** + L40S | **164** (agregado oficial) | **n/p** (mezcla de gens; cota ≥ la del clúster) | **n/p** (decenas de PFLOP/s en IA; no publicado el total) | innovationnewsnetwork (UTHPC) ; etais.ee news | agregado A / desglose M |
| **TalTech HPC** | Tallinn Univ. of Technology / ETAIS | Tallinn | HPC académico nacional | Operativo | No listado | n/p | **n/p** | green: 32× 2×Xeon Gold 6148 (40c); gray: 48× 2×Xeon E5-2630L (12c); mem1tb: 4×Xeon E5-4640; GPU: 2×EPYC 7742/7713 64C (amp), 2×EPYC 9354 32C (ada) | **A100-40** (amp1) + **A100-80** (amp2) + **L40-48** (ada) [+ Tesla K20Xm en viz, heredado] | **20** (16× A100 + 4× L40) | **≈161** (8×9.7 + 8×9.7 + 4×1.4) | **≈5.000** (16× A100 ×312) | docs.hpc.taltech.ee/hardware, /gpu | A (conteo) |
| **NICPB cluster** | National Inst. of Chemical Physics & Biophysics (KBFI) / ETAIS | Tallinn | HPC/Grid Tier-2 (WLCG/CMS), mayoría CPU | Operativo | No listado | n/p | **n/p** | ~205 nodos, **~8.000 cores** (modelos Intel/AMD no publicados en snippet) | Pocas GPU: **9× RTX 2070 Super 8GB** (gpu0) + **2× A100-80** (gpu1) | **≈11** (2 de cómputo FP64 + 9 consumo) | **≈19** (2× A100 ×9.7; las RTX2070S ≈0 FP64 útil) | **≈624** (2× A100 ×312) | docs.hep.kbfi.ee/about, /compute, kbfi.ee | nodos A / GPU M |
| **LUMI (cuota Estonia)** | EuroHPC / CSC — **Kajaani, FINLANDIA** | (no nacional) | pre-exascale EuroHPC | Operativo | **#9** (Nov-2025) | **≈379–380** PFLOP/s = 379.000 TF | **≈531** PFLOP/s = 531.000 TF | 2× AMD EPYC 64C "Trento"/3rd gen | AMD Instinct **MI250X** | **10.240** (sistema completo) | — (sistema completo) | — | top500.org/system/180048; Wikipedia LUMI; lumi-supercomputer.eu | A (sistema) |

> **EXCLUSIÓN LUMI:** la fila LUMI se incluye **solo como anexo/nota**. NO entra en los totales nacionales (sistema físicamente en Finlandia; ver §(e) y Anexo LUMI). La cuota estonia exacta (%) **no se encontró publicada**.

### Desglose de GPUs de Rocket (clúster Slurm) — conteo por nodo

| Nodo(s) | GPU modelo | nº | FP64/tarjeta (TF) | Σ FP64 (TF) | FP16/BF16 Tensor/tarjeta (TF) | Σ FP16 (TF) | Confianza | Fuente |
|---|---|---|---|---|---|---|---|---|
| Falcon 1–6 | Tesla **V100** (16/32GB) | **~48** (incierto; snippet "44") | 7.8 | ~374 | 125 (Tensor FP16) | ~6.000 | **B** (44 vs 48) | hpc.ut.ee/Rocket-harware; portal.hpc.ut.ee |
| Pegasus | **A100-40** | **4** | 9.7 | 38.8 | 312 | 1.248 | M | hpc.ut.ee/Rocket-harware |
| Pegasus2 | **A100-80** | **8** | 9.7 | 77.6 | 312 | 2.496 | M | hpc.ut.ee/Rocket-harware |
| Firefly 1–2 | **H200-141 NVL** | **8** (4+4) | 34 | 272 | ~835–990 (NVL dense) | ~6.700–7.900 | **A** (corroborado ETAIS) | etais.ee; hpc.ut.ee/Rocket-harware |
| **Σ clúster Slurm** | — | **≈68** | — | **≈762** (cota) | — | **≈10.500** (cota IA) | mixta | — |

> Nota: el titular oficial de Rocket dice **"64 GPUs"**, pero la suma por nodo da ~68 (48 V100 + 4 + 8 + 8). El "64" probablemente es anterior a los 8× H200 (ago-2025) o el conteo de V100 es menor. **Discrepancia → REVISIÓN MANUAL.** Σ FP64 ≈ 762 TF y Σ FP16 ≈ 10,5 PFLOP/s son **cotas inferiores** sujetas a confirmar el nº de V100.

---

## (b) FUENTES Y CITAS POR SISTEMA

### ROCKET / UTHPC (University of Tartu)

- **Composición general (variante "actual"):** "Rocket is a heterogeneous HPC cluster that currently consists of **50 compute nodes**, featuring almost **12000 cores**, a bit over **5 terabytes of memory and 64 GPUs**, interconnected by high-speed low-latency Infiniband networking." — https://hpc.ut.ee/services/HPC-services/Rocket — acceso 2026-06-16 — **M** (snippet).
- **Variante de docs (más antigua, en conflicto):** "Rocket ... currently consists of about **175 compute nodes**, ... almost **7000 cores**, ... **40 terabytes of memory and 40 GPUs**." — https://docs.hpc.ut.ee/public/ — acceso 2026-06-16 — **M** (snippet; versión distinta).
- **Variante histórica / Rpeak original (OBSOLETA):** "equipped with **135 compute nodes**, a separate server with large memory, RAM 2TB, ... **8 accelerator cards**, with a **theoretical maximum capacity of 59 Tflops**." — https://ut.ee/en/content/high-performance-computing-centre-university-tartu-will-receive-more-capacity-amount-14 — acceso 2026-06-16 — **M** (era ~2014; no usar como Rpeak actual).
- **Tipos de GPU (gres Slurm) — confirmado:** "The available GPU types on the rocket cluster are: **gpu:tesla, gpu:a100-40g, gpu:a100-80g, and gpu:h200-141g**." — https://docs.hpc.ut.ee/public/cluster/Running_jobs/gpu_computing/ — acceso 2026-06-16 — **A**. (Implica V100 + A100-40 + A100-80 + H200; **sin H100 ni A40**.)
- **Falcon (V100):** "Falcon 1-6 nodes with NVIDIA Tesla V-100 GPUs ... 2x Intel Xeon CPU E5-2650 v4 @ 2.20GHz (48 cores total), 512 GB RAM ... Falcon 3 GPUs having 16 GB of vRAM and others having 32 GB." — https://hpc.ut.ee/services/HPC-services/Rocket-harware — acceso 2026-06-16 — **M**. (Un snippet citó "**44x** NVIDIA Tesla V-100 GPUs total" — **B**, dudoso.)
- **Conteo V100/A100 (portal):** "the Rocket cluster has **16 A100 GPUs** ... In addition to the A100s, there are **48 Tesla V100 GPUs**." — https://portal.hpc.ut.ee/rocket-cluster — acceso 2026-06-16 — **B** (16 A100 no reconcilia con 4+8=12 por nodo).
- **Pegasus (A100-40):** "pegasus.hpc.ut.ee: 2x AMD EPYC 7642 ... **4x NVIDIA Tesla A-100 with 40 GB** of vRAM each, ... 200 Gbps link." — https://hpc.ut.ee/services/HPC-services/Rocket-harware — acceso 2026-06-16 — **M**.
- **Pegasus2 (A100-80):** "pegasus2.hpc.ut.ee: 2x AMD EPYC 7713 64-Core ... 2 TB RAM ... **8x NVIDIA Tesla A-100 with 80 GB** of vRAM each." — https://hpc.ut.ee/services/HPC-services/Rocket-harware — acceso 2026-06-16 — **M**.
- **Firefly (H200) — ago-2025:** "two new machines, each equipped with **four high-VRAM H200 NVL 141GB PCIe 5.0 x16 GPUs** ... combined video memory of up to 564 GB within a single machine ... 200gbps Infiniband connection between the machines." — https://etais.ee/en/etais-member-university-of-tartus-center-for-scientific-computing-ramps-up-ai-power-with-cutting-edge-gpus-to-secure-digital-future/ — acceso 2026-06-16 — **A**.
- **L40S (NUBE, no Rocket):** "expanded its cloud resources with **eight NVIDIA L40S GPUs**, each boasting 48GB of VRAM ... up to two per virtual machine." — misma URL ETAIS — acceso 2026-06-16 — **A**. (No es clúster Slurm; es OpenStack.)
- **Ampliación FEB-2026 + agregado del centro (CLAVE):** "In February 2026, the University of Tartu's computing capacity increased by approximately an order of magnitude with ... **12 NVIDIA H200, 24 NVIDIA B200, and 40 NVIDIA RTX Pro 6000 Blackwell Max-Q GPUs** ... In collaboration with the **Ministry of Justice and Digital Affairs** ... the combined cloud, Kubernetes, and cluster infrastructure now comprises **164 GPUs, 21,520 CPU threads, and 118 TB of system memory**, alongside more than 17 petabytes of usable storage and over 30 petabytes ... archival." — https://www.innovationnewsnetwork.com/university-of-tartu-high-performance-computing-centre-building-fully-sovereign-ai-infrastructure/67352/ — acceso 2026-06-16 — **M/A** (medio especializado; el agregado de 164 GPUs es A).
- **CPU AMD (ares/artemis):** "40 nodes with AMD CPUs (called ares 1-20, artemis 1-20) ... 2x AMD EPYC 7702 64-Core ... Artemis nodes have AMD EPYC 7763 CPUs." — https://docs.hpc.ut.ee/public/ETAIS/adding_rocket/ — acceso 2026-06-16 — **M**.
- **Partición GPU:** "#SBATCH --partition=gpu" / "srun -p gpu --gres gpu:tesla:1". — https://docs.hpc.ut.ee/public/cluster/Running_jobs/gpu_computing/ — acceso 2026-06-16 — **A** (la partición se llama `gpu`; "falcon/pegasus/firefly" son hostnames, no particiones).

### TALTECH HPC (Tallinn University of Technology)

- **green (CPU):** "TalTech has **32 green nodes**, each with **2 x Intel Xeon Gold 6148 20C 2.40 GHz** (40 cores, 80 threads per node) ... 96 GB DDR4-2666 R ECC RAM. 18 of these green nodes are connected with FDR InfiniBand (green-ib partition)." — https://docs.hpc.taltech.ee/hardware.html — acceso 2026-06-16 — **A**.
- **gray (CPU):** "There are **48 gray nodes** (former hpc.ttu.ee nodes), each with **2 x Intel Xeon E5-2630L 6C** with 64 GB RAM ... QDR InfiniBand." — https://docs.hpc.taltech.ee/hardware.html — acceso 2026-06-16 — **A**.
- **mem1tb:** "1 mem1tb large memory node, 1 TB RAM, **4x Intel Xeon CPU E5-4640** (together 32 cores, 64 threads)." — https://docs.hpc.taltech.ee/hardware.html — acceso 2026-06-16 — **A**.
- **amp1 (A100-40):** "amp1: CPU: **2x AMD EPYC 7742 64core** (Zen2) ... RAM: 1 TB ... **GPUs: 8x A100 Nvidia 40GB**, OS: Rocky8." — https://docs.hpc.taltech.ee/gpu.html — acceso 2026-06-16 — **A**.
- **amp2 (A100-80):** "amp2: CPU: **2x AMD EPYC 7713 64core** (Zen3) ... RAM: 2 TB ... **GPUs: 8x A100 Nvidia 80GB**." — https://docs.hpc.taltech.ee/gpu.html — acceso 2026-06-16 — **A**. (Un resumen genérico dijo "7742" para amp2; la página dedicada dice **7713**.)
- **ada (L40):** "ada[1,2]: CPU: **2x AMD EPYC 9354 32core** (Zen4) RAM: 1.5 TB, **GPUs: 2x L40 Nvidia 48GB**, Features: avx512" y "**2 ada GPU nodes with 2x Nvidia L40/48GB**." — https://docs.hpc.taltech.ee/gpu.html — acceso 2026-06-16 — **A** (texto literal dice **"L40"**, no "L40S"; gres `--gres=gpu:L40`, capability nvcc89/sm_89).
- **viz (heredado):** "The visualization node viz is equipped with **2x Nvidia Tesla K20Xm** ... Intel Xeon E5-2630L v2, 64 GB RAM." — https://docs.hpc.taltech.ee/visualization.html — acceso 2026-06-16 — **M** (legado; no se cuenta en GPU de cómputo). *Conflicto:* un snippet mapeó "viz" a "8× A100 + EPYC 7742" (idéntico a amp1) → casi seguro error del buscador → REVISIÓN MANUAL.
- **Rpeak/TFLOP/s:** **no encontrado** en ningún snippet (existe página `performance.html` sin cifra visible). — https://docs.hpc.taltech.ee/performance.html — acceso 2026-06-16 — **A** (de que no se encontró cifra).

### NICPB / KBFI (National Institute of Chemical Physics and Biophysics)

- **Nodos/cores:** "The NICPB compute cluster contains **205 compute nodes** and 11 distributed storage nodes." / "around **8000 compute cores** and ... **3.8 PB** of raw disk ... 10Gbit local network." — https://docs.hep.kbfi.ee/about/ — acceso 2026-06-16 — **A** (cifra alternativa ~7100 threads / ~4.5 PB en otra fuente → **M**).
- **GPUs (SÍ tiene, pocas):** nodo "gpu0 with **9x 8GB RTX2070S** and gpu1 with **2x 80GB A100**". — https://docs.hep.kbfi.ee/compute/ — acceso 2026-06-16 — **M/A** (recuento exacto a verificar en la página).
- **Rol Tier-2:** "The Tier-2 computing centre is one of the biggest computing centres for the CMS experiment in Europe, consisting of **7600+ computing cores and 4.5 PB** of disk space plus dedicated machines for cosmological simulations." — https://kbfi.ee/en/nicpb/research-programmes/high-energy-physics-and-theoretical-physics/ — acceso 2026-06-16 — **M**.
- **Modelos de CPU:** **no publicado** en snippet (la página /compute/ los lista pero no se devolvieron las marcas). — REVISIÓN MANUAL.
- **Rpeak/TFLOP/s:** **no encontrado.**

### TOP500 Nov-2025 (verificación Estonia)

- "As of November 2025, **171** of the world's 500 most powerful supercomputers were located in the United States ... Japan ... 43 ... China and Germany ... 40 each." y "**Estonia does not appear to have any systems ranked in the TOP500** list itself ... zero systems." — https://www.statista.com/statistics/264445/ ; https://www.top500.org/lists/top500/2025/11/highs/ — acceso 2026-06-16 — **A** (Estonia sin sistemas nacionales).

---

## (c) REVISIÓN MANUAL (sistemas/cifras sin specs confirmadas + página/PDF exacto)

> Prioridad ALTA para el per-cápita: Estonia es pequeña; cada GPU y cada TF cuentan.

1. **Rocket — nº exacto de V100 (44 vs 48) y reconciliación "64 GPUs" vs ~68.**
   Abrir: `https://hpc.ut.ee/services/HPC-services/Rocket-harware` (tabla de hardware por nodo) y `https://portal.hpc.ut.ee/rocket-cluster`. Confirmar V100 por Falcon (1–6) y total A100.
2. **Rocket — Rpeak FP64 actual.** No publicado. Abrir `https://hpc.ut.ee/services/HPC-services/Rocket` y `https://docs.hpc.ut.ee/public/cluster/overview/`. Si no existe, **derivar** de nº de nodos AMD EPYC × specs (la cifra 59 TF está obsoleta).
3. **Rocket — cores/sockets reales de los nodos GPU.** Los snippets dieron "192/256 cores" que parecen *threads* (2× 64C = 128 cores). Abrir `Rocket-harware`.
4. **UTHPC centro completo — desglose de las 164 GPUs por modelo y su FP64/FP16.** Abrir `https://www.innovationnewsnetwork.com/university-of-tartu-high-performance-computing-centre-building-fully-sovereign-ai-infrastructure/67352/` y noticias en `https://etais.ee/en/category/news-en/` (nota feb-2026). Confirmar si los 12× H200 (feb-2026) **incluyen o se suman** a los 8× H200 (ago-2025), y cuántas B200/RTX Pro 6000 entran en cómputo FP64.
5. **TalTech — Rpeak/TFLOP/s.** Abrir `https://docs.hpc.taltech.ee/performance.html`.
6. **TalTech — nodo "viz".** Confirmar K20Xm vs A100 en `https://docs.hpc.taltech.ee/visualization.html` y `https://docs.hpc.taltech.ee/hardware.html`. ¿"L40" o "L40S"? `https://docs.hpc.taltech.ee/gpu.html` (texto literal: "L40").
7. **TalTech — total oficial de nodos/cores.** Ninguna fuente da un total textual; los totales son aritméticos. Confirmar tabla resumen en `hardware.html`.
8. **NICPB — modelos de CPU, cores/nodo, y recuento exacto de GPU (gpu0/gpu1).** Abrir `https://docs.hep.kbfi.ee/compute/` y `https://hep.kbfi.ee/index.php/IT/Cluster`. Reconciliar 8000 cores/3.8 PB vs 7100 threads/4.5 PB. Rpeak: ¿publicado en algún lugar?
9. **LUMI — cuota exacta de Estonia (%).** No encontrada. Abrir `https://lumi-supercomputer.eu/lumi-consortium/`, `https://www.eurohpc-ju.europa.eu/` (decisión LUMI 2020) y `https://eurocc-estonia.ee/hpc-in-estonia/`. (Solo para la nota; no entra en el cómputo.)
10. **B200 FP64 (dato datasheet en disputa: ~40 TF dense vs ~90 TF con Tensor).** Confirmar en datasheet NVIDIA Blackwell antes de imputar FP64 de las 24× B200 de Tartu.

---

## (d) TOTALES PAÍS (COTA INFERIOR) — SIN LUMI

> Criterio: se suman solo cifras con confianza ≥ media y **tarjetas físicas confirmadas**. Donde un dato falta, NO se imputa (se manda a revisión). Por eso son **cotas inferiores**. Se ofrecen DOS lecturas para Tartu (conservadora = clúster Slurm; ampliada = agregado del centro 164 GPUs), porque las fuentes mezclan ambos marcos.

### nº de GPUs (tarjetas físicas)

| Sistema | GPUs contadas (cota) | Detalle |
|---|---|---|
| Rocket (clúster Slurm) | **≈68** (o 64 titular) | 48 V100 + 4 A100-40 + 8 A100-80 + 8 H200 |
| TalTech | **20** | 16 A100 + 4 L40 (sin viz) |
| NICPB | **2** (cómputo FP64) / 11 (con 9 RTX2070S) | 2 A100-80 útiles FP64; 9 RTX2070S ≈0 FP64 |
| **Σ país (conservadora, clúster Rocket)** | **≈90 GPUs** (cómputo) / ~99 con RTX2070S | — |
| **Σ país (ampliada, UTHPC centro completo = 164)** | **≈184 GPUs** (164 Tartu + 20 TalTech) / ~195 con RTX2070S | usar SOLO si el indicador admite cloud/K8s |

### Σ Rpeak FP64 (TFLOP/s)

- **No computable de forma fiable:** **ningún** sistema publica Rpeak FP64 actual. → **null + REVISIÓN MANUAL** (puntos 2, 5, 8). Cota inferior derivable únicamente de GPUs (abajo). Evitar la cifra obsoleta de 59 TF.

### Σ GPU FP64 (TFLOP/s) — derivada de datasheet, cota inferior

| Sistema | Cálculo | Σ FP64 (TF) |
|---|---|---|
| Rocket | 48×7.8 (V100) + 4×9.7 + 8×9.7 (A100) + 8×34 (H200) = 374 + 38.8 + 77.6 + 272 | **≈762** |
| TalTech | 8×9.7 + 8×9.7 (A100) + 4×1.4 (L40) = 77.6 + 77.6 + 5.6 | **≈161** |
| NICPB | 2×9.7 (A100; RTX2070S≈0 útil) | **≈19** |
| **Σ país (conservadora)** | — | **≈942 TF FP64 ≈ 0,94 PFLOP/s** |
| *Adicional si se cuenta el centro Tartu completo* | + B200/H200/RTX Pro 6000 feb-2026 | **n/p** (B200 FP64 en disputa; revisión punto 4/10) |

### Σ GPU FP16/BF16 Tensor (TFLOP/s) — métrica IA, cota inferior

| Sistema | Cálculo (dense) | Σ FP16 (TF) |
|---|---|---|
| Rocket | 48×125 (V100) + 12×312 (A100) + 8×~990 (H200) ≈ 6.000 + 3.744 + ~7.900 | **≈17.600** |
| TalTech | 16×312 (A100) | **≈4.992** |
| NICPB | 2×312 (A100) | **≈624** |
| **Σ país (conservadora)** | — | **≈23.200 TF ≈ 23 PFLOP/s (FP16)** |
| *Adicional centro Tartu completo (feb-2026)* | 24× B200 (~2.250 TF c/u dense FP16) + 12× H200 + 40× RTX Pro 6000 | **n/p** — del orden de **>70 PFLOP/s FP16** (no publicado el total; revisión punto 4) |

**Qué ENTRA:** Rocket (UTHPC), TalTech, NICPB — todos en Estonia (ETAIS).
**Qué SALE:** **LUMI** (en Finlandia; solo cuota) — ver §(e). GPUs de **nube/Kubernetes** de Tartu (L40S, parte de B200/RTX Pro 6000) en la lectura conservadora; se listan en la lectura ampliada.

---

## (e) NOTAS DE CALIDAD

### Tratamiento de LUMI (cuota, EXCLUIDA del cómputo nacional)
- **Por qué se excluye:** LUMI está **físicamente en Kajaani, Finlandia (CSC)** y en TOP500 Nov-2025 figura como sistema **finlandés (#9)**. Imputarlo a Estonia sería doble conteo y rompería la comparabilidad por país. Se registra **solo como anexo**.
- **Datos LUMI (contexto):** Rmax ≈ **379–380 PFLOP/s** (HPL FP64), Rpeak ≈ **531 PFLOP/s**; **10.240 GPU AMD Instinct MI250X**; 362.496 cores; **TOP500 Nov-2025 #9**. Fuentes: top500.org/system/180048, Wikipedia LUMI, lumi-supercomputer.eu. Confianza **A** (sistema).
- **Cuota de Estonia:** estructura confirmada = **50 % EuroHPC JU + 50 % consorcio** (repartido por contribución financiera); Estonia es **miembro fundador** del consorcio (Finlandia + 10 países). El **porcentaje exacto de Estonia NO está publicado** (referencias: Finlandia ~23–25 %, Suecia ~3.5 %). Acceso vía **ETAIS** y portal **Puhuri** (operado por UTHPC). → **null + REVISIÓN MANUAL** (punto 9). No afirmar un % sin fuente.

### Concentración
- **Altísima concentración en Tartu (UTHPC/Rocket).** Tartu concentra la práctica totalidad de la capacidad GPU/IA nacional y, tras la ampliación feb-2026 (B200/H200/RTX Pro 6000) con el Ministerio de Justicia y Asuntos Digitales, **un orden de magnitud más**. TalTech aporta 20 GPU A100/L40; NICPB es CPU-dominante (Tier-2 CMS) con uso GPU marginal.
- **Riesgo metodológico (doble marco Tartu):** las fuentes mezclan "clúster Rocket (Slurm)" y "centro completo (cloud+K8s+clúster, 164 GPUs)". El indicador debe decidir explícitamente **qué frontera usa**; aquí se reportan ambas. La diferencia (≈64–68 vs 164 GPUs) es grande y **material para el per-cápita**.

### Calidad de las cifras
- **Punto débil principal:** ausencia total de **Rpeak FP64 oficial actual** (todos los centros) y conteo exacto de **V100 en Rocket**. Ambos a REVISIÓN MANUAL.
- Todas las sumas FP64/FP16 son **derivadas de datasheet** sobre tarjetas confirmadas → **cotas inferiores**, no Rpeak medidos. Σ GPU FP64 ≤ Rpeak por construcción.
- Acceso a fuentes degradado (solo snippets de buscador). Para cierre de dato, abrir manualmente las URLs de §(c).

---

## TABLA DE REFERENCIA DE ACELERADORES (FP64 / FP16-BF16 Tensor por tarjeta)

| Acelerador | FP64 (TF) | FP64 Tensor (TF) | FP16/BF16 Tensor dense (TF) | Variante/nota | Confianza |
|---|---|---|---|---|---|
| NVIDIA Tesla V100 | 7.8 | — | 125 (Tensor) | SXM2/PCIe 16/32GB | A |
| NVIDIA A100 | 9.7 | 19.5 | 312 | 40GB/80GB | A |
| NVIDIA H100 | 34 | 67 | ~990 | (no presente en Estonia) | A |
| NVIDIA H200 | 34 | 67 | ~990 dense (NVL ~835) | 141GB NVL en Rocket | A / M (NVL) |
| NVIDIA A40 | ~0.58 | — | ~150 | (no presente) | A |
| NVIDIA L40 / L40S | ~1.4 | — | ~362 (L40S) | TalTech usa "L40" 48GB | M |
| NVIDIA B200 | **~40 dense** (¿~90 c/Tensor? — EN DISPUTA) | — | ~2.250 dense | Blackwell; Tartu feb-2026 | **B** (FP64) |
| NVIDIA RTX Pro 6000 Blackwell | **~1.97** (1/64 de FP32) | — | ~? (orientada IA/gráficos) | Max-Q; Tartu feb-2026 | M |
| AMD Instinct MI250X | 47.9 (vector) / 95.7 (matrix) | — | 383 | LUMI (excluido) | A |

> Convención aplicada: para Σ GPU FP64 se usó la tasa **vector/no-Tensor** coherente (V100 7.8, A100 9.7, H200 34). FP16/BF16 con cifras Tensor **dense**. Reconciliación: Σ GPU FP64 (≈942 TF) es **cota inferior** y ≤ cualquier Rpeak total real (no publicado).

---

## FUENTES (índice de URLs)

- TOP500 Nov-2025: https://www.top500.org/lists/top500/2025/11/ · https://www.top500.org/lists/top500/2025/11/highs/ · https://www.top500.org/system/180048/ (LUMI)
- Statista nº supercomputadores por país: https://www.statista.com/statistics/264445/
- UTHPC Rocket: https://hpc.ut.ee/services/HPC-services/Rocket · https://hpc.ut.ee/services/HPC-services/Rocket-harware · https://portal.hpc.ut.ee/rocket-cluster
- UTHPC docs: https://docs.hpc.ut.ee/public/ · https://docs.hpc.ut.ee/public/cluster/Running_jobs/gpu_computing/ · https://docs.hpc.ut.ee/public/ETAIS/adding_rocket/
- UTHPC press/ampliaciones: https://ut.ee/en/content/high-performance-computing-centre-university-tartu-will-receive-more-capacity-amount-14 · https://etais.ee/en/etais-member-university-of-tartus-center-for-scientific-computing-ramps-up-ai-power-with-cutting-edge-gpus-to-secure-digital-future/ · https://www.innovationnewsnetwork.com/university-of-tartu-high-performance-computing-centre-building-fully-sovereign-ai-infrastructure/67352/
- TalTech: https://docs.hpc.taltech.ee/hardware.html · https://docs.hpc.taltech.ee/gpu.html · https://docs.hpc.taltech.ee/visualization.html · https://docs.hpc.taltech.ee/performance.html · https://taltech.ee/en/itcollege/hpc-centre
- NICPB/KBFI: https://docs.hep.kbfi.ee/about/ · https://docs.hep.kbfi.ee/compute/ · https://docs.hep.kbfi.ee/slurm/ · https://kbfi.ee/en/nicpb/research-programmes/high-energy-physics-and-theoretical-physics/
- ETAIS / EuroCC / LUMI: https://etais.ee/en/ · https://eurocc-estonia.ee/hpc-in-estonia/ · https://lumi-supercomputer.eu/lumi-consortium/ · https://lumi-supercomputer.eu/resource-allocation/ · https://en.wikipedia.org/wiki/LUMI
- Datasheets aceleradores: NVIDIA V100/A100/H100/H200/B200/RTX Pro 6000 (nvidia.com/resources.nvidia.com); AMD MI250X.

*Fin del informe — Estonia · generado 2026-06-16.*
