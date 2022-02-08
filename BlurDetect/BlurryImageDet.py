import cv2

image = cv2.imread('test1.jpg')
image = cv2.resize(image, (600, 400))
blur_image = cv2.medianBlur(image, 7)

laplacian = cv2.Laplacian(image, cv2.CV_64F).var()
laplacian_blur = cv2.Laplacian(blur_image, cv2.CV_64F).var()
print(laplacian)
print(laplacian_blur)


""" 
cv2.imshow('image', image)
cv2.imshow('Blurry image', blur_image)
 """

cv2.waitKey(0)
cv2.destroyAllWindows()
