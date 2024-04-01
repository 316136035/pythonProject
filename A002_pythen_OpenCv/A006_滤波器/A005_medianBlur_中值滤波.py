from my_package import imagesApi  # 引入自定义包
import cv2  # 导入cv2模块
import numpy as np

# 获取所有图片
images = imagesApi.return_Image_all()  # 假设这是一个返回图片列表的函数
newImages = []

# 遍历所有图片
for image in images:
    # 对图片进行模糊处理,消除椒盐噪声特别有效，(图像,卷积大小)
    newImage = cv2.medianBlur( image , 5)
    # 将处理后的图片添加到列表中
    newImages.append(newImage)
# 显示处理后的图片
imagesApi.show_Image_all(newImages)
