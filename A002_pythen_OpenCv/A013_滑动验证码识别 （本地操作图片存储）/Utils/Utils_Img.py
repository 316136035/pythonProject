import json
import base64
import numpy as np
import cv2

import os
from glob import glob


import numpy as np
import binascii
import random
import string  


import base64
from io import BytesIO
import imghdr



class Utils_Img:
    @staticmethod
    # json解析函数
    def Json_explanation(response):
        type = response.headers.get("Content-Type")
        if type == "application/json":
            try:
                return response.json()
            except json.JSONDecodeError:
                print("response.json()异常")
                return None

        else:
            # 提取 JSON 字符串部分
            try:
                # 从响应文本中提取 JSON 字符串
                json_str = response.text.split("(", 1)[1].rstrip(")")
                # 将 JSON 字符串转换为 Python 字典
                json_obj = json.loads(json_str)
                # 返回 JSON 对象
                return json_obj
            except (IndexError, json.JSONDecodeError):
                print("json.loads(json_str)异常")
                return None

    # 判断是否是base64格式的图片
    @staticmethod
    def is_image_base64(base64_string):
    # 尝试解码Base64字符串
        try:
            data = base64.b64decode(base64_string)
        except (TypeError, binascii.Error):  # 如果不是有效的Base64数据会抛出异常
            return False
    
     # 检查字节流的头部来初步判断图片类型
        file_type = imghdr.what(BytesIO(data))
    
        # 如果imghdr.what返回了非None值，则表明数据可能是某种图片类型
        return file_type is not None

# 使用示例
     
    @staticmethod
    # 判断图片相似度否相同
    def similarity_img_recognition(image1, image2):
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
    
    @staticmethod
    # 判断目录是否存在/创建目录和创建文件
    def create_directories_an_create_files(local_Storage, file_name):
        try:
            # 使用os.path.isdir()函数检查给定路径是否为一个存在的目录
            if not os.path.isdir(local_Storage):
            # 如果目录不存在，则调用os.makedirs()函数创建目录
                os.makedirs(local_Storage)
                print(f"目录 {local_Storage} 不存在，已创建成功！")

                # 定义要在新创建的目录中创建的.txt文件名及完整路径
                file_path = os.path.join(local_Storage, file_name)
            
                
               # 创建文件，如果文件不存在的话
                os.open(file_path, os.O_CREAT | os.O_WRONLY)
                return False
            
            else:
                print(f"目录 {local_Storage} 已存在...")

            return True

        except FileNotFoundError as fnf_error:
            print(f"创建目录或文件时发生错误: {fnf_error}")
            return False
        except PermissionError as perm_error:
            print(f"没有足够的权限创建目录或文件: {perm_error}")
            return False
        except Exception as e:
            print(f"未知错误: {e}")
        return False
           
    @staticmethod
    # 统计picture_storage.txt文件中相似度不同的图片 存放在字典中返回
    def Pictures_with_different_statistical_similarities(local_Storage,file_path):
        my_dictionary ={} # 定义字典 确保键值唯一
        with open(os.path.join(local_Storage,file_path), 'r') as file:
            while True:
                line =file.readline() # 一行一行读取
                if not line: # 读取到文件末尾
                    break
                lines_split=line.split('----')[0] # 分割成数据
                my_dictionary[lines_split[0]]=lines_split[1] # 添加到字典
        return my_dictionary

    # 统计picture_storage.txt文件中相似度相同同的图片 存放在数组中返回
    def Images_with_the_same_statistical_similarity(local_Storage,file_path,img_name):
        pass
        
    @staticmethod
    # base64字符串转图片
    def base64_to_image(base64_string: str):
        try:
            # 解码Base64字符串  据Base64编码规则计算需要补充的'='数量
            padding_needed = (4 - len(base64_string) % 4) % 4
            base64_string += '=' * padding_needed
            image_data = base64.b64decode(base64_string)
            # 使用NumPy从字节串创建数组，推荐使用frombuffer代替fromstring
            parr = np.frombuffer(image_data , dtype=np.uint8)
            # 使用OpenCV将字节串转换为图像
            img = cv2.imdecode(parr, cv2.IMREAD_COLOR)
            # 转换为灰度图
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            return img_gray # 转换成功
        except binascii.Error as e:
            print(f"解码错误: {e}","base64_string:",base64_string)
            return None  # 转换失败

    @staticmethod
    #将图片二进制数据转换为Base64编码
    def image_to_base64(image):
        try:
            #将图像转换为JPEG格式并编码为字节串
            _, img_encoded = cv2.imencode('.jpg',image)
            print(len(img_encoded))
            # 将图片二进制数据转换为Base64编码
            base64_string = base64.b64encode(img_encoded).decode("utf-8")
            return base64_string  # 转换成功
        except Exception as e:
            print(f"将图片转换为Base64编码时发生错误!!!!")
            return None

    @staticmethod
    #生产随机字符串 参数：长度，种子值，生成数量
    def generate_unique_random_strings(length, seed_value, count):
        # 设置固定的随机种子
        random.seed(seed_value)

        # 定义可用字符集
        chars = string.ascii_lowercase

        # 创建一个集合用于存储已生成过的字符串，防止重复
        generated_strings = set()

        result = []
        # 循环生成指定数量的字符串
        for _ in range(count+1):
            while True:
                # 生成随机字符串
                random_string = "".join(random.choices(chars, k=length))

                # 检查是否已生成过此字符串，若未生成过，则添加到结果列表中
                if random_string not in generated_strings:
                    generated_strings.add(random_string)
                    result.append(random_string)
                    break

        return result
    
