import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    host = '127.0.0.1'
    port = 50000
    sock.bind((host, port))
    sock.listen(1)
    print('waiting connection')
    connection, addr = sock.accept()
    with connection:
        print('Connection from: ' + str(addr))
        while True:
            data = connection.recv(1024).decode('utf-8')
            if data == 'exit':
                break
            print("Received a message: " + str(data))
            connection.send(data.encode('utf-8'))
            print("send a message: " + str(data))
