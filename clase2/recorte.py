import cv2
import matplotlib.pyplot as plt
import numpy as np



# creamos imagen, crear matriz principal
img = 100 * np.ones((10,10,3), np.uint8)
imageCopy = 100 * np.ones((10,10,3), np.uint8)
R, G, B = cv2.split(img)

img[4,5,0] = 255
img[4,4,0] = 0
img[5,4,0] = 255
img[5,5,0] = 0

img[4,5,1] = 0
img[4,4,1] = 255
img[5,4,1] = 0
img[5,5,1] = 255

img[4,5,2] = 255
img[4,4,2] = 255
img[5,4,2] = 0
img[5,5,2] = 0

# realizamos recorte(filas, columnas)
recorte = img[3:7, 3:7]


fig = plt.figure()
ax1 = fig.add_subplot(1,2,1)
ax1.imshow(img)
ax1.set_title("IMAGEN")

ax2 = fig.add_subplot(1,2,2)
ax2.imshow(recorte)
ax2.set_title("Recorte")


plt.show()


img = cv2.imread("img.png")
# truco paint
rct = img[8:30, 225:275]

#~mostramos el recorte
cv2.imshow('Imagen Original', img)
cv2.imshow('Recorte', rct)

cv2.waitKey(0)

