import cv2
import numpy as np
img=cv2.imread("D:\\Programacion\\Python\\Opencv\\Naipes.jpg")
print(img.shape)

w,h=[250,350] #Ancho y Alto

puntos=np.float32([[455,100],[600,160],[355,280],[528,376]]) #puntos de recorte de la imagen
puntos1=np.float32([[0,0],[w,0],[0,h],[w,h]])
matriz=cv2.getPerspectiveTransform(puntos,puntos1)
imagensalida=cv2.warpPerspective(img,matriz,(w,h))

cv2.imshow("Salida",img)
cv2.imshow("Perspectiva",imagensalida)
cv2.waitKey(0)