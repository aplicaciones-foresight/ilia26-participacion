# Gate 1 — Reporte de Triage (Fase 1: Descubrimiento)

**Fecha de corrida:** 2026-06-04  ·  **Pipeline ILIA 2026 — Participación Ciudadana**

> El Gate 1 es HUMANO. Este reporte prepara insumos; no autoaprueba candidatos. El operador decide qué pasa a Fase 2 (extracción).

## 1. Resumen

- Candidatos del baseline activo 2025 (canal A.0): **28**
- Casos excluidos 2025 a re-verificar (canal A.0-excluidos): **49**
- Candidatos marcados de canal único (`flag_canal_unico=1`): **77** (esperable en esta corrida: solo se ejecutó A.0)
- Cobertura: **19/19** países representados en candidatos.csv

## 2. Candidatos nuevos vs. baseline

En esta corrida NO hay candidatos *nuevos* (canales A.1–A.11 aún no ejecutados con fetch / Anexo B). Todos los candidatos provienen del baseline 2025 (canal A.0). Los nuevos aparecerán al ejecutar el `search_frame.csv`.

## 3. Candidatos del baseline ACTIVO 2025 por país (a re-verificar 2026)

| País | N | Casos |
|---|---|---|
| AR | 0 | — |
| BO | 1 | Bolivia Conversa |
| BR | 4 | Portal e-Cidadania: Marcado automático de respuestas ciudadanas en videos de audiencias públicas; Plan Plurianual de la ciudad de Natal; Colab; ParticipACT Brasil |
| CL | 9 | Cabildos 2016; Estudio dIAlogos - Percepciones de Futuro; Tenemos que hablar de Chile; Jornada de Escucha Lanzamiento Instituto de Políticas Públicas UNAB; Participación Ciudadana Proceso Constitucional; Participación Ciudadana Proceso Constitucional; La voz de los nuevos votantes; Un encuentro para la equidad de género en la movilidad en Chile; Estrategia de Gobierno Digital. Informe proceso participativo segunda consulta ciudadana |
| CO | 4 | ECHO – HáblameD Medellín; Tenemos que hablar de Colombia; Chatico; Descongestión de solicitudes diarias del programa Ingreso Solidario |
| CR | 2 | dIAra; U-Report Costa Rica – chatbot juvenil |
| CU | 0 | — |
| DO | 1 | CiudadanIA |
| EC | 1 | PAGA IA |
| GT | 1 | Guatemala Joven Conversa |
| HN | 1 | RedPública + iVerify |
| JM | 0 | — |
| MX | 2 | Sufragio seguro; Presupuesto CRECES |
| PA | 0 | — |
| PE | 2 | Consulta Ciudadana sobre el Proyecto Nacional de Educación; Sistema de cómputo con IA para las Elecciones Generales 2026 |
| PY | 0 | — |
| SV | 0 | — |
| UY | 0 | — |
| VE | 0 | — |

## 4. Duplicados probables (mismo país + nombre normalizado)

- **CL** · «participacion ciudadana proceso constitucional» → CL-participacion-ciudadana-proceso-constitu, CL-participacion-ciudadana-proceso-constitu-2

## 5. Casos del baseline SIN señal de actividad 2026

Todos los casos del baseline activo entran como `a_reverificar`: en esta corrida (sin fetch) NO se ha confirmado su actividad 2026. El Gate 1 debe priorizar la re-verificación de actividad antes de Fase 2.

## 6. Estado de canales (frame de búsqueda)

- Canal A.0 (baseline): **ejecutado**.
- Canales operables sin Anexo B, **pendientes de fetch**: 171 celdas país×canal (A.1–A.9).
- Canales **bloqueados por falta de Anexo B** (A.10/A.11): 38 celdas. Pedir Anexo B al operador.

Detalle por canal (celdas en el frame):

| Canal | Nombre | Estado | Celdas |
|---|---|---|---|
| A.0 | Re-verificación baseline 2025 (casos + excluidos) | ejecutado | 19 |
| A.1 | Participedia | pendiente_fetch | 19 |
| A.2 | OGP / IRM (Open Government Partnership) | pendiente_fetch | 19 |
| A.3 | Repositorios OCDE / observatorios | pendiente_fetch | 19 |
| A.4 | Literatura académica y gris | pendiente_fetch | 19 |
| A.5 | Portales de gobierno digital/participación país | pendiente_fetch | 19 |
| A.6 | Ecosistema Decidim | pendiente_fetch | 19 |
| A.7 | Ecosistema Polis / CitizenLab(Go Vocal) y similares | pendiente_fetch | 19 |
| A.8 | Redes regionales de sociedad civil | pendiente_fetch | 19 |
| A.9 | Organismos multilaterales (PNUD, UNICEF, CEPAL...) | pendiente_fetch | 19 |
| A.10 | Medios por país (2-3 c/u) — señal, no evidencia | bloqueado_anexo_b | 19 |
| A.11 | Instituciones de participación por país | bloqueado_anexo_b | 19 |

## 7. Decisiones que requieren al operador

1. **Anexo B** (directorio medios/instituciones por país): bloquea A.10/A.11. Sin él, la Fase 1 queda incompleta para esos canales.
2. **Ejecución del `search_frame.csv`**: requiere una corrida con fetch (web) para A.1–A.9. Define presupuesto y prioridad por país.
3. **Tratamiento de `flag_canal_unico`** y de los **49 excluidos** (¿re-verificar todos o muestrear?).
