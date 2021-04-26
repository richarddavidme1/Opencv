import cv2
import numpy as np

img=cv2.imread("D:\\Programacion\\Python\\Opencv\\Bul.png")
C1 = img[:,:,0]
C2 = img[:,:,1]
C3 = img[:,:,2]
cv2.imshow('BGR',np.hstack([C1,C2,C3]))
#Matriz de 300x300,3 columbas
brg=np.zeros((300,300,3),dtype=np.uint8)
brg[ : ,: ,:]=[255,0,0]
cv2.imshow("Azul",brg)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()