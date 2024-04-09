import 动态获取验证码背景图片
import cv2
import os

class opencv_identification:
    different_pictures_path="./different_pictures"

    
    
    def __init__(self):
       pass

              
      
    
    def get_subdirectory_names(self,directory):
      subdirs = set()
      for root, dirs, _ in os.walk(directory):
        # 添加当前层级的子目录名到集合中，避免重复
          subdirs.update(dirs)
    
      # 返回子目录名称列表
      return list(subdirs)
    
    #获取文件夹下所有文件名不相似的图片
    def get_different_pictures(self,subdirs):
      # for str in subdirs:
      #   img=cv2.imread(self.different_pictures_path+"/"+str+"/"+str+".jpg")
      #   cv2.imshow(str,img)
      #   cv2.waitKey(0)
      pass
    
    
    

