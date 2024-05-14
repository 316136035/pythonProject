import tkinter as tk
import os
from datetime import datetime
from tkinter import messagebox


# 定义 窗口类 继承自tk.Frame的类。这意味着Application类将拥有tk.Frame类的所有属性和方法  Frame是一个容器类
class Application(tk.Frame):
    # 构造器 # master: 窗口的父容器
    def __init__(self, master=None):
        super().__init__(
            master, bg="lightblue"
        )  # super()函数用于调用tk.Frame父类的方法  把Frame容器放到master父容器
        master.title("A004_Entry_单行输入框组件")  # 设置窗口标题
        self.master = master  # 设置窗口父容器
        self.center_window(800, 600)  # 调用窗口居中函数
        self.create_widgets()  # 调用窗口组件函数
        self.pack(
            fill=tk.BOTH, expand=True
        )  # 设置容器类布局 通过fill=tk.BOTH），而且当父容器的大小发生变化时，Frame也会随之扩大以继续填充父容器（通过expand=True）

    # 定义一个函数，用于将窗口居中于屏幕 参数：root：窗口实例，width：窗口宽度，height：窗口高度
    def center_window(self, width, height):
        """将窗口居中于屏幕"""
        screen_width = root.winfo_screenwidth()  # 获取屏幕宽度
        screen_heigh = root.winfo_screenheight()  # 获取屏幕高度
        x_coordinate = int((screen_width / 2) - (width / 2))  # 计算窗口的x坐标
        y_coordinate = int((screen_heigh / 2) - (height / 2))  # 计算窗口的y坐标
        self.master.geometry(
            f"{width}x{height}+{x_coordinate}+{y_coordinate}"
        )  # 设置窗口大小和位置


    """ height (int): 文本框的高度，以文本行数为单位，默认为一列。

width (int): 文本框的宽度，以字符单位计数，默认值取决于系统。

bg / background (color): 文本框的背景颜色。

fg / foreground (color): 文本的前景色（即文本颜色）。

font (tuple or str): 字体样式，例如("Arial", 12)。

wrap (str): 文本换行方式，可以是"char"（在字符边界换行）、"word"（在单词边界换行）或"none"（不自动换行）。

bd / borderwidth (int): 边框宽度。

relief (str): 边框样式，如"SUNKEN", "RAISED", "GROOVE", "RIDGE", 或 "FLAT"。

insertbackground (color): 插入光标的颜色。

insertwidth (int): 插入光标的宽度。

state (str): 控制文本框的状态，如"normal"（可编辑）、"disabled"（不可编辑）或"readonly"（只读）。

undo (bool): 是否允许撤销/重做功能，默认False。

yscrollcommand (function): 绑定一个滚动条，用于垂直滚动。需要与Scrollbar组件一起使用。

xscrollcommand (function): 绑定一个滚动条，用于水平滚动。同样需要与Scrollbar组件配合使用。 """
    # 创建窗口组件
    def create_widgets(self
                       ):
        
        self.username = tk.StringVar()
        self.Lable_username = tk.Text()

root = tk.Tk()  # 创建主窗口
app = Application(master=root)  # 创建Application对象
app.mainloop()  # 进入消息循环
