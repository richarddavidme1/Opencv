import cv2
import numpy as np

#cap = cv2.VideoCapture("C:\\Users\\Richard\\Documents\\Videos\\flor.mp4")
cap = cv2.VideoCapture("C:\\Users\\Richard\\Documents\\a.mp4")

while (1):

    _, frame = cap.read()
    frame=cv2.resize(frame,(600,600))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([102, 0, 0])
    upper_red = np.array([179, 255, 180])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    kernel = np.ones((15, 15), np.float32) / 225
    suavizado = cv2.filter2D(res, -1, kernel)
    blur=cv2.GaussianBlur(res,(15,15),0)
    MediaBlur=cv2.medianBlur(res,15)
    BilateralBlur=cv2.bilateralFilter(res,15,75,75)


    cv2.imshow('Original', frame)
    cv2.imshow('Suavizado', suavizado)
    cv2.imshow('Blur', blur)
    cv2.imshow('MedianaBlur', MediaBlur)
    cv2.imshow('BilateralBlur', BilateralBlur)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()

