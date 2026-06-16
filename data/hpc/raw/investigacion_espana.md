# Investigación HPC — ESPAÑA (estado jun-2026; TOP500 nov-2025)

> **NOTA DE PROCESO:** corrida interrumpida por límite de sesión. Recoge nodos RES ya
> investigados con dato sólido y deja PENDIENTE el resto. Webs RES/TOP500/centros dan
> HTTP 403 a fetch automático → datos de TOP500 + prensa + snippets, confianza marcada.

> **⚠️ CORRECCIÓN DE INVENTARIO:** "**Correfoc**" (fila 17 de la planilla, atribuido a UPF)
> **NO existe** como HPC. La búsqueda exhaustiva confirma que "correfoc" es solo la fiesta
> del fuego catalana. El HPC real de la UPF se llama **Marvin / Marvin II** (modesto,
> GPU NVIDIA Quadro RTX 4000, NO es nodo RES, NO en TOP500). El nodo RES catalán es
> **Pirineus III (CSUC)**, ya en la lista. → **Quitar "Correfoc" del censo** o sustituir
> por "Marvin (UPF)" como nodo no-RES. Esto baja el conteo España de 17 a 16 nodos RES.

## Tabla por sistema/partición (investigados)

| sistema | centro | estado jun-26 | TOP500 nov-25 | Rmax FP64 (TF) | Rpeak FP64 (TF) | CPU | acelerador | nº GPUs | GPU FP64 (TF) | GPU FP16 (TF) | conf. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **MareNostrum 5 ACC** | BSC/EuroHPC | Operativo | **#14** | **175.300** | ~314.000 (verificar) | Intel Sapphire Rapids | NVIDIA H100 64GB | ~4.480 (verificar) | ~150.080 (TC 4.480×?) ⚠ | ~ (verificar) | media |
| **MareNostrum 5 GPP** | BSC/EuroHPC | Operativo | **#50** | **40.100** | ~45.000 (verificar) | Intel Sapphire Rapids | — (solo CPU) | 0 | 0 | 0 | media |
| Caléndula | SCAYLE, León | Operativo | no | n/d | ~7.000 nominal (precisión n/d) | 200×2 Xeon 8462Y (12.800c) + 35×2 EPYC 9374F (2.240c) | NVIDIA H100 SXM5 80GB | **140** (35×4) | ~4.760 (vector) / ~9.380 (TC) | ~138.600 (TC) | media-alta |
| Picasso | UMA/SCBI, Málaga | Operativo | no | n/d | **>2.000** (FP64 oficial) | Xeon Gold 6230R + EPYC 7H12/9754/7742 | NVIDIA A100 | **32** (4 DGX×8) | ~310 (vector) / ~624 (TC) | ~9.984 (dense) | alta |
| FinisTerrae III | CESGA, Santiago | Operativo | no (prob.) | ~1.968 (sin confirmar HPL) | **4.360** | 708× Intel Xeon Ice Lake 8352Y (22.656c) | NVIDIA A100 + T4 | **128 A100 + 16 T4** | A100 ~1.242 (v)/~2.496 (TC) | A100 ~39.936 | alta |
| Agustina (Caesaraugusta IV) | BIFI/Unizar | Operativo | no | n/d | **511** (solo CPU) | 192× AMD EPYC 7513 (6.144c) | NVIDIA H100 + L40S | **12 H100 + 36 L40S** | H100 ~408(v)/~804(TC); L40S ~50 | H100 ~11.880 | alta |
| Altamira | IFCA/UC, Santander | Operativo (renovando) | no | ~74 (2012) | **>50** | Intel Xeon E5-2670 (Sandy Bridge) | NVIDIA Tesla M2090 | **10** (5×2) | ~6,65 (0,665×10) | N/A (sin Tensor) | media |
| Pirineus III | CSUC, Barcelona | Operativo (oct-2024) | no | n/d | **>2.000** | ~15.000 cores | (GPU por verificar) | verificar | verificar | verificar | media |

### Notas de cómputo / decisiones
- **MareNostrum 5 es EL sistema dominante de España** (ACC #14, Rmax 175,3 PF). **PRIORIDAD máxima** para 2ª corrida: confirmar **Rpeak ACC** y **nº exacto de H100** (clave para var.1, var.2 y var.3 y para verificar la afirmación "MN5 ≈ 95% de la capacidad FP64 nacional"). Cifras de Rpeak/GPU arriba son **estimaciones a verificar**.
- Ningún nodo RES salvo MN5 (y FinisTerrae) está en TOP500; sus capacidades vienen de fichas de centro (snippets) → cota inferior.
- **Caléndula "7.000 TF"** es cifra nominal de prensa, precisión no especificada (probable agregado CPU+GPU mixto), NO un Rpeak FP64 medido.
- **Agustina/Picasso/FinisTerrae**: el Rpeak oficial publicado es parcial (solo CPU en Agustina; ">2 PF" en Picasso). GPU FP64/FP16 son cálculo propio con `ref_aceleradores.csv`, no cifras de centro.

## Fuentes y citas (clave)
- **MN5 ACC/GPP** — *"ACC partition ranked 14th globally with 175.3 petaFLOPS Rmax, while the GPP ranked 50th with 40.1 petaFLOPS Rmax"* (TOP500 nov-2025 vía snippet); https://www.top500.org/lists/top500/2025/11/ , https://en.wikipedia.org/wiki/MareNostrum (2026-06-16, media)
- **Caléndula** — SCAYLE: *"200 servidores con 2 Intel Xeon Platinum 8462Y… 12800 cores… 35 servidores con 2 AMD EPYC 9374F… 4 tarjetas GPU NVIDIA H100 SXM5 80G… 140 tarjetas GPUs H100"*; https://www.scayle.es/manual/es/hpc/infraestructura . Prensa: *"7000 teraflops… el segundo más potente de España"* (2026-06-16, media-alta)
- **Picasso** — SCBI: *"more than 30K compute cores, 150 TB main memory, 32 NVIDIA A100 GPUs… peak performance over 2 PFlops (FP64) and 20 PFlops (AI in GPUs)"*; https://www.scbi.uma.es/web/supercomputing/ ; nodos: https://github.com/SCBI-Picasso/Picasso-Documentation (2026-06-16, alta)
- **FinisTerrae III** — Atos/HPCwire: *"4 PetaFLOPS… 354 nodes… Intel Xeon Ice Lake 8352Y 32 cores… 144 GPU accelerators: Nvidia A100 and Nvidia T4… 118 TB"*; CESGA: *"4,36 PetaFLOPS… 22,656 Intel Xeon Ice Lake 8352Y cores, 128 Nvidia A100 and 16 Nvidia T4"*; https://www.cesga.es/en/infrastructures/computing/ , https://www.hpcwire.com/off-the-wire/atos-multiplies-supercomputing-capacity-by-12-at-cesga-in-spain-with-new-finisterrae-iii/ . **OJO:** constructor = **Atos/Bull (Eviden)**, no HPE. (2026-06-16, alta)
- **Agustina** — CESAR-Unizar: *"6144 cores… 192 AMD EPYC 7513… 12 NVIDIA H100 GPUs (80GB)… 36 NVIDIA L40S GPUs… Rpeak 511 TFLOPS"*; https://cesar.unizar.es/hpc/ , https://bifi.es/ (2026-06-16, alta)
- **Altamira** — RES/IFCA: *"163 IBM iDataPlex nodes… Xeon E5-2670… five nodes with Tesla M2090 GPUs… exceeds 50 Tflops/s"*; M2090 FP64 0,665 TF/tarjeta; https://confluence.ifca.es/display/IC/Altamira+Users+Guide (2026-06-16, media)
- **Pirineus III** — CSUC: *"Pirineus III… operation in October 2024… more than 2 Pflop/s and 15,000 cores… fourth supercomputer in the RES"*; https://www.csuc.cat/en/serveis/supercomputadors (2026-06-16, media)
- **Correfoc (no existe)** — https://en.wikipedia.org/wiki/Correfoc (fiesta); UPF real: Marvin/Marvin II https://www.upf.edu/web/sct-sit/hpc (2026-06-16, alta)

## PENDIENTE de investigar (límite de sesión) — 2ª CORRIDA
- **MareNostrum 5**: confirmar Rpeak ACC + nº exacto H100 + (NGT/MN5-NG si existe). **PRIORIDAD 1.**
- Nodos RES sin dato: **Tirant III** (UV), **LaPalma** (IAC), **Lusitania III** (COMPUTAEX), **Cibeles** (UAM), **Urederra** (NASERTIC), **Xula** y **Turgalium** (CIEMAT), **Magerit** (UPM), **TALA IA / BSAI** (UIB). Confirmar GPU de **Pirineus III** (CSUC).
- Posible **AI Factory del BSC** (EuroHPC) — verificar si añade sistema.

## Revisión manual (URLs 403 a fetch; abrir en navegador)
- https://www.res.es/es/sobre-la-res/nodos (fichas oficiales de TODOS los nodos)
- https://www.top500.org/lists/top500/list/2025/11/ → filtrar Spain (confirmar que solo MN5 ACC+GPP están; ¿FinisTerrae?)
- https://www.bsc.es/marenostrum/marenostrum-5 (Rpeak ACC + nº H100)
