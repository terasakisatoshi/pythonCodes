from multiprocessing.managers import BaseManager
from time import sleep
from socket import gethostname 

def send_message(word):
    return word

def main():
    class QueueManager(BaseManager):
        pass

    QueueManager.register('get_queue', callable=lambda: queue)
    m=QueueManager(address=('127.0.0.1',8002),authkey=b'a')

    m.connect()

    queue=m.get_queue()

    for i in range(4):
        queue.put(gethostname())
        queue.put(send_message("Hello"))
if __name__ == '__main__':
    main()