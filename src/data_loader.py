import pandas as pd
import os

class DataLoader:
    """Clase encargada de la carga y sanitización automática de archivos CSV y Excel."""
    
    def __init__(self, source):
        self.source = source

    def _sanitizar_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        """Aplica reglas generales de limpieza para corregir inconsistencias frecuentes."""
        # 1. Eliminar filas y columnas completamente vacías
        df = df.dropna(how="all").dropna(how="all", axis=1)

        # 2. Normalizar nombres de columnas (eliminar espacios extra)
        df.columns = df.columns.str.strip()

        # 3. Limpiar columnas de texto (espacios en blanco al inicio/final)
        for col in df.select_dtypes(include=['object']):
            df[col] = df[col].astype(str).str.strip()

        # 4. Eliminar registros duplicados exactos
        df = df.drop_duplicates()

        return df

    def load_data(self) -> pd.DataFrame:
        """Carga y sanitiza automáticamente los datos de CSV o Excel."""
        # Carga desde objeto subido en Streamlit (file_uploader)
        if hasattr(self.source, "name"):
            nombre_archivo = self.source.name.lower()
            if nombre_archivo.endswith((".xlsx", ".xls")):
                df = pd.read_excel(self.source)
            else:
                df = pd.read_csv(self.source)

        # Carga desde ruta local (string)
        elif isinstance(self.source, str):
            if not os.path.exists(self.source):
                raise FileNotFoundError(f"No se encontró el archivo en la ruta: {self.source}")
            
            if self.source.lower().endswith((".xlsx", ".xls")):
                df = pd.read_excel(self.source)
            else:
                df = pd.read_csv(self.source)
        else:
            raise ValueError("Tipo de fuente de datos no soportado.")

        # Retornar el DataFrame limpio
        return self._sanitizar_dataframe(df)

    def get_dimensions(self) -> tuple:
        """Retorna las dimensiones (filas, columnas) del conjunto de datos."""
        df = self.load_data()
        return df.shape