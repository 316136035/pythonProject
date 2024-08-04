from typing import Any


class Stu:
  def __init__(self,name,age) -> None:
    self.name = name
    self.age = age
    
  # 重写函数当设置属性事调用
  # key:属性名 value:属性值
  def __setattr__(self, key, value) -> None:
    print(key,value)
    if key == 'age':
      if value < 0: # 负数
        raise ValueError('年龄不能为负数') # 抛出异常
      else:
          self.__dict__[key] = value
    else:
        self.__dict__[key] = value #设置属性 添加到字典中 不能用self.age=value 会死循环

stu=Stu("张三",1)

stu.__dict__["gender"]="男" # 添加属性 这样不会调用__setattr__
print(stu.gender)