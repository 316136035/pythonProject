import threading
import random
import time

mylocal=threading.local()
mylocal.name="主线程"
class myThread(threading.Thread):
    def __init__(self):
        super().__init__()
        
    def run(self):
        #获取当前线程并获取当前线程的属性
        print("子线程前:",threading.current_thread(),mylocal.__dict__)
        #设置当前线程的属性
        mylocal.name=f"消息/隔离{threading.current_thread().name}"
        #获取当前线程并获取当前线程的属性
        print("子线程后:",threading.current_thread(),mylocal.__dict__)


if __name__ == "__main__":
    thread1 = myThread()
    thread2 = myThread()
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    #获取主线程的属性
    print(mylocal.__dict__)