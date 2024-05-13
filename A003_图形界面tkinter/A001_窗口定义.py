import tkinter as tk
from tkinter import messagebox
#定义 窗口类 继承自tk.Frame的类。这意味着Application类将拥有tk.Frame类的所有属性和方法  Frame是一个容器类
class Application(tk.Frame):
    # 构造器 # master: 窗口的父容器
    def __init__(self, master=None):
        super().__init__(master,bg="lightblue")  # super()函数用于调用tk.Frame父类的方法  把Frame容器放到master父容器
        master.title("A001_窗口定义")  # 设置窗口标题
        self.master = master  # 设置窗口父容器
        self.center_window(800,600) # 调用窗口居中函数
        self.create_widgets()# 调用窗口组件函数
        self.pack(fill=tk.BOTH, expand=True )  # 设置容器类布局 通过fill=tk.BOTH），而且当父容器的大小发生变化时，Frame也会随之扩大以继续填充父容器（通过expand=True）

    # 定义一个函数，用于将窗口居中于屏幕 参数：root：窗口实例，width：窗口宽度，height：窗口高度
    def center_window(self,width, height):
        """将窗口居中于屏幕"""
        screen_width = root.winfo_screenwidth()# 获取屏幕宽度
        screen_heigh = root.winfo_screenheight()# 获取屏幕高度
        x_coordinate = int((screen_width / 2) - (width / 2))  # 计算窗口的x坐标
        y_coordinate = int((screen_heigh  / 2) - (height / 2))  # 计算窗口的y坐标
        self.master.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")  # 设置窗口大小和位置
    # 创建窗口组件
    def create_widgets(self):
        """ 定于窗口标签组件 """
        self.Label = tk.Label(self) # 创建Label组件 并存放到Frame容器中
        self.Label["text"] = "A001_窗口定义Label" # 设置Label组件的文本
        self.Label.pack() # 设置Label组件的布局
        """ 定于窗口按钮组件 """
        self.button=tk.Button(self) # 创建Button组件 并存放到Frame容器中
        self.button["text"]="按钮"     # 设置Button组件的文本
        self.button["command"]=self.button_click # 设置Button组件的点击事件
        self.button.pack()    # 设置Button组件的布局
        """ 定义窗口按钮组件 """
        self.button=tk.Button(self) # 创建Button组件 并存放到Frame容器中
        self.button["text"]="退出"     # 设置Button组件的文本
        self.button["command"]=self.button_Quit # 设置Button组件的点击事件
        self.button.pack()    # 设置Button组件的布局     
    def button_click(self):
         messagebox.showinfo("提示","按钮被点击")
        
        
    def button_Quit(self):
         self.master.destroy() # 销毁主窗口 
        
root = tk.Tk()  # 创建主窗口
app = Application(master=root)  # 创建Application对象
app.mainloop()# 进入消息循环
