import cv2 as cv
import sys


img = cv.imread("D:\\Programacion\\Python\\Opencv\\1.png")
if img is None:
    sys.exit("No hay imagen cargada.")
cv.imshow("Ventana de Salida", img)
k = cv.waitKey(0)
if k == ord("s"):
    #Guarda la imagen con este nombre al presionar ss
    cv.imwrite("SalidaNombre.png", img)