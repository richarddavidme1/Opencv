import cv2
import numpy as np

img= cv2.imread("D:\\Programacion\\Python\\Opencv\\FrutasColores.jpg")
print(img.shape)

#Sacar la region de interes
roi=img[43:309,98:419]
#tranformacion HSV
imgHSV=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
#rangos de colores HSV
Inf = np.array([78, 22, 50])  # minumos
Sup = np.array([151, 183,217])  # maximos
#Mascara de rangos
mask=cv2.inRange(imgHSV,Inf,Sup)
imgMask=cv2.bitwise_and(roi,roi,mask=mask)
retval,umbral=cv2.threshold(mask,150,255,cv2.THRESH_BINARY)
mask1=cv2.cvtColor(umbral,cv2.COLOR_GRAY2BGR)
u2=cv2.addWeighted(mask1,1,roi,1,1)
img[43:309,98:419]=u2

cv2.imshow("ImagenOriginal",img)
cv2.imshow("ROI",roi)
cv2.imshow("HSV",imgHSV)
cv2.imshow("Mascara",mask)
cv2.imshow("Corte",imgMask)
cv2.imshow("Umbral",umbral)
cv2.imshow("UmbralBGR",mask1)
cv2.imshow("UmbralBGR1",u2)

cv2.waitKey(0)