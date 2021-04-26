import cv2
import numpy as np


def nothing(x):
    pass
cap = cv2.VideoCapture("C:\\Users\\Richard\\Documents\\Videos\\flor.mp4")
cv2.namedWindow("BarraDeRangosHSV")
cv2.createTrackbar("Inf - H", "BarraDeRangosHSV", 0, 179, nothing)
cv2.createTrackbar("Inf - S", "BarraDeRangosHSV", 0, 255, nothing)
cv2.createTrackbar("Inf - V", "BarraDeRangosHSV", 0, 255, nothing)
cv2.createTrackbar("Sup - H", "BarraDeRangosHSV", 179, 179, nothing)
cv2.createTrackbar("Sup - S", "BarraDeRangosHSV", 255, 255, nothing)
cv2.createTrackbar("Sup - V", "BarraDeRangosHSV", 255, 255, nothing)


while (1):
    _, frame = cap.read()
    frame = cv2.resize(frame, (600, 400), interpolation=cv2.INTER_LINEAR)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    l_h = cv2.getTrackbarPos("Inf - H", "BarraDeRangosHSV")
    l_s = cv2.getTrackbarPos("Inf - S", "BarraDeRangosHSV")
    l_v = cv2.getTrackbarPos("Inf - V", "BarraDeRangosHSV")
    u_h = cv2.getTrackbarPos("Sup - H", "BarraDeRangosHSV")
    u_s = cv2.getTrackbarPos("Sup - S", "BarraDeRangosHSV")
    u_v = cv2.getTrackbarPos("Sup - V", "BarraDeRangosHSV")
    lower_blue = np.array([l_h, l_s, l_v])
    upper_blue = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    kernel = np.ones((15,15),np.float32)/225
    smoothed = cv2.filter2D(res,-1,kernel)
    #cv2.imshow('Original',frame)
    cv2.imshow("Salida",mask)
    #cv2.imshow('Averaging',smoothed)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()



