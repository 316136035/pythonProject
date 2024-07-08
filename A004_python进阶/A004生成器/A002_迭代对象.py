from itertools import count # 迭代器
from collections.abc import Iterable  # 判断对象是否为可迭代对象

# 创建迭代器
counter = count(10)

print("查看类型:",type(counter))
 # 判断对象是否为可迭代对象 有__iter__方法和__next__方法 就是迭代器
if isinstance(counter,Iterable) and hasattr(counter,'__next__'):
  print("可迭代对象")
  
for i in range(10): 
  # 获取下一个值 这个是迭代器 没有索引值
  print(next(counter)) 


# print(len(counter)) # 获取长度会报错

class Person(object):
  def __init__(self,personal):
    self.personal =personal
  def __getitem__(self,item):
    return self.personal[item]
 
 
p=Person(["A","B"]) # 创建对象

# print(dir(p)) # 查看对象属性
print(type(p)) # 查看类型
p_iter = iter(p) # 获取对象迭代器
print(type(p_iter)) # 查看类型
# print(dir(p_iter)) # 查看对象属性


for i in p: # 迭代对象
  print(i)

