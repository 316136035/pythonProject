from Utils.Utils_Img import Utils_Img 
from My_requests.my_requests import HttpRequest
import cv2
import os

#定义目录
local_Storage= "./local_Storage"
file_name="picture_storage.txt"
# 定义请求url
base_url= "https://iv.jd.com"
# 定义请求endpoint
endpoint="/slide/g.html"
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
# 初始化请求对象
HttpRequest=HttpRequest(base_url)
# 初始化图片工具对象
Utils_Img =Utils_Img ()
response=HttpRequest.get(endpoint,params,headers)
# 使用完后关闭会话
response.close()
# 将响应转换为json对象
Json_object=Utils_Img .Json_explanation(response)

different_pictures={} #定义一个字典存放背景不同的图片
#定义一个变量
is_similarity_img_recognition=True #定义一个变量
 
# 获取图片 返回base64
def get_base64_img(endpoint,params,headers):
    img_data=HttpRequest.get(endpoint,params,headers) #获取响应体
    Json_object=Utils_Img .Json_explanation(img_data) #将响应转换为json对象
    return Json_object.get("bg")
    
# 
Utils_Img .create_directories_an_create_files(local_Storage,file_name)



        




# for i in range(0,20):
#     str_list=Utils_Img.generate_unique_random_strings(10,88,i)
    
#     base64_img=get_base64_img(endpoint,params,headers)
   
#     with open(os.path.join(local_Storage, file_name), 'a') as file:
#         file.writelines( str_list[i]+"----"+base64_img+"\n")
        
    
Utils_Img.number_of_pictures_with_the_same_similarity(os.path.join(local_Storage, file_name))