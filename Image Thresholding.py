import cv2 as cv

image = cv.imread("Gradient.jpg")
#_, th0 = cv.threshold(image, 50, 255, cv.THRESH_BINARY)
#_, th0 = cv.threshold(image, 50, 255, cv.THRESH_BINARY_INV)
#_, th0 = cv.threshold(image, 50, 255, cv.THRESH_TRUNC)
_, th0 = cv.threshold(image, 50, 255, cv.THRESH_TOZERO)

cv.imshow("Image", image)
cv.imshow("New Image", th0)

cv.waitKey(0)
cv.destroyAllWindows()