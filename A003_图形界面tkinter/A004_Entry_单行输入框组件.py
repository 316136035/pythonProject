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

    # 创建窗口组件
    def create_widgets(self):
        
        self.username = tk.StringVar()
        self.Lable_username = tk.Entry(self,
                                       width=200,# 设置Entry控件的宽度，以平均字符宽度为单位。默认情况下，宽度是20个字符。
                                       textvariable= self.username,# 关联一个Tkinter变量（如StringVar），使得Entry中的文本与该变量的值同步。当Entry中的文本改变时，该变量的值也会自动更新，反之亦然。
                                       font =("Arial", 12),#设置字体样式，例如("Arial", 12)表示使用Arial字体，大小为12。
                                       bg='red',#bg / background (color): 设置Entry背景颜色。
                                       fg="white", #fg / foreground (color): 设置Entry前景（文本）颜色。
                                       bd=1,#bd / borderwidth (int): 设置边框宽度，单位为像素。
                                       relief= 'flat',# 设置边框样式，如"SUNKEN", "RAISED", "GROOVE", "RIDGE", 或 "flat"。
                                       state ='normal',# 控制Entry的状态，如"normal"（可编辑）、"disabled"（禁用）或"readonly"（只读）。
                                       justify ='left',#文本对齐方式，可以是"left", "center", 或 "right"。
                                       show="*",# 当需要隐藏输入内容时（如密码输入框），可以设置为特定字符，如"*"，来代替实际输入的字符。
                                      # validate启用输入验证，配合validatecommand和invalidcommand使用，可以控制何时以及如何验证用户输入。
                                            # "none"：默认值，不进行任何验证。
                                            # "focus"：当Entry失去或获得焦点时触发验证。
                                            # "focusin"：仅当Entry获得焦点时触发验证。
                                            # "focusout"：仅当Entry失去焦点时触发验证。
                                            # "key"：每次按键（按下并释放）后触发验证。
                                            # "all"：每次Entry内容变化时都触发验证，包括粘贴操作。
                                       validate= 'focus',
                                       validatecommand=self.verification,#验证函数，定义输入验证的逻辑。
                                       invalidcommand=self.verification_failed #当验证失败时调用的函数。) # Entry标签组件
        )
        self.Lable_username.pack() # pack()方法用于布局
        self.username = tk.StringVar()# StringVar()用于保存字符串变量
        self.Entry_username = tk.Entry(self, textvariable= self.username, bg="lightblue") # Entry单行输入框组件
        self.Entry_username.pack(fill=tk.X) # pack()方法用于布局

    def verification(value_if_allowed):
        """验证函数示例，这里简单检查输入是否全为字母"""
        if value_if_allowed.isalpha():  # 根据需要自定义验证逻辑
            return True
        else:
            messagebox.showerror("输入错误", "请输入字母！")
            return False

    def verification_failed():
        """验证失败时调用的函数"""
        messagebox.showwarning("警告", "输入未能通过验证，请检查你的输入。")



root = tk.Tk()  # 创建主窗口
app = Application(master=root)  # 创建Application对象
app.mainloop()  # 进入消息循环
