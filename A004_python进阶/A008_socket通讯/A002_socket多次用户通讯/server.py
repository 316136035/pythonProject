import socket
import threading
def send_message(sock, message):
    # 编码消息为字节串
    encoded_message = message.encode()
    # 创建长度前缀，这里使用10个字节，不足的部分填充空格
    prefix = f"{len(encoded_message):<10}".encode()
    # 发送长度前缀和消息
    sock.sendall(prefix + encoded_message)

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


def client_socket_fun(client_socke,addr):
    # 处理客户端连接
    with client_socke:
        print(f"连接来自 {addr}")
        try:
            while True:
                # 接收客户端消息
                message = receive_message(client_socket)
                if message=="exit":
                    break
                print(f"接收到消息: {message}")
                # 发送响应消息
                response = f"服务器收到了: {message}"
                send_message(client_socket, response)
        except Exception as e:
            print(f"客户端连接异常: {e}")
    client_socket.close() # 关闭客户端套接字
    
    

# 创建服务器套接字
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("等待客户端连接...")
    while True:
        # 等待客户端连接
        client_socket, addr = server_socket.accept()
        # 创建线程处理客户端连接
        threading_socket=threading.Thread(target=client_socket_fun,args=(client_socket,addr))
        threading_socket.start()
        print("客户端连接成功")
