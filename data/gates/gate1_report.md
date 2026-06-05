# Gate 1 — Reporte de Triage (Fase 1: Descubrimiento)

**Fecha de corrida:** 2026-06-05  ·  **Pipeline ILIA 2026 — Participación Ciudadana**

> El Gate 1 es HUMANO. Este reporte prepara insumos; no autoaprueba candidatos. El operador decide qué pasa a Fase 2 (extracción).

## 1. Resumen

- Candidatos del baseline activo 2025 (canal A.0): **28**
- Casos excluidos 2025 a re-verificar (canal A.0-excluidos): **49**
- Candidatos NUEVOS de descubrimiento web (canales A.1–A.10): **13**
- Candidatos marcados de canal único (`flag_canal_unico=1`): **78**
- Cobertura: **20/20** países representados en candidatos.csv

## 2. Candidatos NUEVOS (descubrimiento web) por país

| País | Candidato | Canal(es) | Fuente/nota | Tipo |
|---|---|---|---|---|
| BR | 5a Conferencia Nacional de CT&I - sistematizacio | A.5 | fuente=institucional | nuevo |
| BR | Brasil Participativo - clustering semantico (BER | A.4 | fuente=academico; confirmar adopción oficial v | nuevo |
| BR | Cátedra Brasil / Co:Lab USP - IA generativa en p | A.4 | fuente=academico; piloto búsqueda ampliada; in | dudoso |
| BR | OPA Piaui - Presupuesto Participativo Digital (C | A.5 | fuente=prensa; confirmar rol de IA sobre conte | dudoso |
| BR | Sao Paulo - Programa de Metas / Participe Mais ( | A.6 | fuente=institucional; verificar uso operaciona | nuevo |
| BR | e-Cidadania Senado - IA matching de ideas legisl | A.5 | fuente=institucional; confirmado por IPU; dist | nuevo |
| CL | LXS 400 - Chile Delibera | A.3 | fuente=institucional; 2021; nuevo para el índi | nuevo |
| CO | Citibeats + PNUD Colombia (deliberación pública  | A.9 | fuente=institucional; confirmar si es proceso  | nuevo |
| CU | Consulta Popular Código de las Familias (GEMA-CE | A.4 | fuente=prensa; 2022; verificar si 'análisis in | dudoso |
| MX | Guanajuato Inteligente 2024-2030 | A.5 | fuente=prensa; verificar software de IA especí | nuevo |
| PA | Mansa Idea (Pacto del Bicentenario) | A.8 | fuente=prensa; proceso (Pacto del Bicentenario | nuevo |
| TT | EngageTT (plataforma Go Vocal) | A.5 | fuente=institucional; confirmar tier/activació | dudoso |
| VE | Plan de la Patria 7 Transformaciones - IA y Big  | A.5 | fuente=prensa; fuente estatal única; ningún pr | dudoso |

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
| TT | 0 | — |
| UY | 0 | — |
| VE | 0 | — |

## 4. Duplicados probables (mismo país + nombre normalizado)

- **CL** · «participacion ciudadana proceso constitucional» → CL-participacion-ciudadana-proceso-constitu, CL-participacion-ciudadana-proceso-constitu-2

## 5. Casos del baseline SIN señal de actividad 2026

Todos los casos del baseline activo entran como `a_reverificar`: en esta corrida (sin fetch) NO se ha confirmado su actividad 2026. El Gate 1 debe priorizar la re-verificación de actividad antes de Fase 2.

## 6. Estado de canales (frame de búsqueda)

- Canal A.0 (baseline): **ejecutado**.
- Canales operables sin Anexo B, **pendientes de fetch**: 260 celdas país×canal (A.1–A.9).
- Canales **bloqueados por falta de Anexo B** (A.10/A.11): 20 celdas. Pedir Anexo B al operador.

Detalle por canal (celdas en el frame):

| Canal | Nombre | Estado | Celdas |
|---|---|---|---|
| A.0 | Re-verificación baseline 2025 (casos + excluidos) | ejecutado | 20 |
| A.1 | Participedia | pendiente_fetch | 20 |
| A.2 | OGP / IRM (Open Government Partnership) | pendiente_fetch | 20 |
| A.3 | Repositorios OCDE / observatorios | pendiente_fetch | 20 |
| A.4 | Literatura académica y gris | pendiente_fetch | 20 |
| A.5 | Portales de gobierno digital/participación país | pendiente_fetch | 20 |
| A.6 | Ecosistema Decidim | pendiente_fetch | 20 |
| A.7 | Ecosistema Polis / CitizenLab(Go Vocal) y similares | pendiente_fetch | 20 |
| A.8 | Redes regionales de sociedad civil | pendiente_fetch | 20 |
| A.9 | Organismos multilaterales (PNUD, UNICEF, CEPAL...) | pendiente_fetch | 20 |
| A.10 | Medios por país (2-3 c/u) — señal, no evidencia | pendiente_fetch | 20 |
| A.11 | Instituciones de participación por país | bloqueado_anexo_b | 20 |
| A.12 | Compras/licitaciones públicas (SECOP, ComprasNet, COMPR.AR, Mercado Público) | pendiente_fetch | 20 |
| A.13 | Premios e innovación pública (Gobernarte-BID, OGP Awards, CLAD, labs) | pendiente_fetch | 20 |
| A.14 | Proveedores/herramientas (Citibeats, Go Vocal, Pol.is, Remesh, Decidim-IA…) | pendiente_fetch | 20 |

## 7. Decisiones que requieren al operador

1. **Anexo B** (directorio medios/instituciones por país): bloquea A.10/A.11. Sin él, la Fase 1 queda incompleta para esos canales.
2. **Ejecución del `search_frame.csv`**: requiere una corrida con fetch (web) para A.1–A.9. Define presupuesto y prioridad por país.
3. **Tratamiento de `flag_canal_unico`** y de los **49 excluidos** (¿re-verificar todos o muestrear?).
