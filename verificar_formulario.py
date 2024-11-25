import streamlit as st
import re

def validar_nombre(nombre):
    patron = r"^[A-Z][a-zA-Z]*$"
    return re.match(patron, nombre)

def validar_email(email):
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(patron, email)

def validar_telefono(telefono):
    # Ajusta el patrón según el formato de teléfono que desees validar
    patron = r"^\d{10}$"  # Ejemplo: 10 dígitos
    return re.match(patron, telefono)

def validar_fecha(fecha):
    # Ajusta el patrón según el formato de fecha que desees validar
    patron = r"^\d{4}-\d{2}-\d{2}$"  # Ejemplo: YYYY-MM-DD
    return re.match(patron, fecha)

# Título de la aplicación
st.title("Validador de Formularios Web")

# Subtítulo indicando el autor
st.subheader("Desarrollado por Alejandro Gómez Franco")

# Campos de entrada para los datos
nombre = st.text_input("Ingrese su nombre")
email = st.text_input("Ingrese su correo electrónico")
telefono = st.text_input("Ingrese su número de teléfono")
fecha = st.text_input("Ingrese una fecha (AAAA-MM-DD)")

# Botón para validar los datos
if st.button("Validar"):
    if validar_nombre(nombre):
        st.success("Nombre válido.")
    else:
        st.error("Nombre inválido. Debe comenzar con mayúscula y solo contener letras.")

    if validar_email(email):
        st.success("Correo electrónico válido.")
    else:
        st.error("Correo electrónico inválido.")

    if validar_telefono(telefono):
        st.success("Número de teléfono válido.")
    else:
        st.error("Número de teléfono inválido.")

    if validar_fecha(fecha):
        st.success("Fecha válida.")
    else:
        st.error("Fecha inválida. Utilice el formato AAAA-MM-DD.")
