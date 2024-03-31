def recursive_function(n):
    """
    递归函数，计算阶乘

    参数:
    n (int): 需要计算阶乘的整数

    返回:
    int: n的阶乘
    """
    # 基本情况：当n为0或1时，阶乘为1
    if n == 0 or n == 1:
        return 1
    # 递归情况：n的阶乘等于n乘以(n-1)的阶乘
    else:
        return n * recursive_function(n - 1)

# 测试递归函数
num = 5
result = recursive_function(num)
print(f"{num}的阶乘为: {result}")
