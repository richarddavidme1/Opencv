import cv2
import numpy as np

img=cv2.imread('C:\\Users\\Richard\\Documents\\98F.jpg')
cv2.line(img,(0,0),(300,300),(255,255,255),15)
cv2.rectangle(img,(50,85),(250,200),(0,0,255),15)
cv2.circle(img,(100,100),50,(120,145,100),-1)
#Poligono
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
cv2.polylines(img, [pts], True, (0,255,255), 3)
#Poner Texto
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'MODO SABIO !!!', (0, 130), font,3, (200, 255, 155), 5, cv2.LINE_AA)

cv2.imshow("Dibujo",img)
cv2.waitKey(0)
cv2.destroyAllWindows()