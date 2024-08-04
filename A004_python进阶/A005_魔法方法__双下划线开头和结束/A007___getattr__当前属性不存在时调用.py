
from typing import Any


class Stu:
  def __init__(self,name,age) -> None:
    self.name = name
    self.__age = age
    
  #重写函数当前属性不存在时调用
  def __getattr__(self, name) :
    print("当前属性不存在时调用")
    return name
  
  
stu=Stu("张三",18)
stu.xxx