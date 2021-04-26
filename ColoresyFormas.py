import cv2
import numpy as np


def dibujarContorno(contornos, color):
  for (i, c) in enumerate(contornos):
    M = cv2.moments(c)
    area = cv2.contourArea(c)
    if (M["m00"]==0): M["m00"]==1
    x = int((M["m10"]+0.001)/(M["m00"]+0.001))
    y = int((M["m01"]+0.001)/(M["m00"]+0.001))
    if area > 100:
      cv2.drawContours(imagen, [c], 0, color, 2)
      perimetro = cv2.arcLength(c, True)
      aproximar = cv2.approxPolyDP(c, 0.04 * perimetro, True)
      ObjetoCreado = len(aproximar)




#primer color
verdeBajo = np.array([63, 77, 51], np.uint8)
verdeAlto = np.array([91, 255, 221], np.uint8)
#Segundo color
blancoBajo = np.array([21, 158, 69], np.uint8)
blacoAlto = np.array([44, 255, 248], np.uint8)
#tercercolor
moradoBajo = np.array([124, 116, 69], np.uint8)
moradoAlto = np.array([159, 218, 219], np.uint8)

imagen = cv2.imread("D:\\Programacion\\Python\\Opencv\Material\\pelotas.jpg")
imagen=cv2.resize(imagen,(800,600))
imagenHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

#Detectando colores
maskverde = cv2.inRange(imagenHSV, verdeBajo, verdeAlto)
contornosverde = cv2.findContours(maskverde, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
maskblanco = cv2.inRange(imagenHSV, blancoBajo, blacoAlto)
contornosblanco = cv2.findContours(maskblanco, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
maskmorado = cv2.inRange(imagenHSV, moradoBajo, moradoAlto)
contornosmorado= cv2.findContours(maskmorado, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

dibujarContorno(contornosverde, (0, 0,255))
dibujarContorno(contornosblanco, (0, 255,255))
dibujarContorno(contornosmorado, (255, 0,0))


totalverde =int(len(contornosverde)/1.6)
totalblanco =int(len(contornosblanco)/1.9)
totalmorado=int(len(contornosblanco))
print("Numero de color verde:" +str(totalverde))
print("Numero de color blanco:" +str(totalblanco))
print("Numero de color morado:" +str(totalblanco))
cv2.imshow('Imagen', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()