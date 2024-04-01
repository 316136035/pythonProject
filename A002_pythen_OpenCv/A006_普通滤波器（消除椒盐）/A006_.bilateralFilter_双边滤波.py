from my_package import imagesApi  # 引入自定义包
import cv2  # 导入cv2模块
import numpy as np
from my_package import imagesApi  # 引入自定义包
import cv2  # 导入cv2模块
import numpy as np
img=cv2.imread('././images/salt_and_pepper.png')
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#转换为灰度图
   # 更好地保留图像的边缘和细节，尤其适合去除噪声的同时保持边缘清晰。
    #（图像，滤波器直径必须为正奇数，颜色空间的标准差，坐标空间的标准差）
bilateralFilter=cv2.bilateralFilter(img, 9, 75, 75)
cv2.imshow('img',np.hstack([img,bilateralFilter]))
cv2.waitKey(5000)


 