import cv2
import numpy as np
import matplotlib.pyplot as plt
Video = cv2.VideoCapture("./images/1.mp4")  # 获取视频
print(cv2.__version__)
# 创建背景减除器
subtractor=cv2.createBackgroundSubtractorMOG2()
while True:
    # 读取视频 返回值和视频帧
    ret, frame = Video.read()
    # 灰度化
    cvtColor_img=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    
    # 高斯模糊 去噪声
    GaussianBlur_img=cv2.GaussianBlur( cvtColor_img , (5,5),50)
    cv2.imshow("GaussianBlur", GaussianBlur_img)
    # 腐蚀
    erode_img=cv2.erode( GaussianBlur_img, (5, 5), 50)
    cv2.imshow("erode_img", erode_img)
    # 膨胀
    dilate_iomg=cv2.dilate(erode_img, (5, 5),50)
    cv2.imshow("dilate",  dilate_iomg)
    #闭运算
    morphologyEx_img=cv2.morphologyEx( dilate_iomg, cv2.MORPH_CLOSE, (5, 5))
    cv2.imshow(" morphologyEx",  morphologyEx_img)
     # 第一阈值，高于此阈值的强度被认为是边缘候选区 第二阈值，低于此阈值的点会被忽略； 而大于等于第一阈值但小于第二阈值的点仅在连接到强边缘时被标记为边缘。
    # Canny_img=cv2.Canny( morphologyEx_img,10,50) 
    # cv2.imshow("Canny_img", Canny_img)
    subtractor_img=subtractor.apply(morphologyEx_img)
    cv2.imshow("subtractor_img=", subtractor_img)
    
    contours, hierarchy  =cv2.findContours(subtractor_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    copyimg=frame.copy()
    i=int(0)
    for contour in contours:
        area = cv2.contourArea(contour) # 轮廓面积
        Length= cv2.arcLength(contour, True) # 轮廓长度（轮廓,是否闭合）
        x, y, w, h = cv2.boundingRect(contour) # 获取轮廓的边界矩形
        if area>1000:
                  #画矩形(图片,(开始坐标xy),(结束坐标xy),(BGR颜色),线型大小,像素位置的偏移值) （当线宽为-1时，表示填充全部）
            cv2.rectangle(copyimg, (x,y), (int(x+w), int(y+w)), (255,0,0), 2,16)
            print("画矩形面积：",area,"周长：",Length,"X:",x,"Y:",y,"W:",w,"H:",h)
            cv2.imshow("copyimg", copyimg)
            
    
    k=cv2.waitKey(10) & 0xFF
    if k==27:
        break
    
cv2.destroyAllWindows()