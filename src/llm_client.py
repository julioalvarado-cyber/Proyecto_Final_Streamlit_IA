import os
from groq import Groq

def consultar_llm(prompt_sistema, prompt_usuario):
    # Lee la API Key desde los Secrets de Streamlit Cloud o variables de entorno
    api_key = os.getenv("GROQ_API_KEY")
    
    if not api_key:
        return "⚠️ Error: No se encontró la API Key de Groq configurada en la aplicación."

    try:
        client = Groq(api_key=api_key)

        response = client.chat.completions.create(
            model="llama-3.2-3b-preview",
            messages=[
                {"role": "system", "content": prompt_sistema},
                {"role": "user", "content": prompt_usuario}
            ],
            temperature=0.2,
            max_tokens=1024
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ Error al conectar con el servicio de IA: {str(e)}"
