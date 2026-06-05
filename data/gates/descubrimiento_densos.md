# Descubrimiento ampliado — países densos (CO · MX · BR · CL · CR)

**Fecha:** 2026-06-05 · **Pipeline ILIA 2026 — Participación Ciudadana**

Aplicación del **método ampliado** (licitaciones A.12, premios A.13, proveedores
A.14, subnacional profundo, académico/gris) a los **5 países que faltaban** por
recibirlo completo: los densos CO, MX, BR (re-corrido tras el corte del piloto),
CL (íd.) y CR. Un investigador profundo por país, con síntesis temprana
(los 5 entregaron informe completo).

## Saldo: 2 nuevos sólidos + 3 dudosos + refuerzos

| País | Nuevo / dudoso | Caso |
|---|---|---|
| **CO** | 🆕 **nuevo** | **ISIDataInsights / "Reto de Ciudad: Datos con Historia"** — herramienta de IA ganadora de concurso SDP Bogotá + Maloka (2024) que identifica patrones en los aportes ciudadanos de planificación distrital. |
| **CL** | 🆕 **nuevo** | **El Chile que Queremos (ECQQ) — MinCiencia** — diálogos 2019-2020 (~132k participantes); RNN + Random Forest + LDA + clasificación de emociones sobre el texto de los aportes (**código público en GitHub**). |
| **CO** | 🔶 dudoso | **POT Bogotá** (artículo Auditoría General, jun-2025): ¿piloto o propuesta de diseño? |
| **CO** | 🔶 dudoso | **DNP – Diálogos Regionales Vinculantes** (89.788 propuestas; "Unidad de Científicos de Datos"): ¿NLP o codificación manual? |
| **CL** | 🔶 dudoso | **Senador Virtual / CrowdLaw** (GobLab UAI + IMFD): NLP sobre aportes legislativos; no verificado en producción. |
| **BR** | ⬆️ refuerzo | **Brasil Participativo** sube de "investigación" a **evidencia de producción**: paper *"From Pre-labeling to Production"* (arXiv 2511.01545) + clasificador ML (UnB-LAPPIS). |
| **CL** | ⬆️ refuerzo | **Cabildos 2016** (baseline) documentado con NLP: argument mining 240k argumentos (ACL 2017) + topic modeling (PLOS One 2022). |
| **MX** | = | El caso fuerte (**Guanajuato InteliGENTE**) es el **mismo** ya registrado, ahora mejor documentado. Sin caso nuevo. |
| **CR** | = | **0 casos nuevos**; solo dudosos sin evidencia de IA (PND, ENIA). dIAra y U-Report siguen siendo los únicos. |

## Exclusiones rigurosas notables (densos)

- **MX**: CDMX PGD 2025-2045 (la IA **redactó** el plan, no analizó aportes);
  Jalisco/Mérida/Monterrey (presupuesto participativo de **votación cerrada**, sin
  IA); ATDT/Gobernarte-MX "Llave CDMX" (identidad, no participación).
- **CO**: Ciclos Deliberativos (Chatico solo **convoca**); paper que usa **Twitter**
  (no es proceso participativo formal); Medellín POT (sin IA sobre contenido).
- **CL**: Consulta Política Nacional de IA (consulta *sobre* IA); Merlin Research
  (**encuesta** de opinión); Vincula/Parlamento.ai (no son aportes ciudadanos).
- **BR**: Plano Clima / consultas MEC (sin sistematización IA confirmada); paper
  USP de OP São Paulo (exploratorio).

## Lectura

El método ampliado en países densos cumple lo previsto en el piloto: **re-confirma
y enriquece** lo conocido (BR a producción, CL Cabildos con NLP, MX Guanajuato
documentado) y destapa **algún caso nuevo puntual** — aquí **2 sólidos (CO
ISIDataInsights, CL ECQQ)** y 3 dudosos. CO y CL fueron los más productivos.

**Limitación recurrente:** HTTP 403 en `.gob.*`/`.gov.co`/`.gob.mx`/`gov.br` y
buscadores de compras (SECOP, CompraNet, ComprasNet, Mercado Público) **no
indexados** → varios vacíos solo se cierran con acceso directo.

## Estado final del descubrimiento (20/20 países)

- **18 candidatos nuevos/dudosos** (10 sólidos + 8 dudosos) + 13 reverificaciones.
- Brasil, Colombia y Chile concentran la práctica real con IA sobre el contenido
  de aportes; el resto de la región es escaso o nulo en este vector.
