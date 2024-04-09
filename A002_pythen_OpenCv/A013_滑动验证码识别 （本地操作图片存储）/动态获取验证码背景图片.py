import requests
import json
import base64
import numpy as np
import cv2
import random
import shutil
import string
import os

# 定义类 作用：获取图片并作用图像处理分类 
class sliding_verification_code_recognition:
    different_pictures={}
    different_pictures_path="./different_pictures"
    max_amount_images_in_folder=int(50)
    # 定义方法 获取图片
    
    def get_image(self, url, params, headers):
        try:
            # 发送带有参数和请求头的GET请求
            response = requests.get(url=url, params=params, headers=headers)
            response.raise_for_status()  # 抛出HTTPError异常（如果状态码不是200）

            # 直接提取JSON内容并解码，使用json.loads()的loads()方法避免手动切分字符串
            json_content = json.loads(response.text)
            bg = json_content.get("bg")  # 使用get方法获取"bg"字段

            if bg and len(bg) > 1000:
                # 将Base64字符串解码为字节串
                decoded_image = base64.b64decode(bg)
                # 使用NumPy从字节串创建数组，推荐使用frombuffer代替fromstring
                nparr = np.frombuffer(decoded_image, dtype=np.uint8)
                # 使用OpenCV将字节串转换为图像
                img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                # 转换为灰度图
                img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                return img_gray
            else:
                print("获取验证码失败，bg字段可能为空或长度不足")

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP 错误: {http_err}")
        except json.JSONDecodeError as json_err:
            print(f"JSON 解析错误: {json_err}")
        except Exception as err:
            print(f"未知错误: {err}")

        return None
    
    # 定义方法 判断图像相似度
    def similarity_img_recognition(self, image1, image2):
        # 直接使用 NumPy 数组进行操作，避免重复计算直方图
        hist1 = cv2.calcHist([image1], [0], None, [256], [0, 256]).astype(np.float32)
        hist2 = cv2.calcHist([image2], [0], None, [256], [0, 256]).astype(np.float32)

        # 归一化直方图
        cv2.normalize(hist1, hist1, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
        cv2.normalize(hist2, hist2, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

        # 直接比较而不打印中间结果，将相似度阈值作为一个类属性或方法参数
        similarity_score = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

        # 根据相似度阈值决定是否相似，返回布尔值即可
        if similarity_score > 0.9:
            return True
        else:
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