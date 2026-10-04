import streamlit as st
import pandas as pd
import io
import matplotlib.pyplot as plt
import seaborn as sns

st.title("⚽ FIFA World Cup 2026")
st.sidebar.title("🏡Contenido")
contenido=st.sidebar.selectbox("",["Home",
                                   "Módulo 2",
                                   "Ítem 1",
                                   "Ítem 2",
                                   "Ítem 3",
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
  st.write(
        "En este ítem se revisará la información general del dataset, "
        "los tipos de datos, los valores nulos y los registros duplicados." )
  archivo = st.file_uploader(
        "Selecciona el archivo CSV",
        type=["csv"],
        key="archivo_item1")
  if archivo is not None:
        df = pd.read_csv(archivo)
        st.success("✅ Archivo cargado correctamente.")
        st.subheader("1️⃣ Información general")
        buffer = io.StringIO()
        df.info(buf=buffer)
        informacion = buffer.getvalue()

        st.text(informacion)
        st.subheader("2️⃣ Tipos de datos de las variables")

        tabla_tipos = pd.DataFrame({
            "Variable": df.columns,
            "Tipo de dato": df.dtypes.astype(str).values})

        st.dataframe(
            tabla_tipos,
            use_container_width=True)
    
        st.subheader("3️⃣ Valores nulos")

        nulos = df.isnull().sum()

        tabla_nulos = pd.DataFrame({
            "Variable": nulos.index,
            "Valores nulos": nulos.values})

        st.dataframe(
            tabla_nulos,
            use_container_width=True)
        st.subheader("4️⃣ Registros duplicados")

        duplicados = df.duplicated().sum()

        col1, col2 = st.columns(2)
        with col1:
            st.metric(
                "Registros duplicados",
                duplicados
            )

        with col2:
            st.metric(
                "Registros no duplicados",
                len(df) - duplicados
            )

        if duplicados == 0:
            st.success("✅ No se encontraron registros duplicados.")
        else:
            st.warning(
             f"⚠️ Se encontraron {duplicados} registros duplicados."
            )
  else:
        st.warning("⚠️ Debes cargar el archivo CSV para realizar el Ítem 1.")
  
elif contenido ==("Ítem 2"):
  st.write("✅Te encuentras en el Ítem 2: Clasificación de variables")
  st.write(
        "En este ítem se identificarán las variables numéricas y categóricas "
        "del dataset mediante una función personalizada."
    )
  archivo = st.file_uploader(
        "Selecciona el archivo CSV",
        type=["csv"],
        key="archivo_item2")
  if archivo is not None:
        df = pd.read_csv(archivo)
        st.success("✅ Archivo cargado correctamente.")
    
        def clasificar_variables(dataframe):
            variables_numericas = []
            variables_categoricas = []
            for columna in dataframe.columns:

                if pd.api.types.is_numeric_dtype(dataframe[columna]):
                    variables_numericas.append(columna)
                else:
                    variables_categoricas.append(columna)
            return variables_numericas, variables_categoricas
        numericas, categoricas = clasificar_variables(df)
        st.subheader("🔢 Variables numéricas")
        st.write(f"Cantidad de variables numéricas: **{len(numericas)}**")
        st.dataframe(
            pd.DataFrame({"Variable numérica": numericas}),
            use_container_width=True )
        st.subheader("🔤 Variables categóricas")
        st.write(f"Cantidad de variables categóricas: **{len(categoricas)}**")
        st.dataframe(
            pd.DataFrame({"Variable categórica": categoricas}),
            use_container_width=True)
        st.subheader("📈 Conteo de variables por tipo")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Variables numéricas",
                len(numericas) )

        with col2:
            st.metric("Variables categóricas",
                len(categoricas))
  else:
        st.warning( "⚠️ Debes cargar el archivo CSV para realizar el Ítem 2.")        
elif contenido ==("Ítem 3"):
    st.write("✅Te encuentras en el Ítem 3: Estadísticas descriptivas")
    st.write(
        "En este ítem se analizarán las principales estadísticas "
        "descriptivas de las variables numéricas del dataset.")
    archivo = st.file_uploader(
        "Selecciona el archivo CSV",
        type=["csv"],
        key="archivo_item3")
    if archivo is not None:

        df = pd.read_csv(archivo)

        st.success("✅ Archivo cargado correctamente.")
        
        
        st.subheader("1️⃣ Estadísticas descriptivas")

        estadisticas = df.describe()

        st.dataframe(
            estadisticas,
            use_container_width=True )
        st.subheader("2️⃣ Media y mediana")

        datos_numericos = df.select_dtypes(include="number")

        resumen = pd.DataFrame({
            "Variable": datos_numericos.columns,
            "Media": datos_numericos.mean().values,
            "Mediana": datos_numericos.median().values})
        st.dataframe(resumen,
            use_container_width=True)

        st.write( "La **media** representa el promedio de los valores, "
            "mientras que la **mediana** corresponde al valor central "
            "cuando los datos se ordenan.")
      
        st.subheader("3️⃣ Cuartiles y dispersión")

        dispersion = pd.DataFrame({
            "Variable": datos_numericos.columns,
            "Q1": datos_numericos.quantile(0.25).values,
            "Q3": datos_numericos.quantile(0.75).values,
            "Desviación estándar": datos_numericos.std().values})
        st.dataframe(
            dispersion,
            use_container_width=True)

        st.write(
            "El **Q1** representa el 25% de los datos y el **Q3** "
            "representa el 75%. La desviación estándar permite observar "
            "qué tan dispersos están los valores respecto a la media." )
      
        st.subheader("4️⃣ Detección preliminar de valores extremos")

        Q1 = datos_numericos.quantile(0.25)
        Q3 = datos_numericos.quantile(0.75)

        IQR = Q3 - Q1

        limite_inferior = Q1 - 1.5 * IQR
        limite_superior = Q3 + 1.5 * IQR

        valores_extremos = (
            (datos_numericos < limite_inferior) |
            (datos_numericos > limite_superior)).sum()
        tabla_extremos = pd.DataFrame({
            "Variable": datos_numericos.columns,
            "Valores extremos": valores_extremos.values})

        st.dataframe(
            tabla_extremos,
            use_container_width=True)

        st.write(
            "La detección preliminar identifica valores que se encuentran "
            "por debajo o por encima de los límites establecidos mediante "
            "el rango intercuartílico (IQR)." )
    else:

        st.warning("⚠️ Debes cargar el archivo CSV para realizar el Ítem 3." )




elif contenido ==("Ítem 4"):
    st.write("✅Te encuentras en el Ítem 4: Análisis de valores faltantes")
    st.write(
        "En este ítem se analizará la cantidad y el porcentaje "
        "de valores faltantes en cada variable del dataset.")
    archivo = st.file_uploader(
        "Selecciona el archivo CSV",
        type=["csv"],
        key="archivo_item4" )
    if archivo is not None:

        df = pd.read_csv(archivo)

        st.success("✅ Archivo cargado correctamente.")
      
        st.subheader("1️⃣ Conteo de valores faltantes")

        valores_nulos = df.isnull().sum()
        porcentaje_nulos = (valores_nulos / len(df)) * 100

        tabla_faltantes = pd.DataFrame({
            "Variable": df.columns,
            "Valores faltantes": valores_nulos.values,
            "Porcentaje (%)": porcentaje_nulos.values })
        tabla_faltantes["Porcentaje (%)"] = tabla_faltantes[
            "Porcentaje (%)"].round(2)

        st.dataframe(
            tabla_faltantes,
            use_container_width=True)
      
        st.subheader("2️⃣ Resumen de valores faltantes")

        total_nulos = valores_nulos.sum()

        variables_con_nulos = (valores_nulos > 0).sum()

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Total de valores faltantes",
                total_nulos)

        with col2:
            st.metric(
                "Variables con valores faltantes",
                variables_con_nulos)
          
        st.subheader("3️⃣ Visualización de valores faltantes")

        tabla_grafico = tabla_faltantes[
            tabla_faltantes["Valores faltantes"] > 0 ]
        if len(tabla_grafico) > 0:

            st.bar_chart( tabla_grafico.set_index("Variable")[ "Valores faltantes"] )

        else:

            st.info( "ℹ️ No existen valores faltantes para visualizar.")
          
        st.subheader("4️⃣ Tratamiento de los valores faltantes")

        if total_nulos == 0:

            st.success( "✅ El dataset no presenta valores faltantes. "
                "Por lo tanto, no es necesario aplicar técnicas de "
                "imputación o eliminación de registros por valores nulos.")

        else:

            st.warning( "⚠️ Se identificaron valores faltantes. "
                "Antes de eliminarlos o imputarlos, se debe analizar "
                "la variable y determinar si los datos faltantes pueden "
                "afectar el análisis.")
    else:

        st.warning( "⚠️ Debes cargar el archivo CSV para realizar el Ítem 4.")

elif contenido ==("Ítem 5"):
    st.write("✅Te encuentras en el Ítem 5: Distribución de variables numéricas")
    st.write(
        "En este ítem se analizará la distribución de variables numéricas "
        "mediante histogramas, observando su forma, concentración, "
        "asimetría y posibles valores extremos.")

    archivo = st.file_uploader(
        "Selecciona el archivo CSV",
        type=["csv"],
        key="archivo_item5")
    if archivo is not None:

        df = pd.read_csv(archivo)

        st.success("✅ Archivo cargado correctamente.")
       
        variables = [
            "player_rating",
            "performance_score",
            "pass_accuracy",
            "distance_covered_km",
            "top_speed_kmh"]
        st.subheader("1️⃣ Histogramas de las variables")

        for variable in variables:

            st.write(f"### 📌 {variable}")

            fig, ax = plt.subplots(figsize=(8, 4))

            sns.histplot(
                data=df,
                x=variable,
                bins=20,
                kde=True,
                ax=ax)
            ax.set_title(f"Distribución de {variable}")
            ax.set_xlabel(variable)
            ax.set_ylabel("Frecuencia")

            st.pyplot(fig)

            plt.close(fig)

        st.subheader("2️⃣ Distribución de variables según posición")

        st.write(
            "Se revisan las distribuciones por posición para evitar "
            "comparaciones inadecuadas entre porteros y jugadores de campo.")

        variable_posicion = st.selectbox(
            "Selecciona una variable:",
            variables)
        fig, ax = plt.subplots(figsize=(10, 5))

        sns.histplot(
            data=df,
            x=variable_posicion,
            hue="position",
            bins=20,
            kde=True,
            element="step",
            common_norm=False,
            ax=ax )
        ax.set_title(f"Distribución de {variable_posicion} según posición")

        ax.set_xlabel(variable_posicion)
        ax.set_ylabel("Frecuencia")

        st.pyplot(fig)

        plt.close(fig)

        st.subheader("3️⃣ Interpretación visual")

        st.write(
            """
            **Forma:** permite observar si la distribución presenta una
            forma aproximadamente simétrica, concentrada o irregular.

            **Concentración:** permite identificar en qué rango se agrupan
            la mayoría de los valores.

            **Asimetría:** una distribución puede presentar mayor
            concentración hacia un extremo y una cola hacia el otro.

            **Valores extremos:** los valores alejados de la concentración
            principal pueden representar posibles valores extremos y deben
            revisarse considerando el contexto de cada variable.

            **Posición:** las variables de rendimiento deben interpretarse
            considerando la posición del jugador, debido a que las funciones
            de un portero son diferentes a las de los jugadores de campo.
            """
        )
   else:

        st.warning( "⚠️ Debes cargar el archivo CSV para realizar el Ítem 5.")
       
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
