import random
import string

def generate_unique_random_strings(length, seed_value, count):
    # 设置固定的随机种子
    random.seed(seed_value)

    # 定义可用字符集
    chars = string.ascii_lowercase

    # 创建一个集合用于存储已生成过的字符串，防止重复
    generated_strings = set()

    result = []

    for _ in range(count):
        while True:
            # 生成随机字符串
            random_string = ''.join(random.choices(chars, k=length))

            # 检查是否已生成过此字符串，若未生成过，则添加到结果列表中
            if random_string not in generated_strings:
                generated_strings.add(random_string)
                result.append(random_string)
                break

    return result

# 使用示例
length = 5
seed_value = 42
count = 10
unique_random_strings = generate_unique_random_strings(length, seed_value, count)

print(unique_random_strings )