import cv2
import matplotlib.pyplot as plt
import numpy as np

#img = 100 * np.ones((10, 10, 3), np.uint8)

img = cv2.imread("img.png")

# redimensionar
red1 = cv2.resize(img, None, fx=1.5, fy=1.5)
red2 = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_AREA)
red3 = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)

#red 4
ancho = 400
alto = 500
tam = (ancho, alto)
red4 = cv2.resize(img, tam, interpolation=cv2.INTER_CUBIC)

cv2.imshow("Original", img)
#cv2.imshow("Redimension 1", red1)
#cv2.imshow("Redimension 2", red2)
#cv2.imshow("Redimension 3", red3)
cv2.imshow("Redimension 4", red4)

cv2.waitKey(0)