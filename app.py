import streamlit as st



st.title("👨🏻‍💻Proyecto Individual📈")
st.sidebar.image("dmvc.png",width=1100)
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
elif contenido ==("Modulo 2"):
  st.write("✅Te encuentras en el modulo 2")
elif contenido ==("Ítem 1"):
  st.write("✅Te encuentras en el Ítem 1: Información general del dataset")
elif contenido ==("Ítem 2"):
elif contenido ==("Ítem 3"):
elif contenido ==("Ítem 4"):
elif contenido ==("Ítem 5"):
elif contenido ==("Ítem 6"):
elif contenido ==("Ítem 7"):
elif contenido ==("Ítem 8"):
elif contenido ==("Ítem 9"):
else:
  st.write("✅Te encuentras en el Ítem 10: Hallazgos clave")
