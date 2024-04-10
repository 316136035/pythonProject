import json
import base64
import numpy as np
import cv2

import shutil

import os
from glob import glob
from typing import List, Tuple
from PIL import Image
import numpy as np
import binascii
import random
import string


class ImgUtils:
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
    # 判断目录是否存在/创建目录
    def create_directory(directory_path):
        
        # 使用os.path.isdir()函数检查给定路径是否为一个存在的目录
        if not os.path.isdir(directory_path):
            # 如果目录不存在（即os.path.isdir()返回False），则调用os.makedirs()函数创建目录
            # os.makedirs()函数会创建指定路径的目录及其所有不存在的父目录
            os.makedirs(directory_path)
            # 创建成功后输出提示信息
            print(f"目录 {directory_path} 不存在，已创建。")
        else:
            # 如果目录已存在（即os.path.isdir()返回True），则输出提示信息
            print(f"目录 {directory_path} 已存在。")
           
    @staticmethod
    # # 读取指定目录下的所有图片的数量 参数1:目录路径
    def count_amount_images_in_folder(self, folder_path):
        image_extensions = {
            ".jpg",
            ".jpeg",
            ".png",
            ".bmp",
            ".gif",
        }  # 可拓展的图片格式集合
        count = sum(
            1
            for _, _, files in os.walk(folder_path)
            for file in files
            if file.lower().endswith(image_extensions)
        )
        return count

    @staticmethod
    # 读取指定目录下的所有图片
    def read_images_from_folder(folder_path: str) -> List[np.ndarray]:
        """
        读取指定目录及其子目录下的所有图片，并将图片数据存入一个列表中返回。

        :param folder_path: 目标目录的路径字符串
        :return: 包含所有读取到的图片数据的numpy数组列表
        """
        supported_formats = ("*.jpg", "*.jpeg", "*.png")  # 支持的图片格式
        image_paths: List[str] = [
            os.path.join(dp, f)
            for dp, dn, fn in os.walk(folder_path)
            for f in fn
            if f.endswith(supported_formats)
        ]

        images: List[np.ndarray] = []
        for img_path in image_paths:
            try:
                img: np.ndarray = cv2.imread(img_path)
                if img is not None:
                    images.append(img)
            except cv2.error as e:
                print(f"Error reading image from path '{img_path}': {e}")

        return images

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
    