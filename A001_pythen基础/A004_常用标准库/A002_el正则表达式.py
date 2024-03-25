import re


def is_valid_id(id_card):
    # 身份证号码正则表达式，简单格式验证
    pattern = r'^\d{6}(18|19|20)?\d{2}(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])\d{3}[\dXx]$'

    # 使用正则表达式验证身份证号码格式
    if re.match(pattern, id_card):
        # 如果仅仅是格式验证通过，这里仅返回True，但实际校验还需要进一步计算校验码
        return True
    else:
        return False


# 测试函数
id_number = '440181199102051211'
print(is_valid_id(id_number))