
# my-new-repo

## 🚗 Aplicación web: Análisis de anuncios de vehículos usados

Esta aplicación web interactiva fue desarrollada como parte del Proyecto del Módulo 7 de TripleTen. Permite a los usuarios visualizar datos de un conjunto de anuncios de vehículos en venta mediante gráficos dinámicos construidos con **Streamlit** y **Plotly Express**.

---

## 🔍 Funcionalidad

La app ofrece un panel visual para el análisis de datos automotrices, incluyendo:

- 📊 **Histograma de kilometraje (odometer)**
- 🟣 **Gráfico de dispersión entre kilometraje y precio**
- ✅ **Controles mediante casillas de verificación** para mostrar u ocultar los gráficos

---

## 📁 Estructura del proyecto

```
my-new-repo/
├── vehicles_us.csv           # Conjunto de datos
├── app.py                    # Aplicación principal de Streamlit
├── test3.py                  # Código auxiliar de pruebas con gráficos
├── requirements.txt          # Librerías necesarias para la app
├── README.md                 # Este archivo
├── notebooks/
│   └── EDA.ipynb             # Exploración de datos con Jupyter Notebook
└── vehicles_env/             # Entorno virtual (no incluido en GitHub)
```

---

## ⚙️ Tecnologías utilizadas

- Python 3.12
- pandas
- plotly-express
- streamlit

---

## ▶️ Cómo ejecutar localmente

1. Clona el repositorio:
   ```
   git clone https://github.com/TU_USUARIO/my-new-repo.git
   cd my-new-repo
   ```

2. Activa el entorno virtual (si ya existe) o créalo:
   ```
   python -m venv vehicles_env
   .\vehicles_env\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. Ejecuta la app:
   ```
   streamlit run app.py
   ```

---

## ☁️ Despliegue en Render

### Build Command:
```
pip install --upgrade pip && pip install -r requirements.txt
```

### Start Command:
```
streamlit run app.py
```

Accede a tu aplicación en:  
➡️ https://<NOMBRE-DE-TU-APP>.onrender.com/

---

## 📌 Créditos

Proyecto desarrollado por Victor819-ai de GitHub] como parte del programa **TripleTen Bootcamp de Data Analyst**.
