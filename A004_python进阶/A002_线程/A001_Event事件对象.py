import threading 
import time

class MyThread(threading .Thread):
    def __init__(self,event, name):
        """初始化线程"""
        super().__init__()  # 调用父类初始化方法
        self.event=event # 线程事件
        self.name = name
        

    def run(self):
        """线程执行的操作在此方法定义"""
        self.event.wait() # 等待事件触发
        print(self.name)
        
        
if __name__ == '__main__':
  # 创建事件
  event=threading.Event()
  
  
  myThread=MyThread(event,"线程1")
  event.clear() # 重置事件对象
  myThread.start() # 启动线程
  time.sleep(5)
  event.set()  # 触发事件
  myThread.join() # 等待线程结束 会阻塞主线程
  print("主线程结束")