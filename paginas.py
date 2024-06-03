import streamlit as st
import cv2
import numpy as np
from PIL import Image

from filtros_calculados import aplicar_filtro, aplicar_filtro_media, aplicar_filtro_mediana, aplicar_filtro_laplaciano, aplicar_filtro_sobel

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
             En el procesamiento de imágenes digitales, **la aplicación de filtros** es una técnica esencial para la 
             **modificación y mejora de las imágenes**. Los filtros ayudan a destacar ciertas características, reducir ruido, 
             o preparar imágenes para análisis posteriores. En este proyecto, se aplican cuatro tipos de filtros:

             - **Filtro de la Mediana**: Utilizado para reducir el ruido de tipo "sal y pimienta". Este filtro sustituye cada píxel por la mediana de los píxeles en su vecindad.
             - **Filtro de la Media**: Suaviza la imagen reemplazando cada píxel por el promedio de los píxeles de su entorno, reduciendo el ruido.
             - **Filtro Laplaciano**: Detecta bordes en las imágenes y realza regiones de cambio rápido de intensidad, usado comúnmente para afilar imágenes.
             - **Filtro de Sobel**: Destaca los bordes verticales y horizontales mediante el uso de dos matrices de convolución, una para cada dirección.

             Estos filtros se aplicaron de diferentes maneras: 
             - Con la librería `cv2`
             - Con cálculos matemáticos

        """)
    st.code("""
    Integrantes:
    - Marsi Valeria Figueroa Larragán (U202220990)
    - Rafael Tomas Chui Sanchez (U201925837)
    - Davis Jefferson Rojas Torres (U202120763)
    """, language='text')


def pagina_aplicar_filtros_con_calculo():
    archivo_cargado = st.file_uploader("Carga una imagen", type=["jpg", "png", "jpeg"], key="uploader2")
    if archivo_cargado is not None:
        imagen = Image.open(archivo_cargado).convert("RGB")     #.convert("L") => para escalas de grises  , .convert("RGB") => a colores
        st.image(imagen, caption='Imagen Original', use_column_width=True)

        ancho, alto = imagen.size
        filtro = st.selectbox("Selecciona un tipo de filtro", ["Seleccionar filtro", "Filtro de la mediana", "Filtro de la media", "Filtro de Laplaciano", "Filtro de Sobel"])
        
        if filtro == "Filtro de la mediana":
            imagen_filtrada = aplicar_filtro_mediana(imagen, ancho, alto)
            st.image(imagen_filtrada, caption='Imagen con Filtro de Mediana', use_column_width=True)
        
        elif filtro == "Filtro de la media":
            mask_image_path = "mascaras.png"  
            st.image(mask_image_path, caption='Máscaras Disponibles', use_column_width=True)

            mascara = st.selectbox("Selecciona una máscara", [1, 2])
            imagen_filtrada = aplicar_filtro_media(imagen, ancho, alto, mascara)
            st.image(imagen_filtrada, caption='Imagen con Filtro de Media', use_column_width=True)

        elif filtro == "Filtro de Laplaciano":
            mask_image_path = "mascaras-lapla.png"  
            st.image(mask_image_path, caption='Máscaras Disponibles', use_column_width=True)

            mascara = st.selectbox("Selecciona una máscara", [1, 2, 3, 4])
            imagen_filtrada = aplicar_filtro_laplaciano(imagen, ancho, alto, mascara)
            st.image(imagen_filtrada, caption='Imagen con Filtro de Laplaciano', use_column_width=True)
        
        elif filtro == "Filtro de Sobel":
            mask_image_path = "sobel.png"
            st.image(mask_image_path, caption='Máscaras de Sobel', use_column_width=True)
            imagen_filtrada = aplicar_filtro_sobel(imagen, ancho, alto)
            st.image(imagen_filtrada, caption='Imagen con Filtro de Sobel', use_column_width=True)
