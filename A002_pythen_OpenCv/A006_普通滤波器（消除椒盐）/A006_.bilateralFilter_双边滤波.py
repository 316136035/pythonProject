from my_package import imagesApi  # 引入自定义包
import cv2  # 导入cv2模块
import numpy as np
from my_package import imagesApi  # 引入自定义包
import cv2  # 导入cv2模块
import numpy as np
img=cv2.imread('././images/salt_and_pepper.png')
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#转换为灰度图
#持边缘的锐利性，尤其适用于保持图像细节的情况下进行降噪处理（消除椒盐噪声特不好）
#灰色图像，75为灰度窗口大小，75为高斯核标准差
bilateralFilter=cv2.bilateralFilter(img,3,75, 75)
cv2.imshow('img',np.hstack([img,bilateralFilter]))
cv2.waitKey(5000)


 