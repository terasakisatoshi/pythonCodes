# Reference: Benchmark of Cython VS Numba
import numpy as np
from numba.decorators import jit 
from numba import double


@jit("void(f8[:,:],f8[:,:])")
def pair_wise_python(X, D):
    M, N = X.shape
    for i in range(M):
        for j in range(M):
            d = 0.0
            for k in range(N):
                tmp = X[i, k]-X[j, k]
                d += tmp*tmp
            D[i, j] = np.sqrt(d)


def main():
    X = np.random.random((1000, 3))
    D = np.empty((1000, 1000))
    pair_wise_python(X, D)
    print(D)

if __name__ == '__main__':
    main()
