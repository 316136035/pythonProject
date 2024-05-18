import tkinter as tk
from tkinter import Menu


# 定义 窗口类 继承自tk.Frame的类。这意味着Application类将拥有tk.Frame类的所有属性和方法  Frame是一个容器类
class Application(tk.Frame):
    # 构造器 # master: 窗口的父容器
    def __init__(self, master=None):
        super().__init__(
            master, bg="#0066FF"
        )  # super()函数用于调用tk.Frame父类的方法  把Frame容器放到master父容器
        master.title("A020_messagebox_简单消息框")  # 设置窗口标题
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
        # 创建主菜单栏
        self.mainMenu=tk.Menu(self.master)  
        #主菜单栏的配置 参数：bg：背景颜色，fg：前景颜色，activebackground：选中时的背景颜色，activeforeground：选中时的前景颜色，relief：边框样式
        self.mainMenu.configure(activebackground="#6778da", activeforeground="white",bg="white", fg="black",relief="flat")
        
  
        file_menu = tk.Menu(self.mainMenu, tearoff=0) # 创建"文件"子菜单
        file_menu.add_command(label="新建", command=self.myShowinfo)
        file_menu.add_command(label="打开", command=self.myShowinfo)
        file_menu.add_command(label="保存", command=self.myShowinfo)
        file_menu.add_separator() # 添加分割线
        file_menu.add_command(label="退出", command=self.myShowinfo)
        
        
        edit_menu = tk.Menu(self.mainMenu, tearoff=0) # 创建"编辑"子菜单
        edit_menu.add_command(label="全选", command=self.myShowinfo)
        
        help_menu = tk.Menu(self.mainMenu, tearoff=0) # 创建"查看"子菜单
        help_menu .add_command(label="查看帮助", command=self.myShowinfo)
        

    
        # 将"文件"子菜单添加到主菜单栏
        self.mainMenu.add_cascade(label="文件", menu=file_menu)
        self.mainMenu.add_cascade(label="编辑", menu=edit_menu)
        self.mainMenu.add_cascade(label="帮助", menu=help_menu)
        # 配置根窗口使用菜单栏
        self.master.config(menu=self.mainMenu)  # 注意这里的menu关键字
        
        # 创建右键菜单
        self.right_click_menu=Menu(self.master)
        self.right_click_menu.add_command(label="新建", command=self.myShowinfo)
        # 绑定鼠标右键事件
        self.bind("<Button-3>", lambda event: self.contextMenu.post(event.x_root, event.y_root))
        
        
    def myShowinfo (self):  
        pass
     
        
   
   
   
       

root = tk.Tk()  # 创建主窗口
app = Application(master=root)  # 创建Application对象
app.mainloop()  # 进入消息循环
