import requests
import json
import base64
import requests
import numpy as np
import cv2  
import matplotlib.pyplot as plt  # 绘图
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
};
# 或者对于requests 3.x及以上版本，可以直接将params作为参数传递
  url = 'https://iv.jd.com/slide/g.html'
# 发送带有参数和请求头的GET请求
  response = requests.get(url, params=params, headers=headers)
# 检查响应状态码
  if response.status_code == 200:
    json_content= response.text.split('(')[1].rstrip(')')
  # 解析JSON内容为Python对象
    json_obj = json.loads(json_content)
  # 将Base64字符串解码为字节串
    decoded_image = base64.b64decode(json_obj["bg"])
  # 将字节串转换为NumPy数组
    nparr=np.fromstring(decoded_image, np.uint8)
  # 使用OpenCV库将字节串转换为图像
    img=cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img
  else:
    print("请求失败")
    
 # 读取所有图片
# 读取本地所有图片
# 读取本地所有图片并返回处理为灰色的图片数组
def return_Image_all():
    list = []
    for i in range(100):
        img = cv2.imread(f"./images/{i+1}.jpg")  # 读取图片
        new_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转换颜色通道
        list.append(new_img)  # 转换灰度图
    return list
# 显示所有图片
def showImage_all(images):

    # 获取所有图片的最大高度和宽度（假设都是灰度图像）
    max_height = max([img.shape[0] for img in images])
    max_width = max([img.shape[1] for img in images])

    # 计算行数和列数，尽量让每行每列都有图片
    n_rows = (len(images) // 10) + min(1, len(images) % 10)
    n_cols = min(10, len(images))

    # 指定figsize，这里假设你想将整体背景设置为特定的宽度和高度，比如宽度为12英寸，高度自适应
    # 你需要根据实际情况调整这两个值
    fig_width_inches =25  # 示例宽度
    fig_aspect_ratio = max_width / max_height  # 图片总体的宽高比
    fig_height_inches = fig_width_inches / fig_aspect_ratio  # 根据宽度和图片的宽高比计算高度

    # 创建子图，同时设置figsize
    fig, axs = plt.subplots(
        nrows=n_rows,
        ncols=n_cols,
        figsize=(fig_width_inches, fig_height_inches),
        squeeze=True,
        gridspec_kw={"wspace": 0, "hspace": 0},
    )
    
    # 遍历每一个 Axes 对象并显示图片
    for i, ax in enumerate(axs.flat):
        if i < len(images):
            ax.imshow(images[i], cmap="gray", aspect="equal")
            ax.axis("off")

    # 自动调整子图间距以防止重叠
    plt.tight_layout(pad=0)

    # 显示图形
    plt.show()
# 获取所有图片
images = return_Image_all()  # 假设这是一个返回图片列表的函数


showImage_all(return_Image_all())

