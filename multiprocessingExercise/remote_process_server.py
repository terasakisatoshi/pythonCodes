from multiprocessing.managers import BaseManager 
from threading import Thread
from multiprocessing import Queue 
from time import sleep 

queue=Queue()

def watch():
    while 1:
        while not queue.empty():
            print(queue.get())
        sleep(1)

def StartManager():
    class QueueManager(BaseManager):
        pass

    QueueManager.register("get_queue",lambda:queue)
    m=QueueManager(address=('',8002),authkey=b'a')

    t=Thread(target=watch)
    t.start()

    server=m.get_server()
    server.serve_forever()

def main():
    StartManager()

if __name__ == '__main__':
    main()