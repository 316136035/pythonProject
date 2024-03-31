d = dict()  # 创建空对象
# 创建对象
object = {"name": "猴子", "gender": False, "age": 19}
object["key"] = "value"  # 添加属性/修改
print(object)
print(object["name"])  # 通过属性获取属性值
print(object.get("name"))# 通过属性获取属性值
object.update( {"name": "猴子", "gender": False, "age": 19}) #修改对象

print("name" in object)  # 判断对象是否有这个属性
for key in object:  # 遍历对象
    print(object[key])

print(object.items())  # 转成列表
for key, value in object.items():  # 转成列表再遍历对象
    print(key, value, sep="----")


for key in object.keys():  # 转成keys列表再遍历对象
    print(key)
for value in object.values():  # 转成value s列表列表再遍历对象
    print(value)

object.pop("key") #移除属性
object.popitem() #移除属性后面开始删除

# object.clear()#清空对象
o1=object.copy() #克隆对象 克隆过程创建了一个新的对象实例。
print(o1 is object) #判断对象地址是否相等



