import cv2
import numpy as np

# 创建一个空白图像用于显示
img = np.zeros((500, 500, 3), np.uint8)
# 初始化鼠标按下时的坐标
start_pos = None
# 鼠标事件回调函 事件类型，x、y：鼠标坐标，flags：鼠标按键状态，param：用户自定义参数
def mouse_callback(event, x, y, flags, param):
    global start_pos, img
    if event == cv2.EVENT_LBUTTONDOWN: # 鼠标左键按下
        # 记录鼠标左键按下时的初始坐标
        start_pos = (x, y)
        print("鼠标左键按下时的坐标 X  Y ：", x, y,"flags",flags)
    elif event == cv2.EVENT_MOUSEMOVE and flags & cv2.EVENT_FLAG_LBUTTON: # 鼠标左键移动
        # 如果鼠标左键被按住并移动，则绘制轨迹
        if start_pos is not None:
            cv2.line(img, start_pos, (x, y), (255, 0, 0), 1)  # 绘制轨迹线
            start_pos = (x, y)  # 更新起点为当前坐标
            print("鼠标移动的坐标 X  Y ：", x, y,"flags",flags)
            cv2.imshow('image', img)  # 显示带有轨迹的图像

    elif event == cv2.EVENT_LBUTTONUP:
        # 鼠标左键释放，停止记录轨迹
        start_pos = None



cv2.namedWindow('image')
# 设置鼠标事件函数
cv2.setMouseCallback('image', mouse_callback  ,{"key":"value"})

# 循环显示图像
while True:
    cv2.imshow('image', img) # 显示图像
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # 按Esc键退出
        break

cv2.destroyAllWindows() # 关闭所有窗口