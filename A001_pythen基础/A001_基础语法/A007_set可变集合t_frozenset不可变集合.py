"""
集合内的元素没有特定的顺序，每次迭代或者打印可能得到不同的顺序。
集合内的元素不允许重复，添加重复元素不会改变集合的大小。
可变性/不可变性：Python中有两种类型的集合：
      可变集合（set）：可以通过添加新元素、删除已有元素等方式直接修改集合内容。
      不可变集合（frozenset）：一旦创建就不能修改，但它仍然可以作为其他集合操作的元素或参与集合运算。

集合的一些常见操作包括：
添加元素：s.add(element)
移除元素：s.remove(element)
集合合并（并集）：s.union(other_set)
交集：s.intersection(other_set)
差集：s.difference(other_set)
对称差集：s.symmetric_difference(other_set)
检查是否为子集或超集：s.issubset(other_set) 或 s.issuperset(other_set)
清空集合：s.clear()
此外，集合还支持成员测试操作（如 in 和 not in），以及转换为列表或其他序列类型的操作。
  """
lst = [1, 2, 2, 3, 4, 4, 5]
unique_lst = set(lst)  # 结果为 {1, 2, 3, 4, 5}
print(type(unique_lst))
print(unique_lst)