import cv2 as cv
import os
import sys

detector = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

cv.namedWindow('pictures', cv.WINDOW_NORMAL)

for path, dir_list, file_list in os.walk('.'):
    for file_name in file_list:
        if ("JPG" in file_name or 'jpg' in file_name) and 'gray' not in file_name:
            #img_file = os.path.join(path, file_name)
            img_file = file_name
            print(img_file)

            file_name, file_ext = os.path.splitext(img_file)
            gray_file_name = '%s_gray%s' % (file_name, file_ext)

            img = cv.imread(img_file)
            print('size, dtype, shape', img.size, img.dtype, img.shape)
            #img = cv.resize(img, (1000, 500))
            img = cv.resize(img, (int(img.shape[1] * 0.8), int(img.shape[0] * 0.8)))

            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            cv.imwrite(gray_file_name, gray)
            #img_gray = cv.imread('gray_2564.jpg')
            #cv.imshow('gray', img_gray)

            faces = detector.detectMultiScale(gray, 1.3, 5)
            print(faces)

            for (x, y, w, h) in faces:
                cv.rectangle(img, (x, y), (x+w, y+h), (250, 0, 0), 2)

            cv.imshow('pictures', img)
            #cv.resizeWindow('pictures', 1920, 1080)
            cv.setWindowProperty('pictures', cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)
            #cv.imshow('gray', img_gray)
            cv.waitKey(0)
            cv.destroyAllWindows()
