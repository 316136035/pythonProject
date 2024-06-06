import requests
import urllib.parse


# 请求Url
url = "https://qifu-api.baidubce.com/ip/local/geo/v1/district"
# 请求参数
params={"wd":"ip"}

# 请求头
headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Origin": "https://www.baidu.com",
    "Pragma": "no-cache",
    "Referer": "https://www.baidu.com/s?wd=ip地址查询&rsv_spt=1&rsv_iqid=0x813bc93b0000ce7c&issp=1&f=3&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_dl=ts_0&rsv_sug3=5&rsv_sug1=4&rsv_sug7=100&rsv_sug2=1&rsv_btype=i&prefixsug=ip&rsp=0&inputT=6555&rsv_sug4=7436",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"'
}
# 对Referer进行编码
encoded_referer =urllib.parse.quote(headers['Referer']) 
headers["Referer"] = encoded_referer # 更新Referer


# 请求Cookie
cookies={"A":"B"}

proxies={
  "https":"127.0.0.1:8888"
  
}
timeout=10 # 超时时间
verify=False #忽略SSL验证



# 发送请求参数：get请求 带url 带参数 带cookie 带代理 带超时时间 忽略SSL验证
response = requests.get( url,params=params, headers=headers,cookies=cookies,proxies=proxies,timeout=timeout,verify=verify )
# 打印响应信息
print(f"{response.url}---{response.status_code}---{response.encoding}---{response.headers}---{response.cookies}---{response.request.headers}---{response.request.body}---{response.request.url}---{response.request.method}---{response.request.headers}---{response.request.body}---{response.request.url}---{response.request.method}---{response.request.headers}---{response.request.body}")


# 打印响应内容 默认编码是utf-8
print(response.content.decode("utf-8")) 