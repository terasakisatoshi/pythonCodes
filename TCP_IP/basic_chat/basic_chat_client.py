import socket

host="127.0.0.1"
port=1234

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))

client.send(bytes("Hello","utf-8"))
response=client.recv(4096)

print(response)
