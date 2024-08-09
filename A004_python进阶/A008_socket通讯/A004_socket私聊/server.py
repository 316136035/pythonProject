import socket
import threading

# 定义一个线程锁，用于保护对client_sockets列表的并发访问
lock = threading.Lock()

# 存储所有已连接客户端的套接字
client_sockets ={}

# 发送消息到指定的套接字
def send_message(sock, message):
    # 将消息编码成字节串
    encoded_message = message.encode()
    # 创建一个长度前缀，这里使用10个字节，不足的部分填充空格
    prefix = f"{len(encoded_message):<10}".encode()
    # 发送长度前缀和消息
    print(f"服务器发送消息: {message}")
    sock.sendall(prefix + encoded_message)

# 从套接字接收消息
def receive_message(sock):
    # 接收长度前缀
    length_prefix = sock.recv(10)
    # 将前缀转换为整数
    message_length = int(length_prefix.strip())
    # 初始化接收的字节串
    received_data = b''
    # 循环接收直到接收到完整的消息
    while len(received_data) < message_length:
        chunk = sock.recv(min(4096, message_length - len(received_data)))
        received_data += chunk
    # 返回解码后的消息
    return received_data.decode()

# 处理单个客户端连接的函数
def client_socket_fun(client_socket, addr):
    # 使用with语句确保即使发生异常，套接字也会被关闭
    with client_socket:
        print(f"连接来自 {addr}")
        try:
            # 主循环，不断接收和处理消息
            while True:
                # 接收客户端消息
                message = receive_message(client_socket)
                # 如果消息为"exit"，则退出循环，结束与该客户端的连接
                if message == "exit":
                    break
                print(f"收到消息: {message}")
                user,msg=message.split(":",1)
                if client_sockets.get(user)==None:
                    client_sockets[user]=client_socket
                    print(f"欢迎: {user} 进群！！！！")
                else:
                     print("用户已存在群中")
                with lock:
                    # 遍历所有已连接的客户端，发送消息
                    for user, client_socket in client_sockets.items():
                        send_message(client_socket, f"{user}:{msg}")
                    # 打印消息转发成功的日志
                    print(f"消息转发成功!!: {message}")
        # 捕获异常并处理
 
        except Exception as e:
            print(f"客户端连接异常: {e}")
            with lock:
                # 移除断开连接的客户端套接字
                client_sockets.pop(user)
                
                # 遍历所有客户端套接字，除了自身以外，将消息广播给其他所有客户端
                for other_user, other_client_socket in client_sockets.items():
                    if other_client_socket != client_socket:
                        send_message(other_client_socket, f"客户端 {user} 断开连接")
                
                

# 创建服务器套接字
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # 绑定服务器套接字到指定的IP地址和端口
    server_socket.bind(('0.0.0.0', 12345))
    # 设置服务器套接字为监听模式，允许最大50个连接排队等待
    server_socket.listen(50)
    
    # 无限循环，等待并处理新客户端的连接
    print("等待客户端连接...")
    try:
        while True:
            # 等待客户端连接，accept()方法会阻塞直到有客户端连接
            client_socket, addr = server_socket.accept()
            # 使用线程锁保护对client_sockets的访问
       
          
            # 创建一个新线程来处理这个客户端连接
            threading.Thread(target=client_socket_fun, args=(client_socket, addr)).start()
            # 打印客户端连接成功的日志
            print("客户端连接成功{addr}")
    finally:
        # 关闭服务器套接字
        server_socket.close()