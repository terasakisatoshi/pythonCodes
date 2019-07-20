"""
Reference:
https://github.com/bokeh/bokeh/blob/master/examples/app/sliders.py
"""

import numpy as np
from bokeh.io import curdoc
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Slider, TextInput
from bokeh.layouts import row, widgetbox
from bokeh.client import push_session


def main():
    N = 200
    xs = np.linspace(0, 4*np.pi, N)
    ys = np.sin(xs)
    source = ColumnDataSource(data=dict(xs=xs, ys=ys))

    f = figure(title='sin function',
               x_range=[0, 4*np.pi],
               y_range=[-2.5, 2.5])
    f.line('xs', 'ys', source=source)

    text = TextInput(title="Title",
                     value="sin function")

    offset = Slider(title="offset", value=0.0,
                    start=-5.0, end=5.0, step=0.1)
    amplitude = Slider(title="amplitude", value=1.0,
                       start=-5.0, end=5.0, step=0.1)
    phase = Slider(title="phase", value=0.0,
                   start=0.0, end=2*np.pi, step=0.1)
    freq = Slider(title="frequency", value=1.0,
                  start=0.1, end=5.1, step=0.1)

    def update_title(attr, old, new):
        f.title.text = text.value

    text.on_change("value", update_title)

    def update_data(attr, old, new):
        a = amplitude.value
        b = offset.value
        w = phase.value
        k = freq.value
        xs = np.linspace(0, 4*np.pi, N)
        ys = a*np.sin(k*xs+w)+b
        source.data = dict(xs=xs, ys=ys)

    for widget in [offset, amplitude, phase, freq]:
        widget.on_change('value', update_data)

    inputs = widgetbox(text, offset, amplitude, phase, freq)
    plot = row(inputs, f, width=800)
    document = curdoc()
    document.add_root(plot)

main()
