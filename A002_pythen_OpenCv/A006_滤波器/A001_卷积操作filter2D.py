from my_package import imagesApi #引入自定义包
import cv2 #导入cv2模块
import numpy as np
# 获取所有图片
images = imagesApi.return_Image_all()  # 假设这是一个返回图片列表的函数
newImages = []
  #定义一个3x3的均值滤波器
# kerne = np.ones((3,3),np.float32)
# 定义一个3x3的卷积核
kerne1 = np.array([[-1, -1, -1], [-1, 10, -1], [-1, 0, -1]])  # 显示突出轮廓
kerne2 = np.array([[-2, -1, 0], [-1,1, 1], [0, 1,2]])  #  显示浮雕效果
kerne3 = np.array([[0,-1,0], [-1, 5, -1], [0, -1, 0]])  # 显示锐化效果
# 遍历所有图片
for image in images:
  # 对图片进行卷积操作(图片，输出图像的深度，卷积核)
    newImage=cv2.filter2D( image ,-1,kerne1)
    # 将处理后的图片添加到列表中
    newImages.append(newImage)
# 显示处理后的图片
imagesApi.show_Image_all(newImages )
