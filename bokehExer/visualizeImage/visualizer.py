"""
Usage
$ bokeh serve --show visualizer.py 
"""
from bokeh.layouts import row, column, gridplot
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Select
from bokeh.plotting import figure
from bokeh.models.ranges import Range1d
import imageio
import numpy as np


class DataViewer():

    def __init__(self):
        img = imageio.imread("gray.png").astype(np.uint8)
        self.target = np.empty(img.shape[:2], dtype=np.uint32)
        view = self.target.view(dtype=np.uint8).reshape((img.shape[0], img.shape[1], 4))
        view[:, :, :3] = img
        view[:, :, 3] = 255
        self.fig = self.define_figure('image')
        dh, dw = self.target.shape[:2]
        self.source = ColumnDataSource(
            data={"image": [self.target], "dh": [dh], "dw": [dw]}
        )
        self.register_image(self.fig, self.source)
        self.select = Select(
            title="Option:",
            value="gray.png",
            options=["gray.png", "white.png", "black.png", "python.png"]
        )
        self.plot = column(self.select, self.fig)
        self.select.on_change("value", self.update_image)

    def define_figure(self, title):
        return figure(
            title=title,
            match_aspect=True,
            tools="",
        )

    def register_image(self, fig, source):
        fig.image_rgba(
            'image',
            x=0, y=0,
            dh="dh",
            dw="dw",
            source=source,
        )

    def update_image(self, attr, old, new):
        print(attr, old, new)
        img = imageio.imread(new).astype(np.uint8)
        dh, dw = img.shape[:2]
        img_ = np.empty(img.shape[:2], dtype=np.uint32)
        # RGBA
        view = img_.view(dtype=np.uint8).reshape((dh, dw, 4))
        view[:, :, :3] = img
        view[:, :, 3] = 255
        self.fig.title.text = new
        self.source.data = {"image": [img_], "dh": [dh], "dw": [dw]}


def main():
    import imageio
    imageio.imwrite("black.png", 10 * np.ones((100, 200, 3)).astype(np.uint8))
    imageio.imwrite("gray.png", 128 * np.ones((400, 100, 3)).astype(np.uint8))
    imageio.imwrite("white.png", 240 * np.ones((100, 10, 3)).astype(np.uint8))
    document = curdoc()
    viewer = DataViewer()
    document.add_root(viewer.plot)

main()
