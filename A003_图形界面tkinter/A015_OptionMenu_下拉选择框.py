import tkinter as tk



# 定义 窗口类 继承自tk.Frame的类。这意味着Application类将拥有tk.Frame类的所有属性和方法  Frame是一个容器类
class Application(tk.Frame):
    # 构造器 # master: 窗口的父容器
    def __init__(self, master=None):
        super().__init__(
            master, bg="#0066FF"
        )  # super()函数用于调用tk.Frame父类的方法  把Frame容器放到master父容器
        master.title("A015_OptionMenu_下拉选择框")  # 设置窗口标题
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
         # 定义一个StringVar变量来存储选中的值(root确保这个变量与应用程序的生命周期绑定在一起)
        self.variable = tk.StringVar(root)
        self.variable.set("请选择...")  # 设置默认值
        # 定义OptionMenu的选项列表
        options = ["选项1", "选项2", "选项3", "选项4"]
        # 创建OptionMenu小部件
        option_menu = tk.OptionMenu(root, self.variable, *options)
        option_menu.pack(pady=10)  # 打包到窗口并设置垂直填充
        # 绑定选项变化事件到回调函数
        self.variable.trace("w", self.on_option_select)  # "w" 表示写入操作，即值发生变化时
    
    def on_option_select( self,*args):
        """选项改变时的回调函数"""
        selected_value = self.variable.get()
        print(f"你选择了: {selected_value}")
        print(args)

    
root = tk.Tk()  # 创建主窗口
app = Application(master=root)  # 创建Application对象
app.mainloop()  # 进入消息循环
