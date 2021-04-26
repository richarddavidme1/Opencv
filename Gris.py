import cv2

img=cv2.imread("C:\\Users\\richa\\Documents\\Android Recursos\\iconorick.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imshow("hola",img)

#esperar a que presione una tecla
cv2.waitKey(0)