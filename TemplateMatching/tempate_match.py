import cv2
import numpy as np

image = cv2.imread('test1.jpg', cv2.IMREAD_GRAYSCALE)
template = cv2.imread('test2.jpg', cv2.IMREAD_GRAYSCALE)
height, width = template.shape

matchs = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
locations = np.where(matchs >= 0.9)

min_heigth = np.amin(locations[0])
min_width = np.amin(locations[1])

cv2.rectangle(image, (min_width, min_heigth), (min_width + width, min_heigth + height), (255, 0, 0), 3)
cv2.imshow('image', image)

cv2.waitKey(0)

