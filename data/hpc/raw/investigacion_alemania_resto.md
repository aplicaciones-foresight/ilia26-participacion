# Investigación HPC — ALEMANIA (resto de sistemas grandes; estado jun-2026; TOP500 nov-2025)

> **ALCANCE:** completa los sistemas grandes que faltaban tras `investigacion_alemania.md`.
> **JUPITER (Booster/Cluster), HammerHAI, JAIF/JARVIS YA están en ese archivo y NO se repiten aquí.**
> Prioridad por capacidad: GCS Tier-0/1 + NHR Tier-2 con GPU + Investigación con GPU.
> El **Tier-3 universitario** NO se investiga: solo se lista para REVISIÓN MANUAL (sección c).
>
> **NOTA DE PROCESO/FUENTES:** top500.org, fz-juelich.de, lrz.de, hlrs.de, etc. devuelven HTTP 403
> a fetch automático → datos vía **WebSearch** (extractos citables) + prensa de fabricante/centro.
> Confianza marcada por dato. Convención de aceleradores y FP64 según `data/hpc/ref_aceleradores.csv`
> y el brief: **FP64 vector** como principal (cota inferior); 1 GH200 = 1 GPU; 1 MI300A = 1 acelerador (APU).
> Σ(GPU FP64 vector) reconciliada para ser ≤ Rpeak del sistema.

---

## (a) Tabla por sistema

| sistema | centro | tier | estado jun-26 | rank TOP500 nov-25 | Rmax FP64 (TF) | Rpeak FP64 (TF) | CPU | acelerador | nº GPUs | GPU FP64 vector (TF) | GPU FP16/BF16 (TF) | fuente | conf. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **JUWELS Booster** | JSC (GCS) | Tier-0/1 | **Operativo** (superado por JUPITER) | **en lista, rank bajo (no publicado exacto; ~30-40s)** | **44.120** | **70.980** | AMD EPYC 7402 (Rome) | NVIDIA A100 SXM 40GB | **3.744** (936×4) | ~36.317 (3.744×9.7) | ~1.168.128 (3.744×312) | TOP500 sys/179894; JSC docs; arXiv 2108.11976 | alta |
| **JUWELS Cluster (Módulo 1)** | JSC (GCS) | Tier-0/1 | **Operativo** | no (Rmax ~6.2 PF histórico) | ~6.200 | ~12.000 (≈9.9 en entrada TOP500) | Intel Xeon Platinum 8168 (Skylake) | NVIDIA V100 (48 nodos×4) + 4×P100 vis. | 192 V100 + 4 P100 | V100 ~1.498 (192×7.8) | V100 ~24.000 (192×125) | Gauss/JSC; JLSRF 171; TOP500 sys/179424 | media-alta |
| **JEDI** (JUPITER Exascale Dev. Instrument) | JSC (GCS/EuroHPC) | Tier-0 (dev) | **Operativo** (fue #1 Green500 jun-2024) | sí (rank exacto no publicado; sistema pequeño) | **~4.500** (HPL) | ~5.500–6.000 (no publicado exacto) | NVIDIA Grace (Arm) | NVIDIA GH200 | **48** (24+24 nodos, 1 GH200/nodo) | ~1.632 (48×34) | ~47.472 (48×989) | fz-juelich PR 2024; TNW; JEDI docs | alta (nº GPU) / media (Rpeak) |
| **JURECA-DC** (módulo GPU) | JSC (GCS) | Tier-0/1 | **Operativo** | no (probable; ~18.5 PF histórico fuera del top) | ~15.000–18.000 (no publicado exacto) | **~18.500** (módulo DC GPU) | AMD EPYC 7742 (Rome) | NVIDIA A100 SXM 40GB | **768** (192 nodos×4) | ~7.450 (768×9.7) | ~239.616 (768×312) | fz-juelich PR 2021; HPCwire; DCD | alta (nº GPU) / media (Rpeak) |
| **JUSUF** | JSC (GCS) | Tier-2 | **Operativo** | no | n/d | n/d (multi-PF) | AMD EPYC Rome 64C (×2) | NVIDIA V100-16G (61 nodos×1) | **61 V100** | ~476 (61×7.8) | ~7.625 (61×125) | fz-juelich JUSUF; JLSRF | media |
| **SuperMUC-NG Fase 1** | LRZ (GCS) | Tier-0/1 | **Operativo** | sí (rank bajo; ~19.5 PF Rmax) | **~19.476** | **~26.900** | Intel Xeon Platinum 8174 (Skylake) | — (solo CPU) | 0 | 0 | 0 | LRZ docs; Wikipedia SuperMUC; TOP500 sys/179566 | alta |
| **SuperMUC-NG Fase 2** | LRZ (GCS) | Tier-0/1 | **Operativo** | sí (rank bajo; era #52 en nov-2023) | **~17.190** | ~24.000–26.000 (verificar) | Intel Xeon Platinum 8480 (Sapphire Rapids) | **Intel Data Center GPU Max 1550 (Ponte Vecchio)** | **960** (240 nodos×4) | ~24.960 (960×26) ⚠ ver nota | n/d (sin TC FP16 estándar) | TOP500 sys/180182; LRZ; HPCwire | alta (nº GPU) / media (Rpeak) |
| **Hunter** | HLRS (GCS) | Tier-0/1 | **Operativo** (desde ene-2025) | **#12** (Green500 #12) | **~38.000** (HPL, verificar dígitos) | **48.100** | AMD EPYC 4ª gen 24C (en APU) | **AMD Instinct MI300A (APU)** | **752 APU** (188 nodos×4) | **~46.098** (752×61.3) | ~737.411 (752×980.6) | TOP500 sys/180391; HLRS; heise; AMD | alta |
| **Hawk** (sistema base) | HLRS (GCS) | Tier-0/1 | **RETIRADO** (abr-2025) | no | ~19.300 (histórico) | ~26.000 (histórico) | AMD EPYC 7742 (Rome) | — (solo CPU) | 0 | 0 | 0 | HLRS; nextplatform; DCD | alta |
| **Hawk AI Expansion** | HLRS (GCS) | Tier-0/1 | **Operativo** (sobrevive a Hawk base) | no | n/d | n/d (24 nodos GPU) | AMD EPYC Rome (host) | NVIDIA A100 | **192** (24 nodos×8) | ~1.862 (192×9.7) | ~59.904 (192×312) | HLRS news; NVIDIA blog; siliconangle | alta (nº GPU) |
| **Vulcan** | HLRS (GCS) | Tier-2/3 | **Operativo** (sistema de propósito general/pre-proc.) | no | n/d | n/d (no publicado) | mixto (NEC/Intel/AMD legado) | NVIDIA (parcial, varias gen.) | no publicado | no publicado | no publicado | HLRS systems | baja → REVISIÓN MANUAL |
| **Capella** | TU Dresden (NHR) | Tier-2 | **Operativo** | **#51** (Green500 #5) | n/d (HPL exacto no publicado; <38) | **>38.000** (peak FP64) | AMD EPYC 32C (×2) | NVIDIA H100 SXM 94GB | **624** (144 nodos×4) | ~21.216 (624×34) | ~617.136 (624×989) | TU Dresden PR; Silicon Saxony; Megware | alta |
| **Alex** | FAU Erlangen (NHR) | Tier-2 | **Operativo** | sí (histórico; rank bajo) | n/d (no publicado exacto) | ~5.000–6.000 (mixto A100+A40) | AMD EPYC 7713 (Milan) | NVIDIA A100 (256) + A40 (304) | **256 A100 + 304 A40 = 560** | A100 ~2.483 (256×9.7) + A40 ~176 (304×0.58) = ~2.659 | A100 ~79.872 + A40 ~45.296 = ~125.168 | NHR@FAU docs; Megware; HPCwire | alta (nº GPU) |
| **Helma** | FAU Erlangen (NHR) | Tier-2 | **Operativo** (inaugurado oct-2025) | sí (era #51 jun-2025; rank bajó nov-25, no publicado) | **~32.220** (HPL, jun-2025) | ~40.000–50.000 (verificar) | (host AMD/Intel) | **NVIDIA H100 + H200** (mitad y mitad) | **768** (~384 H100 + ~384 H200) | ~26.112 (768×34) | ~759.552 (768×989) | NHR@FAU PR; FAU news; Megware | alta (nº GPU) / media (Rpeak) |
| **Grete** (partición GPU de Emmy) | GWDG Göttingen (NHR) | Tier-2 | **Operativo** | sí (histórico Green500; rank bajo) | n/d (no publicado exacto) | ~8.000–10.000 (estimado) | AMD EPYC 7513 / 7662 | NVIDIA A100 (40/80GB) — algunas H100 en ampliaciones | **~556** (≈139 nodos×4) — verificar | ~5.393 (556×9.7) aprox. | ~173.472 (556×312) aprox. | GWDG Grete; idw-online | media |
| **HoreKa** | KIT (NHR) | Tier-2 | **Operativo** (multi-partición GPU) | sí (histórico; rank bajo) | ~8.000 (HoreKa-Green HPL) | **~17.000** (sistema combinado CPU+GPU) | Intel Xeon Ice Lake 8358 | NVIDIA A100 (Green) + H100 (Teal) + H200 (Ruby) | **668 A100** + H100/H200 (nº no publicado) | A100 ~6.480 (668×9.7) + (H100/H200 sin nº) | A100 ~208.416 (668×312) | NHR@KIT userdocs; HPCwire; DCD | media-alta (A100) / baja (H100/H200 nº) |
| **Lise** (NHR@ZIB) | ZIB Berlín (NHR) | Tier-2 | **Operativo** | no (CPU+GPU mixto; ~9 PF) | n/d | **~9.000** (pico total CPU+GPU) | Intel Xeon Sapphire Rapids (GPU) + CLX (CPU) | NVIDIA A100 80GB (168) + **Intel GPU Max 1550 PVC (32)** | **168 A100 + 32 PVC = 200** | A100 ~1.630 (168×9.7) + PVC ~832 (32×26) = ~2.462 | A100 ~52.416 + PVC n/d | NHR@ZIB wiki; Lenovo | alta (nº GPU) |
| **Noctua 2** | Paderborn PC2 (NHR) | Tier-2 | **Operativo** | sí (histórico #121 jun-2022; rank bajo) | n/d (no publicado exacto) | ~5.400 (CPU+GPU; verificar) | AMD EPYC 7763 (Milan) | NVIDIA A100 (32 nodos×4) | **128 A100** | ~1.242 (128×9.7) | ~39.936 (128×312) | TOP500 sys/180071; PC2; JLSRF | alta (nº GPU) |
| **Otus** (NUEVO) | Paderborn PC2 (NHR) | Tier-2 | **Operativo** (nov-2025) | verificar (entró 2025) | no publicado | no publicado | (verificar) | (GPU AMD/NVIDIA — verificar) | no publicado | no publicado | no publicado | HPCwire 2025-11-11 | baja → REVISIÓN MANUAL |
| **CLAIX-2023** (segmento GPU) | RWTH Aachen (NHR) | Tier-2 | **Operativo** | sí (histórico; rank bajo) | n/d (no publicado exacto) | **>14.000** (segmento ML/GPU) | Intel Xeon Platinum 8468 (Sapphire Rapids) | NVIDIA H100 | **204** (51 nodos×4) | ~6.936 (204×34) | ~201.756 (204×989) | TOP500 sys/180295; RWTH blog | alta (nº GPU) |
| **CLAIX-2025** | RWTH Aachen (NHR) | Tier-2 | **PREVISTO** (no en producción jun-26) | no | no publicado | no publicado | (verificar) | NVIDIA H100/H200 (verificar) | no publicado | no publicado | no publicado | RWTH blog | baja → REVISIÓN MANUAL |
| **Raven** (partición GPU) | MPCDF Garching (Max Planck) | Investigación | **Operativo** | sí (histórico #47 jun-2021; rank bajo) | n/d (no publicado exacto) | **~16.000** (FP64, GPU + CPU host, incl. TC) | Intel Xeon Ice Lake | NVIDIA A100 SXM 40GB | **768** (192 nodos×4) | ~7.450 (768×9.7) | ~239.616 (768×312) | MPCDF Raven; docs.mpcdf | alta |
| **Viper-GPU** | MPCDF Garching (Max Planck) | Investigación | **Operativo** (2024/2025) | verificar (puede estar en TOP500) | n/d (no publicado exacto) | **~36.780** (600×61.3 FP64 vector) | AMD EPYC Genoa (en APU) | **AMD Instinct MI300A (APU)** | **600 APU** (300 nodos×2) | **~36.780** (600×61.3) | ~588.360 (600×980.6) | MPCDF Viper; docs.mpcdf | alta (nº GPU) / media (Rpeak) |
| **Levante** (CPU+partición GPU A100) | DKRZ Hamburg | Investigación (clima) | **Operativo** | **#164** (sistema base) | n/d | ~16.800 (total: 14.000 CPU + 2.800 GPU) | AMD EPYC Milan | NVIDIA A100 (40/80GB) | **240 A100** (60 nodos×4) | ~2.328 (240×9.7) | ~74.880 (240×312) | DKRZ PR; DCD | alta (nº GPU) |
| **Levante GPU extension** (NUEVA, GH200) | DKRZ Hamburg | Investigación (clima) | **Operativo** | **#227** (Green500 **#3**) | **6.747** (HPL) | ~8.000 (estimado; no publicado) | NVIDIA Grace (Arm) | **NVIDIA GH200** | nº no publicado (~196 GH200 estimado) | ~6.664 (196×34) aprox. | ~193.844 (196×989) aprox. | DKRZ news; TOP500 nov-2025 highlights | alta (Rmax/rank) / nº GPU NO publicado → REVISIÓN MANUAL |
| **Maxwell** | DESY Hamburg | Investigación | **Operativo** | no | n/d | no publicado (agregado) | mixto (Intel/AMD) | NVIDIA A100 + otras (varias gen.) | no publicado (agregado) | no publicado | no publicado | DESY wiki/IT | baja → REVISIÓN MANUAL |
| **fortytwo** | hessian.AI / GSI Darmstadt | Investigación (IA) | **Operativo** | sí (histórico ~#100; Green500 #41) | n/d (no publicado exacto) | **~8.000** (pico medido) | (host) | NVIDIA A100 80GB (+4 Graphcore IPU) | **632 A100** | ~6.130 (632×9.7) | ~197.184 (632×312) | hessian.AI PR | alta (nº GPU) |
| **fortythree** (ampliación de fortytwo) | hessian.AI / GSI Darmstadt | Investigación (IA) | **Operativo** (desde nov-2024) | **#108** (lista nov-2024; Green500 #42) | no publicado exacto | no publicado exacto | (host) | **NVIDIA H200** | **no publicado** | no publicado | no publicado | hessian.AI PR | media (sistema) / nº GPU NO publicado → REVISIÓN MANUAL |

⚠ **Nota Ponte Vecchio (Intel GPU Max 1550):** la cifra FP64 "vector" 26 TF se usa como cota inferior (ref_aceleradores). En SuperMUC-NG Fase 2 (960 PVC) eso da ~24.960 TF, cercano al Rpeak; con FP64 *matrix* (XMX, 52 TF) daría ~49.920 TF, que probablemente **supera** el Rpeak real → usar 26 (vector) para no inflar. Reconciliación: el Rmax 17.19 PF y Rpeak ~25 PF son coherentes con vector.

---

## (b) Fuentes y citas (verbatim corto; acceso 2026-06-16)

- **JUWELS Booster** — TOP500: *"JUWELS Booster Module - Bull Sequana XH2000, AMD EPYC 7402 24C 2.8GHz, NVIDIA A100… theoretical peak of 70.980 petaflops… 44.1 HPL petaflops (Rmax)"*; *"936 compute nodes hosting four GPUs each, providing access to 3744 GPUs… NVIDIA A100 Tensor Core GPUs (40 GB)… peak of all GPUs together sums up to 73 PFLOP/s"*. https://top500.org/system/179894/ , https://apps.fz-juelich.de/jsc/hps/juwels/booster-overview.html , https://juser.fz-juelich.de/record/902889/files/2108.11976.pdf . Estado nov-2025: *"JUWELS Booster Module at FZJ has 44.1 PFlop/s and remains on the TOP500 list as of November 2025"* (rank exacto no en snippet). (alta)
- **JUWELS Cluster** — Gauss/JSC: *"theoretical peak performance sums up to 12 petaflops… Linpack-performance of 6.2 petaflops (Rmax)… ~2500 dual-socket Intel-Skylake Platinum 8168 nodes… 48 accelerated nodes, each with four NVIDIA V100 GPUs"*. https://www.gauss-centre.eu/gauss-centre/EN/AboutGCS/Locations/JSC/juwels.html , https://top500.org/system/179424/ (media-alta)
- **JEDI** — fz-juelich/HPCwire: *"JEDI… same hardware as the JUPITER booster module… NVIDIA GH200 Grace Hopper Superchip… single rack containing 24 compute nodes, with an additional 24 nodes being added… 4.5 petaflops… 72.73 GFlops/Watt… #1 Green500"*. https://www.fz-juelich.de/en/news/archive/press-release/2024/european-exascale-supercomputer-jupiter-sets-new-energy-efficiency-standards-with-1-ranking-on-green500 , https://thenextweb.com/news/eu-jedi-supercomputer-most-energy-efficient-hpc-system-world (alta nº GPU / media Rpeak)
- **JURECA-DC** — fz-juelich/HPCwire/DCD: *"JURECA-DC consists of a total of 768 compute nodes… 192 of the 768 nodes are equipped with four NVIDIA A100 GPUs each… the new JURECA-DC module alone, with its 18.5 petaflops, is currently among the 30 fastest supercomputers"*. https://www.fz-juelich.de/en/news/archive/press-release/2021/2021-06-23-jureca-dc , https://www.datacenterdynamics.com/en/news/jureca-supercomputer-gets-multi-petaflops-module-upgrade/ (alta nº GPU)
- **JUSUF** — fz-juelich: *"JUSUF consists of 205 nodes, each equipped with two AMD EPYC Rome 64-core processors… 61 nodes are equipped with an additional NVIDIA V100-16G GPU"*. https://www.fz-juelich.de/en/jsc/systems/supercomputers/jusuf (media)
- **SuperMUC-NG Fase 1** — LRZ/Wikipedia: *"theoretical peak of 26.9 petaflops… 6,400 compute nodes… Intel Xeon Skylake… more than 311,040 cores… Linpack 19.46 petaflops (#8 nov-2018)"*. https://doku.lrz.de/hardware-of-supermuc-ng-phase-1-11482553.html , https://top500.org/system/179566/ (alta)
- **SuperMUC-NG Fase 2** — TOP500/HPCwire: *"SuperMUC-NG Phase 2 - ThinkSystem SD650-I V3, Xeon Platinum 8480L 56C 2GHz, Intel Data Center GPU Max… 480 Intel CPUs and 960 Max Series GPUs for a total of 240 nodes… No. 52 at 17.190 petaflops (nov-2023)"*. https://top500.org/system/180182/ , https://www.lrz.de/en/news/detail/2024-02-28-supermuc-ng-phase2-in-test-en (alta nº GPU)
- **Hunter** — TOP500/HLRS/heise: *"Hunter - HPE Cray EX255a, AMD 4th Gen EPYC 24C 1.8GHz, AMD Instinct MI300A, Slingshot-11… theoretical peak performance of 48.1 Petaflops… 752 MI300A accelerators… No. 12 (nov-2025 TOP500)… Green500 #12… 64.653 GFlops/Watt"*. https://top500.org/system/180391/ , https://www.hlrs.de/solutions/systems/hunter , https://www.heise.de/en/news/HRLS-Hunter-First-German-supercomputer-with-AMD-s-giant-APU-MI300A-10245729.html (alta)
- **Hawk / AI Expansion** — HLRS/NVIDIA/nextplatform: *"Hawk… 5,632 CPU nodes… dual AMD Epyc Rome 7740… debut #16 (2020)… Hawk was taken out of service in April 2025, though its AI expansion including NVIDIA A100 GPUs remains in operation… 24 HPE Apollo 6500 Gen10 Plus systems with 192 NVIDIA A100 GPUs… 120 petaflops of AI performance"*. https://www.hlrs.de/news/detail/hawk-upgrade-artificial-intelligence , https://blogs.nvidia.com/blog/stuttgart-supercomputer-hawk-ai/ (alta)
- **Capella** — TU Dresden/Silicon Saxony: *"144 nodes, each equipped with four NVIDIA H100 accelerators… 624 NVIDIA H100 GPUs… 94 Gigabytes of HBM per GPU… more than 38 Petaflops/s… ranked 51st in the world and 3rd in Germany… 5th place on the Green500"*. https://tu-dresden.de/zih/das-department/news/tud-supercomputer-capella-in-top500-und-green500 , https://silicon-saxony.de/en/tu-dresden-tud-high-performance-computer-capella-is-number-3-of-the-most-powerful-german-supercomputers/ (alta)
- **Alex** — NHR@FAU/Megware: *"Alex contains a total of 256 NVIDIA A100 Tensor Core GPUs (160x 40GB, 96x 80GB) and 304 NVIDIA A40 Tensor Core GPUs, making 560 GPUs in total… 140 AMD EPYC 7713 CPUs"*. https://doc.nhr.fau.de/clusters/alex/ , https://www.megware.com/en/company/references/fau-erlangen-nuernberg-fritz-and-alex/ (alta nº GPU)
- **Helma** — NHR@FAU: *"Helma comprises 96 nodes with four NVIDIA H100 GPUs each (384) installed fall 2024… expanded with another 96 nodes for a total of 768 H100 and H200 GPUs (half each)… LINPACK 16.94 Pflop/s #79 (nov-2024)… 32.22 Pflop/s #51 (jun-2025)… now the most powerful system at German universities"*. https://hpc.fau.de/2025/06/10/nhrfau-gpu-cluster-helma-hits-51-in-the-64th-top500-list/ , https://www.fau.eu/2025/10/news/research/hochleistungscomputer-superrechner-helma-eingeweiht/ (alta nº GPU / media Rpeak nov-25)
- **Grete** — GWDG: *"Grete… extends the HPC system Emmy… 36 nodes, each with two AMD Epyc 7513 CPUs and four NVIDIA A100 GPUs, 40 GB HBM2… Phase 2 with 103 additional nodes (A100 40/80GB)… grete:shared with 8×A100 80GB nodes"*. https://gwdg.de/hpc/systems/grete/ (media)
- **HoreKa** — NHR@KIT/HPCwire/DCD: *"HoreKa… 668 NVIDIA A100 Tensor Core GPUs… partitions HoreKa Green (A100), HoreKa Teal (H100), HoreKa Ruby (H200)… hybrid system peak total 17 petaflops… HoreKa-Green Linpack 8 petaflops… 60,000 Intel Xeon Ice Lake cores"*. https://www.nhr.kit.edu/userdocs/horeka , https://www.datacenterdynamics.com/en/news/horeka-hybrid-supercomputer-inaugurated-at-karlsruhe-institute-of-technology/ (media-alta A100)
- **Lise (NHR@ZIB)** — NHR@ZIB/Lenovo: *"NVIDIA GPU partition consists of 42 computing nodes, each containing 4 NVIDIA A100/80 GPUs (168 total)… Eight nodes with four Intel Data Center GPU Max 1550 (PVC) (32 PVC)… more than 120,000 CPU cores, more than 150 GPUs, peak performance of almost 9 Pflop/s"*. https://nhr.zib.de/en/gpu-a100-partition-of-lise-is-online/ , https://user.nhr.zib.de/wiki/spaces/PUB/pages/10158109/GPU+PVC+partition (alta nº GPU)
- **Noctua 2** — PC2/TOP500: *"Noctua 2 has a GPU partition with 32 nodes and a total of 128 Nvidia A100 GPUs… BullSequana XH2000, AMD EPYC 7763 64C… #121 (jun-2022)"*. https://top500.org/system/180071/ , https://pc2.uni-paderborn.de/systems-and-services/noctua-2 (alta nº GPU)
- **Otus (PC2, NUEVO)** — HPCwire: *"'Otus' Now Open for Business at Germany's PC2"* (2025-11-11). https://www.hpcwire.com/2025/11/11/otus-now-open-for-business-at-germanys-pc2/ → especificaciones NO recogidas (REVISIÓN MANUAL). (baja)
- **CLAIX-2023** — RWTH/TOP500: *"CLAIX-2023… 51-52 compute nodes equipped with four NVIDIA Hopper H100 GPUs each (204 H100)… over 14 PFLOPS in the ML segment… NEC HPC12G4Rk-3 DLC, Xeon Platinum 8468 48C, NVIDIA H100, Infiniband NDR"*. https://blog.rwth-aachen.de/itc/en/2024/02/09/claix-2023/ , https://top500.org/system/180295/ . CLAIX-2025: *"isn't yet in production… intended to complement CLAIX-2023"* (previsto). (alta nº GPU CLAIX-2023)
- **Raven** — MPCDF: *"Raven provides 192 GPU-accelerated compute nodes, each with 4 Nvidia A100 GPUs (768 total)… 30 TB GPU RAM (HBM2) and 16 PFlop/s theoretical peak performance (FP64, including tensor cores and host CPUs)… ranked 47th (jun-2021)"*. https://www.mpcdf.mpg.de/services/supercomputing/raven (alta)
- **Viper-GPU** — MPCDF: *"Viper-GPU provides 300 GPU compute nodes, with 2 AMD Instinct MI300A APUs and 128 GB HBM3 per APU (600 APUs total)… AMD Epyc Genoa… installed 2024/2025"*. https://www.mpcdf.mpg.de/services/supercomputing/viper , https://docs.mpcdf.mpg.de/doc/computing/viper-gpu-user-guide.html (alta nº GPU)
- **Levante** — DKRZ/DCD: *"GPU partition consists of 60 GPU nodes… each with two AMD EPYC and four NVIDIA A100 GPUs; 56 nodes with 80GB and 4 with 40GB (240 total)… GPU partition 2.8 PetaFLOPS… CPU partition 14 PetaFLOPS… combined 16.8 petaflops"*. En nov-2025 **Levante (base) rank #164**. https://www.dkrz.de/en/communication/pressemitteilungen/new-high-performance-supercomputer-starts-its-operation-at-dkrz (alta nº GPU)
- **Levante GPU extension (NUEVA, GH200)** — DKRZ/TOP500: *"New GPU extension… based on BullSequana XH-3000 from Eviden: NVIDIA Grace Hopper Superchip 72C 3GHz, NVIDIA GH200 Superchip, Quad-Rail NVIDIA InfiniBand NDR200… 6.747 PFlop/s HPL… 69.43 GFlops/Watt… Green500 #3… TOP500 #227"* (nov-2025). **OJO: es GH200, NO A100; es un módulo NUEVO distinto de la partición A100.** nº de GH200 NO publicado en snippet (≈196 estimado por 6.747 PF / 34 TF). https://www.dkrz.de/en/communication/news-archive/gpu-extension-green500 , https://www.top500.org/lists/top500/2025/11/highs/ (alta Rmax/rank / nº GPU no publicado)
- **fortytwo / fortythree** — hessian.AI: *"fortytwo… 632 NVIDIA A100 Tensor Core GPUs (80GB) + 4 Graphcore IPU… 80 compute nodes… ~8 PFlops… Green500 #41 (353 kW)"*; *"fortythree… first expansion stage of fortytwo… NVIDIA H200 GPUs… 108th place on the Top500 list… Green500 #42… Green IT Cube of GSI/FAIR"* (nov-2024). https://hessian.ai/hessian-ais-supercomputer-fortytwo-achieves-outstanding-position-in-the-international-top500-ranking-of-supercomputers/ , https://hessian.ai/hessian-ais-supercomputer-fortythree-starts-operation-and-achieves-top-position-in-the-international-top500-ranking-of-supercomputers/ (alta fortytwo / media fortythree; nº GPU H200 NO publicado)
- **Maxwell (DESY)** — DESY: *"The Maxwell Cluster is the computing platform at DESY (Hamburg) for Photon Science data analysis, GPU accelerated computations (AI), HPC… nodes with 4 GPUs and 1 GPU… NVIDIA A100"* (agregado NO publicado). https://wiki.desy.de/maxwell/ , https://it.desy.de/services/computing_infrastructure/maxwell_hpc_cluster_including_gpu_computing/index_eng.html (baja → REVISIÓN MANUAL)

---

## (c) REVISIÓN MANUAL (URLs 403 a fetch automático; abrir en navegador)

### Cifras concretas a confirmar de sistemas YA investigados (huecos)
- **JUWELS Booster — rank EXACTO TOP500 nov-2025** (sigue en lista con 44.12 PF Rmax; rank no recogido en snippet). → https://top500.org/system/179894/ y filtrar la lista nov-2025.
- **JEDI — Rpeak exacto** (48×GH200; HPL 4.5 PF conocido; Rpeak ~5.5–6 PF estimado, no publicado). → https://apps.fz-juelich.de/jsc/hps/jedi/configuration.html
- **JURECA-DC — Rmax/rank exactos nov-2025** (módulo DC GPU ~18.5 PF peak; ¿sigue listado?). → top500.org sitio JSC.
- **SuperMUC-NG Fase 1 y Fase 2 — rank y Rmax EXACTOS nov-2025** (Fase 2 era #52 en nov-2023; Fase 1 ~19.5 PF). → https://top500.org/system/179566/ , https://top500.org/system/180182/
- **Hunter — Rmax HPL exacto** (Rpeak 48.1 PF confirmado, rank #12; Rmax dígitos exactos a confirmar). → https://top500.org/system/180391/
- **Capella — Rpeak exacto** (Rmax >38 PF, #51; Rpeak ~46–48 PF estimado). → https://compendium.hpc.tu-dresden.de/jobs_and_resources/capella/
- **Helma — rank y Rmax nov-2025** (era #51 con 32.22 PF en jun-2025; reparto exacto H100/H200; Rpeak). → https://hpc.fau.de/ , https://doc.nhr.fau.de/clusters/helma/
- **Alex / Grete / HoreKa / Noctua 2 / CLAIX-2023 / Raven — Rmax/Rpeak/rank exactos** (nº GPU sólido; cifras de rendimiento HPL no recogidas). → páginas TOP500 de cada sitio.
- **HoreKa — nº de H100 (Teal) y H200 (Ruby)** (solo A100=668 confirmado). → https://www.nhr.kit.edu/userdocs/horeka
- **Viper-GPU (MPCDF) — ¿está en TOP500 nov-2025? Rmax exacto** (600 MI300A; Rpeak ~36.8 PF FP64 vector). → https://www.mpcdf.mpg.de/services/supercomputing/viper
- **Levante GPU extension — nº exacto de GH200** (RESUELTO que es ampliación NUEVA con GH200, NO la partición A100; #227 TOP500 / #3 Green500 / 6.747 PF HPL). Falta solo el conteo de GH200 (≈196 estimado). → https://www.dkrz.de/en/communication/news-archive/gpu-extension-green500

### Sistemas grandes con cifras NO públicas (deben verificarse a mano)
- **fortythree (hessian.AI)** — nº de H200 y Rmax/Rpeak NO publicados en snippets (solo #108 TOP500 nov-2024, H200). → https://hessian.ai/hessian-ais-supercomputer-fortythree-starts-operation-and-achieves-top-position-in-the-international-top500-ranking-of-supercomputers/
- **Maxwell (DESY)** — agregado de GPU (A100 + otras) NO publicado. → https://wiki.desy.de/maxwell/
- **Otus (PC2, nuevo nov-2025)** — especificaciones completas (CPU/GPU/Rpeak). → https://www.hpcwire.com/2025/11/11/otus-now-open-for-business-at-germanys-pc2/
- **Vulcan (HLRS)** — sistema heterogéneo de propósito general; composición GPU no publicada de forma agregada. → https://www.hlrs.de/solutions/systems
- **CLAIX-2025 (RWTH)** — previsto, no en producción jun-2026. → https://blog.rwth-aachen.de/itc/en/tag/claix/

### Otros sistemas de Investigación con GPU NO investigados (prioridad media)
- **CARA/CARO/terrabyte (DLR)**, **Virgo (GSI/FAIR)**, **Hemera/RoSI (HZDR)**, **Albedo (AWI)**, **NEC SX-Aurora (DWD)**, **GridKa (KIT)**, **HAICORE**, **foote (PIK)**, **ML Cloud (Tübingen)**.

### TIER-3 universitario + bwHPC (NO investigado por brief — solo lista para revisión manual)
~30 sistemas, en su mayoría CPU o GPU modesto (A40/L40/A100 parcial), aporte FP64 pequeño:
- **bwHPC (Baden-Württemberg):** bwUniCluster 3.0, Helix (Heidelberg), JUSTUS 2 (Ulm), BinAC 2 (Tübingen), NEMO 2 (Freiburg).
- **Otros universitarios:** RAMSES, Athene, ALCC/LiCCA (Augsburg), LiDO3 (Dortmund), PALMA II (Münster), OMNI (Siegen), Elysium, HILBERT (Düsseldorf), PLEIADES (Bielefeld), MaRC3 (Marburg), Hummel-2 (Hamburg), HSUper (HSU Hamburg), NESH (Kiel), ROSA (Oldenburg), LUIS (Hannover), Aether, Paula/Clara (Leipzig), Sofja, Draco, Brain, Curta (FU Berlin).
- **NHR Tier-2 restantes (CPU/menos GPU, no en este informe):** Fritz (FAU, CPU), Lichtenberg II (TU Darmstadt), Barnard/Alpha Centauri/Romeo/Julia (TU Dresden — Alpha Centauri tiene A100), Emmy (GWDG, CPU base), Goethe-NHR (Frankfurt), MOGON-NHR (Mainz), Elwetritsch III (RPTU Kaiserslautern).

### Comerciales/industriales (anexo, NO al titular público)
- Industrial AI Cloud (Telekom+NVIDIA), alpha ONE (Aleph Alpha), IONOS, StackIT (Schwarz), Taiga Cloud (Northern Data); clusters internos BMW/VW/Mercedes/Bosch/Continental/Porsche/Fraunhofer.

---

## (d) Subtotales de los sistemas investigados (cota inferior; FP64 vector)

### Aceleradores físicos confirmados (nº de tarjetas/APU)
| acelerador | nº confirmado | sistemas |
|---|---|---|
| NVIDIA A100 | **6.625** | JUWELS Booster 3.744 + JURECA-DC 768 + Hawk AI Exp. 192 + Alex 256 + HoreKa 668 + Lise 168 + Noctua 2 128 + Raven 768 + Levante 240 + fortytwo 632 + Grete ~556 (parcial; algunas pueden ser H100) → **(Grete cuenta parcial)** |
| NVIDIA H100 | **828+** | Capella 624 + CLAIX-2023 204 + Helma (~384) + HoreKa Teal (n/d) → (Helma reparte con H200) |
| NVIDIA H200 | **384+** | Helma (~384) + HoreKa Ruby (n/d) + fortythree (n/d) |
| NVIDIA GH200 | **48 + (~196 Levante ext., no publicado)** | JEDI 48 + Levante GPU extension (~196 estimado) |
| NVIDIA A40 | **304** | Alex 304 |
| NVIDIA V100 | **253** | JUWELS Cluster 192 + JUSUF 61 |
| AMD Instinct MI300A (APU) | **1.352** | Hunter 752 + Viper-GPU 600 |
| Intel GPU Max 1550 (PVC) | **992** | SuperMUC-NG Fase 2 960 + Lise 32 |

### Σ Rpeak FP64 aprox. de los sistemas con dato (excl. JUPITER/HammerHAI ya en el otro archivo)
Sistemas con Rpeak FP64 publicado/estimado fiable:
- JUWELS Booster 70.98 PF + JUWELS Cluster 12 PF + Hunter 48.1 PF + SuperMUC-NG F1 26.9 PF + SuperMUC-NG F2 ~25 PF + JURECA-DC 18.5 PF + Viper-GPU ~36.8 PF + Capella ~38 PF (peak) + Helma ~45 PF + Raven 16 PF + HoreKa 17 PF + CLAIX-2023 >14 PF + Lise ~9 PF + Levante (base) 16.8 PF + Levante GPU ext. ~8 PF + JEDI ~5.5 PF + fortytwo ~8 PF + Alex ~5.5 PF + Grete ~9 PF + Noctua 2 ~5.4 PF + Hawk AI Exp ~1.9 PF
- **Σ ≈ 500 PF (0,50 EF) Rpeak FP64** en sistemas distintos de JUPITER (cota inferior; varios Rpeak son estimados).
- **Contexto:** JUPITER Booster solo = **1.226 PF (1,226 EF) Rpeak** (archivo `investigacion_alemania.md`). Es decir, **todo el resto del parque alemán investigado (GCS+NHR+investigación) ≈ 0,51 EF, < 42% del Rpeak de JUPITER Booster.** La concentración en JUPITER es abrumadora.

### Sistemas en TOP500 nov-2025 (confirmados o muy probables)
- **Confirmados con rank/dato nov-2025:** Hunter (#12), Capella (#51), Levante base (#164), Levante GPU ext. GH200 (#227; Green500 #3; 6.747 PF HPL), JUWELS Booster (en lista, rank bajo).
- **En lista pero rank exacto no recogido (históricamente listados, sistemas operativos):** SuperMUC-NG F1, SuperMUC-NG F2, Helma, Alex, Grete, HoreKa, Noctua 2, CLAIX-2023, Raven, JEDI, fortytwo, fortythree (era #108 nov-2024), JURECA-DC (probable).
- **NO en TOP500:** Hawk (retirado abr-2025), Hawk AI Expansion, JUSUF, Lise (probable), Vulcan, Maxwell.

### Cambios de estado relevantes a jun-2026
- **Hawk (base):** RETIRADO abr-2025; su AI Expansion (192 A100) sigue operativa.
- **JUWELS Booster:** operativo pero superado por JUPITER (mismo centro JSC).
- **CLAIX-2025, Blue Lion (LRZ), Herder (HLRS):** PREVISTOS, no operativos jun-2026.
- **Helma:** ampliado e inaugurado oct-2025 (768 H100/H200).
- **Otus (PC2):** nuevo, operativo nov-2025 (specs pendientes).
