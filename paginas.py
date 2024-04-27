import streamlit as st
import cv2
import numpy as np
from PIL import Image

from filtros_calculados import aplicar_filtro, aplicar_filtro_media, aplicar_filtro_mediana

def pagina_aplicar_filtros():
    archivo_cargado = st.file_uploader("Carga una imagen", type=["jpg", "png", "jpeg"])
    if archivo_cargado is not None:
        imagen = Image.open(archivo_cargado).convert("RGB")
        st.image(imagen, caption='Imagen Original', use_column_width=True)
        filtro = st.selectbox("Selecciona un tipo de filtro", ["Filtro de la mediana", "Filtro de la media", "Filtro laplaciano", "Filtro de Sobel"])

        if st.button("Aplicar Filtro"):
            resultado_imagen = aplicar_filtro(imagen, filtro)
            if resultado_imagen is not None:
                st.image(resultado_imagen, caption=f'Imagen con filtro {filtro}', use_column_width=True)

def pagina_sobre_el_programa():
    st.header("Sobre este programa")
    st.write("""
            Este programa tiene el fin de aplicarle a diferentes imágenes los diferentes filtros de la mediana, la media, laplaciano 
                 y de Sobel. Esto con el fin de reducirle el ruido o hacerlo más nitido.
            
                 
                Integrantes:
                 -Marsi Valeria Figueroa Larragán (U202220990)
                 -Rafael Tomas Chui Sanchez (U201925837)
                 -Davis Jefferson Rojas Torres (U202120763)
        """)


def pagina_aplicar_filtros_con_calculo():
    archivo_cargado = st.file_uploader("Carga una imagen", type=["jpg", "png", "jpeg"], key="uploader2")
    if archivo_cargado is not None:
        imagen = Image.open(archivo_cargado).convert("L")
        st.image(imagen, caption='Imagen Original', use_column_width=True)

        ancho, alto = imagen.size
        filtro = st.selectbox("Selecciona un tipo de filtro", ["Seleccionar filtro", "Filtro de la mediana", "Filtro de la media"])
        
        if filtro == "Filtro de la mediana":
            imagen_filtrada = aplicar_filtro_mediana(imagen, ancho, alto)
            st.image(imagen_filtrada, caption='Imagen con Filtro de Mediana', use_column_width=True)
        
        elif filtro == "Filtro de la media":
            mask_image_path = "mascaras.png"  
            st.image(mask_image_path, caption='Máscaras Disponibles', use_column_width=True)

            mascara = st.selectbox("Selecciona una máscara", [1, 2])
            imagen_filtrada = aplicar_filtro_media(imagen, ancho, alto, mascara)
            st.image(imagen_filtrada, caption='Imagen con Filtro de Media', use_column_width=True)
