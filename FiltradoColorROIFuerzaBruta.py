import cv2
import numpy as np
from PIL import Image
import PIL.ImageOps
from PIL import Image
image = cv2.imread("D:\\Programacion\\Python\\Opencv\\FrutasPrueba.jpg")
image1 = cv2.imread("D:\\Programacion\\Python\\Opencv\\FrutasPrueba.jpg")
print(image1.size)
print(image1.shape)
image=cv2.resize(image,(550,434))
image1=cv2.resize(image1,(550,434))


roi1=image[141:203,146:285]
roi2=image[307:354,200:255]
roi3=image[137:199,365:418]
roi4=image[177:255,0:46]
roi5=image[318:428,0:73]

HSV = cv2.cvtColor(roi1,cv2.COLOR_BGR2HSV)#Conversión
HSV2 = cv2.cvtColor(roi2,cv2.COLOR_BGR2HSV)#Conversión
HSV3 = cv2.cvtColor(roi3,cv2.COLOR_BGR2HSV)#Conversión
HSV4 = cv2.cvtColor(roi4,cv2.COLOR_BGR2HSV)#Conversión
HSV5 = cv2.cvtColor(roi5,cv2.COLOR_BGR2HSV)#Conversión

n1bajo = np.array([21,243,239],np.uint8) #[21,195,215]
n1alto = np.array([33,255,255],np.uint8)
n2bajo = np.array([16,201,244],np.uint8)#[11,196,193]
n2alto = np.array([24,241,255],np.uint8)#[28,255,255]
n3bajo = np.array([135,1,42],np.uint8)#[11,196,193]
n3alto = np.array([180,255,255],np.uint8)#[28,255,255]
n4bajo = np.array([155,16,100],np.uint8)#[11,196,193]
n4alto = np.array([179,156,226],np.uint8)#[28,255,255]
n5bajo = np.array([0,67,205],np.uint8)#[0,5,181]
n5alto = np.array([5,255,255],np.uint8)#[5,255,255]

mask=cv2.inRange(HSV,n1bajo,n1alto)
mask2=cv2.inRange(HSV2,n2bajo,n2alto)
mask3=cv2.inRange(HSV3,n3bajo,n3alto)
mask4=cv2.inRange(HSV4,n4bajo,n4alto)
mask5=cv2.inRange(HSV5,n5bajo,n5alto)

imgMask=cv2.bitwise_and(roi1,roi1,mask=mask)
imgMask2=cv2.bitwise_and(roi2,roi2,mask=mask2)
imgMask3=cv2.bitwise_and(roi3,roi3,mask=mask3)
imgMask4=cv2.bitwise_and(roi4,roi4,mask=mask4)
imgMask5=cv2.bitwise_and(roi5,roi5,mask=mask5)

u=roi1-(imgMask)
u2=roi2-(imgMask2)
u3=roi3-(imgMask3)
u4=roi4-(imgMask4)
u5=roi5-(imgMask5)


image[141:203,146:285]=u
image[307:354,200:255]=u2
image[137:199,365:418]=u3
image[177:255,0:46]=u4
image[318:428,0:73]=u5

cv2.imshow('Imag en negro',image)
G = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)#Conversión a HSV
G = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)#Conversión a HSV
masku=cv2.inRange(G,(0,0,0),(1,1,1))
cnv=image1.copy()
filas=np.size(image1,0)
columnas=np.size(image1,1)
print(filas)
print(columnas)
i=0
suma=0
b = cnv[:, :, 0]
g = cnv[:, :, 1]
roj = cnv[:, :, 2]
for e in range(filas):
    for r in range(columnas):
        if masku[e, r] == 255:
             b[e, r] = 255
             g[e, r] = 255
             roj[e, r] = 255
IF = cv2.merge([b, g, roj])
cv2.imshow('Imagen1',IF)
cv2.imshow('Comparacion',np.hstack([IF,image1]))
cv2.waitKey(0)
cv2.destroyAllWindows()