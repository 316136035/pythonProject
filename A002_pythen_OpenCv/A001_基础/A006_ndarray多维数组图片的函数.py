import cv2 
import numpy as np
cv2.namedWindow('image', cv2.WINDOW_NORMAL) #创建窗口大小可变
cv2.resizeWindow('image',1350, 600) #窗口大小
img=cv2.imread('./images/1.png') #读取图片


print(img.dtype) #数据类型
print(img.size) #像素点个数
print(img.shape) #图像尺寸
print(img.ndim) #图像维度（颜色通道 BGR）
img1=img.view() #浅拷贝图片 （地址一样）
img2=img.copy() #深拷贝图片 （地址不一样创建的新图片）


#[100:200, 100:300, :]是一个切片操作，分别指定了高度（从第100行到第299行）、宽度（从第100列到第299列）以及通道（:, 表示所有通道）。
#[50,60,0]  代表颜色通道RGB的值  设置b,g,r  b蓝色  g绿色 r红色
img[100:200, 100:300, :] = [50,60,10]  
while True:
     #python中把图片mat转化成了ndarray（多维数组的图片）
    cv2.imshow('image', np.hstack((img, img1, img2)))  #hstack水平拼接图片 vstack垂直拼接图片 
    #cv2.imshow('image', img)
    key =cv2.waitKey(0)
    if key == ord('\x1b'):  # 按键esc退出
        break
cv2.destroyAllWindows() #销毁所有窗口




