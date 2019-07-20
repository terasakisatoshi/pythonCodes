def fib(int n):
    """
    calc value of n-th fib
    n : int n-th 
    return n-th value of fib
    """
    cdef int i
    cdef double a = 0.0, b = 1.0
    for i in range(n):
        a, b = a + b, a
    return a
