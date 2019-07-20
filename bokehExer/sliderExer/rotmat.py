import numpy as np
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Slider
from bokeh.layouts import column, widgetbox, gridplot
from bokeh.io import curdoc


def rot_mat(degree):
    theta = np.deg2rad(degree)
    mat = np.array([[np.cos(theta), -np.sin(theta)],
                    [np.sin(theta), np.cos(theta)]])
    return mat


class RotationViewer(object):

    def __init__(self):
        xs = np.linspace(-np.pi, np.pi, 11)
        ys = xs
        Xs, Ys = np.meshgrid(xs, ys)
        self.Xs, self.Ys = Xs.flatten(), Ys.flatten()
        initdegree = 0
        mat = rot_mat(initdegree)
        transXs, transYs = mat @ np.array([self.Xs, self.Ys])

        TOOLS = "pan,lasso_select,save,reset"

        self.source = ColumnDataSource(data=dict(Xs=self.Xs, Ys=self.Ys,
                                                 transXs=transXs,
                                                 transYs=transYs))

        self.fig = figure(tools=TOOLS, title="target",
                          x_range=(-np.pi*np.sqrt(2)-1, np.pi*np.sqrt(2)+1),
                          y_range=(-np.pi*np.sqrt(2)-1, np.pi*np.sqrt(2)+1))
        self.fig.circle('Xs', 'Ys', source=self.source)

        self.transfig = figure(tools=TOOLS, title="transformed",
                               x_range=self.fig.x_range, y_range=self.fig.y_range)
        self.transfig.circle('transXs', 'transYs', source=self.source, size=6)

        self.rot_param = Slider(title="degree", value=0,
                                start=0, end=360, step=1)
        self.rot_param.on_change('value', self.update_data)

        self.plot = column(self.rot_param, gridplot([[self.fig, self.transfig]]))

    def update_data(self, attr, old, new):
        mat = rot_mat(self.rot_param.value)
        transXs, transYs = mat @ np.array([self.Xs, self.Ys])
        self.source.data = dict(Xs=self.Xs, Ys=self.Ys,
                                transXs=transXs, transYs=transYs)
        self.transfig.title.text = "degree {}".format(self.rot_param.value)


def main():
    viewer = RotationViewer()
    document = curdoc()
    document.add_root(viewer.plot)

main()
