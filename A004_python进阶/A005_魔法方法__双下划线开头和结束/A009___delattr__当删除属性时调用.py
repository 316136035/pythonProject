class Stu:
  def __init__(self,name,age) -> None:
    self.name = name
    self.age = age
  def __delattr__(self, name: str) -> None:
    print("删除属性",name)
    
    
stu=Stu("张三",1)
del stu.name