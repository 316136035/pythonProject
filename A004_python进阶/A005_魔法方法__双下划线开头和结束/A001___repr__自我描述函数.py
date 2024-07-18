class Stu:
  def __init__(self,name,age) -> None:
      self.name = name
      self.age = age
      
      
  # 重写__repr__方法 自我描述函数 当直接打印对象时，会自动调用__repr__方法
  def __repr__(self) -> str:
     return f'姓名：{self.name}，年龄：{self.age}'
   
stu = Stu('张三',18)
print("直接打印：",stu)
print(stu.__repr__())