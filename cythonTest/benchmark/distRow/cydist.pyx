# Reference: Benchmark of Cython VS Numba
cimport cython 
from libc.math cimport sqrt

@cython.boundscheck(False)
@cython.wraparound(False)
def pairwise_cython(double[:,::1] X, double[:,::1] D):
    M, N = X.shape[0],X.shape[1]
    cdef :
        size_t i,j,k
        double d
    for i in range(M):
        for j in range(M):
            d = 0.0
            for k in range(N):
                tmp = X[i, k]-X[j, k]
                d += tmp*tmp
            D[i, j] = sqrt(d)
