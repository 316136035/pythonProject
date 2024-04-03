
import cv2  # 导入cv2模块
import numpy as np


img=cv2.imread('././images/erod.png')
image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # 灰度图
while True:
  #必须是黑白图，二值化的图片
  # 膨胀白色部分 参数1：原图 2：卷积核 3：迭代次数
  erode=cv2.dilate(image,np.ones((5,5),np.uint8),iterations=1)
  image= erode
  cv2.imshow("erode", erode)
  cv2.waitKey(1000)




