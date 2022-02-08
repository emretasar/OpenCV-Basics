import cv2

cap = cv2.VideoCapture(0)
circles = []
rectangle_pos = []

def mouse(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        circles.append((x,y))
    elif event == cv2.EVENT_RBUTTONDOWN:
        rectangle_pos.append((x, y))
        

cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame",mouse)

while True:
    _,frame = cap.read()
    frame = cv2.resize(frame,(640,480))
    for center in circles:
        cv2.circle(frame,center,20,(255,0,0),-1)
    if len(rectangle_pos) == 2:
        cv2.rectangle(frame, rectangle_pos[0], rectangle_pos[1], (255, 0, 0))
    elif len(rectangle_pos) > 2:
        rectangle_pos = []
    cv2.imshow("Frame",frame)
    key = cv2.waitKey(1)
    if key==27:
        break
    elif key == ord("h"):
        circles =[]

    if cv2.waitKey(20) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
    
















