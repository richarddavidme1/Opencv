import numpy as np
import cv2

cap = cv2.VideoCapture(0)
Foco = cv2.VideoWriter_fourcc(*'XVID')
Salida = cv2.VideoWriter('VideoGrabacion.avi',Foco, 20.0, (640,480))

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    Salida.write(frame)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
Salida.release()
cv2.destroyAllWindows()