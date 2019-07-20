import socket 
import threading

def handle_client(client_socket):
    request=client_socket.recv(1024)
    print(request)
    client_socket.send(b"Hi")
    client_socket.close()

def main():
    bind_ip='127.0.0.1'
    bind_port=9876

    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((bind_ip,bind_port))
    server.listen(5)

    while True:
        client,addr=server.accept()
        print(addr)
        client_handler=threading.Thread(target=handle_client,args=(client,))
        client_handler.start()

if __name__ == '__main__':
    main()