import tkinter as tk


# 定义 窗口类 继承自tk.Frame的类。这意味着Application类将拥有tk.Frame类的所有属性和方法  Frame是一个容器类
class Application(tk.Frame):
    # 构造器 # master: 窗口的父容器
    def __init__(self, master=None):
        super().__init__(
            master, bg="#0066FF"
        )  # super()函数用于调用tk.Frame父类的方法  把Frame容器放到master父容器
        master.title("A010_grid_网格布局")  # 设置窗口标题
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
        # 输入框 参数：父容器 列数 行数 列宽 行高
        tk.Entry(self).grid(row=0, column=0, columnspan=4, pady=10, padx=10)
        button_text = (
            ("MC", "MR", "M+", "M-"),
            ("C", "*", "/", "+"),
            ("7", "8", "9", "-"),
            ("4", "5", "6", "+"),
            ("1", "2", "3", "="),
            ("0", "."),
        )
        # 循环创建按钮
        for index, columns_text in enumerate(button_text):
            # 创建列
            for i, text in enumerate(columns_text):
               
                if text == "=": 
                    # 创建按钮 参数：父容器，文本 grid布局参数：列，行 列偏移，多列或多行
                    tk.Button(self, text=text).grid(row=index + 1, column=i, rowspan=2, sticky="NSEW") # 
                elif text == "0":
                     # 创建按钮 参数：父容器，文本 grid布局参数：列，行 列偏移，多列或多行
                    tk.Button(self, text=text).grid(row=index + 1, column=i, columnspan=2, sticky="NSEW")
                elif text == ".":
                     # 创建按钮 参数：父容器，文本 grid布局参数：列，行 列偏移，多列或多行
                    tk.Button(self, text=text).grid(row=index + 1, column=i+1, sticky="NSEW")
                else:
                    tk.Button(self, text=text).grid(row=index + 1, column=i, sticky="NSEW")



root = tk.Tk()  # 创建主窗口
app = Application(master=root)  # 创建Application对象
app.mainloop()  # 进入消息循环
