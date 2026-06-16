# SESSION_LOG — Indicador "Programas de doctorado de IA" (países extra)

**Indicador:** cantidad de programas de doctorado que forman competencias en IA,
en 5 países de referencia (DE, ES, PT, SG, EE). Metodología completa en
`METODOLOGIA.md`. **Idioma:** es.

## Restricciones del entorno (críticas)
- **Sin salida de red directa:** `WebFetch`/`curl` → HTTP 403 contra todo dominio.
- **Sólo `WebSearch`** (proxy): da títulos + snippets + URLs, **no** páginas
  completas. Impacto: C3 (≥3 cursos del plan) normalmente NO verificable → muchos
  casos europeos caen en **PARCIAL** + marca `requiere_acceso_manual`.
- **`WebSearch` tiene límite de sesión** (se agotó una vez; se repuso). Estrategia:
  pocas búsquedas por turno, **commit por país** para no perder avance.

## Estado de avance
| País | Universos QS 2026 | Estado | CUMPLE | PARCIAL | NO CUMPLE |
|---|---|---|---|---|---|
| Estonia (EE) | 3 | ✅ COMPLETO | 0 | 3 | 0 |
| Singapur (SG) | 4 | ✅ COMPLETO | 4 | 0 | 0 |
| Portugal (PT) | 9 | ⏳ pendiente | – | – | – |
| España (ES) | 38 | ⏳ pendiente | – | – | – |
| Alemania (DE) | 49 | ⏳ pendiente | – | – | – |
| **Total** | **103** | **7/103** | **4** | **3** | **0** |

Entregables ya escritos: `paises/estonia.md`, `paises/singapur.md`,
`clasificacion.csv` (7 filas), `universidades_qs2026.csv` (7 filas).

## Datos QS 2026 ya confirmados para países pendientes (no perder)
**Portugal (9):** Lisboa (#230), Porto (#237), NOVA Lisboa (#327), Coimbra,
Aveiro, Minho, ISCTE-IUL (#711–720), U. Católica Portuguesa (#781–790), Algarve
(#1001–1200). Fuente: `clsbe.lisboa.ucp.pt/news/qs-world-university-rankins-2026-portugal-nine-universities-among-best-world`; `up.pt/portal/en/explore/about-uporto/rankings/`. *(Confirmar ranks de Coimbra/Aveiro/Minho.)*

**España (38 = 31 públicas + 7 privadas).** Confirmadas: U. de Barcelona (#160),
UAM (#206), UAB, UCM, UPF, U. Navarra, UC3M, UPM, UPC. Debuts 2026: U. Europea de
Madrid (#901–950), U. Jaume I (#1001–1200), UCAM (#1201–1400). Fuentes:
`uam.es/uam/en/noticias/ranking-qs-world-university-2026`;
`upc.edu/ranquings/.../nota-de-premsa-qs-wur-2026.pdf`;
`prnewswire.com/news-releases/clasificacion-mundial-de-universidades-qs-2026-302485797.html`.
*(Falta enumerar las ~26 restantes — hacer por bandas de rank.)*

**Alemania (49).** Confirmadas top: TU München (#22), LMU München (#58),
Heidelberg (#80), FU Berlin (#88), KIT (#98), U. Freiburg (~top-10 DE). Fuentes:
`uni-freiburg.de/en/qs-world-university-rankings-europe-2026-...`;
`learngermanonline.org/top-german-universities/` (403 a fetch; sólo vía search);
`msingermany.com/blog/germany-qs-world-ranking`.
*(Falta enumerar las ~43 restantes — hacer por bandas de rank.)*

## Plan de continuación (orden sugerido)
1. **Portugal (9)** — lista casi cerrada; clasificar las 9. Ojo: ISCTE y Católica
   son más de gestión, pero evaluar sus escuelas de tecnología/ciencia de datos
   (no excluir la universidad entera; excluir sólo programas de Negocios/Economía).
2. **España (38)** — enumerar por bandas de rank y clasificar. Candidatas fuertes
   a CUMPLE: UPC, UPM, UPV (politécnicas, con coursework), UGR, UAM, UC3M.
3. **Alemania (49)** — enumerar por bandas; mayoría *research-based* → muchas
   PARCIAL; excepciones con escuelas doctorales estructuradas (TUM, RWTH, KIT,
   Saarland, Tübingen-IMPRS, etc.).
4. Consolidar: actualizar `clasificacion.csv` + `universidades_qs2026.csv`,
   escribir `RESUMEN.md` (conteos por país y total: CUMPLE, PARCIAL, suma) y
   `DUDAS_ACCESO_MANUAL.md` (lista priorizada de verificación manual).

> **Opción de aceleración:** si el presupuesto de `WebSearch` lo permite, lanzar
> agentes `general-purpose` en paralelo (uno por banda de rank de ES/DE) con la
> metodología + esquema de salida. Riesgo: comparten el límite de búsqueda.

## Reglas de conteo (recordatorio, ver METODOLOGIA §6.3)
Reportar SIEMPRE: `n_CUMPLE`, `n_PARCIAL`, y `n_CUMPLE+PARCIAL`. La decisión de
si el indicador publicado usa sólo CUMPLE o CUMPLE+PARCIAL es **del operador**.
