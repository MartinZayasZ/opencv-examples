import cv2

img = cv2.imread("img.png")

rot1 = cv2.flip(img, 0)
rot2 = cv2.flip(img, 1)
rot3 = cv2.flip(img, -1)

cv2.imshow("Imagen Original", img)
#cv2.imshow("Rotación 1", rot1)
cv2.imshow("Rotación 2", rot2)
#cv2.imshow("Rotación 3", rot3)


cv2.waitKey(0)