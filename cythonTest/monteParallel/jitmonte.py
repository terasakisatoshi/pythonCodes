import random
from numba import jit, prange
import time


@jit(nopython=True, parallel=True)
def calc_pi(NUM):
    counter = 0
    for i in prange(NUM):
        x = random.random()
        y = random.random()
        if x*x+y*y < 1.0:
            counter += 1
    pi = 4.0*counter/NUM
    return pi


def main():
    NUM = 1000000000
    start = time.time()
    pi = calc_pi(NUM)
    end = time.time()
    print("pi, {}, elapsed={}".format(pi, end-start))

if __name__ == '__main__':
    main()
