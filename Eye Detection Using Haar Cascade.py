import cv2 as cv
i = input("Put in part of body to detect.")
if i == "eye":
    eyeCascade = cv.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")
    img = cv.imread("Ronaldo-1.jpg")
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    eyeDetect = eyeCascade.detectMultiScale(gray_img, 1.1, 4)

    for (x, y, w, h) in eyeDetect:
        cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), thickness=2)

    cv.imshow("Image", img)
    cv.waitKey(0)
elif i == "face":
    faceCascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
    img = cv.imread("Ronaldo-1.jpg")
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faceDetect = faceCascade.detectMultiScale(gray_img, 1.1, 4)

    for (x, y, w, h) in faceDetect:
        cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), thickness=2)

    cv.imshow("Image", img)
    cv.waitKey(0)
else:
    pass
