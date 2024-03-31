is_Str = input("请求输入0-3字符")
# 单分支判断
if is_Str == "0":
    print("单分支判断")


# 双分支判断
if is_Str == "0":
    print("双分支判断0")
else:
    print("双分支判断输入错误")


# 多分支判断
if is_Str == "0":
    print("多分支判断0")
elif is_Str == "1":
    print("多分支判断1")
elif is_Str == "2":
    print("多分支判断2")
elif is_Str == "3":
    print("多分支判断3")
else:
    print("多分支判断输入错误")


# 等值判断
match is_Str:
     case "0":
        print("等值判断0")
     case "1":
        print("等值判断1")
     case "2":
        print("等值判断2")
     case "3":
        print("等值判断3")
     case _:
        print("等值判断--输入错误")


age = int(17)
is_adult = "Adult" if age >= 18 else "Minor" #如果 age 大于等于18，is_adult 将被赋值为 "Adult"；否则，它将被赋值为 "Minor"。
print(is_adult)
