import os
import cv2 as cv
img = cv.imread('elephant.jpg')
key = 0
while key != 27:
    cv.imshow('elephant', img)
    key = cv.waitKey()

    msg = '{} is pressed'.format(chr(key) if key < 256 else key)
    print(msg)
