import  time
print(time.time()) # 获取当前时间戳
print(time.strftime("年 %Y-%m-%d %H:%M:%S", time.localtime())) # 获取当前时间
# while True:
#     print(time.strftime("%Y年-%m月-%d日 %H时:%M分:%S秒", time.localtime(time.time()))) # 获取当前时间 %H:%M:%S", time.localtime(time.time()))) # 获取当前时间
#     time.sleep(0.001) # 睡眠1毫秒
#
import  datetime
print(datetime.datetime.now())
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))