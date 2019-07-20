cdef inline size_t cgcd(size_t a, size_t b):
    while b != 0:
        a, b = b, a % b
    return a
