import cv2
import numpy as np

img=np.zeros((480,640,3),np.uint8)#Crear una imagen

print(img.shape)
img[:]=(255,0,0)#Crea el color de la imagen
img[250:320,400:600]=(0,0,255)#(y,x)

#Lineas
cv2.line(img,(100,50),(500,400),(255,255,255),1)
cv2.line(img,(50,20),(120,120),(255,255,255),2)
cv2.line(img,(320,0),(320,480),(255,255,255),3)
cv2.line(img,(0,240),(640,240),(255,255,255),3)
#Rectangulo
cv2.rectangle(img,(450,50),(550,100),(0,250,255),6)
cv2.rectangle(img,(0,400),(100,480),(0,250,255),cv2.FILLED) #llenar el rectangulo
#Circulo
cv2.circle(img,(320,240),100,(255,0,255),2)
cv2.circle(img,(320,240),50,(255,0,255),cv2.FILLED)#llenar el circulo
#Texto
cv2.putText(img," OpenCV ",(100,150),cv2.FONT_ITALIC,3,(0,0,0),3)

cv2.imshow("Salida",img)
cv2.waitKey(0)