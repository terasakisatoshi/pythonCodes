"""
Reference:
https://github.com/bokeh/bokeh/blob/master/examples/plotting/server/animated.py
"""

import numpy as np
from bokeh.plotting import figure, output_file, show, curdoc
from bokeh.models import ColumnDataSource, Div
from bokeh.layouts import gridplot, column
from bokeh.client import push_session

init_degree = 30


def rot_mat(degree):
    theta = np.deg2rad(degree)
    mat = np.array([[np.cos(theta), -np.sin(theta)],
                    [np.sin(theta), np.cos(theta)]])
    return mat


def main():
    xs = np.linspace(-np.pi, np.pi, 11)
    ys = xs
    Xs, Ys = np.meshgrid(xs, ys)
    Xs, Ys = Xs.flatten(), Ys.flatten()

    mat = rot_mat(init_degree)

    transXs, transYs = mat @ np.array([Xs, Ys])

    output_file("lasso_selector.html")
    TOOLS = "pan,lasso_select,save,reset"
    source = ColumnDataSource(data=dict(Xs=Xs,
                                        Ys=Ys,
                                        transXs=transXs,
                                        transYs=transYs))

    f = figure(tools=TOOLS, title="target",
               x_range=(-np.pi*np.sqrt(2)-1, np.pi*np.sqrt(2)+1),
               y_range=(-np.pi*np.sqrt(2)-1, np.pi*np.sqrt(2)+1))
    f.circle('Xs', 'Ys', source=source)

    transf = figure(x_range=f.x_range,
                    y_range=f.y_range,
                    tools=TOOLS,
                    title="trans")
    transf.circle('transXs', 'transYs', source=source, size=6)

    degree = init_degree
    def update():
        nonlocal degree
        degree += 1
        new_mat = rot_mat(degree)
        transXs, transYs = new_mat @ np.array([Xs, Ys])
        source.data = dict(Xs=Xs,
                           Ys=Ys,
                           transXs=transXs,
                           transYs=transYs)
        transf.title.text = "theta={}".format(degree % 360)

    grid = gridplot([[f, transf]])
    plot = column(Div(text="<h2>Transform before and after</h2>"),
                  grid)
    document = curdoc()
    document.add_root(plot)
    document.add_periodic_callback(update, 60)


main()
