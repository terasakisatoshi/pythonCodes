"""
Image Extractor
You can use this code at your own responsibility because some bugs exist.
Reference:
https://qiita.com/ceptree/items/c547116bda4a5db11596
https://matplotlib.org/gallery/event_handling/viewlims.html#sphx-glr-gallery-event-handling-viewlims-py
"""

import imageio
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


class Box():

    def __init__(self, x1, y1, x2, y2):
        self.update(x1, y1, x2, y2)
        self.rect = Rectangle(
            xy=[self.x1, self.y1], width=self.x2 - self.x1, height=self.y2 - self.y1, fill=False)

    def update(self, x1, y1, x2, y2):
        self.x1, self.x2 = sorted([x1, x2])
        self.y1, self.y2 = sorted([y1, y2])

    def update_rect(self, x1, y1, x2, y2):
        self.update(x1, y1, x2, y2)
        self.rect.set_xy([self.x1, self.y1])
        self.rect.set_width(self.x2 - self.x1)
        self.rect.set_height(self.y2 - self.y1)

    def extract_image(self, image):
        x1, y1, x2, y2 = list(map(int, [self.x1, self.y1, self.x2, self.y2]))
        return image[y1:y2, x1:x2, :]


class ImageExtractor():

    def __init__(self, image):
        fig = plt.figure()
        self.fig = fig
        self.image = image
        self.image_ax = fig.add_subplot(121)
        self.zoom_ax = fig.add_subplot(122)
        self.image_ax.imshow(image)
        self.x1, self.y1, self.x2, self.y2 = 20, 30, 40, 50
        self.box = Box(x1=20, y1=30, x2=40, y2=50)
        self.zoom_ax.imshow(self.box.extract_image(image))
        self.start_drag = False
        self.image_ax.add_patch(self.box.rect)
        self.fig.canvas.mpl_connect('button_press_event', self.onclick)
        self.fig.canvas.mpl_connect('motion_notify_event', self.ondrag)
        self.fig.canvas.mpl_connect("button_release_event", self.onrelease)

    def onclick(self, event):
        if event.inaxes != self.image_ax:
            return
        self.x1 = event.xdata
        self.y1 = event.ydata
        self.start_drag = True

    def ondrag(self, event):
        if event.inaxes != self.image_ax:
            return
        if not self.start_drag:
            return

        self.x2, self.y2 = event.xdata, event.ydata
        self.box.update_rect(self.x1, self.y1, self.x2, self.y2)
        self.zoom_ax.imshow(self.box.extract_image(self.image))
        self.image_ax.figure.canvas.draw()

    def onrelease(self, event):
        if event.inaxes != self.image_ax:
            return
        self.start_drag = False


def main():
    image = imageio.imread("goma.jpg")
    extractor = ImageExtractor(image)
    plt.show()


if __name__ == '__main__':
    main()
