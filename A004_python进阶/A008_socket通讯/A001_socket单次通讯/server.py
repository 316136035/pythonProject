import socket
import threading



def handle_client(client_socket, addr):

    try:
        # 接收数据长度信息
        data_length_str = client_socket.recv(10).decode().strip()
        data_length = int(data_length_str)

        # 根据长度接收数据
        total_received = 0
        received_data = b'' # 初始化接收数据变量
        while total_received < data_length: 
            chunk = client_socket.recv(min(4096, data_length - total_received)) # 读取数据
            if not chunk: # 如果没有接收到数据，则关闭连接
                break
            received_data += chunk # 将接收到的数据添加到接收数据变量中
            total_received += len(chunk) # 更新已接收数据长度
        print(received_data.decode())
        

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # 关闭客户端套接字
        client_socket.close()
        

def start_server():
    host = '0.0.0.0'
    port = 8080

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(5)

        while True:
            client_socket, addr = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
            client_thread.start()

if __name__ == "__main__":
    start_server()