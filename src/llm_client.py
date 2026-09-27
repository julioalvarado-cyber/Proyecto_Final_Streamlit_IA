import os
try:
    import streamlit as st
except ImportError:
    st = None

import google.generativeai as genai

class GroqClient:
    """Cliente robusto para Google Gemini en Streamlit Cloud."""
    def __init__(self):
        self.api_key = None
        
        # 1. Leer de los Secrets de Streamlit Cloud
        try:
            if st and hasattr(st, "secrets") and "GEMINI_API_KEY" in st.secrets:
                self.api_key = st.secrets["GEMINI_API_KEY"]
        except Exception:
            pass
            
        # 2. Respaldo por variable de entorno
        if not self.api_key:
            self.api_key = os.getenv("GEMINI_API_KEY")

    def consultar(self, prompt_sistema: str, prompt_usuario: str) -> str:
        if not self.api_key:
            return "⚠️ Error: No se encontró la GEMINI_API_KEY en los Secrets."

        try:
            genai.configure(api_key=str(self.api_key).strip())
            
            # Usamos el modelo que seleccionaste directamente en Google AI Studio
            model = genai.GenerativeModel(
                model_name="gemini-3.1-flash-lite",
                system_instruction=prompt_sistema
            )
            response = model.generate_content(prompt_usuario)
            return response.text
        except Exception as e:
            return f"⚠️ Error al conectar con Google Gemini: {str(e)}"

# Alias de compatibilidad total
OllamaClient = GroqClient
