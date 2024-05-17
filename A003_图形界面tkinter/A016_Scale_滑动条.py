import tkinter as tk
from tkinter import IntVar


# 定义 窗口类 继承自tk.Frame的类。这意味着Application类将拥有tk.Frame类的所有属性和方法  Frame是一个容器类
class Application(tk.Frame):
    # 构造器 # master: 窗口的父容器
    def __init__(self, master=None):
        super().__init__(
            master, bg="#0066FF"
        )  # super()函数用于调用tk.Frame父类的方法  把Frame容器放到master父容器
        master.title("A016_Scale_滑动条")  # 设置窗口标题
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
        # 定义IntVar变量
        scale_var = tk.IntVar()  # 更改变量名为scale_var以避免命名冲突
        # 定义Scale滑动条的属性
        scale = tk.Scale(
            root,  # 父容器
            from_=0,  # 滑动条的最小值
            to=100,  # 滑动条的最大值
            orient=tk.HORIZONTAL,  # 方向，HORIZONTAL为水平，VERTICAL为垂直
            length=200,  # 滑动条的长度
            resolution=1,  # 改变的步长
            tickinterval=10,  # 刻度间隔
            showvalue=True,  # 是否显示当前值
           variable=scale_var,  # 绑定的变量，可以是IntVar或DoubleVar
            command=lambda value=scale_var: self.on_scale_change(value),  # 使用value作为参数名称
            )

        # 将滑动条放置到窗口上
        scale.pack(pady=10)
    def on_scale_change(self, value):  # 滑动时调用的回调函数
        print(f"当前值：{value}")
     
    
root = tk.Tk()  # 创建主窗口
app = Application(master=root)  # 创建Application对象
app.mainloop()  # 进入消息循环
