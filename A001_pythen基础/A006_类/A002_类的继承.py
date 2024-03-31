# 定义父类
class Animal:
    def __init__(self, name: str) -> None:
        self.name: str = name

    from typing import List

    # 定义父类


class Animal:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def speak(self, sound: str) -> None:
        print(f"{self.name} says {sound}")


# 子类继承父类Animal，并添加新的属性和方法
class Dog(Animal):
    def __init__(self, name: str, breed: str) -> None:
        super().__init__(name)  # 继承父类的初始化方法
        self.breed: str = breed

    def bark(self) -> None:
        self.speak("Woof")  # 继承并使用父类的speak方法

    # 创建Dog类的实例，并使用继承的和新增的方法


d = Dog("Rex", "Labrador Retriever")
d.speak("Hello")  # 继承的speak方法
d.bark()  # Dog类特有的方法

# 注解在IDE和类型检查工具中提供类型信息，不影响程序的实际运行
