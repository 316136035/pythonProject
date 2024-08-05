class Stu:
  def __init__(self,name) -> None:
    self.name = name

  def sleep(self):
    print(f'{self.name}正在睡觉')

stu = Stu('张三')


def eat():
  print('正在吃饭')

keyinput=input('请输入属性名')
valueinput=input('请输入属性值')
if valueinput.isdigit(): #判断是否是数字
  setattr(stu,keyinput,int(valueinput)) #设置对象的属性 value转成数字
  print(stu.__dict__) #打印对象
  
funstr=input('请输入方法名')
setattr(stu,funstr,eat) #设置对象的方法参数(对象,方法名,方法)
stu.addeat() #调用对象的方法注意就是输入的方法名















