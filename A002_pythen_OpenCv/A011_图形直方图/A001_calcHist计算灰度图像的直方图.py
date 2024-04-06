import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图像并转为灰度图像
img = cv2.imread("./images/A010.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("GImage", img)
cv2.imshow("Gray Image", img_gray)
cv2.waitKey(0)

# 计算灰度图像的直方图  单通道
#  参数：图像，通道，ROI，直方图大小，范围
hist_gray = cv2.calcHist([img_gray], [0], None, [256], [0, 255])
plt.hist(hist_gray)
plt.show()


# 计算灰度图像的直方图  三通道
#  参数：图像，通道，ROI，直方图大小，范围
hist_gray1 = cv2.calcHist([img], [0], None, [256], [0, 255])
hist_gray2 = cv2.calcHist([img], [1], None, [256], [0, 255])
hist_gray3 = cv2.calcHist([img], [2], None, [256], [0, 255])
# 绘制图像
plt.plot(hist_gray1 ,color='b')
plt.plot(hist_gray2 ,color='g')
plt.plot(hist_gray3 ,color='r')
plt.xlim([0, 250])  # 设置 X 轴显示范围

plt.legend(('B','G','R'))
plt.show()

