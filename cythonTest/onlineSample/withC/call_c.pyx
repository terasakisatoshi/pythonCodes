cimport numpy as np

cdef extern from "sum_by_c.h":
    unsigned long long sum_combi(int *xs, int *ys, int lenxs, int lenys)
def csum_combi(np.ndarray[int ,ndim=1] xs,np.ndarray[int,ndim=1] ys):
    return sum_combi(&xs[0],&ys[0],len(xs),len(ys))