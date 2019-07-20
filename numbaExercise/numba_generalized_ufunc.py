import math 
import numpy as np 
from numba import guvectorize

@guvectorize(['void(int32[:,:],int32[:,:],int32[:,:])',
			  'void(float64[:,:],float64[:,:],float64[:,:])'],
			  '(x,y),(x,y)->(x,y)')
def guvectorized_func(a,b,c):
	for i in range(c.shape[0]):
		for j in range(c.shape[1]):
			c[i,j]=a[i,j]+b[i,j]

def python_func(a,b,c):
	for i in range(c.shape[0]):
		for j in range(c.shape[1]):
			c[i,j]=a[i,j]+b[i,j]

def main():
	a=np.arange(1.0,10.0,dtype='f8').reshape(3,3)
	b=np.arange(1.0,10.0,dtype='f8').reshape(3,3)
	guvectorized_func(a,b)
if __name__ == '__main__':
	main()