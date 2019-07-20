from itertools import product
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def main():
    f = lambda x, y: (2 * x**2 + y**2) * np.exp(-(2 * x**2 + y**2))
    num_point = 30
    xs = np.linspace(-2, 2, num_point)
    ys = np.linspace(-2, 2, num_point)
    XX, YY = np.meshgrid(xs, ys, indexing="xy")
    fig, ((ax1, ax2), (ax3, )) = plt.subplots(2, 2, figsize=(5, 5))
    ax1.pcolor(f(XX, YY), cmap="gray")
    ax1.set_aspect('equal')
    ax2 = fig.add_subplot(2, 2, 2, projection='3d')
    ax2.plot_surface(XX, YY, f(XX, YY),
                     rstride=1, cstride=1,
                     alpha=0.3,
                     color="blue", edgecolor="black")
    ax2.set_aspect('equal')
    cs = ax3.contour(XX, YY, f(XX, YY), 5, colors='black')
    ax3.clabel(cs, fmt='%3.2f', fontsize=8)
    ax3.set_aspect('equal')
    plt.show()
if __name__ == '__main__':
    main()
