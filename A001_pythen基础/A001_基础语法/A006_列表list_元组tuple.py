#元组：由于不可变性，Python可以在创建时优化其存储，因此在某些情况下，元组的访问速度可能会更快。
my_tuple =tuple()
my_tuple = (1, True,"字符串", False,1)
print("获取元组中元素的个数:",my_tuple.count("字符串"))
print("获取元组中指定元素的索引:",my_tuple.index(False))


#列表：是可变的，这意味着您可以向列表中添加、删除或更改元素。例如，可以使用append()、extend()、insert()、remove()、pop()等方法操作列表。
my_list = [1, True,"字符串", False]
my_listnode = []
print(my_listnode)
print(my_list)
print("列表长度:",len(my_list))
my_list.append('末尾') #将元素添加到列表的末尾
print("将元素添加到列表的末尾:",my_list)
my_list.insert(2,"指定位置") #在指定位置插入元素
print("在指定位置插入元素:",my_list)
my_list.extend('append') #将字符串扩展到列表中
print("将字符串扩展到列表中:",my_list)
my_list.remove('末尾') #删除列表中的元素
print("删除列表中的元素:",my_list)
my_list.pop(2) #删除指定位置的元素
print("删除指定位置的元素:",my_list)
my_list.reverse() #列表反转
print("列表反转:",my_list)
my_list = my_list + ['末尾']#列表拼接
print("列表拼接:",my_list)
my_list.clear()#清空列表
print("清空列表:",my_list)