# 示例代码

# 基本类型转换
int_value = int("123")  # 字符串转整数
int_value1 = int(float("123.45"))  # 字符串小数转整数
float_value = float("3.14")  # 字符串转浮点数
str_value = str(42)  # 整数转字符串
bool_value = bool("True")  # 字符串转布尔值(0以下是false,其他都是true)
print(
    "字符串转整数:",
    int_value,
    "字符串小数转整数:",
    int_value1,
    " 字符串转浮点数:",
    float_value,
    "整数转字符串:",
    str_value,
    "字符串转布尔值",
    bool_value,
)
# 其他类型转换
list_value = list((1, 2, 3))  # 元组转列表
tuple_value = tuple([4, 5, 6])  # 列表转元组
dict_value = dict([("a", 1), ("b", 2)])  # 元组列表转字典
set_value = set("hello")  # 字符串转集合
print("元组转列表",list_value,"列表转元组:", tuple_value,"元组列表转字典:", dict_value,"字符串转集合:", set_value)

# 特殊转换

bytes_value = bytes("我爱你", "utf-8")  # 字符串转字节串
str_bytes=bytes_value.decode("utf-8")   # 字节串转字符串
bytearray_value = bytearray(range(10))  # 整数序列转字节码
print("字符串转字节串:", bytes_value,"字节串转字符串",str_bytes, "整数序列转字节码",bytearray_value)
# 枚举转换（假设已定义枚举类 Color）
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


color_value = Color.GREEN  # 直接访问枚举成员
print(color_value)
