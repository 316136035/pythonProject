import cv2
import numpy as np

# 创建一个显示窗口并设置大小
cv2.namedWindow('Trackbar')
cv2.resizeWindow('Trackbar', 512, 300)

# 创建一个全黑的图像
img = np.zeros((300, 512, 3), np.uint8)

# 定义回调函数，用于获取并可能处理滑动条变动事件
def callback(x):
    # 在这里我们不需要处理，只需在主循环中获取和更新图像
    pass

# 创建RGB三个滑动条并关联回调函数(滑动条名,窗口名,最小值,最大值,回调函数)
cv2.createTrackbar('R', 'Trackbar', 0, 255, callback)
cv2.createTrackbar('G', 'Trackbar', 0, 255, callback)
cv2.createTrackbar('B', 'Trackbar', 0, 255, callback)

while True:
    # 获取当前滑动条的位置作为RGB(滑动条名,窗口名)
    r_val = cv2.getTrackbarPos('R', 'Trackbar')
    g_val = cv2.getTrackbarPos('G', 'Trackbar')
    b_val = cv2.getTrackbarPos('B', 'Trackbar')
    
    # 打印当前的RGB值
    print(r_val, g_val, b_val)
    
    # 更新图像的颜色
    img[:] = [b_val, g_val, r_val]  # BGR顺序是OpenCV中的标准顺序

    # 显示图像
    cv2.imshow('Trackbar', img)

    # 检查按键事件，如果按下Esc键则退出
    key = cv2.waitKey(1)
    if key == 27:  # Esc键的ASCII码是27
        break

# 关闭所有窗口
cv2.destroyAllWindows()