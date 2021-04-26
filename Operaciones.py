import cv2
import numpy as np

img=cv2.imread('C:\\Users\\Richard\\Documents\\98F.jpg')


#Cambio de color del pixel

img[150,150]=[255,255,255]
img[100: 150, 100: 150]=[123,100,150]

#Posicion del pixel especifico

px=img[150,150]
px1 = img[100: 150, 100: 150]


#Imprimir pixeles

print(px)
print(px1)

#Mover el ROI
Sapo = img[37:111,107:194]
img[0:74,0:87] = Sapo

#Imprimir caracteristicas

print(img.shape) #Dimensiones
print(img.size) #Tamaño
print(img.dtype) #Codificacion

cv2.imshow("Operaciones",img)
cv2.waitKey(0)
cv2.destroyAllWindows()