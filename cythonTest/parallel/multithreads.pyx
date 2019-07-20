#Reference:https://www.isus.jp/products/python-distribution/thread-parallelism-in-cython/
cimport cython

import numpy as np 
cimport openmp 
from libc.math cimport log
from cython.parallel cimport prange
from cython.parallel cimport parallel

THOUSAND =1024
FACTOR=200
NUM_TOTAL_ELEMENTS = FACTOR * THOUSAND * THOUSAND

X1=np.random.uniform(-1.0,1.0,NUM_TOTAL_ELEMENTS)
X2=np.random.uniform(-1.0,1.0,NUM_TOTAL_ELEMENTS)
Y=np.zeros(X1.shape)

def test_serial():
    serial_loop(X1,X2,Y)
    return Y

def serial_loop(double[:] A, double[:] B, double[:] C):
    cdef int N = A.shape[0]
    cdef int i 

    for i in range(N):
        C[i]=log(A[i]) * log(B[i])

def test_parallel():
    parallel_loop(X1,X2,Y)
    return Y

@cython.boundscheck(False)
@cython.boundscheck(False)
def parallel_loop(double[:] A, double[:] B, double[:] C):
    cdef int N = A.shape[0]
    cdef int i

    with nogil:
        for i in prange(N, schedule='dynamic'):
            C[i]=log(A[i]) * log(B[i])

