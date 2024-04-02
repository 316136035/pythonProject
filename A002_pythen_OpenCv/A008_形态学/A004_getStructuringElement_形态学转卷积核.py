
from my_package import imagesApi  # 引入自定义包
import cv2  # 导入cv2模块
import numpy as np


img=cv2.imread('././images/erod.png')
image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # 灰度图

while True:
  #主要用于创建形态学操作中使用的结构元素（structuring element），例如膨胀、腐蚀等操作。
  #cv2.MORPH_RECT：矩形结构元素
  #cv2.MORPH_CROSS：十字形结构元素
  #cv2.MORPH_ELLIPSE：椭圆形结构元素
  # 形态学转卷积核    1：结构元素的形状，  2：卷积核大小
  StructuringElement=cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
  # 腐蚀 参数1：原图 2：形态学转卷积核 3：迭代次数
  erode=cv2.erode(image, StructuringElement, iterations=1)
  image= erode
  cv2.imshow("erode", erode)
  cv2.waitKey(1000)





