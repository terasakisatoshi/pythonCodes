import socket 
import threading 
from contextlib import closing
def handle_client(client_socket):
    with closing(client_socket):
        request=client_socket.recv(1024)
        print("[*] Received:%s"% request)
        client_socket.send(b"ACK!")
        client_socket.close()

def main():
    bind_ip="127.0.0.1"
    bind_port=9998

    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((bind_ip,bind_port))
    server.listen(5)

    print("[*] Listening on %s:%d"%(bind_ip,bind_port))

    while True:
        client,addr=server.accept()
        print("[*] Accepted connection from: %s:%d"%(addr[0],addr[1]))
        client_handler=threading.Thread(target=handle_client,args=(client,))
        client_handler.start()
if __name__ == '__main__':
    main()


