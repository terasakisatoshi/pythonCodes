from scipy import ndimage as ndi
import numpy as np
import scipy
from bokeh.io import curdoc
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Slider, TextInput
from bokeh.layouts import row, widgetbox
from bokeh.layouts import gridplot
from bokeh.client import push_session


class ImageViewer():

    def __init__(self, target):
        self.target = target[::-1]
        self.source1 = ColumnDataSource(data=dict(image=[self.target]))
        self.alpha = Slider(title="alpha", value=30,
                            start=10, end=50, step=1)
        self.sigma = Slider(title="sigma", value=3,
                            start=1, end=20, step=1)

        self.fig1 = self.define_figure('image')
        self.regist_image(self.fig1,self.source1)

        blurred = ndi.gaussian_filter(self.target, sigma=self.sigma.value)
        self.source2 = ColumnDataSource(data=dict(image=[blurred]))
        self.fig2 = self.define_figure('blurred')
        self.regist_image(self.fig2,self.source2)


        filtered = ndi.gaussian_filter(blurred, sigma=1)
        sharped = blurred+self.alpha.value*(blurred-filtered)
        sharped = sharped.astype(np.uint8)
        self.source3 = ColumnDataSource(data=dict(image=[sharped]))
        self.fig3 = self.define_figure('sharped')
        self.regist_image(self.fig3,self.source3)

        widget_list = [self.alpha, self.sigma]
        for widget in widget_list:
            widget.on_change('value', self.update_data)
        inputs = widgetbox(*[widget_list])
        self.plot = row(inputs, gridplot(
            [[self.fig1, self.fig2, self.fig3]]), width=600)

    def define_figure(self, title):
        return figure(title=title,
                      plot_width=self.target.shape[1]//2,
                      x_range=[0, self.target.shape[1]],
                      plot_height=self.target.shape[0]//2,
                      y_range=[0, self.target.shape[0]])

    def regist_image(self, fig, source):
        fig.image('image',
                  x=0, y=0,
                  dh=self.target.shape[0], dw=self.target.shape[1],
                  source=source, palette='Greys256')

    def update_data(self, attr, old, new):
        blurred = ndi.gaussian_filter(self.target, sigma=int(self.sigma.value))
        filtered = ndi.gaussian_filter(blurred, sigma=1)
        sharped = blurred+self.alpha.value*(blurred-filtered)
        sharped = sharped.astype(np.uint8)
        self.source2.data = dict(image=[blurred])
        self.source3.data = dict(image=[sharped])
        self.fig1.title.text = '{} {}'.format(
            self.sigma.value, self.alpha.value)


def main():
    target = scipy.misc.face(gray=True)
    viewer = ImageViewer(target)
    document = curdoc()
    document.add_root(viewer.plot)

main()
