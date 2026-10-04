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
    st.write(
        "En este ítem se analizarán las variables categóricas mediante "
        "conteos, proporciones y gráficos de barras."
    )

    archivo = st.file_uploader(
        "Selecciona el archivo CSV",
        type=["csv"],
        key="archivo_item6"
    )
    if archivo is not None:

        df = pd.read_csv(archivo)

        st.success("✅ Archivo cargado correctamente.")
        variables_categoricas = [
            "position",
            "team",
            "tournament_stage",
            "match_result",
            "preferred_foot"
        ]
        st.subheader("1️⃣ Selección de variable categórica")

        variable = st.selectbox(
            "Selecciona una variable:",
            variables_categoricas)
        st.subheader("2️⃣ Conteo de categorías")

        conteo = df[variable].value_counts()

        tabla_conteo = pd.DataFrame({
            "Categoría": conteo.index,
            "Conteo": conteo.values})

        st.dataframe(
            tabla_conteo,
            use_container_width=True )
      
        st.subheader("3️⃣ Proporción de categorías")

        proporciones = df[variable].value_counts(normalize=True) * 100

        tabla_proporciones = pd.DataFrame({
            "Categoría": proporciones.index,
            "Proporción (%)": proporciones.values.round(2)})

        st.dataframe(
            tabla_proporciones,
            use_container_width=True )
      
        st.subheader("4️⃣ Gráfico de barras")

        fig, ax = plt.subplots(figsize=(10, 5))

        conteo.plot(
            kind="bar",
            ax=ax)

        ax.set_title(f"Distribución de {variable}")
        ax.set_xlabel(variable)
        ax.set_ylabel("Cantidad")

        plt.xticks(rotation=45)

        st.pyplot(fig)

        plt.close(fig)

        st.subheader("5️⃣ Comparación de categorías")

        categoria_mayor = conteo.idxmax()
        cantidad_mayor = conteo.max()

        categoria_menor = conteo.idxmin()
        cantidad_menor = conteo.min()

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Categoría con mayor frecuencia",
                categoria_mayor,
                cantidad_mayor )

        with col2:
            st.metric(
                "Categoría con menor frecuencia",
                categoria_menor,
                cantidad_menor)

        st.write(
            f"La categoría con mayor frecuencia es **{categoria_mayor}**, "
            f"con **{cantidad_mayor} registros**.")
    else:

        st.warning("⚠️ Debes cargar el archivo CSV para realizar el Ítem 6.")


elif contenido ==("Ítem 7"):
    st.write("✅Te encuentras en el Ítem 7: Análisis bivariado (numérico vs categórico)")
    st.write(
        "En este ítem se compararán variables numéricas según diferentes "
        "variables categóricas para identificar diferencias entre grupos."
    )

    archivo = st.file_uploader(
        "Selecciona el archivo CSV",
        type=["csv"],
        key="archivo_item7"
    )
    if archivo is not None:

        df = pd.read_csv(archivo)

        st.success("✅ Archivo cargado correctamente.")

        st.subheader("1️⃣ Player rating según posición")

        fig, ax = plt.subplots(figsize=(10, 5))

        sns.boxplot(
            data=df,
            x="position",
            y="player_rating",
            ax=ax )

        ax.set_title("Player rating según posición")
        ax.set_xlabel("Posición")
        ax.set_ylabel("Player rating")

        plt.xticks(rotation=45)

        st.pyplot(fig)

        plt.close(fig)

        st.write(
            "Este gráfico permite comparar la distribución del rating "
            "de los jugadores según su posición. La línea central de "
            "cada caja representa la mediana.")
      
        st.subheader("2️⃣ Performance score según resultado del partido")

        fig, ax = plt.subplots(figsize=(8, 5))

        sns.boxplot(
            data=df,
            x="match_result",
            y="performance_score",
            ax=ax
        )

        ax.set_title("Performance score según resultado del partido")
        ax.set_xlabel("Resultado del partido")
        ax.set_ylabel("Performance score")

        st.pyplot(fig)

        plt.close(fig)

        st.write(
            "Este análisis permite comparar el nivel de performance "
            "de los jugadores según el resultado obtenido en el partido.") 
        st.subheader("2️⃣ Performance score según resultado del partido")

        fig, ax = plt.subplots(figsize=(8, 5))

        sns.boxplot(
            data=df,
            x="match_result",
            y="performance_score",
            ax=ax
        )

        ax.set_title("Performance score según resultado del partido")
        ax.set_xlabel("Resultado del partido")
        ax.set_ylabel("Performance score")

        st.pyplot(fig)

        plt.close(fig)

        st.write(
            "Este análisis permite comparar el nivel de performance "
            "de los jugadores según el resultado obtenido en el partido."
        )

        st.subheader("3️⃣ Distancia recorrida según posición")

        fig, ax = plt.subplots(figsize=(10, 5))

        sns.boxplot(
            data=df,
            x="position",
            y="distance_covered_km",
            ax=ax
        )

        ax.set_title("Distancia recorrida según posición")
        ax.set_xlabel("Posición")
        ax.set_ylabel("Distancia recorrida (km)")

        plt.xticks(rotation=45)

        st.pyplot(fig)

        plt.close(fig)

        st.write(
            "La distancia recorrida permite observar diferencias en "
            "el esfuerzo físico registrado entre las diferentes posiciones."
        )

        st.subheader("4️⃣ Resumen de las comparaciones")

        resumen_position = df.groupby("position")[
            ["player_rating", "distance_covered_km"]
        ].median().round(2)

        st.write("**Medianas de player rating y distancia recorrida por posición:**")

        st.dataframe(
            resumen_position,
            use_container_width=True
        )

        resumen_resultado = df.groupby("match_result")[
            "performance_score"
        ].median().round(2)

        st.write("**Mediana de performance score según resultado:**")

        st.dataframe(
            resumen_resultado,
            use_container_width=True
        )
        st.subheader("5️⃣ Interpretación")

        st.write(
            """
            **Player rating:** permite identificar cómo se distribuye
            el rating de los jugadores según su posición.

            **Performance score:** permite comparar el desempeño de los
            jugadores según el resultado del partido.

            **Distancia recorrida:** permite observar diferencias en la
            actividad física registrada entre posiciones.

            Los boxplots permiten observar la mediana, la dispersión
            de los datos y posibles valores extremos. Las diferencias
            encontradas deben interpretarse considerando las funciones
            específicas de cada posición.
            """
        )
    else:
        st.warning( "⚠️ Debes cargar el archivo CSV para realizar el Ítem 7.")
      

elif contenido ==("Ítem 8"):
    st.write("✅Te encuentras en el Ítem 8: Análisis bivariado (categórico vs categórico)")
    st.write(
        "En este ítem se analizarán las relaciones entre dos variables "
        "categóricas mediante tablas de frecuencia y gráficos de barras."
    )

    archivo = st.file_uploader(
        "Selecciona el archivo CSV",
        type=["csv"],
        key="archivo_item8"
    )

    if archivo is not None:

        df = pd.read_csv(archivo)

        st.success("✅ Archivo cargado correctamente.")
        st.subheader("1️⃣ Posición según fase del torneo")

        tabla_position_stage = pd.crosstab(
            df["position"],
            df["tournament_stage"])

        st.write("**Tabla de frecuencia:**")

        st.dataframe(
            tabla_position_stage,
            use_container_width=True)

        fig, ax = plt.subplots(figsize=(10, 5))

        tabla_position_stage.plot(
            kind="bar",
            ax=ax)

        ax.set_title("Posición según fase del torneo")
        ax.set_xlabel("Posición")
        ax.set_ylabel("Cantidad de registros")

        plt.xticks(rotation=45)

        st.pyplot(fig)

        plt.close(fig)

        st.subheader("2️⃣ Equipo según resultado del partido")

        tabla_team_resultado = pd.crosstab(
            df["team"],
            df["match_result"])

        st.write("**Tabla de frecuencia:**")

        st.dataframe(
            tabla_team_resultado,
            use_container_width=True)

        fig, ax = plt.subplots(figsize=(12, 6))

        tabla_team_resultado.plot(
            kind="bar",
            ax=ax)

        ax.set_title("Equipo según resultado del partido")
        ax.set_xlabel("Equipo")
        ax.set_ylabel("Cantidad de registros")

        plt.xticks(rotation=90)

        st.pyplot(fig)

        plt.close(fig)
      
        st.subheader("3️⃣ Pie preferido según posición")

        tabla_pie_position = pd.crosstab(
            df["preferred_foot"],
            df["position"])

        st.write("**Tabla de frecuencia:**")

        st.dataframe(
            tabla_pie_position,
            use_container_width=True)

        fig, ax = plt.subplots(figsize=(10, 5))

        tabla_pie_position.plot(
            kind="bar",
            ax=ax)

        ax.set_title("Pie preferido según posición")
        ax.set_xlabel("Pie preferido")
        ax.set_ylabel("Cantidad de registros")

        plt.xticks(rotation=0)

        st.pyplot(fig)

        plt.close(fig)

        st.subheader("4️⃣ Interpretación de los resultados")

        st.write(
            """
            **Position vs tournament_stage:** permite observar cómo se
            distribuyen las posiciones de los jugadores en las diferentes
            fases del torneo.

            **Team vs match_result:** permite identificar la frecuencia
            de los diferentes resultados de partido para cada equipo.

            **Preferred_foot vs position:** permite observar la relación
            entre el pie preferido de los jugadores y su posición.

            Las tablas de frecuencia permiten conocer la cantidad de
            registros que pertenecen a cada combinación de categorías.
            Los gráficos de barras facilitan la comparación visual
            entre los grupos.
            """
        )

    else:
        st.warning( "⚠️ Debes cargar el archivo CSV para realizar el Ítem 8.")
      
elif contenido ==("Ítem 9"):
    st.write("✅Te encuentras en el Ítem 9: Análisis basado en parámetros seleccionados")
    st.write(
        "En este ítem el usuario podrá seleccionar diferentes filtros "
        "y métricas para realizar un análisis dinámico del dataset."
    )

    archivo = st.file_uploader(
        "Selecciona el archivo CSV",
        type=["csv"],
        key="archivo_item9"
    )

    if archivo is not None:

        df = pd.read_csv(archivo)

        st.success("✅ Archivo cargado correctamente.")

        if "match_date" in df.columns:

            df["match_date"] = pd.to_datetime(
                df["match_date"],
                errors="coerce"
            )
          
        st.subheader("🔎 1. Filtros del análisis")

        col1, col2 = st.columns(2)
      
        with col1:

            equipos = sorted(
                df["team"].dropna().unique().tolist()
            )

            equipos_seleccionados = st.multiselect(
                "Selecciona el equipo:",
                equipos
            )

      
        with col2:

            posiciones = sorted(
                df["position"].dropna().unique().tolist()
            )

            posiciones_seleccionadas = st.multiselect(
                "Selecciona la posición:",
                posiciones
            )

        col3, col4 = st.columns(2)
      
        with col3:

            fases = sorted(
                df["tournament_stage"].dropna().unique().tolist()
            )

            fases_seleccionadas = st.multiselect(
                "Selecciona la fase del torneo:",
                fases
            )
        with col4:

            resultados = sorted(
                df["match_result"].dropna().unique().tolist()
            )

            resultados_seleccionados = st.multiselect(
                "Selecciona el resultado:",
                resultados
            )

        jugadores = sorted(
            df["player_name"].dropna().unique().tolist()
        )

        jugadores_seleccionados = st.multiselect(
            "Selecciona jugadores:",
            jugadores
        )
        df_filtrado = df.copy()

        if equipos_seleccionados:
            df_filtrado = df_filtrado[
                df_filtrado["team"].isin(equipos_seleccionados)
            ]

        if posiciones_seleccionadas:
            df_filtrado = df_filtrado[
                df_filtrado["position"].isin(posiciones_seleccionadas)
            ]

        if fases_seleccionadas:
            df_filtrado = df_filtrado[
                df_filtrado["tournament_stage"].isin(fases_seleccionadas)
            ]

        if resultados_seleccionados:
            df_filtrado = df_filtrado[
                df_filtrado["match_result"].isin(resultados_seleccionados)
            ]

        if jugadores_seleccionados:
            df_filtrado = df_filtrado[
                df_filtrado["player_name"].isin(jugadores_seleccionados)
            ]
        st.subheader("🎚️ 2. Filtro por rango numérico")

        minimo_rating = float(df["player_rating"].min())
        maximo_rating = float(df["player_rating"].max())

        rango_rating = st.slider(
            "Selecciona el rango de Player Rating:",
            min_value=minimo_rating,
            max_value=maximo_rating,
            value=(minimo_rating, maximo_rating)
        )

        df_filtrado = df_filtrado[
            (df_filtrado["player_rating"] >= rango_rating[0]) &
            (df_filtrado["player_rating"] <= rango_rating[1])
        ]
        st.subheader("📊 3. Selección de métricas")

        tipo_metrica = st.selectbox(
            "Selecciona el tipo de métrica:",
            [
                "Ofensivas",
                "Defensivas",
                "Físicas"
            ]
        )

        if tipo_metrica == "Ofensivas":

            metricas = [
                "goals",
                "assists",
                "shots",
                "shots_on_target",
                "expected_goals_xg",
                "key_passes"
            ]

        elif tipo_metrica == "Defensivas":

            metricas = [
                "tackles",
                "interceptions",
                "clearances",
                "blocks",
                "recoveries",
                "defensive_actions"
            ]

        else:

            metricas = [
                "distance_covered_km",
                "sprint_distance_km",
                "top_speed_kmh",
                "accelerations",
                "decelerations",
                "stamina_score"
            ]

        metricas_seleccionadas = st.multiselect(
            "Selecciona las métricas que deseas comparar:",
            metricas
        )

        st.subheader("📋 4. Resultado del análisis")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Registros encontrados",
                len(df_filtrado)
            )

        with col2:
            st.metric(
                "Jugadores encontrados",
                df_filtrado["player_name"].nunique()
            )
        if metricas_seleccionadas:

            columnas_mostrar = [
                "player_name",
                "team",
                "position"
            ] + metricas_seleccionadas

            tabla_resultado = df_filtrado[columnas_mostrar]

            st.dataframe(
                tabla_resultado,
                use_container_width=True
            )

            st.subheader("📈 5. Comparación de jugadores")

            if len(metricas_seleccionadas) == 1:

                metrica = metricas_seleccionadas[0]

                promedio_jugador = (
                    df_filtrado
                    .groupby("player_name")[metrica]
                    .mean()
                    .sort_values(ascending=False)
                    .head(15)
                )

                fig, ax = plt.subplots(figsize=(10, 5))

                promedio_jugador.plot(
                    kind="bar",
                    ax=ax
                )

                ax.set_title(
                    f"Promedio de {metrica} por jugador"
                )

                ax.set_xlabel("Jugador")
                ax.set_ylabel(metrica)

                plt.xticks(rotation=75)

                st.pyplot(fig)

                plt.close(fig)

            else:

                st.write(
                    "Selecciona una sola métrica para visualizar "
                    "el gráfico de comparación."
                )

        else:

            st.info(
                "ℹ️ Selecciona al menos una métrica para realizar "
                "la comparación.")
            st.subheader("📈 5. Comparación de jugadores")

            if len(metricas_seleccionadas) == 1:

                metrica = metricas_seleccionadas[0]

                promedio_jugador = (
                    df_filtrado
                    .groupby("player_name")[metrica]
                    .mean()
                    .sort_values(ascending=False)
                    .head(15)
                )

                fig, ax = plt.subplots(figsize=(10, 5))

                promedio_jugador.plot(
                    kind="bar",
                    ax=ax
                )

                ax.set_title(
                    f"Promedio de {metrica} por jugador"
                )

                ax.set_xlabel("Jugador")
                ax.set_ylabel(metrica)

                plt.xticks(rotation=75)

                st.pyplot(fig)

                plt.close(fig)

            else:

                st.write(
                    "Selecciona una sola métrica para visualizar "
                    "el gráfico de comparación."
                )

    else:

            st.info(
                "ℹ️ Selecciona al menos una métrica para realizar "
                "la comparación."
            )

    st.subheader("📅 6. Análisis temporal")

    if df["match_date"].notna().sum() > 0:

            fecha_min = df["match_date"].min().date()
            fecha_max = df["match_date"].max().date()

            rango_fechas = st.date_input(
                "Selecciona el rango de fechas:",
                value=(fecha_min, fecha_max),
                min_value=fecha_min,
                max_value=fecha_max
            )

            if len(rango_fechas) == 2:

                fecha_inicio = pd.to_datetime(
                    rango_fechas[0]
                )

                fecha_fin = pd.to_datetime(
                    rango_fechas[1]
                )

                df_temporal = df_filtrado[
                    (df_filtrado["match_date"] >= fecha_inicio) &
                    (df_filtrado["match_date"] <= fecha_fin)
                ]

                st.write(
                    f"Registros dentro del periodo seleccionado: "
                    f"**{len(df_temporal)}**"
                )

                st.dataframe(
                    df_temporal[
                        [
                            "match_date",
                            "player_name",
                            "team",
                            "position",
                            "player_rating"
                        ]
                    ],
                    use_container_width=True
                )

    else:
            st.warning(
                "⚠️ No se encontraron fechas válidas en match_date."
            )

 else:
        st.warning( "⚠️ Debes cargar el archivo CSV para realizar el Ítem 9.")


else:
    st.write("✅Te encuentras en el Ítem 10: Hallazgos clave")
