import os
import cv2 as cv
import numpy as np

path = r"C:\Users\lingkong\Documents\LingKong\myUSB"

def cv_imread(file_path = ''):
    file_path_gbk = file_path.encode('gbk')
    img_mat = cv.imread(file_path_gbk.decode())
    print(img_mat)
    return img_mat


#cv.namedWindow('smile', cv.WINDOW_NORMAL)
cv.namedWindow('smile', cv.WINDOW_AUTOSIZE)
#cv.cvResizeWindow('smile', 500, 500)

for path, dir_list, file_list in os.walk(path):
    for file_name in file_list:
        if 'jpg' in file_name or 'JPG' in file_name:
            img_file = os.path.join(path, file_name)
            print(img_file)
            try:
                ##img = cv.imread(im)
                im = cv.imdecode(np.fromfile(img_file, dtype=np.uint8), cv.IMREAD_UNCHANGED)
                #im_gbk = img_file.encode('gbk')
                #img = cv.imread(im_gbk.decode())
                #im = cv_read(img_file)
                cv.imshow('smile', im)
                k = cv.waitKey()
                if k & 0xFF == 27: #ESC key to exit
                    cv.destroyAllWindows()
                    break
            except:
                pass

