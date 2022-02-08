import cv2

video = cv2.VideoCapture('../test_media/eye.mp4')

while True:
    ret, frame = video.read()
    if ret is False:
        break
    
    roi = frame[80:480, 160:850]
    rows, columns, _ = roi.shape
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, 5, 255, cv2.THRESH_BINARY_INV)

    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

    for contour in contours:
        (x1, y1, x2, y2) = cv2.boundingRect(contour)
        cv2.rectangle(roi, (x1, y1), (x1+x2, y1+y2) , (0, 0, 255))
        cv2.line(roi, (x1 + x2//2, 0), (x1 + x2//2, rows), (255, 0, 0), 2)
        cv2.line(roi, (0, y1 + y2//2), (columns, y1 + y2//2), (255, 0, 0), 2)
        break

    frame[80:480, 160:850] = roi
    cv2.imshow('frame', frame)
    cv2.imshow('thresh_roi', threshold)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
