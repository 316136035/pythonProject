class ClassName:
    # 类变量（Class Variables）: 这些变量属于整个类，所有类的实例共享这些变量的值
    class_variable = "This is a class variable"

    # 构造方法（Constructor）: 初始化一个类实例的特殊方法 self代表是this
    def __init__(self, name , age ):
        # 实例变量（Instance Variables）: 每个类实例有自己的独立副本
        self.name = name
        self.age = age

    # 实例方法（Instance Methods）: 可以通过类实例调用的方法  self代表是this
    def method_name(self):
        # 这里是方法的实现细节
         print('实例方法（Instance Methods）: 可以通过类实例调用的方法  ')

    # 静态方法（Static Methods）: 不需要访问实例变量的方法，可通过类直接调用  self代表是this
    @staticmethod
    def static_method():
       print('静态方法（Static Methods）: 不需要访问实例变量的方法，可通过类直接调用  ')

    # 类方法（Class Methods）: 需要访问类变量，而不是实例变量的方法，可通过类直接调用  self代表是this
    @classmethod
    def class_method(cls):
        print('类方法（Class Methods）: 需要访问类变量，而不是实例变量的方法，可通过类直接调用  ')

# 创建类的实例
instance_of_class = ClassName( 'key', "value")

# 访问类的属性和方法
print(instance_of_class.name) # 输出: key
instance_of_class.method_name() # 输出: 实例方法（Instance Methods）: 可以通过类实例调用的方法
ClassName.class_method()  #类方法（Class Methods）: 需要访问类变量，而不是实例变量的方法，可通过类直接调用

ClassName.class_method() # 输出: 类方法（Class Methods）: 需要访问类变量，而不是实例变量的方法，可通过类直接调用
ClassName.static_method() # 输出: 静态方法（Static Methods）: 不需要访问实例变量的方法，可通过类直接调用