# data/external/ — insumos externos NO versionados

Archivos grandes/externos que el pipeline cruza pero no mantiene bajo control de
versiones (ver `.gitignore`).

- `BD_IA_LATAM.xlsx` — inventario general de IA en el sector público de América
  Latina (BD_IA_LATAM, p. ej. Gutiérrez et al.). Insumo del canal **A.15**
  (`src/cruce_inventario_ia_latam.py`). Colocar aquí el .xlsx para reproducir el
  cruce; las salidas (CSV de pool + reporte) sí se versionan.
