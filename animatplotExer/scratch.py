import itertools
import logging
logging.basicConfig(level=logging.INFO)
import random

import matplotlib.animation as animation
from matplotlib import pyplot as plt
import numpy as np


def do_somehting(xs, ts):
    for t in ts:
        yield xs, np.sin(2 * np.pi * (xs + t))


class Visualizer():

    def __init__(self, xs, ts):
        self.fig, self.ax = plt.subplots()
        self.iterator = itertools.cycle(do_somehting(xs, ts))

    def init_func(self):
        self.step = 0

    def update(self, *args):
        self.ax.clear()
        logging.info("i={}".format(self.step))
        xs, ys = self.iterator.__next__()
        self.ax.plot(xs, ys)
        self.ax.set_title("step={}".format(self.step))
        self.step += 1


def main():
    xs = np.linspace(0, 1, 50)
    ts = np.linspace(0, 1, 20)
    visualizer = Visualizer(xs, ts)

    ani = animation.FuncAnimation(visualizer.fig,
                                  visualizer.update,
                                  init_func=visualizer.init_func,
                                  frames=100,
                                  interval=100)

    ani.save('test.gif', writer="imagemagick")


if __name__ == '__main__':
    main()
