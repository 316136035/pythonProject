class Stu:
  def __init__(self,name,age) -> None:
    self.name = name
    self.age = age
  
  def sleep(self):
    print(f'{self.name}正在睡觉')

  def eat(self):
    print(f'{self.name}正在吃饭')

    
stu = Stu('张三',18)








