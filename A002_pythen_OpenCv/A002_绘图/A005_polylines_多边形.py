import cv2
import numpy as np

# 创建一个黑色背景的图像
img = np.zeros((500, 500, 3), dtype=np.uint8)

# 定义一个多边形的顶点 必须是np.int32以上
polygon_pts = np.array([[100, 100], [200, 50], [300, 150], [150, 200]],np.int32)

# 使用cv2.polylines()绘制多边形，并闭合图形,颜色，线的宽度
cv2.polylines(img, [polygon_pts], True, (0, 255, 0), thickness=2)
while True:
    cv2.imshow('img ',img ) # 显示图像
    k=cv2.waitKey(0) & 0xFF   # 获取键盘输入
    if k==27:
        break
cv2.destroyAllWindows() # 关闭所有窗口