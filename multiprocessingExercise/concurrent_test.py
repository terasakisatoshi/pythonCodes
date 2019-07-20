import time 
import threading
import concurrent
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

def spam(index):
    for i in range(3):
        time.sleep(1)
        print("thread: {},value:{}".format(index,i))
    return "Done"

def main():
    executor=ThreadPoolExecutor(max_workers=3)
    futures=[]
    for i in range(6):
        print("Threads: {}".format(len(executor._threads)))
        futures.append(executor.submit(spam,i))
    print("main thread exit")
    for future in concurrent.futures.as_completed(futures):
            print(future.result())

    executor.shutdown()

if __name__ == '__main__':
    main()