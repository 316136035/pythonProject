import tkinter as tk
from tkinter import messagebox


# 定义 窗口类 继承自tk.Frame的类。这意味着Application类将拥有tk.Frame类的所有属性和方法  Frame是一个容器类
class Application(tk.Frame):
    # 构造器 # master: 窗口的父容器
    def __init__(self, master=None):
        super().__init__(
            master, bg="#0066FF"
        )  # super()函数用于调用tk.Frame父类的方法  把Frame容器放到master父容器
        master.title("A020_messagebox_简单消息框")  # 设置窗口标题
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
        
        tk.Button(self, text="显示信息性的消息框", command=self.myShowinfo).pack(pady=10)
        tk.Button(self, text="显示警告消息框", command=self.myshowwarning).pack(pady=10)
        tk.Button(self, text="显示错误消息框。", command=self.myshowerror).pack(pady=10)
        tk.Button(self, text="询问一个问题，用户可以选择Yes或No", command=self.myaskquestion).pack(pady=10)
        tk.Button(self, text="询问用户是否确定操作，返回True或False", command=self.myaskokcancel).pack(pady=10)
        tk.Button(self, text="询问用户是或否，返回True或False。", command=self.myaskyesno).pack(pady=10)
        tk.Button(self, text="询问用户是否重试操作，返回True或False。", command=self.myaskretrycancel).pack(pady=10)
       
    def myShowinfo (self):
        messagebox.showinfo("标题", "信息")
    def myshowwarning (self):
        messagebox.showwarning("标题", "警告")
    def myshowerror (self):
        messagebox.showerror("标题", "错误")
    def myaskquestion (self):
        b=messagebox.askquestion("标题", "询问一个问题，用户可以选择Yes或No")
        print(b)
        
    def myaskokcancel(self):
        b=messagebox.askokcancel("标题", "询问用户是否确定操作，返回True或False")
        print(b)
    def myaskyesno(self):
        b=messagebox.askyesno("标题", "询问用户是或否，返回True或False。")
        print(b)
    def myaskretrycancel(self):
        b=messagebox.askretrycancel("标题", "询问用户是否重试操作，返回True或False。")
        print(b)
        
   
   
   
       

root = tk.Tk()  # 创建主窗口
app = Application(master=root)  # 创建Application对象
app.mainloop()  # 进入消息循环
