"""
https://matplotlib.org/users/event_handling.html
"""
from imageio import imread
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


def update(event_handler):
    """post processing updating artist objects"""

    def event_handler_decorated(self, *args, **kwargs):
        event_handler(self, *args, **kwargs)
        # self.ax.imshow(self.bgimg)
        self.ax.set_xlim(0, self.bgimg.shape[1])
        self.ax.set_ylim(0, self.bgimg.shape[0])
        self.ax.invert_yaxis()
        self.fig.canvas.draw()
    return event_handler_decorated


def visible_selector(action):
    def actions_decorated(self, x, y):
        action(self, x, y)
        self.selected_object.set_visible(True)
        self.selected_object.set_data(x, y)
    return actions_decorated


def unvisible_selector(action):
    def action_decorated(self, *args):
        action(self, *args)
        self.selected_object.set_visible(False)
    return action_decorated


class PointHandler:

    def __init__(self, fig, ax, img):
        self.fig = fig
        self.ax = ax
        self.bgimg = img
        # coords
        xs = np.array([])
        ys = np.array([])
        # artists
        self.moving_object, = ax.plot([0], [0], 'go', visible=False)
        self.selected_object, = ax.plot([0], [0], 'ro', ms=12, visible=False)
        self.plot_objects = {}
        # picking flag
        self.picking_object = None
        self.num_artists = 0
        self.ax.set_xlim(0, self.bgimg.shape[1])
        self.ax.set_ylim(0, self.bgimg.shape[0])
        self.ax.imshow(self.bgimg)
        self.ax.invert_yaxis()
        # regist event handler
        # the order of mpl_connect is important
        self.fig.canvas.mpl_connect("button_press_event", self.on_pressed)
        self.fig.canvas.mpl_connect("motion_notify_event", self.on_motion)
        self.fig.canvas.mpl_connect("pick_event", self.on_picked)
        self.fig.canvas.mpl_connect("button_release_event", self.on_release)

    @update
    def on_pressed(self, event):
        """generate point where mouse pushed with left click"""
        if event.button != LEFT_CLICK:
            return
        if event.inaxes != self.ax:
            return
        if self.picking_object:
            return
        self.add_point(event.xdata, event.ydata)

    @update
    def on_motion(self, event):
        """drag point"""
        if not self.picking_object:
            return
        self.moving_object.set_data(event.xdata, event.ydata)
        self.moving_object.set_visible(True)
        self.fig.canvas.draw()

    @update
    def on_picked(self, event):
        """select point which mouse does"""
        artists = self.plot_objects.keys()
        if not event.artist in artists:
            # do nothing
            return
        if not len(event.ind):
            # do nothing
            return

        if event.mouseevent.button == RIGHT_CLICK:

            # remove point where mouse pushed with right click
            self.remove_point(event.artist)

        if event.mouseevent.button == LEFT_CLICK:
            self.picking_object = event.artist

    @update
    def on_release(self, event):
        if self.picking_object:
            self.move_picking_object(event.xdata, event.ydata)
        # reset state
        self.picking_object = None
        self.moving_object.set_visible(False)

    @visible_selector
    def add_point(self, x, y):
        i = self.num_artists % len(COLOR_MAP)
        artist, = self.ax.plot([x], [y], 'o', color=COLOR_MAP[i], picker=5)
        self.num_artists += 1
        self.plot_objects[artist] = [i, x, y]

    @visible_selector
    def move_picking_object(self, x, y):
        self.picking_object.set_data(x, y)

    @unvisible_selector
    def remove_point(self, artist):
        del self.plot_objects[artist]
        artist.set_visible(False)
        del artist


def main():
    fig, ax = plt.subplots()
    ax.set_title(
        "Left click to build point. Right click to remove point.")
    bgimg = imread("goma.jpg")
    pthandler = PointHandler(fig, ax, bgimg)
    plt.show()


if __name__ == '__main__':
    main()
