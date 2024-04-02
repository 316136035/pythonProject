from my_package import imagesApi  # 引入自定义包
import cv2  # 导入cv2模块
import numpy as np

# 获取所有图片
images = imagesApi.return_Image_all()  # 假设这是一个返回图片列表的函数
newImages = []


# 遍历所有图片
for image in images:
    newImage = cv2.Canny(image, 150,100)  # 第一阈值，高于此阈值的强度被认为是边缘候选区 第二阈值，低于此阈值的点会被忽略； 而大于等于第一阈值但小于第二阈值的点仅在连接到强边缘时被标记为边缘。
    # 将处理后的图片添加到列表中

    newImages.append(newImage)
# 显示处理后的图片
imagesApi.show_Image_all(newImages)
