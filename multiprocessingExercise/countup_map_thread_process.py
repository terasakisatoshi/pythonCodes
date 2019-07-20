import time
from threading import Thread 
from multiprocessing import Process

COUNT_RANGE=50000000
def count_up():
    ret_odd=sum((-i for i in range(1,COUNT_RANGE,2)))
    ret_even=sum((i for i in range(0,COUNT_RANGE,2)))
    return ret_odd+ret_even

def std_map():
    start=time.time()
    res=list(map(lambda x:count_up(),range(4)))
    finish=time.time()
    print("elapsed time=",finish-start)
    return res

def ThreadTest():
    thread_list=[]
    for i in range(4):
        thread_list.append(Thread(target=count_up))

    start=time.time()

    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()

    finish=time.time()

    print("elapsed time=",finish-start)

def ProcessTest():
    process_list=[]
    for i in range(4):
        process_list.append(Process(target=count_up))

    start=time.time()

    for process in process_list:
        process.start()
    for process in process_list:
        process.join()

    finish=time.time()

    print("elapsed time=",finish-start)

def main():
    print(std_map())
    ThreadTest()
    ProcessTest()
if __name__ == '__main__':
    main()