from numba import jit
import numpy as np
import time

def measure_time(function):
    def func(*args,**kwargs):
        start=time.time()
        res=function(*args,**kwargs)
        end=time.time()
        elapsed=end-start
        return res,end-start
    return func

@measure_time
@jit
def sum1d_jit(my_double_array):
    total=0.0
    for i in range(my_double_array.shape[0]):
        total+=my_double_array[i]
    return total

@measure_time
@jit('f8(f8[:])')
def sum1d_jit_withtype(my_double_array):
    total=0.0
    for i in range(my_double_array.shape[0]):
        total+=my_double_array[i]
    return total

@measure_time
def sum1d_np(my_double_array):
    total=np.sum(my_double_array)
    return total

def main():
    my_double_array=np.random.randn(100000000)

    print(sum1d_jit(my_double_array))
    print(sum1d_jit_withtype(my_double_array))
    print(sum1d_np(my_double_array))

if __name__ == '__main__':
    main()