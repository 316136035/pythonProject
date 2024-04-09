import requests
# 引入类型提示
from typing import Dict, Union, Any 

import json


class HttpRequest:
    # 初始化 参数：base_url 
    def __init__(self, base_url: str = None):
        self.base_url = base_url
        self.session = requests.Session()
    # get请求 参数：endpoint, params, headers
    def get(self, endpoint: str, params: Dict[str, Any] = None, headers: Dict[str, str] = None) -> requests.Response:
        url = self._build_url(endpoint)
        response = self.session.get(url, params=params, headers=headers)
        return self._handle_response(response)

    def post(self, endpoint: str, data: Union[Dict[str, Any], bytes], headers: Dict[str, str] = None) -> requests.Response:
        url = self._build_url(endpoint)
        response = self.session.post(url, data=data, headers=headers)
        return self._handle_response(response)
    # 构建url
    def _build_url(self, endpoint: str) -> str:
        # 判断是否以http://或https://开头
        if self.base_url and not endpoint.startswith(('http://', 'https://')):
            # 如果存在，则直接返回
            return f"{self.base_url}/{endpoint.lstrip('/')}"
        return endpoint
    # 处理响应 
    def _handle_response(self, response: requests.Response) -> requests.Response:
        # 判断响应状态码
        if not response.ok:
            # 抛出异常
            response.raise_for_status()
        return response
    #
    def close(self):
        self.session.close()


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

# # 创建对象
# requester = HttpRequest(base_url=base_url)

# # 发送GET请求 参数：endpoint, params, headers   
# response_get = requester.get(endpoint=endpoint, params=params, headers=headers)

# # 提取 JSON 字符串部分
# json_str =response_get.text.split('(', 1)[1].rstrip(')')

# # 将 JSON 字符串转换为 Python 字典
# json_obj = json.loads(json_str )
# print(json_obj)


# 使用完后关闭会话
# requester.close()
