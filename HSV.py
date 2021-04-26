import cv2

image = cv2.imread("D:\\Programacion\\Python\\Opencv\\Bul.png")

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv_image)
s.fill(255)
v.fill(255)
hsv_image = cv2.merge([h, s, v])

out = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

cv2.imshow('example', out)
cv2.waitKey()