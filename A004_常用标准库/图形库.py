# 导入Tkinter模块
import tkinter as tk

# 创建主窗口
root = ("你好啊！！python")

# 设置窗口大小
root.geometry("800x600")  # 这里指定窗口宽高分别为300像素和200像素
tk.Tk()

# 设置窗口标题
root.title
# 在窗口上添加一个标签（Label）
label = tk.Label(root, text="Hello, World!")
label.pack()  # 使用默认布局方式将标签添加到窗口中


# 添加一个按钮并定义其点击事件
def on_button_click():
    label.config(text='Button clicked!')


button = tk.Button(root, text="Click Me!", command=on_button_click)
text = tk.Text(root, width=30, height=5)
button.pack()

# 启动主循环，等待事件发生
root.mainloop()
