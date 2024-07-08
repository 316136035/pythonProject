import time
# 消费者
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('消费者 %s...' % n)
        r = '200 OK'
        
        
        
# 生产参数 消费者生成器
def producer(consumer):
    # 启动生成器
    consumer.send(None)
    n = 0
    while True:
        n = n + 1
        print('生产者 %s...' % n)
        #发送给消费者消费
        r = consumer.send(n)
        print('生产者接收到 %s' % r)
        time.sleep(1)

    
consumer=consumer()  # 创建生成器
producer(consumer) # 生产者调用生成器消费
