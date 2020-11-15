import cv2 as cv

img = cv.imread("Lena.png", 1)
img = cv.line(img, (0,0), (255, 255),(255, 0, 0),thickness = 7 )
cv.imshow("Image of ...", img)
cv.waitKey(0)
cv.destroyAllWindows()