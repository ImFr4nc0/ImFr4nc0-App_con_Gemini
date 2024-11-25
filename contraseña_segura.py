import streamlit as st
import re

def evaluar_contrasena(contrasena):
    """Evalúa la fortaleza de una contraseña y devuelve un mensaje.

    Args:
        contrasena (str): La contraseña a evaluar.

    Returns:
        str: Un mensaje indicando si la contraseña es segura y sugerencias para mejorarla.
    """

    # Patrones para buscar en la contraseña
    patron_mayusculas = r"[A-Z]"
    patron_minusculas = r"[a-z]"
    patron_numeros = r"\d"
    patron_especiales = r"[^\w\s]"

    # Condiciones para una contraseña segura
    longitud_suficiente = len(contrasena) >= 8
    tiene_mayusculas = re.search(patron_mayusculas, contrasena)
    tiene_minusculas = re.search(patron_minusculas, contrasena)
    tiene_numeros = re.search(patron_numeros, contrasena)
    tiene_especiales = re.search(patron_especiales, contrasena)

    if all([longitud_suficiente, tiene_mayusculas, tiene_minusculas, tiene_numeros, tiene_especiales]):
        return "Excelente! Tu contraseña es muy segura."
    else:
        sugerencias = []
        if not longitud_suficiente:
            sugerencias.append("La contraseña debe tener al menos 8 caracteres.")
        if not tiene_mayusculas:
            sugerencias.append("Incluye al menos una letra mayúscula.")
        if not tiene_minusculas:
            sugerencias.append("Incluye al menos una letra minúscula.")
        if not tiene_numeros:
            sugerencias.append("Incluye al menos un número.")
        if not tiene_especiales:
            sugerencias.append("Incluye al menos un carácter especial (!, $, #, etc.).")
        return "Tu contraseña podría ser más segura. Sugerencias: " + ", ".join(sugerencias)

# Título de la aplicación
st.title("Evaluador de Contraseñas")

# Subtítulo indicando el autor
st.subheader("Desarrollado por Alejandro Gómez Franco")

# Campo de entrada para la contraseña
contrasena = st.text_input("Ingrese su contraseña")

# Botón para evaluar la contraseña
if st.button("Evaluar"):
    resultado = evaluar_contrasena(contrasena)
    st.write(resultado)
