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
        
        
        
# 生产者
def producer(consumer,nuber):
    consumer.send(None)
    n = 0
    while n < nuber:
        n = n + 1
        print('生产者 %s...' % n)
        r = consumer.send(n)
        print('生产者接收到 %s' % r)
        time.sleep(1)
    consumer.close()
    
consumer=consumer()  # 创建生成器
producer(consumer,100) # 生产者调用生成器消费
