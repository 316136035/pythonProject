import cv2
import os

cv2.namedWindow('windows', cv2.WINDOW_NORMAL)  # 创建一个窗口 (窗口名称,固定窗口大小-自动调整大小等)
cv2.resizeWindow('windows', 840, 480)  # 调整窗口大小 (窗口名称,宽度，高度)
img = cv2.imread('./images/1.png', cv2.IMREAD_COLOR )  # 读取图片 默认是彩色的
print(img is None)
while True:
    cv2.imshow('windows', img)  # 显示图片)
    key = cv2.waitKey(0)

    if key == ord('\x1b'):  # 按键esc退出
        print('esc退出')
        break
    elif key == ord('s'):
        cv2.imwrite('./1.png', img)  # 保存图片
        break
    else:
        cv2.destroyAllWindows() # 销毁所有窗口
cv2.destroyAllWindows()# 销毁所有窗口
