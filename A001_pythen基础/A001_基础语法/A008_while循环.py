my_list = [1, 2, 3, 4, 5]  # 列表

number = 0  # 变量
while number < len(my_list):  # 循环条件

    if my_list[number] == 2:  # 条件判断
        print(my_list[number])
        number += 1  # 自增
        continue # 跳出本次循环
    if my_list[number] == 4:  # 条件判断
        print(my_list[number])
        break # 跳出循环
    number += 1  # 自增
  
