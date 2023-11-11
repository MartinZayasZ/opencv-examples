import cv2
import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((10,10,1), np.uint8)

img[0,1] = 30
img[2,3] = 50
img[9,9] = 50


print(img)


plt.imshow(img, cmap='gray')
plt.show()