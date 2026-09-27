import os
from src.llm_client import GroqClient

class AgenteDatos:
    """Clase para la gestión del agente analítico con inyección de contexto."""
    
    def __init__(self, model_name: str = "llama-3.2-3b-preview"):
        self.model_name = model_name
        self.client = GroqClient()

    def esta_disponible(self) -> bool:
        """Verifica si la API Key de Groq está presente para habilitar el agente."""
        api_key = os.getenv("GROQ_API_KEY")
        return bool(api_key and api_key.strip())

    def consultar(self, prompt_sistema: str, prompt_usuario: str) -> str:
        """Envía los prompts al cliente LLM de Groq."""
        return self.client.consultar(prompt_sistema, prompt_usuario)

    def responder(self, prompt_sistema: str, prompt_usuario: str) -> str:
        """Alias de compatibilidad para consultar."""
        return self.consultar(prompt_sistema, prompt_usuario)

    def responder_consulta(self, df, pregunta: str) -> str:
        """
        Construye el contexto con datos del DataFrame y responde la pregunta del usuario.
        """
        prompt_sistema = (
            "Eres un experto consultor en Ciencia de Datos y Estadística de la Universidad Casa Grande. "
            "Responde de forma clara, precisa, fundamentada en los datos proporcionados y estructurada."
        )
        
        # Resumen básico de los datos como contexto
        columnas = list(df.columns)
        num_filas, num_cols = df.shape
        resumen_df = df.describe(include='all').to_string()
        
        prompt_usuario = (
            f"El conjunto de datos tiene {num_filas} filas y {num_cols} columnas.\n"
            f"Columnas disponibles: {columnas}\n\n"
            f"Resumen estadístico de los datos:\n{resumen_df}\n\n"
            f"Pregunta del usuario: {pregunta}"
        )
        
        return self.consultar(prompt_sistema, prompt_usuario)
