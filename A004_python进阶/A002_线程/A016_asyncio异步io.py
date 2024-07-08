import asyncio # 导入异步IO库，用于支持异步操作
import aiohttp # 导入aiohttp库，用于异步HTTP请求
import random # 导入random库，用于生成随机数

# 异步请求处理类
class AsyncRequestHandler:
    def __init__(self, max_concurrent_requests=3): # 初始化方法，设置最大并发请求数量，默认为3
        self.semaphore = asyncio.Semaphore(max_concurrent_requests) # 创建信号量对象，控制并发数
        self.timeout = aiohttp.ClientTimeout(total=60) # 创建超时策略，设置总的超时时间为60秒

    # 内部异步请求处理方法
    async def _request(self, session, url, params, cookies):
        async with self.semaphore: # 使用信号量控制并发，避免超过最大并发数
            print(f"开始执行请求: {url}") # 打印开始请求的信息
            try:
                async with session.get(url, params=params, cookies=cookies) as response: # 发起异步GET请求
                    await asyncio.sleep(random.randint(10, 15)) # 模拟网络延迟，等待随机时间（10到15秒）
                    print(f"请求完成: {url}，状态码: {response.status}") # 打印请求完成的信息和状态码
                    return await response.text() # 返回响应的文本内容
            except aiohttp.ClientError as e: # 捕获aiohttp客户端错误
                print(f"请求{url}时发生错误: {e}") # 打印错误信息
    async def _callback(self, future):
        """处理响应结果的回调函数"""
        try:
            result = await future
            print(f"获取结果: {result}")
        except Exception as e:
            print(f"请求失败: {e}")
    # 异步请求执行方法，用于发起批量异步请求
    async def execute_requests(self, requests_data):
        async with aiohttp.ClientSession(timeout=self.timeout) as session: # 创建aiohttp会话，设置超时策略
            tasks = [self._request(session, **data) for data in requests_data] # 创建任务列表，每个数据项转化为一个请求任务
                        # 使用asyncio.as_completed来监控任务完成状态
            for future in asyncio.as_completed(tasks):
                # 对每个完成的任务绑定回调函数
                asyncio.create_task(self._callback(future))

# 主函数，用于启动异步请求处理
def main():
    requests_data = [ # 请求数据列表
        {"url": 'http://example1.com', "params": {'key1': 'value1'}, "cookies": {'cookie1': 'value1'}},
        {"url": 'http://example2.org', "params": {'key2': 'value2'}, "cookies": {'cookie2': 'value2'}},
        {"url": 'http://example3.net', "params": {'key3': 'value3'}, "cookies": {'cookie3': 'value3'}},
        {"url": 'http://example4.com', "params": {'key1': 'value1'}, "cookies": {'cookie1': 'value1'}},
        {"url": 'http://example5.org', "params": {'key2': 'value2'}, "cookies": {'cookie2': 'value2'}},
        {"url": 'http://example6.net', "params": {'key3': 'value3'}, "cookies": {'cookie3': 'value3'}}
    ]
    handler = AsyncRequestHandler() # 实例化异步请求处理类
    asyncio.run(handler.execute_requests(requests_data)) # 运行异步请求执行方法

if __name__ == "__main__": # 当脚本直接运行时
    main() # 调用主函数