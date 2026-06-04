# Pasada de descubrimiento web — Fase 1 (rondas 1 y 2)

**Fecha:** 2026-06-04 · **Pipeline ILIA 2026 — Participación Ciudadana** · Universo: 20 países (incl. TT)

> Búsqueda en vivo por canales A.1–A.10 con **11 investigadores paralelos**:
> 6 por bloque regional (ronda 1) + 5 temáticos transversales (ronda 2:
> herramientas deliberativas, literatura académica, multilaterales/aceleradoras,
> subnacional/presupuestos, barrido de países flacos). Los resultados son
> **candidatos** (señales) para el Gate 1 y la Fase 2; la prensa solo genera
> candidato (regla anti-paywall). La curación final vive en
> `data/candidatos/hallazgos_web.csv` y la fusiona `discover.py`.

## 1. Directorio de medios (canal A.10 — Anexo B parcial)

`data/baseline/directorio_medios.csv`: **60 medios, 20/20 países** (2-3 por país,
con tipo y relevancia). Cubre el insumo del canal A.10 que faltaba del Anexo B.
A.11 (instituciones de participación por país) sigue pendiente del Anexo B.

## 2. Candidatos NUEVOS (no estaban en el baseline 2025) — 11

| País | Candidato | Canal | Fuente | Tipo |
|---|---|---|---|---|
| MX | Guanajuato Inteligente 2024-2030 | A.5 | prensa | nuevo |
| CO | Citibeats + PNUD (deliberación juvenil) | A.9 | institucional | nuevo |
| BR | Brasil Participativo — clustering BERTopic+LLM (10.186 propuestas) | A.4 | académico | nuevo |
| BR | e-Cidadania — IA matching de ideas legislativas (ene-2026, conf. IPU) | A.5 | institucional | nuevo |
| BR | São Paulo — Programa de Metas / Participe Mais (Gemini, 6.368 prop.) | A.6 | institucional | nuevo |
| BR | 5ª Conferência Nacional de CT&I — sistematización con IA | A.5 | institucional | nuevo |
| PA | Mansa Idea (Pacto del Bicentenario) | A.8 | prensa | nuevo |
| CL | LXS 400 — Chile Delibera | A.3 | institucional | nuevo |
| BR | OPA Piauí — Presupuesto Participativo Digital | A.5 | prensa | **dudoso** |
| TT | EngageTT (Go Vocal) | A.5 | institucional | **dudoso** |
| VE | Plan de la Patria 7 Transformaciones (IA + Big Data) | A.5 | prensa | **dudoso** |

**8 sólidos + 3 dudosos.** Brasil concentra los hallazgos más fuertes (4). Los
dudosos requieren confirmar en Fase 2 que la IA opera sobre el **contenido** de
los aportes (no logística/convocatoria/afirmación no verificada).

## 3. Reverificaciones del baseline con señal de actividad 2025-2026 — 11

Reconfirmados por canal institucional adicional (en `candidatos.csv` con
`canal_origen = "A.0; A.x"` y `flag_canal_unico=0`): BO Bolivia Conversa ·
BR e-Cidadania (audiencias) · BR PPA Natal (nueva edición 2026-2029) ·
CO ECHO-HáblameD · CO Chatico (Plan Distrital 2024-2028, citado por OCDE/OPSI) ·
CR dIAra (OGP 2025) · CR U-Report · DO CiudadanIA · EC PAGA IA (Plan 2025-2027) ·
GT Guatemala Joven Conversa · HN RedPública+iVerify.

## 4. Hallazgos por canal y exclusiones

- **Herramientas deliberativas (A.7):** NO se hallaron despliegues verificados de
  Pol.is, Talk to the City, Remesh, Make.org, Common Ground ni Jigsaw en los 20
  países (2024-2025). Go Vocal/CitizenLab en Chile es de 2019 sin IA-clustering
  confirmada; en TT (EngageTT) la activación de la IA está por verificar.
- **Excluidos por criterio (muy frecuente):** consultas **SOBRE IA** sin IA en su
  proceso (estrategias/ENIA nacionales en AR, UY, CL, EC, GT, DO, CU, PY, TT, JM);
  chatbots de **atención/FAQ** (Anansi TT, CXGenies DO, etc.); **conteo/integridad
  electoral** (firmes: MX Sufragio Seguro, PE ONPE); **civic-tech sin IA** o
  votación entre opciones cerradas; papers **puramente teóricos** sin caso desplegado.

## 5. Vacíos (cobertura honesta)

- **Sin ningún candidato (solo placeholder):** CU, JM, SV.
- **Sin caso nuevo elegible** (más allá del baseline o de dudosos): AR, UY, PY, PE
  (el caso baseline de PE requiere verificación de fuente primaria del CNE).
- La región sigue rezagada en este vector específico; Brasil y, en menor medida,
  Colombia y México concentran la práctica con IA sobre el contenido de aportes.

## 6. Próximos pasos

1. **Gate 1 (humano)** sobre `candidatos.csv` (91 filas): aprobar qué pasa a Fase 2.
2. **Fase 2 (doble pasada)** priorizando los 11 nuevos/dudosos; confirmar con
   evidencia verbatim que la IA opera sobre el contenido de los aportes.
3. Conseguir el **Anexo B** para completar A.11 (instituciones por país).
4. Verificaciones directas pendientes: São Paulo (uso operacional), Brasil
   Participativo (adopción oficial vs investigación), VE Plan de la Patria
   (fuente estatal), TT EngageTT (IA de Go Vocal activa).
