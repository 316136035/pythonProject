#def定义函数
def add(x,y=10): #定义函数  默认参数
    return x+y
add(1,2)

#def定义函数
def show (*list): #可变参数
    for i in list:
        print(i,end=" ")
show(*{1,2,3,4,5})

#def定义函数
def show2(**dict): #可变参数 遍历对象
    print(dict)
    for key,value in dict.items(): #遍历对象
        print(key,value)
item={"name":'周先生',"age":18}
show2(**item)   