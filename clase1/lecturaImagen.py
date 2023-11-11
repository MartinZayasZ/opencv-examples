import cv2
import numpy as np
import matplotlib.pyplot as plt

#si le ponemos el 0, es para escala de grises
#el 1 es para rgb, 3 canales
#por defecto es rgb
imgGray = cv2.imread("LEC.png", 0)
imgRGB = cv2.imread("LEC.png", 1)
img = cv2.imread("LEC.png")


#extraer atributos principales
tamano = imgGray.shape
tipo = imgGray.dtype
print("Tamaño Gray | Tipo de daato | ", tamano, tipo)

#extraer atributos principales
tamanoRGB = imgRGB.shape
tipoRGB = imgRGB.dtype
print("Tamaño RGB | Tipo de dato | ", tamanoRGB, tipoRGB)



cv2.imshow('GRAY', imgGray)
cv2.imshow('RGB', imgRGB)
cv2.imshow('IMG', img)

#corrección de color
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)



plt.imshow(img)
plt.show()


cv2.waitKey(0)