from Utils.ImgUtils.ImgUtils import ImgUtils
from My_requests.my_requests import HttpRequest
import cv2

base_url= "https://iv.jd.com"
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
ImgUtils=ImgUtils()
response=HttpRequest.get(endpoint,params,headers)
# 使用完后关闭会话
response.close()
Json_object=ImgUtils.Json_explanation(response)
print(Json_object.get("bg"))

img=ImgUtils.base64_to_image(Json_object.get("bg"))
cv2.imshow("img",img)
cv2.waitKey(0)

base64_img=ImgUtils.image_to_base64(img)
img1=ImgUtils.base64_to_image(base64_img)
cv2.imshow("img1",img1)
cv2.waitKey(0)


