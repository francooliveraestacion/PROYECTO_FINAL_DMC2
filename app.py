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
    st.header("⚙️ Ítem 9: Análisis basado en parámetros")

    archivo = st.file_uploader(
        "Selecciona el archivo CSV",
        type=["csv"],
        key="archivo_item9"
    )
    if archivo is not None:

        df = pd.read_csv(archivo)

        df["match_date"] = pd.to_datetime(
            df["match_date"],
            errors="coerce"
        )

        st.success("✅ Archivo cargado correctamente.")

        st.subheader("🔎 Filtros")

        col1, col2 = st.columns(2)

        with col1:
            equipos = st.multiselect(
                "Team",
                sorted(df["team"].dropna().unique())
            )

        with col2:
            posiciones = st.multiselect(
                "Position",
                sorted(df["position"].dropna().unique())
            )

        col3, col4 = st.columns(2)

        with col3:
            fases = st.multiselect(
                "Tournament stage",
                sorted(df["tournament_stage"].dropna().unique())
            )

        with col4:
            resultados = st.multiselect(
                "Match result",
                sorted(df["match_result"].dropna().unique())
            )

        jugadores = st.multiselect(
            "Player name",
            sorted(df["player_name"].dropna().unique())
        )

        df_filtrado = df.copy()

        if equipos:
            df_filtrado = df_filtrado[
                df_filtrado["team"].isin(equipos)
            ]

        if posiciones:
            df_filtrado = df_filtrado[
                df_filtrado["position"].isin(posiciones)
            ]

        if fases:
            df_filtrado = df_filtrado[
                df_filtrado["tournament_stage"].isin(fases)
            ]

        if resultados:
            df_filtrado = df_filtrado[
                df_filtrado["match_result"].isin(resultados)
            ]

        if jugadores:
            df_filtrado = df_filtrado[
                df_filtrado["player_name"].isin(jugadores)
            ]

        st.subheader("🎚️ Rango de Player Rating")

        minimo = float(df["player_rating"].min())
        maximo = float(df["player_rating"].max())

        rango = st.slider(
            "Selecciona el rango:",
            minimo,
            maximo,
            (minimo, maximo)
        )

        df_filtrado = df_filtrado[
            df_filtrado["player_rating"].between(
                rango[0],
                rango[1]
            )
        ]

        st.subheader("📊 Selección de métricas")

        tipo = st.selectbox(
            "Tipo de métrica:",
            ["Ofensivas", "Defensivas", "Físicas"]
        )

        if tipo == "Ofensivas":

            opciones = [
                "goals",
                "assists",
                "shots",
                "shots_on_target",
                "expected_goals_xg",
                "key_passes"
            ]

        elif tipo == "Defensivas":

            opciones = [
                "tackles",
                "interceptions",
                "clearances",
                "blocks",
                "recoveries",
                "defensive_actions"
            ]

        else:

            opciones = [
                "distance_covered_km",
                "sprint_distance_km",
                "top_speed_kmh",
                "accelerations",
                "decelerations",
                "stamina_score"
            ]

        metricas = st.multiselect(
            "Selecciona las métricas:",
            opciones
        )

        st.subheader("📋 Resultado")

        st.metric(
            "Registros encontrados",
            len(df_filtrado)
        )

        if len(df_filtrado) == 0:

            st.warning(
                "⚠️ No existen registros con los filtros seleccionados."
            )

        elif metricas:

            columnas = [
                "player_name",
                "team",
                "position"
            ] + metricas

            st.dataframe(
                df_filtrado[columnas],
                use_container_width=True
            )

            if len(metricas) == 1:

                metrica = metricas[0]

                promedio = (
                    df_filtrado
                    .groupby("player_name")[metrica]
                    .mean()
                    .dropna()
                    .sort_values(ascending=False)
                    .head(15)
                )

                if not promedio.empty:

                    fig, ax = plt.subplots(figsize=(10, 5))

                    promedio.plot(
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

                st.info(
                    "Selecciona una sola métrica para mostrar el gráfico."
                )

        else:

            st.info(
                "Selecciona al menos una métrica para realizar el análisis."
            )

        st.subheader("📅 Análisis temporal")

        fechas_validas = df_filtrado["match_date"].dropna()

        if not fechas_validas.empty:

            fecha_inicio = fechas_validas.min().date()
            fecha_fin = fechas_validas.max().date()

            fecha = st.date_input(
                "Selecciona una fecha:",
                value=fecha_inicio,
                min_value=fecha_inicio,
                max_value=fecha_fin
            )

            datos_fecha = df_filtrado[
                df_filtrado["match_date"].dt.date == fecha
            ]

            st.write(
                f"Registros del {fecha}: **{len(datos_fecha)}**"
            )

        else:

            st.info(
                "No existen fechas disponibles con los filtros seleccionados."
            )

    else:

        st.warning(
            "⚠️ Debes cargar el archivo CSV para realizar el Ítem 9."
        )

else:
    st.write("✅Te encuentras en el Ítem 10: Hallazgos clave")
    st.write(
        "En este ítem se presentan los principales hallazgos obtenidos "
        "del análisis exploratorio de datos y algunas recomendaciones "
        "orientadas a la toma de decisiones."
    )

    archivo = st.file_uploader(
        "Selecciona el archivo CSV",
        type=["csv"],
        key="archivo_item10"
    )
    if archivo is not None:

        df = pd.read_csv(archivo)

        st.success("✅ Archivo cargado correctamente.")

        st.subheader("📊 1. Visualización resumen")

        col1, col2 = st.columns(2)

        with col1:

            fig, ax = plt.subplots(figsize=(7, 4))

            sns.histplot(
                data=df,
                x="player_rating",
                bins=20,
                kde=True,
                ax=ax
            )

            ax.set_title("Distribución del Player Rating")
            ax.set_xlabel("Player Rating")
            ax.set_ylabel("Frecuencia")

            st.pyplot(fig)

            plt.close(fig)

        with col2:

            promedio_posicion = (
                df.groupby("position")["performance_score"]
                .mean()
                .sort_values(ascending=False)
            )

            fig, ax = plt.subplots(figsize=(7, 4))

            promedio_posicion.plot(
                kind="bar",
                ax=ax
            )

            ax.set_title(
                "Performance Score promedio por posición"
            )

            ax.set_xlabel("Posición")
            ax.set_ylabel("Performance Score")

            plt.xticks(rotation=45)

            st.pyplot(fig)

            plt.close(fig)

    st.subheader("📈 2. Indicadores principales")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
            st.metric(
                "Player Rating promedio",
                round(df["player_rating"].mean(), 2)
            )

    with col2:
            st.metric(
                "Performance Score promedio",
                round(df["performance_score"].mean(), 2)
            )

    with col3:
            st.metric(
                "Velocidad máxima promedio",
                round(df["top_speed_kmh"].mean(), 2)
            )

    with col4:
            st.metric(
                "Distancia recorrida promedio",
                round(df["distance_covered_km"].mean(), 2)
            )
    st.subheader("🔎 3. Principales hallazgos")

        rating_promedio = df["player_rating"].mean()
        performance_promedio = df["performance_score"].mean()
        velocidad_promedio = df["top_speed_kmh"].mean()
        distancia_promedio = df["distance_covered_km"].mean()

        posicion_mejor_rating = (
            df.groupby("position")["player_rating"]
            .mean()
            .idxmax()
        )

        posicion_mayor_distancia = (
            df.groupby("position")["distance_covered_km"]
            .mean()
            .idxmax()
        )

        resultado_mayor_performance = (
            df.groupby("match_result")["performance_score"]
            .mean()
            .idxmax()
        )

        st.write(
            f"**1. Rating:** El Player Rating promedio registrado "
            f"en el dataset es de **{rating_promedio:.2f}**."
        )

        st.write(
            f"**2. Performance:** El Performance Score promedio es de "
            f"**{performance_promedio:.2f}**."
        )

        st.write(
            f"**3. Posición:** La posición con mayor Player Rating "
            f"promedio es **{posicion_mejor_rating}**."
        )

        st.write(
            f"**4. Actividad física:** La posición con mayor distancia "
            f"recorrida promedio es **{posicion_mayor_distancia}**."
        )

        st.write(
            f"**5. Resultado:** El resultado de partido asociado con "
            f"mayor Performance Score promedio es **{resultado_mayor_performance}**."
        )

        st.subheader("💡 4. Recomendaciones para la toma de decisiones")

        st.write(
            """
            **1. Evaluación por posición:** comparar el rendimiento
            considerando la posición del jugador, debido a que las
            funciones y exigencias son diferentes.

            **2. Seguimiento del rendimiento:** utilizar indicadores
            como Player Rating y Performance Score para complementar
            la evaluación de los jugadores.

            **3. Análisis físico:** utilizar distancia recorrida y
            velocidad máxima como indicadores complementarios para
            analizar la exigencia física de los jugadores.

            **4. Análisis por resultado:** revisar las diferencias de
            rendimiento según el resultado del partido para identificar
            patrones relevantes en el desempeño observado.

            **5. Uso de dashboards:** mantener estos indicadores en
            visualizaciones interactivas para facilitar el seguimiento
            y apoyar la toma de decisiones basada en datos.
            """
        )
        st.subheader("📝 5. Conclusión del EDA")

        st.write(
            """
            El análisis exploratorio permitió identificar diferencias
            en el rendimiento técnico y físico de los jugadores según
            diferentes características del partido. Los resultados
            muestran la importancia de analizar conjuntamente indicadores
            de rendimiento, posición y actividad física. Estos hallazgos
            pueden utilizarse como apoyo para la evaluación y seguimiento
            de jugadores, sin realizar predicciones sobre resultados
            futuros.
            """
        )

    else:

        st.warning(
            "⚠️ Debes cargar el archivo CSV para realizar el Ítem 10."
        )



