from my_package import imagesApi  # 引入自定义包
import cv2  # 导入cv2模块
import numpy as np

# 获取所有图片
images = imagesApi.return_Image_all()  # 假设这是一个返回图片列表的函数
newImages = []


# 遍历所有图片
for image in images:
    #拉普拉斯算子能同时考虑图像局部的水平、垂直以及对角方向的变化，因此它可以检测出图像中灰度变化率较大的区域，即边缘和角落
    newImage = cv2.Laplacian(image, cv2.CV_64F,ksize=3)
    # 将处理后的图片添加到列表中
    newImages.append(newImage)
# 显示处理后的图片
imagesApi.show_Image_all(newImages)
