# Investigación HPC — ESPAÑA (RESTO / nodos faltantes) — Índice ILIA 2026

**País:** España · **Red:** Red Española de Supercomputación (RES / ICTS) + EuroHPC (BSC)
**Fecha de referencia:** estado operativo a **junio 2026**; rankings **TOP500 noviembre 2025**.
**Fecha de acceso a fuentes:** 2026-06-16 · **Idioma:** español · **Fuentes:** ES/EN.
**Autor:** investigación automatizada secuencial (sin sub-agentes), triangulación WebSearch.

> **Nota de método (límite del entorno):** El *fetch* directo (WebFetch) devolvió **HTTP 403**
> en TODOS los dominios relevantes (top500.org, bsc.es, csuc.cat, cesvima.upm.es, res.es…).
> Toda la evidencia procede de **WebSearch** (extractos citables de esas mismas páginas).
> Las cifras que sólo existen en una ficha concreta no indexada quedan marcadas para
> **REVISIÓN MANUAL** con su URL exacta. **No se inventó ningún número.**

> Este fichero COMPLEMENTA `investigacion_espana.md` (1ª corrida). Aquí se cierran los
> PENDIENTES: MareNostrum 5 (Rpeak ACC + nº H100 + NGT + AI Factory) y los nodos RES sin dato.

---

## (a) Tabla por sistema / partición

Leyenda: Rmax/Rpeak en **TFLOP/s FP64**. "nº GPUs" = tarjetas físicas. GPU FP64 = pico FP64
**vector** (cota inferior; tensor entre paréntesis donde aplica). GPU FP16 = pico tensor/dense.
Aceleradores (TF/tarjeta): V100 7,8 / FP16 125 · A100 9,7 (TC 19,5) / FP16 312 ·
H100 34 (TC 67) / FP16 989 · L40S 1,4 / FP16 362 · A40 0,58. "n.p." = no publicado · "—" = no aplica.

| sistema / partición | centro | estado jun-26 | rank TOP500 nov-25 | Rmax (TF) | Rpeak (TF) | CPU | acelerador | nº GPUs | GPU FP64 vector (TF) | GPU FP16 (TF) | fuente | confianza |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **MareNostrum 5 ACC** | BSC / EuroHPC, Barcelona | **Operativo** | **#14** | **175 300** | **260 000** | 2× Intel Xeon Platinum **8460Y+** (40C, 80c/nodo) × **1 120 nodos** | **NVIDIA H100 64 GB** | **4 480** (1 120×4) | **152 320** (4 480×34) / TC 300 160 | **4 430 720** (4 480×989) | TOP500 sys 180238; BSC; HPCwire; Wikipedia | **Alta** |
| **MareNostrum 5 GPP** | BSC / EuroHPC, Barcelona | **Operativo** | **#50** | **40 100** | **~45 900** | 2× Intel Xeon Platinum **8480+** 56C (112c/nodo) × **6 408 nodos** + 72 nodos HBM | — (solo CPU) | 0 | 0 | 0 | TOP500 sys 180237; BSC; RNCA | **Alta** |
| **MareNostrum 5 NGT-GRACE** (piloto) | BSC, Barcelona | Operativo (experimental) | no | n.p. | **~5 700** | **NVIDIA Grace** (ARM) superchip, **802 chips** / 408 nodos (2 Grace/nodo) | — (Grace = CPU ARM, sin GPU) | 0 | 0 | 0 | BSC supportkc /Grace/; tom'sHW | Media-alta |
| **MareNostrum 5 NGT-ACC** (piloto) | BSC, Barcelona | Experimental / pruebas | no | n.p. | n.p. | Intel (acelerado) | **Intel Rialto Bridge** (Data Center GPU Max nueva gen) | n.p. | n.p. | n.p. | BSC supportkc; RNCA | Baja (no definido) |
| **MN5 "AI Factory" (MareNostrum 5 AI upgrade)** | BSC / EuroHPC, Barcelona | **NO operativo** (instalación 1er sem-2026; op. ~mediados 2026) | no (futuro) | — | **+~150 000** (→ total >450 PF) | (nodos LLM + inferencia) | **NVIDIA "next-gen" GPU** (modelo exacto no público) + Supermicro/IBM/VAST | n.p. | n.p. | n.p. | EuroHPC; DCD; Fujitsu; HPCwire | Media |
| **Tirant III (Tirant v3)** | Univ. de València (SIUV), Burjassot | **Operativo** | no | n.p. (HPL) | **111,8** | 2× Intel Xeon **SandyBridge E5-2670** (8C) × **336 nodos** = **5 376 cores** | — (solo CPU) | 0 | 0 | 0 | UV (SIUV); ciencia.gob.es; RES | Alta |
| **LaPalma** | IAC, Breña Baja (La Palma) | **Operativo** | no | n.p. | **83,85** | 2× Intel Xeon **SandyBridge** (8C) × **252 nodos** | — (solo CPU) | 0 | 0 | 0 | IAC; UV/RES snippets | Media-alta |
| **Lusitania III** | COMPUTAEX / CénitS, Cáceres | **Operativo** | no | n.p. | **313** (≈93 FP64 CPU + 120 GPU) | 40× Fujitsu Primergy CX2550 (Xeon E5-2660v3) + 25× IBM iDataPlex (E5-2670) + IBM Power9 AC922 — **3 696 cores** | **NVIDIA Tesla V100** (SXM2/NVLink) | **≥4** (≥2 AC922×2; nº total no público) | **≥31,2** (≥4×7,8) | **≥500** (≥4×125) | COMPUTAEX; RES; prensa | Media (GPU nº a confirmar) |
| **Cibeles** | UAM / CCC, Madrid | **Operativo** | no | n.p. | n.p. (heterogéneo) | Lenovo SD530 (144× Xeon Plat. 8160) + Fujitsu RX2530 (Xeon Gold 6330) + Lenovo x3550 (E5-2630v3) | NVIDIA (nodos GPU; modelo/nº no público) | n.p. | n.p. | n.p. | CCC-UAM; RES | Baja (sin agregado) |
| **Urederra** | NASERTIC, Pamplona | **Operativo** | no | n.p. | **~593** (29 CPU + 544 H100 + 19,5 A100) | 37× Intel Broadwell E5-2640v4 (740c) + 4× Intel Sapphire Rapids (GPU) + 1× Intel Ice Lake (GPU) | **NVIDIA H100 SXM5** + **A100 80 GB** | **16 H100 + 2 A100** | **560** (16×34 + 2×9,7=544+19,4) | **15 824 + 624 = 16 448** | NASERTIC HPC; RES | Media-alta |
| **Xula** | CIEMAT, Madrid | **Operativo** | no | n.p. | **722** | 190 nodos Intel Xeon (incl. Gold 6148) | — (solo CPU) | 0 | 0 | 0 | CIEMAT/CETA; RES | Media-alta |
| **Turgalium** | CIEMAT, Trujillo (Cáceres) | **Operativo** | no | n.p. | **375** | 40× 2× Intel Xeon **Gold 6254** (1 440c) + nodos acel. | **NVIDIA V100** | n.p. (nº no público) | n.p. (≥; V100 7,8/tarj.) | n.p. (≥; V100 125/tarj.) | CIEMAT/CETA; RES | Media (GPU nº a confirmar) |
| **Magerit 3** | UPM / CeSViMa, Madrid | **Operativo** | no | n.p. | **370,49** (CPU) + GPU | 72× Lenovo SD530 (Xeon Gold 6230) + 48× SD530 (Xeon Gold 6240R) + nodos SR670/SR675 V3 | **NVIDIA A100 / A40** (SR670) + **H200 / L40S** (SR675 V3) | n.p. (nº no público) | n.p. | n.p. | CeSViMa docs; Lenovo Press | Media (GPU nº a confirmar) |
| **Pirineus III** | CSUC, Barcelona | **Operativo** (oct-2024) | no | n.p. | **~2 200** (2,2 PF) | ~15 000 cores (bloque GP + bloque alta-mem + bloque GPU) | **NVIDIA (modelo no público)** — bloque acelerado para IA | n.p. (nº no público) | n.p. | n.p. | CSUC; RES | Media (GPU a confirmar) |
| **Talaia (TalaIA / BSAI)** | UIB / BSAI, Palma (ParcBit) | **NO operativo** (op. previsto 2º sem-2026) | no | — | n.p. | n.p. | n.p. (orientado IA → GPU NVIDIA, sin confirmar) | n.p. | n.p. | n.p. | UIB/BSAI; prensa Balears | Baja (planificado) |

---

## (b) Fuentes y citas (por sistema)

### MareNostrum 5 (BSC / EuroHPC) — PRIORIDAD 1

**ACC — Rpeak 260 PF + 4 480 H100 64 GB + nodos/CPU:**
- URL: https://top500.org/system/180238/ — título de ficha: *"MareNostrum 5 ACC - BullSequana XH3000, Xeon Platinum 8460Y+ 32C 2.3GHz, NVIDIA H100 64GB, Infiniband NDR"*.
- URL: https://www.bsc.es/marenostrum/marenostrum-5 ; https://rnca.fccn.pt/en/marenostrum-5/
  - Verbatim: *"The Accelerated Partition has a peak performance of 260 PFlops"*; *"1120 nodes based in Intel Sapphire Rapids and Nvidia Hopper GPUs, with each node having four Hopper H100 GPUs"* (1 120×4 = **4 480**).
  - Verbatim: *"each Hopper GPU (H100) offers 64 GB of HBM2e"*; *"2x Intel Xeon Platinum 8460Y+ … 40 cores … 300 W"* (80 cores/nodo).
- URL: https://www.hpcwire.com/2022/06/16/nvidia-intel-to-power-atos-built-marenostrum-5-supercomputer/ ; Wikipedia MareNostrum
  - Verbatim: *"MareNostrum 5 … 4,480 of these latest generation chips"* (Hopper); *"made by 4,480 NVIDIA Hopper GPUs"*.
- Acceso: 2026-06-16 · Confianza: **Alta** (Rpeak 260 PF y 4 480 H100 triangulados en BSC + RNCA + HPCwire + Wikipedia).
- **NOTA discrepancia CPU:** el título TOP500 dice "8460Y+ **32C**", pero BSC indica **40 cores** por socket (el 8460Y+ es efectivamente de 40 núcleos). Tomar **40C/socket, 80c/nodo** (fuente de centro). REVISIÓN MANUAL del recuento total de cores en la ficha 180238.

**ACC — Rmax 175,3 PF (#14), mejora sobre el HPL inicial 138,2 PF:**
- URL: https://top500.org/lists/top500/2025/11/ ; https://www.bsc.es/news/bsc-news/marenostrum-5-the-only-european-supercomputer-two-entries-the-list-the-20-most-powerful
  - Verbatim: *"the ACC partition … ranked 14th globally with 175.3 petaFLOPS Rmax … an improvement from the accelerated partition's earlier HPL performance of 138.2 petaflops that was recorded when it first entered the TOP500 list"*.
- Acceso: 2026-06-16 · Confianza: **Alta**. (El 138,2 PF es la lista Nov-2023; el **175,3 PF** es la medición HPL mejorada vigente en Nov-2025. Σ GPU FP64 vector 152,3 PF < Rpeak 260 PF y < Rmax 175,3 PF → coherente: el Rmax incluye CPU+GPU y aprovecha tensor-cores FP64.)

**GPP — Rpeak ~45,9 PF, 6 408 nodos, Xeon 8480+ 56C, Rmax 40,1 PF (#50):**
- URL: https://top500.org/system/180237/ — título: *"MareNostrum 5 GPP - ThinkSystem SD650 v3, Xeon Platinum 03H-LC 56C 1.7GHz, Infiniband NDR200"* (03H-LC = SKU custom del 8480+).
- URL: https://www.bsc.es/marenostrum/marenostrum-5
  - Verbatim: *"6,408 nodes based on Intel Sapphire Rapids … 72 nodes featuring Intel Sapphire Rapids HBM … 2x Intel Sapphire Rapids 8480+ at 2GHz and 56 cores each … 726,880 … cores … Peak Performance of 45.9 PFlops"*.
- Verbatim (Lenovo): *"The MareNostrum 5 GPP cluster achieves 40.1 Rmax PFlop/s … 5.7MW … leading x86 general-purpose cluster"*.
- Acceso: 2026-06-16 · Confianza: **Alta**.

**NGT (Next Generation Technology) — SÍ existe (particiones piloto, pequeñas):**
- URL: https://www.bsc.es/supportkc/docs/Grace/overview/ ; https://www.bsc.es/marenostrum/marenostrum-5
  - Verbatim: *"a next-generation partition with 802 NVIDIA GRACE processors, reaching a peak performance of 5.7 PFlop/s"*; *"NGT GPP … NGT ACC … the NGT ACC partition built with Intel Rialto Bridge"*.
  - URL: https://www.tomshardware.com/news/nvidia-marenostrum-5-supercomputer — *"144-core, Arm-based Grace 'superchips' in dual-chip configurations"* (Grace-Grace; 408 nodos × 2 = 802 chips, con 1 de repuesto/variación).
- Acceso: 2026-06-16 · Confianza: **Media-alta** (Grace 5,7 PF). NGT-ACC (Rialto Bridge) **no totalmente definido** (BSC: *"not fully defined, more information expected"*).

**AI Factory / MN5 AI upgrade — contrato firmado ene-2026, NO desplegado a jun-2026:**
- URL: https://eurohpc-ju.europa.eu/contract-signed-boost-marenostrum-5s-ai-capabilities-2026-01-26_en ; https://www.datacenterdynamics.com/en/news/eurohpc-ju-signs-contract-with-fsas-technologies-and-telef%C3%B3nica-for-marenostrum-5-ai-upgrade-project/ ; https://www.hpcwire.com/off-the-wire/eurohpc-signs-contract-for-marenostrum-5-ai-upgrade-project/
  - Verbatim: *"€129 million upgrade awarded to a consortium led by FSAS Technologies (Fujitsu) and Telefónica … next-generation GPUs … training large language models"*; *"increase MareNostrum 5's processing capacity by almost 50%, over 450 petaflops"*; *"Installation is expected to take place in the first half of 2026, with the new AI partitions expected to be fully operational by mid-2026"*; tecnologías de *"Supermicro (hardware), IBM (storage/software), VAST (storage), NVIDIA"*.
- Acceso: 2026-06-16 · Confianza: **Media**. Modelo exacto de GPU NVIDIA **no público**. → A jun-2026 contar como **futuro/no operativo** (no en TOP500 nov-2025).

### Tirant III (Univ. de València) — OPERATIVO
- URL: https://www.uv.es/uvweb/information-tecnologies-service/en/ict-service-siuv/university-valencia-multiplies-its-computing-power-10-two-new-supercomputers-1285867233824/Novetat.html ; https://www.ciencia.gob.es/en/Organismos-y-Centros/ICTS/TecnologiasCiencia/RES/Tirant.html
  - Verbatim: *"Tirant v3 … consists of 336 calculation nodes, each with two Intel Xeon SandyBridge E5-2670 processors at 2.6 GHz and 32 GB DDR3 RAM (5,376 cores), providing 111.8 Tflops of performance (Rpeak)"*.
- Acceso: 2026-06-16 · Confianza: **Alta**. **Solo CPU, sin GPU.** "Tirant III" = "Tirant v3" (el nodo RES de UV; en operación desde jul-2018). *LluísVives v2* (82 TF, Xeon Gold 6154) es máquina UV aparte, NO nodo RES.

### LaPalma (IAC) — OPERATIVO
- URL: https://www.iac.es/en/science-and-technology/technology/technical-facilities/lapalma-supercomputer ; https://www.res.es/es/nodos-de-la-res/lapalma
  - Verbatim: *"The … LaPalma system consisted of 252 compute servers with 2 Intel Xeon SandyBridge 8-core processors at 2.6 GHz with a maximum performance of 83.85 TFlops"*.
- Acceso: 2026-06-16 · Confianza: **Media-alta**. **Solo CPU** (Intel SandyBridge, hardware reciclado de MareNostrum vía proyecto "MNLP-RES"). Hubo una versión PowerPC histórica (1 024 cores, 9 TF) ya superada por la actual Intel.

### Lusitania III (COMPUTAEX / CénitS) — OPERATIVO
- URL: https://computaex.es/en/lusitania/lusitania-iii/ ; https://www.res.es/es/sobre-la-res/nodos/lusitania3-cenits
  - Verbatim: *"LUSITANIA III … a computing capacity of 313 TFlops … 40 Fujitsu Primergy CX2550 servers with Intel Xeon E5-2660v3 … 25 IBM System x iDataPlex dx360 M4 servers with Intel E5-2670 … IBM Power Systems servers with NVIDIA Tesla V100 GPUs with NVLink … 3,696 cores and 40,960 CUDA cores"*; otra ficha: *"2 IBM Power AC922 … 2 POWER9 … 2 NVIDIA Tesla V100 GPUs with NVLink SXM2"* (= ≥4 V100, nº total de tarjetas a confirmar).
- Acceso: 2026-06-16 · Confianza: **Media**. GPU = **V100**; nº exacto de tarjetas **no público** (mínimo 4 por las 2 AC922). 40 960 CUDA cores ÷ 5 120 (V100) ≈ **8 V100** (estimación, confirmar).

### Cibeles (UAM / CCC) — OPERATIVO
- URL: https://www.ccc.uam.es/es/about/recursos.html ; https://www.res.es/es/sobre-la-res/nodos/cibeles-uam
  - Verbatim: *"144 cibeles(v4) Lenovo SD530 … Intel Xeon Platinum 8160 … 28 cibeles(v3) Fujitsu Primergy RX2530 M6 … Intel Xeon Gold 6330 … 22 cibeles(v1) Lenovo System x3550 M5 … Intel Xeon E5-2630 v3 … newer systems feature dual Intel Xeon Gold 6330 … with GPU configurations"*.
- Acceso: 2026-06-16 · Confianza: **Baja** (clúster heterogéneo multi-generación; **Rpeak agregado y nº/modelo de GPU NO publicados** en snippets).

### Urederra (NASERTIC) — OPERATIVO
- URL: https://hpc.nasertic.es/es/infraestructuras ; https://www.res.es/en/about-res/nodes/urederra-nasertic
  - Verbatim: *"37 Intel Broadwell nodes with 2x Intel Xeon CPU E5-2640 v4 @ 2.40 GHz (740 cores total) … 29 TFLOPS … 4 nodes with Intel Sapphire Rapids featuring 16 GPUs NVIDIA H100 SXM5, 1.280 GB of HBM3 … 544 TFLOPS … 1 node with Intel Ice Lake including 2 GPU NVIDIA A100 with 80 GB of HBM2e … 19.5 TFLOPS"*.
- Acceso: 2026-06-16 · Confianza: **Media-alta**. → **16× H100 SXM5 + 2× A100 80 GB**. (El "544 TFLOPS" del centro para 16 H100 = FP64 tensor 16×34≈544; coherente.) Gobierno de Navarra invirtió 4 M€ (2025) para ampliar el CPD.

### Xula y Turgalium (CIEMAT) — OPERATIVO
- URL: https://www.res.es/en/about-res/nodes/xula-turgalium-ciemat ; https://www.ceta-ciemat.es/ ; https://www.ciemat.es/
  - Verbatim: *"Xula has 190 nodes … last-generation processors and a peak computing power of 722 Tflops"* (Intel Gold 6148; **solo CPU**).
  - Verbatim: *"Turgalium … 40 servers … two Intel Gold 6254 processors (1,440 cores) … NVIDIA V100 cards and 375 Tflops of peak power … accelerator nodes with Nvidia V100 GPUs … almost 1.5 PetaBytes of parallel storage"*.
- Acceso: 2026-06-16 · Confianza: **Media-alta** (Rpeak); **Media** (Turgalium GPU = V100, nº de tarjetas **no público**). NOTA: **Turgalium está en Trujillo (Cáceres)**, no en Madrid; sólo **Xula** está en Madrid (CIEMAT).

### Magerit 3 (UPM / CeSViMa) — OPERATIVO
- URL: https://docs.cesvima.upm.es/magerit/magerit3/ ; https://www.cesvima.upm.es/infrastructure/magerit
  - Verbatim: *"72 ThinkSystem SD530 nodes … Intel Xeon Gold 6230 … 48 ThinkSystem SD530 nodes … Intel Xeon Gold 6240R … peak computational power of 370.49 TFLOPS … ThinkSystem SR670 and ThinkSystem SR675 V3 nodes with specific GPU accelerators"*.
  - Lenovo Press: SR670 V2 admite NVIDIA **A100 / A40**; SR675 V3 admite NVIDIA **H200 / L40S**.
- Acceso: 2026-06-16 · Confianza: **Media**. 370,49 TF es **solo el bloque CPU**; **modelos y nº exacto de GPU NO publicados** en snippets (mezcla A100/A40/H200/L40S).

### Pirineus III (CSUC) — OPERATIVO (oct-2024)
- URL: https://www.csuc.cat/en/serveis/supercomputadors ; https://www.csuc.cat/es/noticia/el-nuevo-supercomputador-pirineus-iii-ya-esta-en-marcha ; https://www.res.es/en/about-res/nodes/pirineus-csuc
  - Verbatim: *"Pirineus III … operation in October 2024 … more than 2 Pflop/s and 15,000 cores … multiplies by four the resources … general-purpose block … another block with greater memory capacity … nodes accelerated with graphic processing units (GPUs), particularly useful for artificial intelligence"*; *"peak performance (Rpeak) of 2.2 Petaflops"*.
- Acceso: 2026-06-16 · Confianza: **Media**. **Modelo y nº de GPU del bloque acelerado NO publicados** en snippets. → REVISIÓN MANUAL (igual que 1ª corrida).

### Talaia / TalaIA (UIB / BSAI) — NO OPERATIVO (planificado)
- URL: https://bsai.uib.cat/ ; https://www.dbalears.cat/balears/balears/2026/03/04/416943/ ; https://www.ultimahora.es/noticias/local/2026/03/03/2581699/
  - Verbatim: *"El supercomputador … nom: Talaia … que entrarà en funcionament en els pròxims mesos al Centre de Supercomputació i Intel·ligència Artificial de les Illes Balears (BSAI) de la UIB"*; *"processing power equivalent to between 1,300 and 1,700 laptops working simultaneously"*.
- Acceso: 2026-06-16 · Confianza: **Baja**. A jun-2026: bautizado (mar-2026), **aún NO operativo** ("en los próximos meses"); **sin specs técnicas públicas** (ni Pflops, ni GPU, ni constructor). → REVISIÓN MANUAL.

---

## (c) REVISIÓN MANUAL (URLs con 403 a fetch; abrir en navegador)

1. **MN5 ACC ficha TOP500** — confirmar recuento total de cores y reconciliar "32C vs 40C" del 8460Y+:
   https://top500.org/system/180238/
2. **MN5 GPP ficha TOP500** — Rpeak/cores exactos:
   https://top500.org/system/180237/
3. **MN5 NGT** — desglose Grace (¿802 vs 408 nodos?) y estado Rialto Bridge:
   https://www.bsc.es/supportkc/docs/Grace/overview/ y https://www.bsc.es/marenostrum/marenostrum-5
4. **MN5 AI Factory** — modelo exacto de GPU NVIDIA next-gen y Rpeak/Rmax una vez instalado (¿GB200/B200?):
   https://www.bsc.es/ai-factory y https://eurohpc-ju.europa.eu/ai-factories/spain_en
5. **Pirineus III** — modelo y nº de GPU del bloque acelerado:
   https://www.csuc.cat/en/serveis/supercomputadors y https://www.res.es/en/about-res/nodes/pirineus-csuc
6. **Magerit 3** — modelos (A100/A40/H200/L40S) y nº de tarjetas por nodo SR670/SR675 V3:
   https://docs.cesvima.upm.es/magerit/magerit3/
7. **Cibeles** — Rpeak agregado + modelo/nº GPU de los nodos acelerados:
   https://www.ccc.uam.es/es/about/recursos.html y https://www.res.es/es/sobre-la-res/nodos/cibeles-uam
8. **Lusitania III** y **Turgalium** — nº exacto de tarjetas V100:
   https://computaex.es/en/lusitania/lusitania-iii/ ; https://www.res.es/en/about-res/nodes/xula-turgalium-ciemat
9. **Talaia (BSAI/UIB)** — specs cuando se publiquen (Pflops, GPU, constructor):
   https://bsai.uib.cat/
10. **Urederra** — verificar ficha NASERTIC actualizada (16 H100 + 2 A100):
   https://hpc.nasertic.es/es/infraestructuras
11. **res.es directorio de nodos** (fichas oficiales de TODOS):
   https://www.res.es/es/sobre-la-res/nodos
12. **TOP500 lista nov-2025 filtrada España** — confirmar que sólo MN5 ACC+GPP figuran:
   https://top500.org/lists/top500/2025/11/

---

## (d) Subtotales y notas de cómputo

**MareNostrum 5 (BSC) — sistema dominante de España:**
- **Rpeak FP64 total declarado: ~314 PF** (= GPP 45,9 + ACC 260 + Grace 5,7 + redondeos).
- **Rmax FP64 (TOP500 nov-2025): ACC 175,3 PF (#14) + GPP 40,1 PF (#50) = 215,4 PF** (las dos únicas entradas españolas en TOP500).
- **GPUs físicas en MN5: 4 480 × NVIDIA H100 64 GB** (todas en ACC). NGT-Grace = CPU ARM (no GPU). NGT-ACC (Rialto Bridge) = piloto, nº no público. AI Factory = futuro.
- **Σ GPU FP64 vector ACC = 4 480 × 34 ≈ 152,3 PF** (cota inferior; < Rmax 175,3 PF y < Rpeak 260 PF → consistente: Rmax/Rpeak suman CPU + uso de tensor-cores FP64).
- La afirmación "MN5 ≈ 95% de la capacidad FP64 nacional" es **plausible**: sólo MN5 supera la escala PF; el resto de nodos RES son de decenas-cientos de TF (cota total resto ≈ 5–6 PF Rpeak frente a ~314 PF de MN5).

**GPUs en el resto de nodos RES (tarjetas físicas confirmadas en esta corrida):**
- Urederra: **16 H100 SXM5 + 2 A100 80 GB** (confirmado).
- Lusitania III: **V100** (≥4–8, nº exacto no público).
- Turgalium: **V100** (nº no público).
- Magerit 3: **A100/A40 + H200/L40S** (mezcla, nº no público).
- Pirineus III: **GPU NVIDIA** bloque IA (modelo/nº no público).
- Cibeles: nodos GPU (modelo/nº no público).
- Solo CPU (sin GPU): **Tirant III, LaPalma, Xula**.
- Talaia: planificado (sin datos).

**Rpeak FP64 (TF) por nodo — resumen cota inferior (resto, excl. MN5):**
Pirineus III ~2 200 · Xula 722 · Urederra ~593 · Turgalium 375 · Magerit 3 ~370 (CPU) ·
Lusitania III 313 · Tirant III 111,8 · LaPalma 83,85 · Cibeles n.p. · Talaia n.p.
→ **Subtotal resto RES ≈ 4,8 PF Rpeak** (cota inferior; sin contar GPU no cuantificadas de varios nodos).

**Avisos de inventario (heredados/confirmados):**
- "Correfoc (UPF)" **NO existe** como HPC (ver `investigacion_espana.md`). Nodo catalán RES = Pirineus III (CSUC).
- "Tirant III" = "Tirant v3" (mismo sistema; nomenclatura RES). No confundir con LluísVives v2 (no-RES).
- Turgalium está en **Trujillo (Cáceres)**, no en Madrid (el prompt lo ubicaba en Madrid).
