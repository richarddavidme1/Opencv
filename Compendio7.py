import cv2
import numpy as np

def EncontrarContornos(img):
    contornos,jerarquia=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contornos:
        area=cv2.contourArea(cnt)
        print(area)
        if(area > 500):
            cv2.drawContours(copia,cnt,-1,(0,0,255),1)
            perimetro=cv2.arcLength(cnt,True)
            print(perimetro)
            #Cerrar contornos
            aproximar=cv2.approxPolyDP(cnt,0.02*perimetro,True)
            #Numero de lados (tipo de figuras)
            print(len(aproximar))
            #Creamos la figura geometrica
            ObjetoCreado=len(aproximar)
            x,y,w,h=cv2.boundingRect(aproximar)
            #Cuadros limitadore de la figura
            if ObjetoCreado ==3: objectType ="Triangulo"
            else:objectType="None"
            cv2.rectangle(copia,(x,y),(x+w,y+h),(250,0,0),3)
            cv2.putText(copia,objectType,(x+int(w/2)-10,y+int(h/2)-10),cv2.FONT_ITALIC,0.5,(0,0,0),1)

img=cv2.imread("D:\\Programacion\\Python\\Opencv\\Figu.png")
copia=img.copy()
print(img.shape)

img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img2=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
img3=cv2.GaussianBlur(img1,(5,5),1)
img4=cv2.Canny(img3,75,75)
EncontrarContornos(img4)

cv2.imshow("Original",img)
cv2.imshow("EscaladeGrises",img1)
cv2.imshow("HSV",img2)
cv2.imshow("Blur",img3)
cv2.imshow("Canny",img4)
cv2.imshow("Contornos",copia)

cv2.waitKey(0)