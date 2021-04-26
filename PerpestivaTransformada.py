import numpy as np
import cv2

cap = cv2.VideoCapture(0)


while (True):
    ret, img = cap.read()

  # Puntos de la imagen o video en perspectiva
    cv2.circle(img, (470, 206), 5, (0, 0, 255), -1)
    cv2.circle(img, (1479, 198), 5, (0, 0, 255), -1)
    cv2.circle(img, (32, 1122), 5, (0, 0, 255), -1)
    cv2.circle(img, (1980, 1125), 5, (0, 0, 255), -1)

    pts1 = np.float32([[470, 206], [1479, 198], [32, 1122], [1980, 1125]])
    pts2 = np.float32([[0, 0], [500, 0], [0, 600], [500, 600]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(img, matrix, (500, 600))

    cv2.imshow("Pantalla Origianl", img)
    cv2.imshow("Perspective transformation", result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()