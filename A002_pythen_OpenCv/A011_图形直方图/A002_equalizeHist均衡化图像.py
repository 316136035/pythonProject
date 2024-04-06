import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图像并转为灰度图像
img = cv2.imread("./images/A010.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



img_back =img_gray-40
img_bright =img_gray+40
cv2.imshow("Bright Image", np.hstack((img_gray,img_back,img_bright)))
cv2.waitKey(0)

# 计算灰度图像的直方图  三通道
#  参数：图像，通道，ROI，直方图大小，范围
img_gray_calcHis= cv2.calcHist([img_gray], [0], None, [256], [0, 255])
img_back_calcHis = cv2.calcHist([img_back ], [0], None, [256], [0, 255])
img_bright_calcHis= cv2.calcHist([img_bright], [0], None, [256], [0, 255])

# 均衡化处理
img_back =cv2.equalizeHist(img_back )
img_bright =cv2.equalizeHist(img_bright)
cv2.imshow("Bright Image", np.hstack((img_gray,img_back,img_bright)))
cv2.waitKey(0)


# 绘制图像
plt.plot(img_gray_calcHis ,color='b')
plt.plot(img_back_calcHis ,color='g')
plt.plot(img_bright_calcHis ,color='r')
plt.xlim([0, 250])  # 设置 X 轴显示范围
plt.ylim([0, 20000]) # 设置 Y 轴显示范围


plt.legend(('B','G','R'))
plt.show()

