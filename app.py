import streamlit as st
from supabase import create_client, Client

# 👇 Reemplazá esto con tus datos reales de Supabase
url = "https://TU_PROYECTO.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR..."  # tu anon key

supabase: Client = create_client(url, key)

st.title("Formulario de registro")

nombre = st.text_input("Nombre")
edad = st.number_input("Edad", min_value=0, step=1)

if st.button("Guardar en Supabase"):
    if nombre:
        data = {"nombre": nombre, "edad": int(edad)}
        res = supabase.table("manfred").insert(data).execute()
        if res.status_code == 201:
            st.success("✅ Datos guardados correctamente")
        else:
            st.error(f"❌ Error: {res}")
    else:
        st.warning("⚠️ Ingresa un nombre antes de guardar")

st.markdown("---")
st.subheader("📋 Registros guardados")

res = supabase.table("manfred").select("*").execute()
if res.data:
    for fila in res.data:
        st.write(f"🧾 {fila['nombre']} - {fila['edad']} años")
else:
    st.info("No hay datos aún.")
