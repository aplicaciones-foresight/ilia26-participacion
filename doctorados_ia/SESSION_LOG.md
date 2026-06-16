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
| Portugal (PT) | 9 | ✅ COMPLETO | 6 | 2 | 1 |
| España (ES) | 38 | ✅ COMPLETO (norm.+valid.) | 20 | 17 | 1 |
| Alemania (DE) | 49 | ✅ COMPLETO (valid.) | 19 | 29 | 1 |
| **TOTAL** | **103/103** | ✅ | **49** | **51** | **3** |

> **Tras ronda de validación (2026-06-16):** UEM NO→PARCIAL; Potsdam PARCIAL→CUMPLE;
> UCAM PARCIAL confirmado; Católica/IE/Hohenheim NO CUMPLE confirmados; Estonia
> universo confirmado (TalTech #635, Tallinn U 1001–1200). Entregables en
> `entregables/` (planilla `.xlsx` + informe `.docx`), generados por
> `build_entregables.py` desde `clasificacion.csv`.

> **Forman competencias en IA (CUMPLE+PARCIAL) = 99/103.** Conteo estricto (sólo
> CUMPLE) = 48. Ver `RESUMEN.md`. ES/DE se hicieron con agentes `general-purpose`;
> España se **normalizó** a la regla `CUMPLE ⟺ C1 ∧ (C2=Sí ∨ C3=Sí)` (12 casos
> CUMPLE→PARCIAL). Alemania ya venía conforme a la regla.

Entregables ya escritos: `paises/estonia.md`, `paises/singapur.md`,
`paises/portugal.md`, `clasificacion.csv` (16 filas),
`universidades_qs2026.csv` (16 filas).

> **Forman competencias en IA (CUMPLE+PARCIAL) hasta ahora = 15/16.**

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
1. ✅ **Portugal (9)** — hecho.
2. ⏳ **España (38)** — **lanzado a un agente** `general-purpose` (escribe
   `paises/espana.md` + devuelve filas CSV). Pendiente: fusionar filas al
   `clasificacion.csv` + `universidades_qs2026.csv` y commit.
3. ⏳ **Alemania (49)** — **lanzado a un agente** (escribe `paises/alemania.md` +
   devuelve filas CSV). Mismo merge pendiente.
4. Consolidar: actualizar CSVs, completar `DUDAS_ACCESO_MANUAL.md` (sección D) y
   escribir `RESUMEN.md` (conteos por país y total: CUMPLE, PARCIAL, suma).

> `DUDAS_ACCESO_MANUAL.md` ya creado con EE/SG/PT (secciones A–C).

> **Opción de aceleración:** si el presupuesto de `WebSearch` lo permite, lanzar
> agentes `general-purpose` en paralelo (uno por banda de rank de ES/DE) con la
> metodología + esquema de salida. Riesgo: comparten el límite de búsqueda.

## Reglas de conteo (recordatorio, ver METODOLOGIA §6.3)
Reportar SIEMPRE: `n_CUMPLE`, `n_PARCIAL`, y `n_CUMPLE+PARCIAL`. La decisión de
si el indicador publicado usa sólo CUMPLE o CUMPLE+PARCIAL es **del operador**.
