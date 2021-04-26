#Importacion de librerias
#Import of libraries
import cv2
import numpy as np

#Añadir direccion de la imagen importante ser las mismas dimensiones 
# Add image address important to be the same dimensions

img1=cv2.imread("D:\\Programacion\\Python\Opencv\\2.jpg")
img2=cv2.imread("D:\\Programacion\\Python\Opencv\\1.png")

#Sumar imagenes de forma ordenada
#Add images in an orderly way

sumar=cv2.add(img1,img2)
peso = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)


cv2.imshow("Sumar",sumar)
cv2.imshow("Ponderado",peso)
cv2.waitKey(0)
cv2.destroyAllWindows()
