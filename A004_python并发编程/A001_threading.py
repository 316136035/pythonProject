import threading
import time

# 定义一个全局变量作为共享资源
counter = 0
# 创建一个锁对象
counter_lock = threading.Lock()

def increment_counter(num_times):
    """
    增加计数器的值num_times次
    """
    global counter
    for _ in range(num_times):
        with counter_lock:  # 使用上下文管理器自动获取和释放锁
            counter += 1
            time.sleep(1)  # 模拟耗时操作

def print_counter():
    """
    打印当前计数器的值
    """
    global counter
    with counter_lock:
        print(f"Counter value: {counter}")

# 创建线程
t1 = threading.Thread(target=increment_counter, args=(5,))
t1.daemon = True # 设置为守护线程，主程序退出时自动结束 (默认为False)
t1.setName("Thread 1")

t2 = threading.Thread(target=increment_counter, args=(5,))
t1.daemon = True # 设置为守护线程，主程序退出时自动结束 (默认为False)
t1.setName("Thread 2")


# 启动线程
t1.start()
t2.start()

# 等待线程完成   join()方法会阻塞当前线程，直到指定的线程完成
t1.join()
t2.join()

# 在所有线程完成后打印最终计数器值
print_counter()