
from numba import vectorize
import math 
import numpy as np

@vectorize(['float64(float64,float64)'])
def vectorized_func(x,y):
	return x+y+math.sqrt(x*math.cos(y))

def main():
	a=np.arange(1.0,10.0)
	b=np.arange(1.0,10.0)
	print(vectorized_func(a,b))
if __name__ == '__main__':
	main()