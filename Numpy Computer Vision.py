import numpy as np
import cv2 as cv

# Creating a black image with numpy matrix
img = np.zeros([512, 512, 3], np.uint8)
cv.imshow("Image", img)
cv.waitKey(0)
cv.destroyAllWindows()

# Handle Mouse Click Events
#events = [i for i in dir(cv) if "EVENT" in i]
#print(events)

def click_event(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x, ", ", y)
        font = cv.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ", " + str(y)
        cv.putText(img, strXY, (x, y), font, 1, (0,0,255), 2)
        cv.imshow("Image", img)

img = np.zeros([500, 500, 3], np.uint8)
cv.imshow("Image", img)
cv.setMouseCallback("Image", click_event)

cv.waitKey(0)
cv.destroyAllWindows()