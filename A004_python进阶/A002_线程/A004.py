from concurrent.futures import ThreadPoolExecutor,as_completed
import threading
import time


def myThread(Time):
    print(f'线程:{threading.current_thread().name}----开始执行')
    time.sleep(Time)
    print(f'线程:{threading.current_thread().name}----执行完毕')
    return Time



if __name__ == '__main__':
    url=[10,2,3,4,5,6,7,8,9]
    # 创建线程池 线程池最大线程数3
    executor =ThreadPoolExecutor(max_workers=3) 
    # 提交任务
    add_task = []  # 初始化一个空列表来保存Future对象
    for i in url:
        
        task = executor.submit(myThread, i)  # 提交任务并获取Future对象
        add_task.append(task)  # 将Future对象添加到列表中

        # 获取线程执行结果 谁提交执行完毕就先返回
    for future in as_completed(add_task):
        print(future.result()) # 获取线程执行结果 阻塞
        
    print('主线程执行完毕')