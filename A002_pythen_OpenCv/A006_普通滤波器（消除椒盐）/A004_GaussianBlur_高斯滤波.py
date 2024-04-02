from my_package import imagesApi  # 引入自定义包
import cv2  # 导入cv2模块
import numpy as np
img=cv2.imread('././images/salt_and_pepper.png')
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#转换为灰度图
#常用于降噪、平滑图像或减少图像细节
# 高斯滤波 参数：图像，核大小，标准差 
GaussianBlur=cv2.GaussianBlur(img,(3,3),sigmaX=0,sigmaY=0)

cv2.imshow('img',np.hstack([img,GaussianBlur]))
cv2.waitKey(5000)

