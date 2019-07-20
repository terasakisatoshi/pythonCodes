import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    ip = '127.0.0.1'
    port = 50000
    server = (ip, port)
    sock.connect(server)
    msg = ''
    while msg != 'exit':
        msg = input('->')
        sock.send(msg.encode('utf-8'))
        data = sock.recv(1024).decode('utf-8')
        print('Received from server: ' + str(data))
