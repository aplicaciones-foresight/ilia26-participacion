# Investigación HPC — ALEMANIA (estado jun-2026; TOP500 nov-2025)

> **NOTA DE PROCESO:** la primera corrida de agentes se interrumpió por límite de sesión.
> Este archivo recoge los sistemas YA investigados con dato sólido (JUPITER, HammerHAI,
> JAIF/JARVIS) y deja una lista PENDIENTE para completar (resto de GCS, NHR, Tier-3).
> Muchas webs (top500.org, fz-juelich.de, etc.) devuelven HTTP 403 a fetch automático;
> los datos provienen de TOP500 + prensa de fabricante + snippets, con confianza marcada.

## Tabla por sistema (investigados)

| sistema | centro | tier | estado jun-2026 | TOP500 nov-25 | Rmax FP64 (TF) | Rpeak FP64 (TF) | CPU | acelerador | nº GPUs | GPU FP64 (TF) | GPU FP16/BF16 (TF) | conf. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| JUPITER Booster | JSC/EuroHPC | Tier-0 | **Operativo** | **#4** | **1.000.000** | **1.226.000** | NVIDIA Grace (Arm) | NVIDIA GH200 | **≈23.536** (5.884×4; NVIDIA "≈24.000") | ≈800.224 (vector 34) / nota | ≈23.277.000 (FP16 TC) | alta |
| JUPITER Cluster | JSC/EuroHPC | Tier-0/1 | **En puesta en marcha** (no pleno jun-26) | no | n/d | >5.000 | SiPearl Rhea1 (Arm Neoverse V1) | — (sin GPU) | 0 | 0 | 0 | alta |
| HammerHAI | HLRS/EuroHPC | Tier-1 AI | **Previsto** (2ª mitad 2026) | no | n/d | n/d (IA: >15 EF inferencia) | NVIDIA Grace | NVIDIA GB200 (Blackwell) | **860** (215×4) | ~34.400 (860×40 TC, verificar) | muy alto (Blackwell) | alta |
| JARVIS (módulo JAIF) | JSC/EuroHPC | — | Planificado | no | — | **no publicado** | — | experimental europeo | no publicado | no publicado | no publicado | media |

### Notas de cómputo / decisiones
- **JUPITER GPU FP64:** 23.536 × 34 (FP64 *vector* GH200) = **800.224 TF**, valor consistente con Σ ≤ Rpeak (1.226.000). Con FP64 *Tensor Core* (67) daría 1.576.912 TF, que **supera** el Rpeak listado → el Rpeak de TOP500 NO se computó a tasa TC plena. El resto del Rpeak (≈426.000 TF) lo aportan las CPU Grace. **Decisión de convención (vector vs TC) pendiente** (el motor permite recomputar).
- **JUPITER IA:** oficial JSC ">70 EF en 8-bit con sparsity"; NVIDIA ">90 EF FP8". Ambas **FP8**, no FP16. La estimación FP16 (≈23,3 EF) es coherente (FP8≈2×FP16; +sparsity ×2 ⇒ ~93 EF ✓).
- **JAIF = JUPITER + servicios + JARVIS.** NO sumar "JAIF" como capacidad nueva: su HW grande ES el Booster de JUPITER. Lo único nuevo (JARVIS) está **sin cuantificar**. Evitar doble conteo.
- **JUPITER Cluster** y **HammerHAI**: a jun-2026 **NO plenamente operativos** → en el consolidado van con `incluir_capacidad=0` (registrados, no sumados al titular). HammerHAI (860 GB200) entrará al titular cuando opere (2ª mitad 2026).

## Fuentes y citas (clave)
- **JUPITER Booster** — TOP500 nov-2025: *"1.000 Exaflop/s (Rmax) / 1.226 Exaflop/s (Rpeak)… ranks No. 4"*; https://top500.org/system/180357/ , https://www.top500.org/lists/top500/2025/11/ . NVIDIA: *"a booster module comprising close to 24,000 NVIDIA GH200 Superchips… 18.2 MW… 60 GFLOPS/W"*; https://nvidianews.nvidia.com/news/nvidia-powers-europes-fastest-supercomputer . (acceso 2026-06-16, alta)
- **JUPITER Cluster (Rhea1)** — JSC Tech: *"more than 1300 nodes to achieve a performance of more than 5 PetaFLOP/s (FP64, HPL)"*; https://www.fz-juelich.de/en/jsc/jupiter/tech . SiPearl: *"On May 13, 2026, SiPearl powered on the first Rhea1 processor… full system readiness is expected by the end of 2026"*; https://sipearl.com/ (acceso 2026-06-16, alta)
- **JAIF / JARVIS** — fz-juelich.de: *"JAIF is funded with €55 million…"*; *"the construction of another supercomputer module… JARVIS… The booster module with its approximately 24,000 NVIDIA GPUs will continue to be used for AI training, while JARVIS takes over… inference."* https://www.fz-juelich.de/en/news/archive/press-release/2025/europes-ai-booster-jupiter-ai-factory , https://www.heise.de/en/news/JUPITER-New-supercomputer-module-for-European-AI-factory-10314571.html , CORDIS id 101250607 (acceso 2026-06-16, alta)
- **HammerHAI** — DCD/HLRS: *"215 nodes NVIDIA GB200 NVL4 (4 GPU + 2 Grace/node) = 860 GPUs… more than 15 Exaflops of peak AI inference… contract with HPE signed March 16, 2026… delivery Q2 2026 and operation second half of 2026… €85 million"*; https://www.hlrs.de/solutions/systems/hammerhai , https://www.hammerhai.eu/system/ , https://www.datacenterdynamics.com/en/news/eurohpc-ju-signs-contract-with-hpe-to-deploy-hammerhai-supercomputer-at-hlrs-in-stuttgart-germany/ (acceso 2026-06-16, alta)

## PENDIENTE de investigar (no alcanzado por límite de sesión) — REVISIÓN/2ª CORRIDA
Sistemas del inventario sin dato de capacidad aún. Prioridad por capacidad esperada:
- **GCS Tier-0/1:** JEDI (JSC, 48×GH200, fue #1 Green500), JUWELS (Cluster+Booster, JSC — Booster ~3.744 A100), JURECA-DC (JSC), JUSUF (JSC); SuperMUC-NG Fase 1 (LRZ, Intel) y **Fase 2** (LRZ, Intel PVC Max 1550); Hunter (HLRS, AMD MI300A), Vulcan, Hawk AI Expansion (HLRS). Previstos: Blue Lion (LRZ), Herder (HLRS).
- **NHR Tier-2 (≈12 centros):** CLAIX-2023/2025 (RWTH), Lichtenberg II (Darmstadt), Fritz/Alex/Helma (FAU), HoreKa (KIT), Barnard/Capella/Alpha Centauri/Romeo/Julia (TU Dresden — **Capella** es GPU H100), Lise (ZIB), Emmy/Grete (GWDG), Noctua 2 (Paderborn), Goethe-NHR (Frankfurt), MOGON-NHR (Mainz), Elwetritsch III (RPTU).
- **Investigación:** Levante (DKRZ), Raven/Viper (MPCDF), CARA/CARO/terrabyte (DLR), Maxwell (DESY), Virgo (GSI/FAIR), Hemera/RoSI (HZDR), Albedo (AWI), NEC SX-Aurora (DWD), GridKa (KIT), HAICORE, foote (PIK), fortytwo/fortythree (hessian.AI), ML Cloud (Tübingen).
- **Tier-3 bwHPC + universitarios** (~30): bwUniCluster 3.0, Helix, JUSTUS 2, BinAC 2, NEMO 2, RAMSES, Athene, ALCC/LiCCA, LiDO3, PALMA II, OMNI, Elysium, HILBERT, PLEIADES, MaRC3, Hummel-2, HSUper, NESH, ROSA, LUIS, Aether, Paula/Clara, Sofja, Draco, Brain, Curta, etc.
- **Comerciales/industriales (anexo, NO al titular):** Industrial AI Cloud (Telekom+NVIDIA), alpha ONE (Aleph Alpha), IONOS, StackIT (Schwarz), Taiga Cloud (Northern Data); BMW/VW/Mercedes/Bosch/Continental/Porsche/Fraunhofer.

> **Concentración:** JUPITER Booster (1,226 EF Rpeak) domina abrumadoramente; el resto del parque alemán, aun sumando todos los Tier-2/3, es una fracción pequeña del total FP64 (cota inferior).
