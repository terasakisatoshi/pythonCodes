import csv
from collections import defaultdict
from glob import glob
import os

from imageio import imread
import numpy as np
import sys
import tkinter as tk
from tkinter import scrolledtext as tkst
from tkinter import messagebox as tkmsg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
import tkinter.filedialog as tkfd

from annotations import KEYPOINTS, COLOR_MAP
from handling_point import PointHandler, USAGE


class AnnotationViewer():

    def __init__(self, parent, image_path):
        fig, ax = plt.subplots()
        self.parent = parent
        self.image_path = image_path
        self.back_ground_image = imread(image_path)
        self.fig = fig
        self.ax = ax
        self.plot_frame = tk.Frame(parent)
        self.pthandler = PointHandler(
            self.fig, self.ax, self.image_path)
        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        # regist event handler
        # the order of mpl_connect is important
        canvas.mpl_connect("button_press_event", self.pthandler.on_pressed)
        canvas.mpl_connect("motion_notify_event", self.pthandler.on_motion)
        canvas.mpl_connect("pick_event", self.pthandler.on_picked)
        # both bind is very important for release event but I do not know why
        canvas._tkcanvas.bind('button_release_event',
                              self.pthandler.on_release)
        canvas.mpl_connect('button_release_event', self.pthandler.on_release)
        canvas.mpl_connect("key_press_event", self.pthandler.on_key_press)
        self.canvas = canvas
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


class AnnotationApp(tk.Tk):

    def __init__(self, paths):
        super(AnnotationApp, self).__init__()
        self.paths = paths
        self.current_file_idx = 0
        self.image_path = paths[0]
        self.state_text = ""
        self.setting_gui()
        self.protocol("WM_DELETE_WINDOW", self.quit_app)

    def setting_gui(self):
        self.viewer = AnnotationViewer(self, self.image_path)
        self.viewer.plot_frame.pack(fill=tk.BOTH, expand=True)

        operation_frame = tk.Frame(self)
        operation_frame.pack()
        usage_label = tkst.ScrolledText(
            master=self,
            height=6,
        )
        usage_label.insert(tk.INSERT, USAGE)
        usage_label.config(state=tk.DISABLED)
        usage_label.pack(expand=True)

        quit_frame = tk.Frame(self)
        quit_frame.pack(fill=tk.X, expand=True)
        # buttons
        open_button = tk.Button(operation_frame, text="open[ctrl or cmd + o]")
        open_button.bind("<Button-1>", self.load_data)
        open_button.grid(row=0, column=0)

        save_button = tk.Button(operation_frame, text="save[ctrl or cmd + s]")
        save_button.grid(row=0, column=1)
        save_button.bind("<Button-1>", self.save)

        clear_button = tk.Button(operation_frame, text="clear")
        clear_button.bind("<Button-1>", self.clear)
        clear_button.grid(row=0, column=2)

        prev_load_button = tk.Button(
            operation_frame, text="load previous data", command=self.load_prev)
        prev_load_button.grid(row=1, column=0)
        next_load_button = tk.Button(
            operation_frame, text="load next data", command=self.load_next)
        next_load_button.grid(row=1, column=2)

        quit_button = tk.Button(quit_frame,
                                text="quit", command=self.quit_app)
        quit_button.pack()

        self.bind('<Control-o>', self.load_data)
        self.bind('<Command-o>', self.load_data)
        self.bind('<Control-s>', self.save)
        self.bind('<Command-s>', self.save)

    def ask_save_or_not(self):
        if self.viewer.pthandler.state_changed:
            msg = tkmsg.askyesnocancel("information",
                                       "Do you want to save the changes")
            if msg is None:
                return None
            if msg:
                self.save()
                self.viewer.pthandler.state_changed = False
                # save and go to next
                return True
            else:
                self.viewer.pthandler.state_changed = False
                # no save
                return False
        # no save
        return False

    def quit_app(self, *_):
        if self.ask_save_or_not() is None:
            # do nothing
            return
        self.quit()
        self.destroy()

    def load(self, image_path):
        self.clear()
        try:
            bgimg = imread(image_path)
        except Exception as e:
            tkmsg.showerror("Error", "invalid file this is not image file")
            return
        self.viewer.pthandler.image_path = image_path
        self.viewer.pthandler.bgimg = bgimg
        ax = self.viewer.pthandler.ax
        ax.imshow(bgimg)
        tsv_path = os.path.splitext(image_path)[0] + ".tsv"
        if not os.path.exists(tsv_path):
            return
        with open(tsv_path, "r") as tsvfile:
            reader = csv.DictReader(tsvfile, delimiter="\t")
            for obj_idx, row in enumerate(reader):
                for anno_idx, anno in enumerate(KEYPOINTS):
                    x = row[anno + "X"]
                    y = row[anno + "Y"]
                    if x != "None" and y != "None":
                        x, y = int(x), int(y)
                        artist, = ax.plot(x, y, 'o', color=np.array(
                            COLOR_MAP[anno]) / 255.0)
                        self.viewer.pthandler.plotted_objects[
                            (obj_idx, anno_idx)] = artist
                        self.viewer.pthandler.plotted_objects[
                            artist] = (obj_idx, anno_idx)
        # update
        self.viewer.pthandler.update_ax()
        self.viewer.pthandler.fig.canvas.draw()
        # reset state_changed property
        self.viewer.pthandler.state_changed = False

    def load_data(self, event):
        if self.ask_save_or_not() is None:
            # do nothing
            return
        # TODO select file types
        image_path = tkfd.askopenfilename()
        if image_path:
            self.image_path = image_path
            self.load(self.image_path)

    def load_next(self):
        if self.ask_save_or_not() is None:
            # do nothing
            return
        self.current_file_idx += 1
        self.image_path = self.paths[self.current_file_idx % len(self.paths)]
        self.load(self.image_path)

    def load_prev(self):
        if self.ask_save_or_not() is None:
            # do nothing
            return
        self.current_file_idx -= 1
        self.image_path = self.paths[self.current_file_idx % len(self.paths)]
        self.load(self.image_path)

    def clear(self, *_):
        self.viewer.pthandler.state_changed = True
        self.viewer.pthandler.current_target_idx = 0
        self.viewer.pthandler.current_annotation_idx = 0
        self.viewer.pthandler.plotted_objects = {}
        self.viewer.pthandler.ax.clear()
        self.viewer.pthandler.ax.imshow(self.viewer.pthandler.bgimg)
        self.viewer.pthandler.update_ax()
        self.viewer.pthandler.selected_object, = self.viewer.pthandler.ax.plot(
            [], [], 'ko', ms=12, visible=False)
        self.viewer.pthandler.fig.canvas.draw()

    def save(self, *_):
        objects = self.viewer.pthandler.plotted_objects
        fieldnames = ["ID"]
        for anno in KEYPOINTS:
            fieldnames.extend([anno + "X", anno + "Y"])

        save_path = os.path.splitext(self.image_path)[0]
        save_path = save_path + ".tsv"
        with open(save_path, "w") as tsvfile:
            writer = csv.DictWriter(tsvfile,
                                    fieldnames=fieldnames, delimiter="\t")
            writer.writeheader()
            data_dict = defaultdict(dict)
            for k in objects:
                if isinstance(k, tuple):
                    artist = objects[k]
                    if artist.get_visible():
                        x, y = artist.get_xydata()[0]
                        x = int(x + 0.5)
                        y = int(y + 0.5)
                        obj_id, anno_id = k
                        data_dict[obj_id][KEYPOINTS[anno_id] + "X"] = x
                        data_dict[obj_id][KEYPOINTS[anno_id] + "Y"] = y
                        data_dict[obj_id]["ID"] = obj_id
            for obj_id, data in data_dict.items():
                # fill "None" for non registered annotations
                for anno in KEYPOINTS:
                    if data.get(anno + "X") is None:
                        data[anno + "X"] = "None"
                    if data.get(anno + "Y") is None:
                        data[anno + "Y"] = "None"

                writer.writerow(data)
        self.viewer.pthandler.state_changed = False


def main():
    targetdir = "resized"
    paths = glob(os.path.join(targetdir, "*.JPG"))
    app = AnnotationApp(paths)
    app.title('Gomannotation Tool')

    # prevents crashing when scrolling in plot
    # https://github.com/matplotlib/matplotlib/issues/9637
    while True:
        try:
            app.mainloop()
        except UnicodeDecodeError:
            continue
        break


if __name__ == '__main__':
    main()
