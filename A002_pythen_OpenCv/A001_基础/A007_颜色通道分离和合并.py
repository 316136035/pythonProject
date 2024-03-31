import cv2
import numpy as np
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 600, 600)
img1=np.zeros((800,800,3),np.uint8)

b,g,r= cv2.split(img1)

# #[100:200, 100:300, :]是一个切片操作，分别指定了高度（从第100行到第299行）、宽度（从第100列到第299列）以及通道（:, 表示所有通道）。  
# 设置b,g,r  b蓝色  g绿色 r红色
b[10:100,10:200 ]=100
g[10:100,10:200 ]=0
r[110:100,10:200]=20

img2=cv2.merge((b,g,r))
while True:
    cv2.imshow('image',img2)
    k=cv2.waitKey(0) & 0xFF
    if k==27:
        break
  

cv2.destroyAllWindows()