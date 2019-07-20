"""
http://yutori-datascience.hatenablog.com/entry/2014/12/10/123157
"""
from numba import cuda
import numpy as np 
from numba import double
from numba.decorators import jit 
from numba import guvectorize
import time 
import math

@jit 
def pairwise_numba(X,D):
	M,N=X.shape[0],X.shape[1]
	for i in range(M):
		for j in range(M):
			d=0.0
			for k in range(N):
				tmp=X[i,k]-X[j,k]
				d+=tmp *tmp
			D[i,j]=np.sqrt(d)

@jit('void(f8[:,:],f8[:,:])') 
def pairwise_numba_with_type(X,D):
	M,N=X.shape[0],X.shape[1]
	for i in range(M):
		for j in range(M):
			d=0.0
			for k in range(N):
				tmp=X[i,k]-X[j,k]
				d+=tmp *tmp
			D[i,j]=np.sqrt(d)

@guvectorize(['void(f8[:, :], f8[:, :])'], '(x, y)->(x, x)')
def pairwise_vectorize(X, D):
    M = X.shape[0]
    N = X.shape[1]
    for i in range(M):
        for j in range(M):
            d = 0.0
            for k in range(N):
                tmp = X[i, k] - X[j, k]
                d += tmp * tmp
            D[i, j] = np.sqrt(d)

def pairwise_python(X,D):
	M,N=X.shape[0],X.shape[1]
	for i in range(M):
		for j in range(M):
			d=0.0
			for k in range(N):
				tmp=X[i,k]-X[j,k]
				d+=tmp *tmp
			D[i,j]=np.sqrt(d)

@cuda.jit('void(f8[:, :], f8[:, :])')
def pairwise_numba_cuda1(X, D):
    M = X.shape[0]
    N = X.shape[1]
    
    i, j = cuda.grid(2)
    
    if i < M and j < M:
        d = 0.0
        for k in range(N):
            tmp = X[i, k] - X[j, k]
            d += tmp * tmp
            
        D[i, j] = math.sqrt(d)

def measure_time(func,X,D):
	start=time.time()
	func(X,D)
	end=time.time()
	print("elapsed time",end-start)

def main():
	griddim = (100, 100)
	blockdim =(16, 16)
	SIZE=5000
	X=np.random.random((SIZE,3))
	D=np.empty((SIZE,SIZE))
	measure_time(pairwise_python,X,D)
	measure_time(pairwise_numba,X,D)
	measure_time(pairwise_numba_with_type,X,D)
	measure_time(pairwise_vectorize,X, D)
	
	start=time.time()
	pairwise_numba_cuda1[griddim, blockdim](X, D)
	end=time.time()
	print("elapsed gpu=",end-start)
if __name__ == '__main__':
	main()