import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture("hsv.mp4")
cv2.namedWindow("Trackbar")
cv2.createTrackbar("Lower Hue", "Trackbar", 0, 179, nothing)
cv2.createTrackbar("Lower Sat", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("Lower Val", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("Upper Hue", "Trackbar", 0, 179, nothing)
cv2.createTrackbar("Upper Sat", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("Upper Val", "Trackbar", 0, 255, nothing)


while True:
    ret, frame = cap.read()
    if ret is False:
        continue
    frame = cv2.resize(frame, (500, 300))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos("Lower Hue", "Trackbar")
    ls = cv2.getTrackbarPos("Lower Sat", "Trackbar")
    lv = cv2.getTrackbarPos("Lower Val", "Trackbar")
    uh = cv2.getTrackbarPos("Upper Hue", "Trackbar")
    us = cv2.getTrackbarPos("Upper Sat", "Trackbar")
    uv = cv2.getTrackbarPos("Upper Val", "Trackbar")

    lower_blue = np.array([lh, ls, lv])
    upper_blue = np.array([uh, us, uv])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    bitwise = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("bitwise", bitwise)

    if cv2.waitKey(20) & 0xFF==ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
