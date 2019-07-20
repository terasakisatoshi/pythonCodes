"""
Usage:
$ pip install bokeh
$ bokeh serve --show triangle.py
Then your web browser starts. Enjoy!
"""

import math

import numpy as np
import bokeh.plotting as bp
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Slider
from bokeh.layouts import column, widgetbox, gridplot
from bokeh.io import curdoc
from bokeh.colors import RGB

from bokeh.models import Range1d


def sin(degree):
    return math.sin(math.radians(degree))


def cos(degree):
    return math.cos(math.radians(degree))


def set_patches(alpha, beta):
    alpha_triangle = np.array([[0, 0],
                               [cos(alpha) * cos(beta), 0],
                               [cos(alpha) * cos(beta), sin(alpha) * cos(beta)]])

    beta_triangle = np.array([[0, 0],
                              [cos(alpha) * cos(beta), sin(alpha) * cos(beta)],
                              [cos(alpha + beta), sin(alpha + beta)]])

    misc_triangle = np.array([[cos(alpha) * cos(beta), sin(alpha) * cos(beta)],
                              [cos(alpha) * cos(beta), sin(alpha + beta)],
                              [cos(alpha + beta), sin(alpha + beta)]])

    alpha_xs = alpha_triangle[:, 0]
    alpha_ys = alpha_triangle[:, 1]

    beta_xs = beta_triangle[:, 0]
    beta_ys = beta_triangle[:, 1]

    ab_xs = misc_triangle[:, 0]
    ab_ys = misc_triangle[:, 1]

    xs = [alpha_xs, beta_xs, ab_xs]
    ys = [alpha_ys, beta_ys, ab_ys]
    return xs, ys


def set_lines(alpha, beta):
    sin_ab_line_xs = np.ones(30) * cos(alpha + beta)
    sin_ab_line_ys = np.linspace(0, sin(alpha + beta), 30)
    cos_ab_line_xs = np.linspace(0, cos(alpha + beta), 30)
    cos_ab_line_ys = np.zeros(30)
    xs = [cos_ab_line_xs, sin_ab_line_xs]
    ys = [cos_ab_line_ys, sin_ab_line_ys]
    return xs, ys

alpha = 20
beta = 35
xs, ys = set_patches(alpha=alpha, beta=beta)

abs_range = 1.2

height = abs_range
width = abs_range * 0.90
# adjust aspect ratio
fig = bp.figure(x_range=(-width, width),
                y_range=(-height, height),
                plot_width=500,
                plot_height=500)

color = [RGB(r=255, g=0, b=0, a=0.5),
         RGB(r=0, g=0, b=255, a=0.5),
         RGB(r=0, g=255, b=0, a=0.5)]

patch_source = ColumnDataSource(data=dict(xs=xs,
                                          ys=ys,
                                          color=color))
fig.patches('xs', 'ys',
            source=patch_source,
            color='color')

xs, ys = set_lines(alpha, beta)
dotted_line_source = ColumnDataSource(data=dict(xs=xs,
                                                ys=ys,
                                                color=["black", "black"]))
fig.multi_line('xs', 'ys',
               color="color",
               source=dotted_line_source,
               line_width=2)

# draw top half circle
fig.line(np.linspace(-1, 1, 100),
         np.sqrt(1 - np.linspace(-1, 1, 100)**2),
         line_dash=[4, 4], line_color="orange", line_width=2)
# draw bottom circle
fig.line(np.linspace(-1, 1, 100),
         -np.sqrt(1 - np.linspace(-1, 1, 100)**2),
         line_dash=[4, 4], line_color="orange", line_width=2)

arc_source = ColumnDataSource(data=dict(x=[0, 0, 0], y=[0, 0, 0, ],
                                        radius=[0.2, 0.25, 0.3],
                                        start=[0, math.radians(alpha), 0],
                                        end=[math.radians(alpha), math.radians(
                                            alpha + beta), math.radians(alpha + beta)],
                                        color=["red", "blue", "purple"]))
fig.arc(x='x', y='y',
        radius='radius',
        start_angle='start',
        end_angle='end',
        radius_units="data", color="color", source=arc_source)


alpha_slider = Slider(title="alpha", value=alpha, bar_color="red",
                      start=0, end=360, step=1)
beta_slider = Slider(title="beta", value=beta, bar_color="blue",
                     start=0, end=360, step=1)


def update_alpha(attr, old, new):
    global alpha
    alpha = alpha_slider.value
    xs, ys = set_patches(alpha, beta)
    patch_source.data = dict(xs=xs, ys=ys, color=color)
    xs, ys = set_lines(alpha, beta)
    dotted_line_source.data = dict(
        xs=xs, ys=ys, color=["black", "black"])
    arc_source.data = dict(x=[0, 0, 0], y=[0, 0, 0, ],
                           radius=[0.2, 0.25, 0.3],
                           start=[0, math.radians(alpha), 0],
                           end=[math.radians(alpha), math.radians(
                               alpha + beta), math.radians(alpha + beta)],
                           color=["red", "blue", "purple"])


def update_beta(attr, old, new):
    global beta
    beta = beta_slider.value
    xs, ys = set_patches(alpha, beta)
    patch_source.data = dict(xs=xs, ys=ys, color=color)
    xs, ys = set_lines(alpha, beta)
    dotted_line_source.data = dict(
        xs=xs, ys=ys, color=["black", "black"])
    arc_source.data = dict(x=[0, 0, 0], y=[0, 0, 0, ],
                           radius=[0.2, 0.25, 0.3],
                           start=[0, math.radians(alpha), 0],
                           end=[math.radians(alpha), math.radians(
                               alpha + beta), math.radians(alpha + beta)],
                           color=["red", "blue", "purple"])


alpha_slider.on_change('value', update_alpha)
beta_slider.on_change('value', update_beta)

sliders = column(alpha_slider,
                 beta_slider)
plot = column(sliders, fig)

document = curdoc()
document.add_root(plot)
