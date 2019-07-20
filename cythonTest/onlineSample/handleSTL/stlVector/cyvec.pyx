from libcpp.vector cimport vector


cpdef vector[int] get_vector(int size):
    cdef:
        vector[int] stl_vector
        int i 
    for i in range(size):
        stl_vector.push_back(i)
    return stl_vector


