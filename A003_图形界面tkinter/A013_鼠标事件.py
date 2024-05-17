import tkinter as tk


# 定义 窗口类 继承自tk.Frame的类。这意味着Application类将拥有tk.Frame类的所有属性和方法  Frame是一个容器类
class Application(tk.Frame):
    # 构造器 # master: 窗口的父容器
    def __init__(self, master=None):
        super().__init__(
            master, bg="#0066FF"
        )  # super()函数用于调用tk.Frame父类的方法  把Frame容器放到master父容器
        master.title("A013_鼠标事件")  # 设置窗口标题
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
        """ 鼠标按键事件 /双击和多击事件 """
        #<Button-1>：左键单击。
        #<Button-2>：中键单击（在某些系统上可能映射为其他功能）。
        #<Button-3>：右键单击。
        #<Button-n>：对于具有更多按钮的鼠标，可以有<Button-4>, <Button-5>, 等等。
        #<Double-Button-1>：左键双击
        #<Triple-Button-1>：理论上是左键三击，但实际支持可能因平台而异。
        """ 按钮按下与释放 """
        #<ButtonPress-1>：左键被按下
        #<ButtonRelease-1>：左键被释放。
        """ 鼠标移动事件 """
        #MouseWheel>
        #<B1-Motion>：左键按下并移动（拖动）。
        #<B2-Motion>：中键按下并移动（如果支持）。
        #<B3-Motion>：右键按下并移动。
        #<Motion>：鼠标在组件上移动，不论按钮是否按下。
        """ 进入与离开事件 """
        # <Enter>：鼠标指针进入组件区域。
        # <Leave>：鼠标指针离开组件区域。
        """ 鼠标滚动事件 """
        #<MouseWheel> 鼠标滚动事件
        """ 按键状态事件 这些事件通常与鼠标按键结合使用，表示按键的同时是否有其他键被按下（如Shift, Ctrl） """
        #<Shift-Button-1>：按住Shift键同时左键单击。
        #<Control-Button-1>：按住Ctrl键同时左键单击
        my_Canvas=tk.Canvas(self, width=300, height=300, bg="white")
        my_Canvas.pack()
        my_Canvas.bind("<ButtonPress-1>", self.myCanvas_ButtonPress)
        my_Canvas.bind("<B1-Motion>",self.myCanvas_bind_motion)
        my_Canvas.bind("<ButtonRelease-1>",self.myCanvas_ButtonRelease)
        my_Canvas.bind("<MouseWheel>",self.myCanvas_MouseWheel)
        
    def myCanvas_ButtonPress(self, event):
        print("鼠标在左键被按下组件位置：", event.x, event.y)
        print("鼠标在左键被按下屏幕位置：", event.x_root, event.y_root)
    def myCanvas_bind_motion(self, event):
       print("鼠标左键在拖拽下组件位置：", event.x, event.y)
       print("鼠标左键在拖拽下屏幕位置：", event.x_root, event.y_root)

    def myCanvas_ButtonRelease(self, event):
        print("鼠标左键被释放下组件位置：", event.x, event.y)
        print("鼠标左键在释放下屏幕位置：", event.x_root, event.y_root)
    
    def myCanvas_MouseWheel(self, event):
        print("鼠标滚轮组件位置：", event.x, event.y)
        print("鼠标滚轮屏幕位置：", event.x_root, event.y_root)
      
root = tk.Tk()  # 创建主窗口
app = Application(master=root)  # 创建Application对象
app.mainloop()  # 进入消息循环
