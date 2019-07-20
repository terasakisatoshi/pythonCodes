import threading,queue 

lock=threading.RLock()
que=queue.Queue()

class MyThread(threading.Thread):
    def run(self):
        while True:
            try:
                val=que.get(False)
            except queue.Empty:
                break 
            i=0
            for n in range(val):
                i+=n 
            with lock:
                print("[end] %s:%d:%d"%(self.getName(),val,i))
            que.task_done()

def main():
    for N in range(10):
        que.put(N*100000)
    th1=MyThread()
    th2=MyThread()
    th1.start()
    th2.start()

    with lock:
        print("in join")
    que.join()

    th1.join()
    th2.join()
    with lock:
        print('finish')

if __name__ == '__main__':
    main()