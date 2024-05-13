import tkinter as tk
import os
from datetime import datetime


# 定义 窗口类 继承自tk.Frame的类。这意味着Application类将拥有tk.Frame类的所有属性和方法  Frame是一个容器类
class Application(tk.Frame):
    # 构造器 # master: 窗口的父容器
    def __init__(self, master=None):
        super().__init__(
            master, bg="lightblue"
        )  # super()函数用于调用tk.Frame父类的方法  把Frame容器放到master父容器
        master.title("A001_窗口定义")  # 设置窗口标题
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

    # 创建窗口组件
    def create_widgets(self):
        self.button_LongIn = tk.Button(
            self,
            text=("按钮"),  # 按钮上显示的文本。
            command=(callable),  # 当按钮被点击时调用的函数。
            bg=('limegreen'),  # 按钮的背景颜色。
            fg=('khaki'),  # 按钮上的文字颜色。
            activebackground=('red'),  # 当鼠标悬停在按钮上时的背景颜色。
            activeforeground=('whitesmoke'),  # 当鼠标悬停在按钮上时的文字颜色。
            font=( ("Arial", 12, "bold")),  # 按钮文本的字体样式，如 ("Arial", 12, "bold")。
            width=(20),  # 按钮的宽度（以字符为单位）。
            height=(200),  # 按钮的高度（以行数为单位）。
            relief=("flat"),  # 按钮边缘样式，如 "flat", "groove", "raised", "ridge", "solid", "sunken"。
            bd=(1),  # 按钮边框的宽度。
            padx=(1),  # 按钮内边距水平方向的空白空间，可以是单个数字或(左, 右)的元组。
            pady=( 1),  # 按钮内边距垂直方向的空白空间，可以是单个数字或(上, 下)的元组。
            anchor=('center'),  # 文本相对于按钮的位置，如 "n", "ne", "e", "se", "s", "sw", "w", "nw", "center"。
            state=('active'),  # 按钮的状态，如 "normal", "active", "disabled"。
            compound=("top"),  # 文本和图像的组合方式，如 "top", "bottom", "left", "right", "center"，当同时有文本和图像时使用。
            # textvariable=(StringVar),  # 与一个Tkinter变量绑定，使得按钮上的文本可以动态更新。
            underline=(1),  # 按钮文本下划线的起始位置，从0开始计数。
        )

    #  image =(PhotoImage),#设置按钮的图像，如果同时设置了 bitmap，则忽略此选项。
    #  ibitmap =(BitmapImage),:#设置位图图像，如果设置了 image，则忽略此选项。

    def LongIn(self):
        print("登录")


root = tk.Tk()  # 创建主窗口
app = Application(master=root)  # 创建Application对象
app.mainloop()  # 进入消息循环
