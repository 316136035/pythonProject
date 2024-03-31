import cv2

cv2.namedWindow("视频数据", cv2.WINDOW_NORMAL)  # 创建窗口
cv2.resizeWindow("视频数据", 800, 600)  # 调整窗口大小
# camera = cv2.VideoCapture(0)  # 获取摄像头
camera = cv2.VideoCapture("./images/1.mp4")  # 获取视频
while camera.isOpened():  # 判断摄像头是否打开并循环读取数据
    ret, frame = camera.read()  # 读取摄像头数据 # ret为布尔值，frame为返回的每一帧图像数据
    if not ret: # 如果读取失败，则跳出循环
        break
    elif ret: # 如果读取成功，则显示图像
        print("读取成功")
        cv2.imshow("视频数据", frame) # 显示图像

    else:
        print("读取失败") # 跳出循环
        break

    key = cv2.waitKey(1)
    if key == ord('\x1b'):  # 按键esc退出
        print('esc退出')
        break
camera.release()  # 释放摄像头
cv2.destroyAllWindows()  # 销毁所有窗口
