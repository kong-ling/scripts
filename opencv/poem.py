import numpy as np
import cv2

# 定义一块宽600，高400的画布，初始化为白色
canvas = np.zeros((400, 600, 3), dtype=np.uint8) + 255
# 在左半部分最上方打印文字
poem_sentences = [
    'first', 'second', 'third', 'forth',
]

for i, sen in enumerate(poem_sentences):
    cv2.putText(canvas,
                #'Python-OpenCV Drawing Example',
                sen,
                (5+15*i, 15+15*i),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 0, 0),
                1)
cv2.imshow('Example of basic drawing functions', canvas)
cv2.waitKey()
