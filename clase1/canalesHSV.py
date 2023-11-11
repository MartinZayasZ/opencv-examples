import cv2
import matplotlib.pyplot as plt

# Creamos la matriz principal
img = cv2.imread('LEC.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# corregimos
imghsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

# extraemos los canales
H, S, V = cv2.split(imghsv)

# Mostramos nuestros canales
fig = plt.figure()
# canal H
ax1 = fig.add_subplot(2, 2, 1)
ax1.imshow(H, cmap="gray")
ax1.set_title("CANAL H")
# canal S
ax2 = fig.add_subplot(2, 2, 2)
ax2.imshow(S, cmap="gray")
ax2.set_title("CANAL S")
# canal V
ax3 = fig.add_subplot(2, 2, 3)
ax3.imshow(V, cmap="gray")
ax3.set_title("CANAL V")

# Reconstrucción
imgre = cv2.merge((H, S, V))

ax4 = fig.add_subplot(2, 2, 4)
ax4.imshow(imgre)
ax4.set_title("IMAGEN ORIGINAL")

plt.imshow(img)
plt.show()