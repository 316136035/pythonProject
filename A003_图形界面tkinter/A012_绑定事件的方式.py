import tkinter as tk


# 定义 窗口类 继承自tk.Frame的类。这意味着Application类将拥有tk.Frame类的所有属性和方法  Frame是一个容器类
class Application(tk.Frame):
    # 构造器 # master: 窗口的父容器
    def __init__(self, master=None):
        super().__init__(
            master, bg="#0066FF"
        )  # super()函数用于调用tk.Frame父类的方法  把Frame容器放到master父容器
        master.title("A012_绑定事件的方式")  # 设置窗口标题
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
 
        # 使用bind绑定事件没参数
        myButton =tk.Button(self, bg="#FFCCCC",text="command按钮", command=self.myFrame_command)
        myButton.pack(side=tk.TOP)  #side: 决定组件是放在父组件的左侧(tk.LEFT)、右侧(tk.RIGHT)、顶部(tk.TOP)还是底部(tk.BOTTOM)。默认是tk.TOP。
        # 使用bind绑定事件带参数
        myButton =tk.Button(self, bg="#FFCCCC",text="command——按钮", command=lambda:self.myFrame_command_lambda("我爱你"))
        myButton.pack(side=tk.TOP)  #side: 决定组件是放在父组件的左侧(tk.LEFT)、右侧(tk.RIGHT)、顶部(tk.TOP)还是底部(tk.BOTTOM)。默认是tk.TOP。 
       
        # 使用bind绑定事件没参数
        myFrame_bind=tk.Frame(self,bg="#FFEE11",width=600 ,height=100)
        myFrame_bind.pack(side=tk.TOP)  #side: 决定组件是放在父组件的左侧(tk.LEFT)、右侧(tk.RIGHT)、顶部(tk.TOP)还是底部(tk.BOTTOM)。默认是tk.TOP。
        myFrame_bind.bind("<Button-1>", self.myFrame_bind)
         # 使用bind绑定事件带参数
        myFrame_bind_lambda=tk.Frame(self, bg="#CD5C5C",width=600 ,height=100)
        myFrame_bind_lambda.pack(side=tk.TOP)  #side: 决定组件是放在父组件的左侧(tk.LEFT)、右侧(tk.RIGHT)、顶部(tk.TOP)还是底部(tk.BOTTOM)。默认是tk.TOP。
        myFrame_bind_lambda.bind("<Button-1>",lambda event:self.myFrame_bind_lambda(event))
        myFrame=tk.Frame(self, bg="#B0C4DE",width=600 ,height=100)
        myFrame.pack(side=tk.TOP)  #side: 决定组件是放在父组件的左侧(tk.LEFT)、右侧(tk.RIGHT)、顶部(tk.TOP)还是底部(tk.BOTTOM)。默认是tk.TOP。
        
        # 绑定全部Frame组件的事件
        myFrame_bind_class=tk.Frame(self, bg="#00FF00",width=600 ,height=100)
        myFrame_bind_class.bind_class("Frame", "<Button-1>", self.myFrame_bind_class)
        myFrame_bind_class.pack(side=tk.TOP)  #side: 决定组件是放在父组件的左侧(tk.LEFT)、右侧(tk.RIGHT)、顶部(tk.TOP)还是底部(tk.BOTTOM)。默认是tk.TOP。
        
        
        
        
    def myFrame_command(self):
        print("command的事件绑定")
    def myFrame_command_lambda(self, str):  # 绑定事件
        print("command=lambda:事件绑定",str)
    
    def myFrame_bind(self, event):
        print("bind的事件绑定",event)

    def myFrame_bind_lambda(self, event):  # 绑定事件
        print("bind=lambda:事件绑定",event)

    def myFrame_bind_class(self, event):  # 绑定事件
        print("bind_class:事件绑定",event)

root = tk.Tk()  # 创建主窗口
app = Application(master=root)  # 创建Application对象
app.mainloop()  # 进入消息循环
