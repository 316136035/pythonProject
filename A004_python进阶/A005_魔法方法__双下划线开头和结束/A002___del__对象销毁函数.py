class Stu:
  def __init__(self,name,age) -> None:
      self.name = name
      self.age = age    
      self.f=open('test.txt','w')  # 打开文件
  def __del__(self):
    self.f.close() # 关闭文件
    print("对象销毁")
    
  

stu = Stu('张三',18)
new_stu=stu  # 引用计数+1
del stu  #这样是销毁不了对象  因为有引用
