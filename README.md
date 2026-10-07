# PROYECTO_FINAL_DMC2
📊 Análisis Exploratorio de Datos - FIFA World Cup 2026
👨‍💻 Información del proyecto

Autor: Franco Olivera Estación
Curso: Especialización en Python for Analytics
Docente: MSc. Carlos Carrillo Villavicencio
Año: 2026

📌 Descripción del proyecto

Este proyecto desarrolla un Análisis Exploratorio de Datos (EDA) utilizando Python y Streamlit sobre información del rendimiento de jugadores de la FIFA World Cup 2026.

El objetivo es explorar las características técnicas, ofensivas, defensivas y físicas de los jugadores mediante estadísticas descriptivas, tablas y visualizaciones interactivas.

La aplicación permite analizar el rendimiento de los jugadores según diferentes características, como posición, equipo, resultado del partido y fase del torneo.

El proyecto tiene un enfoque exploratorio y descriptivo, por lo que no se construyen modelos predictivos.


📸 Capturas de la aplicación

A continuación, se presentan algunas capturas de las principales secciones de la aplicación desarrollada en Streamlit:

🏠 Página principal
<img width="1897" height="916" alt="image" src="https://github.com/user-attachments/assets/61628004-e099-40de-9845-8cfaca14e098" />
📂 Carga y visualización del dataset
<img width="1911" height="867" alt="image" src="https://github.com/user-attachments/assets/de41f29c-4df8-447d-8f07-da03b1ad2a16" />

📊 Análisis de distribuciones

<img width="1725" height="741" alt="image" src="https://github.com/user-attachments/assets/e3a9764c-9d21-47b2-973b-cdb14ad0f6a6" />

⚙️ Análisis basado en parámetros

<img width="1367" height="692" alt="image" src="https://github.com/user-attachments/assets/8158b36f-273a-456a-a030-7198cf8b2612" />

🔎 Hallazgos clave del EDA
<img width="1907" height="892" alt="image" src="https://github.com/user-attachments/assets/71ac90ce-ce6f-4bc5-9643-1c066c3e98c6" />

▶️ Instrucciones de ejecución

Para ejecutar la aplicación de análisis exploratorio de datos, seguir los siguientes pasos:

1. Clonar el repositorio

Descargar el proyecto desde GitHub:

git clone URL_DE_TU_REPOSITORIO
2. Ingresar a la carpeta del proyecto
cd proyecto_final_dmc2
3. Instalar las librerías necesarias

Ejecutar:

pip install -r requirements.txt

Las principales librerías utilizadas son:

Streamlit
Pandas
NumPy
Matplotlib
Seaborn
4. Ejecutar la aplicación

Iniciar la aplicación con:

streamlit run app.py
5. Cargar el dataset

Una vez iniciada la aplicación:

Abrir la aplicación en el navegador.
Seleccionar el módulo correspondiente desde el menú lateral.
Cargar el archivo fifa_world_cup_2026_player_performance.csv.
Explorar los diferentes ítems del análisis exploratorio de datos.
6. Acceso a la aplicación

La aplicación también se encuentra desplegada en Streamlit Community Cloud, permitiendo acceder al análisis directamente desde un navegador web.

## 📋 Descripción breve de las variables principales

El dataset contiene información sobre el rendimiento de jugadores durante partidos de la Copa Mundial. Las principales variables utilizadas en el análisis son:

| Variable                 | Descripción                                                                     |
| ------------------------ | ------------------------------------------------------------------------------- |
| `player_name`            | Nombre del jugador.                                                             |
| `team`                   | Selección o equipo al que pertenece el jugador.                                 |
| `position`               | Posición del jugador en el campo.                                               |
| `age`                    | Edad del jugador.                                                               |
| `preferred_foot`         | Pie preferido del jugador: izquierdo o derecho.                                 |
| `match_date`             | Fecha en la que se disputó el partido.                                          |
| `tournament_stage`       | Etapa del torneo en la que se jugó el partido.                                  |
| `match_result`           | Resultado obtenido por el equipo en el partido.                                 |
| `goals`                  | Cantidad de goles anotados por el jugador.                                      |
| `assists`                | Cantidad de asistencias realizadas.                                             |
| `shots`                  | Número de disparos realizados.                                                  |
| `shots_on_target`        | Número de disparos que fueron dirigidos al arco.                                |
| `pass_accuracy`          | Porcentaje de precisión en los pases realizados.                                |
| `tackles`                | Cantidad de entradas defensivas realizadas.                                     |
| `interceptions`          | Número de intercepciones realizadas.                                            |
| `distance_covered_km`    | Distancia recorrida por el jugador durante el partido, expresada en kilómetros. |
| `top_speed_kmh`          | Velocidad máxima alcanzada por el jugador, expresada en km/h.                   |
| `accelerations`          | Número de aceleraciones realizadas durante el partido.                          |
| `stamina_score`          | Indicador relacionado con la resistencia física del jugador.                    |
| `player_rating`          | Calificación general del rendimiento del jugador.                               |
| `performance_score`      | Puntuación que representa el desempeño del jugador en el partido.               |
| `offensive_contribution` | Indicador de contribución del jugador en acciones ofensivas.                    |
| `defensive_contribution` | Indicador de contribución del jugador en acciones defensivas.                   |
| `creativity_score`       | Indicador relacionado con la creatividad del jugador durante el juego.          |
| `consistency_score`      | Indicador relacionado con la consistencia del rendimiento.                      |
| `tournament_rating`      | Calificación del jugador considerando su participación en el torneo.            |

Estas variables permiten realizar análisis **descriptivos, comparativos y exploratorios** del rendimiento de los jugadores según su posición, equipo, resultado del partido, etapa del torneo y características físicas y técnicas.


