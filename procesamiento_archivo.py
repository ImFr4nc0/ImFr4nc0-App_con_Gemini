import streamlit as st
import pandas as pd
import re
import openpyxl
import requests

def extraer_datos(url):
    """
    Extrae datos de un archivo CSV alojado en GitHub y los exporta a un archivo Excel.

    Args:
        url (str): La URL del archivo CSV en GitHub.
    """

    # Descargar el archivo CSV
    response = requests.get(url)
    open('temp.csv', 'wb').write(response.content)

    # Leer el archivo CSV (ajusta el separador y el encabezado si es necesario)
    df = pd.read_csv('temp.csv', sep=',', header=None)

    # Definir las expresiones regulares (ajusta según tu formato de CSV)
    pattern_producto = r"(\d+)\s+(\w+)\s+(\$\d+\.\d+)\s+(\d{2}/\d{2}/\d{2})"
    pattern_cliente = r"(\w+\s+\w+)\s+(\S+@\S+)\s+(\+\d{12})"

    # Crear listas para almacenar los datos extraídos
    productos = []
    clientes = []

    # Iterar sobre cada fila del DataFrame
    for index, row in df.iterrows():
        # Extraer información del producto
        match_producto = re.search(pattern_producto, str(row[0]))
        if match_producto:
            producto = {
                'Número de serie': match_producto.group(1),
                'Nombre': match_producto.group(2),
                'Valor': match_producto.group(3),
                'Fecha': match_producto.group(4)
            }
            productos.append(producto)

        # Extraer información del cliente
        match_cliente = re.search(pattern_cliente, str(row[0]))
        if match_cliente:
            cliente = {
                'Nombre': match_cliente.group(1),
                'Email': match_cliente.group(2),
                'Teléfono': match_cliente.group(3)
            }
            clientes.append(cliente)

    # Crear un nuevo DataFrame a partir de las listas
    df_nuevo = pd.DataFrame(columns=['Número de serie', 'Nombre del producto', 'Valor', 'Fecha de compra', 'Nombre del cliente', 'Email', 'Teléfono'])

    # Combinar la información de productos y clientes (aquí se asume una relación 1:1, ajustar si es necesario)
    for i in range(len(productos)):
        df_nuevo = df_nuevo.append(productos[i] | clientes[i], ignore_index=True)

    # Guardar el DataFrame como un archivo Excel
    df_nuevo.to_excel('resultado.xlsx', index=False)

# Interfaz de Streamlit
st.title("Extractor de Datos de CSV")

url = st.text_input("Ingrese la URL del archivo CSV en GitHub")

if st.button("Extraer"):
    if url:
        try:
            extraer_datos(url)
            st.success("Datos extraídos y exportados a Excel")
        except Exception as e:
            st.error(f"Error al procesar el archivo: {e}")
    else:
        st.warning("Ingrese una URL válida")
