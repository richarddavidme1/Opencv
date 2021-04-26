import cv2
import numpy as np

cap=cv2.VideoCapture("C:\\Users\\Richard\\Documents\\a.mp4")


while(True):
    _,frame=cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([102, 0, 0])
    upper_red = np.array([179, 255, 180])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    kernel = np.ones((5, 5), np.uint8)


    top=cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernel)
    blackh = cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT, kernel)

    cv2.imshow("Video",frame)
    cv2.imshow("TopHat", top)
    cv2.imshow("Blackhat", blackh)


    k = cv2.waitKey(4) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
