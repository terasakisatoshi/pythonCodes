# generate sample from pdf `f(x) = 7*x**6`

import numpy as np
from matplotlib import pyplot as plt


def main():
    bins = 50
    num_samples = 100000
    uniform = np.random.random(num_samples)
    plt.hist(uniform ** (1 / 7), bins, normed=True, alpha=0.3, label='hist')
    xs = np.linspace(0, 1, 1000)
    ys = 7 * xs**6
    plt.plot(xs, ys, label="pdf")
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()
