import socket
import threading

  
  
def server():
  host = '0.0.0.0' #0.0.0.0 标识监听任意地址 
  port = 8080 # 绑定端口8080..
  #函数是Python的socket模块中的方法，用于创建一个套接字对象。参数指定使用IPv4地址族。参数指定使用面向连接的TCP协议
  my_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  while True:
    try:
      my_server.bind((host, port)) #绑定端口
      my_server.listen(5) #监听
      print('服务器启动成功，监听端口：%s' % port)
      break
    except Exception as e:
      print('服务器启动失败，端口：%s' % port)
      port += 1
      
if __name__ == '__main__':
  server()