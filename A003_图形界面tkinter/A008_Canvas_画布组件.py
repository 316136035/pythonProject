import tkinter as tk


# 定义 窗口类 继承自tk.Frame的类。这意味着Application类将拥有tk.Frame类的所有属性和方法  Frame是一个容器类
class Application(tk.Frame):
    # 构造器 # master: 窗口的父容器
    def __init__(self, master=None):
        super().__init__(
            master, bg="lightblue"
        )  # super()函数用于调用tk.Frame父类的方法  把Frame容器放到master父容器
        master.title("A008_Canvas_画布组件")  # 设置窗口标题
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
        # 创建画布 参数：父容器，背景颜色，宽度，高度
        self.Canvas = tk.Canvas(self, bg="lightblue", width=800, height=600)
        
        # 画直线/线段 参数：x1,y1,x2,y2,x3,y3,x4, 线的颜色
        self.Canvas.create_line(0,400,100,600,150,400,160,450 ,170,50,fill="red")
        self.Canvas.pack(fill=tk.BOTH, expand=True)#设置容器类布局 参数：fill=tk.BOTH），而且当父容器的大小发生变化时，Frame也会随之扩大以继续填充父容器（通过expand=True）
       
        #画矩形：参数：x1,y1,x2,y2,线的颜色
        self.Canvas.create_rectangle(100,100,200,200,fill="green")
        
        #画圆 参数：x1,y1,x2,y2,线的颜色
        self.Canvas.create_oval(300,300,400,400,fill="blue")
        
       
   
      

   
   
   


root = tk.Tk()  # 创建主窗口
app = Application(master=root)  # 创建Application对象
app.mainloop()  # 进入消息循环
