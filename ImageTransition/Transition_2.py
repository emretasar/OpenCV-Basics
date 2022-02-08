import cv2

def nothing(x):
    pass

out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (500,500))
image1 = cv2.imread('test1.jpg')
image1 = cv2.resize(image1, (500, 500))
image2 = cv2.imread('test2.png')
image2 = cv2.resize(image2, (500, 500))

alpha_per = 0
while alpha_per < 100:
    alpha = alpha_per / 100
    beta = 1 - alpha
    output = cv2.addWeighted(image1, alpha, image2, beta, 0)
    out.write(output)
    alpha_per += 1
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()