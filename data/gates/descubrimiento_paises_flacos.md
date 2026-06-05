# Descubrimiento ampliado — países con 0 ó 1 caso

**Fecha:** 2026-06-05 · **Pipeline ILIA 2026 — Participación Ciudadana**

Aplicación del **método ampliado** (licitaciones A.12, premios A.13, proveedores
A.14, subnacional, académico, términos expandidos) a los **15 países con 0 ó 1
caso**: AR, UY, PY, BO, PE, EC, VE, CU, DO, GT, HN, SV, PA, JM, TT.

Ejecución: 5 investigadores (3 países c/u) con **síntesis temprana e
incremental** → esta vez **no se perdió trabajo** ante límites de sesión (los 5
entregaron informe completo; ~25-30 búsquedas focalizadas c/u).

## Resultado por país

| País | Resultado | Detalle |
|---|---|---|
| **PE** | ✅ baseline **verificado** (fuente primaria) | CNE / PEN 2036 con **IBM Watson Discovery+Studio** sobre **87.991 documentos** de aportes (847 eventos); Andina + El Peruano. Resuelve la duda que teníamos. |
| **CU** | 🆕 **0 → 1** (dudoso) | Consulta Popular **Código de las Familias** (2022): **GEMA-CEN (Datys)** hace "análisis inteligente de expedientes" que agrupa propuestas y determina "típicas"; **XISCOP (UCI)**. Falta confirmar si es NLP/ML o reglas. |
| **EC** | ⚠️ baseline con **duda** | *PAGA IA*: podría operar sobre documentos institucionales (sugerir a técnicos), no sobre aportes ciudadanos textuales → revisar elegibilidad en Fase 2. |
| **VE** | dudoso (sin avance) | *Plan de la Patria 7T*: cifra "500k con IA" solo en prensa estatal; lo verificable son 34.491 propuestas con **rapporteurs manuales**. Sin corroboración técnica. |
| **PA** | dudoso (matizado) | *Mansa Idea*: el proceso (Pacto del Bicentenario) fue **2020-21**; la IA organiza ese corpus en 2024; sociedad civil; tecnología sin identificar. |
| **TT** | dudoso (matizado) | *EngageTT* corre sobre **Go Vocal** (confirmado por URL interna) para el NDTS 2024-2027; falta confirmar que la instancia TT **active** la IA (AskNDTS es FAQ, excluido). |
| **GT** | solo baseline | *Guatemala Joven Conversa* reconfirmado; *GuateJoven* parece su continuación. ENIA/SEGEPLAN = uso interno o consulta *sobre* IA. |
| **HN** | solo baseline | *RedPública* sigue dudoso (módulos de "análisis" sin NLP confirmado). |
| **BO** | solo baseline | *Bolivia Participa* (Decidim) sin IA sobre aportes. |
| **DO** | solo baseline | *CiudadanIA* sin nueva evidencia; OGTIC=consulta *sobre* IA; CitizenLab=2021 sin IA. |
| **AR** | ❌ **0 riguroso** | ParticipIA (prototipo), BA Elige/Rosario (sin NLP), CES/6º Plan OGP (manual), Gobernarte-AR (servicios/identidad). |
| **UY** | ❌ **0 riguroso** | AGESIC=consulta *sobre* IA; Montevideo Decide/Consul sin módulo NLP; UdelaR-PLN solo investiga. |
| **PY** | ❌ **0 riguroso** | Paraguay 2050 (Decidim, sistematización manual); MITIC/DNCP no participación. |
| **SV** | ❌ **0 riguroso** | Ley de IA = regulación; DoctorSV = servicio; nada participativo con IA. |
| **JM** | ❌ **0 riguroso** | Gobernanza de IA = consultas *sobre* IA; JET/Citibeats = empleo juvenil. |

## Saldo del run

- **1 caso nuevo (dudoso)**: CU — y CU deja de estar en cero.
- **1 verificación fuerte**: PE (baseline confirmado con fuente primaria).
- **1 duda abierta**: EC (PAGA IA, elegibilidad a revisar).
- **Países confirmados vacíos (0 riguroso):** AR, UY, PY, SV, JM. Solo **JM y SV**
  quedan **sin ninguna señal** en `candidatos.csv` (AR/UY/PY tienen excluidos del
  baseline a re-verificar).

## Limitación recurrente

Los portales `.gob.*` de varios países (AR, PY, BO, CU, VE) devolvieron **HTTP 403**
a WebFetch, y los buscadores internos de compras públicas (COMPR.AR, DNCP,
Guatecompras, COMPRASAL) no están indexados por Google → quedan como vacíos a
cerrar con **acceso directo / contacto institucional** (no resolubles por web abierta).

## Recomendación

El método ampliado en países flacos rinde sobre todo **verificación y descarte
riguroso** (su valor real), más **1 caso nuevo dudoso (CU)**. Se recomienda
**cerrar el descubrimiento en los flacos** y pasar a **Gate 1 + Fase 2**,
priorizando los dudosos (CU, VE, TT, PA, EC-duda) y las verificaciones primarias.
