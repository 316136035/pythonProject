from collections.abc import Iterable  # 判断对象是否为可迭代对象


list =[1,2,3,4,5,6,7,8,9,10]
#查看列表的方法 是否包含__iter__和__getitem__ 实现了其中一个方法就是可迭代对象
# print("列表:",dir(list))
print("isinstance判断列表是否为可迭代对象:",isinstance(list,Iterable))
print("hasattr判断列表是否为可迭代对象:",hasattr(list,'__getitem__'))

dictionary ={"a":1,"b":"2","c":3}
#查看字典的方法 是否包含__iter__和__getitem__ 实现了其中一个方法就是可迭代对象
# print( "字典:",dir(dictionary))
print("isinstance判断字典是否为可迭代对象:",isinstance(dictionary,Iterable))
print("hasattr判断列表是否为可迭代对象:",hasattr(list,'__getitem__'))

# 定义一个类
class Person:
  def __init__(self,personal):
    self.personal =personal


  # 实现迭代对象  
  # def __iter__(self):
  #       yield self.personal
 
  # 实现迭代对象   item是索引
  def __getitem__(self,item):
    return self.personal[item]


p=Person(["周先生",19 ,"男"])
#查看对象的方法 是否包含__iter__和__getitem__ 不包含这个2个方法 不是可迭代对象
# print("对象:",dir( Person))
#实现了其中一个方法就是可迭代对象
print("isinstance判断对象是否为可迭代对象:",isinstance(p,Iterable))
print("hasattr判断对象是否为可迭代对象:",hasattr(p,'__getitem__'))


for i in Person(p):  # 迭代对象
  print(i)



