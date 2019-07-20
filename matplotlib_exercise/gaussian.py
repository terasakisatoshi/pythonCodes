from math import pi, sqrt

import numpy as np
from numpy.linalg import det
from matplotlib import pyplot as plt


def main():
    sigma_xx = 1
    sigma_xy = 0
    sigma_yy = 1
    S = np.array([[sigma_xx, sigma_xy],
                  [sigma_xy, sigma_yy]])
    mu_x = 0
    mu_y = 0
    mus = np.array([mu_x, mu_y])
    xs = np.linspace(-2, 2, 50)
    ys = np.linspace(-2, 2, 50)

    a = 1 / 2 / pi / sqrt(det(S))

    f = lambda x, y: a * np.exp(-1 / 2 / det(S) * (sigma_yy * x**2 -
                                                   2 * sigma_xy * x * y + sigma_xx * y**2))
    XX, YY = np.meshgrid(xs, ys)
    plt.contour(XX, YY, f(XX, YY))
    plt.show()
if __name__ == '__main__':
    main()
