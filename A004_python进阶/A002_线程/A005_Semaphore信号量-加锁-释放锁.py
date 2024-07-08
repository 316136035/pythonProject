from concurrent.futures import ThreadPoolExecutor, as_completed,wait
import threading
import time


semaphore=threading.Semaphore(3)

# 定义任务函数
def myThread(Time):
    try:
      semaphore.acquire() #加锁
      print(f'线程:{threading.current_thread().name}----开始执行任务{Time}')
      time.sleep(Time)
      print(f'线程:{threading.current_thread().name}----执行完毕{Time}')
      return f"完成{Time}"
    finally:
       semaphore.release() #释放锁


# 取消所有任务
def cancel_all_tasks(executor, futures):
    for future in futures:
        if not future.done():  # 只尝试取消未完成的任务
            future.cancel() 
    executor.shutdown(wait=False)  # 立即关闭线程池，不等待任务完成

if __name__ == '__main__':
    # 示例任务列表
    url = list(range(1, 21)) 
    # 创建线程池
    executor = ThreadPoolExecutor(max_workers=10)

    # 提交任务并保存Future对象
    add_task = [executor.submit(myThread, i) for i in url]

    # 处理已完成的任务，同时监控是否需要取消所有任务
    cancel_tasks = False  # 初始化取消任务标志
    # as_completed 遍历已完成的任务，优先处理先完成任务的返回值  
    # map 遍历已完成的任务，按线程提交的顺序返回值  
    for future in as_completed(add_task):
        # print(f"判断任务是否完成:{future.done()}") # 判断任务是否完成  
        # print(f"判断任务是否取消:{future.cancelled()}") # 判断任务是否取消
        # print(f"任务状态：{future.running()}") # 判断任务是否正在运行
        print(f"返回值：{future.result(1)}") # 获取任务返回值会阻塞直到任务完成  参数为超时时间，超时返回None
        time.sleep(1)  # 模拟检查条件的时间延迟
        # 假设基于某些逻辑条件决定是否取消
        if not cancel_tasks :  # 替换some_condition()为实际的判断条件
            cancel_tasks = True
            print("尝试取消所有任务...")
            cancel_all_tasks(executor, add_task)  # 传递executor以关闭线程池
            print("所有任务取消请求已发送。")
            break  # 已经发起取消并关闭线程池，跳出循环

    # 如果没有触发取消，确保最终关闭线程池
    if not cancel_tasks:
        executor.shutdown(wait=True)  # 等待所有任务完成再关闭线程池
    
    # wait() # 阻塞等待所有任务完成 
    print("主线程执行完毕")