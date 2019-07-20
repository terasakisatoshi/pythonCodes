import numpy as np
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, Div
from bokeh.layouts import gridplot, column


def main():
    xs = np.linspace(-np.pi, np.pi, 10)
    ys = xs
    Xs, Ys = np.meshgrid(xs, ys)
    Xs, Ys = Xs.flatten(), Ys.flatten()

    theta = np.deg2rad(30)
    mat = np.array([[np.cos(theta), -np.sin(theta)],
                    [np.sin(theta), np.cos(theta)]])
    mat = np.array([[1,1],
                    [1,1]])

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
    transf.circle('transXs', 'transYs', source=source,size=6)

    grid = gridplot([[f, transf]])
    show(column(Div(text="<h2>Transform before and after</h2>"), 
                grid))

if __name__ == '__main__':
    main()
