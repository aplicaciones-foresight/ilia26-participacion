# Indicador HPC — resultados (5 países extra) · cota inferior · 2026-06-16

Generado por `src/hpc_calc.py` desde `sistemas_consolidado.csv` (50 sistemas; estado
operativo a jun-2026; TOP500 nov-2025). **Cifras = cota inferior verificable.**
Población: `poblacion.csv` (DE 83,58 M · ES 49,08 M · PT 10,75 M · EE 1,37 M · SG 6,04 M).

## Las 3 variables oficiales (per cápita salvo V1 absoluta)

| País | V1 Capacidad HPC (TF) | **V1 TF/Mhab** | V2 nGPU | **V2 GPU/Mhab** | **V3 GPU TF/Mhab (FP64)** | V3 GPU TF/Mhab (FP16-IA) |
|---|--:|--:|--:|--:|--:|--:|
| Alemania | 1.664.798 | 19.919 | 36.397 | 435 | 12.592 | 347.383 |
| Singapur | 170.000 | **28.160** | 2.548 | 422 | **12.901** | **377.059** |
| España | 330.748 | 6.739 | 4.880 | 99 | 3.255 | 95.002 |
| Portugal | 10.402 | 968 | 158 | 15 | 139 | 4.417 |
| Estonia | 943 | 687 | 90 | 66 | 687 | 16.962 |

### Rankings per cápita (lo que mide el indicador)
- **V1 capacidad/Mhab:** Singapur (28.160) > Alemania (19.919) > España (6.739) > Portugal (968) > Estonia (687).
- **V2 GPUs/Mhab:** Alemania (435) ≈ Singapur (422) > España (99) > Estonia (66) > Portugal (15).
- **V3 GPU TF/Mhab (FP64):** Singapur (12.901) ≈ Alemania (12.592) > España (3.255) > Estonia (687) > Portugal (139).
- **V3 en FP16/BF16 (IA):** Singapur (377k) > Alemania (347k) > España (95k) > Estonia (17k) > Portugal (4,4k).

## Sistemas dominantes (concentración)
| País | Sistema dominante | Cuota del Rpeak nacional |
|---|---|---|
| Alemania | JUPITER Booster (1,23 EF) | 74% |
| España | MareNostrum 5 ACC (260 PF) | 79% |
| Portugal | Deucalion (10 PF) | 96% |
| Estonia | Rocket / UTHPC | 81% |
| Singapur | ASPIRE 2B (115 PF) | 68% |

## Caveats CRÍTICOS (leer antes de usar)
1. **Convención de var.3 = FP64 vector** (cota inferior). Con FP64 *Tensor Core* se ~duplica para
   GPUs NVIDIA; la columna **FP16/BF16** (IA) es la métrica relevante para un índice de IA y va aparte.
2. **Singapur lidera V1/Mhab por ASPIRE 2B** (115 PF, lanzado 8-jun-2026). La **precisión de los
   "115 PF" no está confirmada** (probable FP64-Tensor Core o mixto IA, no vector). Si fuese una
   cifra de IA, V1 de Singapur **bajaría mucho**. → verificación manual prioritaria.
3. **Estonia: V1 = piso por GPU.** Ningún centro estonio publica Rpeak FP64 actual → se usa la suma
   FP64 de GPU como piso (por eso V1 = V3 en Estonia). La cifra real es algo mayor (CPU no contada).
   Además, la **ampliación feb-2026** de Tartu (164 GPU agregadas, incl. 24 B200) **no** está en el
   conteo conservador (90 GPU); si se cuenta nube/K8s, Estonia sube fuerte en per-cápita.
4. **Alemania: JUPITER domina** (74%); el resto del parque investigado (GCS+NHR+investigación,
   ~24 sistemas) suma ~0,44 EF, < 40% del Booster. Varios Rpeak de Tier-2 son **estimados**.
5. **Subestimación por cómputo comercial/privado excluido** (regla 3.3): material en **Singapur**
   (un operador, SMC, declara hasta 4.000 H100 — más que todo ASPIRE 2A+2A+) y **Alemania**
   (Telekom-NVIDIA, IONOS, Schwarz/StackIT, Northern Data, OEMs). La capacidad real instalada es mayor.
6. **EuroHPC atribuido al país anfitrión** (JUPITER→DE, MN5→ES, Deucalion→PT). Cofinanciación UE.
7. **LUMI excluido** de Estonia (está en Finlandia; solo cuota). No imputado.
8. **Acceso a fuentes degradado (HTTP 403):** muchas cifras vienen de extractos de buscador → ver
   listas de "REVISIÓN MANUAL" por país en `raw/investigacion_*.md` (URLs exactas a abrir).

## Pendiente / revisión manual (mayores)
- **ASPIRE 2B**: precisión de 115 PF; nº exacto H200. **MN5 ACC**: reconciliar 32C vs 40C (no afecta GPU).
- **España GPU sin nº público:** Pirineus III, Magerit 3, Turgalium, Cibeles, Lusitania III (V100 nº).
- **Alemania:** rank/Rmax exactos nov-2025 de NHR; nº H100/H200 de HoreKa/Helma/fortythree; Otus, Maxwell, Vulcan; Tier-3 (~30) no investigado.
- **Portugal:** Oblivion, Orion, Cirrus-A, Stratus (placeholder, no suman).
- **Estonia:** Rpeak FP64 real; nº exacto V100 de Rocket; desglose de las 164 GPU (feb-2026).

## Decisiones abiertas (parametrizadas en `src/hpc_calc.py`)
- var.3 FP64 vector (actual) | FP64 Tensor-Core | FP16/BF16 (IA).
- var.1 per cápita y/o absoluta (se reportan ambas).
- Cobertura `all_published` (actual) | `top500_only`.
- Estonia: clúster Slurm (actual) | centro completo (nube/K8s).
- EuroHPC: capacidad íntegra del anfitrión (actual) | prorrateo por cuota.
- Población: unificar a Banco Mundial 2024.
