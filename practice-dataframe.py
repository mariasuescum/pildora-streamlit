import streamlit as st
import pandas as pd

# Crear un DataFrame de Pandas
df = pd.DataFrame({
    "Nombre": ["Ana", "Luis", "Carlos"],
    "Edad": [25, 30, 28],
    "Ciudad": ["Madrid", "Barcelona", "Sevilla"]
})

# Mostrar la tabla en Streamlit
st.dataframe(df)

st.dataframe(df, width=500, height=300)
