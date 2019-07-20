import numpy as np
from itertools import tee


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def main():
    M = 50000
    counter = 0
    xs = np.random.random(M)
    intervals = np.linspace(0, 1, M)
    for b, e in pairwise(intervals):
        exist = np.logical_and(b <= xs, xs < e)
        if not np.sum(exist):
            counter += 1
        else:
            xs = xs[np.logical_not(exist)]
    napier_approx = M / counter
    print(napier_approx)


if __name__ == '__main__':
    main()
