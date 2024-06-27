from concurrent.futures import ThreadPoolExecutor
import time


def myThread(n):
    print('线程%d开始执行' % n)
    time.sleep(2)
    print('线程%d执行结束' % n)
    return n



if __name__ == '__main__':
    # 创建线程池 线程池最大线程数3
    with ThreadPoolExecutor(max_workers=3) as executor:
        for i in range(10):
            executor.submit(myThread, i)