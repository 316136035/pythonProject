import tkinter as tk
from ttkbootstrap import ttk, Style

class MultiPanelApp:
    def __init__(self, master):
        self.master = master
        self.style = Style()
        self.master.title("多面板应用")
        self.master.geometry("600x400")

        # 创建Notebook组件
        self.notebook = ttk.Notebook(self.master)

        # 创建并添加第一个面板（Tab1）
        self.tab1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="面板1")

        # 在Tab1中添加控件示例
        ttk.Label(self.tab1, text="这是面板1的内容").pack()

        # 创建并添加第二个面板（Tab2）
        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="面板2")

        # 在Tab2中添加控件示例
        ttk.Label(self.tab2, text="这是面板2的内容").pack()

        # 将Notebook放置到窗口上
        self.notebook.pack(expand=1, fill='both')

if __name__ == "__main__":
    master = tk.Tk()
    app = MultiPanelApp(master)
    master.mainloop()