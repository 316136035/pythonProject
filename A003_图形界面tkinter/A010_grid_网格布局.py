import tkinter as tk


# 定义 窗口类 继承自tk.Frame的类。这意味着Application类将拥有tk.Frame类的所有属性和方法  Frame是一个容器类
class Application(tk.Frame):
    # 构造器 # master: 窗口的父容器
    def __init__(self, master=None):
        super().__init__(master, bg="#0066FF")  # super()函数用于调用tk.Frame父类的方法  把Frame容器放到master父容器
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
        for i in range(0, 10):
            tk.Button(
                self,
                text=f"按钮行{i}",
                bg="lightblue",
                fg="black",
                font=("Arial", 12),
                width=10,
                height=2,
            ).grid(row=0 , column=i,#分别指定小部件所在的行和列。行和列的索引从0开始。
                   sticky=tk.W,#控制小部件在其单元格内的对齐方式。可以是tk.N（北/上）、tk.S（南/下）、tk.E（东/右）、tk.W（西/左）的任意组合，或者用tk.NSEW（全部边缘）来填充整个单元格
                   #padx 和 pady:分别设置小部件在水平方向和垂直方向上的外部间距（即与其他小部件或容器边缘的距离）。
                   #ipadx 和 ipady:设置小部件在水平方向和垂直方向上的内部间距（即小部件内容与其边框的距离）。
                   
                   columnspan=1,#columnspan 和 rowspan:让小部件跨越多列或多行。例如，columnspan=2会使小部件横跨两列。
                   #in_:指定小部件将被添加到哪个父容器中，通常省略，因为小部件已经被创建在特定容器中。
                  )
            
        # for i in range(1, 10):
        #     tk.Button(
        #         self,
        #         text=f"按钮例{i}",
        #         bg="lightblue",
        #         fg="black",
        #         font=("Arial", 12),
        #         width=10,
        #         height=2,
        #     ).grid(row=i , column=0 )
            
            
            
        
     
root = tk.Tk()  # 创建主窗口
app = Application(master=root)  # 创建Application对象
app.mainloop()  # 进入消息循环
