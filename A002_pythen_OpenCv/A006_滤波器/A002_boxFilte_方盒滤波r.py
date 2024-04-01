from my_package import imagesApi  # 引入自定义包
import cv2  # 导入cv2模块
import numpy as np

# 获取所有图片
images = imagesApi.return_Image_all()  # 假设这是一个返回图片列表的函数
newImages = []

# 遍历所有图片
for image in images:
    # 用来平滑图像或者减小噪声
    # 对图片进行盒式滤波器操作(图片，输出图像的深度，卷积核,)
    # normalize：布尔值，若为True，会对滤波结果进行归一化，使得滤波器系数总和为1；若为False，则不会进行归一化，直接对像素块进行求和。
    newImage = cv2.boxFilter(image, -1, (3, 3), normalize=True)
    # 将处理后的图片添加到列表中
    newImages.append(newImage)
# 显示处理后的图片
imagesApi.show_Image_all(newImages)
