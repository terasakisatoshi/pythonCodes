import pyximport
pyximport.install()

import cydist
import numpy as np


def main():
    X = np.random.random((1000, 3))
    D = np.empty((1000, 1000))
    cydist.pairwise_cython(X, D)
    print(D)

if __name__ == '__main__':
    main()
