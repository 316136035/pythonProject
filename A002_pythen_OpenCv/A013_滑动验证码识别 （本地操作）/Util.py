import requests
import json
import base64
import numpy as np
import cv2
import  random
import shutil
import string
import  os


# 获取图片
def get_image(url, params, headers):
    try:
        # 发送带有参数和请求头的GET请求
        response = requests.get(url=url, params=params, headers=headers)
        # 检查响应状态码
        response.raise_for_status()  # 如果状态码不是200，会自动抛出HTTPError异常
        if response.status_code == 200 :
            json_content= response.text.split('(')[1].rstrip(')')
            # 解析JSON内容为Python对象
            json_obj = json.loads(json_content)
            # 使用get方法获取"bg"字段，避免KeyError异常
            bg =  json_obj.get("bg")  
     # 检查bg是否非空且长度足够
        if bg and len(bg) > 1000:
            # 将Base64字符串解码为字节串
            decoded_image = base64.b64decode(bg)
            # 将字节串转换为NumPy数组
            nparr = np.frombuffer(decoded_image, np.uint8)  # 使用np.frombuffer代替np.fromstring，因为np.fromstring已弃用
             # 使用OpenCV库将字节串转换为图像，并转换为灰度图
            img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)  # 直接读取为灰度图，无需再转换
            return img
        else:
            print("获取验证码失败，bg字段可能为空或长度不足")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP 错误: {http_err}")
    except Exception as err:
        print(f"发生错误: {err}")

    return None  # 如果出现异常或获取失败，返回None
# 判断图片是否相同 返回True和False
def Similarity(image1 ,image2):
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
        similarity_score = cv2.compareHist(hist1, hist2, method) # 比较两个直方图 返回值是相似度
        if similarity_score > 0.9: # 相似度大于0.9
            print("两张图像相似....")
            return True
        elif similarity_score < 0.9: # 相似度小于 0.9:
            print("两张图像不相似！！！")
            return False
# 生成指定长度的随机字符串 返回一个列表 参数1:字符串长度 参数2:随机种子 参数3:生成字符串的数量
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
            random_string = ''.join(random.choices(chars, k=length))

            # 检查是否已生成过此字符串，若未生成过，则添加到结果列表中
            if random_string not in generated_strings:
                generated_strings.add(random_string)
                result.append(random_string)
                break

    return result
#断目录是否存在不存在就创建目录 参数1:目录路径
def create_directory(directory_path):
    # 判断目录是否存在
    if os.path.exists(directory_path):
    # 目录存在，删除目录（包括子目录和文件）
        shutil.rmtree(directory_path)
    else:
    # 目录不存在，创建目录
        os.makedirs(directory_path, exist_ok=True)  # 参数exist_ok=True可以防止在目录已存在时抛出异常
    os.makedirs(directory_path, exist_ok=True)
#读取指定目录下的所有图片的数量 参数1:目录路径
def count_amount_images_in_folder(folder_path):
    count = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):  # 添加您需要计数的其他图片格式
                count += 1
    return count
#读取指定目录下的所有图片 返回一个列表 参数1:目录路径
def read_images_from_folder(folder_path):
    images = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):  # 支持常见的图片格式
                img_path = os.path.join(root, file)
                img = cv2.imread(img_path)
                if img is not None:  # 确保图片读取成功
                    images.append(img)
    return images  
