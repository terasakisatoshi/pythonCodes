import threading
import time
import datetime

class TestThread(threading.Thread):
    def __init__(self,n,t):
        super(TestThread,self).__init__()
        self.n=n
        self.t=t

    def run(self):
        print("=== start sub thread (sub class) ===")

        for i in range(self.n):
            time.sleep(self.t)
            print("sub thread (sub class) : " + str(datetime.datetime.today()))
        print("=== end sub thread (sub class) ===")


def do_something(n,t):
    print("=== start sub thread (method) ===")
    for i in range(n):
        time.sleep(t)
        print("[%s] sub thread (method) : " % threading.currentThread().getName()+ str(datetime.datetime.today()))
    print("=== end sub thread (method) ===")

def main():
    th_cl=TestThread(5,5)
    th_cl.start()

    time.sleep(1)

    th_me=threading.Thread(target=do_something,name="th_me",args=(5,5))
    th_me.start()

    print("=== start main thread (main) ===")
    for i in range(5):
        time.sleep(10)
        print("main thread: "+str(datetime.datetime.today()))
    print("=== end main thread ===")


if __name__ == '__main__':
    main()