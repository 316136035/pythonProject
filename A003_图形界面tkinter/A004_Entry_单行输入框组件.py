import tkinter as tk
from tkinter import messagebox # 导入messagebox模块 提示框


# 定义一个函数，用于将窗口居中于屏幕 参数：root：窗口实例，width：窗口宽度，height：窗口高度
def center_window(root, width, height):
    """将窗口居中于屏幕"""
    screen_width = root.winfo_screenwidth()  # 获取屏幕宽度
    screen_height = root.winfo_screenheight()  # 获取屏幕高度
    x_coordinate = int((screen_width / 2) - (width / 2))  # 计算窗口的x坐标
    y_coordinate = int((screen_height / 2) - (height / 2))  # 计算窗口的y坐标
    root.geometry(
        f"{width}x{height}+{x_coordinate}+{y_coordinate}"
    )  # 设置窗口大小和位置
def login():
    username = username_entry.get()
    password = password_entry.get()
    
    # 这里只是一个示例，你可以替换为实际的验证逻辑
    if username == "admin" and password == "password":
        messagebox.showinfo("登录成功", "欢迎，管理员！")
    else:
        messagebox.showerror("登录失败", "用户名或密码错误，请重试。")
def focusin():
    print("当输入框获得焦点时验证")

# 创建窗口
root = tk.Tk()
root.title("登录界面")

# 设置窗口的宽度和高度
window_width = 800
window_height = 600

# 用户名标签和输入框
username_label = tk.Label(root, text="用户名:")
username_label.pack()
# Entry_单行输入框组件
#'none'（默认）：关闭验证。'focusout'：当输入框失去焦点时验证。'focusin'：当输入框获得焦点时验证。'key'：在每次按键后验证（最常用，实时验证）。'all'：在所有情况下验证（包括键盘输入、粘贴等）
username_entry = tk.Entry(root,validate="focusin",validatecommand=focusin)
username_entry.pack()


# 密码标签和输入框
password_label = tk.Label(root, text="密码:")
password_label.pack()
password_entry = tk.Entry(root, show="*")  # 使用show="*"隐藏密码
password_entry.pack()

# 登录按钮
login_button = tk.Button(root, text="登录", command=login)
login_button.pack()

# 调用函数以使窗口居中 参数：root：窗口实例，width：窗口宽度，height：窗口高度
center_window(root, window_width, window_height)


# 窗口主循环
root.mainloop()