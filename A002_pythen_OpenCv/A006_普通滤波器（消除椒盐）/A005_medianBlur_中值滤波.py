from my_package import imagesApi  # 引入自定义包
import cv2  # 导入cv2模块
import numpy as np
from my_package import imagesApi  # 引入自定义包
import cv2  # 导入cv2模块
import numpy as np
img=cv2.imread('././images/salt_and_pepper.png')
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#转换为灰度图
# 对图片进行模糊处理,消除椒盐噪声特别有效，(图像,卷积大小)
# 中值滤波. 参数：图像，核大小
medianBlur=cv2.medianBlur(img,3)
cv2.imshow('img',np.hstack([img,medianBlur]))
cv2.waitKey(5000)










 