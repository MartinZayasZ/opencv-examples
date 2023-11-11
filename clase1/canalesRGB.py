import cv2
import matplotlib.pyplot as plt

img = cv2.imread("LEC.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#extraemos los canales
R = img[:, :, 0]
G = img[:, :, 1]
B = img[:, :, 2]

#o la función simplificada para hacer eso
#R, G, B = cv2.split(img)

# Mostramos nuestros canales
fig = plt.figure()
# canal rojo
ax1 = fig.add_subplot(2, 2, 1)
ax1.imshow(R, cmap="gray")
ax1.set_title("CANAL ROJO")
# canal verde
ax2 = fig.add_subplot(2, 2, 2)
ax2.imshow(G, cmap="gray")
ax2.set_title("CANAL VERDE")
# canal azul
ax3 = fig.add_subplot(2, 2, 3)
ax3.imshow(B, cmap="gray")
ax3.set_title("CANAL AZUL")

# Reconstrucción
imgre = cv2.merge((R, G, B))

# canal azul
ax4 = fig.add_subplot(2, 2, 4)
ax4.imshow(imgre)
ax4.set_title("IMAGEN ORIGINAL")









plt.imshow(img)
plt.show()