import os
try:
    import streamlit as st
except ImportError:
    st = None

from groq import Groq

class GroqClient:
    """Cliente para interactuar con la API de Groq."""
    def __init__(self):
        self.api_key = None
        
        # Leer desde los Secrets de Streamlit Cloud
        try:
            if st and hasattr(st, "secrets") and "GROQ_API_KEY" in st.secrets:
                self.api_key = st.secrets["GROQ_API_KEY"]
        except Exception:
            pass
            
        # Respaldo con variable de entorno
        if not self.api_key:
            self.api_key = os.getenv("GROQ_API_KEY")

    def consultar(self, prompt_sistema: str, prompt_usuario: str) -> str:
        if not self.api_key:
            return "⚠️ Error: No se encontró la API Key de Groq en los Secrets."

        try:
            client = Groq(api_key=self.api_key.strip())
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",  # <--- Usaremos este modelo ultra estable y oficial
                messages=[
                    {"role": "system", "content": prompt_sistema},
                    {"role": "user", "content": prompt_usuario}
                ],
                temperature=0.2,
                max_tokens=1024
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"⚠️ Error al conectar con el servicio de Groq: {str(e)}"

# Alias por compatibilidad
OllamaClient = GroqClient
