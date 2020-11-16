import cv2 as cv

img = cv.imread("Ball.jpg")
img = cv.rectangle(img, (455, 205), (700, 445), (255, 0, 0), 7)
img = cv.rectangle(img, (10,10), (255, 250), (0, 0, 255), 7)

myImg = img[205:445, 455:700]
img[10:250, 10:255] = myImg

cv.imshow("Image", img)
cv.waitKey(0)
cv.destroyAllWindows()