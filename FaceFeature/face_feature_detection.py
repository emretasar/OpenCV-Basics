import cv2
import numpy as np
import math

def findMaxContour(contours):
    max_indice = 0
    max_area = 0
    for i in range(len(contours)):
        area_face = cv2.contourArea(contours[i])
        
        if max_area<area_face:
            max_area=area_face
            max_indice = i
        try:
            contour = contours[max_indice]            
        except:
            contours = [0]
            contour = contours[0]
    return contour  


def nothing(x):
    pass

cv2.namedWindow("Trackbar")
cv2.createTrackbar("Lower Hue", "Trackbar", 0, 179, nothing)
cv2.createTrackbar("Lower Sat", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("Lower Val", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("Upper Hue", "Trackbar", 0, 179, nothing)
cv2.createTrackbar("Upper Sat", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("Upper Val", "Trackbar", 0, 255, nothing)

cap = cv2.VideoCapture('MichaelScott.mp4')


while True:
    ret,frame = cap.read()
    if ret is False:
        continue
    frame = cv2.flip(frame,1)
    
    roi = frame[100:580, 380:860] # frame[y1:y2,x1:x2]
    cv2.rectangle(frame,(380,100),(860,580),(0,0,255),0)

    hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
    lh = cv2.getTrackbarPos("Lower Hue", "Trackbar")
    ls = cv2.getTrackbarPos("Lower Sat", "Trackbar")
    lv = cv2.getTrackbarPos("Lower Val", "Trackbar")
    uh = cv2.getTrackbarPos("Upper Hue", "Trackbar")
    us = cv2.getTrackbarPos("Upper Sat", "Trackbar")
    uv = cv2.getTrackbarPos("Upper Val", "Trackbar")

    lower_color = np.array([lh, ls, lv])
    upper_color = np.array([uh, us, uv])

    mask = cv2.inRange(hsv,lower_color,upper_color)
    
    kernel = np.ones((3,3),np.uint8)
    mask = cv2.dilate(mask,kernel,iterations=1)
    mask = cv2.medianBlur(mask,15)

    contours,_ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
      
        c = findMaxContour(contours)
            
        extLeft = tuple(c[c[:, :, 0].argmin()][0])
        extRight = tuple(c[c[:, :, 0].argmax()][0])
        extTop = tuple(c[c[:, :, 1].argmin()][0])
        extBot = tuple(c[c[:, :, 1].argmax()][0])

        cv2.circle(roi,extLeft,5,(0,255,0),2)
        cv2.circle(roi,extRight,5,(0,255,0),2)
        cv2.circle(roi,extTop,5,(0,255,0),2)
        cv2.circle(roi,extBot,5,(0,255,0),2)

        cv2.line(roi,extLeft,extTop,(255,0,0),2)
        cv2.line(roi,extTop,extRight,(255,0,0),2)
        cv2.line(roi,extRight,extBot,(255,0,0),2)
        cv2.line(roi,extBot,extLeft,(255,0,0),2)

        a = math.sqrt((extRight[0]-extTop[0])**2+(extRight[1]-extTop[1])**2)
        b = math.sqrt((extBot[0]-extRight[0])**2+(extBot[1]-extRight[1])**2)
        c = math.sqrt((extBot[0]-extTop[0])**2+(extBot[1]-extTop[1])**2)

        try:
            angle_ab= int(math.acos((a**2+b**2-c**2)/(2*b*c))*57)
            cv2.putText(roi,str(angle_ab),(extRight[0]-100+50,extRight[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv2.LINE_AA)
        except:
            cv2.putText(roi," ? ",(extRight[0]-100+50,extRight[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv2.LINE_AA)
   
    # cv2.imshow("frame",frame)
    cv2.imshow("roi",roi)
    cv2.imshow("mask",mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
