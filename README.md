# Lab 8 — Visualización de Datos con Matplotlib y Seaborn

Ejercicio práctico de exploración de librerías de visualización en Python.
Se generan **8 gráficos con Matplotlib** y **12 gráficos con Seaborn** a partir
de un dataset simulado de ventas, analizando cada gráfico según su tipo,
propósito y audiencia objetivo.

---

## Estructura del repositorio

```
lab_08/
├── lab_08_visualizacion.py       # Script principal
├── ventas_simuladas.csv          # Dataset de entrada
├── README.md                     # Este archivo
├── MAT_01_step.png
├── MAT_02_funnel_vendedor.png
├── MAT_03_histograma.png
├── MAT_04_boxplot.png
├── MAT_05_barras_producto.png
├── MAT_06_barras_vendedor.png
├── MAT_07_stackplot.png
├── MAT_08_tendencia_mensual.png
├── SNS_01_scatter.png
├── SNS_02_relplot.png
├── SNS_03_funnel_categorias.png
├── SNS_04_residplot.png
├── SNS_05_histograma.png
├── SNS_06_heatmap.png
├── SNS_07_boxplot.png
├── SNS_08_barras_promocion.png
├── SNS_09_barras_galletas_mes.png
├── SNS_10_lineplot_dia_semana.png
├── SNS_11_violin_vendedor.png
└── SNS_12_countplot.png
```

---

## Preparar el entorno

### Requisitos

- Python 3.9+
- pip

### Instalación de dependencias

```bash
pip install pandas matplotlib seaborn
```

> Si usas un entorno virtual (recomendado):
>
> ```bash
> python -m venv venv
> source venv/bin/activate        # Linux / macOS
> venv\Scripts\activate           # Windows
> pip install pandas matplotlib seaborn
> ```

### Ejecutar el script

Coloca `ventas_simuladas.csv` en la misma carpeta que el script y ejecuta:

```bash
python lab_08_visualizacion.py
```

Los 20 gráficos se guardarán automáticamente en la misma carpeta.

---

## Dataset

El archivo `ventas_simuladas.csv` contiene registros de ventas con las
siguientes columnas:

| Columna           | Descripción                              |
|-------------------|------------------------------------------|
| `Fecha`           | Fecha de la transacción                  |
| `Producto`        | Nombre del producto vendido              |
| `Cantidad`        | Unidades vendidas                        |
| `Precio Unitario` | Precio por unidad                        |
| `Vendedor`        | Nombre del vendedor responsable          |
| `Promoción`       | Indica si la venta tuvo promoción o no   |

El script calcula columnas derivadas: `Ventas Totales`, `Mes`, `Año`,
`Dia Semana` y `Categoria`.

---

## Gráficos generados

### Matplotlib (8 gráficos)

| # | Archivo | Tipo | Propósito | Audiencia |
|---|---------|------|-----------|-----------|
| 1 | `MAT_01_step.png` | Gráfico de gradas | Ventas acumuladas en el tiempo | Gerencia, equipo financiero, inversionistas |
| 2 | `MAT_02_funnel_vendedor.png` | Embudo | Comparar ventas entre vendedores | Supervisores de ventas, gerencia comercial |
| 3 | `MAT_03_histograma.png` | Histograma | Distribución de montos de ventas | Gerencia de Operaciones |
| 4 | `MAT_04_boxplot.png` | Boxplot | Estabilidad y rango de precios por producto | Auditores, Analistas Financieros |
| 5 | `MAT_05_barras_producto.png` | Barras horizontales | Productos con mayor venta total | Equipo de ventas, abastecimiento |
| 6 | `MAT_06_barras_vendedor.png` | Barras verticales | Desempeño de ventas por vendedor | Equipo de ventas |
| 7 | `MAT_07_stackplot.png` | Área apilada | Aporte de cada categoría por mes | Equipo comercial estratégico |
| 8 | `MAT_08_tendencia_mensual.png` | Líneas | Tendencia mensual de ventas por año | Gerentes, directores comerciales |

### Seaborn (12 gráficos)

| # | Archivo | Tipo | Propósito | Audiencia |
|---|---------|------|-----------|-----------|
| 1 | `SNS_01_scatter.png` | Dispersión | Relación precio vs cantidad por promoción | Marketing, analistas de precios |
| 2 | `SNS_02_relplot.png` | Líneas por facetas | Evolución mensual de ventas por año | Planificación, gerencia |
| 3 | `SNS_03_funnel_categorias.png` | Embudo | Ventas por categoría | Compras, estrategia comercial |
| 4 | `SNS_04_residplot.png` | Residuos de regresión | Ajuste de modelo lineal precio-ventas | Analistas de datos, estadística |
| 5 | `SNS_05_histograma.png` | Histograma + KDE | Distribución de ventas totales | Gerencia de Operaciones |
| 6 | `SNS_06_heatmap.png` | Mapa de calor | Desempeño por vendedor y producto | Dirección Comercial |
| 7 | `SNS_07_boxplot.png` | Boxplot | Dispersión de precios unitarios | Auditores, Analistas Financieros |
| 8 | `SNS_08_barras_promocion.png` | Barras horizontales | Impacto de promociones en ventas | Equipo de marketing |
| 9 | `SNS_09_barras_galletas_mes.png` | Barras verticales | Cantidad vendida de Galletas y snacks por mes | Equipo ejecutivo estratégico |
| 10 | `SNS_10_lineplot_dia_semana.png` | Líneas | Ventas por día de la semana | Operaciones, gerentes de tienda |
| 11 | `SNS_11_violin_vendedor.png` | Violín | Variabilidad de ventas por vendedor | Supervisores, gerentes de ventas |
| 12 | `SNS_12_countplot.png` | Barras de conteo | Transacciones por producto y promoción | Operaciones, inventario |

---

## Librerías utilizadas

| Librería      | Versión mínima | Uso |
|---------------|---------------|-----|
| `pandas`      | 1.5+          | Carga, limpieza y transformación de datos |
| `matplotlib`  | 3.6+          | Generación de gráficos base (8 gráficos) |
| `seaborn`     | 0.12+         | Gráficos estadísticos avanzados (12 gráficos) |
| `os`          | stdlib        | Manejo de rutas de archivos |
