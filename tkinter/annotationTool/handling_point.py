"""
https://matplotlib.org/users/event_handling.html
"""

import warnings
warnings.filterwarnings(action="ignore")  # to ignore UserWarning

from imageio import imread
import matplotlib as mpl

mpl.use("TkAgg")
mpl.rcParams['toolbar'] = 'None'  # disable toolbar

# Disable default key binding.
# https://github.com/matplotlib/matplotlib/issues/4020/
# says to disable default key bindings write
# `fig.canvas.mpl_disconnect(fig.canvas.manager.key_press_handler_id)`
# But this does not work for our application.
# So we set empty list [] for each keymap.
for k in mpl.rcParams:
    if 'keymap' in k:
        mpl.rcParams[k] = []

from matplotlib import pyplot as plt
import numpy as np

from annotations import NUM_POINT_ANNOTATIONS, POINT_ANNOTATIONS_MAP, COLOR_MAP
LEFT_CLICK = 1
RIGHT_CLICK = 3

USAGE = """
How to use Gomannotation tool:
Left click to build point. Right click to remove point.
Press 's' to skip mark. Press 'shit+s' to focus previous annotation
Press 'n' to focus next id of object. Press "b" to back to previous id of object
"""


def update(event_handler):
    """post processing updating artist objects"""

    def event_handler_decorated(self, *args, **kwargs):
        event_handler(self, *args, **kwargs)
        self.update_ax()
        self.fig.canvas.draw()
    return event_handler_decorated


def visualize_selector(action):
    def actions_decorated(self, x, y):
        action(self, x, y)
        self.set_selector_visible(x, y)
    return actions_decorated


def unvisible_selector(action):
    def action_decorated(self, *args):
        action(self, *args)
        self.selected_object.set_visible(False)
    return action_decorated


class PointHandler:

    def __init__(self, fig, ax, image_path):
        self.fig = fig
        self.ax = ax
        self.image_path = image_path
        self.bgimg = imread(image_path)
        # initialize artists
        self.moving_object, = ax.plot([], [], visible=False)
        self.selected_object, = ax.plot([], [], 'ko', ms=12, visible=False)
        self.plotted_objects = {}
        # picking flag
        self.picking_object = None
        self.idx_counter = 0
        self.current_annotation_idx = 0
        self.current_target_idx = 0
        self.update_ax()
        self.ax.imshow(self.bgimg)
        self.state_changed = False

    def set_selector_visible(self, x, y):
        self.selected_object.set_data(x, y)
        self.selected_object.set_visible(True)

    def update_ax(self):
        self.ax.set_xlim(0, self.bgimg.shape[1])
        self.ax.set_ylim(0, self.bgimg.shape[0])
        self.ax.invert_yaxis()
        anno = POINT_ANNOTATIONS_MAP[self.current_annotation_idx]
        self.ax.set_title("{}\nmark object {}'s' {}".format(
            self.image_path, self.current_target_idx, anno))

    @update
    def on_key_press(self, event):
        if event.key == "n":
            # focus next object to mark annotations for the object
            self.current_target_idx += 1
            self.current_annotation_idx = 0

        if event.key == "b":
            # focus previous object to mark annotations for the object
            self.current_target_idx = max(self.current_target_idx - 1, 0)
            self.current_annotation_idx = 0

        if event.key == "s":
            # prompt to next annotation.
            # if current target object is passed focus to next object
            self.current_annotation_idx += 1
            if self.current_annotation_idx >= NUM_POINT_ANNOTATIONS:
                self.current_annotation_idx = 0
                self.current_target_idx += 1

        if event.key == "S":
            # prompt to previous annotation
            # if current annotation is 0, focus to previous object
            self.current_annotation_idx -= 1
            if self.current_annotation_idx < 0:
                self.current_target_idx = max(self.current_target_idx - 1, 0)
                self.current_annotation_idx = 0

        if event.key == "right":
            # skip the current annotation
            self.current_annotation_idx += 1
            self.current_annotation_idx = self.current_annotation_idx % NUM_POINT_ANNOTATIONS

        if event.key == "left":
            self.current_annotation_idx -= 1
            self.current_annotation_idx = self.current_annotation_idx % NUM_POINT_ANNOTATIONS

        artist = self.plotted_objects.get(
            (self.current_target_idx, self.current_annotation_idx))
        if artist is not None and artist.get_visible():
            x, y = artist.get_xydata()[0]
            self.update_selector(x, y)
        else:
            self.selected_object.set_visible(False)

    @update
    def on_pressed(self, event):
        """generate point where mouse pushed with left click"""
        if event.button != LEFT_CLICK:
            return
        if event.inaxes != self.ax:
            return
        if self.picking_object:
            self.set_selector_visible(event.xdata, event.ydata)
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
        artists = self.plotted_objects.values()
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
            anno_idx = self.plotted_objects[event.artist][1]
            anno = POINT_ANNOTATIONS_MAP[anno_idx]
            moving_object, = self.ax.plot(
                [], [], 'o', color=np.array(COLOR_MAP[anno]) / 255.0, alpha=0.5, visible=False)
            self.moving_object = moving_object

    @update
    def on_release(self, event):
        if self.picking_object:
            self.move_picking_object(event.xdata, event.ydata)
        # reset state
        self.picking_object = None
        self.moving_object.set_visible(False)

    @visualize_selector
    def update_selector(self, x, y):
        return

    @visualize_selector
    def add_point(self, x, y):
        self.state_changed = True
        anno = POINT_ANNOTATIONS_MAP[self.current_annotation_idx]
        artist, = self.ax.plot(x, y, 'o', color=np.array(
            COLOR_MAP[anno]) / 255.0, picker=5)

        # if there is already defined object replace new one
        old_artist = self.plotted_objects.get(
            (self.current_target_idx, self.current_annotation_idx))
        if old_artist is not None:
            old_artist.set_visible(False)
            del self.plotted_objects[old_artist]
        self.plotted_objects[
            (self.current_target_idx, self.current_annotation_idx)] = artist
        self.plotted_objects[artist] = (
            self.current_target_idx, self.current_annotation_idx)
        # prompt to next annotation.
        # if current target object is passed focus to next object
        self.current_annotation_idx += 1
        if self.current_annotation_idx >= NUM_POINT_ANNOTATIONS:
            self.current_annotation_idx = 0
            self.current_target_idx += 1

    @visualize_selector
    def move_picking_object(self, x, y):
        self.state_changed = True
        self.picking_object.set_data(x, y)

    @unvisible_selector
    def remove_point(self, artist):
        self.state_changed = True
        artist.set_visible(False)
        del artist


def main():
    fig, ax = plt.subplots()
    pthandler = PointHandler(fig, ax, "goma.tsv")
    # regist event handler
    # the order of mpl_connect is important
    pthandler.fig.canvas.mpl_connect(
        "button_press_event", pthandler.on_pressed)
    pthandler.fig.canvas.mpl_connect(
        "motion_notify_event", pthandler.on_motion)
    pthandler.fig.canvas.mpl_connect("pick_event", pthandler.on_picked)
    pthandler.fig.canvas.mpl_connect(
        "button_release_event", pthandler.on_release)
    pthandler.fig.canvas.mpl_connect("key_press_event", pthandler.on_key_press)

    while True:
        try:
            plt.show()
        except UnicodeDecodeError:
            continue
        break


if __name__ == '__main__':
    main()
