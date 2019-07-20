def naive(N):
    xs = [i for i in range(N)]
    ys = [i for i in range(N)]
    total = 0
    for x in xs:
        for y in ys:
            total += x+y
    return total

def opt1(int N):
    xs = [i for i in range(N)]
    ys = [i for i in range(N)]
    cdef :
        long long total
        int x,y
    total=0
    for x in xs:
        for y in ys:
            total += x+y
    return total

def opt2(long N):
    xs = [i for i in range(N)]
    ys = [i for i in range(N)]
    cdef :
        unsigned long long total
        int i,j
        unsigned int lenxs,lenys
    lenxs=len(xs)
    lenys=len(ys)
    total=0
    for i in range(lenxs):
        for j in range(lenys):
            total += xs[i]+ys[j]
    return total

import numpy as np
def opt_numpy(int N):
    xs = np.arange(N)
    ys = np.arange(N)
    cdef :
        long long total
        int x,y
    total=0
    for x in xs:
        for y in ys:
            total += x+y
    return total

cimport numpy as np
def opt_cnumpy(int N):
    cdef np.ndarray[int] xs,ys
    xs = np.arange(N)
    ys = np.arange(N)
    cdef :
        long long total
        int x,y
    total=0
    for x in xs:
        for y in ys:
            total += x+y
    return total

