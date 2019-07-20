import socket

HOST='' # Symbolic name meaning all variable interfaces
PORT=5001

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen(1)
    while True:
        conn,addr=s.accept()
        with conn:
            print("Connected by",addr)
            while True:
                data=conn.recv(1024)
                if not data:
                    break
                data=data.decode('utf-8')
                data=data[::-1].encode('utf-8')
                conn.sendall(data)
        print("Closed conn")
print("Closed server socket")