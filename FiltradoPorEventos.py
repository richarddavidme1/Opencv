import numpy as np
import cv2 as cv

drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1
row,colum=1,1
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv.circle(img,(x,y),5,(0,0,255),-1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            roi = img1[row:ix + x, colum:iy + y]
        else:
            cv.circle(img,(x,y),5,(0,0,255),-1)
img = np.zeros((400,700, 3), np.uint8)
cv.namedWindow('Marcador')
cv.setMouseCallback('Marcador', draw_circle)


while (1):
    img1=cv.imread("D:\\Programacion\\Python\\Opencv\\FrutasColores.jpg")
    suma=cv.bitwise_and(img,img1)
    roi=cv.selectROI(suma)
    roi = img1[row:ix, colum:iy]
    print(img1.shape)


    cv.imshow('Marcador', img1)
    cv.imshow('Salida',suma)
    cv.imshow('ROI', roi)

    key = cv.waitKey(1)
    if key == 27:
        break




cv.destroyAllWindows()