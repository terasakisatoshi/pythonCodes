import pyximport
pyximport.install()
import time
import numpy as np
from cymax import get_max

def main():
    N=10000000
    arr=np.arange(N)
    start = time.time()
    ret=get_max(arr)
    end=time.time()
    print("max={}, elapsed={}".format(ret,end-start))

if __name__ == '__main__':
    main()