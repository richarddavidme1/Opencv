import numpy as np
import cv2
import turtle

cap = cv2.VideoCapture(0)


while (True):
    ret, frame1 = cap.read()
    frame = cv2.flip(frame1,1)
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Pantalla Gris', gray)
    cv2.imshow("Pantalla Origianl",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()