import tkinter as tk


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
   
        # 定义选项元组
        self.options_tuple = ("选项A", "选项B", "选项C", "选项D")
        # 使用字典来追踪每个选项的选中状态
        self.selected_options = {option: 0 for option in self.options_tuple}
        
        # 创建Checkbuttons并布局
        for option in self.options_tuple:
            var = tk.IntVar()  # 每个Checkbutton都需要自己的Tkinter变量
            self.checkbutton = tk.Checkbutton( root,
                        text=option, # 显示的文本
                        variable=var, # 绑定Tkinter变量
                        onvalue=1, # 选中时的值
                        offvalue=0, # 未选中时的值
                        command=lambda opt=option, var=var: self.on_checkbutton_change(opt, var)
                        )
            self.checkbutton.pack(anchor="w")  # 使用anchor="w"保持选项左对齐
             
        # 创建一个按钮来打印选中的选项
        print_button = tk.Button(root, text="打印选中项", command=self.print_selected_options)
        print_button.pack(pady=10)
    def on_checkbutton_change(self,option, var):
        print(f"{option} 选中状态: {var.get()}")
        """当Checkbutton状态改变时调用的回调函数，更新选中状态字典"""
        self.selected_options[option] = var.get() # 更新选中状态字典
  
    def print_selected_options(self):
        """打印当前选中的选项 遍历选项元组，并打印出选中的选项"""
        print("选中的选项:", [option for option, selected in self.selected_options.items() if selected])


   
   
   


root = tk.Tk()  # 创建主窗口
app = Application(master=root)  # 创建Application对象
app.mainloop()  # 进入消息循环
