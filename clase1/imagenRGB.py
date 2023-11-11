import cv2
import numpy as np
import matplotlib.pyplot as plt

img = 100 * np.ones((10,10,3), np.uint8)



R = img[:,:,0]
G = img[:,:,1]
B = img[:,:,2]

R[:, :] = 255
G[:, :] = 255
B[:, :] = 0

B[9, 9] = 255


print(img)

plt.imshow(img)
plt.show()


cv2.waitKey(0)