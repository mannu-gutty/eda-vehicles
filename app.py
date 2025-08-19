import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Vehículos EDA", page_icon="🚗", layout="wide")
st.header("🚗 Dashboard de anuncios de coches")

# Carga de datos
CSV_PATH = "Data/vehicles_us.csv"
car_data = pd.read_csv(CSV_PATH)
st.success(f"Datos cargados: {len(car_data):,} filas")

st.divider()

# Botón: Histograma
hist_button = st.button("Construir histograma (odometer)")
if hist_button:
    st.write("Creación de un histograma para la columna **odometer**")
    fig_hist = px.histogram(car_data, x="odometer", nbins=50, title="Distribución del odómetro")
    st.plotly_chart(fig_hist, use_container_width=True)

# Botón: Dispersión
scatter_button = st.button("Construir dispersión (odometer vs price)")
if scatter_button:
    st.write("Creación de una dispersión **odometer** vs **price**")
    fig_scatter = px.scatter(
        car_data, x="odometer", y="price",
        opacity=0.5, title="Precio vs Kilometraje",
        labels={"odometer": "Kilometraje", "price": "Precio (USD)"}
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

# Opcional: checkboxes
with st.expander("Opcional: usar casillas de verificación"):
    if st.checkbox("Histograma (odometer)"):
        st.plotly_chart(px.histogram(car_data, x="odometer", nbins=50), use_container_width=True)
    if st.checkbox("Dispersión (odometer vs price)"):
        st.plotly_chart(px.scatter(car_data, x="odometer", y="price", opacity=0.5), use_container_width=True)
from pathlib import Path

CSV_PATH = Path(__file__).parent / "Data" / "vehicles_us.csv"
car_data = pd.read_csv(CSV_PATH)
