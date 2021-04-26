import cv2
print("OpenCV OK!!!")

"""
#Cargar imagenes
img =cv2.imread("D:\\Programacion\\Python\\Opencv\\1.png")
cv2.imshow("Salida",img)
cv2.waitKey(0)

"""
#Video y caracteristicas
#importar camara con 0
cap=cv2.VideoCapture("D:\\Programacion\\Python\\Opencv\\Women.mp4")
#cap=cv2.VideoCapture(0)
cap.set(3,640) #ID=3 width(ancho) normal 640x480
cap.set(4,480) #ID=4 height(altura)
cap.set(10,75) #ID=10 brillo
while(True):
    comprobar,img=cap.read()
    img1=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    frame = cv2.flip(img, 1) #Camara espejo
    if comprobar :
        print("Video Funciona")
    cv2.imshow("Video",img)
    cv2.imshow("Espejo",frame)
    cv2.imshow("HSV", img1)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()