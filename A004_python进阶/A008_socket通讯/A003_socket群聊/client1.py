import socket
import threading

def send_message(sock):
    while True:
        try:
            # 发送消息
            message = input("请输入消息 (输入 'exit' 退出): ")
            if message.lower() == 'exit':
                break
            
            # 编码消息为字节串
            encoded_message = message.encode()
            # 创建长度前缀，这里使用10个字节，不足的部分填充空格
            prefix = f"{len(encoded_message):<10}".encode()
            
            # 发送长度前缀和消息
            sock.sendall(prefix + encoded_message)

        except Exception as e:
            print(f"错误: {e}")
            break

def receive_message(sock):
    while True:
        try:
            # 接收长度前缀
            length_prefix = sock.recv(10).strip()
            # 如果前缀为空，表示连接已断开
            if not length_prefix:
                break
            # 将前缀转换为整数
            message_length = int(length_prefix)
            # 初始化接收的字节串
            received_data = b''
            # 循环接收直到接收到完整的消息
            while len(received_data) < message_length:
                # 接收数据
                chunk = sock.recv(min(4096, message_length - len(received_data)))
                if not chunk:
                    break
                received_data += chunk
            # 输出解码后的消息
            print(received_data.decode())

        except Exception as e:
            print(f"接收消息时出错: {e}")
            break

# 创建客户端套接字
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect(('localhost', 12345))
    
    # 使用守护线程，这样主线程结束时子线程也会自动结束
    threading.Thread(target=receive_message, args=(client_socket,), daemon=True).start()
    threading.Thread(target=send_message, args=(client_socket,), daemon=True).start()

    # 主线程等待用户输入exit，否则程序会立即退出
    while True:
        pass