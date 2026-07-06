# Revisión del atlas PAVE (pave.pairs.site) — ILIA 2026

*Revisión solicitada tras el lanzamiento del sitio. Objetivo: determinar si el atlas
contiene casos incluibles que no estén en nuestra base.*

## Qué es PAVE
**PAVE — Participatory AI Voice(s) and Engagement Case Book** (pave.pairs.site), de la ONG
británica **Connected by Data**, parte del "Citizens' Track on AI Governance" (vinculado al
simposio PAIRS y al UN Global Dialogue on AI Governance). Descrito académicamente en
*"Voices in the Loop: Mapping Participatory AI"* (Mushkani, FAccT 2026, arXiv:2605.16827):
131 registros armonizados del corpus de **Magaña & Shilton** (FAccT 2025, revisión
sistemática de 95 proyectos, DOI 10.1145/3715275.3732148) más casos auditados adicionales.

**Cómo lo accedimos:** el sitio y el AirTable están fuera del alcance del entorno, pero el
dataset publicado vive en GitHub (`github.com/connectedbydata/pave`); descargamos
`assets/data/cases_aggregated.json` (**83 casos publicados**, snapshot 2026-07-06, guardado
en `data/fetched/pave_cases_aggregated_2026-07-06.json`).

## Resultado: **1 caso nuevo incorporado** (Meta GenAI Forum, BR) y 1 cruce con nuestra base

*(Actualización jul-2026: en la revisión inicial Meta Forum quedó como "borde-NO"; tras la
profundización pedida por el equipo —plataforma y moderador confirmados con verbatim, cohorte
y resultados brasileños— se incorporó como caso BR. El resto se mantiene fuera.)*

El atlas trata mayoritariamente de **"Participatory AI" = participación ciudadana EN el
diseño/gobernanza de sistemas de IA** — el caso *inverso* a nuestro indicador (IA usada
dentro de procesos de participación), que nuestro criterio excluye ("IA como tema").
De los 83 casos, **9 tienen vínculo con América Latina y el Caribe** (~11%; el corpus base
solo tiene 6/95 LatAm). Análisis caso por caso:

| Caso PAVE | País(es) | Qué es | Veredicto ILIA |
|---|---|---|---|
| **A Framework for National Dialogues on Frontier Technologies** (UNDP Accelerator Labs) | PY (+MA) | Diálogos/encuesta sobre riesgos de IA | **Ya está en nuestra base** = "PY Consultas ciudadanas sobre IA (PNUD)", excluido (IA como tema; análisis humano). ✓ cruce confirmado |
| **Collective Intelligence Project — Global Dialogues** | Global (86 países, 12 nuestros) | Diálogo global con **LLM que agrupa/sintetiza respuestas** y ML de consenso | NO: es global sin proceso-país atribuible (precedente Botivist) y el tema es la propia IA. *Es el único con mecanismo de "IA sobre aportes"; si CIP corre un diálogo país-específico en la región, revisar en 2027.* |
| **Meta Generative AI Community Forum** | BR (+DE, ES, US) | Deliberative Polling® (plataforma Stanford con moderador automatizado, la misma de LXS 400) sobre principios para chatbots de IA generativa | **INCORPORADO (jul-2026)** tras profundización dirigida: mini-público formal con cohorte brasileña de muestra científica, resultados desglosados para Brasil y moderador automatizado confirmado (verbatim Stanford/BIT). Convocante 'empresa' está en la taxonomía CENIA; la regla 'IA como tema' no aplica porque la IA es también herramienta del proceso. → nuevo caso BR. |
| **Chilean National AI Policy — Participatory Design and Update** | CL | Actualización participativa de la Política Nacional de IA (2024-25, MinCiencia; ~300 presenciales + 600 online) | NO: participación EN política de IA = "IA como tema" (misma regla que UY ENIA y PY). |
| **Global AI Dialogues** (TU Múnich) | BO, MX (+DE, IN, JP, NG) | Talleres de futuros + encuesta sobre IA | NO: sobre IA (tema) y multi-país. |
| **Data Against Feminicide** | AR, BR, UY (+KE, US) | Contra-datos participativos sobre feminicidio (co-diseño de herramientas ML de detección de noticias) | NO: activismo de datos/monitoreo, no un proceso participativo convocado para una decisión pública; multi-país. |
| **Favel IA** | BR | Investigación-acción participativa (UFF + Instituto Papo Reto + Cambridge CGHR) sobre apropiación y gobernanza de IA desde las favelas | NO: participación EN gobernanza de IA (tema); investigación, no proceso decisorio. |
| **Marialab** | BR | ONG feminista de tecnología (entrada de mapeo, sin proceso) | NO: organización, no proceso. |
| **MTST Technology Hub** | BR | Núcleo tecnológico del movimiento de vivienda MTST | NO: colectivo tecnológico, no proceso participativo con IA sobre aportes. |

**Cobertura cruzada:** los 74 casos restantes del atlas no tienen vínculo con nuestros 20
países (concentración en Norteamérica/Europa, coherente con lo que reporta el propio paper).

## Valor para el ciclo
1. **Evidencia de exhaustividad** para CENIA: revisamos una fuente global nueva (lanzada
   jul-2026) y nuestro inventario ya contenía el único caso regional pertinente (PY-PNUD).
2. **Canal de descubrimiento futuro**: PAVE queda incorporado como canal A.15 en
   `config.yaml` (revisar sus releases en ciclos siguientes; el dataset es versionado).
3. **Confirmación del deslinde conceptual** para el informe: "Participatory AI"
   (participación en la IA) ≠ nuestro indicador (IA en la participación); útil para la
   sección metodológica.

*Método: dataset íntegro inspeccionado (83/83 registros, filtro ISO-2 + texto por los 20
países); verificación externa puntual de los casos ambiguos (Favel IA, CIP, Meta Forum,
PNIA Chile) vía búsqueda web. Enlaces para revisión manual del equipo:
pave.pairs.site · github.com/connectedbydata/pave · airtable.com/apptNBmT3sNVxejwg/shrtD9L3mdwnTJ6ws
(tabla Magaña & Shilton, filtrar región = Latin America).*
