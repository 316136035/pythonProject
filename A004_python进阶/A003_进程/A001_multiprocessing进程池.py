import multiprocessing
import time

def myProcess(time_sleep):
    print(f'进程:{multiprocessing.current_process().name}----开始执行任务{time_sleep}')
    time.sleep(time_sleep)
    print(f'进程:{multiprocessing.current_process().name}----执行完毕{time_sleep}')
    return f"完成{time_sleep}"
    
    
if __name__ == '__main__':
    # 创建进程池，根据CPU核心数量确定进程池大小
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    
    # 异步执行任务
    result_future = pool.apply_async(myProcess, args=(2,))
    
    # 关闭进程池，阻止添加新的任务
    pool.close()
    
    # 等待所有进程执行完毕
    pool.join()
    
    # 获取并打印结果（如果需要处理结果的话）
    result = result_future.get()
    print(result)