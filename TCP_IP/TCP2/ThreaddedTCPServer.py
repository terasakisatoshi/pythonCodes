import socket
import threading
import SocketServer
import numpy as np 

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        data=self.request.recv(1024)
        cur_thread=threading.currentThread()
        response="%s: %s" % (cur_thread.getName(),data)
        arr=np.array([response," 10"])
        self.request.send(arr)
class ThreadedTCPServer(SocketServer.ThreadingMixIn,SocketServer.TCPServer):
    pass

def client(ip,port,message):
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((ip,port))
    sock.send(message)
    response=sock.recv(1024)
    print "Received: %s" % response
    sock.close()

def main():
    #port 0 means to select an arbitary unused port
    zero=0
    HOST,PORT="localhost",zero
    server=ThreadedTCPServer((HOST,PORT),ThreadedTCPRequestHandler)
    ip,port=server.server_address
    #Start a thread with the server --  that thread 
    #will thread will start one more thread for each request
    server_thread=threading.Thread(target=server.serve_forever)
    #Exit the server thread when the main thread terminates
    server_thread.setDaemon(True)
    server_thread.start()
    print("Server loop running in thread:",server_thread.getName())

    for i in range(10):
        client(ip,port,"HelloWorld %s"% str(i))


    server.shutdown()


if __name__ == '__main__':
    main()