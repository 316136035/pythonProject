import socket
import threading


def send_message(sock):
    username="amdin_3"
    while True:
        try:
            # 发送消息
            message = input("请输入消息 (输入 'exit' 退出): ")
            if message.lower() == "exit":
                break

            # 构建带有用户名的消息格式
            full_message = f"{username}:{message}"
            # 打印带有用户名的完整消息
            print(f"准备发送的消息: {full_message}")
            encoded_message = full_message.encode()
            prefix = f"{len(encoded_message):<10}".encode()


            # 发送长度前缀和消息
            sock.sendall(prefix + encoded_message)

        except KeyboardInterrupt:
            print("\n客户端被中断")
            break
        except ConnectionResetError:
            print("服务器端关闭了连接")
            break
        except Exception as e:
            print(f"错误: {e}")
            break
def receive_message(sock):
    while True:
        try:
            # 接收长度前缀
            length_prefix = sock.recv(10).strip()
            if not length_prefix:
                break

            # 将前缀转换为整数
            message_length = int(length_prefix)
            received_data = b""
            while len(received_data) < message_length:
                chunk = sock.recv(min(4096, message_length - len(received_data)))
                if not chunk:
                    break
                received_data += chunk

            # 解析并输出消息
            decoded_message = received_data.decode()
            
            # 分离用户名和消息内容
            parts = decoded_message.split(': ', 1)
            if len(parts) > 1:
                username, message = parts
                print(f"[{username}] {message}")
            else:
                print(f"[未知用户] {decoded_message}")

        except KeyboardInterrupt:
            print("\n客户端被中断")
            break
        except ConnectionResetError:
            print("服务器端关闭了连接")
            break
        except Exception as e:
            print(f"接收消息时出错: {e}")
            break

# 创建客户端套接字
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect(("localhost", 12345))

    # 使用守护线程
    threading.Thread(target=receive_message, args=(client_socket,), daemon=True).start()
    threading.Thread(target=send_message, args=(client_socket,), daemon=True).start()

    # 主线程等待用户输入exit
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("客户端被中断")