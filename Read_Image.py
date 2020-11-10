# Import relevant libraries
import cv2 as cv

# Print an image, remove 0 so that it is not gray-scale
img = cv.imread("Ronaldo-1.jpg", 0)
print(img)

cv.imshow("Image", img)

# Showing a pic of Ronaldo, click any key for it to go away
cv.waitKey()
cv.destroyAllWindows()
