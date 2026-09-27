import os
from src.llm_client import GroqClient

class AgenteDatos:
    """Clase para la gestión del agente analítico con inyección de contexto."""
    
    def __init__(self, model_name: str = "llama-3.2-3b-preview"):
        # Acepta model_name para evitar el TypeError en app.py
        self.model_name = model_name
        self.client = GroqClient()

    def consultar(self, prompt_sistema: str, prompt_usuario: str) -> str:
        """Envía los prompts al cliente LLM de Groq."""
        return self.client.consultar(prompt_sistema, prompt_usuario)

    def responder(self, prompt_sistema: str, prompt_usuario: str) -> str:
        """Alias de compatibilidad para consultar."""
        return self.consultar(prompt_sistema, prompt_usuario)
