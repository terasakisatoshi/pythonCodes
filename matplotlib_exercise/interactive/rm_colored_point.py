from matplotlib import pyplot as plt
import numpy as np

LEFT_CLICK = 1
RIGHT_CLICK = 3

COLOR_MAP = [[255, 0, 0], [255, 85, 0], [255, 170, 0],
             [255, 255, 0], [170, 255, 0], [85, 255, 0],
             [0, 255, 0], [0, 255, 85], [0, 255, 170],
             [0, 255, 255], [0, 170, 255], [0, 85, 255],
             [0, 0, 255], [85, 0, 255], [170, 0, 255],
             [255, 0, 255], [255, 0, 170], [255, 0, 85]]

COLOR_MAP = np.array(COLOR_MAP) / 255.


class PointRemover:
    """point remover"""

    def __init__(self, pts):
        pts = np.asarray(pts)
        fig, ax = plt.subplots()
        self.fig = fig
        self.ax = ax
        self.ax.set_xlim([0, 3])
        self.ax.set_ylim([0, 3])
        xs = pts[:, 0]
        ys = pts[:, 1]
        self.ax.set_title("right click to remove point")
        # register point objects which reacts mouse pick event
        self.plot_objects = {}
        for i, (x, y) in enumerate(zip(xs, ys)):
            artist, = self.ax.plot(x, y, 'o', color=COLOR_MAP[i], picker=5)
            self.plot_objects[artist] = (i, x, y)
        # register event handler
        self.fig.canvas.mpl_connect("pick_event", self.remove_point)

    def remove_point(self, event):
        """
        remove point when user acts right click
        """
        if event.mouseevent.button != RIGHT_CLICK:
            return
        artists = self.plot_objects.keys()
        if not event.artist in artists:
            # do nothing
            return
        if not len(event.ind):
            # do nothing
            return
        del self.plot_objects[event.artist]
        print(len(self.plot_objects))
        new_plot_objects = {}
        self.ax.clear()
        for (i, x, y) in self.plot_objects.values():
            artist, = self.ax.plot(x, y, 'o', color=COLOR_MAP[i], picker=5)
            new_plot_objects[artist] = (i, x, y)

        self.plot_objects = new_plot_objects
        self.ax.set_xlim([0, 3])
        self.ax.set_ylim([0, 3])
        self.fig.canvas.draw()


def main():
    pts = 3 * np.random.rand(10, 10)
    generator = PointRemover(pts)
    plt.show()
if __name__ == '__main__':
    main()
