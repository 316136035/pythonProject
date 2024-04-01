from my_package import imagesApi  # 引入自定义包
import cv2  # 导入cv2模块
import numpy as np

# 获取所有图片
images = imagesApi.return_Image_all()  # 假设这是一个返回图片列表的函数
newImages = []


# 遍历所有图片
for image in images:
    # 更好地保留图像的边缘和细节，尤其适合去除噪声的同时保持边缘清晰。
    # （图像，滤波器直径必须为正奇数，颜色空间的标准差，坐标空间的标准差）
    newImage = cv2.bilateralFilter(image, d=3, sigmaColor=1, sigmaSpace=3)
    newImage = cv2.Canny(newImage, 20,50)  # 边缘检测改变阈值 数值越大检测到的边缘越少
    # 将处理后的图片添加到列表中

    newImages.append(newImage)
# 显示处理后的图片
imagesApi.show_Image_all(newImages)
