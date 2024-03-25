for i in range(2,100,2):  # 循环变量i   #range(2,100,2)循环范围2-100，步长为2
    if i == 20:  # 判断条件
        print(i)
        continue # 跳出本次循环
    if i == 80:  # 判断条件
        print(i)
        break  # 跳出循环
