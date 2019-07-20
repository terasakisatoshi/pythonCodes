import threading
import time

def worker():
    print(threading.currentThread().getName(),"is starting")
    time.sleep(1)
    print(threading.currentThread().getName(),"is exiting")

def my_service():
    print(threading.currentThread().getName(),"is starting")
    time.sleep(2)
    print(threading.currentThread().getName(),"is exiting")

t=threading.Thread(name='my_service',target=my_service)
w=threading.Thread(name='worker',target=worker)
w2=threading.Thread(target=worker)
w3=threading.Thread(target=worker)

w.start()
w2.start()
t.start()
w3.start()
