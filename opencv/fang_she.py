import cv2 as cv
import numpy as np

img = cv.imread('elephant.jpg')

M_crop_elephant = np.array([
    [2, 0, -150], 
    [0, 2, -240]
], dtype=np.float32)

img_sheared = cv.warpAffine(img, M_crop_elephant, (int(1001*2), 1334))
cv.imwrite('elephant_sheared.jpg', img_sheared)

# x轴的剪切变换，角度15°
theta = 15 * np.pi / 180
M_shear = np.array([
    [1, np.tan(theta), 0],
    [0, 1, 0]
], dtype=np.float32)

img_sheared = cv.warpAffine(img, M_shear, (400, 600))
cv.imwrite('elephant_sheared.jpg', img_sheared)

# 顺时针旋转，角度15°
M_rotate = np.array([
    [np.cos(theta), -np.sin(theta), 0],
    [np.sin(theta), np.cos(theta), 0]
], dtype=np.float32)

img_rotated = cv.warpAffine(img, M_rotate, (400, 600))
cv.imwrite('elephant_rotated.jpg', img_rotated)

# 某种变换，具体旋转+缩放+旋转组合可以通过SVD分解理解
M = np.array([
    [1, 1.5, -400],
    [0.5, 2, -100]
], dtype=np.float32)

img_transformed = cv.warpAffine(img, M, (400, 600))
cv.imwrite('elephant_transformed.jpg', img_transformed)
