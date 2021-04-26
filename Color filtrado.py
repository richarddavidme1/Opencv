import cv2
import numpy as np

while (True):
 gris=cv2.imread("C:\\Users\\Richard\\Documents\\Opencv Versiones\\Vision\\Primer Parcial\\Trabajo en clase\\colores.jpg")
 Hsv = cv2.cvtColor(gris, cv2.COLOR_BGR2HSV)
 InferiorColor = np.array([30, 150, 50])
 SuperiorColor = np.array([255, 255, 180])
 mascara = cv2.inRange(Hsv, InferiorColor, SuperiorColor)
 res = cv2.bitwise_and(gris, gris, mask=mascara)

 cv2.imshow('VideoCamara', gris)
 cv2.imshow('MascaraFiltrado', mascara)
 cv2.imshow('Resultado', res)
 key = cv2.waitKey(1)
 if key == 27:
     break



gris.release()
cv2.destroyAllWindows()
