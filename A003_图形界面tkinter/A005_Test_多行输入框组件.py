import tkinter as tk
import os


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
        self.text_module = tk.Text(self,
                            width=400, # 文本框的宽度，以字符单位计数，默认值取决于系统。
                            heigh=20, # 文本框的高度，以文本行数为单位，默认为一列。
                            bg="red", #文本框的背景颜色。
                            fg="black",#文本颜色
                            font=("Arial", 12),#字体样式，例如("Arial", 12)。
                            wrap="word",#文本换行方式，可以是"char"（在字符边界换行）、"word"（在单词边界换行）或"none"（不自动换行）。
                            # undo=False#是否允许撤销/重做功能，默认False。
                            # yscrollcommand (function): 绑定一个滚动条，用于垂直滚动。需要与Scrollbar组件一起使用。
                            # xscrollcommand (function): 绑定一个滚动条，用于水平滚动。同样需要与Scrollbar组件配合使用。
                            )
        self.text_module.pack(side=tk.TOP)
        tk.Button(self, text="插入文本",command=self.insert_text).pack(side=tk.LEFT)
        tk.Button(self, text="读取文本",command=self.get_text).pack(side=tk.LEFT)
        tk.Button(self, text="插入图片",command=self.insert_img).pack(side=tk.LEFT)
        tk.Button(self, text="插入组件",command=self.insert_module).pack(side=tk.LEFT)
        tk.Button(self, text="通过tag控制文件",command=self.tag_control_file).pack(side=tk.LEFT)
        
  

    """ 插入文本 """
    def insert_text(self):
        self.text_module.insert(tk.INSERT, "光标位置插入文本") # tk.INSERT表示插入到光标位置
        self.text_module.insert(1.8, "指定位置插入文本") # 1.8表示第1行第8个字符
        self.text_module.insert(tk.END, "文本框末尾插入文本") # tk.END表示文本框末尾
 
    """ 读取文本 """
    def get_text(self):
        print(self.text_module.get(1.0, tk.END)) # 1.0表示文本框开头，tk.END表示文本框末尾
        
    """ 插入图片 """
    def insert_img(self):
        global img # 全局变量
        current_path = os.getcwd()# 获取当前工作目录，通常是项目路径
        img_path = os.path.join(current_path, "images", "确认按钮.png")  # 拼接图片路径
        img = tk.PhotoImage(file=img_path)  # 创建PhotoImage对象
        self.text_module.image_create(tk.END, image=img) # 在文本框末尾插入图片+
        
    """ 插入组件 """
    def insert_module(self):
        self.BT= tk.Button(self.text_module, text="组件按钮") # 创建组件
        self.text_module.window_create(tk.END, window=self.BT) # 在文本框末尾插入组件
    
    """ 通过tag控制文件 """
    def tag_control_file(self):
        self.text_module.insert(tk.END, "通过tag控制文件")
        self.text_module.tag_add("tag", "1.2", "1.5") # 添加一个名为"red"的tag，并指定范围
        self.text_module.tag_config("tag",background="green", foreground="white") # 配置"red"标签的样式，设置前景色为红色
        self.text_module.tag_bind("tag", "<Button-1>", lambda event: print("点击了标签"))
     
root = tk.Tk()  # 创建主窗口
app = Application(master=root)  # 创建Application对象
app.mainloop()  # 进入消息循环
