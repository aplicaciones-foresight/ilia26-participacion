# RESUMEN — Cantidad de programas de doctorado de IA (países extra, QS 2026)

**Indicador:** nº de programas de doctorado que **forman competencias en IA** en
las universidades de QS World University Rankings 2026 de 5 países de referencia.
**Fecha:** 2026-06-16 · **Método:** sólo `WebSearch` (sin acceso a páginas; ver
`METODOLOGIA.md` §6). Detalle y fuentes por país en `paises/*.md`; datos
máquina en `clasificacion.csv`; verificación manual en `DUDAS_ACCESO_MANUAL.md`.

---

## Cifra principal

> De **103 universidades** en QS 2026 (DE 49 · ES 38 · PT 9 · SG 4 · EE 3),
> **99 tienen ≥1 programa de doctorado que forma competencias en IA**
> (**48 CUMPLE + 51 PARCIAL**). Sólo **4 NO CUMPLE** (provisionales, con flag de
> verificación manual que podría reducir aún más esa cifra).

La **unidad de conteo** es el programa doctoral (≈ una universidad con su programa
de Tec/Ing más relevante; algunas tienen más de uno). "Forman competencias" =
**CUMPLE + PARCIAL** (PARCIAL declara líneas de IA pero no se pudo verificar el
plan de ≥3 cursos por la restricción de acceso — ver más abajo).

## Conteo por país

| País | QS 2026 | CUMPLE | PARCIAL | NO CUMPLE | Forman compet. (C+P) |
|---|---:|---:|---:|---:|---:|
| 🇩🇪 Alemania | 49 | 18 | 30 | 1 | **48** |
| 🇪🇸 España | 38 | 20 | 16 | 2 | **36** |
| 🇵🇹 Portugal | 9 | 6 | 2 | 1 | **8** |
| 🇸🇬 Singapur | 4 | 4 | 0 | 0 | **4** |
| 🇪🇪 Estonia | 3 | 0 | 3 | 0 | **3** |
| **TOTAL** | **103** | **48** | **51** | **4** | **99** |

### Lectura por escenario de conteo (decisión del operador)
La metodología admite dos lecturas del "número de programas de doctorado de IA":
- **Estricto (sólo CUMPLE):** **48** programas (DE 18, ES 20, PT 6, SG 4, EE 0).
- **Amplio (CUMPLE + PARCIAL = "forman competencias"):** **99** programas.

> **Pendiente del operador:** decidir cuál se publica. Recomendado reportar ambos
> (como hace el resto del proyecto). No se resuelve aquí.

## Patrón observado (coherente con la metodología)
- **Singapur (4/4 CUMPLE)** y **Portugal (6 CUMPLE)**: doctorados con **coursework
  estructurado** (modelo anglosajón / 1.er año curricular de 30–60 ECTS) → se
  puede evidenciar C3 → CUMPLE.
- **Alemania (30 PARCIAL)** y **Estonia (3 PARCIAL)**: doctorado *research-based*
  (*Promotion* / individual); C1 (líneas de IA) casi universal vía centros, pero
  C3 (≥3 cursos) rara vez es público → **PARCIAL** (no implica que no formen
  competencias). Las CUMPLE alemanas son las de **escuelas doctorales
  estructuradas / centros nacionales de IA** (Tübingen IMPRS-IS, TU Dresden/Leipzig
  ScaDS.AI, TU Darmstadt ELIZA, Saarland GSCS, TUM/LMU MCML, KIT, TU Berlin BIFOLD,
  Bonn/Dortmund Lamarr, etc.).
- **España (20 CUMPLE / 16 PARCIAL)**: caso mixto; CUMPLE por **programas dedicados
  de IA** (UPC, UPM, USAL) o **perfil/centro de IA explícito**.

## Regla de clasificación aplicada (uniforme en los 5 países)
`CUMPLE ⟺ C1 ∧ (C2=Sí ∨ C3=Sí)` · `PARCIAL ⟺ sólo C1 (o C1 indicio)` ·
`NO_CUMPLE ⟺ sin línea de IA`. La clasificación de **España** del agente se
**normalizó** a esta regla (12 casos CUMPLE→PARCIAL con C2=Indicio y
C3=NoVerificable); ver `paises/espana.md`.

## ⚠️ Limitaciones (leer antes de publicar)
1. **Sin acceso a páginas (HTTP 403):** todo se basó en *snippets* de búsqueda. **C3
   (≥3 cursos) casi nunca verificable** → muchos PARCIAL y muchos
   `requiere_acceso_manual`. La frontera CUMPLE/PARCIAL es **provisional**.
2. **Ranks QS aproximados:** salvo el top de cada país y los debuts confirmados por
   prensa, los puestos individuales (sobre todo bandas ≥600) deben fijarse a mano
   en `topuniversities.com/world-university-rankings?countries=<de|es|pt|ee|sg>`.
3. **Membresías a confirmar:** ES **Universidad de Cantabria** (dudosa, candidata
   de cierre); DE posible debut **TU Hamburg-Harburg** y cola (RPTU, Augsburg,
   Bielefeld, Hohenheim) a cotejar.
4. **4 NO CUMPLE provisionales** (PT Católica; ES UEM, IE; DE Hohenheim): podrían
   pasar a PARCIAL si se confirma un doctorado Tec/Ing con IA. Ver `DUDAS_ACCESO_MANUAL.md`.
5. **C2=Sí de varias CUMPLE** (ES y DE) se infirió de centros/perfiles de IA por
   *snippet*; conviene verificar el perfil de egreso a mano.
