# Guía de fetch para el operador (Fase 2)

**Pipeline ILIA 2026 — Participación Ciudadana**

El fetch automático está **bloqueado (HTTP 403)** para casi todas las fuentes institucionales en este entorno. Para extraer cada ficha hace falta el **texto de la fuente**. Procedimiento por candidato:

1. Abrir la(s) URL(s) y copiar el texto relevante (descripción del caso, rol de la IA sobre los aportes, organización convocante, año/estado).
2. Guardarlo en `data/fetched/<caso_id>/fuente_1.txt` (y `fuente_2.txt` para una 2ª fuente independiente) con este encabezado:

   ```
   ===== FUENTE 1 =====
   URL: <url>
   FETCH: <YYYY-MM-DD>
   ESTADO: ok

   <pega aquí el texto>
   ```
3. Rearmar el payload y validar/extraer:
   ```bash
   python src/extract.py --prepare <caso_id>        # rearma payloads A/B con el texto
   # (correr la doble pasada en Claude -> guardar data/fichas/<caso_id>_{A,B}.json)
   python src/extract.py --validate data/fichas/<caso_id>_A.json --texto data/fetched/<caso_id>
   python src/reconcile.py <caso_id>
   ```

> Idealmente **2 fuentes independientes** por caso (≥2 dominios) para que la conciliación pueda alcanzar confianza ALTA. La prensa solo aporta señal; prioriza la fuente institucional.

## A. NUEVOS sólidos — prioridad ALTA (10)

| Prioridad | caso_id | País | URL(s) a fetchear | Qué resolver |
|---|---|:---:|---|---|
| 1 | `MX-guanajuato-inteligente-2024-2030` | MX | https://guanajuatointeligente.com | verificar software de IA específico |
| 2 | `CO-citibeats-pnud-colombia-deliberacion-pub` | CO | https://www.undp.org/es/colombia/blog/analitica-de-datos-para-mejorar-la-deliberacion-publica-en-colombia | confirmar si es proceso participativo formal o social listening |
| 3 | `BR-brasil-participativo-clustering-semantic` | BR | https://arxiv.org/abs/2509.21292  ; https://arxiv.org/abs/2511.01545  ; https://github.com/ResidenciaTICBrisa/BP-Classificador-de-Propostas | EVIDENCIA DE PRODUCCIÓN: paper 'From Pre-labeling to Production' (arXiv 2511.01545) + clasificador ML (UnB-LAPPIS). Resuelve la duda investigación vs despliegue oficial. |
| 4 | `BR-e-cidadania-senado-ia-matching-de-ideas` | BR | https://www12.senado.leg.br/noticias/materias/2026/01/16/cidadaos-ajudam-a-escrever-projetos-de-lei-com-ferramenta-de-inteligencia-artificial | confirmado por IPU; distinto del baseline |
| 5 | `BR-sao-paulo-programa-de-metas-participe-ma` | BR | https://participemais.prefeitura.sp.gov.br/legislation/processes/323 | verificar uso operacional oficial (programa Agentes de Gobierno Abierto) |
| 6 | `BR-5a-conferencia-nacional-de-ct-i-sistemat` | BR | https://5cncti.org.br/ | — |
| 7 | `PA-mansa-idea-pacto-del-bicentenario` | PA | https://mansaidea.com/ | proceso (Pacto del Bicentenario) 2020-21; la IA organiza ese corpus en 2024; sociedad civil; tecnología de IA sin identificar; ¿corpus histórico vs proceso activo? |
| 8 | `CL-lxs-400-chile-delibera` | CL | https://www.senado.cl/noticias/participacion-ciudadana/chile-delibera-lxs-400-un-fin-de-semana-de-democracia-deliberativa-online | 2021; nuevo para el índice |
| 9 | `CO-isidatainsights-reto-de-ciudad-datos-con` | CO | https://www.sdp.gov.co/noticias/bogota-cuenta-nueva-solucion-optimizar-analisis-de-informacion-cualitativa-basada-ciencia-tecnologia | verificar integración operativa y aplicación a un proceso participativo concreto |
| 10 | `CL-el-chile-que-queremos-ecqq-minciencia` | CL | https://github.com/MinCiencia/ECQQ | evidencia fuerte (código público); verificar que sea distinto del baseline 'Estudio dIAlogos' |

## B. DUDOSOS — resolver elegibilidad (8)

| Prioridad | caso_id | País | URL(s) a fetchear | Qué resolver |
|---|---|:---:|---|---|
| 1 | `BR-opa-piaui-presupuesto-participativo-digi` | BR | https://opa.seplan.pi.gov.br/ | confirmar rol de IA sobre contenido |
| 2 | `TT-engagett-plataforma-go-vocal` | TT | https://engage.gov.tt/projects/national-digital-transformation-strategy | confirmar tier/activación de IA de Go Vocal con MDT/MPAAI |
| 3 | `VE-plan-de-la-patria-7-transformaciones-ia` | VE | https://www.correodelorinoco.gob.ve/venezuela-impulsa-el-debate-sobre-inteligencia-artificial-bajo-principios-de-soberania-y-etica/ | fuente estatal única; ningún proveedor/académico corrobora; verificar con MPPP/MINCYT |
| 4 | `BR-catedra-brasil-co-lab-usp-ia-generativa` | BR | https://colab.each.usp.br/blog/2025/03/28/a-ia-generativa-e-o-futuro-da-participacao-cidada-pesquisas-em-andamento/ | piloto búsqueda ampliada; investigación/prototipo |
| 5 | `CU-consulta-popular-codigo-de-las-familias` | CU | https://oncubanews.com/cuba/softwares-cubanos-seran-utilizados-en-el-proceso-de-consulta-popular-sobre-el-codigo-de-las-familias/  ; https://www.granma.cu/cuba/2022-01-24/herramientas-digitales-seran-claves-durante-la-consulta-popular-del-codigo-de-las-familias-24-01-2022-13-01-18 | 2022; verificar si 'análisis inteligente' es NLP/ML o lógica de reglas (Datys/UCI). CU pasa de 0 a 1 señal. |
| 6 | `CO-ia-para-participacion-en-el-pot-de-bogot` | CO | https://controlvisible.auditoria.gov.co/index.php/rcf/article/view/63 | ¿piloto implementado o propuesta de diseño? verificar |
| 7 | `CO-dnp-dialogos-regionales-vinculantes-pnd` | CO | https://dialogosregionales.dnp.gov.co/ | confirmar si la sistematización usó NLP/IA o codificación manual |
| 8 | `CL-senador-virtual-crowdlaw-goblab-uai-imfd` | CL | https://goblab.uai.cl/en/espanol-sistematizando-la-participacion-ciudadana/ | investigación; confirmar aplicación en producción |
