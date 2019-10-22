import cv2 as cv
import os
import sys

detector = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

cv.namedWindow('pictures', cv.WINDOW_NORMAL)

img_file = '2564.jpg'
img = cv.imread(img_file)
print('size, dtype, shape', img.size, img.dtype, img.shape)
print(img)

for l in img.shape[1]:
    print(img[l])


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imwrite('gray_2564.jpg', gray)
img_gray = cv.imread('gray_2564.jpg')
#cv.imshow('gray', img_gray)

faces = detector.detectMultiScale(gray, 1.3, 5)
print(faces)

for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x+w, y+h), (250, 0, 0), 2)

cv.imshow('pictures', img)
#cv.imshow('gray', img_gray)
cv.waitKey(0)
cv.destroyAllWindows()
