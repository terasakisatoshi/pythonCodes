import numpy as np
from matplotlib import pyplot as plt
import animatplot as amp


def main():
    fig, ax = plt.subplots()
    ax.set_title("sin curve animation")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    xs = np.linspace(0, 1, 50)
    ts = np.linspace(0, 1, 20)
    Xs, Ts = np.meshgrid(xs, ts)
    Ys = np.sin(2 * np.pi * (Xs + Ts))
    block = amp.blocks.Line(Xs, Ys, axis=ax)
    timeline = amp.Timeline(ts, units='s', fps=20)
    anim = amp.Animation([block], timeline)
    anim.controls()
    anim.save_gif("sin_curve_with_contol")
    plt.show()


if __name__ == '__main__':
    main()
