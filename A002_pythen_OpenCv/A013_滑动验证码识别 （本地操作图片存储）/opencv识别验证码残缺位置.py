import cv2
import os
import 动态获取验证码背景图片 as s_v_c_r
# 或者对于requests 3.x及以上版本，可以直接将params作为参数传递
url = "https://iv.jd.com/slide/g.html"
# 定义请求参数
params = {
    # 定义请求头
    "appId": "1604ebb2287",
    "scene": "login",
    "product": "click-bind-suspend",
    "encryptedData": "VZ7ZXIN2SXGMSG7RE7RO2FXF6RXH45UG5TLQNRH3RHZTNM4SJRX5SYDNEE4NPLJ2I3L2L5GA3P4VFJC25YHDQ2NV5Y",
    "lang": "zh_CN",
    "callback": "jsonp_08543940888960628",
}
# 定义请求头
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Cookie": "__jdv=76161171|direct|-|none|-|1711743323476; __jdu=17117433234761952598816; 3AB9D23F7A4B3CSS=jdd03VZ7ZXIN2SXGMSG7RE7RO2FXF6RXH45UG5TLQNRH3RHZTNM4SJRX5SYDNEE4NPLJ2I3L2L5GA3P4VFJC25YHDQ2NV5YAAAAMORPNEB2QAAAAACUT5ELC5OALDA4X; PCSYCityID=CN_440000_440100_0; areaId=19; ipLoc-djd=19-1601-0-0; shshshfpa=67917b71-019f-8727-66d8-3274404b6a45-1711743324; shshshfpx=67917b71-019f-8727-66d8-3274404b6a45-1711743324; shshshfpb=BApXen9LSiOtAZ9Vh89hpk9QRWwP7jdufBlM1NAto9xJ1MuUaGoC2; wlfstk_smdl=kezcc39toktortankuuv3g7eldhzc7zw; __jda=95931165.17117433234761952598816.1711743323.1711863945.1711873934.10; __jdb=95931165.1.17117433234761952598816|10.1711873934; __jdc=95931165; 3AB9D23F7A4B3C9B=VZ7ZXIN2SXGMSG7RE7RO2FXF6RXH45UG5TLQNRH3RHZTNM4SJRX5SYDNEE4NPLJ2I3L2L5GA3P4VFJC25YHDQ2NV5Y",
    "Host": "iv.jd.com",
    "Referer": "https://passport.jd.com/",
    "Sec-Fetch-Dest": "script",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Google Chrome";v="123", "Not\\u00A0A-Brand";v="8", "Chromium";v="123"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
}
   
     

SVCR= s_v_c_r.sliding_verification_code_recognition(url, params, headers) # 创建对象
class OpenCVIdentification:
    different_pictures_path = "./different_pictures"
    different_pictures={}
    def __init__(self):
        pass
    
    def get_subdirectory_names(self, dir_path):  
        subdirectories = [] # 创建空列表
        # os.walk() 递归遍历目录树
        for root, dirs, _ in os.walk(dir_path):
            # 收集第一层子目录名
            subdirectories.extend(dirs)
            break  # 只获取第一级子目录
        # 使用 set 去重后转换回 list
        unique_subdirectories = list(set(subdirectories))
        # 返回子目录列表
        return unique_subdirectories
    #读取目录中相似度不同的图片参数： 数组集合
    def get_images_by_directory_name(self, subdir_list,verify_img):
      for subdir in subdir_list:
         img=cv2.imread(self.different_pictures_path+"/"+subdir+"/"+subdir+".jpg")
         cv2.imshow("img",img)
         cv2.waitKey(0)
         
        #  if s_v_c_r.sliding_verification_code_recognition.similarity_img_recognition(SVCR,img,verify_img):
        #    print(subdir)
         

# 创建实例
OI = OpenCVIdentification()


# 获取 different_pictures_path 目录下的子目录列表 
subdir_list = OI .get_subdirectory_names(OI.different_pictures_path)
img= s_v_c_r.sliding_verification_code_recognition.get_image(SVCR,url=url,params=params,headers=headers)
OI .get_images_by_directory_name(subdir_list,img)





