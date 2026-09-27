import pandas as pd
from src.llm_client import OllamaClient

class AgenteDatos:
    """
    Agente de Inteligencia Artificial especializado en la interpretación analítica
    y estadística de conjuntos de datos tabulares con gobernanza estricta.
    """
    def __init__(self, model_name: str = "llama3.2"):
        self.client = OllamaClient(model_name=model_name)
        
        # System Prompt Definitivo: Blindaje contra alucinaciones y p-valores inventados
        self.system_prompt = (
            "Eres un Científico de Datos Principal y Analista Estadístico Senior. Tu objetivo es interpretar "
            "de forma rigurosa, objetiva y profesional los resúmenes de datos provistos para responder las "
            "preguntas del usuario en español.\n\n"
            "REGLAS INVIOLABLES DE GOBERNANZA Y CERO ALUCINACIÓN:\n"
            "1. ANCLAJE ESTRICTO EN LOS DATOS (GROUNDING): Basa tus conclusiones ÚNICAMENTE en las cifras, promedios, "
            "tablas y coeficientes explícitamente provistos en el contexto de entrada.\n"
            "2. PROHIBICIÓN DE MÉTRICAS NO CALCULADAS: No inventes p-valores, intervalos de confianza, pruebas t, "
            "desviaciones ni significancias estadísticas si no están expresamente calculados en el texto provisto.\n"
            "3. CORRELACIÓN NO ES CAUSALIDAD: Al interpretar una correlación de Pearson (r), descríbela únicamente "
            "por su magnitud (fuerte, moderada, débil, positiva o negativa) y su dirección lineal. Queda prohibido afirmar causalidad directa.\n"
            "4. DISTINCIÓN DE VARIABLES: Respeta la naturaleza de las variables. No trates variables categóricas como si "
            "fueran métricas numéricas continuas ni asumas valores promedios sobre textos o categorías.\n"
            "5. DECLARACIÓN EXPLÍCITA DE LIMITACIONES: Si la pregunta del usuario requiere analizar columnas, métricas "
            "o relaciones que no están presentes en el contexto, declara textualmente: 'No dispongo de información suficiente "
            "en el dataset provisto para responder a este aspecto.'\n\n"
            "ESTRUCTURA OBLIGATORIA DE RESPUESTA:\n"
            "- 📌 Resumen Ejecutivo: Respuesta directa a la pregunta en 1 o 2 oraciones citando la métrica principal.\n"
            "- 📊 Evidencia Estadística: Análisis cuantitativo citando los números, promedios o coeficientes exactos del contexto.\n"
            "- ⚠️ Consideraciones Metodológicas: Aclaración sobre correlación vs. causalidad o limitaciones de los datos disponibles.\n"
            "- 💡 Conclusión / Recomendación: Sugerencia o interpretación lógica derivada exclusivamente de la evidencia presentada."
        )

    def esta_disponible(self) -> bool:
        """Verifica si el servicio local de Ollama responde correctamente."""
        return self.client.verificar_conexion()

    def responder_consulta(self, df: pd.DataFrame, pregunta_usuario: str) -> str:
        """
        Genera un contexto estadístico completo (descriptivos, correlaciones de Pearson 
        y promedios por grupos categóricos) y consulta al LLM.
        """
        # 1. Información de Estructura General
        num_filas, num_cols = df.shape
        columnas = ", ".join(df.columns.tolist())
        
        # 2. Resumen de Variables Numéricas (Estadísticas Descriptivas y Correlaciones)
        cols_num = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
        if cols_num:
            resumen_stats = df[cols_num].describe().T[['mean', 'std', 'min', '50%', 'max']].round(2).to_string()
            matriz_corr = df[cols_num].corr().round(2).to_string() if len(cols_num) > 1 else "Solo existe una variable numérica."
        else:
            resumen_stats = "No existen variables numéricas en este dataset."
            matriz_corr = "No aplica."

        # 3. Resumen de Variables Categóricas (Agrupaciones por variable objetivo)
        cols_cat = df.select_dtypes(include=['object', 'category']).columns.tolist()
        resumen_cat = ""
        
        # Identificar la variable objetivo (Exam_Score por defecto o la primera numérica disponible)
        target_col = "Exam_Score" if "Exam_Score" in df.columns else (cols_num[0] if cols_num else None)
        
        if cols_cat and target_col:
            resumen_cat += f"\n--- Promedio de '{target_col}' según categorías principales ---\n"
            for col in cols_cat[:6]:  # Limitado a las primeras 6 categóricas para optimizar el prompt
                promedios_grupo = df.groupby(col)[target_col].mean().round(2).to_string()
                resumen_cat += f"\n[Variable Categórica: {col}]\n{promedios_grupo}\n"

        # 4. Ensamble del Contexto para el LLM
        contexto = (
            f"=== ESTRUCTURA DEL DATASET ===\n"
            f"- Registros: {num_filas} | Columnas: {num_cols}\n"
            f"- Lista de Columnas: {columnas}\n\n"
            f"=== ESTADÍSTICAS DESCRIPTIVAS (NUMÉRICAS) ===\n"
            f"{resumen_stats}\n\n"
            f"=== MATRIZ DE CORRELACIÓN DE PEARSON (r) ===\n"
            f"{matriz_corr}\n"
        )

        if resumen_cat:
            contexto += f"\n=== AGRUPACIONES Y COMPARACIONES CATEGÓRICAS ===\n{resumen_cat}"

        # 5. Estructura del Prompt Final
        prompt_final = (
            f"Contexto estadístico extraído en tiempo real desde el dataset:\n\n"
            f"{contexto}\n\n"
            f"=== PREGUNTA DEL USUARIO ===\n"
            f"{pregunta_usuario}\n\n"
            f"Aplica las reglas inviolables de tu sistema y responde siguiendo la estructura obligatoria."
        )

        return self.client.consultar(prompt=prompt_final, system_prompt=self.system_prompt)