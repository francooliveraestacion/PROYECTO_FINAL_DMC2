import streamlit as st
import pandas as pd


st.title("⚽ FIFA World Cup 2026")
st.sidebar.title("🏡Contenido")
contenido=st.sidebar.selectbox("",["Home",
                                   "Módulo 2",
                                   "Ítem 1",
                                   "Ítem 2",
                                   "Ítem 4",
                                   "Ítem 5",
                                   "Ítem 6",
                                   "Ítem 7",
                                   "Ítem 8",
                                   "Ítem 9",
                                   "Ítem 10"])
if contenido =="Home":
  st.write("Te encuentras en el modulo de home")
  st.subheader("Estudiante")
  st.write ("Franco Olivera Estacion")
  st.write("Modulo: Python Fundamentals")
  st.write("Año:2026")
  st.subheader("Informacion general")
  st.write("""Estudiante de Ingeniería Industrial orientado al análisis de datos,
automatización y mejora de procesos.
""")
  st.subheader("Descripcion del proyecto")
  st.write("""
El proyecto consiste en desarrollar una aplicación web utilizando
Streamlit para presentar y analizar indicadores relacionados con
el proceso . La aplicación busca facilitar la visualización
de información y el seguimiento de los principales indicadores.
""")
  st.subheader("Tecnologias utilizadas")
  st.markdown("""
🐍 Python
📊 Streamlit
📈 Pandas
📉 Matplotlib
""")
elif contenido ==("Módulo 2"):
  st.write("✅Te encuentras en el modulo 2")
  st.subheader("Análisis Exploratorio de Datos")
  st.header("📂 Módulo 2: Carga del Dataset")
  st.write("Carga el archivo CSV para comenzar con el análisis exploratorio.")
  archivo = st.file_uploader("Selecciona el archivo CSV",type=["csv"])
  if archivo is not None:
    try:
        df = pd.read_csv(archivo)
        st.success("✅ El archivo fue cargado correctamente.")
        st.subheader("👀 Vista previa del dataset")
        st.dataframe( df.head(), use_container_width=True)
        st.subheader("📐 Dimensiones del dataset")

        filas, columnas = df.shape

        col1, col2 = st.columns(2)

        with col1: st.metric("Número de filas",filas)

        with col2:st.metric("Número de columnas",columnas)
     except Exception as e:
       st.error( f"❌ Ocurrió un error al cargar el archivo: {e}" )
   else:
    st.warning( "⚠️ Debes cargar un archivo CSV antes de realizar cualquier análisis.")
          
      
  

 
  
  
 
    
  

elif contenido ==("Ítem 1"):
  st.write("✅Te encuentras en el Ítem 1: Información general del dataset")
elif contenido ==("Ítem 2"):
  st.write("✅Te encuentras en el Ítem 2: Clasificación de variables")

  
elif contenido ==("Ítem 3"):
    st.write("✅Te encuentras en el Ítem 3: Estadísticas descriptivas")
elif contenido ==("Ítem 4"):
    st.write("✅Te encuentras en el Ítem 4: Análisis de valores faltantes")
elif contenido ==("Ítem 5"):
    st.write("✅Te encuentras en el Ítem 5: Distribución de variables numéricas")
elif contenido ==("Ítem 6"):
    st.write("✅Te encuentras en el Ítem 6: Análisis de variables categóricas")
elif contenido ==("Ítem 7"):
    st.write("✅Te encuentras en el Ítem 7: Análisis bivariado (numérico vs categórico)")
elif contenido ==("Ítem 8"):
    st.write("✅Te encuentras en el Ítem 8: Análisis bivariado (categórico vs categórico)")
elif contenido ==("Ítem 9"):
    st.write("✅Te encuentras en el Ítem 9: Análisis basado en parámetros seleccionados")
else:
    st.write("✅Te encuentras en el Ítem 10: Hallazgos clave")
