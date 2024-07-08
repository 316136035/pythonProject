import asyncio

# 定义一个协程
async def coroutines(x):
    # await 等待不会阻塞，模拟耗时操作
    await asyncio.sleep(x)
    return '我是协程!{}'.format(x) # 返回结果

# 定义回调函数 (处理响应结果)
def callback(task):
    print("获取结果:", task.result())

# 创建事件循环对象并运行所有协程
async def main():
    # 创建任务列表
    tasks = [ asyncio.create_task(coroutines(i)) for i in range(1,10) ]
    # 添加回调函数
    for task in tasks:
        # 添加回调函数
        task.add_done_callback(callback)
        
    await asyncio.gather(*tasks)

# 运行事件循环
asyncio.run(main())