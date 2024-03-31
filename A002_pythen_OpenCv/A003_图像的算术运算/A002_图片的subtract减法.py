import cv2
import numpy as np
cv2.namedWindow('image') #创建窗口
cv2.resizeWindow('image', 600, 600) #设置窗口大小

img2=cv2.imread('./images/2.jpg') #读取图片
img3=cv2.imread('./images/3.jpg') #读取图片
print("原有图片大小",img2.shape,"      ",img3.shape) #打印图片大小
img2=cv2.resize(img2,(800,600),cv2.INTER_AREA) #修改图片大小
img3=cv2.resize(img3,(800,600),cv2.INTER_AREA) #修改图片大小
print("修改后图片大小",img2.shape,"      ",img3.shape)

img2+=10 #加法(修改每个像素值 相当于加10 当前图片像素值大于255时 相当于当前值%255   显示280%255=25像素值)
img3-=200#减法(修改每个像素值) 相当于减200 当前图片像素值小于255时  

#使用加减法之前要将图片转换为一样大小 当前图片大小不一样时，使用add()函数会报错 
# cv2.subtract()函数 默认是饱和相加，
img4=cv2.subtract(img2,img3)

while True:
    cv2.imshow('image', np.hstack([img2,img3,img4]))  #hstack水平拼接图片 vstack垂直拼接图片 
    k=cv2.waitKey(0) & 0xFF
    if k==27:
        break
  
cv2.destroyAllWindows() #关闭所有窗口