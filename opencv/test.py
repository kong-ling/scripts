import cv2 as cv
import time

imgs = ["introduction.jpg", "Histogram_Calculation_Tutorial_Cover.jpg", "Remap_Tutorial_Cover.jpg", "introduction.jpg"]

for image in imgs:
    print(image)
    img = cv.imread('C:\posv_cv_script-scripts\opencv\%s' % image)
    cv.namedWindow("Image")
    cv.imshow("Image",img)
    time.sleep(3)
    break
#cv.waitKey(0)
#释放窗口
#cv2.destroyAllWindows()
img = cv.imread('C:\posv_cv_script-scripts\opencv\intruction.jpg')
cv.namedWindow("Image")
cv.imshow("Image",img)
