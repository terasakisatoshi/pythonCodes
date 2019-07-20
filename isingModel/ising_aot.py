# Reference: http://nbviewer.jupyter.org/gist/genkuroki/4fa46c68c56ee0f3b1a6fc8ec628b9d7
# Author MathSorcerer

from math import log, sqrt, exp
from random import choice, random
from copy import deepcopy
import time
from array import array
from matplotlib import pyplot as plt
from numba import jit 
import numpy as np 

from pyising import ising2d_sum_of_adjacent_spins


#@jit('i8[:,:](i8[:,:],f8,i8)')
@jit
def ising2d_sweep(s, beta, niters):
    m, n = s.shape
    prob = np.array([exp(-2*beta*k) for k in [-4, -3, -2, -1, 0, 1, 2, 3, 4]])
    for _ in range(int(niters/(m*n))):
        for i in range(m):
            for j in range(n):
                s1 = s[i][j]
                k = s1*ising2d_sum_of_adjacent_spins(s, m, n, i, j)
                s[i][j] = -s1 if random() < prob[k+4] else s1
    return s

n = 100
beta_critical = log(1+sqrt(2))/2


def main():
    rand_ising2d = np.array([[choice([-1, 1]) for j in range(n)] for i in range(n)]).astype(np.int64)
    s_begin = deepcopy(rand_ising2d)
    begin = time.time()
    s_end = ising2d_sweep(rand_ising2d, beta_critical, 1e6)
    end = time.time()
    print("Elapsed=", end-begin)

    #plot_result(s_begin,s_end)



if __name__ == '__main__':
    main()
