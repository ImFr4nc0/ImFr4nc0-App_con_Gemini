import streamlit as st
import re

# Títulos de la app
st.title("Validador de Textos Comunes")

# Subtítulo indicando el autor
st.subheader("Desarrollado por Alejandro Gómez Franco")

st.write("Ingresa un texto y selecciona el tipo de validación que deseas realizar.")

# Entrada de texto
text = st.text_input("Ingresa tu texto aquí:")

# Opciones de validación
validation_type = st.selectbox(
    "Selecciona el tipo de validación:",
    ["Correo electrónico", "Número de teléfono", "URL"]
)

# Función para validar con regex
def validate_input(text, validation_type):
    patterns = {
        "Correo electrónico": r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.\w{2,}",
        "Número de teléfono": r"^\d{3}[\s-]?\d{3}[\s-]?\d{4}",
        "URL": r"^https?:\/\/\S+"
    }
    pattern = patterns.get(validation_type, "")
    if re.match(pattern, text):
        return True
    return False

# Botón de validación
if st.button("Validar"):
    if text.strip():  # Verifica que no esté vacío
        is_valid = validate_input(text, validation_type)
        if is_valid:
            st.success(f"El texto ingresado es un {validation_type.lower()} válido.")
        else:
            st.error(f"El texto ingresado NO es un {validation_type.lower()} válido.")
    else:
        st.warning("Por favor, ingresa un texto antes de validar.")

# Nota de pie
st.write("---")
st.caption("Esta app fue creada con Python y Streamlit para validar expresiones regulares.")
