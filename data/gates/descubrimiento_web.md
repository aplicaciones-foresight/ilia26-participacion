# Pasada de descubrimiento web — Fase 1 (ronda 1)

**Fecha:** 2026-06-04 · **Pipeline ILIA 2026 — Participación Ciudadana** · Universo: 20 países (incl. TT)

> Búsqueda en vivo por canales A.1–A.10, ejecutada con investigadores paralelos
> por bloque regional. Los resultados son **candidatos** (señales) para el Gate 1
> y la Fase 2; la prensa solo genera candidato (regla anti-paywall). La
> **ronda 2** (temática transversal) está en curso y añadirá más hallazgos.

## 1. Directorio de medios (canal A.10 — Anexo B parcial)

`data/baseline/directorio_medios.csv`: **60 medios, 20/20 países** (2-3 por país,
con tipo y relevancia). Cubre el insumo del canal A.10 que faltaba del Anexo B.
A.11 (instituciones de participación por país) sigue pendiente del Anexo B.

## 2. Candidatos NUEVOS (no estaban en el baseline 2025)

| País | Candidato | Canal | Fuente | Señal (resumen) |
|---|---|---|---|---|
| MX | Guanajuato Inteligente 2024-2030 | A.5 | prensa | IA analiza 26.000+ aportes de talleres regionales para identificar patrones del plan de gobierno. |
| CO | Citibeats + PNUD (deliberación juvenil) | A.9 | institucional | IA agrupa en tiempo real opiniones/propuestas de deliberación pública y clasifica tópicos. |
| BR | Brasil Participativo — clustering PPA (BERTopic+LLM) | A.4 | académico | BERTopic + validación LLM clasifica semánticamente 8.200+ propuestas del PPA federal. |
| BR | e-Cidadania — IA para ideas legislativas | A.5 | institucional | IA cruza 145.993 ideas legislativas ciudadanas con proyectos de ley (función nueva, ene-2026). |
| BR | 5ª Conferência Nacional de CT&I | A.5 | institucional | IA sistematiza las contribuciones de 200+ conferencias preparatorias (100.000+ personas). |
| BR | OPA Piauí — Presupuesto Participativo Digital | A.5 | prensa | *dudoso*: Colab + IA de AWS reduce 40% el análisis de 1.311 propuestas; rol semántico por confirmar. |
| PA | Mansa Idea (Pacto del Bicentenario) | A.8 | prensa | IA organiza y agrega consensos sobre 175.000+ propuestas ciudadanas. |
| CL | LXS 400 — Chile Delibera | A.3 | institucional | Mini-público de 400 personas; IA (Stanford Online Deliberation) gestiona turnos y estructura aportes. |
| TT | EngageTT (Go Vocal) | A.5 | institucional | *dudoso*: plataforma oficial sobre Go Vocal (NLP); activación de funciones de IA por confirmar. |

**9 candidatos nuevos** (7 sólidos + 2 dudosos). Todos entran a `candidatos.csv`
con `estado=candidato_nuevo` para triage en Gate 1; los dudosos requieren
confirmación del rol de la IA sobre el contenido en Fase 2.

## 3. Reverificaciones del baseline con señal de actividad 2025-2026

11 casos del baseline fueron reconfirmados por canal institucional adicional
(quedan en `candidatos.csv` con `canal_origen = "A.0; A.x"` y `flag_canal_unico=0`):
BO Bolivia Conversa · BR e-Cidadania (audiencias) · BR PPA Natal · CO ECHO-HáblameD ·
CO Chatico · CR dIAra (OGP 2025) · CR U-Report · DO CiudadanIA · EC PAGA IA (Plan 2025-2027) ·
GT Guatemala Joven Conversa · HN RedPública+iVerify.

## 4. Exclusiones y vacíos (filtrado de elegibilidad)

Los investigadores descartaron numerosos casos por criterio, principalmente:
- **Consultas SOBRE IA** que no usan IA en su proceso (ENIA/estrategias nacionales
  de IA en AR, UY, CL, EC, GT, DO, CU, PY, TT).
- **Chatbots de atención/FAQ/trámites** (Anansi TT, CXGenies DO, varios MX/CO).
- **Conteo/integridad electoral** (excluidos firmes: MX Sufragio Seguro, PE ONPE).
- **Civic-tech sin IA** o votación entre opciones cerradas sin análisis de aportes.

**Países sin candidatos elegibles en la ronda 1:** AR, UY, PY, VE, CU, JM, SV
(y PE sin caso nuevo; su caso baseline requiere verificación de fuente primaria).
La ronda 2 (deliberativas, académica, multilaterales, subnacional, barrido de
países flacos) busca cerrar estos vacíos.

## 5. Próximos pasos

1. Integrar los hallazgos de la **ronda 2** a `hallazgos_web.csv`.
2. **Gate 1 (humano)** sobre `candidatos.csv`: aprobar qué pasa a Fase 2.
3. Fase 2 (doble pasada) sobre nuevos y dudosos; confirmar rol de la IA + verbatim.
4. Conseguir el **Anexo B** para A.11 (instituciones por país).
