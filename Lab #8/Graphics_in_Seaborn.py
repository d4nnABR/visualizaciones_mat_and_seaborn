"""
Lab 8 - Visualización: 8 gráficos Matplotlib + 12 gráficos Seaborn
Estructura: Tipo | Propósito | Audiencia
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =============================================================================
# CONFIGURACIÓN Y CARGA DE DATOS (una sola vez)
# =============================================================================
ruta_csv = os.path.join(os.path.dirname(__file__), "ventas_simuladas.csv")
df = pd.read_csv(ruta_csv, encoding="utf-8")

df["Ventas Totales"] = df["Cantidad"] * df["Precio Unitario"]
df["Fecha"] = pd.to_datetime(df["Fecha"], errors="coerce")
df["Mes"] = df["Fecha"].dt.month
df["Año"] = df["Fecha"].dt.year
df["Dia Semana"] = df["Fecha"].dt.day_name()

map_categoria = {
    "Leche": "Lácteos", "Pan": "Panadería", "Café": "Bebidas calientes",
    "Té": "Bebidas calientes", "Chocolate": "Bebidas calientes",
    "Cereal": "Cereales", "Galletas": "Galletas y snacks", "Azúcar": "Endulzantes"
}
df["Categoria"] = df["Producto"].map(map_categoria).fillna("Otros")

NOMBRES_MES = {1: "Ene", 2: "Feb", 3: "Mar", 4: "Abr", 5: "May", 6: "Jun",
               7: "Jul", 8: "Ago", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dic"}
fig_std, color_bar = (8, 6), "#48C9B0"


def _etiquetas_barras_h(ax, fmt=",.0f"):
    for p in ax.patches:
        w = p.get_width()
        ax.text(w + 5, p.get_y() + p.get_height() / 2, f"{w:{fmt}}", va="center", fontsize=10, fontweight="bold")


def _etiquetas_barras_v(ax, fmt=",.0f"):
    for p in ax.patches:
        h = p.get_height()
        ax.text(p.get_x() + p.get_width() / 2, h + 5, f"{h:{fmt}}", ha="center", va="bottom", fontsize=10, fontweight="bold")


# =============================================================================
# 8 GRÁFICOS CON MATPLOTLIB
# =============================================================================

# --- MAT 1: Step Chart ---
# Tipo: Líneas escalonadas | Propósito: Evolución de ventas acumuladas
# Audiencia: Gerencia, equipo financiero, inversionistas
ventas_fecha = df.groupby("Fecha")["Ventas Totales"].sum().reset_index().sort_values("Fecha")
ventas_fecha["Acumulado"] = ventas_fecha["Ventas Totales"].cumsum()
fig, ax = plt.subplots(figsize=(10, 5))
ax.step(ventas_fecha["Fecha"], ventas_fecha["Acumulado"], where="post", color="steelblue", linewidth=2)
ax.set_xlabel("Fecha")
ax.set_ylabel("Ventas acumuladas")
ax.set_title("Gráfico de gradas: Ventas acumuladas en el tiempo")
ax.tick_params(axis="x", rotation=45)
plt.tight_layout()
plt.show()

# --- MAT 2: Funnel Chart ---
# Tipo: Barras horizontales proporcionales | Propósito: Comparar ventas por vendedor
# Audiencia: Supervisores de ventas, gerencia comercial, RR.HH
dat = df.groupby("Vendedor")["Ventas Totales"].sum().sort_values(ascending=False).reset_index()
fig, ax = plt.subplots(figsize=fig_std)
y_pos = range(len(dat))
anchos = dat["Ventas Totales"] / dat["Ventas Totales"].max()
ax.barh(y_pos, anchos, left=(1 - anchos) / 2, height=0.7, color="steelblue", edgecolor="white", linewidth=1)
ax.set_yticks(y_pos)
ax.set_yticklabels(dat["Vendedor"])
ax.set_xlim(0, 1)
ax.set_xticks([])
ax.set_title("Funnel chart: Ventas por vendedor")
plt.tight_layout()
plt.show()

# --- MAT 3: Histograma ---
# Tipo: Histograma | Propósito: Distribución de montos de venta
# Audiencia: Gerencia de Operaciones
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(df["Ventas Totales"], bins=15, color=color_bar, edgecolor="black", alpha=0.7)
ax.set_title("Distribución de los Montos de Ventas Totales", fontweight="bold")
ax.set_xlabel("Monto de la Venta ($)")
ax.set_ylabel("Frecuencia")
ax.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

# --- MAT 4: Boxplot ---
# Tipo: Boxplot | Propósito: Variabilidad de precios por producto
# Audiencia: Auditores, analistas financieros
productos = df["Producto"].unique()
datos_bp = [df[df["Producto"] == p]["Precio Unitario"].values for p in productos]
fig, ax = plt.subplots(figsize=(10, 6))
ax.boxplot(datos_bp, labels=productos, patch_artist=True,
           boxprops=dict(facecolor="#a2d2ff", color="blue"), medianprops=dict(color="red"))
ax.set_title("Análisis de Precios Unitarios por Categoría de Producto", fontweight="bold")
ax.set_xlabel("Producto")
ax.set_ylabel("Precio Unitario ($)")
ax.grid(axis="y", linestyle=":", alpha=0.6)
plt.tight_layout()
plt.show()

# --- MAT 5: Barras horizontales (ventas por producto) ---
# Tipo: Barras horizontales | Propósito: Productos que más venden
# Audiencia: Equipo de ventas, abastecimiento
dat = df.groupby("Producto", as_index=False)["Ventas Totales"].sum().sort_values("Ventas Totales", ascending=True)
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(dat["Producto"], dat["Ventas Totales"], color=color_bar)
ax.set_title("Ventas Totales por Producto")
ax.set_xlabel("Ventas Totales")
ax.set_ylabel("Producto")
_etiquetas_barras_h(ax)
plt.tight_layout()
plt.show()

# --- MAT 6: Barras verticales (ventas por vendedor) ---
# Tipo: Barras verticales | Propósito: Desempeño por vendedor
# Audiencia: Equipo de ventas
dat = df.groupby("Vendedor", as_index=False)["Ventas Totales"].sum().sort_values("Ventas Totales", ascending=False)
fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(dat["Vendedor"], dat["Ventas Totales"], color=color_bar)
ax.set_title("Ventas Totales por Vendedor")
ax.set_xlabel("Vendedor")
ax.set_ylabel("Ventas Totales")
plt.xticks(rotation=45, ha="right")
_etiquetas_barras_v(ax)
plt.tight_layout()
plt.show()

# --- MAT 7: Stackplot ---
# Tipo: Área apilada | Propósito: Ventas por mes y categoría
# Audiencia: Equipo comercial estratégico
año_ref = df["Año"].max()
df_año = df[df["Año"] == año_ref].copy()
df_año["Mes"] = df_año["Fecha"].dt.month
dat = df_año.groupby(["Mes", "Categoria"])["Ventas Totales"].sum().reset_index()
pivot = dat.pivot(index="Mes", columns="Categoria", values="Ventas Totales").fillna(0).sort_index()
fig, ax = plt.subplots(figsize=(12, 6))
ax.stackplot(pivot.index, pivot.T.values, labels=pivot.columns)
ax.set_title(f"Ventas Totales por Mes y Categoría - {año_ref}")
ax.set_xlabel("Mes")
ax.set_ylabel("Ventas Totales")
ax.set_xticks(range(1, 13), [NOMBRES_MES[i] for i in range(1, 13)])
ax.legend(title="Categoría", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()
plt.show()

# --- MAT 8: Gráfico de líneas (tendencia mensual) ---
# Tipo: Líneas | Propósito: Evolución ventas mes a mes
# Audiencia: Gerentes de ventas, directores comerciales
ventas_mes = df.groupby(["Año", "Mes"])["Ventas Totales"].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 6))
for año in ventas_mes["Año"].unique():
    d = ventas_mes[ventas_mes["Año"] == año]
    ax.plot(d["Mes"], d["Ventas Totales"], marker="o", label=str(int(año)))
ax.set_title("Tendencia mensual de ventas")
ax.set_xlabel("Mes")
ax.set_ylabel("Ventas Totales ($)")
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.show()

# =============================================================================
# 12 GRÁFICOS CON SEABORN
# =============================================================================
sns.set_theme(style="whitegrid", palette="muted")

# --- SNS 1: Scatter ---
# Tipo: Dispersión | Propósito: Relación precio-cantidad por promoción
# Audiencia: Marketing, analistas de precios
fig, ax = plt.subplots(figsize=fig_std)
sns.scatterplot(data=df, x="Precio Unitario", y="Cantidad", hue="Promoción", ax=ax)
ax.set_title("Cantidad vs Precio por Promoción")
ax.legend(title="Promoción")
plt.tight_layout()
plt.show()

# --- SNS 2: Relplot ---
# Tipo: Líneas por facetas | Propósito: Ventas por mes entre años
# Audiencia: Planificación, gerencia
ventas_ma = df.groupby(["Mes", "Año"])["Ventas Totales"].sum().reset_index()
g = sns.relplot(data=ventas_ma, x="Mes", y="Ventas Totales", col="Año", hue="Año",
                kind="line", palette="crest", linewidth=2, col_wrap=2, height=2.5, aspect=1.2, legend=False)
g.set_titles("Año {col_name}")
g.set_axis_labels("Mes", "Ventas")
plt.tight_layout()
plt.show()

# --- SNS 3: Funnel categorías ---
# Tipo: Embudo | Propósito: Ventas por categoría de producto
# Audiencia: Compras, gerencia de producto
dat = df.groupby("Categoria")["Ventas Totales"].sum().sort_values(ascending=False).reset_index()
fig, ax = plt.subplots(figsize=fig_std)
y_pos = range(len(dat))
anchos = dat["Ventas Totales"] / dat["Ventas Totales"].max()
ax.barh(y_pos, anchos, left=(1 - anchos) / 2, height=0.7,
        color=sns.color_palette("Blues_r", len(dat)), edgecolor="white", linewidth=1)
ax.set_yticks(y_pos)
ax.set_yticklabels(dat["Categoria"])
ax.set_xlim(0, 1)
ax.set_xticks([])
ax.set_title("Funnel chart: Ventas por categoría")
plt.tight_layout()
plt.show()

# --- SNS 4: Residplot ---
# Tipo: Residuos de regresión | Propósito: Ajuste modelo lineal
# Audiencia: Analistas de datos
fig, ax = plt.subplots(figsize=fig_std)
sns.residplot(data=df, x="Precio Unitario", y="Ventas Totales", lowess=True, color="g", ax=ax)
ax.set_title("Residuos: Ventas vs Precio Unitario")
ax.set_ylabel("Residuos")
plt.tight_layout()
plt.show()

# --- SNS 5: Histograma ---
# Tipo: Histograma + KDE | Propósito: Distribución ventas
# Audiencia: Gerencia de Operaciones
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(data=df, x="Ventas Totales", kde=True, color="teal")
ax.set_title("Distribución de Frecuencia de Ventas Totales")
ax.set_xlabel("Monto de Venta ($)")
plt.tight_layout()
plt.show()

# --- SNS 6: Heatmap ---
# Tipo: Mapa de calor | Propósito: Desempeño vendedor-producto
# Audiencia: Dirección Comercial
pivot = df.pivot_table(index="Vendedor", columns="Producto", values="Ventas Totales", aggfunc="sum")
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(pivot, annot=True, fmt=".1f", cmap="YlGnBu", linewidths=0.5)
ax.set_title("Desempeño por Vendedor y Producto")
plt.tight_layout()
plt.show()

# --- SNS 7: Boxplot ---
# Tipo: Boxplot | Propósito: Dispersión precios por producto
# Audiencia: Auditores, analistas financieros
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=df, x="Producto", y="Precio Unitario", hue="Producto", palette="Set2", legend=False)
ax.set_title("Análisis de Dispersión de Precios Unitarios")
ax.set_xlabel("Categoría de Producto")
plt.tight_layout()
plt.show()

# --- SNS 8: Barras ventas por promoción ---
# Tipo: Barras horizontales | Propósito: Impacto de promociones
# Audiencia: Marketing, investigación de mercado
dat = df.groupby("Promoción", as_index=False)["Ventas Totales"].sum().sort_values("Ventas Totales", ascending=False)
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(data=dat, x="Ventas Totales", y="Promoción", color=color_bar)
ax.set_title("Ventas Totales por Promoción")
_etiquetas_barras_h(ax)
plt.tight_layout()
plt.show()

# --- SNS 9: Barras cantidad por mes (categoría) ---
# Tipo: Barras | Propósito: Cantidad vendida por mes de una categoría
# Audiencia: Equipo ejecutivo estratégico
cat_ref = "Galletas y snacks"
df_f = df[(df["Año"] == año_ref) & (df["Categoria"] == cat_ref)].copy()
df_f["Mes"] = df_f["Fecha"].dt.month
dat = df_f.groupby("Mes", as_index=False)["Cantidad"].sum().sort_values("Mes")
dat["Mes_nombre"] = dat["Mes"].map(NOMBRES_MES)
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(data=dat, x="Mes_nombre", y="Cantidad", color=color_bar)
ax.set_title(f"Cantidad Vendida de {cat_ref} por Mes - {año_ref}")
_etiquetas_barras_v(ax, ".0f")
plt.tight_layout()
plt.show()

# --- SNS 10: Lineplot día semana ---
# Tipo: Líneas | Propósito: Ventas por día de la semana
# Audiencia: Gerentes de tienda, operaciones
orden_dias = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
ventas_dia = df.groupby("Dia Semana")["Ventas Totales"].sum().reset_index()
ventas_dia["Dia Semana"] = pd.Categorical(ventas_dia["Dia Semana"], categories=orden_dias, ordered=True)
ventas_dia = ventas_dia.sort_values("Dia Semana")
fig, ax = plt.subplots(figsize=fig_std)
sns.lineplot(data=ventas_dia, x="Dia Semana", y="Ventas Totales", marker="o")
ax.set_title("Tendencia de ventas por día de la semana")
ax.set_xlabel("Día de la semana")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- SNS 11: Violin vendedor ---
# Tipo: Violin | Propósito: Distribución ventas por vendedor
# Audiencia: Gerentes y supervisores de ventas
fig, ax = plt.subplots(figsize=fig_std)
sns.violinplot(data=df, x="Vendedor", y="Ventas Totales")
ax.set_title("Distribución de ventas por vendedor")
plt.tight_layout()
plt.show()

# --- SNS 12: Countplot productos ---
# Tipo: Barras de conteo | Propósito: Frecuencia de transacciones por producto
# Audiencia: Operaciones, inventario
fig, ax = plt.subplots(figsize=(10, 6))
sns.countplot(data=df, x="Producto", hue="Promoción", palette="Set2")
ax.set_title("Cantidad de transacciones por Producto y Promoción")
ax.set_xlabel("Producto")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
