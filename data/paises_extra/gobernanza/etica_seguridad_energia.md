# Gobernanza ILIA 2026 — IA Ética/Segura + Sustentabilidad (EE/SG)

## GIRAI (Global Index on Responsible AI), 1ª edición 2024 — fuente: https://www.global-index.ai
| Subindicador (0–100) | Estonia | Singapur |
|---|---|---|
|138 Protección de datos y privacidad | **NO ENCONTRADO** | **NO ENCONTRADO** |
|139 Seguridad, precisión y confiabilidad | **NO ENCONTRADO** | **NO ENCONTRADO** |

- Ambos países **están cubiertos** por GIRAI (138 países). Agregado de Singapur: score global **53,77**; actores no estatales 40,09. Promedio global del índice 19,8; líder Países Bajos.
- ❌ Los puntajes **por área temática** se renderizan en el portal JS / figuras PDF (no indexados) → no extraíbles por búsqueda.
- **Ruta manual:** https://www.global-index.ai → "Explore the data" → país → dimensión "Human rights and AI" › área "Data protection and privacy"; dimensión "Responsible AI governance" › área "Safety, accuracy and reliability". Alternativa Singapur: informe LIRNEasia "Responsible AI in Asia", Fig. 19 (p.21): https://lirneasia.net/wp-content/uploads/2025/03/Draft-Version-for-Review_GIRAI-Report_LIRNEasia_20-March-2025.pdf

## NRI — "Affordable & clean energy" (SDG 7, pilar Impact) — fuente: https://networkreadinessindex.org (ed. 2025)
| Subindicador (144) | Estonia | Singapur |
|---|---|---|
| Energía limpia y asequible (score) | **80,71** (80,7064) | **86,87** (86,8722) |

- NRI 2025 totales (contexto): Estonia rank 18 (67,85); Singapur rank 3 (75,46). Confianza MEDIA-ALTA (leído de la página país, ed. 2025). Rank puntual del subindicador: no obtenido.
- Páginas país: https://networkreadinessindex.org/country/estonia/ · /country/singapore/

## % ERNC en matriz eléctrica (145) — fuente EMBER (vía OWID, determinístico)
| País | Renovables % generación | Año |
|---|---|---|
| Estonia | **55,75 %** | 2024 |
| Estonia | **59,57 %** | 2025 |
| Singapur | **4,93 %** | 2024 |
| Singapur | **5,49 %** | 2025 |

- **Verificación determinística:** renovables_electricity / electricity_generation cuadra exacto con el share publicado (Estonia 2024: 3,49/6,26 TWh = 55,75 %; Singapur 2024: 2,94/59,61 = 4,93 %). Datos: https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-data.csv
- **ERNC ≈ renovables totales** (hidro Estonia ~0,5 %, Singapur 0 %). EMBER **no** separa "no convencional" ni excluye gran hidro (efecto marginal aquí).
- ⚠️ Un agente reportó "~63 %" para Estonia 2024: **descartado** (lectura imprecisa; el cálculo desde TWh da 55,75 %). Si quieres el decimal del último release exacto de EMBER, confírmalo en su explorer: https://ember-energy.org/data/electricity-data-explorer/ (Estonia importa ~⅓ del consumo → no confundir share de *generación* con share de *consumo*).
