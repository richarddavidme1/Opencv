import cv2
import numpy as np

gris=cv2.imread('C:\\Users\\Richard\\Documents\\pagina.jpg',cv2.IMREAD_GRAYSCALE)

umbraladap=cv2.adaptiveThreshold(gris,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
mean_c = cv2.adaptiveThreshold(gris, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 12)

cv2.imshow("Imagen Normal",gris)
cv2.imshow("Imagen Filtrada Mean",mean_c)
cv2.imshow("Imagen Filtrada Gauus",umbraladap)

cv2.waitKey()
cv2.destroyAllWindows()