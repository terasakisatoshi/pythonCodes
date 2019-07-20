import numpy as np
from bokeh.palettes import Category20
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Slider
from bokeh.layouts import column, widgetbox, gridplot
from bokeh.io import curdoc


def matrix(a, b, c, d):
    mat = np.array([[a, b],
                    [c, d]])
    return mat


class MatrixViewer(object):

    def __init__(self):
        N = 11
        self.N = N
        xs = np.linspace(-np.pi, np.pi, N)
        ys = xs
        Xs, Ys = np.meshgrid(xs, ys)
        self.Xs, self.Ys = Xs.flatten(), Ys.flatten()
        a, b = 1, 0
        c, d = 0, 1
        mat = matrix(a, b, c, d)
        transXs, transYs = mat @ np.array([self.Xs, self.Ys])

        TOOLS = "pan,save,reset"
        self.dic_xs = {"Xs{}".format(step): self.Xs[N*step:N*(step+1)]
                       for step in range(N)}
        self.dic_ys = {"Ys{}".format(step): self.Ys[N*step:N*(step+1)]
                       for step in range(N)}
        dic_trasn_xs = {"transXs{}".format(
            step): transXs[N*step:N*(step+1)] for step in range(N)}
        dic_trans_ys = {"transYs{}".format(
            step): transYs[N*step:N*(step+1)] for step in range(N)}
        data = {**self.dic_xs, **self.dic_ys, **dic_trasn_xs, **dic_trans_ys}
        colors = Category20[11]
        self.source = ColumnDataSource(data=data)
        self.fig = figure(tools=TOOLS, title="target",
                          x_range=(-np.pi*np.sqrt(2)-1, np.pi*np.sqrt(2)+1),
                          y_range=(-np.pi*np.sqrt(2)-1, np.pi*np.sqrt(2)+1))
        for s in range(N):
            eval("""self.fig.scatter('Xs{0}', 'Ys{0}', 
                                     source=self.source, 
                                     color=colors[{0}])""".format(s))

        self.transfig = figure(tools=TOOLS, title="transformed",
                               x_range=self.fig.x_range,
                               y_range=self.fig.y_range)
        for s in range(N):
            eval("""self.transfig.scatter('transXs{0}', 'transYs{0}', 
                                          source=self.source, 
                                          color=colors[{0}])""".format(s))

        self.a_slider = Slider(title="a", value=a,
                               start=-10, end=10, step=0.1)
        self.b_slider = Slider(title="b", value=b,
                               start=-10, end=10, step=0.1)
        self.c_slider = Slider(title="c", value=c,
                               start=-10, end=10, step=0.1)
        self.d_slider = Slider(title="d", value=d,
                               start=-10, end=10, step=0.1)

        for widget in [self.a_slider, self.b_slider,
                       self.c_slider, self.d_slider]:
            widget.on_change('value', self.update_data)
        box = widgetbox([self.a_slider, self.b_slider,
                         self.c_slider, self.d_slider])
        self.plot = column(gridplot([[self.a_slider, self.b_slider],
                                     [self.c_slider, self.d_slider]]),
                           gridplot([[self.fig, self.transfig]]))

    def update_data(self, attr, old, new):
        N = self.N
        mat = matrix(self.a_slider.value,
                     self.b_slider.value,
                     self.c_slider.value,
                     self.d_slider.value)
        transXs, transYs = mat @ np.array([self.Xs, self.Ys])
        dic_trasn_xs = {"transXs{}".format(step): transXs[N*step:N*(step+1)]
                        for step in range(N)}
        dic_trans_ys = {"transYs{}".format(step): transYs[N*step:N*(step+1)]
                        for step in range(N)}
        data = {**self.dic_xs, **self.dic_ys, **dic_trasn_xs, **dic_trans_ys}
        self.source.data = data


def main():
    viewer = MatrixViewer()
    document = curdoc()
    document.add_root(viewer.plot)

main()
