# 'r'：读取模式（默认模式），如果文件不存在则抛出异常。
# 'w'：写入模式，如果文件存在则覆盖原内容，不存在则创建新文件。
# 'a'：追加模式，打开文件进行追加操作，如果文件不存在则创建新文件。
# 'x'：独占创建模式，如果文件已存在则失败，否则创建新文件并打开。
# 't'：文本模式（默认模式），处理文本文件。
# 'b'：二进制模式，处理二进制文件。
# '+'：可读写模式，可以在同一文件上同时进行读写操作

file = open('test.txt', 'r', encoding='utf-8')  # 打开文件 open(文件路径, 模式, 编码方式)
while True:
    line = file.readline()  # 读取一行
    if not line:  # 当读取到文件末尾时，line为空字符串
         break
    print(line, end='')
file.close()  # 关闭文件

# 使用with语句读取文件 自动,关闭文件,释放资源异常
with open('test.txt', 'r', encoding='utf-8') as withfile:
    while True:  # 读取一行
        line = withfile.readline()  # 当读取到文件末尾时，line为空字符串
        if not line:  # 当读取到文件末尾时，line为空字符串
            break
        print(line, end='')
