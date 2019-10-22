import numpy as np
import cv2 as cv

cap=cv.VideoCapture('test1.avi')
while (cap.isOpened()):
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)
    #hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    #cv.imshow('frame', hsv)
    if cv.waitKey(100) & 0xff == ord('q'):
        break

cap.release()
cv.distroyAllWindows()
