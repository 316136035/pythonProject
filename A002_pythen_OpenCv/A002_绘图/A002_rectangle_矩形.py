import cv2
import numpy as np
cv2.namedWindow("image") # 创建一个窗口
cv2.resizeWindow("image", 600, 600) # 设置窗口大小
img = np.zeros((400,400,3), np.uint8) # 创建一个400*400的图像
#画矩形(图片,(开始坐标xy),(结束坐标xy),(BGR颜色),线型大小,像素位置的偏移值) （当线宽为-1时，表示填充全部）
cv2.rectangle(img, (50,50), (300,300), (255,0,0), -1,16)
while True:
    cv2.imshow('image',img ) # 显示图像
    k=cv2.waitKey(0) & 0xFF   # 获取键盘输入
    if k==27:
        break
cv2.destroyAllWindows() # 关闭所有窗口