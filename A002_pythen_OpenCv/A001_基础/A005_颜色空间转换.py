import cv2
import numpy as np

cv2.namedWindow("color_space_conversion", cv2.WINDOW_NORMAL)
cv2.resizeWindow("color_space_conversion", 600, 600)
img = cv2.imread('./images/1.png', cv2.IMREAD_COLOR )  # 读取图片 默认是彩色的

# 以下是一些常用的色彩空间转换常量
color_lists= [
    # 将BGR图像转换为灰度图像
    cv2.IMREAD_COLOR, #读取图片 默认是彩色的
    cv2.COLOR_BGR2GRAY,  # "从BGR色彩空间转换到灰度",
    cv2.COLOR_BGR2RGB,  # ""从BGR色彩空间转换到RGB",
    cv2.COLOR_BGR2HSV,  # ""从BGR色彩空间转换到HSV色彩空间",
    cv2.COLOR_BGR2HLS,  # ""从BGR色彩空间转换到HLS色彩空间",
    cv2.COLOR_BGR2YUV,  # ""从BGR色彩空间转换到YUV色彩空间",
    cv2.COLOR_BGR2YCrCb,  # ""从BGR色彩空间转换到YCrCb色彩空间",
    cv2.COLOR_BGR2LAB,  # ""从BGR色彩空间转换到CIELAB色彩空间",
    cv2.COLOR_RGB2GRAY,  # ""从RGB色彩空间转换到灰度",
    cv2.COLOR_RGB2HSV,  # ""从RGB色彩空间转换到HSV色彩空间",
    cv2.COLOR_RGB2HLS,  # ""从RGB色彩空间转换到HLS色彩空间",
    cv2.COLOR_RGB2YUV,  # ""从RGB色彩空间转换到YUV色彩空间",
    cv2.COLOR_RGB2YCrCb,  # ""从RGB色彩空间转换到YCrCb色彩空间",
    cv2.COLOR_RGB2LAB,  # ""从RGB色彩空间转换到CIELAB色彩空间",
    cv2.COLOR_BGR2LUV,  # ""从BGR色彩空间转换到LUV色彩空间",
    cv2.COLOR_BGR2XYZ,  # ""从BGR色彩空间转换到XYZ色彩空间",
    cv2.COLOR_RGB2LUV,  # ""从RGB色彩空间转换到LUV色彩空间",
    cv2.COLOR_RGB2XYZ,  # ""从RGB色彩空间转换到XYZ色彩空间",
]
 # 创建一个滑动条
cv2.createTrackbar("Trackbar", "color_space_conversion", 0, len(color_lists) - 1, lambda x: None)


while True:
  # 获取当前滑动条的位置
  index= cv2.getTrackbarPos("Trackbar", "color_space_conversion")

  cvt_img=  cvt_img=cv2.cvtColor(img,color_lists[index])
  cv2.imshow("color_space_conversion",   cvt_img)
  # 检查按键事件，如果按下Esc键则退出
    # 检查按键事件，如果按下Esc键则退出
  key = cv2.waitKey(1)
  if key == 27:  # Esc键的ASCII码是27
      break
# 关闭所有窗口
cv2.destroyAllWindows()