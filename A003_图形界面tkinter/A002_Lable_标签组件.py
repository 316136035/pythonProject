import tkinter as tk
import os
from datetime import datetime


# 定义 窗口类 继承自tk.Frame的类。这意味着Application类将拥有tk.Frame类的所有属性和方法  Frame是一个容器类
class Application(tk.Frame):
    # 构造器 # master: 窗口的父容器
    def __init__(self, master=None):
        super().__init__(
            master, bg="lightblue"
        )  # super()函数用于调用tk.Frame父类的方法  把Frame容器放到master父容器
        master.title("A001_窗口定义")  # 设置窗口标题
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
        #写法：组件名 = tk.组件类型(父容器,参数) 参数可以是对象{} 或者 {key=value} 或者self.lable[key]=value
        self.lable = tk.Label(self, text="在Tkinter库中，tk.Label是一个用来显示文本或图像的基本GUI部件。它有许多配置选项（API）可以用来定制其外观和行为",
                              font=( "Arial",22,"bold"),# font: 指定文本的字体样式。可以是一个字体名称字符串，或者一个包含(font_family, size, styles)的元组，例如("Arial", 12, "bold")。(字体、颜色、内边)
                              fg="red",# fg 或 foreground: 设置文本的颜色。可以是颜色名称字符串（如"red"）或颜色的RGB值（如"#FF0000"）。
                              bg= "green",# bg 或 background: 设置标签的背景颜色。justify: 文本的对齐方式，仅当文本多行时有效。可选值有tk.LEFT, tk.RIGHT, tk.CENTER。
                              wraplength=600,# wraplength: # 标签的建议宽度，单位是字符单元。这不影响自动换行，但可能影响布局。
                              width=600,# width: 标签的建议宽度，单位是字符单元。这不影响自动换行，但可能影响布局。
                              height=1,# height: 标签的建议高度，单位是文本行数。对于单行文本，默认为1。
                               # tk.N 或 'n'：北，内容靠上对齐。
                               # tk.S 或 's'：南，内容靠下对齐。
                               # tk.E 或 'e'：东，内容靠右对齐。
                               # tk.W 或 'w'：西，内容靠左对齐。
                               # tk.NE、tk.NW、tk.SE、tk.SW：分别对应东北、西北、东南、西南角对齐。
                               # tk.CENTER 或 'center'：居中对齐（默认值）
                              anchor = tk.N ,
                              padx=10,# padx 和 pady: 分别设置标签内容与其边界之间的水平和垂直内边距。
                              compound=tk.LEFT,# 当同时有文本和图片时，控制它们的相对位置。可能的值包括tk.LEFT, tk.RIGHT, tk.TOP, tk.BOTTOM, tk.CENTER。
                              cursor="hand2",# 鼠标悬停在标签上时的光标形状hand2 是一个预定义的光标形状，表示类似于手的形状，通常用于指示用户界面中的可点击元素。Tkinter支持多种光标类型，包括但不限于 "arrow"（默认箭头光标）、"watch"（表针形状，表示正在处理）、"crosshair"（十字准星，常用于精确选择）、"pirate"（海盗旗，趣味性光标）等
                              relief=tk.RAISED,# relief: 边框样式，如tk.RAISED, tk.SUNKEN, tk.FLAT, tk.GROOVE, tk.RIDGE。
                              )
      
        self.lable.pack()

        global img  # 定义全局变量img
        # 获取当前工作目录，通常是项目路径
        current_path = os.getcwd()
        img_path = os.path.join(current_path, "images", "1.png")  # 拼接图片路径
        img = tk.PhotoImage(file=img_path)  # 创建PhotoImage对象
        self.lable_img = tk.Label(self,
                                  image=img  ## image: 如果要显示图片，可以使用此选项指定一个PhotoImage对象。
        ) 
        self.lable_img.pack()  # 调用窗口组件

        """创建并配置界面组件。"""
         # 创建一个StringVar来存储时间文本
        self.time_var = tk.StringVar()
        # 创建标签用于显示时间
        self.label = tk.Label(self,
                              textvariable=self.time_var ,  # 绑定StringVar到标签
                              font=("Arial", 20))
        self.label.pack(pady=20)
        self.update_time()
    
    def update_time(self):
        """更新当前时间并设置到标签上，然后安排下一秒再次更新"""
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]  # 精确到毫秒并去除多余的微秒
        self.time_var.set(current_time)
        self.after(1, self.update_time)  # 每1000毫秒即1秒后再次调用此方法

  


root = tk.Tk()  # 创建主窗口
app = Application(master=root)  # 创建Application对象
app.mainloop()  # 进入消息循环  
