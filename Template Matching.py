import cv2
import numpy as np

img_rgb = cv2.imread('C:\\Users\\Richard\\Documents\\compu.jpg')
#C:\\Users\\Richard\\Documents\\98F.jpg
#C:\\Users\\Richard\\Documents\\compu.jpg
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('C:\\Users\\Richard\\Documents\\refe.jpg',0)
w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.756
loc = np.where(res >= threshold)
i=0

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img_rgb, "OK", (pt[0] + w, pt[1] + h), font, 0.5, (200, 255, 155), 2, cv2.LINE_AA)


cv2.imshow('Detector',img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()