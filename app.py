import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado principal de la aplicación
st.header('Panel de anuncios de venta de coches (EE. UU.)')

st.write(
      'Esta aplicación permite explorar un conjunto de datos con más de '
      '51,000 anuncios de venta de coches usados en Estados Unidos.'
)

# Mostramos una muestra del dataset
st.write('Muestra de los datos:')
st.dataframe(car_data.head(10))

# Casilla de verificación para el histograma
build_histogram = st.checkbox('Construir un histograma del kilometraje (odómetro)')

if build_histogram:
      st.write('Creación de un histograma para la distribución del kilometraje de los vehículos')

    fig_hist = px.histogram(car_data, x='odometer', nbins=50)
    fig_hist.update_layout(
              title_text='Distribución del kilometraje (odómetro)',
              xaxis_title='Kilometraje (millas)',
              yaxis_title='Número de anuncios'
    )
    st.plotly_chart(fig_hist, use_container_width=True)

# Casilla de verificación para el gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión (precio vs. kilometraje)')

if build_scatter:
      st.write('Creación de un gráfico de dispersión entre el precio y el kilometraje de los vehículos')

    fig_scatter = px.scatter(car_data, x='odometer', y='price')
    fig_scatter.update_layout(
              title_text='Precio del vehículo vs. kilometraje',
              xaxis_title='Kilometraje (millas)',
              yaxis_title='Precio ($)'
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
