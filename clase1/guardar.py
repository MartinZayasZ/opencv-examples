import cv2
import matplotlib.pyplot as plt

# crear matriz principal
img = cv2.imread("LEC.png")

# Corregimos
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

R, G, B = cv2.split(img)

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
imgre = cv2.merge((R+100, G, B))

# canal azul
ax4 = fig.add_subplot(2, 2, 4)
ax4.imshow(imgre)
ax4.set_title("IMAGEN ORIGINAL")

newimage = cv2.cvtColor(imgre, cv2.COLOR_BGR2RGB)
# guardamos la imagen
cv2.imwrite("NUEVAIMAGEN.png", newimage)


plt.show()

cv2.waitKey(0)