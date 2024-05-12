import tkinter
app=tkinter.Tk()
app.title("窗口标题")
app.geometry("800x600")#设置窗口大小
tkinter.Label(app,text="窗口内容").pack()#显示窗口内容
tkinter.Button(app,text="按钮",command=lambda:print("按钮被点击")).pack()#显示按钮
app.mainloop()#运行窗口
