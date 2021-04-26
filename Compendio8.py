import cv2
import numpy as np

Casada=cv2.CascadeClassifier("D:\\Programacion\\Python\\Opencv\\data\\haarcascade_frontalface_default.xml")


cap=cv2.imread("D:\\Programacion\\Python\\Opencv\\Caras.jpg")
cap=cv2.resize(cap,(800,600),interpolation=cv2.INTER_AREA)
capg=cv2.cvtColor(cap,cv2.COLOR_BGR2GRAY)

faces=Casada.detectMultiScale(capg,1.3,5)

for (x,y,w,h) in faces:
    cv2.rectangle(cap,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("DetectarCara",cap)
cv2.imshow("DetectarCaraGris",capg)
cv2.waitKey(0)