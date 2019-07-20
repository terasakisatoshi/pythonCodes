"""
Introduction to animatplot
https://animatplot.readthedocs.io/en/latest/tutorial/getting_started..html#Basic-Animation
"""

import numpy as np
from matplotlib import pyplot as plt
import animatplot as amp


def main():
    xs = np.linspace(0, 1, 50)
    ts = np.linspace(0, 1, 20)
    Xs = np.asarray([xs] * len(ts))
    Ys = [np.sin(2 * np.pi * (xs + t)) for t in ts]
    """
    # you can also write
    Xs, Ts = np.meshgrid(xs, ts)
    Ys = np.sin(2 * np.pi * (Xs + Ts))
    """
    block = amp.blocks.Line(Xs, Ys)
    anim = amp.Animation([block])
    anim.save_gif("sin_curve")
    plt.show()


if __name__ == '__main__':
    main()
