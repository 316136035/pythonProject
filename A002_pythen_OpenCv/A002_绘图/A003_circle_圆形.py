import cv2 
import numpy as np
img = np.zeros((400,400,3), np.uint8) # 创建一个400*400的图像
# 画一个圆形 图像,圆心坐标XY,圆的半径,绘制圆形的颜色,线宽,(可选): 线型标志(可选),:像素位置的偏移值
cv2.circle(img, (200,200), 100, (0,0,255), -1 ,16)
while True:
    cv2.imshow('image',img ) # 显示图像
    k=cv2.waitKey(0) & 0xFF   # 获取键盘输入
    if k==27:
        break
cv2.destroyAllWindows() # 关闭所有窗口