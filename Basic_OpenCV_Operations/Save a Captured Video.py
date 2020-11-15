import cv2 as cv

cap = cv.VideoCapture(0) # No camera installed/activated at cpu, also for storage on GitHub
FourCC = cv.VideoWriter_fourcc(*"XVID")
output = cv.VideoWriter("Output.avi", FourCC, 20.0, (640, 480))

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

        output.write(frame)

        cv.imshow("Frame", frame)

        if cv.waitKey(1) & 0xFF == ord("e"):
            break

cap.release()
output.release()
cv.destroyAllWindows()