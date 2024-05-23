import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
 
class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI() # 初始化UI 
 
    def initUI(self):
        # 创建一个按钮
        button = QPushButton("点击我")
        button.clicked.connect(self.on_click)  # 当按钮被点击时调用 on_click 方法
 
        # 设置窗口的布局
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('PyQt6 示例')
        self.setCentralWidget(button)
        self.show()
 
    def on_click(self):
        print(self==QMainWindow)
        print("按钮被点击了")
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec()) # 开始执行程序
