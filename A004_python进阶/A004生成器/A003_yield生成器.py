def countdown(value):
    # 生成器函数
    while value > 0:
        # yield语句 中断函数执行 等待下次循环从yield语句后面处开始执行
        new_value=yield value
        # 如果new_value不为None，则将new_value赋值给value
        if new_value is not None:
            # value=new_value
            value = new_value
        else:
            # value-=1
            value -= 1
         
#创建生成器对象    
continue_obj=countdown(10)
# 遍历生成器对象 每次循环都会执行一次yield语句
for item in continue_obj:
  print("打印item:",item)
  if item==10:
    # 将10的值传递给生成器
    continue_obj.send(10)

