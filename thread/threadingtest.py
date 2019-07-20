import threading

def worker(num):
    """thread worker function"""
    print("worker: ",num)
    return None

threads=[]

for i in range(5):
    t=threading.Thread(target=worker,args=(i,))
    print("i=",i)
    threads.append(t)
    t.start()
    print("end")

