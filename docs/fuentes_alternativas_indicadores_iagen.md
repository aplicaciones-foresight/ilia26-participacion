# Fuentes alternativas para los indicadores de IA Generativa del ILIA

**Fecha:** 2026-07-06 · **Elaborado por:** equipo Foresight (investigación asistida con agentes de búsqueda web)

## 0. Problema

El CENIA no podrá recolectar tres indicadores del ILIA cuya fuente original era **Sensor Tower**
(que absorbió a data.ai/App Annie en 2024; la metodología del ILIA 2025 cita expresamente
"según datos de Sensor Tower…"):

| # | Indicador | Definición original |
|---|-----------|---------------------|
| 1 | **Usuarios de IA Generativa** | N° total de usuarios de apps móviles de IAGen por suscriptores móviles únicos |
| 2 | **Tiempo de uso de IA Generativa** | Promedio mensual de minutos/día (a dic. 2024) de uso de apps móviles de IAGen |
| 3 | **Gasto en IA Generativa** | Gasto promedio en USD por usuario activo de apps móviles de IAGen (a dic. 2024) |

**Universo:** los 20 países ILIA (AR, BO, BR, CL, CO, CR, CU, DO, EC, GT, HN, JM, MX, PA, PE,
PY, SV, TT, UY, VE) + 5 extras. *Supuesto de trabajo:* los 5 extras son Nicaragua, Haití,
Belice, Guyana y Surinam (no estaban definidos en el repo; la evaluación de cobertura abajo
los incluye y en general aplica a cualquier país pequeño de la región).

Se lanzaron 4 líneas de búsqueda en paralelo: (a) plataformas de app intelligence,
(b) encuestas comparativas internacionales, (c) telemetría de las propias plataformas de IA,
(d) datos de gasto del consumidor y denominadores.

---

## 1. Resumen ejecutivo

1. **No existe un reemplazo 1:1 de Sensor Tower.** Ninguna plataforma de app intelligence
   (Similarweb, Apptopia, AppMagic, Appfigures, Comscore) cubre los 25 países para
   MAU/tiempo/gasto de apps móviles de IAGen. Todas convergen en el mismo patrón "big 6"
   (BR, MX, AR, CO, CL, PE): es un límite estructural de los paneles de medición, no de un
   proveedor puntual.
2. **Sí existe un reemplazo excelente para el indicador de Usuarios**, si se acepta
   reformularlo de "usuarios de apps móviles / suscriptores móviles" a "% de la población que
   usa IAGen": el **Microsoft AI Diffusion Report** — dataset abierto (licencia MIT, CSV en
   GitHub), con serie semestral/trimestral desde H1-2025 y cifras para **23 de los 25 países**
   (faltan solo Trinidad y Tobago y Belice). Se puede triangular con OpenAI Signals y el
   Anthropic Economic Index, ambos también abiertos.
3. **Para Tiempo de uso no hay reemplazo directo** (minutos/día por país no los publica nadie
   con esta cobertura). La opción viable es sustituir el concepto "tiempo" por **intensidad de
   uso** (mensajes per cápita de OpenAI Signals y/o índice AUI de Anthropic), con cobertura
   amplia pero con exclusiones de países pequeños en el caso de OpenAI.
4. **Para Gasto no encontramos un buen reemplazo** con cobertura de los 25 países. Las fuentes
   de gasto real (IAP) solo desglosan Brasil públicamente; Statista mezcla B2B+B2C; y hay
   países donde el gasto es estructuralmente no medible (Cuba sin App Store ni pagos en Google
   Play) o subestimado (Venezuela, por fricciones de pago). Recomendación: **retirar o
   redefinir el indicador**, no forzar un proxy inválido.

---

## 2. Hallazgos por tipo de fuente

### 2.1 Plataformas de app intelligence (la vía "continuista")

| Plataforma | Métricas de las 3 buscadas | Cobertura LatAm verificada | Acceso/costo |
|---|---|---|---|
| **Sensor Tower** (incl. data.ai) | Las 3 (MAU, tiempo, IAP; el gasto/usuario se deriva) | BR, AR, MX citados públicamente; panel de uso probablemente solo mercados grandes (referencia: en EMEA su panel de uso cubre 20 de 63 países) | US$30k–150k+/año, sin precio público ni programa académico documentado |
| **Similarweb App Intelligence** | MAU, sesiones, retención, ingresos (58 países, lista no verificable) | No confirmada por país para apps; su lista amplia de países corresponde a otro producto (Sales Intelligence, tráfico web B2B) | ~US$199–999+/mes web; apps con cotización |
| **Comscore Mobile Metrix** | MAU y engagement (panel real, no modelado) | Solo AR, BR, CL, CO, MX, PE | Contrato empresarial |
| **Apptopia** | Descargas, ingresos, uso ("top 60 countries", lista no verificable) | No confirmada | US$15k–100k+/año |
| **AppMagic** | Descargas e ingresos modelados (no MAU/tiempo/gasto por usuario) | Menciona CO, EC, PE, AR, DO, BR en análisis | Freemium + pago |
| **Appfigures** | Descargas/ingresos estimados; el módulo de "usage" solo funciona para apps propias | Amplia para descargas, inútil para MAU/tiempo de terceros | El más barato (créditos prepagados); existe programa gratuito "for Journalists" |

**Conclusión:** la vía continuista (pagar otra plataforma) no resuelve la cobertura: en el
mejor caso se obtienen 6 países, a costo alto.

### 2.2 Telemetría de plataformas de IA (la vía nueva — mejor cobertura)

**Microsoft AI Diffusion Report (AI Economy Institute)** — ⭐ hallazgo principal, verificado
leyendo los PDF primarios (H2-2025 y Q1-2026):

- Métrica: **"AI User Share"** = % de la población en edad de trabajar (15–64) que usó un
  producto de IAGen en el período. Derivada de telemetría agregada de Microsoft, ajustada por
  cuota de mercado de SO/dispositivo, penetración de internet y población.
- **Dataset abierto, licencia MIT**: `github.com/microsoft/ai-diffusion-report`
  (CSV: `data/AI_Diffusion_Q12026_Update.csv`). Paper técnico: Misra et al. 2025, arXiv:2511.02781.
- Periodicidad: semestral en 2025, **trimestral desde Q1-2026**.
- **Cobertura: 23/25 países** con serie completa H1-2025 → Q1-2026. Valores Q1-2026 (extracto):
  CR 28.5%, DO 24.8%, UY 24.6%, CO 24.5%, JM 24.0%, PA 23.3%, CL 22.7%, AR 21.9%, MX 20.1%,
  EC 19.5%, BR 19.1%, SV 18.3%, GT 16.4%, PE 16.4%, HN 14.0%, BO 12.7%, PY 12.2%, NI 11.8%,
  GY 10.3%, SR 10.3%, VE 10.3%, HT 8.5%, CU 6.7%. **Faltan: TT y BZ.**
- Limitaciones: un solo proveedor (telemetría Windows/Bing/Copilot; subpondera uso
  exclusivamente móvil), estimación modelada, serie corta (desde 2025). Ojo: GY, SR y VE
  comparten valores idénticos en las tres olas — sugiere agrupamiento/imputación regional para
  países con poca señal; conviene tratarlos con cautela y documentarlo.

**OpenAI Signals** (`openai.com/signals`): ranking de países por **mensajes de ChatGPT per
cápita** (usuarios individuales, ventana jul-2024→mar-2026, licencia declarada CC BY 4.0).
Restricción relevante: análisis limitado a países con **población ≥5M**, lo que excluiría a
UY, PA, JM, TT, GY, SR y BZ (CR queda en el borde). Pendiente verificar el bulk download
(bloqueado por red en esta sesión). Complemento: el paper NBER w34255 ("How People Use
ChatGPT") documenta adopción alta en países de ingreso medio (Brasil ≈ niveles de EE.UU./Corea).

**Anthropic Economic Index (AUI)**: índice de uso de Claude per cápita (uso del país /
población 15–64), **dataset abierto en Hugging Face** (`Anthropic/EconomicIndex`), 150+
países, releases recurrentes. Verificado por triangulación: Brasil AUI 0.70x, México 0.44x.
Limitación: mide solo Claude (perfil profesional/desarrollador; subrepresenta uso masivo).

**Cloudflare Radar** (API gratuita) y **Similarweb tráfico web**: solo rankings relativos o
tráfico web (no apps, no usuarios absolutos) — útiles únicamente como triangulación.

### 2.3 Encuestas comparativas internacionales

Ninguna encuesta comercial cubre más de 6–7 de los 25 países; todas concentradas en el big 6:

| Fuente | Países de los 25 | Mide | Acceso |
|---|---|---|---|
| Ipsos AI Monitor (30–32 países) | AR, BR, CL, CO, MX, PE | Uso/actitudes IAGen | PDF gratis |
| Google/Ipsos "Our Life with AI" | AR, BR, MX | Uso de chatbots | Gratis |
| KPMG–U. Melbourne "Trust in AI" (47 países) | AR, BR, CL, CO, **CR**, MX | Uso IAGen trabajo/vida | PDF gratis |
| Reuters Institute Digital News Report (48 mercados, anual, serie desde 2024) | AR, BR, CL, CO, MX, PE | % que usó IAGen (semanal/alguna vez) | Gratis + plataforma de datos |
| GWI Core | AR, BR, CO, MX (+PE) | Uso de herramientas IA último mes | Pago (SaaS) |
| Pew "Views of AI" | AR, BR, MX (**cara a cara**, la única probabilística) | Awareness/actitudes | Gratis |
| Estadística oficial nacional | BR (Cetic.br TIC Domicílios 2025: 32% de internautas usó IAGen), CO (DANE ENTIC 2024: 18% usó herramientas de IA), AR+UY (CEPE-Fundar/BID 2025) | Uso IAGen, muestras probabilísticas de hogares | Gratis |

Notas: los paneles online (Ipsos, GWI, Statista, YouGov) no son probabilísticos —
sobrerrepresentan población urbana/conectada. Latinobarómetro cubre 18 países pero **no tiene
pregunta de IA confirmada** (revisar cuestionario 2025; sería la mejor vía de cobertura si la
incorporara — posible gestión de CENIA). El BID no tiene encuesta regional propia, pero
financia encuestas nacionales tipo CEPE-Fundar y declara agenda de expandirlas (posible socio).

### 2.4 Gasto del consumidor

- **Sensor Tower "State of AI Apps" / "State of Mobile"**: gasto IAP en apps de IAGen; público
  solo agregado regional (LatAm +147% semestral H2-24→H1-25) y Brasil (#7 global en la
  categoría). Desglose fino solo en plataforma paga, y aun ahí probablemente solo mercados grandes.
- **Statista Market Insights "Generative AI"**: revenue por país solo para BR, MX, CL, CO, PE
  (5/25). **Limitación crítica verificada:** la cifra es mercado total **B2B+B2G+B2C** (método
  top-down desde funding/PIB), no gasto de consumidores; no publica "gasto promedio por
  usuario" para esta vertical. Costo desde ~€199/mes.
- **Appfigures**: gasto global en apps de IA (US$1.4B en 2024; EE.UU. concentra ~2/3), sin
  desglose LatAm público. Evidencia útil: volumen de usuarios ≠ gasto (ChatGPT: India 13.7% de
  instalaciones, EE.UU. 40% de ingresos) — un indicador de gasto castigaría doblemente a la región.
- **IDC / eMarketer**: gasto empresarial (B2B) o solo EE.UU. — no aplican.
- **Medibilidad estructural**: **Cuba** no tiene App Store y Google Play bloquea compras →
  gasto no medible (≈0 artificial). **Venezuela** con fricciones severas de pago (tarjetas
  virtuales, Zelle, cripto) → subregistro sistemático. Haití/Guyana con fricciones parciales.

### 2.5 Denominadores

- **ITU DataHub** (gratuito, CC BY-NC-SA): suscripciones móviles-celulares e internautas para
  los 25 países (verificado incl. CU, VE, HT, GY, SR). Ojo: son **conexiones/SIMs**, no
  "suscriptores únicos".
- **GSMA Intelligence**: sí publica "suscriptores móviles únicos" (el denominador original del
  ILIA), agregado regional gratuito (~485M únicos a fines de 2025); el desglose por país
  requiere registro (cuenta institucional gratuita posible — probar con correo de CENIA) o
  suscripción.
- **Población 15–64** (denominador de Microsoft/Anthropic): Banco Mundial/ONU, gratuito, 25/25.

---

## 3. Propuesta metodológica

### Indicador 1 — Usuarios de IA Generativa → **REEMPLAZABLE (recomendado)**

**Reformular** como *"Penetración de uso de IA generativa: % de la población en edad de
trabajar (15–64) que usó herramientas de IA generativa en el período"*.

- **Fuente primaria:** Microsoft AI Diffusion Report (CSV abierto, MIT). Cobertura 23/25,
  serie trimestral, reproducible y citable.
- **Triangulación (robustez):** OpenAI Signals (mensajes per cápita, países ≥5M) y Anthropic
  Economic Index (AUI, 150+ países). Reportar correlación entre fuentes como validación; si se
  quiere un solo número, usar Microsoft y dejar las otras como contraste en anexo.
- **TT y BZ (los 2 faltantes):** (a) marcar como sin dato; o (b) imputar con el AUI de
  Anthropic reescalado contra los países donde ambas fuentes existen (documentando el método).
  Recomendamos (a) para el índice y (b) solo como referencia.
- **Cambio de denominador:** de "suscriptores móviles únicos" a "población 15–64". Es una
  mejora: elimina la dependencia de GSMA (pago) y de la distinción SIMs/personas. Si se quiere
  conservar comparabilidad conceptual con 2025, se puede publicar además la serie reescalada
  usuarios/suscriptores-únicos con GSMA para los países disponibles.
- **Ruptura de serie:** documentar explícitamente que 2026 cambia de fuente (Sensor Tower →
  Microsoft) y de universo (apps móviles → cualquier dispositivo). No empalmar series; reiniciar base 2025.

### Indicador 2 — Tiempo de uso → **SIN REEMPLAZO DIRECTO; sustituir el concepto por "intensidad"**

Nadie publica minutos/día por país fuera de los paneles pagos de app intelligence, y estos
cubren ~6 países. Opciones, en orden de recomendación:

1. **Sustituir por "Intensidad de uso de IAGen":** mensajes de ChatGPT per cápita (OpenAI
   Signals) como métrica principal, con AUI de Anthropic como contraste. Mide *cuánto* se usa,
   que es el constructo que "minutos/día" intentaba capturar. Costo: cambia la unidad (deja de
   ser tiempo) y OpenAI excluye países <5M (UY, PA, JM, TT, GY, SR, BZ) → cobertura ~18/25;
   para los excluidos, AUI de Anthropic o sin dato.
2. **Retirar el indicador** y absorber su peso en el indicador 1 (penetración). Defendible:
   penetración e intensidad están altamente correlacionadas y el constructo "adopción" queda cubierto.
3. **Mantener minutos/día contratando Sensor Tower** solo para el big 6 y dejar 19 países sin
   dato. No recomendado: cobertura inaceptable para un índice regional y costo US$30k+.

**Recomendación: opción 1**, sujeta a verificar el bulk download de OpenAI Signals (no se pudo
confirmar en esta sesión por bloqueos de red); si no es utilizable, opción 2.

### Indicador 3 — Gasto en IA Generativa → **SIN BUEN REEMPLAZO; recomendamos retirarlo**

Razones acumuladas:

- Ninguna fuente publica gasto de consumidor en IAGen por país para más de ~5 de los 25, y la
  única candidata multi-país (Statista) mide mercado total B2B+B2G+B2C — constructo distinto.
- El gasto es **estructuralmente no medible** en Cuba y fuertemente subestimado en Venezuela
  (y parcialmente en Haití/Guyana) por ausencia/fricción de tiendas y medios de pago: el
  indicador confundiría "no gasta" con "no puede pagar por canales medibles".
- La evidencia de Appfigures (EE.UU. ~2/3 del gasto global) muestra que el gasto refleja poder
  de compra y paridad de precios más que adopción — dudoso valor conceptual para un índice de
  desarrollo de IA regional.

Si retirar no es aceptable, la alternativa menos mala es redefinirlo como *"disposición a pagar
por IAGen"* vía encuesta (Ipsos AI Monitor tiene cortes comprables), pero solo cubriría el big
6 y con panel no probabilístico — lo desaconsejamos para el índice; podría ir como recuadro
analítico del informe, no como indicador puntuado.

### Ponderación / consecuencia para el índice

Si se adopta la propuesta: el sub-pilar pasa de 3 indicadores a 2 (penetración + intensidad),
ambos con fuente abierta, licencia permisiva, serie temporal y cobertura ≥18/25 con 23/25 en el
principal. Redistribuir pesos dentro del sub-pilar y documentar el cambio en el anexo metodológico.

---

## 4. Verificaciones pendientes (antes de comprometer la metodología)

1. **OpenAI Signals**: confirmar bulk download/CSV y lista exacta de países (`openai.com/signals/data-download/`) — bloqueado por red en esta sesión.
2. **Anthropic EconomicIndex** (Hugging Face): descargar release más reciente y extraer AUI para los 25 países (verificados por triangulación solo BR y MX).
3. **Microsoft AI Diffusion**: descargar el CSV y revisar el flag/nota metodológica de los países con valores idénticos (GY=SR=VE) para confirmar si hay imputación regional; consultar por qué faltan TT y BZ (issue en el repo de GitHub es viable).
4. **GSMA Intelligence**: probar registro institucional gratuito de CENIA para el denominador "suscriptores únicos" por país (solo si se conserva el denominador original).
5. **Latinobarómetro 2025**: revisar si el cuestionario incorporó pregunta de uso de IA (cubriría 18 países con muestra probabilística; gestión de incidencia posible para 2026/27).
6. **Confirmar la lista real de los 5 países extra** (aquí se asumió NI, HT, BZ, GY, SR).

## 5. Fuentes principales (URLs)

- Microsoft AI Diffusion Report: https://github.com/microsoft/ai-diffusion-report · paper: https://arxiv.org/abs/2511.02781
- OpenAI Signals: https://openai.com/signals/data/ · paper NBER: https://www.nber.org/papers/w34255
- Anthropic Economic Index: https://huggingface.co/datasets/Anthropic/EconomicIndex · https://www.anthropic.com/economic-index
- Sensor Tower State of AI Apps / State of Mobile: https://sensortower.com/report/state-of-ai-apps-2025 · https://sensortower.com/report/state-of-mobile-2026
- Statista Market Insights Generative AI: https://www.statista.com/outlook/tmo/artificial-intelligence/generative-ai/brazil (y páginas análogas MX/CL/CO/PE)
- Reuters Institute DNR: https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2025
- KPMG–Melbourne Trust in AI: https://kpmg.com/xx/en/our-insights/ai-and-technology/trust-attitudes-and-use-of-ai.html
- Ipsos AI Monitor: https://www.ipsos.com/en-us/ipsos-ai-monitor-2024 (y ediciones 2025/2026)
- Cetic.br TIC Domicílios: https://cgi.br/ · DANE ENTIC: https://www.dane.gov.co/ · CEPE-Fundar: https://cepe-fundar.github.io/encuesta.html
- ITU DataHub: https://datahub.itu.int · GSMA Mobile Economy LatAm: https://www.gsmaintelligence.com/research/the-mobile-economy-latin-america-2025
- Cloudflare Radar AI Insights: https://radar.cloudflare.com/ai-insights

*Advertencia de verificación: varias páginas (Similarweb, Apptopia, DataReportal, PDFs de Ipsos
y Pew, Hugging Face, openai.com) devolvieron 403/bloqueo de red durante la investigación; en
esos casos las afirmaciones provienen de fragmentos indexados y triangulación de fuentes
secundarias, y están marcadas como tales en el texto.*
