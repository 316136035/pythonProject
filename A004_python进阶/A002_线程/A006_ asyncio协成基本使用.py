import asyncio

# 定义一个协程
async def hello_world():
    # await等待不会阻塞，模拟耗时操作
    await asyncio.sleep(1)
    print('Hello World!')

# 创建协程对象 不会立即执行
coro = hello_world()

# 检查类型
print(type(coro))          # 输出：<class 'coroutine'>
print(asyncio.iscoroutine(coro))  # 检查是否是协程对象 输出：True

# 创建事件循环对象
loop = asyncio.get_event_loop()
try:
    # 分派任务
    # task = loop.create_task(coro)
     # 分派任务 优先使用
    task=asyncio.ensure_future(coro)
    # 把任务加入事件循环 运行协程
    loop.run_until_complete(task)
finally:
    # 关闭事件循环
    loop.close()  