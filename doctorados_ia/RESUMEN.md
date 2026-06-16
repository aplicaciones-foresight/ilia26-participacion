# RESUMEN — Cantidad de programas de doctorado de IA (países extra, QS 2026)

**Indicador:** nº de programas de doctorado que **forman competencias en IA** en
las universidades del QS World University Rankings 2026 de 5 países de referencia.
**Fecha:** 2026-06-16 · **Método:** sólo `WebSearch` (sin acceso a páginas; ver
`METODOLOGIA.md` §6) + **ronda de validación dirigida**. Detalle y fuentes por
país en `paises/*.md`; datos máquina en `clasificacion.csv`; entregables para
traspaso en `entregables/` (planilla `.xlsx` + informe `.docx`).

---

## Cifra principal (tras validación)

> De **103 universidades** en QS 2026 (DE 49 · ES 38 · PT 9 · SG 4 · EE 3),
> **100 tienen ≥1 programa de doctorado que forma competencias en IA**
> (**49 CUMPLE + 51 PARCIAL**). Sólo **3 NO CUMPLE** (validados).

- **Conteo ESTRICTO (sólo CUMPLE): 49 programas.**
- **Conteo AMPLIO (CUMPLE + PARCIAL = "forman competencias"): 100 programas.**
- **Decisión pendiente del operador:** cuál se publica (recomendado: reportar ambos).

## Conteo por país

| País | QS 2026 | CUMPLE | PARCIAL | NO CUMPLE | Forman compet. (C+P) |
|---|---:|---:|---:|---:|---:|
| 🇩🇪 Alemania | 49 | 19 | 29 | 1 | **48** |
| 🇪🇸 España | 38 | 20 | 17 | 1 | **37** |
| 🇵🇹 Portugal | 9 | 6 | 2 | 1 | **8** |
| 🇸🇬 Singapur | 4 | 4 | 0 | 0 | **4** |
| 🇪🇪 Estonia | 3 | 0 | 3 | 0 | **3** |
| **TOTAL** | **103** | **49** | **51** | **3** | **100** |

### Los 3 NO CUMPLE (validados)
- 🇵🇹 **Universidade Católica Portuguesa** — el ICCD (Braga) ofrece *grado y máster*
  en Ciencia de Datos pero **no doctorado**; sus doctorados son de otras facultades.
- 🇪🇸 **IE University** — la *School of Science & Technology* sólo tiene grado/máster
  en CS-IA; el único PhD es de **IE Business School** (excluido).
- 🇩🇪 **University of Hohenheim** — **AIDAHO** es un *certificado* transversal, no un
  doctorado; sus facultades son agro/vida + economía.

## Cambios introducidos por la validación
- 🇪🇸 **UEM** NO CUMPLE → **PARCIAL** (tiene *Doctorado en Ing. de Control y Sistemas
  Inteligentes*).
- 🇩🇪 **Potsdam (HPI)** PARCIAL → **CUMPLE** (escuela doctoral estructurada + research
  school de métodos de IA).
- 🇪🇸 **UCAM** confirmada **PARCIAL** (Doctorado en Ing. Informática + grupo UKEIM).
- 🇪🇪 **Estonia** confirmada: las 3 del ranking general son **Tartu (#362), TalTech
  (#635), Tallinn University (1001–1200)**; *Univ. of Life Sciences* no está en el
  ranking general.

## Patrón observado (coherente con la metodología)
- **Singapur (4/4 CUMPLE)** y **Portugal (6 CUMPLE)**: doctorados con **coursework
  estructurado** → se evidencia C3 → CUMPLE.
- **Alemania (29 PARCIAL)** y **Estonia (3 PARCIAL)**: doctorado *research-based*; C1
  casi universal vía centros, pero C3 rara vez público → **PARCIAL**. Las CUMPLE
  alemanas son las de **escuelas doctorales estructuradas / centros nacionales de IA**.
- **España (mixto)**: CUMPLE por **programas dedicados de IA** o perfil/centro de IA explícito.

## Regla de clasificación (uniforme en los 5 países)
`CUMPLE ⟺ C1 ∧ (C2=Sí ∨ C3=Sí)` · `PARCIAL ⟺ sólo C1` · `NO_CUMPLE ⟺ sin línea de IA`.
La clasificación de **España** se normalizó a esta regla (12 casos CUMPLE→PARCIAL);
ver `paises/espana.md`.

## ⚠️ Limitaciones (leer antes de publicar)
1. **Sin acceso a páginas (HTTP 403):** todo se basó en *snippets*. **C3 casi nunca
   verificable** → la frontera **CUMPLE/PARCIAL es provisional**; el conteo robusto y
   comparable es el **AMPLIO (CUMPLE+PARCIAL)**.
2. **Ranks QS aproximados** (salvo top y debuts): fijar a mano en
   `topuniversities.com/world-university-rankings?countries=<de|es|pt|ee|sg>`.
3. **Membresías a confirmar:** ES **Universidad de Cantabria** (aparece en by-subject;
   confirmar en el ranking general); DE posible debut **TU Hamburg-Harburg** y cola.
4. **C2=Sí de varias CUMPLE** (ES y DE) se infirió de centros/perfiles por *snippet*;
   conviene verificar el perfil de egreso. Ver `DUDAS_ACCESO_MANUAL.md`.
