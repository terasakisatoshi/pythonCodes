import logging
logging.basicConfig(level=logging.INFO)
import random

import matplotlib.animation as animation
from matplotlib import pyplot as plt


def get_arg_min(arr):
    m = min(arr)
    for i, a in enumerate(arr):
        if a == m:
            return i, m


def do_selection_sort(arr):
    # yield initial array
    yield arr

    for i, v in enumerate(arr):
        if i == len(arr) - 1:
            break
        seq = arr[i + 1:]
        arg_min, minimum = get_arg_min(seq)
        if v > minimum:
            j = i + 1 + arg_min
            arr[i], arr[j] = arr[j], arr[i]
        yield arr


class Visualizer():

    def __init__(self, arr):
        self.fig, self.ax = plt.subplots()
        self.iterator = do_selection_sort(arr)
        self.arr = arr

    def init_func(self):
        self.step = 0

    def update(self, *args):
        self.ax.clear()
        logging.info("i={}".format(self.step))
        try:
            arr = self.iterator.__next__()
        except StopIteration:
            arr = self.arr

        logging.info("arr={}".format(arr))
        self.ax.bar(range(len(arr)), arr)
        self.ax.set_xticks(list(range(max(self.arr) + 1)))
        self.ax.set_yticks(list(range(max(self.arr) + 1)))
        self.ax.set_title("step={}".format(self.step))
        self.step += 1

arr = list(range(20))
random.shuffle(arr)
visualizer = Visualizer(arr)


ani = animation.FuncAnimation(visualizer.fig,
                              visualizer.update,
                              init_func=visualizer.init_func,
                              frames=len(arr),
                              interval=1000)

ani.save('test.gif', writer="imagemagick")
