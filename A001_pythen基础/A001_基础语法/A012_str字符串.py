str = 'hello world'
print(str.count('l')) #获取字符串中某个字符的个数
print(str.strip(' ')) #去除字符串两边的空格
print(str.find('l')) #获取字符串中某个字符第一次出现的位置
print(str.index('l')) #获取字符串中某个字符第一次出现的位置，如果找不到，则报错
print(str.rfind('l')) #获取字符串中某个字符最后一次出现的位置
print(str.rindex('l')) #获取字符串中某个字符最后一次出现的位置，如果找不到，则报错
print(str.replace('l', 'x')) #替换字符串中某个字符
print(str.split(' ')) #将字符串按某个字符分割成多个字符串
print(str.split(' ', 1)) #将字符串按某个字符分割成多个字符串，最多分割几个
print(str.startswith('h')) #判断字符串是否以某个字符开头
print(str.endswith('d')) #判断字符串是否以某个字符结尾
print(str.upper()) #将字符串中的所有字符转换为大写
print(str.lower()) #将字符串中的所有字符转换为小写
print(str.capitalize()) #将字符串中的第一个字符转换为大写