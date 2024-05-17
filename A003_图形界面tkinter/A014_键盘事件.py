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
        """ 键盘按键事件 """
        #<KeyPress>：任意键按下。 <KeyPress-A>按下
        #<KeyRelease>：任意键释放。 <KeyRelease-A>释放
        #<FocusIn>：控件获得焦点。tdh
        #<FocusOut>：控件失去焦点。
        
        self. master.bind("<KeyPress>", self.myCanvas_KeyPress)
        """ 特定键事件 """
        #<Return> 或 <KP_Enter>：回车键或小键盘上的Enter。
        #<Escape>：Esc键。
        #<BackSpace>：退格键。
        #<Tab>：制表符。
        #<Shift_L>/<Shift_R>：左/右Shift键。
        #<Control_L>/<Control_R>：左/右Ctrl键。
        #<Alt_L>/<Alt_R>：左/右Alt键。
        #<Delete>：删除键。
        #<Up>/<Down>/<Left>/<Right>：上下左右箭头键。
        #<F1>-<F12>：功能键F1至F12。
        #对于字母和数字键，直接使用字符即可，如"a"、"b"、"1"、"2"等，但需注意区分大小写。
        #<space>：空格键。
    def myCanvas_KeyPress(self, event):  # 绑定事件
        print("KeyPress:", event.char)
    def myCanvas_KeyRelease(self, event):  # 绑定事件
        print("KeyRelease:", event.char)    
        
root = tk.Tk()  # 创建主窗口
app = Application(master=root)  # 创建Application对象
app.mainloop()  # 进入消息循环
