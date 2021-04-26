import cv2
import numpy as np

img1=cv2.imread("D:\\Programacion\\Python\\Opencv\\Material\\1.png")
img=cv2.imread("D:\\Programacion\\Python\\Opencv\\Material\\1.png",cv2.IMREAD_GRAYSCALE)
retval,umbral=cv2.threshold(img,100,255,cv2.THRESH_BINARY)

cv2.imshow("Imagen Normal",img1)
cv2.imshow("Imagen Gris",img)
cv2.imshow("Imagen Filtrada",umbral)
cv2.waitKey()
cv2.destroyAllWindows()