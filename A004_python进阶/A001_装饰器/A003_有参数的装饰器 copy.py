import time

#定义装饰器 带参数
def decorator(address):
    print("address:",address) # 打印装饰器传入的参数
    def outer (func):    # 装饰器内部函数
        def inner(*args, **kwargs):
            print("函数执行前")  # 自定义执行前的函数
            start = time.time()
            result = func(*args, **kwargs)  # 确保函数结果被返回
            end = time.time()
            print("函数执行后:", end - start)  # 自定义执行后的函数
            return result  # 返回原始函数的结果
        return inner  
    return outer

@decorator(address="广州")  # @decorator 装饰器同等于decorator=decorator(my_func)
#被装饰的函数
def my_func(*args, **kwargs):  # 给 *args 指定了一个形参名args，保持与装饰器内部调用一致
    time.sleep(1)
    print("被装饰的函数执行了")

    return f"函数执行完毕{args}"  # 添加一个返回值以便观察装饰器是否正确返回结果

result = my_func(1, 2, 3, 4)  # 调用装饰后的函数
print(result)  # 打印函数返回值