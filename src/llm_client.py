import os
try:
    import streamlit as st
except ImportError:
    st = None

from groq import Groq

class GroqClient:
    """Cliente seguro y directo para la API de Groq."""
    def __init__(self):
        self.api_key = None
        
        # Leer la API Key de los Secrets de Streamlit Cloud
        try:
            if st and hasattr(st, "secrets") and "GROQ_API_KEY" in st.secrets:
                self.api_key = st.secrets["GROQ_API_KEY"]
        except Exception:
            pass
            
        # Respaldo por variable de entorno local
        if not self.api_key:
            self.api_key = os.getenv("GROQ_API_KEY")

    def consultar(self, prompt_sistema: str, prompt_usuario: str) -> str:
        if not self.api_key:
            return "⚠️ Error: No se encontró la API Key de Groq en los Secrets."

        try:
            # Inicializar cliente de Groq de forma limpia
            client = Groq(api_key=str(self.api_key).strip())
            
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",  # Modelo estable y garantizado en Groq
                messages=[
                    {"role": "system", "content": prompt_sistema},
                    {"role": "user", "content": prompt_usuario}
                ],
                temperature=0.2,
                max_tokens=1024
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"⚠️ Error al conectar con Groq: {str(e)}"

# Alias de compatibilidad
OllamaClient = GroqClient
