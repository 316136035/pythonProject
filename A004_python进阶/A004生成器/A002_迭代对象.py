from itertools import count # 迭代器
from collections.abc import Iterable  # 判断对象是否为可迭代对象

counter = count(10)



print("查看类型:",type(counter))
 # 判断对象是否为可迭代对象
if isinstance(counter,Iterable) and hasattr(counter,'__next__'):
  print("可迭代对象")
  
for i in range(10): 
  # 获取下一个值 这个是迭代器 没有索引值
  print(next(counter)) 


# print(len(counter)) # 获取长度会报错

 
