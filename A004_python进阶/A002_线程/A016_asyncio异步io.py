import asyncio # 引入异步io库
import aiohttp # 引入aiohttp库
import random # 引入随机数库

# 创建一个信号量，限制最大并发数为3
semaphore = asyncio.Semaphore(3)

async def async_request(session, url, params, cookies):
    async with semaphore:
        print(f"开始执行请求: {url}")
        try:
            async with session.get(url, params=params, cookies=cookies) as response:
                await asyncio.sleep(random.randint(10, 15))  # 模拟异步请求，等待随机时间
                print(f"请求完成: {url}，状态码: {response.status}")
                return await response.text()
        except aiohttp.ClientError as e:
            print(f"请求{url}时发生错误: {e}")

async def main():
    requests_data = [
        {
            'url': 'http://example1.com',
            'params': {'key1': 'value1'},
            'cookies': {'cookie1': 'value1'}
        },
        {
            'url': 'http://example2.org',
            'params': {'key2': 'value2'},
            'cookies': {'cookie2': 'value2'}
        },
        {
            'url': 'http://example3.net',
            'params': {'key3': 'value3'},
            'cookies': {'cookie3': 'value3'}
        },
                {
            'url': 'http://example4.com',
            'params': {'key1': 'value1'},
            'cookies': {'cookie1': 'value1'}
        },
        {
            'url': 'http://example5.org',
            'params': {'key2': 'value2'},
            'cookies': {'cookie2': 'value2'}
        },
        {
            'url': 'http://example6.net',
            'params': {'key3': 'value3'},
            'cookies': {'cookie3': 'value3'}
        }
        # 可以添加更多请求...
    ]
    
    timeout = aiohttp.ClientTimeout(total=60)  # 设置超时时间为60秒
    async with aiohttp.ClientSession(timeout=timeout) as session:
        tasks = [async_request(session, **data) for data in requests_data]
        responses = await asyncio.gather(*tasks, return_exceptions=True)
        print("所有请求完成，响应结果为：")
        for i, resp in enumerate(responses):
            if isinstance(resp, Exception):
                print(f"请求{i}失败: {resp}")
            else:
                print(f"请求{i}成功，结果为：{resp}")

if __name__ == "__main__":
    asyncio.run(main())