import streamlit as st
import pandas as pd
import re
import xlsxwriter
from io import BytesIO

# Función para procesar el archivo y generar el Excel
def process_file(uploaded_file):
    # Leer el archivo subido como texto plano
    raw_data = pd.read_csv(uploaded_file, header=None, encoding='utf-8')
    raw_text = raw_data.to_string(index=False, header=False)
    
    # Patrones regex para extraer información
    serial_pattern = r'\b\d{6,}\b'
    product_pattern = r'\b(Tv|Tablet|Radio|Modem|Celular)\b'
    value_pattern = r'\$\d+\.\d{2}'
    date_pattern = r'\b\d{2}/\d{2}/\d{2}\b'
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    phone_pattern = r'\+?\d{2,3} \d{6,10}'
    name_pattern = r'[A-Z][a-z]+(?: [A-Z][a-z]+)*'
    
    # Extraer datos usando regex
    serials = re.findall(serial_pattern, raw_text)
    products = re.findall(product_pattern, raw_text)
    values = re.findall(value_pattern, raw_text)
    dates = re.findall(date_pattern, raw_text)
    emails = re.findall(email_pattern, raw_text)
    phones = re.findall(phone_pattern, raw_text)
    names = re.findall(name_pattern, raw_text)
    
    # Emparejar los datos extraídos
    rows = zip(serials, products, values, dates, names, emails, phones)
    
    # Crear el archivo Excel en memoria
    output = BytesIO()
    workbook = xlsxwriter.Workbook(output, {'in_memory': True})
    worksheet = workbook.add_worksheet()

    # Escribir encabezados
    headers = ["Número de Serie", "Nombre del Producto", "Valor", "Fecha de Compra", "Nombre Cliente", "Correo Electrónico", "Teléfono"]
    for col, header in enumerate(headers):
        worksheet.write(0, col, header)

    # Escribir datos
    for row_idx, row_data in enumerate(rows, start=1):
        for col_idx, cell_data in enumerate(row_data):
            worksheet.write(row_idx, col_idx, cell_data)

    workbook.close()
    output.seek(0)  # Posicionar el cursor al inicio del archivo
    return output

# Configurar la app de Streamlit
st.title("Procesador de Archivos de Productos")
st.write("Sube un archivo CSV y obtén un archivo Excel con los datos estructurados.")

# Subir el archivo
uploaded_file = st.file_uploader("Sube tu archivo CSV", type=["csv"])

if uploaded_file is not None:
    # Procesar el archivo subido
    excel_file = process_file(uploaded_file)

    # Descargar el archivo procesado
    st.download_button(
        label="Descargar archivo procesado",
        data=excel_file,
        file_name="productos_procesados.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
