import cv2
import numpy as np
import math

#Cargar imagenes
img = cv2.imread("D:\\Programacion\\Python\\Opencv\\Bul.png")
img=cv2.resize(img,(200,200))

#Kernel creados
kernel1 = np.ones((3,3),np.float32)/9
kernel2 = np.ones((5,5),np.float32)/25

K1=np.array([
    [0,1,1,1,1,0,1],#1
    [0,1,1,1,0,0,1],#2
    [1,1,1,1,0,0,0],#3
    [0,0,0,0,1,1,1],#4
    [1,1,1,0,0,0,1],#5
    [1,0,1,0,1,0,1],#6
    [0,1,0,1,0,1,0] #7
   ])

K2=np.array([
    [0,0,0,0,0,0,0,0,0,0,1],#1
    [0,0,0,0,0,0,0,0,0,1,1],#2
    [0,0,0,0,0,0,0,0,1,1,1],#3
    [0,0,0,0,0,0,0,1,1,1,1],#4
    [0,0,0,0,0,0,1,1,1,1,1],#5
    [0,0,0,0,0,1,1,1,1,1,1],#6
    [0,0,0,0,1,1,1,1,1,1,1],#7
    [0,0,0,1,1,1,1,1,1,1,1],#8
    [0,0,1,1,1,1,1,1,1,1,1],#9
    [0,1,1,1,1,1,1,1,1,1,1],#10
    [1,1,1,1,1,1,1,1,1,1,1],#11
   ])

#suavizdos
averaging1= cv2.blur(img, (3, 3))
averaging2 = cv2.blur(img, (5, 5))
gaussian1 = cv2.GaussianBlur(img, (3, 3), 0)
gaussian2 = cv2.GaussianBlur(img, (5, 5), 0)
median1 = cv2.medianBlur(img, 3)
median2 = cv2.medianBlur(img, 5)
creado1 = cv2.filter2D(img,-1,kernel1)
creado2 = cv2.filter2D(img,-1,kernel2)
bilateral1 = cv2.bilateralFilter(img, 3, 150, 150)
bilateral2 = cv2.bilateralFilter(img, 5, 150, 150)
kernelpropio1=cv2.filter2D(img,-1,K1)
kernelpropio2=cv2.filter2D(img,-1,K2)

#comparando de 3x3
a=np.count_nonzero(creado1)
b=np.count_nonzero(averaging1)
c=np.count_nonzero(gaussian1)
d=np.count_nonzero(median1)
e=np.count_nonzero(bilateral1)


print("Valores de Suavizado de 3x3")
print("Kernel 3x3: "+str(a),
      "Blur: "+str(b),
      "Gaussiano: "+str(c),
      "Median: "+str(d),
      "Bilateral: "+str(e))

#comparando de 5x5
a2=np.count_nonzero(creado2)
b2=np.count_nonzero(averaging2)
c2=np.count_nonzero(gaussian2)
d2=np.count_nonzero(median2)
e2=np.count_nonzero(bilateral2)
print("Valores de Suavizado de 5x5")
print("Kernel 5x5: "+str(a2),
      "Blur: "+str(b2),
      "Gaussiano: "+str(c2),
      "Median: "+str(d2),
      "Bilateral: "+str(e2))

concat_horizontal = cv2.hconcat([img,creado1,averaging1,gaussian1,median1,bilateral1])
concat_horizontal1 = cv2.hconcat([img,creado2,averaging2,gaussian2,median2,bilateral2])
KernelPropio = cv2.hconcat([img,kernelpropio1,kernelpropio2])

cv2.imshow("Salida 3x3",concat_horizontal)
cv2.imshow("Salida 5x5",concat_horizontal1)
cv2.imshow("Salida De Kernel",KernelPropio)


cv2.waitKey(0)
cv2.destroyAllWindows()