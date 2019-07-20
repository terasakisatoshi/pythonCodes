import numpy as np
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Slider, Div
from bokeh.layouts import column, widgetbox, gridplot
from bokeh.io import curdoc


def matrix(a, b, c, d):
    mat = np.array([[a, b],
                    [c, d]])
    return mat


class EigenViewer(object):

    def __init__(self):
        xs = np.linspace(-np.pi, np.pi, 11)
        ys = xs
        Xs, Ys = np.meshgrid(xs, ys)
        self.Xs, self.Ys = Xs.flatten(), Ys.flatten()
        a, b = 1, 0
        c, d = 0, 1
        mat = matrix(a, b, c, d)
        transXs, transYs = mat @ np.array([self.Xs, self.Ys])

        TOOLS = "pan,lasso_select,save,reset"
        self.source = ColumnDataSource(data=dict(Xs=self.Xs, Ys=self.Ys,
                                                 transXs=transXs, transYs=transYs))
        self.evectors = ColumnDataSource(data=dict(ev0x=[0, 0], ev0y=[0, 1],
                                                   ev1x=[0, 1], ev1y=[0, 0],
                                                   transev0x=[0, 0], transev0y=[0, 1],
                                                   transev1x=[0, 1], transev1y=[0, 0]))

        self.fig = figure(tools=TOOLS, title="target",
                          x_range=(-np.pi*np.sqrt(2)-1, np.pi*np.sqrt(2)+1),
                          y_range=(-np.pi*np.sqrt(2)-1, np.pi*np.sqrt(2)+1))
        self.fig.scatter('Xs', 'Ys', source=self.source)
        self.fig.line('ev0x', 'ev0y', source=self.evectors,
                      line_width=5, line_alpha=0.5, color='red')
        self.fig.line('ev1x', 'ev1y', source=self.evectors,
                      line_width=5, line_alpha=0.5, color='blue')
        self.transfig = figure(tools=TOOLS, title="transformed",
                               x_range=self.fig.x_range, y_range=self.fig.y_range)
        self.transfig.circle('transXs', 'transYs', source=self.source)
        self.transfig.line('transev0x', 'transev0y', source=self.evectors,
                           line_width=5, line_alpha=0.5, color='red')
        self.transfig.line('transev1x', 'transev1y', source=self.evectors,
                           line_width=5, line_alpha=0.5, color='blue')
        self.a_slider = Slider(title="a", value=a,
                               start=-10, end=10, step=0.1)
        self.b_slider = Slider(title="b", value=b,
                               start=-10, end=10, step=0.1)
        self.c_slider = Slider(title="c", value=c,
                               start=-10, end=10, step=0.1)
        self.d_slider = Slider(title="d", value=d,
                               start=-10, end=10, step=0.1)
        self.eigen0 = Div(text="eigen0")
        self.eigen1 = Div(text="eigen1")
        for widget in [self.a_slider, self.b_slider, self.c_slider, self.d_slider]:
            widget.on_change('value', self.update_data)
        box = widgetbox([self.a_slider, self.b_slider,
                         self.c_slider, self.d_slider])
        self.plot = column(gridplot([[self.a_slider, self.b_slider, self.eigen0],
                                     [self.c_slider, self.d_slider, self.eigen1]]),
                           gridplot([[self.fig, self.transfig]]))

    def update_data(self, attr, old, new):
        mat = matrix(self.a_slider.value, self.b_slider.value,
                     self.c_slider.value, self.d_slider.value)
        evals, evecs = np.linalg.eig(mat)
        ev0, ev1 = evals
        evec0 = evecs.T[0]
        evec1 = evecs.T[1]
        trans0 = mat @ evec0
        trans1 = mat @ evec1
        self.eigen0.text = "eigen0 = " + \
            str(ev0) if np.isreal(ev0) else "eigen0 = None"
        self.eigen1.text = "eigen1 = " + \
            str(ev1) if np.isreal(ev1) else "eigen1 = None"
        transXs, transYs = mat @ np.array([self.Xs, self.Ys])
        self.source.data = dict(Xs=self.Xs, Ys=self.Ys,
                                transXs=transXs, transYs=transYs)
        data0x = [0, evec0[0]] if np.isreal(ev0) else [0, 0]
        data0y = [0, evec0[1]] if np.isreal(ev0) else [0, 0]
        data1x = [0, evec1[0]] if np.isreal(ev1) else [0, 0]
        data1y = [0, evec1[1]] if np.isreal(ev1) else [0, 0]
        trans0x = [0, trans0[0]] if np.isreal(ev0) else [0, 0]
        trans0y = [0, trans0[1]] if np.isreal(ev0) else [0, 0]
        trans1x = [0, trans1[0]] if np.isreal(ev1) else [0, 0]
        trans1y = [0, trans1[1]] if np.isreal(ev1) else [0, 0]
        self.evectors.data = dict(ev0x=data0x, ev0y=data0y,
                                  ev1x=data1x, ev1y=data1y,
                                  transev0x=trans0x, transev0y=trans0y,
                                  transev1x=trans1x, transev1y=trans1y)


def main():
    viewer = EigenViewer()
    document = curdoc()
    document.add_root(viewer.plot)

main()
