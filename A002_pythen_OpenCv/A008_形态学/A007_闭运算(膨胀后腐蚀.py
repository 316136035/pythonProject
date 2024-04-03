
from my_package import imagesApi  # 引入自定义包
import cv2  # 导入cv2模块
import numpy as np


img=cv2.imread('././images/A007.jpg')

image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # 灰度图


  #必须是黑白图，二值化的图片
 # 形态学转卷积核    1：结构元素的形状，  2：卷积核大小
StructuringElement=cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
# 开运算 先膨胀，再腐蚀 先膨胀白色在腐蚀白色（作用在消除外面的噪声）
# morphologyEx函数体（形态学图像处理操作）采参数：1：原图，2：操作类型，3：卷积核，4：迭代次数
erode=cv2.morphologyEx(image,cv2.MORPH_CLOSE,StructuringElement, iterations=4)
cv2.imshow("erode", np.hstack([image, erode]))
cv2.waitKey(5000)




