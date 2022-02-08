import numpy as np
import cv2

image1 = cv2.imread('test1.jpg')
image1 = cv2.resize(image1, (600, 400))

image2 = cv2.imread('test2.jpg')
image2 = cv2.resize(image2, (600, 400))

image3 = cv2.medianBlur(image2, 5)

diff = cv2.absdiff(image1, image3)
blue, green, red = cv2.split(diff)

if cv2.countNonZero(blue) == 0 and cv2.countNonZero(green) == 0 and cv2.countNonZero(red) == 0:
    print('Same Pictures')
else:
    print('Different Pictures')
# cv2.imshow('diff', diff)
# cv2.imshow('image1', image1)
# cv2.imshow('image2', image2)

cv2.waitKey(0)
cv2.destroyAllWindows()
