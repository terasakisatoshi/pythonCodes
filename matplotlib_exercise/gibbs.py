from matplotlib import pyplot as plt
import matplotlib.animation as animation
from math import sqrt, log, sin, cos, pi
import numpy as np
from numpy.random import rand, seed

fig, ax = plt.subplots()
ax.set_xlim(-4, 10)
ax.set_ylim(-4, 4)

b = 0.8
x = 10.0
y = 3.0
times = 200


def update(data, *fargs):
    fig, ax = fargs
    global x, y
    u1 = rand()
    u2 = rand()
    x_old = x
    x = sqrt(-2*log(u1))*cos(2*pi*u2) + b*y
    ax.plot([x_old, x], [y, y], lw=1)
    y_old = y
    y = sqrt(-2*log(u1))*sin(2*pi*u2) + b*x
    ax.plot([x, x], [y_old, y], lw=1)
    ax.set_title("{}".format(data))


def main():
    ani = animation.FuncAnimation(fig, update, interval=100, fargs=(fig, ax))
    ani.save("output.html", writer="imagemagick")

if __name__ == '__main__':
    main()
