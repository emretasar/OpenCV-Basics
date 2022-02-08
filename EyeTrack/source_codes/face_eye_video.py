import cv2

face_cascade = cv2.CascadeClassifier("../haar_cascades/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("../haar_cascades/haarcascade_eye.xml")

video = cv2.VideoCapture('../test_media/MichaelScott.mp4')
# video = cv2.VideoCapture(0)
while True:
    ret, frame = video.read()
    frame = cv2.resize(frame, (640, 360))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 5)

    roi_frame = frame[y:y+h, x:x+w]
    roi_gray = gray[y:y+h, x:x+w]

    eyes = eye_cascade.detectMultiScale(roi_gray, 1.2, 5)

    eye_num = 0
    for (ex, ey, ew, eh) in eyes:
        eye_num+=1
        cv2.rectangle(roi_frame, (ex, ey), (ex+ew, ey+eh), (0, 0, 255), 3)
        if eye_num == 2:
            break
        
    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

