import tkinter as tk


# 定义 窗口类 继承自tk.Frame的类。这意味着Application类将拥有tk.Frame类的所有属性和方法  Frame是一个容器类
class Application(tk.Frame):
    # 构造器 # master: 窗口的父容器
    def __init__(self, master=None):
        super().__init__(
            master, bg="#0066FF"
        )  # super()函数用于调用tk.Frame父类的方法  把Frame容器放到master父容器
        master.title("A011_place_绝对定位和相对定位_布局.")  # 设置窗口标题
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
        tk.Label(self, text="指定组件左上角的x/y坐标").place(
            x=10,#指定组件左上角的x坐标。
            y=10,#指定组件左上角的y坐标。
            anchor="nw",#指定对齐方式，可以是"N", "S", "E", "W", "NE", "NW", "SE", "SW"等，定义了当组件大小和位置需要调整时以哪个点作为参照。
            width=200,#指定组件的宽度。
            height=50,#指定组件的高度。
            
        )
        tk.Label(self, text="相对于父组件宽度的x/y坐标（0.0到1.0之间的小数）").place(
            relx=0.5,#相对于父组件宽度的x坐标（0.0到1.0之间的小数）
            rely=0.5,#相对于父组件高度的y坐标（0.0到1.0之间的小数）
            relwidth=0.1,#相对于父组件的宽度。（0.0到1.0之间的小数）
            relheight=0.1,#相对于父组件的高度。（0.0到1.0之间的小数）
        )

      
      
        


root = tk.Tk()  # 创建主窗口
app = Application(master=root)  # 创建Application对象
app.mainloop()  # 进入消息循环
