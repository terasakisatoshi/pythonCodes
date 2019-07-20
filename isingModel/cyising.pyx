# Reference: http://nbviewer.jupyter.org/gist/genkuroki/4fa46c68c56ee0f3b1a6fc8ec628b9d7
# Author MathSorcerer

from math import exp
import array
from cpython cimport array as carray
from random import choice, random
from libc.stdlib cimport rand, RAND_MAX
import time
cimport cython
import numpy as np

@cython.boundscheck(False)
cdef int ising2d_sum_of_adjacent_spins(int[:,:] s, int m, int n,int  i, int j):
    cdef:
        int i_bottom = i+1 if i+1 < m else 0
        int i_top = i-1 if i-1 >= 0 else m-1
        int j_right = j+1 if j+1 < n else 0
        int j_left = j-1 if j-1 >= 0 else n-1
    return s[i_bottom,j]+s[i_top,j]+s[i,j_right]+s[i,j_left]

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef int[:,:] ising2d_sweep(int[:,:] s, double beta, int niters):
    cdef int m, n, s1, loop,num_iteration,k
    m,n= s.shape[0],s.shape[1]
    num_iteration=int(niters/(m*n))
    cdef carray.array prob = array.array('d',[exp(-2*beta*k) for k in [-4, -3, -2, -1, 0, 1, 2, 3, 4]])
    for loop in range(num_iteration):
        for i in range(m):
            for j in range(n):
                s1 = s[i,j]
                k = s1*ising2d_sum_of_adjacent_spins(s, m, n, i, j)
                s[i,j] = -s1 if rand()/RAND_MAX <  prob[k+4] else s1
    return s