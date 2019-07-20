
import socket

host="127.0.0.1"
port=1234

serversock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
serversock.bind((host,port))
serversock.listen(10)

print("waiting for connections...")
clientsock,client_address=serversock.accept()

while True:
    recvmsg=clientsock.recv(1024)
    print("Recv -> %s"%recvmsg)
    if recvmsg=='':
        break
    print("Type message")
    s_msg=input()
    if s_msg=="":
        break
    print("Wait...")

    clientsock.sendall(bytes(s_msg,'utf-8'))
clientsock.clear()