import cv2 as cv
from PIL import Image
import numpy as np

img = cv.imread('2564.jpg')
cv.imshow('opencv', img)

image = Image.fromarray(cv.cvtColor(img, cv.COLOR_BGR2RGB))

image.show()
cv.waitKey()


image = Image.open('2564.jpg')
image.show()

img = cv.cvtColor(np.asarray(image), cv.COLOR_RGB2BGR)
cv.imshow('openv', img)
cv.waitKey()
