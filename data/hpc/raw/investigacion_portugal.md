# Investigación HPC — PORTUGAL (Indicador ILIA 2026)

**País:** Portugal · **Red:** Rede Nacional de Computação Avançada (RNCA / FCCN)
**Fecha de referencia:** estado operativo a **junio 2026**; rankings **TOP500 noviembre 2025**.
**Fecha de acceso a fuentes:** 2026-06-16 · **Idioma de trabajo:** español · **Fuentes:** PT/EN.
**Autor:** investigación automatizada (cascada de fuentes + triangulación).

> **Nota de método (limitación del entorno):** En este entorno la herramienta de *fetch* directo
> de URLs devolvió **HTTP 403** en todos los dominios (incluidos `top500.org`, `rnca.fccn.pt`,
> `fccn.pt`, Wikipedia). Toda la evidencia se obtuvo por **búsqueda web** que devuelve extractos
> citables de esas mismas páginas. Por eso, algunas cifras que SÍ son públicas en una página
> concreta (p. ej. el detalle exacto de cores/Rpeak en la ficha TOP500 del sistema) quedan
> marcadas para **abrir manualmente** la URL exacta y leer el valor verbatim. No se inventó ningún número.

---

## (a) Tabla por sistema / partición

Leyenda: Rmax/Rpeak en **TFLOP/s FP64**. "nº GPUs" = tarjetas aceleradoras físicas.
GPU FP64 / GPU FP16 = picos teóricos agregados desde datasheet (ver tabla de aceleradores).
Estado a jun-2026. "—" = no aplica · "n.p." = no publicado.

| Sistema / partición | Centro | Ciudad | Categoría | Estado (jun-2026) | Rank TOP500 Nov-25 | Rmax FP64 (TF) | Rpeak FP64 (TF) | CPU (modelo, sockets/cores) | Acelerador (modelo) | nº GPUs | GPU FP64 (TF) | GPU FP16/BF16 (TF) | Fuente(s) | Confianza |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Deucalion — TOTAL (3 particiones)** | MACC / EuroHPC | Guimarães | EuroHPC petascale (anfitrión PT) | **Operativo** | #297 (≈; ver nota) | ~3 870 (solo part. ARM)¹ | **~10 000** | A64FX + EPYC Rome 7742 | NVIDIA A100 | **132** | **1 280** (std) / 2 574 (TC) | **41 184** | TOP500 sys 180275; Wikipedia; RNCA; FCCN | Alta (Rpeak/GPU); Media (rank exacto) |
| Deucalion — partición ARM | MACC | Guimarães | CPU vectorial (sin GPU) | Operativo | #297 (entrada TOP500) | ~3 870 | **~5 000** | Fujitsu A64FX 48C @2 GHz × **1 632 nodos** (1 socket/nodo) | — (A64FX no es GPU) | 0 | — | — | TOP500 sys 180275; Wikipedia | Alta |
| Deucalion — partición x86 | MACC | Guimarães | CPU x86 | Operativo | (no listada aparte) | n.p. | **~2 300** | 2× AMD EPYC Rome **7742** 64C × **500 nodos** (BullSequana X440) | — | 0 | — | — | Wikipedia; RNCA | Alta |
| Deucalion — partición GPU | MACC | Guimarães | GPU (acelerada) | Operativo | (no listada aparte) | n.p. | **~2 700** | 2× AMD EPYC (Rome) × **33 nodos** (BullSequana E410) | **NVIDIA A100** (17 nodos×4 de 40 GB + 16 nodos×4 de 80 GB) | **132** | **1 280** (9,7) / 2 574 (19,5 TC) | **41 184** (312/GPU) | RNCA; Wikipedia; eurohpcsupport | Alta |
| **Navigator (+Navigator+)** | LCA-UC, Univ. Coimbra | Coimbra | HPC universitario (CPU+GPU) | **Operativo** | No figura | n.p. | **247,2** (86 + 161,2) | Intel Xeon E5-2697v2 12C / Xeon Gold 6148 20C / Xeon Gold 6154 18C — **~5 216 cores** | 8× NVIDIA Tesla **V100 16 GB** (cómputo) + 2× **A40 48 GB** (visualización) | **8** (+2 vis.) | **62,4** (8×7,8) | **1 000** (8×125 V100-TC) | uc.pt/lca; RNCA | Alta |
| **Vision** | HPC-UÉ, Univ. Évora | Évora | Clúster IA / deep learning (GPU) | **Operativo (en ampliación 2025)** | No figura | n.p. | **n.p.** (UÉ solo publica PFLOPS de IA) | 1× AMD EPYC Milan (head) + DGX: 2× EPYC 7742/DGX — **256 cores** | **NVIDIA A100 40 GB** (2× DGX A100, 8/cja) | **16** | **155,2** (16×9,7) ⟵ estimado, BAJA | **4 992** (16×312) | uevora.pt; sapo.pt; RNCA | Alta (HW); Baja (FP64) |
| **Bob** | MACC | Riba de Ave / Braga | HPC legado (solo CPU) | **RETIRADO (fuera de producción)** | No figura | n.p. | ~1 000 (histórico) | 2× Intel Xeon "Sandy Bridge" 8C @2,7 GHz × 600 nodos — 9 600 cores | — (sin GPU) | 0 | — | — | eurocc.fccn.pt; utaustinportugal | Alta |
| **Oblivion** | HPC-UÉ, Univ. Évora | Évora | HPC (CPU+GPU) | _pendiente subagente_ | No figura | _pend._ | _pend._ | _pend._ | _pend._ | _pend._ | _pend._ | _pend._ | RNCA; indico.hpc.uevora.pt | _pend._ |
| **Orion HPC** | HPC-UÉ, Univ. Évora | Évora | HPC (coprocesadores) | _pendiente subagente_ | No figura | _pend._ | _pend._ | _pend._ | _pend._ | _pend._ | _pend._ | _pend._ | RNCA | _pend._ |
| **Cirrus-A** | INCD, Lisboa | Lisboa | HPC heterogéneo | _pendiente subagente_ | No figura | _pend._ | _pend._ | _pend._ | _pend._ | _pend._ | _pend._ | _pend._ | wiki.incd.pt | _pend._ |
| **Stratus** | INCD, Lisboa | Lisboa | Cloud / VM (OpenStack) | _pendiente subagente_ | No figura | _pend._ | _pend._ | _pend._ | _pend._ | _pend._ | _pend._ | _pend._ | wiki.incd.pt | _pend._ |

¹ El Rmax 3,87 PF (HPL) corresponde a la **partición ARM**, que es la única entrada de Deucalion en la lista TOP500 (sistema 180275). El Rpeak total de las 3 particiones es ~10 PF.

---

## (b) Fuentes y citas (por sistema)

### Deucalion (MACC / EuroHPC, Guimarães) — OPERATIVO

- **Rpeak total ~10 PFLOPS:**
  - URL: https://en.wikipedia.org/wiki/Deucalion_(supercomputer)
  - Verbatim: *"a peak performance of 10 petaFLOPS"*; *"Deucalion achieves a peak of 10 PFLOPS"*.
  - Acceso: 2026-06-16 · Confianza: **alta** (corroborado por Fujitsu y FCCN).
- **Particiones (desglose Rpeak):**
  - URL: https://en.wikipedia.org/wiki/Deucalion_(supercomputer) ; https://rnca.fccn.pt/en/deucalion/
  - Verbatim: *"ARM Partition: 1,632 ... A64FX ... peaking at 5 PFLOPS"*; *"x86 Partition: 500 Atos Bull Sequana X440 nodes with AMD EPYC Rome 7742 ... peaking at 2.3 PFLOPS"*; *"GPU Partition: 33 Sequana E410 nodes with four Nvidia A100 GPUs each ... peaking at 2.7 PFLOPS"*.
  - Acceso: 2026-06-16 · Confianza: **alta** (5+2,3+2,7 = 10 PF, internamente consistente).
- **GPU: 132 A100 (split 40/80 GB):**
  - URL: https://rnca.fccn.pt/en/deucalion/ ; https://eurohpcsupport.eu/eurohpc-system/deucalion/
  - Verbatim: *"33 nodes equipped with 4 Nvidia A100 each"* (= 132); *"17 are equipped with NVIDIA A100 GPUs with 40GB of RAM, while the remaining 16 nodes have NVIDIA A100 GPUs with 80GB"* (17×4=68 de 40 GB + 16×4=64 de 80 GB = 132).
  - Acceso: 2026-06-16 · Confianza: **alta**. (Un solo extracto decía "80 GB per GPU" para todo; es error: la versión RNCA con split 40/80 es la dominante.)
- **Partición ARM = entrada TOP500 (sistema 180275):**
  - URL: https://top500.org/system/180275/
  - Verbatim (título de la ficha): *"Deucalion - PRIMEHPC FX700, Fujitsu A64FX 48C 2GHz, InfiniBand HDR100, Rocky Linux 8.5"*.
  - Acceso: 2026-06-16 · Confianza: **alta** (título); **valores exactos Rmax/Rpeak/cores → REVISIÓN MANUAL**, ver §(c).
- **Rmax 3,9 PF / debut TOP500 #219 (jun-2024) / Green500 #80:**
  - URL: https://www.fct.pt/en/... ; https://www.hpcwire.com/off-the-wire/eurohpc-supercomputers-maintain-prominence-with-3-in-top500s-top-10-and-deucalions-debut/
  - Verbatim: *"achieving 219th place with an HPL performance of 3.9 petaflops"*; *"ranked 81st in energy efficiency in the Arm partition and 219th in processing speed"*; *"delivering 79 percent computational efficiency on HPL"*.
  - Acceso: 2026-06-16 · Confianza: **alta** (debut); el 79% × 5 PF ≈ 3,9 PF ✓.
- **Rank actual #297:**
  - URL: https://en.wikipedia.org/wiki/Deucalion_(supercomputer)
  - Verbatim: *"ranked 297th in the TOP500 global list"*; *"As of October 2025, it's ranked 297th"*.
  - Acceso: 2026-06-16 · Confianza: **media** (un extracto intermedio citaba #259; el valor de la lista de **Nov-2025** debe confirmarse en TOP500, ver §c).
- **CPU x86 (EPYC Rome 7742 / 7H12) y constructor (Fujitsu PRIMEHPC + Atos BullSequana):**
  - URL: https://www.techzine.eu/news/analytics/55906/fujitsu-to-build-10-petaflop-supercomputer-in-portugal/ ; Wikipedia
  - Verbatim: *"combining a Fujitsu PRIMEHPC (ARM partition) and Atos Bull Sequana (x86 partitions)"*; *"AMD EPYC Rome 7742"*. (Otra fuente menciona "EPYC Rome 7H12" en nodos estándar y EPYC Rome en nodos large-memory — ver Nota de calidad.)
  - Acceso: 2026-06-16 · Confianza: **alta** (Rome 7742 es el modelo citado por RNCA/Wikipedia).
- **Coste y almacenamiento (contexto):**
  - URL: Wikipedia · Verbatim: *"11.1 petabytes of storage and cost €20 million"*. Confianza: alta.

### Navigator / Navigator+ (LCA-UC, Coimbra) — OPERATIVO

- **CPU (3 familias) y cores totales:**
  - URL: https://www.uc.pt/lca/ClusterResources/Navigator/description ; https://rnca.fccn.pt/en/lca-uc/
  - Verbatim: *"164 computing nodes (Fujitsu PRIMERGY CX400 S2) with 2 x Intel Xeon E5-2697v2 (12-core) @ 2.70 GHz"*; *"28 computing nodes ... 2 x Intel Xeon Gold 6148 (20-core) @ 2.40 GHz"*; *"1 SMP computing node ... 4 x Intel Xeon Gold 6154 (18-core) @ 3.00 GHz and 3TB"*; *"total of 3936 + 1280 cores"* (= 5 216).
  - Acceso: 2026-06-16 · Confianza: **alta**.
- **GPUs: 8× V100 16 GB + 2× A40 48 GB:**
  - URL: https://www.uc.pt/lca/ClusterResources/Navigator/description ; https://www.uc.pt/lca/computing-resources/navigator-cluster/
  - Verbatim: *"4 GPU computing nodes (Fujitsu PRIMERGY CX2570 M4) with 2 x NVIDIA Tesla V100 16 GB each"* (= 8); *"1 visualization node (Lenovo SR650 V2) equipped with 2 x NVIDIA A40 48GB PCIe GPUs"*.
  - Acceso: 2026-06-16 · Confianza: **alta**. (Corrección: la marca "Tesla A40" que aparece en algún extracto genérico es errónea; la fuente oficial dice "NVIDIA A40 48GB PCIe".)
- **Rpeak 86 + 161,2 = 247,2 TFLOP/s:**
  - URL: https://www.uc.pt/lca (info general) ; corrobora RNCA/ACP2030 con "85 TFlop/s ... total ... 250 TFlop/s" (planificado).
  - Verbatim: *"maximum processing capacity of 86 + 161.2 TFlops"*.
  - Acceso: 2026-06-16 · Confianza: **alta**.
- **Rmax:** no publicado (Navigator no figura en TOP500). Confianza: n/a.

### Vision (HPC-UÉ, Évora) — OPERATIVO (ampliación en curso 2025)

- **2× DGX A100 = 16 A100 40 GB; head AMD EPYC Milan; 256 cores; 2 TB RAM; HDR 200 Gb/s:**
  - URL: https://www.uevora.pt/ue-media/noticias?item=31200 ; https://sapo.pt/artigo/universidade-de-evora-lanca-concurso-publico-... ; https://rnca.fccn.pt/en/hpc-ue/
  - Verbatim: *"a total of 16 NVIDIA A100 GPUs, 2 TB of RAM and 256 CPU cores"*; *"640GB of GPU memory"* (640/16 = 40 GB/GPU → A100 **40 GB**); *"a main node with an AMD EPYC Milan processor, two NVIDIA DGX A100 nodes, a 200 Gb/s HDR network"*.
  - Acceso: 2026-06-16 · Confianza: **alta** (HW). Versión 40 GB: alta (inferida de 640 GB total).
- **Rendimiento de IA "2×5 PFLOPS" (FP16/TF32 con sparsity, NO FP64):**
  - URL: https://www.uevora.pt/ue-media/noticias?item=31200
  - Verbatim: *"global capacity of 2x5 petaflops, 16 GPUs A100, 640GB ... 2 TB of RAM"*.
  - Acceso: 2026-06-16 · Confianza: **alta** (cifra de IA); la UÉ **no publica Rpeak FP64**.
- **Ampliación 2025 (concurso 141/DCP-GCE/UE/2025):**
  - URL: https://sapo.pt/artigo/universidade-de-evora-lanca-concurso-publico-...
  - Verbatim: *"including eight GPGPUs, 2 TB of RAM, and minimum performance capacity of 32 petaFLOPS FP8"*.
  - Acceso: 2026-06-16 · Confianza: **alta**. Nota: 32 PFLOPS es **FP8**, no FP64.
- **GPU FP64 (≈155 TFLOP/s):** estimación propia 16×9,7 desde datasheet NVIDIA A100; **no es cifra de la UÉ**. Confianza: **baja**.

### Bob (MACC) — RETIRADO

- **Estado retirado / colas cerradas:**
  - URL: https://eurocc.fccn.pt/en/supercomputer-bob-successfully-completes-multiple-national-and-international-research-projects/
  - Verbatim: *"the queues have now been closed at MACC, marking the end of its productive tenure"*; *"the MACC team is currently working on newer resources"*.
  - Acceso: 2026-06-16 · Confianza: **alta**.
- **Desmantelamiento parcial 2023 + concurso de reaprovechamiento:**
  - URL: https://tek.sapo.pt/noticias/ciencia/artigos/fct-esta-a-procura-das-melhores-ideias-para-reaproveitar-o-equipamento-do-supercomputador-bob ; https://pt.wikipedia.org/wiki/Deucalion_(supercomputador)
  - Verbatim: *"Em fevereiro de 2023, 15 dos 20 bastidores de compute nodes do supercomputador BOB foram desativados"*; FCT abrió concurso de reaprovechamiento con plazo 31-jul-2023.
  - Acceso: 2026-06-16 · Confianza: **alta**.
- **Specs históricas (600 nodos, 9 600 cores Sandy Bridge, ~1 PFLOP, sin GPU; ex-Stampede 1 de TACC):**
  - URL: https://utaustinportugal.org/bob-is-the-new-supercomputer-in-portugal/ ; https://www.macc.fccn.pt/resources
  - Verbatim: *"600 compute nodes ... 9600 cores"*; *"two Intel 8-core 'Sandy Bridge' generation Xeon processors at 2.7Ghz with 32GB of RAM"*; *"1 petaFLOP of compute performance"*; *"gifted to MACC by the Texas Advanced Computing Center (TACC)"*.
  - Acceso: 2026-06-16 · Confianza: **alta** (specs); **sin GPU**: alta por ausencia consistente.

### Oblivion / Orion (HPC-UÉ, Évora) y Cirrus-A / Stratus (INCD, Lisboa)
_Pendiente de cierre de subagentes — ver §(c) Revisión manual y se completará al recibir resultados._

---

## (c) REVISIÓN MANUAL (sistemas o cifras sin specs públicas confirmadas)

| Sistema / dato | Qué falta | Página/PDF exacto a abrir |
|---|---|---|
| **Deucalion — partición ARM (TOP500)** | Valores exactos verbatim de **Rmax, Rpeak y nº de cores** de la ficha (el fetch dio 403) | https://top500.org/system/180275/ |
| **Deucalion — rank Nov-2025** | Confirmar rank exacto de la lista de **noviembre 2025** (extractos dan #297 "oct-2025"; otro #259) | https://www.top500.org/lists/top500/list/2025/11/ (buscar "Deucalion"); https://top500.org/system/180275/ |
| **Deucalion — Rmax x86/GPU** | Rmax HPL de las particiones x86 y GPU (solo se publica Rpeak por partición) | https://rnca.fccn.pt/en/deucalion/ ; https://docs.macc.fccn.pt/ |
| **Vision — Rpeak FP64** | La UÉ solo publica PFLOPS de IA; falta un Rpeak FP64 oficial | https://rnca.fccn.pt/en/hpc-ue/ ; https://www.uevora.pt/ue-media/noticias?item=31200 |
| **Oblivion** | Specs completas (nodos, CPU, nº/modelo GPU, Rpeak) — un extracto da "239 petaFLOPS" (casi seguro error por "239 TFLOPS") | https://rnca.fccn.pt/en/hpc-ue/ ; https://indico.hpc.uevora.pt/event/86/ ; https://hpc-portal.eu/node/1298 |
| **Orion HPC** | Sin specs públicas ("software acceleration with coprocessors") | https://rnca.fccn.pt/en/hpc-ue/ ; https://www.fccn.pt/en/noticias/rnca-conheca-os-supercomputadores-nacionais/ |
| **Cirrus-A** | nº total de nodos, cores y nº/modelo de GPU (T4) tras ampliación 2022; Rpeak | https://wiki.incd.pt/books/compute-node-specs-and-information/page/incd-lisbon-(cirrusaincdpt) ; https://www.incd.pt/pages/files/organization/INCD-Relatorio-de-Actividades-2023.pdf |
| **Stratus** | Confirmar que es cloud/VM (sin Rpeak HPC); GPUs si las hubiera | https://wiki.incd.pt/books/architecture-and-technical-information/page/stratus-technical-overview |

---

## (d) Totales país — COTA INFERIOR (solo lo confirmado y operativo)

> Se contabilizan **solo sistemas operativos a jun-2026 con cifra confirmada**. Bob queda **fuera**
> (retirado). Oblivion/Orion/Cirrus-A/Stratus **pendientes** (no suman aún → la cota subirá).

**Entran (operativos, con dato):** Deucalion (3 particiones), Navigator, Vision.
**Salen:** Bob (retirado); A40 de Navigator (visualización, FP64 despreciable); A64FX (CPU, no es GPU).
**Pendientes (subirán la cota):** Oblivion, Orion, Cirrus-A, Stratus.

| Métrica | Cota inferior (confirmado) | Composición |
|---|---|---|
| **Σ Rpeak FP64 (TF)** | **≈ 10 247** | Deucalion 10 000 + Navigator 247,2 (Vision FP64 no publicado → no suma) |
| **Σ nº GPUs** | **156** | Deucalion 132 (A100) + Navigator 8 (V100) + Vision 16 (A100) |
| **Σ GPU FP64 (TF) — tasa estándar** | **≈ 1 498** | Deucalion 1 280,4 + Navigator 62,4 + Vision 155,2 |
| **Σ GPU FP64 (TF) — FP64 Tensor Core** | **≈ 2 791** | Deucalion 2 574 + Navigator 62,4 (V100 sin FP64-TC) + Vision 312 (16×19,5) |
| **Σ GPU FP16/BF16 Tensor (TF)** | **≈ 47 176** | Deucalion 41 184 + Navigator 1 000 + Vision 4 992 |

**Reconciliación Σ GPU FP64 ≤ Rpeak (partición GPU de Deucalion):** 132×19,5 = 2 574 TF (FP64-TC) ≈
los 2 700 TF de Rpeak de la partición GPU (la diferencia ~126 TF es la contribución FP64 de las CPU EPYC del nodo). ✓ Coherente.

---

## (e) Notas de calidad

1. **Concentración extrema.** **Deucalion concentra ≈97,6 %** del Rpeak FP64 confirmado del país
   (10 000 / 10 247 TF) y **el 84,6 % de las GPUs** (132/156). El indicador HPC de Portugal está
   dominado por un único sistema EuroHPC.
2. **Salvedad EuroHPC / anfitrión.** Deucalion es un sistema **EuroHPC JU** (cofinanciado UE + FCT);
   Portugal es **país anfitrión**, pero la capacidad NO es 100 % nacional (cuotas de acceso UE).
   Decidir si se computa íntegro o prorrateado por la cuota nacional.
3. **AI Factory.** No hay una "AI Factory" portuguesa autónoma; Portugal participa vía la
   **BSC AI Factory** (consorcio España/Portugal/Türkiye/Romania; FCT representa a PT).
   Fuente: https://www.eurohpc-ju.europa.eu/eurohpc-ju-selects-ai-factory-antennas-broaden-ai-factories-initiative-2025-10-13_en (acceso 2026-06-16).
4. **TOP500 lista solo la partición ARM de Deucalion** (sistema 180275). El Rpeak total de 10 PF
   es de fuentes de fabricante/centro; el Rmax 3,9 PF (HPL) es solo de la partición ARM.
5. **Métricas de IA ≠ FP64.** En Vision, "2×5 PFLOPS" y "32 PFLOPS" (ampliación) son **FP16/TF32/FP8
   con sparsity**, no doble precisión. No mezclar con Rpeak FP64.
6. **A64FX no cuenta como GPU.** Las 1 632 CPU A64FX de Deucalion son CPU vectoriales (~3,4 TFLOP/s
   FP64 c/u); contribuyen al Rpeak total pero **no** a "nº de GPUs" ni a "capacidad GPU".
7. **Conflicto menor de CPU x86 Deucalion.** Modelo citado mayoritariamente EPYC Rome **7742** (64C);
   un extracto menciona **7H12** en nodos estándar + EPYC Rome en nodos large-memory. No afecta a GPU.
8. **Bob fuera.** Retirado (colas cerradas, desmantelado parcialmente feb-2023). Si se exige
   "operativo a jun-2026", Bob no entra.

---

## Tabla de referencia de aceleradores usada (FP64 TFLOP/s por tarjeta; verificada contra datasheet)

| Acelerador | FP64 (TF) | FP64 Tensor Core (TF) | FP16/BF16 Tensor (TF) | Fuente datasheet |
|---|---|---|---|---|
| NVIDIA V100 (16 GB, SXM2) | 7,8 | — (sin FP64-TC) | 125 (FP16 Tensor) | NVIDIA V100 datasheet |
| NVIDIA A100 (40/80 GB) | **9,7** | **19,5** | **312** (624 c/ sparsity) | https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/a100/pdf/nvidia-a100-datasheet.pdf — *"FP64 9.7 TFLOPS, FP64 Tensor Core 19.5 TFLOPS ... BFLOAT16 312 TFLOPS"* (acceso 2026-06-16) |
| NVIDIA A40 (48 GB) | ~0,58 (despreciable HPC) | — | 149,7 (FP16 Tensor) | NVIDIA A40 datasheet (GPU de visualización) |
| NVIDIA T4 (16 GB) | ~0,25 (inferencia) | — | 65 (FP16 Tensor) | NVIDIA T4 datasheet |
| Fujitsu A64FX (48C) | ~3,4 **por CPU** | — | — | **CPU vectorial, NO GPU** |

> Convención aplicada: Rpeak total = el oficial (TOP500/centro). GPU FP64 = tasa NVIDIA datacenter;
> se reportan **ambas** (estándar 9,7 y FP64 Tensor-Core 19,5) para A100. Se cuentan tarjetas físicas.
