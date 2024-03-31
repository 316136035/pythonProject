import cv2  as cv
import numpy as np
cv.namedWindow("image",cv.WINDOW_AUTOSIZE) # 窗口大小自适应
img= cv.imread("./images/2.jpg") # 读取图片
img=cv.resize(img, [400, 400]) # 改变图片大小
# 水平翻转
img1= cv.flip(img, 0)
# 垂直翻转
img2= cv.flip(img, 1)
# 水平和垂直同时翻转
img3 = cv.flip(img, -1)
while True:
    cv.imshow("image", np.hstack([img,img1,img2,img3]))  # hstack水平拼接图片 vstack垂直拼接图片
    k = cv.waitKey(0) & 0xFF
    if k == 27:
        break


cv.destroyAllWindows() # 销毁所有窗口
