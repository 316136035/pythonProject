import cv2 as cv
import numpy as np
cv.namedWindow("image", cv.WINDOW_AUTOSIZE) # 创建窗口
img= cv.imread("./images/2.jpg") # 读取图片
img=cv.resize(img, [400, 400]) # 改变图片大小
img1 =cv.rotate(img,rotateCode=cv.ROTATE_90_CLOCKWISE) #旋转图像90度顺时针
img2 =cv.rotate(img,rotateCode=cv.ROTATE_90_COUNTERCLOCKWISE) #旋转图像90度逆时针
img3 =cv.rotate(img,rotateCode=cv.ROTATE_180) #旋转图像180度
while True:
    cv.imshow("image", np.hstack([img1,img2,img3]))  # hstack水平拼接图片 vstack垂直拼接图片
    k = cv.waitKey(0) & 0xFF
    if k == 27:
        break


cv.destroyAllWindows() # 销毁所有窗口