class Stu :
    def __init__(self,name,age) -> None:
        self.name = name
        self.__age = age   #伪私有属性 不能使用stu.__age 获取要用_Stu__age
    def __repr__(self) -> str:
        return f'{self.name} {self.age}'
      
stu=Stu('张三',18)

print(dir(stu)) # 输出对象的属性和方法 内部调用了__dir__ 函数 做了排序返回列表
print("-------------------------")
print(stu.__dir__()) # 输出对象的属性和方法
print("-------------------------")
print(dir(Stu)) # 输出类属性和方法  不包含实例的属性
print(stu._Stu__age)  #伪私有属性 不能使用stu.__age （__类名__属性名）
