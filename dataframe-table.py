import streamlit as st
import pandas as pd

# Crear un DataFrame inicial
df = pd.DataFrame({
    "Nombre": ["Ana", "Luis", "Carlos"],
    "Edad": [25, 30, 28],
    "Ciudad": ["Madrid", "Barcelona", "Sevilla"]
})


# Mostrar la tabla editable en Streamlit
df_editado = st.data_editor(df, num_rows="dynamic")

# Convertir el DataFrame editado a CSV
csv = df_editado.to_csv(index=False).encode("utf-8")

# Crear un botón para descargar los datos editados
st.download_button(
    label="📥 Descargar datos editados",
    data=csv,
    file_name="datos_editados.csv",
    mime="text/csv"
)

# Mostrar los datos actualizados
st.write("### Datos actualizados:")
st.dataframe(df_editado)