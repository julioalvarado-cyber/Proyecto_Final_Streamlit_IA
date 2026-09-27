from src.llm_client import GroqClient

class AgenteDatos:
    def __init__(self):
        self.client = GroqClient()

    def responder(self, prompt_sistema: str, prompt_usuario: str) -> str:
        return self.client.consultar(prompt_sistema, prompt_usuario)
