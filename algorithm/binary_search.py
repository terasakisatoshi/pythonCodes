import numpy as np
from numba import jit
from measure import get_elapsed_data

@get_elapsed_data
@jit('i8(i8[:],i8)')
def binary_search(array,key):
    left=0
    right=len(array)-1
    while left<=right:
        center=(left+right)//2
        if array[center]==key:
            return center
        elif array[center] < key:
            left=center+1
        else:
            right=center-1
    return -1

def main():
    N=1000000000000
    array=np.arange(N)
    key=500
    print(binary_search(array,key))

if __name__ == '__main__':
    main()
