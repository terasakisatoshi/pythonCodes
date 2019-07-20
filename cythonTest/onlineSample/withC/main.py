from call_c import csum_combi
import numpy as np
import time


def main():
    N = 10000

    xs = np.arange(N).astype(np.int32)
    ys = np.arange(N).astype(np.int32)

    start = time.time()
    total = csum_combi(xs, ys)
    end = time.time()

    print(total)
    print('elapsed', end-start)


if __name__ == '__main__':
    main()
