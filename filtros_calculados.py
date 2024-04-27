import streamlit as st
import cv2
import numpy as np
from PIL import Image


##FILTROS CON CV2
def aplicar_filtro(imagen, filtro):
    image = np.array(imagen)  # converion de la imagen PIL a array de opencv
    if filtro == 'Filtro de la mediana':
        imagen_con_filtro = cv2.medianBlur(image, 5)
    elif filtro == 'Filtro de la media':
        imagen_con_filtro = cv2.blur(image, (5, 5))
    elif filtro == 'Filtro laplaciano':
        laplaciano = cv2.Laplacian(image, cv2.CV_64F)
        imagen_con_filtro = cv2.convertScaleAbs(laplaciano)
    elif filtro == 'Filtro de Sobel':
        sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
        sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
        imagen_con_filtro = cv2.convertScaleAbs(cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0))
    else:
        st.error("Selecciona un filtro válido.")
        return None

    return Image.fromarray(imagen_con_filtro) #convertir de nuevo a imagen PIL para mostrar en streamlit


##FILTROS CALCULADOS
def aplicar_filtro_mediana(imagen, ancho, alto):
    imagen_np = np.array(imagen)  # convertir la imagen a un array de numpy
    imagen_mediana = np.zeros_like(imagen_np)  # crear un array vacio para la nueva imagen

    for y in range(alto):
        for x in range(ancho):
            vecinos = []
            #Ahora se calculara los pixeles vecinos del pixel_central
            #Por tanto, recorrera los vecinos en una ventana 3x3  => por tanto tambien el pixel central
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < ancho and 0 <= ny < alto:#para asegurar que el vecino este dentro de los limites de la imagen
                        vecinos.append(imagen_np[ny, nx]) 
            
            #Aplicar el filtro de la mediana al pixel
            vecinos.sort()
            mid = len(vecinos) // 2
            if len(vecinos) % 2 == 0:
                nuevo_pixel = (vecinos[mid-1] + vecinos[mid]) // 2
            else:
                nuevo_pixel = vecinos[mid]
            imagen_mediana[y, x] = nuevo_pixel

    # Convertir el array de numpy de nuevo a una imagen de PIL para mostrar en streamlit
    return Image.fromarray(imagen_mediana.astype('uint8'))

def aplicar_filtro_media(imagen, ancho, alto, mascara):
    imagen_np = np.array(imagen)  
    imagen_media = np.zeros_like(imagen_np)  # crear un array vacio para la nueva imagen

    # Definición de máscaras como matrices 3x3
    mascara1 = np.array([1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9]).reshape(3, 3)
    mascara2 = np.array([1/16, 2/16, 1/16, 2/16, 4/16, 2/16, 1/16, 2/16, 1/16]).reshape(3, 3)

    if mascara == 1:
        mascara = mascara1
    elif mascara == 2:
        mascara = mascara2

    for y in range(alto):
        for x in range(ancho):
            suma = 0  
            #Ahora se calculara los pixeles vecinos del pixel_central
            #Por tanto, recorrera los vecinos en una ventana 3x3
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < ancho and 0 <= ny < alto:
                        valor_pixel = imagen_np[ny, nx]
                    else:
                        valor_pixel = 0  #para que si se salen de los borden cuenten como cero
                    #print(f"{valor_pixel} x {mascara[dy + 1, dx + 1]} = {valor_pixel*mascara[dy + 1, dx + 1]}")
                    suma += valor_pixel * mascara[dy + 1, dx + 1]
                #print(suma)

            # Asignar el nuevo valor al pixel
            imagen_media[y, x] = int(np.floor(suma + 0.5))  #no funciono np.round() porque redondea al mas cercano => 2.5 = 2 
            #print(imagen_media[y, x])
            

    # Convertir el array de numpy de nuevo a una imagen de PIL para mostrar en streamlit
    return Image.fromarray(imagen_media.astype('uint8'))