import pandas as pd
import plotly.express as px

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')  # asegúrate que el archivo está en la misma carpeta

# Crear histograma
fig = px.histogram(car_data, x='odometer', title='Distribución de Kilometraje (odometer)')
fig.show()


# Crear gráfico de dispersión
fig2 = px.scatter(car_data, x='odometer', y='price', title='Kilometraje vs Precio')
fig2.show()
