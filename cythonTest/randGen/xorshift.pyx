cdef xorshift( unsigned int seed=2463534242):
    cdef unsigned int ret = seed
    def inner():
        nonlocal ret
        ret = c_xor32(ret)
        return ret
    return inner


cdef unsigned int c_xor32(unsigned int y=2463534242):
    y = y ^ (y << 13 )
    y = y ^ (y >> 17 )
    y = y ^ (y << 5 )
    return y

cyrandom32=xorshift()

cpdef double u01():
    return cyrandom32()/4294967295

def calc_pi(int N):
    cdef int counter = 0
    cdef x,y
    for i in range(N):
        x = u01()
        y = u01()
        if x*x+y*y < 1.0:
            counter += 1
    print(4.0*counter/<double>N)