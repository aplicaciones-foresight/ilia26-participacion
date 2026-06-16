# Dudas y fuentes que requieren ACCESO MANUAL

Lista priorizada de lo que **el equipo debe verificar/abrir manualmente**, porque
este entorno **no puede abrir páginas web** (sólo búsqueda — ver
`METODOLOGIA.md` §6). Estado: EE, SG, PT cerrados; **ES y DE en proceso (agentes)**.

---

## A. Limitación global (afecta a TODO el estudio)
`WebFetch`/`curl` → **HTTP 403** contra cualquier dominio (universidades, QS,
Wikipedia…). Toda la clasificación se hizo con **snippets de búsqueda**. Por eso:
- **C3 (≥3 cursos del plan de estudios)** casi nunca es verificable sin abrir el
  plan → muchos casos quedan **PARCIAL** o con C3 = `NoVerificable`.
- **Recomendación:** para confirmar/auditar, abrir manualmente (a) el portal QS
  oficial `topuniversities.com` con filtro de país y (b) las páginas de cada
  programa de doctorado (líneas de investigación + plan de estudios/actividades
  formativas + perfil de egreso).

## B. Verificación de la LISTA QS 2026 (membresía)
| País | Ítem a confirmar | Detalle |
|---|---|---|
| Estonia | 3ª universidad del país en QS 2026 | Se asume **Tallinn University** (#901–950). Verificar que NO sea *Estonian University of Life Sciences*. Abrir `topuniversities.com/world-university-rankings?countries=ee`. |
| Estonia | Puesto de **TalTech** | Fuentes discrepan: **#621** vs **#635**. Confirmar. |
| Portugal | Puestos de Coimbra/Aveiro/Minho | Confirmados vía search (347/419/566) pero conviene cotejar con QS oficial. |
| España | Lista de 38 (31 púb. + 7 priv.) | **En proceso por agente.** Confirmar la cola (puestos 700–1400) y las 7 privadas. |
| Alemania | Lista de 49 | **En proceso por agente.** Confirmar la cola (bandas 600–1400). |

## C. Ítems por programa (acceso manual), por prioridad

### 🔴 Prioridad ALTA (cambian la clasificación)
1. **Portugal — U. Católica Portuguesa** (NO_CUMPLE provisional): verificar si el
   *Institute of Computing and Data Science* (ICCD, Braga) **ofrece o alimenta un
   programa de DOCTORADO** en computación/ciencia de datos/IA. Si existe →
   reclasificar a PARCIAL/CUMPLE. Abrir `ucp.pt/educationprogrammes/doctorate` y la
   web del ICCD Braga.
2. **Estonia — University of Tartu** (PARCIAL, mejor candidato a CUMPLE): abrir el
   currículo del doctorado *Mathematics and Computer Science* (sistema ÕIS) y la
   página de la especialización CS para confirmar **≥3 cursos de IA (C3)** y/o un
   **perfil de egreso con IA (C2)**. Si se confirma → **CUMPLE**.

### 🟠 Prioridad MEDIA (confirman líneas/cursos IA)
3. **Estonia — TalTech**: abrir grupos del Dept. of Software Science + plan del
   PhD-ICT → confirmar líneas IA específicas y cursos.
4. **Estonia — Tallinn University**: confirmar que la línea **IA/ciencia de datos**
   está activa **dentro del doctorado** *Information Society Technologies* (la
   escuela es fuerte en HCI/EdTech; la IA aparece sobre todo en máster EMJM).
5. **Portugal — ISCTE-IUL**: confirmar **línea y cursos de IA/ML** dentro del *PhD
   in Information Science and Technology* (las áreas declaradas lideran con
   IS/Business Intelligence/Telecom/AR; ISTAR).
6. **Portugal — U. do Algarve**: confirmar **líneas/cursos de IA** en el
   *Doutoramento em Engenharia Informática*.

### 🟡 Prioridad BAJA (sólo afinan evidencia; ya son CUMPLE)
7. **Singapur — NUS**: confirmar el requisito de *coursework* del **PhD** (no del
   MComp-AI) en el NUS Bulletin.
8. **Singapur — SUTD**: contar los cursos de IA en la página *Courses* de ISTD.
9. **Portugal — Lisboa/IST, NOVA, Aveiro**: confirmar el nº exacto de cursos de IA
   del bloque curricular (ya clasificados CUMPLE por evidencia suficiente).

---

## D. España y Alemania
Se completará esta sección al cerrar los agentes de **ES (38)** y **DE (49)**, con
sus propios ítems de acceso manual (esperado: muchos doctorados alemanes
*research-based* sin plan público → C3 `NoVerificable`).
