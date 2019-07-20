import time 
import multiprocessing 
import socket 

class MultiProcessingSocketStreamServer(object):
    def __init__(self,port,process):
        self._serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self._serversocket.bind(('localhost',port))
        self._serversocket.listen(5)
        self.process=process

    def _parent_main_loop(self):
        while True:
            time.sleep(1)

    def start(self,handler):
        for i in range(self.process):
            p=multiprocessing.Process(target=handler,args=(self._serversocket, ))
            p.daemon=True
            p.start()
        self._parent_main_loop()

class SocketStreamHandler(object):
    def __init__(self):
        self._sock=None
        self._address=None

    def __call__(self,serversocket):
        while True:
            (self._sock,self._address)=serversocket.accept()
            with self:
                self.hander()

    def __enter__(self):
        pass

    def __exit__(self,exc_type,exc_value,traceback):
        self._sock.shutdown(socket.SHUT_RDWR)
        self._sock.close()

    def handle(self):
        raise NotImplementedError

class HelloWorldHandler(SocketStreamHandler):

    def handle(self):
        self._sock.send("Hello World\n")

def main():
    print("Hello")
    server=MultiProcessingSocketStreamServer(8080,5)
    handler=HelloWorldHandler()
    server.start(handler)


if __name__ == '__main__':
    main()