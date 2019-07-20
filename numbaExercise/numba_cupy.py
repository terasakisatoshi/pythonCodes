import chainer
from chainer import cuda
import numpy as np 
from numba.decorators import jit 
xp=cuda.cupy if cuda.available else np
print(xp)
SIZE=500
MAX_ITER=100
def test():
	mat=xp.arange(SIZE*SIZE).reshape(SIZE,SIZE)
	for i in range(MAX_ITER):
		mat.dot(mat)
@jit
def test_numba():
	mat=xp.arange(SIZE*SIZE).reshape(SIZE,SIZE)
	for i in range(MAX_ITER):
		mat.dot(mat)
	#print(mat)

def measure_time(func):
	import time
	start=time.time()
	func()
	end=time.time()
	print("elapsed time=",end-start)

def main():
	measure_time(test)
	measure_time(test_numba)
if __name__ == '__main__':
	main()