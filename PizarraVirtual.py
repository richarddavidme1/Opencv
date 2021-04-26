import cv2
import numpy as np

MisColores=[[88,157,111,136,247,253],[45, 95, 61 ,95 ,238 ,208],[0, 142 ,151 ,32, 228, 241]]
# Azul,Verde,Rojo
ColoresPunta=[[204,0,0],[0,204,0],[0,0,255]]
#BGR Azul,Verde,ROjo
Punto=[]
#[x,y,colorid]

#FIltrado y rango de colores

def Colores(img,MisColores,ColoresPunta):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    c=0
    NuevosPuntos=[]
    #LLamar valors de los rangos dentro del array
    """Inf = np.array(MisColores[2][0:3])  # minumos
    Sup = np.array(MisColores[2][3:6])
    mask = cv2.inRange(hsv, Inf, Sup)
    cv2.imshow("mask",mask)"""
    for color in MisColores:
        #ciclo for para buscar el numeor de colores en el array
        Inf = np.array(color[0:3])  # minumos
        Sup = np.array(color[3:6])  # maximos
        mask = cv2.inRange(hsv, Inf, Sup)
        #imprimir el numero de colores en ventanas
        #cv2.imshow(str(color[0]), mask)
        x,y=EncontrarContornos(mask)
        cv2.circle(copia,(x,y),10,ColoresPunta[c],cv2.FILLED)
        if x!=0 and y!=0:
            NuevosPuntos.append([x,y,c])
        c +=1
    return NuevosPuntos
#Encontrar con los contornos

def EncontrarContornos(img):
    contornos,jerarquia=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    for cnt in contornos:
        area=cv2.contourArea(cnt)
        print(area)
        if(area > 500):
            #cv2.drawContours(copia,cnt,-1,(0,255,255),3)
            perimetro=cv2.arcLength(cnt,True)
            print(perimetro)
            #Cerrar contornos
            aproximar=cv2.approxPolyDP(cnt,0.02*perimetro,True)
            #Numero de lados (tipo de figuras)
            print(len(aproximar))
            #Creamos la figura geometrica
            ObjetoCreado=len(aproximar)
            x,y,w,h=cv2.boundingRect(aproximar)
            #Cuadros limitadore de la figura
    return x+w//2,y

#Dibujar seguidor del marcador

def DibujarMarcador(Mispuntos,MisColores):
    for puntos in  Mispuntos:
        #se pasa al vector Puntos como referencia
        cv2.circle(copia, (puntos[0], puntos[1]), 20, ColoresPunta[puntos[2]], cv2.FILLED)


cap=cv2.VideoCapture(0)
cap.set(3,800) #ID=3 width(ancho) normal 640x480
cap.set(4,600) #ID=4 height(altura)
while(True):
    c1,frame1=cap.read()
    frame = cv2.flip(frame1, 1)
    copia=frame.copy()
    NuevosPuntos=Colores(frame,MisColores,ColoresPunta)
    #Enlistar de la funcion return
    if len(NuevosPuntos) !=0:
        for npt in NuevosPuntos:
            Punto.append(npt)
    #Dibujamos en la pantalla
    if len(Punto)!=0:
        DibujarMarcador(Punto,MisColores)

    cv2.imshow("Dibujar", copia)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
