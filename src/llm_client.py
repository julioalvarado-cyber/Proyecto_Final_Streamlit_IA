import os
try:
    import streamlit as st
except ImportError:
    st = None

from groq import Groq

class GroqClient:
    """Cliente oficial y robusto para la API de Groq en Streamlit Cloud."""
    def __init__(self):
        self.api_key = None
        
        # 1. Leer desde los Secrets de Streamlit Cloud
        try:
            if st and hasattr(st, "secrets") and "GROQ_API_KEY" in st.secrets:
                self.api_key = st.secrets["GROQ_API_KEY"]
        except Exception:
            pass
            
        # 2. Respaldo por variable de entorno
        if not self.api_key:
            self.api_key = os.getenv("GROQ_API_KEY")

    def consultar(self, prompt_sistema: str, prompt_usuario: str) -> str:
        if not self.api_key:
            return "⚠️ Error: No se encontró la API Key de Groq configurada en los Secrets."

        try:
            client = Groq(api_key=self.api_key.strip())
            
            # Intentar con el modelo estándar actual de Groq
            response = client.chat.completions.create(
                model="llama-3.2-90b-vision-preview",
                messages=[
                    {"role": "system", "content": prompt_sistema},
                    {"role": "user", "content": prompt_usuario}
                ],
                temperature=0.2,
                max_tokens=1024
            )
            return response.choices[0].message.content
        except Exception as e:
            # Fallback automático por si falla el primero
            try:
                client = Groq(api_key=self.api_key.strip())
                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[
                        {"role": "system", "content": prompt_sistema},
                        {"role": "user", "content": prompt_usuario}
                    ],
                    temperature=0.2,
                    max_tokens=1024
                )
                return response.choices[0].message.content
            except Exception as e2:
                return f"⚠️ Error crítico al conectar con Groq: {str(e2)}"

# Alias de compatibilidad modular
OllamaClient = GroqClient
