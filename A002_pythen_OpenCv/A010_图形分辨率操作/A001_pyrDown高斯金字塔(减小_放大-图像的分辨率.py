import cv2
import numpy as np

# 读取图像
img = cv2.imread("./images/A010.jpg")
# 高斯金字塔 减小图像的分辨率
pyrDownImg=cv2.pyrDown(img)
# 高斯金字塔 放大图像的分辨率
pyrUpImg=cv2.pyrUp(img)
cv2.imshow("Img",img )
cv2.imshow("pyrDownImg",pyrDownImg)
cv2.imshow("pyrUpImg",pyrUpImg)
cv2.waitKey(5000)



