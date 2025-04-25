import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://wallpapers.com/images/hd/black-carbon-fiber-1biekffyzs37csto.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título en rojo
st.markdown("<h1 style='color: red;'>Reconocimiento óptico de Caracteres</h1>", unsafe_allow_html=True)

# Subheader de la cámara en azul
st.markdown("<h3 style='color: blue;'>Toma una Foto</h3>", unsafe_allow_html=True)
img_file_buffer = st.camera_input("")

# Sidebar con header en azul
with st.sidebar:
    st.markdown("<h3 style='color: blue;'>Opciones</h3>", unsafe_allow_html=True)
    filtro = st.radio("Aplicar Filtro", ('Con Filtro', 'Sin Filtro'))

if img_file_buffer is not None:
    # Leer imagen del buffer
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    if filtro == 'Con Filtro':
        cv2_img = cv2.bitwise_not(cv2_img)

    img_rgb = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    text = pytesseract.image_to_string(img_rgb)

    # Mostrar resultado
    st.markdown("<h3 style='color: blue;'>Texto Detectado</h3>", unsafe_allow_html=True)
    st.write(text)
