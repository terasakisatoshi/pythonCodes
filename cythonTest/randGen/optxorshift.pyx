from cython cimport cdivision
cdef unsigned int y = 2463534242

cdef unsigned int c_xor32():
    global y
    y = y ^ (y << 13 )
    y = y ^ (y >> 17 )
    y = y ^ (y << 5 )
    return y

cdef unsigned int uint32_max = 0xffffffff
@cdivision(True)
cpdef double u01():
    return 1.0*c_xor32()/uint32_max

def cycalc_pi(int N):
    cdef int counter = 0
    cdef double x,y
    for i in range(N):
        x = u01()
        y = u01()
        if x*x+y*y < 1.0:
            counter += 1
    print(4.0*counter/<double>N)