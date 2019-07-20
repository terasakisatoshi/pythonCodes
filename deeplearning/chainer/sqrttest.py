import numpy as np
import chainer
import chainer.functions as F


def main():

    for _ in range(1000):
        inp = np.random.random((2, 3, 224, 224)).astype(np.float32)
        ret = F.sqrt(F.relu(inp - 0.5)).array
        assert np.sum(np.isnan(ret)) == 0

    print("no error")


if __name__ == '__main__':
    main()
