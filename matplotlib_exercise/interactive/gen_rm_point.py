"""
https://matplotlib.org/users/event_handling.html
"""

from matplotlib import pyplot as plt
import numpy as np

LEFT_CLICK = 1
RIGHT_CLICK = 3


class PointHander:

    def __init__(self):
        fig, ax = plt.subplots()
        self.fig = fig
        self.ax = ax
        self.ax.set_xlim([0, 3])
        self.ax.set_ylim([0, 3])
        self.ax.set_title(
            "left click to build point. right click to remove point")
        self.xs = np.array([])
        self.ys = np.array([])
        self.plot_objects, = self.ax.plot(self.xs, self.ys, 'o', picker=5)
        # regist event handler
        self.fig.canvas.mpl_connect("pick_event", self.remove_point)
        self.fig.canvas.mpl_connect("button_press_event", self.generate_point)

    def generate_point(self, event):
        """generate point where mouse pushed"""
        print("button pushed")
        if event.button != LEFT_CLICK:
            # do nothing
            return
        if event.inaxes != self.ax:
            # do nothing
            return
        self.xs = np.append(self.xs, event.xdata)
        self.ys = np.append(self.ys, event.ydata)

        self.plot_objects.set_data(self.xs, self.ys)
        self.fig.canvas.draw()

    def remove_point(self, event):
        """remove point when user acts right click"""
        print("hi")
        if event.mouseevent.button != RIGHT_CLICK:
            return
        if event.artist != self.plot_objects:
            # do nothing
            return
        if not len(event.ind):
            # do nothing
            return
        # find nearest object from position which is mouse clicked
        mouse_x = event.mouseevent.xdata
        mouse_y = event.mouseevent.ydata
        distances = np.hypot(mouse_x - self.xs[event.ind],
                             mouse_y - self.ys[event.ind])
        argmin = distances.argmin()
        remove_index = event.ind[argmin]

        self.xs = np.delete(self.xs, remove_index)
        self.ys = np.delete(self.ys, remove_index)

        self.plot_objects.set_data(self.xs, self.ys)
        self.fig.canvas.draw()


def main():
    pthandler = PointHander()
    plt.show()


if __name__ == '__main__':
    main()
