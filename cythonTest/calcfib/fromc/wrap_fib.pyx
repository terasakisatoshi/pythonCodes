cdef extern from 'cfib.h':
    double cfib(int n)


def fib(n):
    """calc value of n-th fib"""
    return cfib(n)
