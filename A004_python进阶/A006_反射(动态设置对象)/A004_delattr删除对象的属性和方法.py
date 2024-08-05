class Stu:
  def __init__(self,name) -> None:
    self.name = name

  def sleep(self):
    print(f'{self.name}正在睡觉')

stu = Stu('张三')



def eat():
  print('正在吃饭')
setattr(stu,'eat',eat)

if hasattr(stu,'eat'):
  delattr(stu,'eat') # 只能删除动态添加的属性或者方法  要删除对象的原有属性或者方法请使用del Stu.sleep
  print(dir(stu))















