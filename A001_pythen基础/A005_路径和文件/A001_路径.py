import  os
print(os.path.abspath(__file__)) #获取当前文件的绝对路径
print(os.path.dirname(os.path.abspath(__file__))) #获取当前文件的目录
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) #获取当前文件的父目录
print(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))#获取当前文件的父目录
print(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))#获取当前文件的父目录
print(os.path.abspath(__file__) ) # 获取当前模块文件的绝对路径)
