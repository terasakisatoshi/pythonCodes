from itertools import product
import numpy as np
from scipy.ndimage import maximum_filter


def scipy_case(domain):
    window_size = 3
    result = maximum_filter(
        domain, size=3)
    return result


def maximum_filter(domain, size=3):
    """
    naive implementation of maximum filter
    """
    ph = pw = size // 2
    extended = np.pad(domain, (ph, pw), 'constant')
    h, w = domain.shape
    pos = [(i, j) for (i, j) in product(
        range(-(size // 2), size // 2 + 1), repeat=2)]
    result = np.zeros((h, w)).astype(domain.dtype)
    for r in range(ph, extended.shape[0] - ph):
        for c in range(pw, extended.shape[1] - pw):
            maximum = max([extended[r + wr][c + wc] for wr, wc in pos])
            result[r - ph][c - pw] = maximum
    return result


def main():
    domain = np.array([[0, 0, 0, 0, 0],
                       [0, 2, 0, 0, 0],
                       [0, 0, 1, 0, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0]])
    print(scipy_case(domain))
    print(scratch(domain))
if __name__ == '__main__':
    main()
