from numba import jit 
import numpy as np 
import time

def measure_time(args):
    start=time.time()
    args[0](*args[1:])
    end=time.time()
    print("elapsed time=",(end-start)*1000,"[ms]")

def func_np(a,b):
    return np.exp(2.1*a+3.2*b)

@jit('void(double[:],double[:],double[:])',nopython=True,nogil=True)
def func_numba(result,a,b):
    for i in range(len(result)):
        result[i]=np.exp(2.1*a[i]+3.2*b[i])

N=1000000

def main():
    x_np=np.random.rand(N)-0.5
    y_np=np.random.rand(N)-0.5
    measure_time([func_np,x_np,y_np])
    measure_time([func_numba,np.zeros(N),x_np,y_np])

if __name__ == '__main__':
    main()