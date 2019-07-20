from matplotlib import pyplot as plt
import numpy as np

LEFT_CLICK = 1
RIGHT_CLICK = 3


class PointRemover:
    """point remover"""

    def __init__(self, pts):
        pts = np.asarray(pts)
        fig, ax = plt.subplots()
        self.fig = fig
        self.ax = ax
        self.ax.set_xlim([0, 3])
        self.ax.set_ylim([0, 3])
        self.xs = pts[:, 0]
        self.ys = pts[:, 1]
        self.ax.set_title("right click to remove point")
        # register point objects which reacts mouse pick event
        self.plot_objects, = self.ax.plot(self.xs, self.ys, 'o', picker=5)
        # register event handler
        self.fig.canvas.mpl_connect("pick_event", self.remove_point)

    def remove_point(self, event):
        """
        remove point when user acts right click
        """
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
    pts = 3 * np.random.rand(10, 10)
    generator = PointRemover(pts)
    plt.show()
if __name__ == '__main__':
    main()
