
def get_max(array):
    cdef int ret=array[0]
    cdef int i
    for i in range(len(array)):
        ret = array[i] if ret < array[i] else ret
    return ret