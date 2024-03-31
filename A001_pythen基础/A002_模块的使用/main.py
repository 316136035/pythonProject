
import show # 导入整个模块
my_list = [1, 2, 3, 4, 5]
show.print_python_list(my_list) # 调用模块中的函
print(show.auto) # 调用模块中的变量

# 导入模块中的函数和变量
from show import print_python_list, auto 
my_list = [1, 2, 3, 4, 5]
print_python_list(my_list)
print(auto)