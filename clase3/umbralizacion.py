import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("monedas.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

matriz = np.ones(gray.shape, dtype='uint8') * 50
