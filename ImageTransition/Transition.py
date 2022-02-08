import cv2

def nothing(x):
    pass

image1 = cv2.imread('test1.jpg')
image1 = cv2.resize(image1, (500, 500))
image2 = cv2.imread('test2.png')
image2 = cv2.resize(image2, (500, 500))

output = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)

window_name = 'Transition'
cv2.namedWindow(window_name)
cv2.createTrackbar('Alpha-Beta', window_name, 0, 100, nothing)

while True:
    cv2.imshow(window_name, output)
    alpha = cv2.getTrackbarPos('Alpha-Beta', window_name)
    alpha /= 100
    beta = 1 - alpha
    output = cv2.addWeighted(image1, alpha, image2, beta, 0)
    if cv2.waitKey(1) == 27:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
