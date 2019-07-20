
import queue
import threading 
import time 


def worker(name,q):
    while True:
        item=q.get()
        if item is None:
            break
        do_work(name,item)
        q.task_done()

def do_work(name,item):
    print("hello",name,item)
    time.sleep(1.0)

def main():
    num_workers=4
    source=[i for i in range(100)]
    q=queue.Queue(5)
    threads=[]
    for i in range(num_workers):
        t=threading.Thread(target=worker,args=[i,q])
        t.start()
        threads.append(t)

    for item in source:
        q.put(item)

    q.join()

    for i in range(num_workers):
        q.put(None)
    for t in threads:
        t.join()

if __name__ == '__main__':
    main()