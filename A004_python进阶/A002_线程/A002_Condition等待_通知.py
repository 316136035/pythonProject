import threading
import random
import time

# 定义最大缓冲区大小
MAX_BUFFER_SIZE = 5

# 用于存储共享数据的类，包括缓冲区和条件变量
class SharedData:
    def __init__(self):
        # 缓冲区用于存放生产的产品
        self.buffer = []
        # 条件变量用于线程间的同步
        self.condition = threading.Condition()

# 生产者类
class Producer:
    def __init__(self, id, shared_data):
        # 生产者的标识符
        self.id = id
        # 生产者访问的共享数据
        self.shared_data = shared_data

    def produce(self):
        for i in range(10):  # 每个生产者生产10个产品
            product = f"创建产品 {self.id}-{i}"  # 创建产品
            print(f"生产信息 {product}") # 打印生产信息
            
            # 使用条件变量确保线程安全
            with self.shared_data.condition: # 获取条件变量锁
                # 当缓冲区满时，生产者等待
                while len(self.shared_data.buffer) == MAX_BUFFER_SIZE:
                    print(" 打印缓冲区满信息") # 打印缓冲区满信息
                    self.shared_data.condition.wait() # 等待
                    
                # 将产品添加到缓冲区 #
                self.shared_data.buffer.append(product)
                # 打印生产信息
                print(f"制作 {product}, 缓冲区大小: {len(self.shared_data.buffer)}")
                
                # 通知消费者有新商品
                self.shared_data.condition.notify_all() # 通知
                
            # 模拟生产过程需要的时间
            time.sleep(random.uniform(0.1, 0.5))

# 消费者类
class Consumer:
    def __init__(self, id, shared_data):
        self.id = id  # 消费者的标识符
        self.shared_data = shared_data  # 消费者访问的共享数据

    def consume(self):
        for _ in range(10):  # 每个消费者消费10次
            with self.shared_data.condition:
                # 当缓冲区空时，消费者等待
                while not self.shared_data.buffer:
                    print("缓冲区为空，消费者正在等待")
                    self.shared_data.condition.wait() # 等待
                    
                # 从缓冲区取出并消费第一个产品
                product = self.shared_data.buffer.pop(0)
                print(f"消耗量 {product} 按消费者 {self.id}, 缓冲区大小: {len(self.shared_data.buffer)}")
                
                # 通知生产者可以生产更多产品
                self.shared_data.condition.notify_all() # 通知
                
            # 模拟消费过程需要的时间
            time.sleep(random.uniform(0.1, 0.5))

def main():
    # 初始化共享数据
    shared_data = SharedData()
    
    # 创建生产者和消费者实例
    producers = [Producer(i, shared_data) for i in range(3)]  # 创建3个生产者
    consumers = [Consumer(i, shared_data) for i in range(2)]   # 创建2个消费者
    
    # 启动生产者和消费者的线程
    threads = []
    for producer in producers:
        thread = threading.Thread(target=producer.produce)
        threads.append(thread)
        thread.start()
    for consumer in consumers:
        thread = threading.Thread(target=consumer.consume)
        threads.append(thread)
        thread.start()
    
    # 等待所有线程完成
    for thread in threads:
        thread.join()
    
    print("所有生产和消费任务已完成。")

# 程序入口点
if __name__ == "__main__":
    main()