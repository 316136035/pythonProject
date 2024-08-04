

class Stu:
  def __init__(self,name,age) -> None:
    self.name = name
    self.__age = age
    
  #重写函数每次访问属性都会调用item:属性名
  def __getattribute__(self, item) :
    try:
      print("__getattribute__被调用了",item)
      #获取属性
      return super().__getattribute__(item)
    except AttributeError as e:
      print(e)
      return "属性不存在"
  
stu=Stu("张三",18)
stu.name
stu.xxx