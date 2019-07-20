import threading
import queue
import numpy as np 

def task(args):
    print(args)
    args[0]=33
    

def main():
    args=np.array([1,2,3])
    t=threading.Thread(target=task,args=args)
    t.start()

if __name__ == '__main__':
    main()
