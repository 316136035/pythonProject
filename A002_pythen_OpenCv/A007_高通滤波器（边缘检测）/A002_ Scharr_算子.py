from my_package import imagesApi  # 引入自定义包
import cv2  # 导入cv2模块
import numpy as np

# 获取所有图片
images = imagesApi.return_Image_all()  # 假设这是一个返回图片列表的函数
newImages = []


# 遍历所有图片
for image in images:
    #它基于Scharr梯度算子，该算子设计用于提供比标准Sobel算子更准确的边缘方向估计，特别是在近似45度角的方向上
    # 对图片进行卷积操作(图片，输出图像的深度，x 轴和 ，y 轴，缩放因子)
    # newImage=cv2.Scharr(image, cv2.CV_64F,dx=1,dy=0, scale=1) 垂直方向不见了
    newImage = cv2.Scharr(image, cv2.CV_64F, dx=0, dy=1, scale=1)  # 水平方向不见了
    # 将处理后的图片添加到列表中
    newImages.append(newImage)
# 显示处理后的图片
imagesApi.show_Image_all(newImages)
