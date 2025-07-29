import streamlit as st
from supabase import create_client, Client

# ⚠️ Reemplaza estas variables con los datos reales de tu proyecto Supabase
url = "https://unavjraqjvqbsorqtzhj.supabase.co"  # ← pega tu URL real aquí
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVuYXZqcmFxanZxYnNvcnF0emhqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTE3MjcxMTYsImV4cCI6MjA2NzMwMzExNn0.xnvR7-O-hNK2Jq671I1Yt9WVnBsrR8KY0FhLE3RJUv8"  # ← pega tu anon key real aquí

# Crear cliente Supabase
supabase: Client = create_client(url, key)

# UI de Streamlit
st.title("Formulario de registro")

nombre = st.text_input("Nombre")
edad = st.number_input("Edad", min_value=0, step=1)

# Botón para guardar en Supabase
if st.button("Guardar en Supabase"):
    if nombre:
        data = {"nombre": nombre, "edad": int(edad)}
        try:
            res = supabase.table("manfred").insert(data).execute()
            if res.data:
                st.success("✅ Datos guardados correctamente")
            else:
                st.error(f"❌ No se insertó ningún dato: {res}")
        except Exception as e:
            st.error(f"❌ Error de conexión al guardar en Supabase: {e}")
    else:
        st.warning("⚠️ Ingresa un nombre antes de guardar")

st.markdown("---")
st.subheader("📋 Registros guardados")

# Mostrar los datos guardados
try:
    res = supabase.table("manfred").select("*").execute()
    if res.data:
        for fila in res.data:
            st.write(f"🧾 {fila['nombre']} - {fila['edad']} años")
    else:
        st.info("No hay datos aún.")
except Exception as e:
    st.error(f"❌ Error al consultar los datos desde Supabase: {e}")
import pandas as pd

# Convertimos los datos a DataFrame
df = pd.DataFrame(res.data)

# Creamos CSV y habilitamos botón de descarga
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="⬇️ Descargar registros como CSV",
    data=csv,
    file_name="registros_manfred.csv",
    mime="text/csv"
)
