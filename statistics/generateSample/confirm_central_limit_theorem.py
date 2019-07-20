import numpy as np
from matplotlib import pyplot as plt
from scipy import integrate


def main():
    fig, axes = plt.subplots(2, 2, figsize=(7, 7))
    f = lambda x: 7 * x**6
    print("theoretical truth")
    mu_ground_truth, _ = integrate.quad(lambda x: x * f(x), 0, 1)
    print("mu", mu_ground_truth)
    print("sigma^2", integrate.quad(lambda x: x **
                                    2 * f(x), 0, 1)[0] - mu_ground_truth**2)

    for i, n in enumerate([5, 10, 1000, 10000]):
        mus = []
        for repeat in range(10000):
            uniform = np.random.random(n)
            mu = np.mean(uniform**(1 / 7))
            mus.append(mu)
        print("mu bar", np.mean(mus))
        print("var bar", n * np.var(mus))
        axes[i // 2][i % 2].set_title('num sample = {}'.format(n))
        axes[i // 2][i % 2].set_xlabel('average')
        axes[i // 2][i % 2].set_ylabel('frequency')
        axes[i // 2][i % 2].hist(mus, bins=50)

    plt.show()
if __name__ == '__main__':
    main()
