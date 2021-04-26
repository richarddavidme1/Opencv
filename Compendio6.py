import cv2
import numpy as np

def SobreponerImagenesDeSalida(scale,imgArray):

    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def empty(a):
    pass

cv2.namedWindow("RangosHSV")
cv2.resizeWindow("RangosHSV",(400,320))

cv2.createTrackbar("H Max","RangosHSV",60,179,empty)
cv2.createTrackbar("H Min","RangosHSV",1,179,empty)
cv2.createTrackbar("S Max","RangosHSV",255,255,empty)
cv2.createTrackbar("S Min","RangosHSV",98,255,empty)
cv2.createTrackbar("V Max","RangosHSV",255,255,empty)
cv2.createTrackbar("V Min","RangosHSV",69,255,empty)

while (True):
    img = cv2.imread("D:\\Programacion\\Python\\Opencv\\taza.jpg")
    imgHsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    imgBGR=cv2.cvtColor(imgHsv,cv2.COLOR_HSV2BGR)

    h_max = cv2.getTrackbarPos("H Max", "RangosHSV")
    h_min = cv2.getTrackbarPos("H Min", "RangosHSV")
    s_max = cv2.getTrackbarPos("S Max", "RangosHSV")
    s_min = cv2.getTrackbarPos("S Min", "RangosHSV")
    v_max = cv2.getTrackbarPos("V Max", "RangosHSV")
    v_min = cv2.getTrackbarPos("V Min", "RangosHSV")

    print(h_min,h_max,s_min,s_max,v_min,v_max)

    Inf=np.array([h_min,s_min,v_min])#minumos
    Sup=np.array([h_max,s_max,v_max])#maximos
    mask=cv2.inRange(imgHsv,Inf,Sup)
    imaresul=cv2.bitwise_and(img,img,mask=mask)


    """cv2.imshow("Original",img)
    cv2.imshow("HSV",imgHsv)
    cv2.imshow("BGR",imgBGR)
    cv2.imshow("Mascara",mask)
    cv2.imshow("Resultado",imaresul)"""

    ImagenesSalida=SobreponerImagenesDeSalida(0.4,([img,imgHsv,imgBGR],[img,mask,imaresul]))
    cv2.imshow("SalidaDeProcesos",ImagenesSalida)

    key = cv2.waitKey(1)
    if key == 27:
        break
cv2.destroyAllWindows()