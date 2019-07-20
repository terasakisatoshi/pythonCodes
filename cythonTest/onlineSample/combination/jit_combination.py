import time
from numba import jit
import numpy as np 

@jit()
def jit_sum_conbination(N):
    xs = [i for i in range(N)]
    ys = [i for i in range(N)]
    total = 0
    for x in xs:
        for y in ys:
            total += x+y
    return total

def py_sum_conbination(N):
    xs =  np.arange(N)
    ys =  np.arange(N)
    total = 0
    for x in xs:
        for y in ys:
            total += x+y
    return total

def main():
    N = 10000
    start = time.time()
    total = jit_sum_conbination(N)
    end = time.time()
    print(total)
    print('elapsed time=', end-start)

if __name__ == '__main__':
    main()
