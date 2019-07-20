"""
Main Reference:
https://qiita.com/ceptree/items/c547116bda4a5db11596
"""

import numpy as np
from matplotlib import pyplot as plt


def update(event_hanlder):
    def decorated_function(self, *args, **kwargs):
        event_hanlder(self, *args, **kwargs)
        self.track_object.set_data(self.xs, self.ys)
        self.fig.canvas.draw()
    return decorated_function


class MouseOrbitTracker:

    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(0, 5)
        self.ax.set_ylim(0, 5)
        self.xs, self.ys = [], []
        self.is_tracking = False
        self.track_object, = self.ax.plot([], [], 'b')
        # regist event handler
        self.fig.canvas.mpl_connect("button_press_event", self.on_pressed)
        self.fig.canvas.mpl_connect("motion_notify_event", self.on_motion)
        self.fig.canvas.mpl_connect("button_release_event", self.on_released)

    @update
    def reset_state(self):
        self.xs, self.ys = [], []

    @update
    def on_pressed(self, event):
        # if event.inaxes != self.ax:
        #    return
        self.reset_state()
        # start to track
        self.is_tracking = True
        self.xs = [event.xdata]
        self.ys = [event.ydata]

    @update
    def on_motion(self, event):
        if not self.is_tracking:
            return
        else:
            self.xs.append(event.xdata)
            self.ys.append(event.ydata)

    @update
    def on_released(self, event):
        # end tracking
        self.is_tracking = False


def main():
    tracker = MouseOrbitTracker()
    plt.show()

if __name__ == '__main__':
    main()
