
from my_package import imagesApi  # 引入自定义包
import cv2  # 导入cv2模块
import numpy as np

# 获取所有图片
images = imagesApi.return_Image_all()  # 假设这是一个返回图片列表的函数
newImages = []
imagesApi.show_Image_all(images)

# 遍历所有图片
for image in images:
  # cv2.THRESH_BINARY:
# 当像素值大于或等于阈值时，像素值被设置为 maxVal（例如，通常是255代表白色）。
# 当像素值小于阈值时，像素值被设置为0（黑色）。
# 创建了一个传统的黑白二值图像。
# cv2.THRESH_BINARY_INV:
# 类似于二值阈值，但是逻辑取反。
# 当像素值大于或等于阈值时，像素值被设置为0（黑色）。
# 当像素值小于阈值时，像素值被设置为 maxVal（白色）。
# 创建了一个黑白翻转的二值图像。
# cv2.THRESH_TRUNC:
# 当像素值大于阈值时，像素值被裁剪为阈值本身。
# 当像素值小于或等于阈值时，像素值保持不变。
# 图像中超过阈值的部分变为阈值，低于阈值的部分保留原始值。
# cv2.THRESH_TOZERO:
# 当像素值大于或等于阈值时，像素值保持不变。
# 当像素值小于阈值时，像素值被设置为0。
# 图像中小于阈值的部分变为0，大于阈值的部分保留原始值。
# cv2.THRESH_TOZERO_INV:
# 类似于 cv2.THRESH_TOZERO，但逻辑取反。
# 当像素值大于或等于阈值时，像素值被设置为0。
# 当像素值小于阈值时，像素值保持不变。
# 图像中大于阈值的部分变为0，低于阈值的部分保留原始值。
# cv2.THRESH_OTSU:
# 不是单独使用，而是与其他阈值类型结合使用，例如 cv2.THRESH_BINARY + cv2.THRESH_OTSU。
# Otsu's二值化方法会自动计算出一个最优的全局阈值，以最大程度地提高前景和背景像素之间的类间方差。
# 在这种情况下，thresh 参数不再是你直接指定的阈值，而是程序会自动计算阈值。
  # 二值化:灰度图像,阈值,最大值,阈值类型（请求查看上面）
  _,newImage= cv2.threshold( image, 100, 255, cv2.THRESH_BINARY)
  newImages.append(newImage)
# 显示处理后的图片
imagesApi.show_Image_all(newImages)
