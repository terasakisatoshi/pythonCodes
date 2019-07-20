from numba import jit
import numpy as np 
import time 

def mult_abs_basic(N,x,y):
    r=[]
    for i in range(N):
        r.append(abs(x[i]+y[i]))
    return r

def multi_abs_numpy(N,x,y):
    return np.abs(x+y)

@jit('f8[:](i8,c16[:],c16[:])',nopython=True)
def multi_abs_numba(N,x,y):
    r=np.zeros(N)
    for i in range(N):
        r[i]=abs(x[i]+x[i])
    return r

def measure_time(func,x,y):
    start=time.time()
    b=func(N,x,y)
    end=time.time()
    print("elapsed time=",end-start)

N=10000000

def main():    
    x_np=(np.random.rand(N)-0.5)+1J*(np.random.rand(N)-0.5)
    y_np=(np.random.rand(N)-0.5)+1J*(np.random.rand(N)-0.5)
    x=list(x_np)
    y=list(y_np)
    measure_time(mult_abs_basic,x,y)
    measure_time(multi_abs_numpy,x_np,y_np)
    measure_time(multi_abs_numba,x_np,y_np)
if __name__ == '__main__':
    main()