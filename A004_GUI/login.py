import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import os
from tkinter import messagebox
from views import MultiPanelApp


class DataEntryForm(ttk.Frame):
    """数据输入表单类，用于创建和管理用户界面中的数据输入表单。"""

    def __init__(self, master):
            
        """初始化数据输入表单。Args:master (tkinter.Tk or tkinter.Toplevel): 父级窗口对象。"""
        # 初始化父类框架
        super().__init__(master, padding=(20, 10) )  # super()函数用于调用tk.Frame父类的方法  把Frame容器放到master父容器
        self.pack(fill=BOTH, expand=YES)  # 使用pack布局管理器 填充X方向
        self.master=master # 保存父级窗口对象
        self.master.title("淘神价登录页面")
        self.master.geometry("400x300") # 设置窗口大小
        self.master.style.theme_use("darkly") # 设置主题
        self.center_window( ) # 窗口居中
        # 初始化输入绑定变量
        self.username = ttk.StringVar(value="")
        self.password = ttk.StringVar(value="")
       
        # 创建标题标签
        hdr_txt = "欢迎来到淘神价学习交流！！！" 
        hdr = ttk.Label(master=self, font = ("Arial", 10),anchor="center", text=hdr_txt, width=50)
        hdr.pack(fill=X, pady=10) # 使用pack布局管理器 填充X方向，并设置ypadding为10

        # 创建表单输入字段
        self.create_form_entry("账号：", self.username)
        self.create_form_entry("密码：", self.password)
        self.create_buttonbox()  # 创建按钮框


    def center_window(self):
        window = self.master  # 使用self.master来引用父窗口
        """使窗口居中于屏幕中央"""
        window.update_idletasks()  # 确保窗口尺寸已计算
        width = window.winfo_width() # 获取窗口宽度
        height = window.winfo_height() # 获取窗口高度
        screen_width = window.winfo_screenwidth() # 获取屏幕宽度
        screen_height = window.winfo_screenheight() # 获取屏幕高度
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        window.geometry(f"{width}x{height}+{x}+{y}")   
    def create_form_entry(self, label, variable):
        """创建单个表单输入条目"""
        container = ttk.Frame(self)  # 创建包含输入框的框架
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=10)  # 创建标签
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Entry(master=container, textvariable=variable)  # 创建输入框
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)

    def create_buttonbox(self):
        """创建应用按钮框。"""
        container = ttk.Frame(self)  # 创建按钮容器框架
        container.pack(fill=X, expand=YES, pady=(15, 10)) # 使用pack布局管理器 填充X方向，并设置ypadding为10

        # 创建提交按钮 参数：master: 父级容器，text: 按钮文本，command: 点击按钮时执行的命令，bootstyle: 按钮样式，width: 按钮宽度
        sub_btn = ttk.Button(master=container,text="登录",command=self.on_submit,bootstyle=SUCCESS,width=6,)
        sub_btn.pack(side=RIGHT, padx=5) # 使用pack布局管理器 填充X方向，并设置ypadding为10
        sub_btn.focus_set()  # 设置焦点

        # 创建退出按钮 参数：master: 父级容器，text: 按钮文本，command: 点击按钮时执行的命令，bootstyle: 按钮样式，width: 按钮宽度
        cnl_btn = ttk.Button(master=container,text="退出",command=self.on_cancel,bootstyle=DANGER,width=6,)
        cnl_btn.pack(side=RIGHT, padx=5) # 使用pack布局管理器 填充X方向，并设置ypadding为10

    def on_submit(self):
       
        print("username:", self.username.get())
        print("password:", self.password.get())
      
        if self.username.get() == "admin" and self.password.get() == "admin":
            print("登录成功")
            
            self.destroy()
            MultiPanelApp(self.master)
        else:
            messagebox.askokcancel("登录失败", "用户名或密码错误")
      

    def on_cancel(self):
        """取消并关闭应用程序。"""
        self.quit()


if __name__ == "__main__":

    app = ttk.Window()

    
    # 获取当前工作目录，通常是项目路径
    current_path = os.getcwd()
    img_path = os.path.join(current_path, "A004_GUI", "jd.ico")  # 拼接图片路径
 
    app.wm_iconbitmap(img_path)
    DataEntryForm(app)
    app.mainloop()  
    
  
    


