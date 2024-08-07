import socket
import threading

def send_message(sock, message):
    # 将消息编码为字节串
    encoded_message = message.encode()
    # 计算消息的长度
    message_length = len(encoded_message)
    # 将消息长度格式化为固定宽度的字符串（这里为10位）
    length_str = f"{message_length:<10}"
    # 发送消息长度
    sock.sendall(length_str.encode())
    # 发送实际的消息
    sock.sendall(encoded_message)


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
    send_message( sock,received_message.decode())



# 启动服务器
def start_server():
    host = '0.0.0.0'
    port = 8080
    # 创建服务器套接字
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # 绑定服务器地址和端口
        server_socket.bind((host, port))
        # 最大连接数
        server_socket.listen(5)
        print("服务器已启动，等待客户端连接...")
        while True:
            # 接受客户端连接 客户端套接字和客户端地址
            client_socket, addr = server_socket.accept()
            # 创建线程处理客户端连接
            client_thread = threading.Thread(target=receive_message, args=(client_socket, addr))
            # 启动线程
            client_thread.start()

if __name__ == "__main__":
    start_server()