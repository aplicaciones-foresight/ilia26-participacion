# Investigación HPC — SINGAPUR (estado jun-2026; rankings TOP500 nov-2025)

> **NOTA DE PROCESO (control de coste):** investigación secuencial, sin sub-agentes. **WebFetch
> devolvió HTTP 403 en TODOS los hosts probados** (top500.org, nscc.sg, nusit.nus.edu.sg,
> nsccsg.github.io, news.nus.edu.sg, hpcwire.com, computerweekly.com, datacenterdynamics.com,
> opengovasia.com, metebalci.com). **Todos los datos provienen de extractos de WebSearch**
> (citables) + páginas TOP500 (título del sistema visible en resultados). Cifras de Rmax/Rpeak
> exactos por sistema y **ranks específicos de nov-2025** quedan en REVISIÓN MANUAL.

> **⚠️ HALLAZGO CLAVE 1 — ASPIRE 2B (NTU):** lanzado **8-jun-2026** (operativo a jun-2026,
> demasiado nuevo para TOP500 nov-2025). **>1.500 GPU NVIDIA H200**, AMD EPYC, **115 PFLOPS**,
> 63,5 PB. Es ahora el sistema dominante de Singapur. La precisión de los "115 PFLOPS" NO está
> clara (probable FP64 *Tensor Core* o pico mixto, NO FP64 vector — ver notas).

> **⚠️ HALLAZGO CLAVE 2 — SUBESTIMACIÓN MATERIAL:** Singapur es el mayor hub de datacenters de
> IA del Sudeste Asiático. La capacidad GPU comercial/privada (no verificable) es **muy superior**
> a la suma de sistemas públicos verificables. Solo un operador (SMC) declara 1.600–4.000 H100.
> Estos NO entran al cómputo; ver ANEXO.

## (a) Tabla por sistema

| sistema | centro | estado jun-26 | rank TOP500 nov-25 | Rmax FP64 (TF) | Rpeak FP64 (TF) | CPU | acelerador | nº GPUs | GPU FP64 vector (TF) | GPU FP16 (TF) | fuente | conf. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Hopper** | NUS (NUS-IT) | Operativo (jun-2025) | en lista (#105 jun-25; **rank exacto nov-25 → REV.**) | **~25.000** (HPL "25 PFLOPS") | no publicado (REV.) | 2× Intel Xeon Platinum 8480+ 56C (92×? cores) | NVIDIA **H100 80GB / H200 141GB** (mezcla) | **368** (46 nodos × 8) | ~12.512 (368×34) | ~363.952 (368×989) | TOP500 sys 180379; NUS-IT; ComputerWeekly | media-alta |
| **ASPIRE 2A+** | NSCC (Fusionopolis) | Operativo | en lista (#90 nov-24; **rank nov-25 → REV.**) | **~13.000** ("13 PF HPL") | ~20.000 (FP64 *Tensor Core*, dato NSCC) | 2× Intel Xeon Platinum 8480C 56C | NVIDIA **H100 SXM5 80GB** (DGX H100) | **320** (40 DGX × 8) | ~10.880 (320×34) | ~316.480 (320×989) | TOP500 sys 180325; NSCC | alta |
| **ASPIRE 2A (GPU)** | NSCC (Fusionopolis) | Operativo | #167 (GPU, **nov-2022**); **nov-25 prob. fuera → REV.** | no publicado (REV.; #167 era ~? PF) | no publicado (REV.) | AMD EPYC 7713 64C (Milan) | NVIDIA **A100 SXM4 40GB** | **352** (82 nodos × 4) | ~3.414 (352×9,7) | ~109.824 (352×312) | TOP500 sys 180077; NSCC user guide | alta |
| **ASPIRE 2B** | NSCC @ **NTU** | **Operativo (lanzado 8-jun-2026)** | NO (post-lista nov-25) | no publicado (REV.) | **~115.000** (precisión ⚠ FP64-TC/mixto, NO vector) | AMD EPYC (~184.000 cores, verificar) | NVIDIA **H200** | **>1.500** (~1.500) | ~51.000 (1.500×34) | ~1.483.500 (1.500×989) | DCD; Malay Mail; Mothership; MDDI | media-alta |
| **CHROMA** | SingHealth / SGH (Alice Lee CoE) | Operativo (2024) | NO | no publicado | no publicado | 1.024 cores CPU (modelo no publ.) | NVIDIA **DGX A100** (HBM 320GB) | **~8** (≥1 DGX A100; **REV.** nº exacto) | ~77,6 (8×9,7) | ~2.496 (8×312) | SingHealth; HealthcareITNews; AsianScientist | media-baja |
| **NTU HPCC (GEKKO etc.)** | NTU | Operativo | NO | n/d | n/d | varios | NVIDIA (varias) | ~8+ (GEKKO: 2 srv × 8; **REV.**) | n/d | n/d | NTU HPCC; MIG docs | baja |
| **A*STAR IHPC** | A*STAR (Fusionopolis) | Operativo (usa ASPIRE) | — | — | — | — | — (sin sistema TOP500 propio; usa NSCC) | — | — | — | A*STAR; A*CRC | media |

> **Convención aplicada:** nº GPUs = tarjetas físicas (1 GH200 = 1 GPU; aquí no hay GH200).
> GPU FP64 *vector* como cota inferior principal; H100/H200/GH200 = 34 TF vector (67 TF Tensor
> Core); A100 = 9,7 TF vector (19,5 TF TC); FP16 tensor: H100/H200 = 989 TF, A100 = 312 TF.
> **Reconciliación Σ GPU FP64 ≤ Rpeak:** donde hay Rpeak público (Hopper, ASPIRE 2B), el Rpeak
> declarado en "PFLOPS" parece corresponder a FP64-TC o pico mixto IA, **superior** a la suma
> FP64 vector — coherente (la cota inferior vector queda por debajo del pico anunciado).

## (b) Fuentes y citas por sistema (fecha de consulta: 2026-06-16)

### Hopper (NUS)
- **Rank / Rmax** — *"Hopper has been placed in 105th position on the TOP500 … capable of performing 25 quadrillion calculations per second, or 25 petaflops … went live in June 2025"* — ComputerWeekly / NUS News (vía WebSearch). https://www.computerweekly.com/news/366631370/NUS-supercomputer-enters-global-Top500 ; https://news.nus.edu.sg/nus-ramps-up-high-performance-computing-capability-to-propel-research/ — confianza **alta** (rank #105 es de la lista de **junio 2025**; persistencia en nov-2025 confirmada por existencia de la página TOP500 del sistema, pero **el número de rank exacto en nov-2025 → REV.**).
- **Config HW** — *"46 nodes … 8x NVIDIA H100 80GB or 8x NVIDIA H200 141GB per node … 2 x Intel 8480+ 56-cores per node … 2 TB per node … Infiniband NDR (400Gb)"*; *"a total of 368 GPUs across the H100 and H200 accelerators"* — NUS-IT HPC (vía WebSearch). https://nusit.nus.edu.sg/hpc/?p=175 — confianza **media-alta** (368 = 46×8 derivado; reparto exacto H100 vs H200 **no publicado → REV.**).
- **TOP500 título de sistema** — *"Hopper NUS - PowerEdge XE9680, Xeon Platinum 8480+ 56C 2GHz, NVIDIA H100/H200, Infiniband NDR400, RedHat 9.4"* — https://www.top500.org/system/180379/ — confianza **alta** (confirma vendor Dell PowerEdge XE9680, CPU, GPU mixta).
- **Builder** — *"built with infrastructure from Dell Technologies"* — NUS News — confianza **alta**.

### ASPIRE 2A+ (NSCC)
- **Config / Rmax / pico** — *"40 x DGX H100 nodes with a total of 320 H100 GPUs and achieves 13 PF (HPL Benchmark) … estimated 20 PFLOPS of raw compute power at FP64 Tensor Core precision"* — NSCC (vía WebSearch). https://www.nscc.sg/aspire-2a-plus/ — confianza **alta**.
- **Rank** — *"ASPIRE 2A+ is ranked 90th in the November 2024 TOP500"* — confianza **alta** para nov-24; **rank nov-2025 → REV.**
- **TOP500 título** — *"ASPIRE 2A+ - NVIDIA DGX H100, Xeon Platinum 8480C 56C 2GHz, NVIDIA H100 SXM5 80GB, Infiniband NDR, Ubuntu 22.04"* — https://www.top500.org/system/180325/ — confianza **alta**.

### ASPIRE 2A (NSCC) — particiones GPU y CPU
- **Config** — *"ASPIRE 2A has 82 GPU nodes with a total of 352 GPUs … 4 x NVIDIA A100-40G SXM per node … 768 compute nodes (98,304 cores) … 16 large memory nodes (2,048 cores) … 16 High Frequency Nodes (1,024 cores) … 2x AMD EPYC Milan 7713 … up to 10 PFlops"* — NSCC user guide (vía WebSearch). https://nsccsg.github.io/systems/aspire2a/system-specifications/ ; https://www.nscc.sg/aspire-2a/ — confianza **alta**.
- **TOP500 título (GPU partition)** — *"ASPIRE 2A (GPU Partition) - HPE Cray EX235n, Apollo 6500, AMD EPYC 7713 64C 2GHz, NVIDIA A100 SXM4 40 GB, Slingshot-10"* — https://top500.org/system/180077/ — confianza **alta**.
- **Rank histórico** — *"ranked 167th (GPU portion) and 275th (CPU portion) in the November 2022 TOP500"* — A*STAR Research / NSCC — confianza **alta** (histórico). **Estado en nov-2025: probablemente fuera de la lista** (sistema de 2022, A100); Rmax/Rpeak exactos **no surgieron en snippets → REV.**

### ASPIRE 2B (NSCC @ NTU) — NUEVO
- **Lanzamiento / GPUs / pico** — *"Aspire 2B … launched on June 8, 2026 … equipped with more than 1,500 Nvidia H200 GPUs … the country's largest Nvidia cluster dedicated to research and public sector use … features AMD Epyc CPUs and 63.5PB of storage … delivers up to 115 petaflops … close to four times the combined capacity of … Aspire 2A and Aspire 2A+"* — DataCenterDynamics / Malay Mail / Mothership (vía WebSearch). https://www.datacenterdynamics.com/en/news/singapore-launches-new-national-supercomputer/ ; https://www.malaymail.com/news/singapore/2026/06/08/.../223025 ; https://mothership.sg/2026/06/singapore-supercomputer-aspire-2b/ — confianza **media-alta** (cifras consistentes en varias fuentes; **precisión de "115 PFLOPS" no especificada → REV.**).
- **Cores / quantum** — *"powered by about 1,500 Nvidia H200 GPUs and 184,000 AMD CPUs [cores]"*; *"expected to be connected to Quantinuum's Helios quantum computer"* — confianza **media** ("184.000 AMD CPUs" → casi seguro **cores**, verificar). https://www.mddi.gov.sg/newsroom/opening-address-by-minister-josephine-teo-...
- **Ubicación / vendor** — *"housed in NTU in a facility that measures around 400 square meters"*; vendor (HPE/Dell/Lenovo) **no publicado → REV.** — confianza **media**.

### CHROMA (SingHealth / SGH)
- *"CHROMA … SingHealth's first supercomputer … at the Alice Lee Innovation Centre of Excellence @ SGH Campus … has 1,024 CPU cores … equipped with an NVIDIA DGX 320 GB AI accelerator … researchers can use … multiple NVIDIA DGX A100 compute nodes"* — SingHealth / HealthcareITNews / AsianScientist (vía WebSearch). https://www.singhealth.com.sg/news/announcements/supercomputer-for-complex-health-research-at-new-centre ; https://www.healthcareitnews.com/news/asia/singhealth-nscc-and-nvidia-team-large-scale-and-complex-healthcare-research — confianza **media-baja** ("DGX 320 GB" = **DGX A100** con 8×A100 40GB = 320 GB HBM; **nº de DGX/total GPUs no publicado → REV.**). Sistema modesto, **no TOP500**.

### NTU HPCC / A*STAR IHPC
- **NTU HPCC** — clúster comunitario universitario; *"GEKKO … 8 GPU … 2 GPU servers with 8 GPU cards each"* — modesto, **no TOP500**. https://www.ntu.edu.sg/hpcc ; https://migg-ntu.github.io/MIG_Docs/ntu/cluster/gekko/ — confianza **baja** (config detallada → REV.).
- **A*STAR IHPC** — instituto de investigación; usa los sistemas **ASPIRE de NSCC** (alojados en Fusionopolis); no se halló un sistema TOP500 propio actual. https://www.a-star.edu.sg/ihpc ; https://www.a-star.edu.sg/acrc — confianza **media**.

## (c) REVISIÓN MANUAL (URLs exactas a abrir en navegador — todas dieron 403 a WebFetch)

1. **TOP500 sublista Singapur nov-2025** (confirmar QUÉ sistemas SG siguen en lista + rank/Rmax/Rpeak/cores exactos):
   - https://top500.org/lists/top500/list/2025/11/ (filtrar "Singapore")
   - https://top500.org/site/50631/ (National Supercomputing Centre Singapore — lista de sus entradas)
2. **Hopper NUS** — Rmax/Rpeak exactos, cores totales, reparto H100/H200, rank nov-25:
   - https://www.top500.org/system/180379/
   - https://nusit.nus.edu.sg/hpc/?p=175
3. **ASPIRE 2A+** — Rmax/Rpeak/cores, rank nov-25:
   - https://www.top500.org/system/180325/
   - https://www.nscc.sg/aspire-2a-plus/
4. **ASPIRE 2A (GPU partition)** — Rmax/Rpeak/cores, confirmar si sigue en nov-25:
   - https://top500.org/system/180077/
   - https://nsccsg.github.io/systems/aspire2a/system-specifications/
5. **ASPIRE 2B** — precisión de "115 PFLOPS" (¿FP64 vector / FP64-TC / IA?), nº exacto H200, cores AMD, modelo EPYC, vendor:
   - https://www.nscc.sg/aspire-2b/
   - https://www.datacenterdynamics.com/en/news/singapore-launches-new-national-supercomputer/
   - https://www.mddi.gov.sg/newsroom/opening-address-by-minister-josephine-teo-at-national-supercomputing-centre--nscc--s-launch-of-aspire-2b-supercomputer/
6. **CHROMA** — nº de DGX A100 / total GPUs, modelo CPU:
   - https://www.singhealth.com.sg/news/announcements/supercomputer-for-complex-health-research-at-new-centre
7. **NTU HPCC** — inventario GPU del clúster comunitario:
   - https://www.ntu.edu.sg/hpcc

## (d) Totales país — COTA INFERIOR (solo sistemas verificables; FP64 vector como principal)

> Incluye sistemas operativos a jun-2026 con datos públicos: **Hopper, ASPIRE 2A+, ASPIRE 2A,
> ASPIRE 2B, CHROMA**. Excluye NTU HPCC/A*STAR (sin datos firmes) y TODO cómputo comercial (anexo).

| Métrica | Valor cota inferior | Cómo se obtiene |
|---|---|---|
| **Σ Rpeak FP64 (declarado)** | **≥ ~173 PFLOPS** | Hopper 25 + 2A+ 20(FP64-TC) + 2A ~3,1(vector) + 2B 115(mixto/FP64-TC) + CHROMA n/d. **⚠ mezcla precisiones** (2A+ y 2B son pico TC/IA, no FP64 vector). |
| **Σ nº GPUs (tarjetas físicas)** | **≥ 2.548** | 368 + 320 + 352 + 1.500 + ~8 = **2.548** |
| **Σ GPU FP64 vector (TF)** | **≥ ~77.884 TF (~77,9 PF)** | 12.512 + 10.880 + 3.414 + 51.000 + 78 |
| **Σ GPU FP64 Tensor Core (TF)** | **≥ ~153.700 TF (~153,7 PF)** | (368+320+1.500)×67 + 352×19,5 + 8×19,5 |
| **Σ GPU FP16 tensor (TF)** | **≥ ~2.276.252 TF (~2,28 EF FP16)** | 363.952 + 316.480 + 109.824 + 1.483.500 + 2.496 |

> **Cota inferior conservadora:** si se desea estricta "FP64 vector como cota inferior", usar
> **Σ Rpeak ≈ 77,9 PF (FP64 vector)** y **2.548 GPUs**. Las cifras de prensa (25/20/115 PF)
> mezclan precisiones y deben tratarse con cautela para comparación FP64 vector.

## (e) Notas

1. **Concentración nacional:** la capacidad pública verificable está MUY concentrada en **NSCC**
   (ASPIRE 2A + 2A+ + 2B = ~2.172 de las 2.548 GPUs, ~85%) y **NUS (Hopper, 368)**. ASPIRE 2B
   solo (>1.500 H200) representa ~59% de las GPUs físicas del país. Es el nuevo sistema dominante.
2. **Salto generacional jun-2026:** ASPIRE 2B (H200, lanzado 8-jun-2026) cuadruplica la capacidad
   nacional de investigación previa (2A+2A+). **No aparece en TOP500 nov-2025** (posterior); si se
   presenta a HPL podría entrar alto en listas futuras (jun-2026/nov-2026).
3. **Ambigüedad de precisión (CRÍTICO para ILIA):** las cifras de prensa "25/20/115 PFLOPS"
   probablemente NO son FP64 vector (Linpack). ASPIRE 2A+ "20 PF" está explícitamente etiquetado
   *FP64 Tensor Core*. ASPIRE 2B "115 PF" sin etiqueta (coherente con FP64-TC de ~1.500 H200).
   Hopper "25 PF" probablemente Rmax HPL (FP64). **Homogeneizar la base de comparación es esencial.**
4. **SUBESTIMACIÓN MATERIAL por cómputo comercial excluido (ver ANEXO):** Singapur es el centro
   de gravedad de IA del Sudeste Asiático. La capacidad GPU comercial/privada instalada es **muy
   superior** a la suma pública verificable, pero es **opaca y no verificable** → registrada solo
   como anexo, **fuera del cómputo**. El total país (d) es una **cota inferior fuerte**.

---

## ANEXO — Cómputo comercial/privado (NO verificable; NO entra al cómputo)

> Singapur concentra capacidad GPU de hyperscalers y nubes IA muy por encima de los sistemas de
> investigación públicos. Ejemplos puntuales hallados (solo ilustrativos, NO exhaustivos):

- **Sustainable Metal Cloud (SMC):** *"1,600 H100 SXM GPUs today, and up to 4,000 by 2024"* —
  Singapore EDB. https://www.edb.gov.sg/en/business-insights/insights/why-this-ai-cloud-provider-chose-to-launch-its-sustainable-ai-solutions-from-singapore.html (2026-06-16, media).
- **Mercado DC-GPU SG:** *"Hyperscalers and cloud service providers held 61.54% of the Singapore
  data center GPU market share in 2025 … Singapore … the region's AI gravity center"*; tope de
  **200 MW** (programa DC-CFA2) + obligación de refrigeración líquida >30 MW — Mordor Intelligence.
  https://www.mordorintelligence.com/industry-reports/singapore-data-center-gpu-market (2026-06-16, media).
- **Nubes con H100/H200/B200 en SG:** OVHcloud, y proveedores APAC con B200 — Spheron.
  https://www.spheron.network/blog/gpu-cloud-providers-asia-pacific-2026/ (2026-06-16, baja).

> **Conclusión del anexo:** un único operador comercial (SMC, hasta 4.000 H100) ya supera en
> tarjetas a TODO ASPIRE 2A+2A+. La capacidad nacional REAL instalada (pública + privada) es
> **materialmente superior** a la cota inferior verificable de la sección (d). Para ILIA, declarar
> explícitamente esta subestimación.

## Fuentes (enlaces)
- TOP500 sistemas: https://www.top500.org/system/180379/ ; https://www.top500.org/system/180325/ ; https://top500.org/system/180077/ ; https://top500.org/site/50631/ ; https://top500.org/lists/top500/list/2025/11/
- NSCC: https://www.nscc.sg/aspire-2a/ ; https://www.nscc.sg/aspire-2a-plus/ ; https://www.nscc.sg/aspire-2b/ ; https://nsccsg.github.io/systems/aspire2a/system-specifications/
- NUS: https://nusit.nus.edu.sg/hpc/?p=175 ; https://news.nus.edu.sg/nus-ramps-up-high-performance-computing-capability-to-propel-research/ ; https://www.computerweekly.com/news/366631370/NUS-supercomputer-enters-global-Top500
- ASPIRE 2B prensa: https://www.datacenterdynamics.com/en/news/singapore-launches-new-national-supercomputer/ ; https://www.malaymail.com/news/singapore/2026/06/08/singapore-rolls-out-aspire-2b-supercomputer-to-strengthen-ai-quantum-and-climate-research-says-minister/223025 ; https://mothership.sg/2026/06/singapore-supercomputer-aspire-2b/ ; https://www.mddi.gov.sg/newsroom/opening-address-by-minister-josephine-teo-at-national-supercomputing-centre--nscc--s-launch-of-aspire-2b-supercomputer/
- CHROMA: https://www.singhealth.com.sg/news/announcements/supercomputer-for-complex-health-research-at-new-centre ; https://www.healthcareitnews.com/news/asia/singhealth-nscc-and-nvidia-team-large-scale-and-complex-healthcare-research
- A*STAR / NTU: https://www.a-star.edu.sg/ihpc ; https://research.a-star.edu.sg/articles/features/the-petascale-push/ ; https://www.ntu.edu.sg/hpcc
- Comercial: https://www.edb.gov.sg/en/business-insights/insights/why-this-ai-cloud-provider-chose-to-launch-its-sustainable-ai-solutions-from-singapore.html ; https://www.mordorintelligence.com/industry-reports/singapore-data-center-gpu-market
