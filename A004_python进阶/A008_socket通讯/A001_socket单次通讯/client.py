import socket

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

# 创建客户端套接字
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect(('localhost', 12345))
    while True:
        # 发送消息
        message = input("请输入消息 (输入 'exit' 退出): ")
        if message.lower() == 'exit':
            break
        send_message(client_socket, message)
        # 接收响应
        response = receive_message(client_socket)
        print(f"服务器响应: {response}")