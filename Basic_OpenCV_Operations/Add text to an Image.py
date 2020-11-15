import cv2 as cv

img = cv.imread("lena.png", 1)
font = cv.FONT_HERSHEY_SIMPLEX
img = cv.putText(img, "Lena", (0, 100), font, 2.5, (255, 200,0), 3, cv.LINE_AA)
cv.imshow("Image", img)
cv.waitKey(0)
cv.destroyAllWindows()