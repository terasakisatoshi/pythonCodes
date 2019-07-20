from bokeh.layouts import gridplot
from bokeh.plotting import figure, output_file, show

import numpy as np


def main():
    xs = np.linspace(-np.pi, np.pi, 100, endpoint=True)
    xs = np.linspace(0, 4*np.pi, 100)
    ys_exp = np.exp(xs)
    ys_sin = np.sin(xs)
    ys_cos = np.sin(xs)
    ys_tan = np.tan(xs)

    output_file("grid_example.html")

    fig1 = figure(width=250, plot_height=250, title=None)
    fig1.circle(xs, ys_exp, size=10, color="navy", alpha=0.5)

    fig2 = figure(width=250, plot_height=250, title=None)
    fig2.triangle(xs, ys_sin, size=10, color="firebrick", alpha=0.5)

    fig3 = figure(width=250, height=250, title=None)
    fig3.square(xs, ys_cos, color="olive")

    fig4 = figure(width=250, height=250, title=None)
    fig4.line(xs, ys_tan, color="green")

    show(gridplot([[fig1,fig2],[fig3,fig4]]))

if __name__ == '__main__':
    main()
