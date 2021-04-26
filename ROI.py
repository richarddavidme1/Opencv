import cv2
import numpy as np



def empty(a):
    pass
cv2.namedWindow("RangosHSV")
cv2.resizeWindow("RangosHSV",(400,320))

cv2.createTrackbar("H Max","RangosHSV",179,179,empty)
cv2.createTrackbar("H Min","RangosHSV",0,179,empty)
cv2.createTrackbar("S Max","RangosHSV",255,255,empty)
cv2.createTrackbar("S Min","RangosHSV",0,255,empty)
cv2.createTrackbar("V Max","RangosHSV",255,255,empty)
cv2.createTrackbar("V Min","RangosHSV",0,255,empty)

img = cv2.imread("D:\\Programacion\\Python\\Opencv\\FrutasColores.jpg")
print(img.shape)
roi = cv2.selectROI(img)
roi_cropped = img[int(roi[1]):int(roi[1] + roi[3]), int(roi[0]):int(roi[0] + roi[2])]
print(roi)
data1 = np.array(roi)


while (True):
    h_max = cv2.getTrackbarPos("H Max", "RangosHSV")
    h_min = cv2.getTrackbarPos("H Min", "RangosHSV")
    s_max = cv2.getTrackbarPos("S Max", "RangosHSV")
    s_min = cv2.getTrackbarPos("S Min", "RangosHSV")
    v_max = cv2.getTrackbarPos("V Max", "RangosHSV")
    v_min = cv2.getTrackbarPos("V Min", "RangosHSV")


    imgHsv = cv2.cvtColor(roi_cropped, cv2.COLOR_BGR2HSV)
    imgHsv1 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    imgBGR = cv2.cvtColor(roi_cropped, cv2.COLOR_HSV2BGR)


    #print("Valores de HSV")
    #print(h_min,h_max,s_min,s_max,v_min,v_max)

    Inf=np.array([h_min,s_min,v_min])#minumos
    Sup=np.array([h_max,s_max,v_max])#maximos

    transformed_image = cv2.merge((h_min,h_max,s_min, s_max,v_min, v_max))

    mask=cv2.inRange(imgHsv,Inf,Sup)
    mask_inv = cv2.bitwise_not(mask)


    #print("Valores de RGB")
   # print(imgBGR)
    imaresul=cv2.bitwise_and(roi_cropped,roi_cropped,mask=mask_inv)
    #sumar = cv2.add(img,data1)
    #sumar=cv2.bitwise_and(img,roi,mask)

    #print("El valor de roi "+str(roi_cropped))

    cv2.imshow("Original",img)
    cv2.imshow("ROI",roi_cropped)
    cv2.imshow("HSV",imgHsv)
    #cv2.imshow("HSV", resta)
    #cv2.imshow("BGR",imgBGR)
    cv2.imshow("Mascara",mask)
    cv2.imshow("Mascara Inversa", mask_inv)
    cv2.imshow("Resultado",imaresul)


    key = cv2.waitKey(1)
    if key == 27:
        break
cv2.destroyAllWindows()


