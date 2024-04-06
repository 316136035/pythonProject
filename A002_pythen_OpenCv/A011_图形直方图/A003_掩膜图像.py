import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图像并转为灰度图像
img = cv2.imread("./images/A010.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
mask=np.zeros((825, 660),np.uint8) # 生成一个和灰度图像一样大小的矩阵
mask[100:500,100:500]=255 # 创建一个矩形区域


cv2.imshow("img", cv2.bitwise_and(img_gray, mask)) #使用与运算掩膜图像显示

img_calcHist =cv2.calcHist([img ], [0],None, [256], [0, 256])
img_gray_calcHist=cv2.calcHist([img_gray], [0], mask, [256], [0, 256])


# 绘制图像
plt.plot(img_calcHist  ,color='b')
plt.plot(img_gray_calcHist ,color='g')

plt.xlim([0, 250])  # 设置 X 轴显示范围
plt.ylim([0, 20000]) # 设置 Y 轴显示范围
plt.show()
cv2.waitKey(0)


