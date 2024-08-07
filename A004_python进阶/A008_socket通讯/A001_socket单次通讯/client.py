import socket

def send_message(sock, message):
    # 将消息编码为字节串
    encoded_message = message.encode()
    # 获取消息的长度
    message_length = len(encoded_message)
    # 将长度信息转换为一个字符串，并填充至10位（这里假设长度信息固定为10个字符）
    length_str = f"{message_length:<10}"
    # 将长度信息编码为字节串
    encoded_length = length_str.encode()
    # 发送长度信息
    sock.sendall(encoded_length)
    # 发送实际的消息
    sock.sendall(encoded_message)# 辅助函数，用于接收带有长度前缀的消息
def receive_message(sock):
    # 初始化一个空字节串作为长度信息的缓存
    length_buffer = b''
    # 循环直到接收到完整的长度信息（这里假定长度信息为10个字符）
    while len(length_buffer) < 10:
        # 每次接收剩余的长度信息，直到达到10个字符
        length_buffer += sock.recv(10 - len(length_buffer))
    # 将接收到的长度信息从字节串转换为字符串并去除可能的空白字符
    length_str = length_buffer.decode().strip()
    # 将字符串形式的长度信息转换为整数
    message_length = int(length_str)
    # 初始化一个空字节串来存储接收到的消息
    received_message = b''
    # 循环接收直到接收到完整的消息
    while len(received_message) < message_length:
        # 每次接收一小块数据（这里最多4096字节），直到接收完全部消息
        chunk = sock.recv(min(4096, message_length - len(received_message)))
        # 将接收到的数据追加到已接收的消息中
        received_message += chunk
    # 将接收到的字节串解码为字符串
    print("打印接收到的消息:", received_message.decode())
    return received_message.decode()

def start_client():
    """启动客户端，连接到服务器，发送消息，并接收服务器的响应。"""
    host = '127.0.0.1'  # 服务器的IP地址
    port = 8080         # 服务器监听的端口

    # 创建客户端套接字
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # 连接到服务器
        client_socket.connect((host, port))

        # 准备要发送的消息
        message = "Hello from the client"

        # 使用辅助函数发送带有长度前缀的消息
        send_message(client_socket, message)

        # 使用辅助函数接收带有长度前缀的消息
        response = receive_message(client_socket)

        # 打印接收到的响应
        print("打印接收到的响应:", response)

    finally:
        # 关闭客户端套接字
        client_socket.close()

if __name__ == "__main__":
    # 启动客户端
    start_client()