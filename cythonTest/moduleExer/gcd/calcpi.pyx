from libc.math cimport sqrt
from mod cimport cgcd


def gcd(a, b):
    return cgcd(a, b)


def calc_pi(size_t N):
    cdef:
        size_t s = 0
        size_t a, b
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            if gcd(a, b) == 1:
                s += 1
    cdef float pi = sqrt(6.0 * N**2 / s)
    return pi
