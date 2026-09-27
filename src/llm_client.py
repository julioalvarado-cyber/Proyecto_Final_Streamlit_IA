import ollama

class OllamaClient:
    """Cliente para la comunicación local con el servidor de Ollama."""
    def __init__(self, model_name: str = "llama3.2"):
        self.model_name = model_name

    def verificar_conexion(self) -> bool:
        """Comprueba si el servicio local de Ollama está activo."""
        try:
            ollama.list()
            return True
        except Exception:
            return False

    def consultar(self, prompt: str, system_prompt: str = "") -> str:
        """Envia una consulta al modelo local y retorna su respuesta."""
        mensajes = []
        if system_prompt:
            mensajes.append({"role": "system", "content": system_prompt})
        mensajes.append({"role": "user", "content": prompt})

        respuesta = ollama.chat(model=self.model_name, messages=mensajes)
        return respuesta['message']['content']