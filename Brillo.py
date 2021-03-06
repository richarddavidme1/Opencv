import cv2
import numpy as np

image1= cv2.imread("C:\\Users\\richa\\Documents\\Android Recursos\\foco.jpg")
image = cv2.cvtColor(image1, cv2.COLOR_BGR2HSV)

increase = 50
v = image[:, :, 2]
v = np.where(v <= 255 - increase, v + increase, 255)
image[:, :, 2] = v

image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)

cv2.imshow("Sin Brillo",image1)
cv2.imshow('Brillo', image)
cv2.waitKey(0)
cv2.destroyAllWindows()