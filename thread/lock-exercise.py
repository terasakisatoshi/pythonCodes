import threading 

rlock=threading.RLock() 

class MyThread(threading.Thread):
    def __init__(self,num=10000):
        self._count_num=num
        threading.Thread.__init__(self)

    def run(self):
        i=0
        for n in range(self._count_num):
            i+=n
            if 0== (n% 10000):
                rlock.acquire()
                print("mid %s:%d" % (self.getName(),n))
                rlock.release()

        rlock.acquire()
        print("end %s :%d"%(self.getName(),i))
        rlock.release()

def main():
    thread1=MyThread(300000)
    thread2=MyThread(200000)
    thread1.start()
    thread2.start()

    with rlock:
        print("in join ")
    
    thread1.join()
    thread2.join()

    print("[finish]")

if __name__ == '__main__':
    main()