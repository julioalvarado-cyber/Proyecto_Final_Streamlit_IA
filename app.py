import streamlit as st
import pandas as pd
from src.data_loader import DataLoader
from src.eda import obtener_perfil_calidad, obtener_estadisticas_numericas
from src.visualizations import (
    generar_histograma, 
    generar_scatterplot, 
    generar_boxplot, 
    generar_grafico_barras
)
from src.agent import AgenteDatos

# Configuración principal de la interfaz en Streamlit
st.set_page_config(
    page_title="Proyecto Integrador | IA y Datos", 
    page_icon="📊", 
    layout="wide"
)

def main():
    st.title("📊 Explorador Modular de Datos & IA Local")
    st.markdown("---")

    # Panel Lateral: Carga de Datos y Configuración
    st.sidebar.title("Configuración y Datos ⚙️")
    
    # Soporte híbrido: Permite subir archivos CSV y hojas de cálculo de Excel (.xlsx, .xls)
    archivo_subido = st.sidebar.file_uploader(
        "Sube un archivo personalizado (CSV o Excel)", 
        type=["csv", "xlsx", "xls"]
    )

    # Lógica de Selección de Dataset (Carga Dinámica o Predeterminada)
    try:
        if archivo_subido is not None:
            loader = DataLoader(archivo_subido)
            st.sidebar.success("¡Dataset personalizado cargado con éxito!")
        else:
            loader = DataLoader("data/StudentPerformanceFactors.csv")
            st.sidebar.info("Usando conjunto de datos predeterminado (Estudiantes).")

        df = loader.load_data()
        filas, columnas = loader.get_dimensions()
        datos_cargados = True
    except Exception as e:
        st.error(f"Error al procesar el conjunto de datos: {e}")
        datos_cargados = False

    # Panel Lateral: Menú de Navegación entre Módulos
    st.sidebar.title("Navegación 🧭")
    opcion = st.sidebar.radio(
        "Seleccione un módulo:",
        ["Carga y Vista Previa", "Análisis Exploratorio (EDA)", "Visualizaciones", "Agente de IA (Ollama)"]
    )

    if not datos_cargados:
        st.warning("No se pudo cargar ningún conjunto de datos. Verifique el archivo de origen.")
        return

    # -------------------------------------------------------------------------
    # MÓDULO 1: CARGA Y VISTA PREVIA
    # -------------------------------------------------------------------------
    if opcion == "Carga y Vista Previa":
        st.subheader("📁 Módulo de Carga de Datos")
        st.success(f"Conjunto de datos cargado correctamente: **{filas} filas** y **{columnas} columnas**.")
        
        st.write("### Vista previa de los primeros registros")
        st.dataframe(df.head(10), use_container_width=True)

    # -------------------------------------------------------------------------
    # MÓDULO 2: ANÁLISIS EXPLORATORIO (EDA)
    # -------------------------------------------------------------------------
    elif opcion == "Análisis Exploratorio (EDA)":
        st.subheader("🔍 Módulo de Análisis Exploratorio (EDA)")
        
        col1, col2 = st.columns([1, 1])
        with col1:
            st.write("### Perfil de Calidad de Datos")
            df_calidad = obtener_perfil_calidad(df)
            st.dataframe(df_calidad, use_container_width=True)
            
        with col2:
            st.write("### Resumen Estadístico (Variables Numéricas)")
            df_stats = obtener_estadisticas_numericas(df)
            st.dataframe(df_stats, use_container_width=True)

    # -------------------------------------------------------------------------
    # MÓDULO 3: VISUALIZACIONES INTERACTIVAS (PLOTLY)
    # -------------------------------------------------------------------------
    elif opcion == "Visualizaciones":
        st.subheader("📈 Módulo de Visualizaciones Interactivas")
        
        cols_numericas = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
        cols_categoricas = df.select_dtypes(include=['object', 'category']).columns.tolist()

        tab1, tab2, tab3 = st.tabs(["Univariado", "Bivariado (Num vs Num)", "Por Categorías"])

        with tab1:
            st.write("### Análisis Univariado")
            tipo_var = st.radio("Tipo de variable a analizar:", ["Numérica", "Categórica"], horizontal=True)
            
            if tipo_var == "Numérica" and cols_numericas:
                var_num = st.selectbox("Seleccione la variable numérica:", cols_numericas)
                fig = generar_histograma(df, var_num)
                st.plotly_chart(fig, use_container_width=True)
            elif tipo_var == "Categórica" and cols_categoricas:
                var_cat = st.selectbox("Seleccione la variable categórica:", cols_categoricas)
                fig = generar_grafico_barras(df, var_cat)
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("No se encontraron variables del tipo seleccionado en este dataset.")

        with tab2:
            st.write("### Relación entre Variables Numéricas")
            if len(cols_numericas) >= 2:
                c1, c2, c3 = st.columns(3)
                var_x = c1.selectbox("Eje X:", cols_numericas, index=0)
                var_y = c2.selectbox("Eje Y:", cols_numericas, index=min(1, len(cols_numericas)-1))
                var_color = c3.selectbox("Agrupar por color (opcional):", [None] + cols_categoricas)
                
                fig = generar_scatterplot(df, var_x, var_y, var_color)
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("Se requieren al menos dos variables numéricas en el dataset para realizar este gráfico.")

        with tab3:
            st.write("### Comparación por Categorías (Boxplot)")
            if cols_categoricas and cols_numericas:
                c1, c2 = st.columns(2)
                var_c = c1.selectbox("Variable Categórica (Grupos):", cols_categoricas)
                var_n = c2.selectbox("Variable Numérica (Métrica):", cols_numericas)
                
                fig = generar_boxplot(df, var_c, var_n)
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("Se requiere al menos una variable categórica y una numérica en el dataset.")

    # -------------------------------------------------------------------------
    # MÓDULO 4: AGENTE DE IA (OLLAMA LOCAL)
    # -------------------------------------------------------------------------
    elif opcion == "Agente de IA (Ollama)":
        st.subheader("🤖 Asistente Virtual Local (Llama 3.2)")
        st.markdown(
            "Consulte en lenguaje natural sobre las métricas, patrones y hallazgos del conjunto de datos cargado."
        )

        agente = AgenteDatos(model_name="llama3.2")

        # Comprobar el estado del servicio Ollama en Mac
        if not agente.esta_disponible():
            st.error("⚠️ No se pudo conectar con el servicio local de Ollama.")
            st.info(
                "Asegúrese de tener Ollama ejecutándose en su Mac y el modelo descargado. "
                "Comando sugerido en terminal: `ollama run llama3.2`"
            )
        else:
            st.success("🟢 Servicio Ollama conectado exitosamente (Modelo: Llama 3.2).")

            pregunta = st.text_input(
                "Escriba su consulta sobre los datos:",
                placeholder="Ejemplo: ¿Cuáles son las variables que tienen mayor impacto según las correlaciones?"
            )

            if st.button("Consultar al Agente", type="primary"):
                if pregunta.strip():
                    with st.spinner("El agente de IA está analizando los datos..."):
                        try:
                            respuesta = agente.responder_consulta(df, pregunta)
                            st.write("### Respuesta del Agente:")
                            st.info(respuesta)
                        except Exception as e:
                            st.error(f"Ocurrió un error al procesar la consulta: {e}")
                else:
                    st.warning("Por favor ingrese una pregunta antes de consultar.")

if __name__ == "__main__":
    main()
