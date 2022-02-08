import cv2
import numpy as np

font = cv2.FONT_HERSHEY_SIMPLEX

image = cv2.imread('polygons.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, threshold = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    epsilon = 0.01 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    cv2.drawContours(image, [approx], 0, (0), 5)

    x = approx.ravel()[0]
    y = approx.ravel()[1]

    if(len(approx) == 3):
        cv2.putText(image, "Triangle", (x, y), font, 1, (0))
    elif(len(approx) == 4):
        cv2.putText(image, "Rectangle", (x, y), font, 1, (0))
    elif(len(approx) == 5):
        cv2.putText(image, "Pentagon", (x, y), font, 1, (0))
    elif(len(approx) == 6):
        cv2.putText(image, "Hexagon", (x, y), font, 1, (0))
    else:
        cv2.putText(image, "Elips", (x, y), font, 1, (0))

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()