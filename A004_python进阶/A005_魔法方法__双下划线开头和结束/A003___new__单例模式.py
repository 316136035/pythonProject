class Stu:
  __isinstance = False  # 私有属性保存实例
  #重写__new__方法 创建对象 当__new__方法被调用时，会返回一个对象  
  def __new__(cls,*args,**kwargs) :
      if not cls.__isinstance:  # 如果没有被实例化过
      # 调用父类的__new__方法
        cls.__isinstance =super().__new__(cls)
      # 返回对象
      return cls.__isinstance
  # 重写__init__方法  初始化对象 当__init__方法被调用时，会先调用__new__方法
  def __init__(self,name,age):
      self.name = name
      self.age = age    
      print('__init__方法被调用', self.name )


  

stu1 = Stu('张三',18)

stu2 = Stu('李四',18)
print(stu1)
print(stu2)
