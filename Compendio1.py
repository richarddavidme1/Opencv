import cv2
import numpy as np

img=cv2.imread("D:\\Programacion\\Python\\Opencv\\Material\\1.png")
kernel=np.ones((7,7),np.uint8)

imgG=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgG,(7,7),0)
imgCanny=cv2.Canny(img,170,200)
imgDilatacion=cv2.dilate(imgCanny,kernel,iterations=1)#Grosos del contorno
imgErode=cv2.erode(imgDilatacion,kernel,iterations=1)#Contraccion del contorno
imgErode1=cv2.erode(imgCanny,kernel,iterations=1)#Contraccion del contorno


cv2.imshow("Gris",imgG)
cv2.imshow("Blur",imgBlur)
cv2.imshow("Canny",imgCanny)
cv2.imshow("Dilatacion",imgDilatacion)
cv2.imshow("Erosion del Canny",imgErode1)
cv2.imshow("Erosion",imgErode)

cv2.waitKey(0)
cv2.destroyAllWindows()