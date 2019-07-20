import pyximport 
pyximport.install()
from math import log,sqrt
import numpy as np 
from cyising import ising2d_sweep
from random import choice
from copy import deepcopy
import time

from matplotlib import pyplot as plt 

def plot_result(s_begin,s_end):
    fig = plt.figure()
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    ax1.imshow(s_begin, cmap='gray')
    ax2.imshow(s_end, cmap='gray')
    plt.show()

from copy import deepcopy
from math import log,sqrt 
import numpy as np
n=100
beta_critical = log(1+sqrt(2))/2

def main():
    rand_ising2d = np.array([[choice([-1, 1]) for j in range(n)] for i in range(n)]).astype(np.int32)
    s_begin = deepcopy(rand_ising2d)
    begin = time.time()
    s_end = ising2d_sweep(rand_ising2d, beta_critical, 1e8)
    end = time.time()
    print("Elapsed=", end-begin)
    plot_result(s_begin,s_end)

if __name__ == '__main__':
    main()