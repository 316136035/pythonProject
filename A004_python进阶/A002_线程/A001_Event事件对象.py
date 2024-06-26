import threading 
import time

# 创建线程 继承线程父类
class MyThread(threading .Thread):
    # 重写构造方法
    def __init__(self,event,number, name):
        """初始化线程"""
        super().__init__()  # 调用父类初始化方法
        self.event=event # 线程事件
        self.number = number
        self.name = name # 线程名称
        

    def run(self):
        time.sleep(self.number) # 线程休眠
        print("准备执行：{}".format(self.name)) # 输出线程名称
        """线程执行的操作在此方法定义"""
        self.event.wait() # 等待事件触发 会阻塞主线程
        print("执行线程：{}".format(self.name)) # 输出线程名称
        return self.name
        
        
if __name__ == '__main__':
    # 创建事件
    event=threading.Event()
    myThreads=[]
    for i in range(5): # 创建5个线程
        # 创建线程
        myThreads.append(MyThread(event,i,"线程{}".format(i)))

    event.clear() # 重置事件对象
    # 启动线程
    startThreads = [myThread.start() for myThread in myThreads]
    time.sleep(1)
    event.set()  # 触发事件
    # 等待线程结束 保证线程顺序输出
    joinThreads = [myThread.join() for myThread in myThreads] 
    
    
    
    print("主线程结束")