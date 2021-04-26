import numpy as np
import cv2

cap=cv2.VideoCapture("C:\\Users\\Richard\\Documents\\Videos\\flor.mp4")
while (True):

  ret,frame=cap.read()
  resize = cv2.resize(frame, (600,400), interpolation=cv2.INTER_LINEAR)
  cv2.imshow("Color",resize)

  if cv2.waitKey(1) & 0xFF ==ord('q'):
      break

cap.release()
cv2.destroyAllWindows()

