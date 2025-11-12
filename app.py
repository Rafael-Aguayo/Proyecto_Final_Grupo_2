import streamlit as st
import pandas as pd
import joblib

# Cargar modelo y columnas
model = joblib.load("modelo_rotacion.pkl")
columns = joblib.load("columnas_modelo.pkl")

st.title("Clasificador de Rotación de Productos")

# Inputs del usuario
sales_dollars = st.number_input("Ventas en pesos")
purchase_price = st.number_input("Precio de compra")
volume = st.selectbox("Formato", ['375', '750', '1000'])
month = st.selectbox("Mes", list(range(1,13)))
store = st.selectbox("Tienda", ['Tienda 1', 'Tienda 2', 'Tienda 3'])

# Preparar datos
input_df = pd.DataFrame({
    'SalesDollars': [sales_dollars],
    'PurchasePrice': [purchase_price],
    'Volume': [volume],
    'Month': [month],
    'Store': [store]
})

# Codificar igual que en entrenamiento
input_encoded = pd.get_dummies(input_df).reindex(columns=columns, fill_value=0)

# Predicción
pred = model.predict(input_encoded)
st.write(f"Categoría de rotación estimada: {le.inverse_transform(pred)[0]}")