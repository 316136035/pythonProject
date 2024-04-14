
from My_requests.my_requests import HttpRequest
from Utils.Utils_Img import Utils_Img 
import cv2
import os
import numpy as np
#定义目录
local_Storage= "./local_Storage"
file_name="picture_storage.txt"
Number_imgs=1000 #定义要获取图片数量


# 定义请求url
base_url= "https://iv.jd.com"
# 定义请求endpoint
endpoint="/slide/g.html"
# 定义请求参数
params = {
  "appId": "1604ebb2287",
  "scene": "login",
  "product": "click-bind-suspend",
  "e": "LVTKBCL3U2GFMTENFAXU4WBLDGVFXMWC4SGUP2UWZKC6TRULQUFKH4FQWFYTVLT3YFI4UXNFSVUNK2YKNUTE45PR6U",
  "j": "",
  "lang": "zh_CN",
  "callback": "jsonp_046025285995505727"

}
# 定义请求头
headers = {
  'Accept': '*/*',
  'Accept-Encoding': 'gzip, deflate, br, zstd',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Cache-Control': 'no-cache',
  'Connection': 'keep-alive',
  'Cookie': 'wlfstk_smdl=mhxk8za0x0ks1h8p3nnyp8qxsv6qyiak; __jda=95931165.17130829074491058740260.1713082907.1713082907.1713082907.1; __jdb=95931165.1.17130829074491058740260|1.1713082907; __jdc=95931165; __jdv=95931165|direct|-|none|-|1713082907449; 3AB9D23F7A4B3C9B=LVTKBCL3U2GFMTENFAXU4WBLDGVFXMWC4SGUP2UWZKC6TRULQUFKH4FQWFYTVLT3YFI4UXNFSVUNK2YKNUTE45PR6U; __jdu=17130829074491058740260',
  'Host': 'iv.jd.com',
  'Pragma': 'no-cache',
  'Referer': 'https://passport.jd.com/',
  'Sec-Fetch-Dest': 'script',
  'Sec-Fetch-Mode': 'no-cors',
  'Sec-Fetch-Site': 'same-site',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
  'sec-ch-ua': '"Google Chrome";v="123", "Not\\A-Brand";v="8", "Chromium";v="123"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}
# 初始化请求对象
HttpRequest=HttpRequest(base_url)


def Dynamically_obtain_images_to_ensure_success(retry_count=0, max_retries=5):
    response = HttpRequest.get(endpoint, params, headers)  # 发送请求
    json_obj = Utils_Img.Json_explanation(response)  # 解析json
    bg = json_obj.get("bg")  # 获取bg

    if Utils_Img.is_image_base64(bg) is not None:  # 判断是否是base64
        return bg  # 返回

    # 添加递归结束条件，例如重试次数
    if retry_count >= max_retries:
        print("达到最大重试次数，未能获取到有效图片")
        return None  # 返回None表示获取失败

    print("尝试重新获取图片...")
    return Dynamically_obtain_images_to_ensure_success(retry_count + 1)

# 在循环中检查bg是否为None
for i in range(Number_imgs):
    bg = Dynamically_obtain_images_to_ensure_success()
    
    if bg is not None:
        print("第" + str(i) + "张图片", len(bg))
        cv2.imshow("bg", Utils_Img.base64_to_image(bg))
        cv2.waitKey(100)
    else:
        print("第" + str(i) + "张图片获取失败")


    
    
 








      

 
    
    



