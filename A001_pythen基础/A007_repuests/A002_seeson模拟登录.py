import requests
import urllib.parse


# 请求Url
url = "https://passport.jd.com/uc/login"
# 请求参数
params={}

# 请求头
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}
# 对Referer进行编码
# encoded_referer =urllib.parse.quote(headers['Referer']) 
# headers["Referer"] = encoded_referer # 更新Referer


#请求Cookie
cookies={}

proxies={ }
timeout=10 # 超时时间
verify=False #忽略SSL验证


session=requests.session()

# 发送请求参数：get请求 带url 带参数 带cookie 带代理 带超时时间 忽略SSL验证
response = session.get( url,params=params, headers=headers,cookies=cookies,proxies=proxies,timeout=timeout,verify=verify )
# 打印响应信息
print(f"{response.url}---{response.status_code}---{response.encoding}---{response.headers}---{response.cookies}---{response.request.headers}---{response.request.body}---{response.request.url}---{response.request.method}---{response.request.headers}---{response.request.body}---{response.request.url}---{response.request.method}---{response.request.headers}---{response.request.body}")


# 打印响应内容 默认编码是utf-8
print(response.content.decode("GBK")) 