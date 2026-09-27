# 🏛️ Universidad Casa Grande
## Maestría en Inteligencia Artificial y Ciencia de Datos
### Proyecto Final Integrador

* **Institución:** Universidad Casa Grande
* **Módulo:** Paradigmas de Programación para Inteligencia Artificial y Ciencia de Datos
* **Profesor:** Ing. Carlos Carillo, Mgs.
* **Estudiante:** Ing. Julio Alvarado, Mgs.
* **Fecha:** Septiembre 2026

---

## 📊 Proyecto Explorador Modular de Datos & Agente de IA Local

Este proyecto es una plataforma interactiva desarrollada en **Streamlit** para la carga dinámica de conjuntos de datos, análisis exploratorio (EDA), visualización interactiva con **Plotly** e interpretación inteligente mediante un agente de **IA local (Ollama - Llama 3.2)**.

---

## 🛠️ Características Principales

- **Carga Dinámica de Datos Híbrida:** Soporte nativo para archivos `.csv` y hojas de cálculo de Excel (`.xlsx`, `.xls`), con sanitización automática de registros (eliminación de espacios extra, duplicados y nulos).
- **Análisis Exploratorio de Datos (EDA):** Perfilado automático de calidad de datos y cálculo de estadísticas descriptivas.
- **Visualización Interactiva:** Generación de histogramas, diagramas de dispersión con líneas de tendencia OLS y gráficos de caja (Boxplots) mediante Plotly.
- **Agente de IA Local:** Conexión con Ollama (Llama 3.2) alimentada por motores estadísticos en Python (matrices de correlación de Pearson y resúmenes por grupos categóricos) para garantizar respuestas cuantitativamente exactas y sin alucinaciones numéricas.

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
│   ├── llm_client.py           # Cliente para servicio local de Ollama
│   └── agent.py                # Agente analítico con System Prompt blindado
├── app.py                      # Interfaz principal de Streamlit
├── requirements.txt            # Dependencias del proyecto
└── README.md                   # Documentación técnica
```
---

## 🚀 Requisitos e Instalación

### 1. Requisitos Previos
- **Python 3.10** o superior.
- [Ollama](https://ollama.com/) instalado en el sistema.

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
### 3. Iniciar el Servicio de IA (Ollama)
En una ventana de terminal independiente, inicia el modelo:
```bash
ollama run llama3.2
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
