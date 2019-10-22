import numpy as np
import cv2
import matplotlib.pyplot as plt

color_img = cv2.imread('introduction.jpg')
print(color_img.shape)

gray_img = cv2.imread('introduction.jpg', cv2.IMREAD_GRAYSCALE)
print(gray_img.shape)

cv2.imwrite('test_grayscale.jpg', gray_img)
reload_grayscale = cv2.imread('test_grayscale.jpg')
print(reload_grayscale.shape)

cv2.imwrite('test_imwrite.jpg', color_img, (cv2.IMWRITE_JPEG_QUALITY, 80))
cv2.imwrite('test_imwrite.png', color_img, (cv2.IMWRITE_PNG_COMPRESSION, 5))
