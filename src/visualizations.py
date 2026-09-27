import plotly.express as px
import pandas as pd

def generar_histograma(df: pd.DataFrame, columna: str):
    """Genera un histograma interactivo para una variable numérica."""
    fig = px.histogram(
        df, 
        x=columna, 
        nbins=30,
        title=f"Distribución de {columna}",
        marginal="box",
        color_discrete_sequence=["#1f77b4"]
    )
    fig.update_layout(template="plotly_white", xaxis_title=columna, yaxis_title="Frecuencia")
    return fig

def generar_scatterplot(df: pd.DataFrame, col_x: str, col_y: str, col_color: str = None):
    """Genera un gráfico de dispersión para analizar la relación entre dos variables numéricas."""
    fig = px.scatter(
        df, 
        x=col_x, 
        y=col_y, 
        color=col_color,
        title=f"Relación entre {col_x} y {col_y}",
        trendline="ols",
        opacity=0.7
    )
    fig.update_layout(template="plotly_white")
    return fig

def generar_boxplot(df: pd.DataFrame, col_cat: str, col_num: str):
    """Genera un gráfico de caja por categorías para comparar distribuciones."""
    fig = px.box(
        df, 
        x=col_cat, 
        y=col_num, 
        color=col_cat,
        title=f"Comparación de {col_num} según {col_cat}"
    )
    fig.update_layout(template="plotly_white", showlegend=False)
    return fig

def generar_grafico_barras(df: pd.DataFrame, columna: str):
    """Genera un gráfico de barras de frecuencias para variables categóricas."""
    conteo = df[columna].value_counts().reset_index()
    conteo.columns = [columna, "Frecuencia"]
    fig = px.bar(
        conteo, 
        x=columna, 
        y="Frecuencia", 
        color=columna,
        title=f"Distribución Categórica de {columna}",
        text_auto=True
    )
    fig.update_layout(template="plotly_white", showlegend=False)
    return fig