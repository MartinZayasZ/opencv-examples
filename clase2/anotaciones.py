import cv2

img = cv2.imread("dibujo.png")

# redimensionamos
img = red3 = cv2.resize(img, None, fx=0.5,fy=0.5, interpolation=cv2.INTER_CUBIC)

# línea
linea = cv2.line(img, (int(1070/2), int(194/2)), (int(1152/2),int(461/2)), (0, 255, 0), thickness=5, lineType=cv2.LINE_AA)

#circulo
linea = cv2.circle(img, (int(1080/2), int(185/2)), 70, (255, 255, 0), thickness=1, lineType=cv2.LINE_AA)

#rectangulo
linea = cv2.rectangle(img, (int(1010/2), int(425/2)), (int(1381/2),int(566/2)), (255, 0, 255), thickness=3, lineType=cv2.LINE_AA)

#Texto
text = "Robot Detectado"
tpletra = cv2.FONT_ITALIC
tmletra = 1.1
color = (0,255,0)
grosor = 2
texto = cv2.putText(img, text, (int(995/2), int(650/2)), tpletra, tmletra, color, grosor)


cv2.imshow("Hola mundo", img)

cv2.waitKey(0)
