import numpy as np

from bokeh.io import curdoc
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Slider, TextInput
from bokeh.layouts import row, widgetbox
from bokeh.client import push_session


class BokehViewer():

    def __init__(self, xs, ys):
        self.xs=xs
        self.ys=ys
        self.source = ColumnDataSource(data=dict(xs=xs, ys=ys))
        self.fig = figure(title='sin function',
                          x_range=[min(xs), max(ys)],
                          y_range=[min(ys), max(ys)])
        self.fig.line('xs', 'ys', source=self.source)
        self.text = TextInput(title='Title',
                              value='sin function')
        self.offset = Slider(title="offset", value=0.0,
                             start=-5.0, end=5.0, step=0.1)
        self.amplitude = Slider(title="amplitude", value=1.0,
                                start=-5.0, end=5.0, step=0.1)
        self.phase = Slider(title="phase", value=0.0,
                            start=0.0, end=2*np.pi, step=0.1)
        self.freq = Slider(title="frequency", value=1.0,
                           start=0.1, end=5.1, step=0.1)
        
        widget_list = [self.text, self.offset,
                       self.amplitude, self.phase, self.freq]
        for widget in widget_list:
            if widget!=self.text:
                widget.on_change('value', self.update_data)
            else:
                widget.on_change('value', self.update_title)
        inputs=widgetbox(*[widget_list])
        self.plot=row(inputs,self.fig,width=800)

    def update_data(self, attr, old, new):
        a = self.amplitude.value
        b = self.offset.value
        w = self.phase.value
        k = self.freq.value
        ys = a*np.sin(k*self.xs+w)+b
        self.source.data = dict(xs=self.xs, ys=ys)

    def update_title(self,attr,old,new):
        self.fig.title.text=self.text.value


def main():
    N = 200
    xs = np.linspace(0, 4*np.pi, N)
    ys = np.sin(xs)
    viewer=BokehViewer(xs,ys)
    document=curdoc()
    document.add_root(viewer.plot)

main()