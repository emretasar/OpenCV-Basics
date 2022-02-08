import numpy as np
import cv2

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while True:
	ret, image = cap.read()
	gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	eyes = eye_cascade.detectMultiScale(gray_image)
	
	
	for (ex,ey,ew,eh) in eyes:
   		cv2.rectangle(image,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
   		roi = image[ex:ey, ex+ew:ey+eh]

	cv2.imshow('Frame', image)
	cv2.imshow('Roi', roi)
	key = cv2.waitKey(30) & 0xFF
	if key == 27:
   		break

cap.release()
cv2.destroyAllWindows()