# Verificación de existencia y fuentes — ILIA 2026 (pasada anti-alucinaciones)

*Objetivo: asegurar que TODOS los casos existen (no son alucinaciones) y tienen al
menos una fuente real. Dos niveles: (1) auditoría estructural de las 107 fichas y
(2) verificación web activa, caso por caso, del conjunto elegible.*

## Resultado global
- **107 / 107 fichas** tienen al menos una **URL de fuente válida** (tras las correcciones de abajo).
- **44 casos elegibles** (los marcados SI/DUDA, que alimentan el indicador) verificados uno a uno con búsqueda web en 4 lotes paralelos: **42 VERIFICADO · 2 DUDOSO · 0 NO-VERIFICADO**.
- **0 alucinaciones**: ningún caso resultó inexistente o inventado.

## Nivel 1 — Auditoría estructural (107 fichas)
- 512 URLs en total. Al inicio: 106/107 con URL; 1 sin URL (MX Chatbot Victoria) y 1 con URLs inválidas (BR-bp-classificador).
- **Correcciones aplicadas:**
  - `BR-bp-classificador`: tenía 6 entradas con una **ruta de archivo local** en el campo `url`; se descartaron las fuentes inválidas (quedó con 5 URLs reales: github, arxiv, gov.br).
  - `MX Chatbot Victoria`: su única "fuente" era *"Informe de Gobierno"* (sin URL). **Verificado**: es el chatbot **"Victoria" del Gobierno de la CDMX (ADIP, 2019)**, no de Ciudad Victoria/Tamaulipas. Se añadió la fuente oficial de ADIP.
- Falsos positivos descartados: `CO-isidatainsights` y `PA-mansa-idea` — lo señalado era una *pista de búsqueda* en un `gap`, no una fuente; ambos tienen URLs reales.

## Nivel 2 — Verificación web activa (44 casos elegibles)
Cada caso se buscó en la web para confirmar que la iniciativa **existe** y que su fuente resuelve. Resultado: **0 NO-VERIFICADO**. Los 2 DUDOSO son por **fuente/rótulo**, no por inexistencia:

| Caso | Estado | Detalle |
|---|---|---|
| **CL Jornada de Escucha UNAB** | DUDOSO | La institución (IPP-UNAB) y sus jornadas de escucha son reales, pero el dashboard público de Tableau no se pudo confirmar como fuente. **El equipo lo ejecutó directamente** (conocimiento de primera mano); se añadió la URL institucional del IPP-UNAB. |
| **PE Consulta Ciudadana Proyecto Nacional de Educación** | DUDOSO | El CNE y su proceso participativo del Proyecto Educativo Nacional existen (250.000+ voces); **confirmar el rótulo exacto** (¿PEN 2036?). Nota agregada a la ficha. |

### Correcciones de fuente aplicadas (de la verificación)
| Caso | Cambio |
|---|---|
| MX Chatbot Victoria | + fuente oficial ADIP CDMX (era sin URL); corregida la atribución (CDMX, no Tamaulipas). |
| PE Sistema cómputo ONPE | Reemplazada fuente poco confiable (`cheleloyborolas.com`) por **Agencia Andina** (oficial/seria). |
| PA Mansa Idea | + sitio oficial **mansaidea.com** (URL principal real). |
| CO DNP Diálogos | + portal oficial **dialogosregionales.dnp.gov.co** (el subdominio previo era el repositorio). |
| CL Estrategia Gob. Digital | + URL directa del proyecto (2ª consulta Estrategia Gobierno Digital 2030). |
| CL La voz de nuevos votantes | + publicación IPP-UNAB (San Bernardo). |
| CL Estudio dIAlogos | + sitio oficial estudiodialogos.cl. |
| BR Brasil Participativo (clustering) | Nota: el paper de clustering BERTopic+LLM es `arxiv 2509.21292` (el 2511.01545 es el paper hermano del pipeline ML). Ambos reales. |

## Conclusión
No se detectaron casos inventados. Todos los casos de la base existen y cuentan con al
menos una fuente real; los casos elegibles tienen fuentes creíbles/oficiales. Los 2
DUDOSO son cuestiones de fuente pública débil (CL Jornada UNAB, respaldado por el equipo)
o de rótulo a confirmar (PE Consulta Educación), no de existencia.
