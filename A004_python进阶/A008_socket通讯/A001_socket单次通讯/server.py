import socket
import threading
#函数是Python的socket模块中的方法，用于创建一个套接字对象。参数指定使用IPv4地址族。参数指定使用面向连接的TCP协议
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#0.0.0.0 标识监听任意地址 绑定端口8080
server.bind(('0.0.0.0', 8080))

data,address= server.accept()  #等待客户端连接 阻塞直到有客户端连接

print(data.recv(1024))
  
  
  
