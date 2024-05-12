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

def update_time():
    """更新Label中的时间显示"""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]  # 获取当前时间到毫秒
    time_var.set(current_time)  # 更新StringVar的值
    root.after(1, update_time)  # 每隔1000毫秒（1秒）调用一次update_time

# 创建窗口
root = tk.Tk()

# 设置窗口的宽度和高度
window_width = 800
window_height = 600



# 创建Label组件参数：root：窗口实例，text：文本内容，font：字体，fg：字体颜色，bg：背景颜色 
label = tk.Label(root, text="你好！！!", font=("Arial", 16), fg="blue", bg="yellow" )
# 使用pack方法将Label添加到窗口中 参数：fill：填充方式，expand：是否扩展，side：放置位置，anchor：对齐方式，padx：水平间距，pady：垂直间距
label.pack(fill="none", expand=tk.YES, side=tk.TOP, anchor="nw", padx=0, pady=0)

# 创建一个StringVar对象来存储时间字符串(动态文本内容)
time_var = tk.StringVar()  
# 创建Label组件参数：root：窗口实例，text：动态文本内容，font：字体，fg：字体颜色，bg：背景颜色
time_label = tk.Label(root, textvariable=time_var, font=("Arial", 16), fg="blue", bg="yellow")
# 使用pack方法将Label添加到窗口中 参数：fill：填充方式，expand：是否扩展，side：放置位置，anchor：对齐方式，padx：水平间距，pady：垂直间距
time_label.pack(fill="none", expand=tk.YES, side=tk.TOP, anchor="se", padx=0, pady=0)


# 获取当前工作目录
current_working_dir = os.getcwd() 
# 图片路径
img_path = current_working_dir + "/images/1.png"
# 加载图片
img=tk.PhotoImage(file=img_path)
# 创建Label组件参数：root：窗口实例，image：图片对象（必须要在这读取图片,在下面读取图片会是null）
img_label=tk.Label(root, image=img)
# 使用pack方法将Label添加到窗口中 参数：fill：填充方式，expand：是否扩展，side：放置位置，anchor：对齐方式，padx：水平间距，pady：垂直间距
img_label.pack(fill="none", expand=tk.YES, side=tk.TOP, anchor="center", padx=0, pady=0)


# 调用函数以使窗口居中 参数：root：窗口实例，width：窗口宽度，height：窗口高度
center_window(root, window_width, window_height)

update_time()# 首次启动时间更新

# 窗口主循环
root.mainloop()