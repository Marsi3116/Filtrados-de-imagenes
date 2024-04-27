import streamlit as st
import cv2
import numpy as np
from PIL import Image

from paginas import pagina_aplicar_filtros, pagina_aplicar_filtros_con_calculo, pagina_sobre_el_programa

def main():
    
    st.title("Aplicación para Filtros de Imágenes")

    tab1, tab2, tab3 = st.tabs(["Sobre el Programa", "Aplicar Filtros (Libreria cv2)", "Aplicar Filtros (con cálculo)"])  #creacion de nuevas pestañas

    with tab1:
        pagina_sobre_el_programa()

    with tab2:
        pagina_aplicar_filtros()
    
    with tab3:
        pagina_aplicar_filtros_con_calculo()


if __name__ == "__main__":
    main()



