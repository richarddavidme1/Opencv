import numpy as np
import cv2

#captura de video 0 para la camara predeterminada
cap = cv2.VideoCapture(0)


while (True):
    
    #Lectrua de fotogramas
    ret, frame1 = cap.read()
    #Salida espejo
    frame = cv2.flip(frame1,1)
    #Transformacion a escala de grises
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    #Salida de consola
    cv2.imshow('Pantalla Gris', gray)
    cv2.imshow("Pantalla Origianl",frame)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
