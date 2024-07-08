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
                    # return await response.text() # 返回响应的文本内容
                    return await {response.status} 
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
        async with aiohttp.ClientSession(timeout=self.timeout) as session:
            tasks = [self._request(session, **data) for data in requests_data]

            for future in asyncio.as_completed(tasks):
                # 对每个完成的任务绑定回调函数，处理其结果
                asyncio.create_task(self._callback(future))
            
            # 等待所有任务的回调函数执行完毕，这里可选，取决于回调函数是否异步且有后续依赖
            await asyncio.gather(*[task for task in asyncio.all_tasks() if task is not asyncio.current_task()])

# 主函数，用于启动异步请求处理
def main():
    requests_data = [
    {"url": f'http://example.com?id={idx}', "params": {'key1': f'value{idx}'}, "cookies": {'cookie1': f'value{idx}'}}
    for idx in range(1, 51)
    ]
    handler = AsyncRequestHandler() # 实例化异步请求处理类
    asyncio.run(handler.execute_requests(requests_data)) # 运行异步请求执行方法

if __name__ == "__main__": # 当脚本直接运行时
    main() # 调用主函数