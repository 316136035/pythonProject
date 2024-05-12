import tkinter as tk
from datetime import datetime
import os

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
def button_1():
    print("按钮1被点击")

# 创建窗口
root = tk.Tk()

# 设置窗口的宽度和高度
window_width = 800
window_height = 600

# 创建按钮 参数：root：父容器，text：按钮文本，width：按钮宽度，height：按钮高度，fg：字体颜色，bg：背景颜色，command：点击按钮时执行的函数
button_1=tk.Button(root, text="按钮", width=10, height=1 ,fg="white", bg="red", command=button_1)
button_1.pack()

# 调用函数以使窗口居中 参数：root：窗口实例，width：窗口宽度，height：窗口高度
center_window(root, window_width, window_height)


# 窗口主循环
root.mainloop()