from predictor import predict
from kivy.config import Config
Config.set('graphics', 'width', 560)
Config.set('graphics', 'height', 560)
Config.set('graphics', 'resizable', 0)
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex
from kivy.graphics import Color, Line, BindTexture
from matplotlib import pyplot as plt
import numpy as np
from scipy import interpolate
from scipy.misc import imresize


class CanvasWidget(Widget):

    def __init__(self):
        super(CanvasWidget, self).__init__()
        self.locked = False

    def on_touch_down(self, touch):
        # avoid painting line on button
        if Widget.on_touch_down(self, touch):
            return
        if self.locked:
            return

        with self.canvas:
            # add line primitive
            Color(*get_color_from_hex("#0080FF80"))
            touch.ud['current_line'] = Line(
                points=(touch.x, touch.y), width=10)

    def on_touch_move(self, touch):
        if Widget.on_touch_down(self, touch):
            return
        if self.locked:
            return
        if 'current_line' in touch.ud:
            touch.ud['current_line'].points += (touch.x, touch.y)

    def clear_canvas(self):
        # copy children by writing [:]
        saved = self.children[:]

        self.clear_widgets()
        self.canvas.clear()
        for widget in saved:
            self.add_widget(widget)

    def predict_number(self):
        all_pts = []
        for w in self.canvas.children:
            if isinstance(w, Line):
                wpts = np.array(w.points)
                xs = wpts[::2]
                ys = wpts[1::2]
                try:
                    tck, u = interpolate.splprep([xs, ys], s=0)
                except Exception as e:
                    print('warn', e)
                    continue
                u_new = np.arange(np.min(u), np.max(u), 0.01)
                out = interpolate.splev(u_new, tck)
                all_pts += out
        
        img = np.zeros((560+10, 560+10)).astype(np.uint8)
        polyx = np.array(all_pts[::2]).astype(np.int)
        polyy = np.array(all_pts[1::2]).astype(np.int)
        R = 10
        from itertools import product
        for xs, ys in zip(polyx, polyy):
            for x, y in zip(xs, ys):
                circle = [(x+i, y+j) for (i, j) in product(range(-R,
                                                                 R+1), repeat=2) if i**2+j**2 < R**2]
                for c in circle:
                    img[c[0], c[1]] = 128
        img = imresize(np.rot90(img), (28, 28),
                       interp='bilinear').astype('f')/np.max(img)
        plt.imshow(img, cmap='gray')
        plt.show()
        predict(img)


class PaintApp(App):

    def build(self):
        return CanvasWidget()


def main():
    Config.set("input", "mouse", "mouse,disable_multitouch")
    Window.clearcolor = get_color_from_hex("#FFFFFF")
    PaintApp().run()

if __name__ == '__main__':
    main()
