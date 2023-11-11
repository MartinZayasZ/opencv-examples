import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("monedas.jpg")
imgmat = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# convertimos a EDG
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# creamos una matrix del tamaño de la IMG
matriz = np.ones(gray.shape, dtype='uint8') * 50
matrizrgb = np.ones(img.shape, dtype='uint8') * 50

#aumentamos el brillo en RGB
brillantergb = cv2.add(img, matrizrgb)
brillantergbm = cv2.cvtColor(brillantergb, cv2.COLOR_BGR2RGB)

#disminuimos el brillo de la imagen RGB
oscurargb = cv2.subtract(img, matrizrgb)
oscurargbm =  cv2.cvtColor(oscurargb, cv2.COLOR_BGR2RGB)


#mostramos con matplotlib
fig = plt.figure()
ax1 = fig.add_subplot(2,3,1)
ax1.imshow(imgmat)
ax1.set_title("Imagen Original")

ax2 = fig.add_subplot(2,3,2)
ax2.imshow(brillantergbm)
ax2.set_title("Brillante RGB")

ax3 = fig.add_subplot(2,3,3)
ax3.imshow(oscurargbm)
ax3.set_title('Oscura RGB')

plt.show()