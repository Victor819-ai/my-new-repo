import streamlit as st
import pandas as pd
import plotly.express as px

# Título del dashboard
st.header("Panel interactivo de análisis de vehículos")

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Casilla para histograma
build_histogram = st.checkbox('Mostrar histograma de kilometraje')

if build_histogram:
    st.write("Histograma de la columna 'odometer'")
    fig = px.histogram(car_data, x='odometer', title='Distribución del kilometraje')
    st.plotly_chart(fig, use_container_width=True)

# Casilla para gráfico de dispersión
build_scatter = st.checkbox('Mostrar gráfico de dispersión: Kilometraje vs Precio')

if build_scatter:
    st.write("Relación entre kilometraje (odometer) y precio")
    fig2 = px.scatter(car_data, x='odometer', y='price', title='Kilometraje vs Precio')
    st.plotly_chart(fig2, use_container_width=True)
