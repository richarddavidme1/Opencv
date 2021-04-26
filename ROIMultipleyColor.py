import cv2
import numpy as np


def empty(a):
    pass

#primera imagen
cv2.namedWindow("RangosHSV")
cv2.resizeWindow("RangosHSV", (400, 320))

cv2.createTrackbar("H Max", "RangosHSV", 179, 179, empty)
cv2.createTrackbar("H Min", "RangosHSV", 0, 179, empty)
cv2.createTrackbar("S Max", "RangosHSV", 255, 255, empty)
cv2.createTrackbar("S Min", "RangosHSV", 0, 255, empty)
cv2.createTrackbar("V Max", "RangosHSV", 255, 255, empty)
cv2.createTrackbar("V Min", "RangosHSV", 0, 255, empty)

#segunda imagen
cv2.namedWindow("RangosHSV1")
cv2.resizeWindow("RangosHSV1", (400, 320))

cv2.createTrackbar("H1 Max", "RangosHSV1", 179, 179, empty)
cv2.createTrackbar("H1 Min", "RangosHSV1", 0, 179, empty)
cv2.createTrackbar("S1 Max", "RangosHSV1", 255, 255, empty)
cv2.createTrackbar("S1 Min", "RangosHSV1", 0, 255, empty)
cv2.createTrackbar("V1 Max", "RangosHSV1", 255, 255, empty)
cv2.createTrackbar("V1 Min", "RangosHSV1", 0, 255, empty)



#Primera imagen


img = cv2.imread("D:\\Programacion\\Python\\Opencv\\FrutasColores.jpg")
print(img.shape)
roi = cv2.selectROI(img)
roi_cropped = img[int(roi[1]):int(roi[1] + roi[3]), int(roi[0]):int(roi[0] + roi[2])]


#segunda imagen

img1 = cv2.imread("D:\\Programacion\\Python\\Opencv\\Figuras.jpg")
roi1 = cv2.selectROI(img1)
roi_cropped1= img1[int(roi1[1]):int(roi1[1] + roi1[3]), int(roi1[0]):int(roi1[0] + roi1[2])]
print(roi1)
data1 = np.array(roi)

while (True):
    #primera imagen
    h_max = cv2.getTrackbarPos("H Max", "RangosHSV")
    h_min = cv2.getTrackbarPos("H Min", "RangosHSV")
    s_max = cv2.getTrackbarPos("S Max", "RangosHSV")
    s_min = cv2.getTrackbarPos("S Min", "RangosHSV")
    v_max = cv2.getTrackbarPos("V Max", "RangosHSV")
    v_min = cv2.getTrackbarPos("V Min", "RangosHSV")

    # primera imagen

    imgHsv = cv2.cvtColor(roi_cropped, cv2.COLOR_BGR2HSV)
    imgHsv1 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    imgBGR = cv2.cvtColor(roi_cropped, cv2.COLOR_HSV2BGR)


    # primera imagen
    Inf = np.array([h_min, s_min, v_min])  # minumos
    Sup = np.array([h_max, s_max, v_max])  # maximos


    mask = cv2.inRange(imgHsv, Inf, Sup)
    mask_inv = cv2.bitwise_not(mask)
    imaresul = cv2.bitwise_and(roi_cropped, roi_cropped, mask=mask_inv)

    cv2.imshow("Original", img)
    cv2.imshow("ROI", roi_cropped)
    cv2.imshow("HSV", imgHsv)
    cv2.imshow("Mascara", mask)
    cv2.imshow("Mascara Inversa", mask_inv)
    cv2.imshow("ResultadoImagen1", imaresul)


    #segunda imagen
    h1_max = cv2.getTrackbarPos("H1 Max", "RangosHSV1")
    h1_min = cv2.getTrackbarPos("H1 Min", "RangosHSV1")
    s1_max = cv2.getTrackbarPos("S1 Max", "RangosHSV1")
    s1_min = cv2.getTrackbarPos("S1 Min", "RangosHSV1")
    v1_max = cv2.getTrackbarPos("V1 Max", "RangosHSV1")
    v1_min = cv2.getTrackbarPos("V1 Min", "RangosHSV1")

    #segunda imagen

    imgHsv1 = cv2.cvtColor(roi_cropped1, cv2.COLOR_BGR2HSV)
    imgHsv11 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
    imgBGR1 = cv2.cvtColor(roi_cropped1, cv2.COLOR_HSV2BGR)

    #segunda imagen
    Inf1 = np.array([h1_min, s1_min, v1_min])  # minumos
    Sup1= np.array([h1_max, s1_max, v1_max])  # maximos

    transformed_image = cv2.merge((h_min, h_max, s_min, s_max, v_min, v_max))

    #segunda imagen
    mask1 = cv2.inRange(imgHsv1, Inf1, Sup1)
    mask_inv1 = cv2.bitwise_not(mask1)

    #segunda imagene

    imaresul1 = cv2.bitwise_and(roi_cropped1,roi_cropped1,mask=mask_inv1)


    cv2.imshow("Original1", img1)
    cv2.imshow("ROI1", roi_cropped1)
    #cv2.imshow("HSV1", imgHsv1)
    cv2.imshow("Mascara1", mask1)
    cv2.imshow("Mascara Inversa1", mask_inv1)
    cv2.imshow("ResultadoImagen2", imaresul1)




    key = cv2.waitKey(1)
    if key == 27:
        break



cv2.destroyAllWindows()