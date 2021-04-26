import cv2
import numpy as np

camara=cv2.VideoCapture(0)

while(True):
    _,cuadros=camara.read()
    Hsv=cv2.cvtColor(cuadros,cv2.COLOR_BGR2HSV)
    InferiorColor=np.array([175, 100, 20])
    SuperiorColor=np.array([179, 255, 255])
    mascara=cv2.inRange(Hsv,InferiorColor,SuperiorColor)
    res = cv2.bitwise_and(cuadros, cuadros, mask=mascara)


    cv2.imshow('VideoCamara',cuadros)
    cv2.imshow('MascaraFiltrado',mascara)
    cv2.imshow('Resultado',res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cuadros.release()
cv2.destroyAllWindows()
