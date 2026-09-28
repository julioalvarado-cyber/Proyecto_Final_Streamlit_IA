# 🏛️ Universidad Casa Grande
## Maestría en Inteligencia Artificial y Ciencia de Datos
### Proyecto Final Integrador

* **Módulo:** Paradigmas de Programación para Inteligencia Artificial y Ciencia de Datos
* **Profesor:** Ing. Carlos Carillo, Mgs.
* **Estudiante:** Ing. Julio Alvarado, Mgs.
* **Fecha:** Septiembre 2026

---

## 📊 Proyecto Explorador Modular de Datos & Agente de IA Local

Este proyecto es una plataforma interactiva desarrollada en **Streamlit** para la carga dinámica de conjuntos de datos, análisis exploratorio (EDA), visualización interactiva con **Plotly** e interpretación inteligente mediante un agente de **IA local (Ollama - Llama 3.2)**.

---

## 🛠️ Características Principales

- **Carga Dinámica de Datos Híbrida:** Soporte nativo para archivos `.csv` y hojas de cálculo de Excel (`.xlsx`, `.xls`), con sanitización automática de registros.
- **Análisis Exploratorio de Datos (EDA):** Perfilado automático de calidad de datos y cálculo de estadísticas descriptivas detalladas.
- **Visualización Interactiva:** Generación de histogramas, diagramas de dispersión con líneas de tendencia OLS y gráficos de caja (Boxplots) mediante Plotly.
- **Agente de IA en la Nube:** Conectado mediante la API de Google Gemini (`gemini-3.1-flash-lite`), alimentado por motores estadísticos en Python para garantizar respuestas cuantitativamente exactas y fundamentadas en los datos.

---

## 📁 Estructura del Repositorio

```text

PROYECTO_INTEGRADOR/
│
├── .venv/                      # Entorno virtual de Python
├── data/
│   └── StudentPerformanceFactors.csv   # Dataset predeterminado
├── src/
│   ├── __init__.py
│   ├── data_loader.py          # Carga dinámica y sanitización de CSV/Excel
│   ├── eda.py                  # Perfil de calidad y descriptivos
│   ├── visualizations.py       # Gráficos interactivos Plotly
│   ├── llm_client.py           # Cliente robusto para Google Gemini
│   └── agent.py                # Agente analítico con System Prompt blindado
├── app.py                      # Interfaz principal de Streamlit
├── requirements.txt            # Dependencias del proyecto
└── README.md                   # Documentación técnica
```
---

## 🚀 Requisitos e Instalación

### 1. Requisitos Previos
- **Python 3.10** o superior.
- Una clave de API de Google Gemini (GEMINI_API_KEY) obtenida desde Google AI Studio [https://aistudio.google.com/].

---

### 2. Configuración del Entorno Virtual e Instalación de Dependencias

#### 🍎 En macOS / Linux
Abre la Terminal y ejecuta:

```bash
# Crear entorno virtual
python3 -m venv .venv

# Activar el entorno virtual
source .venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```
---
#### 🪟 Windows
Abre PowerShell o Símbolo del Sistema (CMD) y ejecuta:

```PowerShell
# Crear entorno virtual
python -m venv .venv

# Activar el entorno virtual (PowerShell)
.\.venv\Scripts\Activate.ps1

# O activar el entorno virtual (CMD)
# .\.venv\Scripts\activate.bat

# Instalar dependencias
pip install -r requirements.txt
```
---
### 3. Configuración de Credenciales Locales
Para que el agente de Gemini funcione de forma local, crea una carpeta llamada `.streamlit` en la raíz del proyecto y dentro un archivo llamado `secrets.toml`:

```Ini, TOML
GEMINI_API_KEY = "tu_clave_de_api_aqui"
```
También puedes configurarla como una variable de entorno en tu terminal:

```bash
# Mac/Linux: export GEMINI_API_KEY="tu_clave_de_api_aqui"

# Windows (PowerShell): $env:GEMINI_API_KEY="tu_clave_de_api_aqui"
```
---

## 💻 Ejecución de la Aplicación
Con el entorno virtual activo y el servicio de Ollama en ejecución:

### 🍎 macOS / Linux
Abre la Terminal y ejecuta:
```bash
python3 -m streamlit run app.py
```

### 🪟 En Windows
Abre PowerShell o Símbolo del Sistema y ejecuta:

```PowerShell
python -m streamlit run app.py
```
La aplicación se abrirá automáticamente en tu navegador web en http://localhost:8501.
