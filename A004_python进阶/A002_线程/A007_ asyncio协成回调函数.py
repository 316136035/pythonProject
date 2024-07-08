import asyncio

# 定义一个协程
async def hello_world(x):
    # await等待不会阻塞，模拟耗时操作
    await asyncio.sleep(x)
    return 'Hello World!{}'.format(x) # 返回结果

# 创建协程对象 不会立即执行
coro = hello_world(1)


#定义回调函数 (处理响应结果)
def callback(future):
    print("获取结果:",future.result())
    


# 创建事件循环对象
loop = asyncio.get_event_loop()
try:
    # 分派任务
    # task = loop.create_task(coro)
     # 分派任务 优先使用
    task=asyncio.ensure_future(coro)
    
    # 将回调函数绑定到task上
    task.add_done_callback(callback)
    
    
    # 把任务加入事件循环 运行协程
    loop.run_until_complete(task)

    # 获取结果 (第一中方法)
    # print("获取结果:",task.result())
finally:
    # 关闭事件循环
    loop.close()  
    
    
    