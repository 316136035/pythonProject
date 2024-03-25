numbers = [1, 2, 3, 4, 5, 6]
newlist =map(lambda item:item*2,numbers) #map函数(匿名函数 每一个元素:表达式,存入的列表)#返回迭代对象
print(list(newlist))

newlist1=filter(lambda item:item%2==0,numbers) #filter函数(匿名函数 每一个元素:表达式,存入的列表)  #返回迭代对象
print(list(newlist1))