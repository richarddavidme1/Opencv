import cv2

img=cv2.imread("D:\\Programacion\\Python\\Opencv\\evil.jpg")
print("Dimensiones de la imagen original"+str(img.shape))#Conocer las dimensiones de la imagen

Dimesionar=cv2.resize(img,(640,480))
Recortar=img[0:400,0:600]
print("Recorte de la imagen"+str(Recortar.shape))
cv2.imshow("Salida",img)
cv2.imshow("Dimensionar",Dimesionar)
cv2.imshow("Recorte",Recortar)

cv2.waitKey(0)