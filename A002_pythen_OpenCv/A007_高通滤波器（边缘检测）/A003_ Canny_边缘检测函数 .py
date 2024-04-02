from my_package import imagesApi  # 引入自定义包
import cv2  # 导入cv2模块
import numpy as np

# 获取所有图片
images = imagesApi.return_Image_all()  # 假设这是一个返回图片列表的函数
newImages = []


# 遍历所有图片
for image in images:
    image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) # 灰度图
    # 对图片进行模糊处理,消除椒盐噪声特别有效，(图像,卷积大小)
    # 中值滤波. 参数：图像，核大小
    medianBlur=cv2.medianBlur(image,3)
     # 第一阈值，高于此阈值的强度被认为是边缘候选区 第二阈值，低于此阈值的点会被忽略； 而大于等于第一阈值但小于第二阈值的点仅在连接到强边缘时被标记为边缘。
    newImage = cv2.Canny( medianBlur,10,50) 
    # 将处理后的图片添加到列表中
    newImages.append(newImage)
# 显示处理后的图片
imagesApi.show_Image_all(newImages)
