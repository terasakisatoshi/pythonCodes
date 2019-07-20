"""
https://matplotlib.org/users/event_handling.html
"""

from matplotlib import pyplot as plt
import numpy as np

LEFT_CLICK = 1
RIGHT_CLICK = 3


def update(event_handler):
    """post processing updating artist objects"""

    def event_handler_decorated(self, *args, **kwargs):
        event_handler(self, *args, **kwargs)
        self.plot_objects.set_data(self.xs, self.ys)
        self.fig.canvas.draw()
    return event_handler_decorated


def visible_selector(action):
    def actions_decorated(self, x, y):
        action(self, x, y)
        self.selected_object.set_visible(True)
        self.selected_object.set_data(x, y)
    return actions_decorated


def unvisible_selector(action):
    def action_decorated(self):
        action(self)
        self.selected_object.set_visible(False)
    return action_decorated


class PointHandler:

    def __init__(self, fig, ax):
        self.fig = fig
        self.ax = ax
        # coords
        self.xs = np.array([])
        self.ys = np.array([])
        # artists
        self.moving_object, = ax.plot([0, 0], 'go', visible=False)
        self.selected_object, = ax.plot([0, 0], 'ro', ms=12, visible=False)
        self.plot_objects, = ax.plot(
            self.xs, self.ys, 'bo', picker=5, mew=2, mec='g')
        # picking flag
        self.is_picking_object = False

    @update
    def on_pressed(self, event):
        """generate point where mouse pushed with left click"""
        if event.button != LEFT_CLICK:
            return
        if event.inaxes != self.ax:
            return
        if self.is_picking_object:
            return
        self.add_point(event.xdata, event.ydata)

    @update
    def on_motion(self, event):
        """drag point"""
        if not self.is_picking_object:
            return
        self.moving_object.set_visible(True)
        self.moving_object.set_data([event.xdata], [event.ydata])

    @update
    def on_picked(self, event):
        """select point which mouse does"""
        if event.artist != self.plot_objects:
            return
        # find nearest object from position which is mouse clicked
        mouse_x = event.mouseevent.xdata
        mouse_y = event.mouseevent.ydata
        distances = np.hypot(mouse_x - self.xs[event.ind],
                             mouse_y - self.ys[event.ind])
        argmin = distances.argmin()
        self.select_index = event.ind[argmin]

        if event.mouseevent.button == RIGHT_CLICK:
            # remove point where mouse pushed with right click
            self.remove_point()

        if event.mouseevent.button == LEFT_CLICK:
            self.selected_object.set_data(
                self.xs[self.select_index], self.ys[self.select_index])
            self.is_picking_object = True

    @update
    def on_release(self, event):
        if self.is_picking_object:
            self.move_point(event.xdata, event.ydata)
        # reset state
        self.is_picking_object = False
        self.moving_object.set_visible(False)

    @visible_selector
    def add_point(self, x, y):
        self.xs = np.append(self.xs, x)
        self.ys = np.append(self.ys, y)

    @visible_selector
    def move_point(self, x, y):
        self.xs[self.select_index] = x
        self.ys[self.select_index] = y

    @unvisible_selector
    def remove_point(self):
        self.xs = np.delete(self.xs, self.select_index)
        self.ys = np.delete(self.ys, self.select_index)


def main():
    fig, ax = plt.subplots()
    ax.set_title(
        "Left click to build point. Right click to remove point.")
    pthandler = PointHandler(fig, ax)
    # regist event handler
    # the order of mpl_connect is important
    fig.canvas.mpl_connect("button_press_event", pthandler.on_pressed)
    fig.canvas.mpl_connect("motion_notify_event", pthandler.on_motion)
    fig.canvas.mpl_connect("pick_event", pthandler.on_picked)
    fig.canvas.mpl_connect("button_release_event", pthandler.on_release)
    plt.show()


if __name__ == '__main__':
    main()
