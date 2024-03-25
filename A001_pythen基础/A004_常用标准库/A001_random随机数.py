import random

# 生成一个0（包含）到1（不包含）之间的随机浮点数
print(random.random())

# 生成一个指定范围内的随机整数，如生成一个0-10之间的随机整数
print(random.randint(0, 10))

# 从序列中随机选取一个元素
my_list = [1, 2, 3, 4, 5]
print(random.choice(my_list))