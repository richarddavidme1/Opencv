import numpy as np
import cv2

img = cv2.imread('C:\\Users\\Richard\\Documents\\esquinas.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 20)
corners = np.int0(corners)
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 3, 255, -1)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'MODO SABIO !!!', (0, 130), font,3, (200, 255, 155), 5, cv2.LINE_AA)
cv2.imshow('Corner', img)
cv2.waitKey(0)
cv2.destroyAllWindows()