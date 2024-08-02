class Stu :
  num=0 # 类属性 共享的
  def __init__(self,name,age) -> None:
    self.name = name
    self.__age = age
  def __repr__(self) -> str:
    return '我是%s,今年%d岁' % (self.name,self.__age)
  
stu=Stu('张三',18)
print(stu)
print("-------------------------")
print(stu.__dict__) # 获取实例的所有属性并打印
print("-------------------------")
print(Stu .__dict__) # 获取类属性并打印 

print("-------------------------")
stu.__dict__['name']='李四' # 修改实例属性
print(stu.__dict__['name']) # 获取实例属性

stu.__dict__['gender']='男' # 添加实例属性
print(stu.__dict__) # 获取实例属性
 