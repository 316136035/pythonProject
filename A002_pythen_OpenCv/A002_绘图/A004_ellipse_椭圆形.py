import cv2
import numpy as np
img = np.zeros((400,400,3), np.uint8) # 创建一个400*400的图像
#创建椭圆 图片,椭圆中心坐标,椭圆长宽,椭圆旋转的角度,椭圆弧线开始起始角度,椭圆弧线结束角度,颜色，线条宽度
cv2.ellipse(img, (200,200), (100,20), 0, 20, 360, (255,255,255), -1 ,16) 
while True:
    cv2.imshow('image',img ) # 显示图像
    k=cv2.waitKey(0) & 0xFF   # 获取键盘输入
    if k==27:
        break
cv2.destroyAllWindows() # 关闭所有窗口