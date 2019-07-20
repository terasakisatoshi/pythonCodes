from multiprocessing import Pool
import time
import numpy as np 
N=1000

def func(x):
    ret=sum([x**n * (-1)**n for n in range(x)])
    return ret

def std_map():
    res=map(func,range(N))
    #print(list(res))

def proc_test():
    p=Pool()
    res=p.map(func,range(N))
    #print(res)

def time_measure(func):
    start=time.time()
    func()
    end=time.time()

    print("elapsed time=",end-start)

def main():
    time_measure(std_map)
    time_measure(proc_test)
if __name__ == '__main__':
    main()