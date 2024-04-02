
from my_package import imagesApi  # 引入自定义包
import cv2  # 导入cv2模块
import numpy as np


img=cv2.imread('././images/erod.png')
image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # 灰度图
while True:
  # 腐蚀 参数1：原图 2：卷积核 3：迭代次数
  erode=cv2.erode(image, np.ones((3, 3), np.uint8), iterations=1)
  image= erode
  cv2.imshow("erode", erode)
  cv2.waitKey(1000)




