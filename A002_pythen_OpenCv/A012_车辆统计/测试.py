

import requests
import json
import base64
import requests
import numpy as np
import cv2  
import matplotlib.pyplot as plt  # 绘图
import time

# 从京东接口获取图片
def get_images():
  params = {
  "appId": "1604ebb2287",
  "scene": "login",
  "product": "click-bind-suspend",
  "encryptedData": "VZ7ZXIN2SXGMSG7RE7RO2FXF6RXH45UG5TLQNRH3RHZTNM4SJRX5SYDNEE4NPLJ2I3L2L5GA3P4VFJC25YHDQ2NV5Y",
  "lang": "zh_CN",
  "callback": "jsonp_08543940888960628"
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
  "sec-ch-ua": "\"Google Chrome\";v=\"123\", \"Not\\u00A0A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
  "sec-ch-ua-mobile": "?0",
  "sec-ch-ua-platform": "\"Windows\"",
}
# 或者对于requests 3.x及以上版本，可以直接将params作为参数传递
  url = 'https://iv.jd.com/slide/g.html'
# 发送带有参数和请求头的GET请求
  response = requests.get(url, params=params, headers=headers)
# 检查响应状态码
  if response.status_code == 200:
    json_content= response.text.split('(')[1].rstrip(')')
  # 解析JSON内容为Python对象
    json_obj = json.loads(json_content)
    bg=json_obj["bg"]
    if bg=="" or bg==None  or len(bg)<1000:
        print("获取验证码失败")
    else:
        # 将Base64字符串解码为字节串
        decoded_image = base64.b64decode(bg)
        # 将字节串转换为NumPy数组
        nparr=np.fromstring(decoded_image, np.uint8)
        # 使用OpenCV库将字节串转换为图像
        img=cv2.imdecode(nparr, cv2.IMREAD_COLOR)
  
        return img
        

    
 # 读取所有图片
# 读取本地所有图片

def Similarity(image1 ,image2):
    # 确保图像已成功加载
    if image1 is None or image2 is None:
        print("图片加载失败！")
        cv2.imshow("Error", image1)
    else:
        print("图片加载成功！")
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
        
        if similarity_score > 0.9: # 相似度大于0.8
            print("两张图像相似")
            return image2
        elif similarity_score < 0.9: # 相似度小于0.8
            print("两张图像不相似")
            return None

    print(f"相似度: {similarity_score}")
        

img = cv2.imread('./images/4.jpg', )  # 读取图片 默认是彩色的      
image1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


while True:
    
    images=get_images()
    if    images is not None:
        image2=cv2.cvtColor(images,cv2.COLOR_BGR2GRAY) 
        cv2.imshow("image1", image1)
        cv2.imshow("image2", image2)
        new_img=Similarity(image1 ,image2)
        current_timestamp = time.time()
        if new_img is not None:
            cv2.imwrite('./img/' + str(int(current_timestamp)) + '.jpg', image2)  # 保存图片
        cv2.waitKey(20)
    
    
    
