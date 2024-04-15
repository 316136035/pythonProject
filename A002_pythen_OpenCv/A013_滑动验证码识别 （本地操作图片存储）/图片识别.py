import cv2
import numpy as np
import matplotlib.pyplot as plt

import os

# 列出指定目录下的所有文件
files = os.listdir("./img/")
  
# 创建背景减除器
subtractor = cv2.createBackgroundSubtractorMOG2()
def graphics_processing(img):
     # 高斯模糊 去噪声
    GaussianBlur_img = cv2.GaussianBlur(img, (3, 3), 1)
    # 腐
    erode_img = cv2.erode(GaussianBlur_img, (3, 3), 1)
    # 膨胀
    dilate_iomg = cv2.dilate(erode_img, (3, 3), 1)
    # 闭运算
    morphologyEx_img = cv2.morphologyEx(dilate_iomg, cv2.MORPH_CLOSE, (3, 5))
    # 背景减除
    subtractor_Img = subtractor.apply(morphologyEx_img)
    cv2.imshow("copyimg", subtractor_Img)
    cv2.waitKey(1000)
    return subtractor_Img



for file in files:
    img = cv2.imread("./img/"+file)
    subtractor_Img=graphics_processing(img)
     # 轮廓检测 
    contours, hierarchy  =cv2.findContours( subtractor_Img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    copyimg=img.copy()
    for contour in contours:
        area = cv2.contourArea(contour) # 轮廓面积
        Length= cv2.arcLength(contour, True) # 轮廓长度（轮廓,是否闭合）
        x, y, w, h = cv2.boundingRect(contour) # 获取轮廓的边界矩形
        if 2000>area > 1000:
         #画矩形(图片,(开始坐标xy),(结束坐标xy),(BGR颜色),线型大小,像素位置的偏移值) （当线宽为-1时，表示填充全部）
            cv2.rectangle(copyimg, (x,y), (int(x+w), int(y+w)), (0,0, 255), 1,16)
            print("画矩形面积：",area,"周长：",Length,"X:",x,"Y:",y,"W:",w,"H:",h)
            cv2.imshow("copyimg", copyimg)
            cv2.waitKey(1000)
    
    



