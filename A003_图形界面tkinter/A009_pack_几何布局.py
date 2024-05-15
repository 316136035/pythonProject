import tkinter as tk


# 定义 窗口类 继承自tk.Frame的类。这意味着Application类将拥有tk.Frame类的所有属性和方法  Frame是一个容器类
class Application(tk.Frame):
    # 构造器 # master: 窗口的父容器
    def __init__(self, master=None):
        super().__init__(master, bg="#0066FF")  # super()函数用于调用tk.Frame父类的方法  把Frame容器放到master父容器
        master.title("A009_pack_布局")  # 设置窗口标题
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
        for i in range(1, 10):
            tk.Button(
                self,
                text=f"按钮{i}",
                bg="lightblue",
                fg="black",
                font=("Arial", 12),
                width=10,
                height=2,
            ).pack(side=tk.LEFT, #side: 决定组件是放在父组件的左侧(tk.LEFT)、右侧(tk.RIGHT)、顶部(tk.TOP)还是底部(tk.BOTTOM)。默认是tk.TOP。
                   fill=tk.NONE,#fill: 控制组件在分配给它的空间内如何填充。可选值有tk.NONE(默认，不填充额外空间)、tk.X(填充水平空间)、tk.Y(填充垂直空间)、tk.BOTH(在两个方向上填充)。
                   expand=True,#expand: 布尔值，如果设置为True，则当父组件的大小改变时，该组件会扩展以填充额外的空间。默认是False。
                   padx=10,  pady=10,#padx 和 pady: 分别为组件在水平和垂直方向上的外部间距，即组件与其他组件或父组件边缘之间的空白空间。它们接受整数值。
                   ipadx=0, ipady=0,#ipadx 和 ipady: 分别为组件在水平和垂直方向上的内部间距，即组件内容与其边框之间的空白空间。
                   anchor=tk.NW #anchor: 决定当组件小于分配给它的空间时，组件在该空间内的对齐方式。可选值有tk.NW(西北)、tk.N(北)、tk.NE(东北)、tk.W(西)、tk.CENTER(中心，默认)、tk.E(东)、tk.SW(西南)、tk.S(南)、tk.SE(东南)。
                   )
     
root = tk.Tk()  # 创建主窗口
app = Application(master=root)  # 创建Application对象
app.mainloop()  # 进入消息循环
