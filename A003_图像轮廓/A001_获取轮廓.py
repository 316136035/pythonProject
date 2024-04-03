from my_package import imagesApi  # 引入自定义包
import cv2  # 导入cv2模块
import numpy as np
list_images = imagesApi.return_Image_all()

newlist = []
def get_contours(image):
  image1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 灰度图
# 对图片进行模糊处理,消除椒盐噪声特别有效，(图像,卷积大小)
# 中值滤波. 参数：图像，核大小
  image2 = cv2.medianBlur(image1, 3)
# 自适应阈值
  image3 = cv2.adaptiveThreshold(image2, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 1)
# 轮廓检测
  contours, _ = cv2.findContours(image3, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
  image_copy = image.copy()
  for contour in contours:
    area = cv2.contourArea(contour)
    Length= cv2.arcLength(contour, True)
 
    x, y, w, h = cv2.boundingRect(contour)
    
   
    print("面积：",area)
    print("周长：",Length)
    if w==45:
      print("坐标：",x,"  ",y,"  ",w,"  ",h)
      cv2.drawContours(
            image=image_copy,
            contours=[contour],  # 仅绘制当前满足条件的单个轮廓
            contourIdx=0,  # 当前轮廓索引设为0，因为只有一个轮廓
            color=(0,  0,2500),
            thickness=2,
        )
      cv2.imshow("image", np.hstack([image3]))
      cv2.imshow("image", np.hstack([image , image_copy]))
      cv2.waitKey(1000)
    
    
        
       
   
  
  

for image in list_images:
    get_contours(image)

