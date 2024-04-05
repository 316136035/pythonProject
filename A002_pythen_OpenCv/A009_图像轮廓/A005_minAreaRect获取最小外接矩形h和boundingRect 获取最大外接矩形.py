import cv2
import numpy as np

# 读取图像并转换为灰度图像
img = cv2.imread("./images/1.jpg")
# 转换为灰度图像
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 二值化:灰度图像,阈值,阈值最大值,阈值类型（请求查看上面）
_, ATimage = cv2.threshold(gray_img, 100, 255, cv2.THRESH_BINARY)

cv2.imshow("ATimage ",ATimage )
cv2.waitKey(0)

# 腐蚀白色部分 参数1：原图 2：卷积核 3：迭代次数
erode = cv2.erode(ATimage, np.ones((3, 3), np.uint8), iterations=2)
# 膨胀白色部分 参数1：原图 2：卷积核 3：迭代次数
dilate = cv2.dilate(erode, np.ones((3, 3), np.uint8), iterations=2)


cv2.waitKey(0)
# image：输入图像，通常应该是经过预处理（如二值化）的单通道图像（灰度图像），其中物体轮廓区域为白色，背景为黑色。
# mode：轮廓检索模式，可选值包括：
# cv2.RETR_EXTERNAL：只检测最外层轮廓。
# cv2.RETR_LIST：检测所有轮廓，不建立层次关系。
# cv2.RETR_CCOMP：检测所有轮廓，并且为每个连通组件建立两个级别的轮廓。
# cv2.RETR_TREE：检测所有轮廓，并建立完整的层次结构。  (常用)
# cv2.RETR_FLOODFILL：使用 floodfill 算法检测轮廓。
# method：轮廓近似方法，可选值包括：
# cv2.CHAIN_APPROX_NONE：存储所有的边界点。
# cv2.CHAIN_APPROX_SIMPLE：垂直或斜率为 0 的连续边界的点，仅保留端点 比喻正方形。 (常用)
# cv2.CHAIN_APPROX_TC89_L1, cv2.CHAIN_APPROX_TC89_KCOS：使用 Teh-Chin 链码近似算法。
# findContours函数参数：image单通道图像, mode轮廓检索模式, method轮廓近似方法
contours, hierarchy = cv2.findContours(ATimage, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print("轮廓数量：", len(contours))
copyimg1 = img.copy()
copyimg2 = img.copy()

i=int(0)
for contour in contours:

    area = cv2.contourArea(contours[12])  # 轮廓面积
    Length = cv2.arcLength(contour, True)  # 轮廓长度（轮廓,是否闭合）
    x, y, w, h = cv2.boundingRect(contour)  # 获取轮廓的边界矩形
    print("面积：", area, "周长：", Length, "X:", x, "Y:", y, "W:", w, "H:", h)
    if 1800>area>1600:
      # 获取最小外接矩形：轮廓   
      #函数返回一个 RotatedRect 结构，其中包括：center：旋转矩形的中心点坐标（(x, y) size：旋转矩形的尺寸（(width, height)），宽度和高度都是相对于中心点的angle：旋转矩形的旋转角度，范围在 -90 到 +90 度之间，逆时针方向为正。
      RotatedRect=cv2.minAreaRect(contours[12])
      # 获取旋转矩形的四个顶点坐标
      RotatedRect=cv2.boxPoints(RotatedRect)
      # 坐标取整
      RotatedRect=np.round(RotatedRect).astype(int)
      # 绘制最小外接矩形
      cv2.drawContours(copyimg1, [RotatedRect], -1, (0,255, 0), 2)
    
    
    
      ## 获取最大外接矩形：轮廓
      x, y, w, h=cv2.boundingRect(contours[12])
      # 绘制最大外接矩形
      cv2.rectangle(copyimg2, (x, y), (x+w, y+h), (0,0, 255), 2)
 


# 显示图像
cv2.imshow("drawContours", np.hstack((img, copyimg1,copyimg2)))
cv2.waitKey(0)
cv2.destroyAllWindows()
