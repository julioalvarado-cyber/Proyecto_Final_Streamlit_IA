import pandas as pd

def obtener_perfil_calidad(df: pd.DataFrame) -> pd.DataFrame:
    """Genera una tabla con el perfil de calidad de datos (tipos, nulos, % nulos, únicos)."""
    resumen = pd.DataFrame({
        "Tipo de Dato": df.dtypes.astype(str),
        "Valores Nulos": df.isnull().sum(),
        "% Nulos": (df.isnull().sum() / len(df) * 100).round(2),
        "Valores Únicos": df.nunique()
    })
    return resumen.reset_index().rename(columns={"index": "Variable"})

def obtener_estadisticas_numericas(df: pd.DataFrame) -> pd.DataFrame:
    """Calcula estadísticas descriptivas para las variables numéricas."""
    numeric_df = df.select_dtypes(include=['int64', 'float64'])
    return numeric_df.describe().T.round(2)