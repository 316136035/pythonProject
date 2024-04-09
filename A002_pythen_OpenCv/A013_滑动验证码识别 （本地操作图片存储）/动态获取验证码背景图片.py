import requests
import json
import base64
import numpy as np
import cv2
import random
import shutil
import string
import os





class sliding_verification_code_recognition:
    different_pictures={}
    different_pictures_path="./different_pictures"
    max_amount_images_in_folder=int(50)
    # 定义方法 获取图片
  
    def get_image(self,url, params, headers):
        try:
            # 发送带有参数和请求头的GET请求
            response = requests.get(url=url, params=params, headers=headers)
            # 检查响应状态码
            response.raise_for_status()  # 如果状态码不是200，会自动抛出HTTPError异常
            if response.status_code == 200:
                json_content = response.text.split("(")[1].rstrip(")")
                # 解析JSON内容为Python对象
                json_obj = json.loads(json_content)
                # 使用get方法获取"bg"字段，避免KeyError异常
                bg = json_obj.get("bg")
            # 检查bg是否非空且长度足够
            if bg and len(bg) > 1000:
                # 将Base64字符串解码为字节串
                decoded_image = base64.b64decode(bg)
                # 将字节串转换为NumPy数组
                nparr=np.fromstring(decoded_image, np.uint8)
                 # 使用OpenCV库将字节串转换为图像
                img=cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#转换为灰度图
                
                
                return img
            else:
                print("获取验证码失败，bg字段可能为空或长度不足")

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP 错误: {http_err}")
        except Exception as err:
            print(f"发生错误: {err}")

        return None  # 如果出现异常或获取失败，返回None
        # 判断图片是否相同 返回True和False

    #判断图片相似度否相同
    def similarity_img_recognition(self,image1, image2):
        # 定义直方图参数
        hist_size = 256
        ranges = [0, 256]
        # 计算每张图像的直方图，并将其转换为32位浮点数类型
        hist1 = cv2.calcHist([image1], [0], None, [hist_size], ranges)
        hist1 = np.float32(hist1)
        hist2 = cv2.calcHist([image2], [0], None, [hist_size], ranges)
        hist2 = np.float32(hist2)
        # 归一化直方图
        cv2.normalize(hist1, hist1, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
        cv2.normalize(hist2, hist2, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
        # 设置比较方法（例如 Correlation 方法）
        method = cv2.HISTCMP_CORREL
        # 比较直方图
        similarity_score = cv2.compareHist(
            hist1, hist2, method
        )  # 比较两个直方图 返回值是相似度
        if similarity_score > 0.9:  # 相似度大于0.9
            print("两张图像相似....")
            return True
        elif similarity_score < 0.9:  # 相似度小于 0.9:
            print("两张图像不相似！！！")
            return False

    # 生成指定长度的随机字符串 返回一个列表 参数1:字符串长度 参数2:随机种子 参数3:生成字符串的数量
    def generate_unique_random_strings(self,length, seed_value, count):
        # 设置固定的随机种子
        random.seed(seed_value)

        # 定义可用字符集
        chars = string.ascii_lowercase

        # 创建一个集合用于存储已生成过的字符串，防止重复
        generated_strings = set()

        result = []

        for _ in range(count):
            while True:
                # 生成随机字符串
                random_string = "".join(random.choices(chars, k=length))

                # 检查是否已生成过此字符串，若未生成过，则添加到结果列表中
                if random_string not in generated_strings:
                    generated_strings.add(random_string)
                    result.append(random_string)
                    break

        return result

    # 断目录是否存在不存在就创建目录 参数1:目录路径
    def create_directory(self,directory_path):
        # 判断目录是否存在
        if os.path.exists(directory_path):
            # 目录存在，删除目录（包括子目录和文件）
            shutil.rmtree(directory_path)
        else:
            # 目录不存在，创建目录
            os.makedirs(
                directory_path, exist_ok=True
            )  # 参数exist_ok=True可以防止在目录已存在时抛出异常
        os.makedirs(directory_path, exist_ok=True)

    # 读取指定目录下的所有图片的数量 参数1:目录路径
    def count_amount_images_in_folder(self,folder_path):
        count = 0
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(
                    (".jpg", ".jpeg", ".png", ".bmp", ".gif")
                ):  # 添加您需要计数的其他图片格式
                    count += 1
        return count

    # 读取指定目录下的所有图片 返回一个列表 参数1:目录路径
    def read_images_from_folder(self,folder_path):
        images = []
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if (
                    file.endswith(".jpg")
                    or file.endswith(".png")
                    or file.endswith(".jpeg")
                ):  # 支持常见的图片格式
                    img_path = os.path.join(root, file)
                    img = cv2.imread(img_path)
                    if img is not None:  # 确保图片读取成功
                        images.append(img)
        return images
    # 遍历集合的函数    
    def traverse_different_pictures(self, new_img):
        if len( self.different_pictures )>0 and new_img is not None:  # 判断集合和新图片是否为空
            is_similarity = True  # 定义变量
            print("开始遍历集合",len( self.different_pictures))
         # 遍历集合
            for key, img in self.different_pictures.items():  # 请确保使用 self.different_pictures 而不是 different_pictures
                # 判断相似度 如果相似度大于0.9 则返回True
                similarity_result = self.similarity_img_recognition(img, new_img)
                if similarity_result:  # 假设 similarity_img_recognition 返回 True 或 False 表示是否相似
                    print("判断相似度",similarity_result)
                    num=self.count_amount_images_in_folder( self.different_pictures_path+"/"+key)
                    if num<=self.max_amount_images_in_folder:
                        cv2.imwrite(self.different_pictures_path+"/"+key+"/"+str(num)+".jpg",new_img)
                    is_similarity = False  # 当相似度满足条件时，将 is_similarity 更新为 False
                    break  # 跳出循环
            #要是全部不相同才返回new_img
            if is_similarity:
                return  True
        
        #分类验证码图片 参数：初始化图片，
    def classify_verification_code_images(self,new_img):
        
        is_similarity = self.traverse_different_pictures(new_img)
        if is_similarity:
            self.random_strings=self.generate_unique_random_strings(6,88,len(self.different_pictures)+1) #生成随机字符串
            #获取随机字符串数组的最后一位
            key= self.random_strings[len(self.different_pictures)]
            self.different_pictures[key]=new_img
            self.create_directory(self.different_pictures_path+"/"+key) #断目录是否存在不存在就创建目录 参数1:目录路径
            cv2.imwrite(self.different_pictures_path+"/"+key+"/"+key+".jpg",new_img)
            
            
            
          
        
             
     
                      
    def __init__(self,url,params,headers):
        #定义集合存放相似度不同的图片    
        self.image = self.get_image(url,params,headers) #获取图片
        self.random_strings=self.generate_unique_random_strings(6,88,1) #生成随机字符串
        self.different_pictures[str(self.random_strings[0])]=self.image #将图片和随机字符串存入字典
        self.create_directory(self.different_pictures_path)
        self.create_directory(self.different_pictures_path+"/"+str(self.random_strings[0]))
        cv2.imwrite(self.different_pictures_path+"/"+str(self.random_strings[0])+"/"+str(self.random_strings[0])+".jpg",self.image)
       
        
        
           

# # 或者对于requests 3.x及以上版本，可以直接将params作为参数传递
# url = "https://iv.jd.com/slide/g.html"
# # 定义请求参数
# params = {
#     # 定义请求头
#     "appId": "1604ebb2287",
#     "scene": "login",
#     "product": "click-bind-suspend",
#     "encryptedData": "VZ7ZXIN2SXGMSG7RE7RO2FXF6RXH45UG5TLQNRH3RHZTNM4SJRX5SYDNEE4NPLJ2I3L2L5GA3P4VFJC25YHDQ2NV5Y",
#     "lang": "zh_CN",
#     "callback": "jsonp_08543940888960628",
# }
# # 定义请求头
# headers = {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate, br, zstd",
#     "Accept-Language": "zh-CN,zh;q=0.9",
#     "Connection": "keep-alive",
#     "Cookie": "__jdv=76161171|direct|-|none|-|1711743323476; __jdu=17117433234761952598816; 3AB9D23F7A4B3CSS=jdd03VZ7ZXIN2SXGMSG7RE7RO2FXF6RXH45UG5TLQNRH3RHZTNM4SJRX5SYDNEE4NPLJ2I3L2L5GA3P4VFJC25YHDQ2NV5YAAAAMORPNEB2QAAAAACUT5ELC5OALDA4X; PCSYCityID=CN_440000_440100_0; areaId=19; ipLoc-djd=19-1601-0-0; shshshfpa=67917b71-019f-8727-66d8-3274404b6a45-1711743324; shshshfpx=67917b71-019f-8727-66d8-3274404b6a45-1711743324; shshshfpb=BApXen9LSiOtAZ9Vh89hpk9QRWwP7jdufBlM1NAto9xJ1MuUaGoC2; wlfstk_smdl=kezcc39toktortankuuv3g7eldhzc7zw; __jda=95931165.17117433234761952598816.1711743323.1711863945.1711873934.10; __jdb=95931165.1.17117433234761952598816|10.1711873934; __jdc=95931165; 3AB9D23F7A4B3C9B=VZ7ZXIN2SXGMSG7RE7RO2FXF6RXH45UG5TLQNRH3RHZTNM4SJRX5SYDNEE4NPLJ2I3L2L5GA3P4VFJC25YHDQ2NV5Y",
#     "Host": "iv.jd.com",
#     "Referer": "https://passport.jd.com/",
#     "Sec-Fetch-Dest": "script",
#     "Sec-Fetch-Mode": "no-cors",
#     "Sec-Fetch-Site": "same-site",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
#     "sec-ch-ua": '"Google Chrome";v="123", "Not\\u00A0A-Brand";v="8", "Chromium";v="123"',
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": '"Windows"',
# }
# SVCR=sliding_verification_code_recognition(url, params, headers) # 创建对象

# for i in range(1, 10000):
#     new_img=SVCR.get_image(url, params, headers)
#     SVCR.classify_verification_code_images(new_img)
   
    





