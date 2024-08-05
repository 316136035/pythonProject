x=1
exec('x=10+20') #执行字符串不会返回值
exec('print(x)') #执行字符串不会返回值

exec('list = [1,2,3]\nlist.append(4)' ) #执行字符串 转换代码伪数组
exec('print(list)')
print(type(list)) #<class 'list'>


str = "stu = {'name': '周先生', 'age': 18}"
exec(str)
print(type(stu))  # 注意这里打印的是 stu 的类型 dict