import numpy
import cv2
import tkinter

tkinter.Tk()
def empty(a):
    pass
img1 = cv2.imread("D:\\Programacion\\Python\\Opencv\\FrutasColores.jpg")
img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

cv2.namedWindow("Umbralizacion")
cv2.resizeWindow("RangosUmbral",(400,320))
cv2.createTrackbar("Tipo","Umbralizacion",0,5,empty)
cv2.createTrackbar("Rango","Umbralizacion",1,255,empty)

while(True):
    Rango = cv2.getTrackbarPos("Rango", "Umbralizacion")
    Tipo = cv2.getTrackbarPos("Tipo", "Umbralizacion")
    if(Tipo ==   1):
     _, threshold_binary = cv2.threshold(img, Rango, 255, cv2.THRESH_BINARY)
     cv2.imshow("th binary", threshold_binary)
    elif(Tipo == 2):
     _, threshold_binary_inv = cv2.threshold(img, Rango, 255, cv2.THRESH_BINARY_INV)
     cv2.imshow("th binary inv", threshold_binary_inv)
    elif(Tipo == 3):
     _, threshold_trunc = cv2.threshold(img, Rango, 255, cv2.THRESH_TRUNC)
     cv2.imshow("th trunc", threshold_trunc)
    elif(Tipo == 4):
     _, threshold_to_zero = cv2.threshold(img, Rango, 255, cv2.THRESH_TOZERO)
     cv2.imshow("th to zero", threshold_to_zero)
    elif(Tipo == 5):
     _, threshold_to_zero_inv = cv2.threshold(img, Rango, 255, cv2.THRESH_TOZERO_INV)
     cv2.imshow("th to zero inv", threshold_to_zero_inv)

    cv2.imshow("Original", img1)


    key = cv2.waitKey(100)
    if key == 27:
         break
cv2.destroyAllWindows()