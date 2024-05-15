import tkinter as tk
import os
import webbrowser


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
        # 使用IntVar来控制Radiobutton的选中状态
        self.is_Radiobutton = tk.IntVar()
        self.Radiobutton_0 = tk.Radiobutton(
            self,
            text="男",  # 设置单选按钮旁边的文本标签。例如：text="Option A"。
            variable=self.is_Radiobutton,  # 这是一个Tkinter变量（如 StringVar, IntVar等），用于存储单选按钮的当前选中状态的值。所有属于同一组的单选按钮应共享同一个变量。例如：variable=var。
            value=1,  # 指定当这个单选按钮被选中时，variable 应该被设置为什么值。例如：value="A"。
            command=self.print_selection,  # 当单选按钮的状态改变（通常是因为用户点击了它）时调用的函数。例如：command=print_selection。
            indicatoron=True,  # 布尔值，决定是否以标准的指示器样式显示单选按钮，默认为 True。如果设为 False，则单选按钮看起来更像一个按钮。例如：indicatoron=False。
            selectcolor="lightblue",  # 选中时的背景色。例如：selectcolor="lightblue"。
            bg="green",  # bg 或 background= ,单选按钮的背景颜色。例如：bg="white"。
            activebackground="red",  # 鼠标悬停或按钮被激活时的背景颜色。
            state="normal",  # 指定单选按钮的状态，可以是 "normal", "disabled" 或 "active"。默认为 "normal"。
            # padx 和 pady: 分别设置文本与单选按钮图形之间的水平和垂直内边距。
            anchor="center",  # 设置文本相对于单选按钮的位置，默认为 "center"。
            bd=1,  # borderwidth 或 bd: 设置单选按钮边框的宽度。
            cursor="hand2",  # 当鼠标悬停在单选按钮上时，光标的形状。
            relief="raised",  # 设置单选按钮的边框样式，可以是 "flat", "groove", "raised", "ridge", "solid", 或 "sunken"。默认为 "flat"。
)
        self.Radiobutton_0.pack(side="left")  # 设置单选按钮在窗口中的位置

        self.Radiobutton_1 = tk.Radiobutton(
            self,
            text="女",  # 设置单选按钮旁边的文本标签。例如：text="Option A"。
            variable=self.is_Radiobutton,  # 这是一个Tkinter变量（如 StringVar, IntVar等），用于存储单选按钮的当前选中状态的值。所有属于同一组的单选按钮应共享同一个变量。例如：variable=var。
            value=0,  # 指定当这个单选按钮被选中时，variable 应该被设置为什么值。例如：value="A"。
            command=self.print_selection,  # 当单选按钮的状态改变（通常是因为用户点击了它）时调用的函数。例如：command=print_selection。
            indicatoron=True,  # 布尔值，决定是否以标准的指示器样式显示单选按钮，默认为 True。如果设为 False，则单选按钮看起来更像一个按钮。例如：indicatoron=False。
            selectcolor="lightblue",  # 选中时的背景色。例如：selectcolor="lightblue"。
            bg="green",  # bg 或 background= ,单选按钮的背景颜色。例如：bg="white"。
            activebackground="red",  # 鼠标悬停或按钮被激活时的背景颜色。
            state="normal",  # 指定单选按钮的状态，可以是 "normal", "disabled" 或 "active"。默认为 "normal"。
            # padx 和 pady: 分别设置文本与单选按钮图形之间的水平和垂直内边距。
            anchor="center",  # 设置文本相对于单选按钮的位置，默认为 "center"。
            bd=1,  # borderwidth 或 bd: 设置单选按钮边框的宽度。
            cursor="hand2",  # 当鼠标悬停在单选按钮上时，光标的形状。
             relief="sunken",  # 设置单选按钮的边框样式，可以是 "flat", "groove", "raised", "ridge", "solid", 或 "sunken"。默认为 "flat"。
        )
        self.Radiobutton_1.pack(side="left")  # 设置单选按钮在窗口中的位置

    def print_selection(self):
        print(self.is_Radiobutton.get())


root = tk.Tk()  # 创建主窗口
app = Application(master=root)  # 创建Application对象
app.mainloop()  # 进入消息循环
