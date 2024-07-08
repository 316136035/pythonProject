import time

#定义装饰器
def  decorator(func):
    def inner():
        print("函数执行前") #自定义执行的函数
        start=time.time()
        func()
        end=time.time()
        print("函数执行后:",start-end)  #自定义执行的函数
    return inner  #返回自定义函数 
  
#被装饰的函数
@decorator  # @foor 装饰器同等于func=foor(func)
def func ():
    time.sleep(3)
    print("func")

func() # func=inner()