
import numpy as np
from scipy import integrate
from scipy.stats import norm
from bokeh.models import ColumnDataSource, LabelSet
from bokeh.models.widgets import Slider, RangeSlider, Div
from bokeh.plotting import figure, show, output_file
from bokeh.layouts import row, widgetbox
from bokeh.io import curdoc

def func(xs, mu, sigma):
    return 1/(sigma*np.sqrt(2*np.pi))*np.exp(-(xs-mu)**2/(2*sigma**2))
    #return norm.pdf(xs,mu,sigma)


def get_patches(a, b, xs, mu, sigma):
    mask = np.all([a <= xs, xs <= b], axis=0)
    xs2 = xs[mask]
    ys2 = func(xs2, mu, sigma)
    xs2 = np.concatenate([[a, a], xs2, [b, b]])
    ys2 = np.concatenate(
        [[0, func(a, mu, sigma)], ys2, [func(b, mu, sigma), 0]])
    return xs2, ys2

a, b = -1, 1
mu = 0
sigma = 1
xs = np.linspace(-5, 5, 100)
ys = func(xs, mu=mu, sigma=sigma)


p = figure(x_range=(-5, 5), y_range=(-0.05, 0.5))
source = ColumnDataSource(data=dict(xs=xs, ys=ys))
p.line('xs', 'ys', source=source)

ab_slider = RangeSlider(title='a_b', value=[a, b],
                        start=-5, end=5, step=0.1)
mu_slider = Slider(title="mu", value=0,
                   start=-5.0, end=5.0, step=0.1)
sigma_slider = Slider(title="sigma", value=b,
                      start=0.1, end=5.0, step=0.1)
info = Div(text='integral value= {}'.format(
    integrate.quad(lambda x: func(x, mu, sigma), a, b)[0]))


labels_source = ColumnDataSource(
    data=dict(xs=[a, b], ys=[0, 0], names=['a', 'b']))
labels = LabelSet(x='xs', y='ys', text='names', level='glyph',
                  x_offset=-3, y_offset=-15, source=labels_source,
                  render_mode='canvas')
p.add_layout(labels)

xs2, ys2 = get_patches(a, b, xs, mu, sigma)
patches_source = ColumnDataSource(data=dict(xs=[xs2], ys=[ys2]))
p.patches('xs', 'ys', fill_color='blue', alpha=0.5, source=patches_source)
output_file('brewer.html', title='brewer.py example')


def update(attr, old, new):
    a, b = ab_slider.value
    mu = mu_slider.value
    sigma = sigma_slider.value
    ys = func(xs, mu, sigma)
    xs2, ys2 = get_patches(a, b, xs, mu, sigma)
    source.data.update(dict(xs=xs, ys=ys))
    labels_source.data.update(dict(xs=[a, b]))
    patches_source.data.update(dict(xs=[xs2], ys=[ys2]))
    info.text = 'integral value= {}'.format(
        integrate.quad(lambda x: func(x, mu, sigma), a, b)[0])

ws = [ab_slider, mu_slider, sigma_slider]
for w in ws:
    w.on_change('value', update)
w = widgetbox(*ws, info)
root = row([w, p])

document = curdoc()
document.add_root(root)
