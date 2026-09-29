# Panel de anuncios de venta de coches (vehicles_us)

## Descripción del proyecto

Esta es una aplicación web interactiva construida con **Streamlit** que permite explorar
un conjunto de datos de anuncios de venta de coches usados en Estados Unidos
(`vehicles_us.csv`, más de 51,000 anuncios).

La aplicación permite a los usuarios:

- Ver una muestra del conjunto de datos.
- Generar un **histograma** interactivo de la distribución del kilometraje (odómetro)
  de los vehículos.
- Generar un **gráfico de dispersión** interactivo entre el precio y el kilometraje
  de los vehículos.

El análisis exploratorio de datos (EDA) inicial se encuentra en el notebook
`notebooks/EDA.ipynb`.

## Aplicación desplegada

🔗 **[Abrir la aplicación en Render](https://vehicles-dashboard-0o3t.onrender.com)**



## Cómo ejecutar el proyecto localmente

1. Clona este repositorio:
   ```bash
   git clone <URL_DE_TU_REPOSITORIO>
   cd <NOMBRE_DEL_REPOSITORIO>
   ```

2. Crea y activa un entorno virtual:
   ```bash
   conda create --name vehicles_env python=3.9
   conda activate vehicles_env
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Ejecuta la aplicación:
   ```bash
   streamlit run app.py
   ```

5. Abre tu navegador en `http://localhost:8501`.

## Estructura del proyecto

```
.
├── app.py                 # Código de la aplicación web Streamlit
├── vehicles_us.csv         # Dataset de anuncios de coches
├── requirements.txt        # Librerías necesarias
├── README.md
├── .gitignore
└── notebooks/
    └── EDA.ipynb            # Análisis exploratorio de datos
```

## Tecnologías utilizadas

- Python
- Pandas
- Plotly
- Streamlit
- Render (despliegue)
