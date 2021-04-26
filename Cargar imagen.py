#cargar imagenes y poner a escala de grises

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('C://Users//Richard//Documents//98F.jpeg',1)
cv.imshow('image',img)
cv.waitKey(10)
cv.destroyAllWindows()