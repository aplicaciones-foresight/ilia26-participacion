# Validación de Singapur con texto primario (NAIS 2019 + NAIS 2.0 2023 + Update 2026)

**Fecha:** 2026-06-22 · **Documentos:** *National AI Strategy* (NAIS 1.0, 2019, 45 pp), *National AI Strategy 2.0*
(2023, 68 pp), *NAIS Update* (2026, 44 pp). **Método:** extracción verbatim con PyMuPDF + barrido amplio de
sinónimos por subindicador (mecanismos vs sectores; secciones de ejecución). Quita el estado PRELIM de Singapur.

## 1. Cambio de puntaje (1)
| ID | Subindicador | Antes | Después | Motivo (texto primario) |
|---|---|---|---|---|
| **121** | Multistakeholder (elaboración) | 3 (Gob+2) | **4** (Gob+3) | SCAI reunió "40 … experts from **academia, non-profit, industry and government**" (NAIS 2.0 p.33); RAISE.SG "**academia, industry, and non-profit**" (p.46) → Gob+3. *(Posible 5 si se cuenta internacional/público general.)* |

## 2. Confirmaciones (se quita PRELIM; sin cambio de puntaje)
| ID | Subindicador | Punt. | Evidencia primaria |
|---|---|---|---|
| 104 | Antigüedad | 4 | El Update 2026 ("Refreshed Priorities/Enablers") refresca NAIS 2.0; cuenta como estrategia vigente (decisión operador). |
| 106 | Mec. de evaluación | 3 | NAIS se revisa (1.0→2.0→Update, que evalúa el progreso) + "committed to continually reviewing our actions" (Update p.7). |
| 107 | Presupuesto | 3 | "committed over **S$1 billion** to fund public AI research and talent development **from 2025 to 2030**" (Update p.21). |
| 117 | Perspectiva de género | **0** | "gender"/"women" no aparecen como tema en los 3 PDF; "diversity"=lingüística/industria; "inclusive growth"=capacidades amplias (Update p.26). |
| 118 | Sostenibilidad | **1** | Prioridad refrescada: "Advance **resource-efficient AI** … in line with Singapore's **sustainability goals**" (Update p.3/33) + **Green Data Centre Roadmap** (p.31) + tema "Resource-Efficient AI" (NAIS 2.0 p.20). |
| 119 | Particip. ciudadana (elab.) | **1** | La estrategia se hizo "in close consultation with **AI ecosystem representatives**" (NAIS 2.0 p.45) = stakeholders (cuentan en 121), **no** público general. Consultas públicas existen para guías puntuales (MGF GenAI, Securing AI), no para la estrategia. |
| 122 | Multistakeholder (impl.) | 4 | "A **Whole-of-Nation Movement**" (NAIS 2.0 p.67); **Tripartite** Jobs Council = Gob + NTUC + Employers Federation (Update p.26); AI Verify Foundation (non-profit). → Gob+3 *(defendible 5)*. |
| 128 | Iniciativa legal | 1 | Soft law: Model AI Governance Frameworks (2019; GenAI 2024; **Agentic 2026, 1º del mundo**, Update p.36); "lighter-touch frameworks" (p.41). No es debilidad. |
| 129 | Clasificación de riesgo | **1** | "interventions that are **risk-based, tiered**" (NAIS 2.0 p.59); "balanced, **risk-based** approach … for **higher-risk** use cases" (Update p.17). |
| 130 | Sandbox | 1 | AI Verify + **Global AI Assurance Sandbox** (Update p.37) + **PET Sandbox** (9 casos, p.34). |

## 3. Tópicos (109-116) — confirmados = 1
- 109 Ética/gobernanza: "trusted AI", "responsible AI", **Model AI Governance Frameworks** (NAIS 2.0 p.9; Update p.36).
- 110 Infraestructura: enabler "**Compute**" + data centres (Update p.31-33).
- 111 Capacidades: sistema "**Talent**"/"Capabilities" (Update p.26).
- 112 Datos: enabler "**Data**" + data governance (Update p.3).
- 113 Gobierno digital: sistema "**Government**"; IA en servicio público (Update p.14).
- 114 Industria: sistema "**Industry**" (Update p.10-11).
- 115 I+D: sistema "**Research**"; S$1B R&D (Update p.21).
- 116 Cooperación int'l: "**Leader in Thought and Action**"; gobernanza global (Update p.39).

## 4. Notas / decisiones abiertas
- **121 y 122**: con el criterio amplio (contar internacional —comunidad global de AI Verify, países socios— o
  público general/comunidad "Whole-of-Nation" como un 4º sector no-gob), ambos subirían a **5**. Las dejo en **4**
  (Gob+3 con sectores nombrados: industria + academia + non-profit). **Decisión del operador**, igual que en Estonia.
- **119**: Singapur **no** tiene mecanismo de participación *ciudadana* en la estrategia (a diferencia de Estonia con
  sus encuestas ómnibus); su fuerte es la consulta a *representantes del ecosistema* → eso eleva 121, no 119.
- Pendiente externo (no en estos PDF): GCI ciberseguridad (133-137), GIRAI (138-139), ISO (125-126), NRI (144).
