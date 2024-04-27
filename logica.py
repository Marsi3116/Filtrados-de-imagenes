import numpy as np


imagen_np = np.array([3, 3, 6, 3, 3, 1, 6, 5, 5])
imagen_np = imagen_np.reshape(3, 3) 


imagen_media = np.zeros_like(imagen_np)


mascara = np.array([1/16, 2/16, 1/16, 2/16, 4/16, 2/16, 1/16, 2/16, 1/16])
num= 1/16
mascara = mascara.reshape(3, 3)  

alto, ancho = 3, 3  


for y in range(alto):
    for x in range(ancho):
        suma = 0  
        vecinos = []
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                nx, ny = x + dx, y + dy
                if 0 <= nx < ancho and 0 <= ny < alto:
                    valor_pixel = imagen_np[ny, nx]
                else:
                    valor_pixel = 0  #para que si se salen de los borden cuenten como cero
                #print(f"{valor_pixel} x {mascara[dy + 1, dx + 1]} = {valor_pixel*mascara[dy + 1, dx + 1]}")
                suma += valor_pixel * mascara[dy + 1, dx + 1]
            print(suma)
            
    
        imagen_media[y, x] = int(np.floor(suma + 0.5))  #no funciono np.round() porque redondea al mas cercano => 2.5 = 2 
        print(imagen_media[y, x])

print(imagen_media)
