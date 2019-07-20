import time
import numpy as np

def double_loop():
    li=[]
    for i in range(100):
        for j in range(100):
            a=np.random.rand()
            li.append(a)

def slow():
    li=[]
    n=10000
    for _ in range(n):
        a=np.random.rand()
        li.append(a)

def fast():
    n=10000
    li=np.random.rand(n)

def tuptest():
    n=10000
    tup=(np.random.rand() for _ in range(n))
    tupnp=np.array(tup)

def litest():
    n=10000
    [np.random.rand() for _ in range(n)]

def copyope():
    n=10000
    x=np.arange(n)
    x=2*x
def replaceope():
    n=10000
    x=np.arange(n)
    x*=2
def get_processtime(func):
    start=time.time()
    func()
    end=time.time()
    diff=end-start
    return diff


def main():
    process_times=[]
    process_times.append(get_processtime(copyope))
    process_times.append(get_processtime(replaceope))
    print(process_times)

if __name__ == '__main__':
    main()