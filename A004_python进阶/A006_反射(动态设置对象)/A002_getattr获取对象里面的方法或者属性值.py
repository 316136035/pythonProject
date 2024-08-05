class Stu:
  def __init__(self,name,age) -> None:
    self.name = name
    self.age = age
  
  def sleep(self):
    print(f'{self.name}正在睡觉')

  def eat(self):
    print(f'{self.name}正在吃饭')

    
stu = Stu('张三',18)

inputstr=input('请输入要调用的方法：')

if hasattr(stu,inputstr): # 判断对象里面是否有这个方法
  try:
      fun= getattr(stu,inputstr) # 获取对象里面的方法（不是函数就会直接获取到属性值）
      fun() # 调用方法
  except:
      print( getattr(stu,inputstr)) # 获取对象里面的方法（不是函数就会直接获取到属性值）
else:
  print("对象中没有这个属性或者方法")









